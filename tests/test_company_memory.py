"""HTTP contract tests use synthetic fixtures, never a configured memory service."""
import json
import os
import tempfile
from pathlib import Path
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import unittest

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / 'skills/cdb-company-memory/scripts/hindsight_documents.py'


class MemoryHTTP(unittest.TestCase):
    def setUp(self):
        self.calls = []
        self.document = {'id': 'fixture-1', 'bank_id': 'synthetic-fixture',
                         'original_text': '{"synthetic":true}', 'tags': [],
                         'document_metadata': {}}
        owner = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, format, *args):
                pass

            def do_POST(self):
                body = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
                owner.calls.append((self.command, self.path, body))
                item = body['items'][0]
                owner.document.update(id=item['document_id'], original_text=item['content'],
                                      tags=item['tags'], document_metadata=item['metadata'])
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'{"success":true}')

            def do_GET(self):
                owner.calls.append((self.command, self.path, self.headers.get('Authorization')))
                body = json.dumps(owner.document).encode()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(body)

        self.server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)
        self.base = 'http://127.0.0.1:' + str(self.server.server_port)

    def cli(self, *args):
        return subprocess.run([sys.executable, str(HELPER), '--url', self.base, *args],
                              env={**os.environ, 'HINDSIGHT_API_KEY': 'synthetic-test-key'},
                              capture_output=True, text=True)

    def test_get_exact_document_uses_authorized_bank_and_document_route(self):
        result = self.cli('get', '--bank', 'synthetic-fixture', '--id', 'fixture-1')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), self.document)
        self.assertEqual(self.calls, [('GET', '/v1/default/banks/synthetic-fixture/documents/fixture-1',
                                      'Bearer synthetic-test-key')])


    def test_retain_rejects_missing_bank_and_invalid_item_before_network(self):
        with tempfile.TemporaryDirectory() as directory:
            payload = Path(directory) / 'item.json'
            for item in ({}, {'document_id': 'fixture-1', 'content': 'x', 'tags': [],
                              'metadata': {}, 'update_mode': 'append'}):
                payload.write_text(json.dumps(item))
                result = self.cli('retain', '--bank', 'synthetic-fixture', '--item', str(payload))
                self.assertNotEqual(result.returncode, 0)
            result = self.cli('retain', '--item', str(payload))
            self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.calls, [])

    def test_verify_detects_text_tags_metadata_and_identity_mismatch(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location('documents', HELPER)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        item = {'document_id': 'fixture-1', 'content': '{"synthetic":true}', 'tags': [], 'metadata': {}}
        for key, value in [('id', 'wrong'), ('bank_id', 'wrong'), ('original_text', None),
                           ('tags', ['wrong']), ('document_metadata', {'wrong': 'value'})]:
            with self.subTest(key=key), self.assertRaises(ValueError):
                module.verify({**self.document, key: value}, 'synthetic-fixture', item)

    def test_lock_excludes_second_process_and_recovers_after_kill(self):
        with tempfile.TemporaryDirectory() as directory:
            lock = Path(directory) / 'writer.lock'
            command = [sys.executable, str(HELPER), 'lock', '--path', str(lock), '--',
                       sys.executable, '-c', 'import time; print("ready", flush=True); time.sleep(60)']
            child = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, start_new_session=True)
            try:
                assert child.stdout is not None
                self.assertEqual(child.stdout.readline().strip(), 'ready')
                blocked = subprocess.run([sys.executable, str(HELPER), 'lock', '--path', str(lock), '--',
                                          sys.executable, '-c', 'print("unexpected")'], capture_output=True, text=True)
                self.assertNotEqual(blocked.returncode, 0)
                self.assertNotIn('unexpected', blocked.stdout)
            finally:
                # Kill lock runner and its command together, like an interrupted local run.
                import signal
                os.killpg(child.pid, signal.SIGKILL) if child.poll() is None else None
                child.communicate()
            recovered = subprocess.run([sys.executable, str(HELPER), 'lock', '--path', str(lock), '--',
                                        sys.executable, '-c', 'print("recovered")'], capture_output=True, text=True)
            self.assertEqual(recovered.returncode, 0, recovered.stderr)
            self.assertEqual(recovered.stdout.strip(), 'recovered')

    def test_verify_command_reads_without_mutating(self):
        with tempfile.TemporaryDirectory() as directory:
            payload = Path(directory) / 'item.json'
            payload.write_text(json.dumps({'document_id': 'fixture-1', 'content': '{"synthetic":true}',
                                           'tags': [], 'metadata': {}, 'update_mode': 'replace'}))
            result = self.cli('verify', '--bank', 'synthetic-fixture', '--item', str(payload))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout)['verified'])
        self.assertEqual([c[0] for c in self.calls], ['GET'])

    def test_empty_bank_is_rejected_before_network(self):
        result = self.cli('get', '--bank', '', '--id', 'fixture-1')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.calls, [])

    def test_url_policy_rejects_remote_plaintext_and_credentials(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location('documents', HELPER)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for url in ('http://remote.invalid', 'https://user:secret@remote.invalid',
                    'https://remote.invalid?key=value', 'file:///missing'):
            with self.subTest(url=url), self.assertRaises(ValueError):
                module.request(url, 'synthetic-fixture', 'GET', '/documents/fixture')

    def test_retain_single_item_verifies_exact_text_tags_metadata_and_identity(self):
        with tempfile.TemporaryDirectory() as directory:
            payload = Path(directory) / 'item.json'
            item = {'document_id': 'fixture-1', 'content': 'synthetic evidence',
                    'timestamp': '2026-01-01T00:00:00Z', 'tags': ['synthetic'],
                    'metadata': {'source': 'fixture'}, 'update_mode': 'replace'}
            payload.write_text(json.dumps(item))
            result = self.cli('retain', '--bank', 'synthetic-fixture', '--item', str(payload))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout)['verified'])
        self.assertEqual(self.calls[0][2], {'async': False, 'items': [item]})
        self.assertEqual([call[0] for call in self.calls], ['POST', 'GET'])


if __name__ == '__main__':
    unittest.main()

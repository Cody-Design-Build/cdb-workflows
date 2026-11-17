#!/usr/bin/env python3
"""Small exact-document client for Hindsight 1.2.1; no business integrations."""
import argparse
import json
import os
import sys
from urllib.parse import quote, urlsplit
from urllib.request import Request, build_opener, HTTPRedirectHandler


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError('Redirect refused; check service URL')


def request(url, bank, method, suffix, payload=None):
    parsed = urlsplit(url)
    if parsed.scheme not in ('http', 'https') or not parsed.netloc or parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise ValueError('Expected HTTP(S) service URL without credentials/query/fragment')
    if parsed.scheme == 'http' and parsed.hostname not in ('127.0.0.1', 'localhost', '::1'):
        raise ValueError('Remote connections require HTTPS')
    key = os.environ.get('HINDSIGHT_API_KEY')
    if not key:
        raise ValueError('HINDSIGHT_API_KEY must be supplied by private environment')
    endpoint = url.rstrip('/') + '/v1/default/banks/' + quote(bank, safe='') + suffix
    req = Request(endpoint, method=method,
                  data=None if payload is None else json.dumps(payload).encode(),
                  headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'})
    with build_opener(NoRedirect).open(req, timeout=90) as response:
        return json.load(response)


def verify(document, bank, item):
    if (document.get('id') != item['document_id'] or document.get('bank_id') != bank
            or document.get('original_text') != item['content']
            or set(document.get('tags', [])) != set(item['tags'])
            or document.get('document_metadata') != item['metadata']):
        raise ValueError('Exact document verification failed')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url')
    commands = parser.add_subparsers(dest='command', required=True)
    lock = commands.add_parser('lock', help='POSIX cooperative lock held for lifetime of command')
    lock.add_argument('--path', required=True)
    lock.add_argument('argv', nargs=argparse.REMAINDER)
    get = commands.add_parser('get')
    get.add_argument('--bank', required=True)
    get.add_argument('--id', required=True)
    for name in ('retain', 'verify'):
        item_command = commands.add_parser(name)
        item_command.add_argument('--bank', required=True)
        item_command.add_argument('--item', required=True, help='Private JSON file containing one MemoryItem')
    args = parser.parse_args()
    if args.command == 'lock':
        import fcntl
        argv = args.argv[1:] if args.argv[:1] == ['--'] else args.argv
        if not argv:
            parser.error('lock requires a foreground command after --')
        fd = os.open(args.path, os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW, 0o600)
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        os.set_inheritable(fd, True)
        # Replace the runner: no surviving child can outlive a dead lock parent.
        os.execvp(argv[0], argv)
    if not args.url:
        parser.error('--url is required for document operations')
    if not args.bank or args.bank != args.bank.strip():
        parser.error('Explicit nonempty bank required; whitespace is not normalized')
    if args.command == 'get':
        result = request(args.url, args.bank, 'GET', '/documents/' + quote(args.id, safe=''))
    else:
        with open(args.item) as source:
            item = json.load(source)
        required = {'document_id': str, 'content': str, 'tags': list, 'metadata': dict}
        if not isinstance(item, dict) or any(not isinstance(item.get(k), t) for k, t in required.items()):
            raise ValueError('Item requires document_id/content/tags/metadata')
        if (not item['document_id'] or not item['content'] or item.get('update_mode') != 'replace'
                or any(not isinstance(t, str) for t in item['tags'])
                or any(not isinstance(k, str) or not isinstance(v, str) for k, v in item['metadata'].items())):
            raise ValueError('Expected nonempty ID/text, string tags/metadata and explicit replace')
        if args.command == 'retain':
            response = request(args.url, args.bank, 'POST', '/memories', {'async': False, 'items': [item]})
            if response.get('success') is not True:
                raise ValueError('Retain unsuccessful; reconcile before retry')
        document = request(args.url, args.bank, 'GET', '/documents/' + quote(item['document_id'], safe=''))
        verify(document, args.bank, item)
        result = {'verified': True, 'id': item['document_id'], 'bank_id': args.bank}
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        # Do not echo response bodies, payloads, credentials or record content on error.
        print('Document operation failed: ' + type(exc).__name__, file=sys.stderr)
        sys.exit(1)

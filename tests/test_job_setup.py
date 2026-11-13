"""Offline acceptance checks for the CDB setup procedure and installation."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
NAME = 'jobtread-job-setup'


class JobSetup(unittest.TestCase):
    def test_procedure_preserves_intake_and_completion_gates(self):
        text = (ROOT / 'skills' / NAME / 'SKILL.md').read_text()
        for phrase in ['all known owners', 'primary contact', 'email', 'phone',
                       'address - short scope', 'length constraint', 'timed-out',
                       'Notifications', 'plan sheets', 'original bytes', 'Dropbox',
                       'reconcile uncertain writes', 'Return four concise sections']:
            self.assertIn(phrase.lower(), text.lower())
        self.assertNotIn('697 Rhode', text)
        self.assertNotIn('edward.s.hsu', text)

    def test_general_skill_requires_setup_procedure(self):
        text = (ROOT / 'skills/jobtread/SKILL.md').read_text()
        self.assertIn('../jobtread-job-setup/SKILL.md', text)
        self.assertIn('must follow', text)

    def test_new_skill_installs_for_shared_and_hermes_idempotently(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            command = [sys.executable, str(ROOT / 'scripts/install.py'), '--agents', 'shared', 'hermes']
            for _ in range(2):
                result = subprocess.run(command, env={**os.environ, 'HOME':tmp}, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                for directory in ['.agents/skills', '.hermes/skills/productivity']:
                    self.assertEqual((home / directory / NAME).resolve(), ROOT / 'skills' / NAME)
            self.assertFalse((home / '.config/jobtread').exists())


if __name__ == '__main__':
    unittest.main()

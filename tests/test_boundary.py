"""Public source boundary, independent mail/file installs and final send gate."""
import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
PRIVATE = {'cdb-operations', 'cdb-company-memory', 'cdb-task-management', 'cdb-surface-orders', 'email-inbox-triage', 'grilling', 'grill-with-docs', 'domain-modeling'}

class Boundary(unittest.TestCase):
    def test_public_inventory_has_ten_modules_and_no_operations_source(self):
        spec = importlib.util.spec_from_file_location('installer', ROOT/'scripts/install.py')
        assert spec is not None and spec.loader is not None
        installer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(installer)
        self.assertEqual(len(installer.SKILLS), 10)
        self.assertEqual(set(installer.SKILLS), {p.name for p in (ROOT/'skills').iterdir() if p.is_dir()})
        self.assertFalse(PRIVATE & set(installer.SKILLS))
        for name in PRIVATE:
            self.assertFalse((ROOT/'skills'/name).exists())
        for name in ('OPERATIONS-DESIGN.md', 'OPERATIONS-ACTIVATION.md', 'OPERATIONS-VALIDATION.md', 'HINDSIGHT-REVIEW.md'):
            self.assertFalse((ROOT/'docs'/name).exists())

    def test_mail_and_dropbox_select_independently_without_jobtread(self):
        for module in ('business-email', 'cdb-dropbox-management'):
            with self.subTest(module=module), tempfile.TemporaryDirectory() as tmp:
                result = subprocess.run([sys.executable, str(ROOT/'scripts/install.py'), '--modules', module], env={**os.environ, 'HOME': tmp}, text=True, capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual({p.name for p in (Path(tmp)/'.agents/skills').iterdir()}, {module})
                self.assertEqual({p.name for p in Path(tmp).iterdir()}, {'.agents'})

    def test_email_has_separate_final_send_approval_and_unsent_draft(self):
        text = (ROOT/'skills/business-email/SKILL.md').read_text()
        for phrase in ('own authorized mailbox', 'UNSENT', 'separate explicit confirmation', 'Any change invalidates', 'SENT status', 'uncertain', 'Do not invent'):
            self.assertIn(phrase.lower(), text.lower())
        self.assertNotRegex(text, r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}')
        self.assertNotIn('/home/', text)

if __name__ == '__main__':
    unittest.main()

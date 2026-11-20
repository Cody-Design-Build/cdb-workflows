"""Offline Dropbox workflow, linking and installer acceptance checks."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
NAME = 'cdb-dropbox-management'

class DropboxWorkflow(unittest.TestCase):
    def test_filing_and_safety_policy(self):
        text = (ROOT / 'skills' / NAME / 'SKILL.md').read_text()
        for phrase in ['01 - customer orders','02 - vendor orders','03 - plans & design',
                       '04 - procurement','05 - trade partners','06 - permits & compliance',
                       'all job stages','original bytes','no-overwrite','Ask before',
                       'cloud sync unconfirmed','JobTread status','share URL']:
            self.assertIn(phrase, text)
        self.assertNotIn('/home/', text)
        self.assertNotRegex(text, r'\b\d{3,}\s+[A-Z][a-z]+\s+(?:Street|St|Avenue|Ave|Road|Rd)\b')

    def test_setup_links_to_filing_owner(self):
        text = (ROOT / 'skills/cdb-dropbox-management/SKILL.md').read_text()
        self.assertIn('../jobtread-job-setup/SKILL.md', text)
        self.assertTrue((ROOT / 'skills/jobtread-job-setup').exists())

    def test_installer_exposes_dropbox_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run([sys.executable,str(ROOT/'scripts/install.py'),'--agents','shared','hermes'],
                env={**os.environ,'HOME':tmp}, capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            for rel in ['.agents/skills','.hermes/skills/productivity']:
                self.assertEqual((Path(tmp)/rel/NAME).resolve(),ROOT/'skills'/NAME)

if __name__ == '__main__':
    unittest.main()

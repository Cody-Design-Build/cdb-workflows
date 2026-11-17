"""Offline publication and discovery contracts for migrated CDB modules."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
MIGRATED = ('email-inbox-triage', 'cdb-surface-orders')
MODULES = (*MIGRATED, 'cdb-dropbox-management')


class MigratedSkills(unittest.TestCase):
    def test_publication_records_provenance_without_private_evidence(self):
        provenance = ROOT / 'docs/MIGRATED-SKILLS.md'
        self.assertTrue(provenance.is_file())
        notices = provenance.read_text()
        for value in ['Ben Barclay (benbarclay)', 'David Cody', 'MIT', *MIGRATED]:
            self.assertIn(value, notices)
        for name in MODULES:
            for path in (ROOT / 'skills' / name).rglob('*'):
                if not path.is_file():
                    continue
                self.assertEqual(path.suffix, '.md', str(path))
                text = path.read_text()
                self.assertNotRegex(text, r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}')
                self.assertNotRegex(text, r'/(?:home|Users)/[^/\s]+/')
                self.assertNotRegex(text, r'\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f-]{23,}\b')
                self.assertNotRegex(text, r'\b\d{3,}\s+[A-Z][a-z]+\s+(?:Street|St|Avenue|Ave|Road|Rd)\b')

    def test_migrated_policies_keep_coverage_and_system_boundaries(self):
        email = (ROOT / 'skills/email-inbox-triage/SKILL.md').read_text()
        continuity = (ROOT / 'skills/email-inbox-triage/references/project-briefings.md').read_text()
        surface = (ROOT / 'skills/cdb-surface-orders/SKILL.md').read_text()
        for phrase in ['read-only', 'complete threads', 'existing drafts', 'read back', 'backlog']:
            self.assertIn(phrase, email)
        for phrase in ['48-hour overlap', '40 relevant complete threads', 'watermark',
                       '~/.local/share/cdb-email-triage/', 'legacy']:
            self.assertIn(phrase, continuity)
        for phrase in ['list_operations', 'baseRev', 'non-atomic', 'archive_record',
                       'parallel tracker', '../cdb-dropbox-management/SKILL.md']:
            self.assertIn(phrase, surface)

    def test_default_installs_all_modules_without_client_copies_or_configuration(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            command = [sys.executable, str(ROOT / 'scripts/install.py')]
            for _ in range(2):
                result = subprocess.run(command, env={**os.environ, 'HOME': tmp},
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                for name in MODULES:
                    path = home / '.agents/skills' / name
                    self.assertTrue(path.is_symlink(), name)
                    self.assertEqual(path.resolve(), ROOT / 'skills' / name)
            self.assertEqual({p.name for p in home.iterdir()}, {'.agents'})

    def test_explicit_legacy_hermes_uses_original_skill_names_and_categories(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/install.py'),
                                     '--agents', 'hermes'], env={**os.environ, 'HOME': tmp},
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            for category, name in [('email', MIGRATED[0]), ('productivity', MIGRATED[1])]:
                self.assertEqual((Path(tmp) / '.hermes/skills' / category / name).resolve(),
                                 ROOT / 'skills' / name)


if __name__ == '__main__':
    unittest.main()

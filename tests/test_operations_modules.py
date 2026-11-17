"""Public module contracts and shared-only installation, without business access."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
NAMES = ('cdb-company-memory', 'cdb-task-management', 'cdb-operations')


class OperationsModules(unittest.TestCase):
    def test_modules_document_independent_contracts_and_failure_boundaries(self):
        for name in NAMES:
            with self.subTest(name=name):
                text = (ROOT / 'skills' / name / 'SKILL.md').read_text()
                for section in ('## When to Use', '## Prerequisites', '## Procedure',
                                '## Contract and failure boundary', '## Pitfalls', '## Verification'):
                    self.assertIn(section, text)
                self.assertIn(name, (ROOT / 'README.md').read_text())

    def test_shared_installer_registers_all_three_without_hermes_links(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            for _ in range(2):
                result = subprocess.run([sys.executable, str(ROOT / 'scripts/install.py'), '--agents', 'shared'],
                                        env={**os.environ, 'HOME': directory}, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
            for name in NAMES:
                self.assertEqual((home / '.agents/skills' / name).resolve(), ROOT / 'skills' / name)
            self.assertFalse((home / '.hermes').exists())

    def test_existing_modules_defer_memory_to_owner_without_migrating_legacy_state(self):
        triage = (ROOT / 'skills/email-inbox-triage/references/project-briefings.md').read_text()
        surface = (ROOT / 'skills/cdb-surface-orders/SKILL.md').read_text()
        self.assertIn('cdb-company-memory', triage)
        self.assertIn('Preserve existing local checkpoints', triage)
        self.assertIn('Hindsight', surface)
        self.assertIn('concise local', surface)

    def test_operations_preserves_consequence_gates_and_real_dependencies(self):
        text = (ROOT / 'skills/cdb-operations/SKILL.md').read_text()
        for word in ('email-inbox-triage', 'cdb-surface-orders', 'jobtread', 'cdb-task-management',
                     'cdb-company-memory', 'one writer', 'read-only', 'Needs your decision',
                     'not-yet-automated', 'closure', 'cached/as-of'):
            self.assertIn(word, text)


if __name__ == '__main__':
    unittest.main()

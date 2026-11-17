"""Offline integrity checks for imported interview procedures."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class DesignInterview(unittest.TestCase):
    def test_entrypoint_loads_both_dependencies(self):
        text = (ROOT / 'skills/grill-with-docs/SKILL.md').read_text()
        for name in ['grilling', 'domain-modeling']:
            self.assertIn(name, text)
            self.assertTrue((ROOT / 'skills' / name / 'SKILL.md').is_file())
        self.assertNotIn('Call the Skill tool', text)

    def test_upstream_attribution_and_license_preserved(self):
        for name in ['grill-with-docs', 'grilling', 'domain-modeling']:
            folder = ROOT / 'skills' / name
            self.assertIn('5863806dd4e15c63174bee4e7515a4256792ecfa', (folder / 'SKILL.md').read_text())
            self.assertIn('Copyright (c) 2026 Matt Pocock', (folder / 'LICENSE').read_text())

    def test_document_templates_and_interview_gate(self):
        folder = ROOT / 'skills/domain-modeling'
        for name in ['ADR-FORMAT.md', 'GLOSSARY-FORMAT.md']:
            self.assertTrue((folder / name).is_file())
        text = (ROOT / 'skills/grilling/SKILL.md').read_text()
        self.assertIn('prerequisites', text)
        self.assertIn('Do not act on it until the user confirms', text)


if __name__ == '__main__':
    unittest.main()

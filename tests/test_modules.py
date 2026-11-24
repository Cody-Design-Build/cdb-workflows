"""Offline contracts for modular installation, policy ownership and safe updates."""
import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Modules(unittest.TestCase):
    def test_all_eight_modules_have_operating_dependency_and_verification(self):
        installer = load_script('install')
        self.assertEqual(len([n for n in installer.SKILLS if n.startswith("jobtread")]), 8)
        for name in (n for n in installer.SKILLS if n.startswith("jobtread")):
            text = (ROOT / 'skills' / name / 'SKILL.md').read_text()
            self.assertIn('## Verification', text)
            if name != 'jobtread':
                self.assertIn('../jobtread/SKILL.md', text)
            front = text.split('---', 2)[1]
            description = next(line.split(': ', 1)[1] for line in front.splitlines() if line.startswith('description:'))
            self.assertLessEqual(len(description), 60)
            self.assertTrue(description.endswith('.'))
            self.assertIn('platforms:', front)

    def test_core_has_resumable_workflow_and_partial_failure_contract(self):
        text = (ROOT / 'skills/jobtread/SKILL.md').read_text()
        for phrase in ['## Workflow checkpoints and recovery',
                       'verified record IDs', 'completed, blocked and not attempted',
                       'do not replay the whole batch', 'notification state']:
            self.assertIn(phrase, text)

    def test_selective_install_includes_core_and_required_not_unrelated_modules(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            cmd = [sys.executable, str(ROOT / 'scripts/install.py'), '--modules', 'jobtread-estimating', '--agents', 'shared', 'codex']
            for _ in range(2):
                p = subprocess.run(cmd, env={**os.environ, 'HOME':tmp}, capture_output=True, text=True)
                self.assertEqual(p.returncode, 0, p.stderr)
            for folder in ['.agents/skills', '.codex/skills']:
                self.assertEqual({p.name for p in (home/folder).iterdir()}, {'jobtread', 'jobtread-estimating', 'jobtread-budget-writing'})
                for link in (home/folder).iterdir():
                    self.assertEqual(link.resolve(), ROOT/'skills'/link.name)
            self.assertEqual({p.name for p in home.iterdir()}, {'.agents', '.codex'})

    def test_management_dependencies_and_optional_dropbox_boundary(self):
        installer = load_script('install')
        modules = installer.selected_modules(['jobtread-job-management'])
        self.assertTrue({'jobtread', 'jobtread-job-setup', 'jobtread-scheduling', 'jobtread-daily-logs', 'jobtread-budget-writing'} <= set(modules))
        setup = (ROOT/'skills/jobtread-job-setup/SKILL.md').read_text()
        self.assertIn('optional `cdb-dropbox-management`', setup)
        self.assertTrue((ROOT/'skills/cdb-dropbox-management').exists())

    def test_daily_log_policy_has_one_owner_and_estimate_has_no_private_rate_table(self):
        ref = (ROOT/'skills/jobtread/references/schedule-daily-logs.md').read_text()
        self.assertNotIn('## Daily-log intake and discovery', ref)
        self.assertIn('../../jobtread-daily-logs/SKILL.md', ref)
        text = (ROOT/'skills/jobtread-estimating/SKILL.md').read_text()
        for phrase in ['Locked for estimating', 'same scope', 'decimal arithmetic', 'issued versions', 'read']:
            self.assertIn(phrase, text)
        self.assertNotRegex(text, r'\$\s*\d|\b\d+%')


class Updates(unittest.TestCase):
    def test_preflight_refuses_dirty_wrong_origin_detached_or_wrong_tracking(self):
        module = load_script('update')
        cases = [ [' M local.md'], ['', 'https://example.invalid/wrong.git'], ['', next(iter(module.ORIGINS)), ''], ['', next(iter(module.ORIGINS)), 'main', 'another/main'] ]
        for values in cases:
            with self.subTest(values=values), patch.object(module, 'git', side_effect=values):
                with self.assertRaises(ValueError): module.preflight()

    def test_check_only_does_not_merge(self):
        module = load_script('update')
        with patch.object(module, 'preflight'), patch.object(module, 'git', side_effect=['0 1', 'incoming', 'stat', 'abc']), patch.object(module.subprocess, 'run') as run, patch.object(sys, 'argv', ['update.py']):
            module.main()
            self.assertEqual(run.call_count, 1)
            self.assertEqual(run.call_args.args[0], ['git', 'fetch', 'origin', '--tags'])

    def test_apply_uses_fast_forward_only_and_rechecks(self):
        module = load_script('update')
        with patch.object(module, 'preflight') as pre, patch.object(module, 'git', side_effect=['0 1', 'incoming', 'stat', 'abc', 'def']), patch.object(module.subprocess, 'run') as run, patch.object(sys, 'argv', ['update.py','--apply']):
            module.main()
            self.assertEqual(pre.call_count, 2)
            self.assertEqual(run.call_args.args[0], ['git', 'merge', '--ff-only', 'origin/main'])

    def test_divergence_does_not_merge(self):
        module = load_script('update')
        with patch.object(module, 'preflight'), patch.object(module, 'git', return_value='1 1'), patch.object(module.subprocess, 'run') as run, patch.object(sys, 'argv', ['update.py','--apply']):
            with self.assertRaises(ValueError): module.main()
            self.assertEqual(run.call_count, 1)


if __name__ == '__main__':
    unittest.main()

"""Exercise conflict protection and shared discovery without touching a real profile."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/install.py"


class InstallSafety(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name)

    def run_install(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            env={**os.environ, "HOME": str(self.home)},
            text=True, capture_output=True,
        )

    def test_conflict_refuses_before_any_links_are_created(self):
        conflict = self.home / ".codex/skills/jobtread"
        conflict.mkdir(parents=True)
        (conflict / "local-notes").write_text("retain these notes")
        result = self.run_install("--agents", "codex")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((conflict / "local-notes").read_text(), "retain these notes")
        self.assertFalse((self.home / ".agents/skills/jobtread").exists())

    def test_migration_preserves_work_and_all_clients_read_canonical_skills(self):
        conflict = self.home / ".agents/skills/jobtread"
        conflict.mkdir(parents=True)
        (conflict / "local-notes").write_bytes(b"uncommitted work\x00")
        result = self.run_install("--agents", "shared", "hermes", "codex", "claude", "omp", "opencode", "--migrate")
        self.assertEqual(result.returncode, 0, result.stderr)
        saved = list((self.home / ".local/state/cdb-workflows/backups").glob("*/shared/jobtread/local-notes"))
        self.assertEqual([p.read_bytes() for p in saved], [b"uncommitted work\x00"])
        for relative in (".agents/skills", ".hermes/skills/productivity", ".codex/skills", ".claude/skills", ".omp/agent/skills", ".config/opencode/skills"):
            for name in ("jobtread", "jobtread-budget-writing"):
                self.assertEqual((self.home / relative / name).resolve(), ROOT / "skills" / name)
                self.assertEqual((self.home / relative / name / "SKILL.md").read_bytes(), (ROOT / "skills" / name / "SKILL.md").read_bytes())
        self.assertEqual((self.home / ".hermes/skills/jobtread-catalog-standards").resolve(), ROOT / "skills/jobtread-catalog-standards")
        again = self.run_install("--agents", "codex", "hermes")
        self.assertEqual(again.returncode, 0, again.stderr)
        self.assertEqual(len(list((self.home / ".local/state/cdb-workflows/backups").iterdir())), 1)

    def test_dangling_link_requires_migration_and_is_preserved(self):
        link = self.home / ".agents/skills/jobtread"
        link.parent.mkdir(parents=True)
        link.symlink_to("/missing/original-skill")
        self.assertNotEqual(self.run_install().returncode, 0)
        result = self.run_install("--migrate")
        self.assertEqual(result.returncode, 0, result.stderr)
        saved = list((self.home / ".local/state/cdb-workflows/backups").glob("*/shared/jobtread"))
        self.assertEqual(len(saved), 1)
        self.assertEqual(os.readlink(saved[0]), "/missing/original-skill")
        self.assertEqual(link.resolve(), ROOT / "skills/jobtread")


if __name__ == "__main__":
    unittest.main()

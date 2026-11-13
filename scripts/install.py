#!/usr/bin/env python3
"""Link this checkout into agent skill directories without overwriting local work."""
import argparse
from datetime import datetime, timezone
from pathlib import Path
import shutil
import sys

SKILLS = ("jobtread", "jobtread-budget-writing", "jobtread-catalog-standards", "jobtread-job-setup")
AGENTS = ("shared", "hermes", "codex", "claude", "omp", "opencode")


def destinations(home, agents):
    shared = home / ".agents/skills"
    for agent in dict.fromkeys(("shared", *agents)):
        for name in SKILLS:
            if agent == "shared":
                path = shared / name
            elif agent == "hermes":
                base = home / ".hermes/skills"
                path = base / name if name == "jobtread-catalog-standards" else base / "productivity" / name
            else:
                base = {
                    "codex": home / ".codex/skills",
                    "claude": home / ".claude/skills",
                    "omp": home / ".omp/agent/skills",
                    "opencode": home / ".config/opencode/skills",
                }[agent]
                path = base / name
            target = ROOT / "skills" / name if agent == "shared" else shared / name
            yield agent, path, target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agents", nargs="+", choices=AGENTS, default=["shared"])
    parser.add_argument("--migrate", action="store_true", help="Back up conflicting destinations before linking")
    args = parser.parse_args()
    for name in SKILLS:
        if not (ROOT / "skills" / name / "SKILL.md").is_file():
            parser.error(f"Incomplete checkout: missing skill {name}")
    plans = []
    for agent, path, target in destinations(Path.home(), args.agents):
        if path.is_symlink() and path.resolve() == target.resolve():
            print(f"Already linked: {path}")
            continue
        occupied = path.exists() or path.is_symlink()
        if occupied and not args.migrate:
            parser.error(f"Refusing to replace {path}; inspect it, then use --migrate to preserve a backup")
        plans.append((agent, path, target, occupied))
    backup = Path.home() / ".local/state/jobtread-skills/backups" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    for agent, path, target, occupied in plans:
        if occupied:
            saved = backup / agent / path.name
            saved.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(path), str(saved))
            print(f"Preserved: {saved}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.symlink_to(target, target_is_directory=True)
        print(f"Linked: {path} -> {target}")
    print("Skills installed. Restart/reload agents; configure MCP separately using docs/CONNECTING.md.")


ROOT = Path(__file__).resolve().parents[1]
if __name__ == "__main__":
    try:
        main()
    except OSError as exc:
        print(f"Installation failed: {exc}", file=sys.stderr)
        sys.exit(1)

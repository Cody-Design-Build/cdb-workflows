#!/usr/bin/env python3
"""Check distributable skill structure, JSON examples, links and credential hazards."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
patterns = {
    "private key": r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    "GitHub credential": r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,})\b",
    "Google token": r"\bya29\.[A-Za-z0-9_-]{20,}",
    "JWT": r"\beyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\b",
    "workstation path": r"/(?:home/ductape|Users/davidcody)(?:/|\b)",
    "historical OAuth grant": r"Access for 127\.0\.0\.1:\d+",
}


def fail(path, message):
    errors.append(f"{path.relative_to(ROOT)}: {message}")


files = [p for p in ROOT.rglob("*") if not any(part in {".git", "__pycache__", ".venv"} for part in p.relative_to(ROOT).parts)]
for path in files:
    if path.is_symlink():
        fail(path, "symlinks do not belong in the published checkout")
        continue
    if not path.is_file():
        continue
    if path.name in {"auth.json", ".env", "local-access-token", "client_secret.json", "oauth-store.key"} or path.suffix in {".sqlite", ".db", ".pdf", ".log"}:
        fail(path, "credential/runtime/business-evidence filename is not distributable")
    text = path.read_text()
    # Scan publication material, not the validator's own detection expressions.
    if path.suffix in {".md", ".json", ".yml", ".yaml"}:
        for label, pattern in patterns.items():
            if re.search(pattern, text):
                fail(path, label)
    if path.suffix == ".json":
        try:
            json.loads(text)
        except ValueError as exc:
            fail(path, f"invalid JSON: {exc}")
    if path.suffix != ".md":
        continue
    for example in re.findall(r"^```json\s*\n(.*?)^```", text, re.M | re.S):
        try:
            json.loads(example)
        except ValueError as exc:
            fail(path, f"invalid JSON example: {exc}")
    for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", link) or link.startswith("#"):
            continue
        target = link.split("#", 1)[0]
        if target and not (path.parent / target).exists():
            fail(path, f"missing relative link: {link}")
    if path.name == "SKILL.md":
        if not text.startswith("---\n") or "\n---\n" not in text[4:]:
            fail(path, "missing YAML frontmatter")
            continue
        front = text.split("---", 2)[1]
        name = re.search(r"^name:\s*(.+)$", front, re.M)
        description = re.search(r"^description:\s*(.+)$", front, re.M)
        if not name or name.group(1).strip() != path.parent.name:
            fail(path, "skill name must match its directory")
        if not description or len(description.group(1).strip()) > 1024:
            fail(path, "missing or oversized description")
        if name and (not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name.group(1).strip()) or len(name.group(1).strip()) > 64):
            fail(path, "invalid skill name")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"Validated {sum(p.is_file() for p in files)} files: skill metadata, JSON examples, links and credential-pattern checks.")
print("Pattern checks do not establish exhaustive privacy or runtime workflow correctness.")

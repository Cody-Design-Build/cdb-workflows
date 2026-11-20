#!/usr/bin/env python3
"""Check for updates; apply only explicitly to clean, correctly tracked main."""
import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ORIGINS = {
    'https://github.com/Cody-Design-Build/cdb-workflows.git',
    'https://github.com/Cody-Design-Build/cdb-workflows',
    'git@github.com:Cody-Design-Build/cdb-workflows.git',
}


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()


def preflight():
    if git('status', '--porcelain'):
        raise ValueError('Dirty checkout: preserve/reconcile tracked and untracked work first')
    if git('remote', 'get-url', 'origin') not in ORIGINS:
        raise ValueError('Unexpected origin; inspect repository identity before updating')
    if git('branch', '--show-current') != 'main':
        raise ValueError('Only tracking main can update; pinned/detached checkouts require deliberate review')
    if git('rev-parse', '--abbrev-ref', '@{upstream}') != 'origin/main':
        raise ValueError('Expected upstream origin/main')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Explicitly apply the reviewed fast-forward update')
    args = parser.parse_args()
    preflight()
    subprocess.run(['git', 'fetch', 'origin', '--tags'], cwd=ROOT, check=True)
    behind, ahead = map(int, git('rev-list', '--left-right', '--count', 'HEAD...origin/main').split())
    # Left side is local-only; do not rewrite or merge it.
    if behind:
        raise ValueError('Local commits or divergence: reconcile manually; no automatic merge/reset')
    print(git('log', '--oneline', 'HEAD..origin/main') or 'Already current')
    print(git('diff', '--stat', 'HEAD..origin/main'))
    print(f'Incoming commits: {ahead}; installed commit: {git("rev-parse", "HEAD")}')
    if args.apply:
        preflight()
        subprocess.run(['git', 'merge', '--ff-only', 'origin/main'], cwd=ROOT, check=True)
        print('Updated commit:', git('rev-parse', 'HEAD'))
        print('Run validation/tests and refresh your existing module/client links; OAuth is unchanged.')
    else:
        print('Check only. Review incoming changes before explicitly requesting --apply.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(f'Update stopped: {exc}', file=sys.stderr)
        sys.exit(1)

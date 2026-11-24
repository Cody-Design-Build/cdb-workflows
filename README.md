# CDB workflows

Public CDB procedures for JobTread, estimating, Dropbox and lightweight business Gmail/mail. No GitHub account is needed to download them; each person authorizes their own business accounts. This is CDB policy, not an official vendor product.

## Start here — ask your assistant

> Install https://github.com/Cody-Design-Build/cdb-workflows into ~/Work/cdb-workflows. Read README.md, MAINTAINER.md and docs/MAINTAINING.md. Preserve existing changes and stop for conflicts. Run offline validation/tests and install shared discovery, adding only my actual client. Help me connect my own accounts separately, verify discovery and a harmless read without business changes. Report the installed commit, modules and checks.

## Modules

- `jobtread`: operating safety, discovery, connection and documents
- `jobtread-job-setup`: owners, property, job, plans and Dropbox reconciliation
- `jobtread-job-management`: coordination and closeout
- `jobtread-budget-writing`: CDB scope language and allowances
- `jobtread-estimating`: approved scope baseline and traceable pricing
- `jobtread-scheduling`: whole-week schedules
- `jobtread-daily-logs`: factual site reports and corrections
- `jobtread-catalog-standards`: reusable scope catalog
- `cdb-dropbox-management`: folder/file/revision safety and cloud verification
- `business-email`: own-mailbox search, unsent drafts and final send approval

Operations, company memory, task orchestration, Surface, heavy inbox triage, checkpoints/reports and runtime services are **not distributed**. Their local source is separate, including generic interview dependencies with licenses preserved. Previously published generic operations remain in Git history; no history rewrite is implied.

## Install

Git and Python 3.10+ are required:

```sh
git clone https://github.com/Cody-Design-Build/cdb-workflows.git ~/Work/cdb-workflows
cd ~/Work/cdb-workflows
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/install.py
```

Keep the checkout: discovery links depend on it. Defaults link all ten modules into `~/.agents/skills`. Choose modules/clients explicitly:

```sh
python3 scripts/install.py --modules jobtread-estimating --agents shared codex
python3 scripts/install.py --agents shared claude omp opencode
```

Selecting JobTread modules includes core and required dependencies. Dropbox/email work independently. Conflicts are refused before any links change. Inspect first, then opt into `--migrate` to preserve backups under `~/.local/state/cdb-workflows/backups/`. Hermes scanning shared discovery needs no local copy; `--agents hermes` is an explicit legacy option. No profile configuration is edited.

## Connect separately

Follow [JobTread](docs/CONNECTING.md) and [Google Workspace](docs/GOOGLE-WORKSPACE.md). Discover Dropbox through an approved connector or verified local sync. Installation grants no permissions or credentials. Drafting does not authorize sending, notifying, issuing or paying.

Hosted assistants require reviewed Markdown skills and linked references through supported project attachments/instructions; local links do not reach them. A URL alone does not install skills. Track the adopted commit and refresh attachments deliberately.

## Update deliberately

> Check my cdb-workflows installation for updates. Preserve tracked/untracked work, verify repository identity and tracking, fetch and summarize incoming changes. Do not apply yet or schedule updates.

```sh
python3 scripts/update.py
# After review and explicit request:
python3 scripts/update.py --apply
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The updater refuses dirty, wrong-origin, detached, incorrectly tracked or divergent checkouts and only fast-forwards main. Refresh existing selected links after updating. No automatic updates, credential changes or service deployment. Pin exact commits or verified existing releases when needed.

## Maintenance and limits

Read [MAINTAINER.md](MAINTAINER.md), [maintenance](docs/MAINTAINING.md), [provenance](docs/PROVENANCE.md), [validation](docs/VALIDATION.md) and [changelog](CHANGELOG.md). The short-lived jobtread-skills package is retired; maintain JobTread only here. Its complete eight-module feature set is preserved and extended here; see the [parity and migration record](docs/JOBTREAD-MIGRATION.md). Do not install or update from the old repository.

Linux offline checks do not establish live OAuth, every client/version or business workflow correctness. Windows/macOS runtime is untested here; Windows symlinks may require Developer Mode. Original CDB source is [MIT](LICENSE); upstream schemas/trademarks retain their terms. Never publish private records, rates, identities, credentials, evidence or machine state.

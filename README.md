# CDB JobTread workflow skills

A public library of Cody Design Build (CDB) operating policies for AI assistants working with JobTread. Install the instructions into your assistant’s filesystem, then connect that assistant to JobTread separately through its official Model Context Protocol (MCP) endpoint.

These are CDB-specific workflows, not generic JobTread defaults or an official JobTread product. Public policy belongs here; customer records, credentials, authorization history, and machine configuration do not.

## Choose a skill

| Skill | Purpose |
| --- | --- |
| `jobtread` | Connection discovery, permissions, safe operations, verification, and vendor order/bill/payment workflows |
| `jobtread-budget-writing` | CDB budget names, customer-facing scope, allowances, inclusions, exclusions, and group descriptions |
| `jobtread-catalog-standards` | CDB reusable catalog scope, naming and catalog-rebuild approval rules |

Keep these skills together: writing and catalog rules depend on the operating skill’s discovery and business-safety rules.

## Install the instructions

You need Git, Python 3, and a filesystem-based skills client. Clone into a location you intend to keep:

```sh
mkdir -p ~/Work
git clone https://github.com/Cody-Design-Build/jobtread-skills.git \
  ~/Work/jobtread-skills
cd ~/Work/jobtread-skills
python3 scripts/install.py
```

The default installs shared discovery links under `~/.agents/skills`. It does not authorize JobTread, install a gateway, create credentials, or write MCP connection settings. Restart your assistant or reload its skill discovery after installation.

Select discovery targets with `--agents`; it accepts a space-separated list:

```sh
python3 scripts/install.py --agents shared hermes codex claude omp opencode
```

Choose only the clients you use; the installer always installs the shared discovery hub first. Read `python3 scripts/install.py --help` before changing an existing installation. Keep the clone available because the installed skills link to it.

The installer refuses conflicting directories or links by default. Inspect and reconcile existing contents before opting into migration:

```sh
python3 scripts/install.py --agents shared hermes codex claude omp opencode \
  --migrate
```

Migration backs up conflicts under `~/.local/state/jobtread-skills/backups/`, grouped by timestamp, agent, and skill. Re-running against the same source links is idempotent. See [maintenance guidance](docs/MAINTAINING.md#install-reviewed-edits-without-losing-local-work) before removing backups.

## Connect your assistant

Follow [Connect an assistant to JobTread](docs/CONNECTING.md) for configuration formats checked against upstream documentation for Codex, Claude Code, Hermes, OpenCode, and omp. Prefer direct OAuth authorization at `https://api.jobtread.com/mcp`, using your own JobTread account and browser consent.

Installing skills and configuring tools are separate actions. This repository does not import skills into JobTread itself, grant account permissions, or authorize business changes. A visible mutation-capable tool does not prove your grant permits mutations.

For ChatGPT or Claude in a browser, see [hosted assistant setup](docs/CONNECTING.md#use-a-hosted-chatgpt-or-claude-assistant). Supply a reviewed release's Markdown procedures through supported project instructions/attachments; local filesystem links do not reach hosted sessions.

## Update deliberately

For consumers, pin a reviewed published release or exact commit. Do not assume a release tag exists before checking the repository’s published releases. To pin an available tag, replace `reviewed_release_tag` below:

```sh
git fetch --tags
git checkout --detach reviewed_release_tag
python3 scripts/install.py
```

For a clone tracking its existing branch, inspect incoming changes before updating:

```sh
cd ~/Work/jobtread-skills
git status --short
git fetch origin
git log --oneline HEAD..@{upstream}
git diff HEAD..@{upstream} -- skills scripts docs AGENTS.md README.md
git pull --ff-only
python3 scripts/install.py
```

Stop if local changes or incoming policy changes need reconciliation. These commands never push. There is no automatic pull, push, background updater, or business-record synchronization.

## Understand the limits

The library documents CDB policy and schema-led operating procedures. Captured upstream schemas are reference snapshots, not live capability or permission guarantees. Client configuration examples follow linked upstream documentation; they are not a claim that every client or complete business workflow has been runtime-tested.

Before using a connection, complete the read-only verification checklist in [CONNECTING.md](docs/CONNECTING.md#verify-the-connection-without-changing-records). Never create, send, pay, or delete a real record to test setup.

[Initial rollout verification](docs/VALIDATION.md) records the checks actually performed and their limits.

## Maintain or reuse this library

[AGENTS.md](AGENTS.md) is the canonical repository policy for maintaining all JobTread instructions here. [Maintaining the library](docs/MAINTAINING.md) covers review, provenance, releases, and privacy. Record user-visible changes in [CHANGELOG.md](CHANGELOG.md).

Original authored material uses the [MIT license](LICENSE). Upstream JobTread tool descriptions, schemas, documentation, and trademarks retain their respective ownership and terms. Preserve source attribution; the repository’s MIT license does not relicense upstream material.

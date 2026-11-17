# Maintain and release the workflow library

Maintain CDB company workflows and their modular procedures/integrations in this repository, review public/private boundaries, and release only the evidence you can support. [AGENTS.md](../AGENTS.md) owns repository policy; this guide covers the maintenance procedure.

## Change the canonical source

Work in `~/Work/cdb-workflows`, not an independent copy inside an agent profile. Keep rules in their owning skill and use relative references between repository files. Preserve the CDB-specific operating intent when making instructions portable.

Before changing a procedure:

1. Read the owning skill and its linked references.
2. Identify whether the change is CDB policy, an upstream API change, client configuration, or a machine-only setting.
3. Confirm policy changes with the owner. Do not infer new business permissions from a schema or an existing full-access grant.
4. Edit the source here, remove obsolete instructions/callers, and update affected docs and `CHANGELOG.md`.
5. Review the diff for private data, unsupported claims, broken relative references, and client-version assumptions.

Keep changes focused. Company operations, email, Surface and Dropbox procedures are in scope, alongside JobTread. Add modules deliberately with documented inputs, outputs, evidence, coverage and failure behavior. Do not add unrelated skills, a second JobTread backend, a gateway installer, automatic pushes, or live business mutations as maintenance conveniences.

## Install reviewed edits without losing local work

The filesystem installer links the canonical skills into the shared discovery hub and optional client discovery locations. It does not configure MCP or create credentials:

```sh
cd ~/Work/cdb-workflows
python3 scripts/install.py --agents shared codex claude omp opencode
```

The shared hub is always installed first. The default target is `shared`; choose only the extra clients you need. Re-running with links already pointing to this source is idempotent. Restart the relevant clients or reload skill discovery afterward. Hermes profiles with `skills.external_dirs` already scanning `~/.agents/skills` need only shared installation, not local symlinks. `--agents hermes` is an explicit legacy option, not a required companion to shared discovery. Never rewrite client configuration or cron during this installation.

If installation reports a conflicting directory or link, inspect it first. Preserve any unique policy before choosing an explicit migration:

```sh
python3 scripts/install.py --agents shared codex claude omp opencode \
  --migrate
```

`--migrate` backs up conflicts under `~/.local/state/jobtread-skills/backups/`, grouped by timestamp, agent, and skill, before replacing their discovery entries. Review the installer’s reported paths; do not delete backups until you have reconciled local changes. The installer does not overwrite conflicts by default.

For a source migration, inspect every file in each original directory before copying reusable material. Preserve full original private copies under `~/.local/state/cdb-workflows/backups/` before sanitizing public source or retiring local discovery copies. Verify backup bytes and exact shared targets before removing the old local directories; do not leave duplicate local names shadowing external skills. This manual source backup is separate from the installer's historical `jobtread-skills` conflict-backup path. Never bring checkpoints, raw evidence or private backup inventories into the public checkout. See [current migrated modules and attribution](MIGRATED-SKILLS.md).

## Keep customer data and credentials private

Review every file destined for publication, including examples and generated output. Approved CDB policy is public; customer records and the evidence used to perform a customer’s work remain private.

Do not publish:

- Customer/vendor names, addresses, contacts, real record IDs, private prices, balances, bids, documents, signatures, or account details
- OAuth tokens, grant IDs/names/history, callbacks containing codes, bearer credentials, encryption keys, client secrets, or environment files
- Session histories, logs, local agent configuration, machine-specific service state, backups, screenshots, or raw tool responses containing business data

Use synthetic examples instead of lightly redacted live records. A schema can contain descriptive defaults or examples: inspect those too. `.gitignore` cannot protect a tracked secret or identify a private value embedded in documentation.

If private material is exposed, stop publication, notify the owner, and revoke or rotate affected credentials through the appropriate account controls. Coordinate repository/history cleanup with the owner; do not silently rewrite shared history or assume deleting the current file removes prior exposure.

## Preserve upstream provenance

Original CDB-authored instructions and repository code use MIT. JobTread schemas, tool descriptions, help content, third-party code, and trademarks retain their own ownership and terms. The MIT grant in `LICENSE` does not relicense upstream material or authorize redistribution beyond its original terms.

For each added or refreshed upstream reference, record provenance in the reference itself or an adjacent existing provenance document:

- Source URL or official MCP endpoint and tool/schema path
- Capture date and upstream/client version when available
- Whether the content is an exact capture, an excerpt, or an authored summary
- Any sanitization or transformations, without including private source values
- Applicable copyright/license notices or terms, and any unresolved redistribution restriction

Do not invent a capture date or claim a snapshot reflects current production. If source terms do not permit republication, link to the official source and write an original summary instead. Preserve existing attribution when updating a reference.

Refresh schemas through authorized read-only discovery. Store raw captures outside the repository, inspect for records and authorization metadata, and publish only reviewed API documentation. Reference completeness is separate from permission coverage; never exercise create/update/delete/send/payment operations to prove a schema exists.

## Verify only what you can substantiate

Choose checks appropriate to the change, then record commands, outcomes, and limitations in the review. Installer checks should cover isolated temporary homes, target links, idempotency, conflicts, explicit migration, backups, and absence of credential/config creation. Documentation checks should cover the installer CLI, links, skill names, public/private boundaries, and client configuration schemas.

Run the repository’s offline checks from its root:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The validator checks skill structure, metadata, JSON examples, relative links, and targeted credential/machine-path patterns. Installer tests use isolated homes. The GitHub Actions workflow in `.github/workflows/validate.yml` runs repository checks; it does not authorize JobTread or execute business workflows. Automated patterns do not replace a privacy review.

For an authorized live connection check, use the read-only checklist in [CONNECTING.md](CONNECTING.md#verify-the-connection-without-changing-records). Keep record responses and OAuth evidence private. An optional local gateway additionally needs unauthenticated rejection and authenticated reconnect checks.

Distinguish these evidence levels:

| Evidence | What it establishes |
| --- | --- |
| Source/configuration inspection | The documented format matches an inspected implementation or upstream reference |
| Installer checks | The tested filesystem installation behavior |
| OAuth, discovery, and harmless read | That client/account/transport connected and performed the specific read |
| Reconnect with saved authorization | Credential reuse for that tested connection |
| Authorized workflow execution and read-back | Only that exact workflow and target, not every operation |

Do not describe unperformed checks as passed. Neither a tool inventory nor full-access consent proves end-to-end budget, order, bill, payment, compliance, or deletion workflows. This public rollout does not itself claim runtime coverage of all workflows or every client/version.

## Review updates and pin releases

Consumers should use a reviewed release tag or exact commit. Maintainers tracking a branch should fetch, inspect incoming policy/code, and then explicitly update with `git pull --ff-only`; see the [README update commands](../README.md#update-deliberately). Never add scheduled pulls or pushes to the installer.

Before publishing a release:

1. Review changes to every affected skill and resolve policy conflicts.
2. Complete the privacy and upstream provenance review.
3. Run the scoped checks and document actual outcomes without private captures.
4. Update `CHANGELOG.md` with the release version/date and user-visible changes, including compatibility or migration notes.
5. Complete owner review under the publication authorization for the release, then publish its versioned tag/release.

Do not advertise a tag before it exists. Do not push automatically, rewrite tags consumers may have pinned, or include private machine configuration in release assets. A release is reviewed instructions and tooling, not a guarantee of JobTread API availability or a grant of business authority.

The current public CDB library rollout is authorized. This does not authorize unrelated deployments or business-record changes, and it does not enable automatic pushes.

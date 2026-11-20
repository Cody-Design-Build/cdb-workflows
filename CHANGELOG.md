# Changelog

## Owner-approved consolidation

- Consolidate latest eight JobTread modules, scheduling helper, installer/updater and tests here as canonical public source.
- Retain Dropbox and add lightweight business-email with own-account authorization, unsent drafts and separate final send approval.
- Move operations, memory/task/Surface/heavy-triage and generic interview dependencies to a separate local-only source repository with no remote. Preserve licenses, runtime paths and discovery names.
- Preserve private all-byte backups; leave protected policy files and shared history unchanged.

## Historical changes (former boundaries are superseded)

## JobTread extraction (superseded working migration)

- Move maintained JobTread source and its setup/scheduling tests to the independent public jobtread-skills package, including latest local edits.
- Keep company operations and Dropbox filing here; use an explicit external JobTread dependency rather than duplicate maintained procedures.
- Operations-only installer no longer replaces external JobTread skill links or credentials. Existing unrelated working edits are preserved; this migration is not automatically published.


Record user-visible changes to the public CDB company workflow library. Unreleased entries do not imply a published release tag.

## Unreleased

- Treat clear owner-directed JobTread writes as authorized without repeat confirmation; retain target, cascade, notification, and readback checks.
- Require MCP-only JobTread work, with no unsolicited browser or desktop preview opens.
- Add the shared `jobtread-scheduling` skill and a Sunday–Saturday week-block helper for draft schedule builds and revisions.
- Default JobTread line-item descriptions to short, plan-referenced scope while preserving responsibilities and scope limits.
- Keep individually owner-directed routine internal task changes usable during a memory outage with private local receipts, the same writer guard, live duplicate checks and exact readback. No change to scheduled or batch authorization.

- Add independently usable `cdb-company-memory`, `cdb-task-management` and `cdb-operations` procedures with explicit contracts, consequence-based approvals, incremental coverage/receipts, correction/freshness handling and reporting templates.
- Add a source-grounded Hindsight 1.2.1 stdlib helper for explicit-bank exact GET, synchronous single-item retain/readback, read-only verification and cooperative POSIX foreground locking. No production bank default, automatic retries, business API wrapper or source import/sync.
- Register all three modules in the filesystem installer; document tested synthetic helper behavior and limitations separately from unproven company operations.
- Align Surface Context and authorized email continuity with Hindsight-first ownership while preserving human notes, historical checkpoints and the existing read-only triage mandate. No cron/services/config, business records, memory routing or publication changes.

- Broaden the canonical library to general CDB company workflows and modular integrations without claiming a company-operations orchestrator is implemented.
- Register Matt Pocock's `grill-with-docs`, `grilling` and `domain-modeling` skills for installation; preserve their dependency links, original licenses and provenance. No `grill-me` module is included.
- Migrate `email-inbox-triage` and `cdb-surface-orders` with original names, attribution and MIT notices; sanitize private identities, project paths and supplier anecdotes while keeping reusable policy and private checkpoint compatibility.
- Add `cdb-dropbox-management` as the owning filing procedure; link job setup and Surface filing to it. Document how to find the team root when the Dropbox desktop account path points to a member's folder and how to handle an empty duplicate blocking a corrected stage move.
- Document shared Hermes external discovery and keep `--agents hermes` as an explicit legacy option. Shared-only installation does not create Hermes-local symlinks or edit config/cron.
- Add offline migration, provenance, targeted privacy and discovery regression checks; retain private original backups outside publication.
- Align checkout and clone instructions with `Cody-Design-Build/cdb-workflows`. Existing installer backup paths remain unchanged for compatibility.

- Add required `jobtread-job-setup` workflow for sourced intake, duplicate-safe customer/contact/property/job setup, plans, Dropbox reconciliation and a four-part handoff.
- Install the new workflow through shared and selected client discovery; link it from the general JobTread operating skill.
- Add offline setup-policy and installer regression checks; no live business-workflow coverage is implied.

## 0.1.0 - 2026-11-13

### Added

- Public CDB workflow skills: `jobtread`, `jobtread-budget-writing`, and `jobtread-catalog-standards`.
- Filesystem skill installation with shared discovery and explicit client targets, conflict protection, and opt-in migration backups.
- Portable onboarding that separates skill installation from official per-user JobTread OAuth connections.
- Client configuration examples for Codex, Claude Code, Hermes, OpenCode, and omp, with links to upstream references.
- Canonical repository policy, maintenance and provenance guidance, and an MIT license scoped to original authored material.
- Schema-led budget intake, proposal/preliminary proposal/change-order procedures, and schedule/daily-log procedures.
- Maintained query examples and documented inherited-schema provenance and errata.
- Installer regression checks and GitHub Actions validation.

### Publication boundaries

- CDB operating policy is public; customer records, credentials, OAuth history, and private machine state are excluded.
- Upstream reference snapshots retain their attribution and terms. They do not establish current tool availability or grant permissions.
- Documentation and configuration examples do not assert full runtime coverage across clients or end-to-end business workflows.

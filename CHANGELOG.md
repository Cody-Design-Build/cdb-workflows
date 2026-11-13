# Changelog

Record user-visible changes to the public CDB JobTread workflow library. Unreleased entries do not imply a published release tag.

## Unreleased

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

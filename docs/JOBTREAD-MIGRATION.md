# One maintained JobTread library

Use **Cody-Design-Build/cdb-workflows** for all eight JobTread modules. The owner authorized removing the duplicate **Cody-Design-Build/jobtread-skills** GitHub repository after verification and backup. Do not install or update from that retired repository.

## Feature-parity review

The comparison used these exact published main commits:

- Canonical cdb-workflows baseline: `14f35e3ea5cfc35adddb5de190a9f237ca5579e0`
- Retired jobtread-skills baseline: `ee1cdf845923b5fceb55a53bf9f849e618a2ed6d`

All 23 files under `skills/jobtread*` were byte-identical by Git blob identity: eight skill entry points, the scheduling helper and fourteen references. There were no retired-package-only file paths. All 40 retired file paths exist in the canonical library; package documentation, installers and tests differ where the broader library requires it. The official per-user connection guide, validator and CI workflow were identical at these baselines. The retired repository had only a main branch, no tags, releases or issues/pull requests at review. Its Git history was privately mirrored and integrity-checked before removal.

| Preserved module | Coverage |
| --- | --- |
| jobtread | MCP connection/discovery, safety, documents, vendor orders/bills/payments and structural references |
| jobtread-job-setup | Sourced intake, duplicate-safe records, Lead default, plans and Dropbox handoff |
| jobtread-job-management | Ongoing coordination, changes and closeout |
| jobtread-estimating | Approved scope baseline, traceable pricing and proposal allocation |
| jobtread-budget-writing | Scope wording, commercial terminology, allowances and rounding |
| jobtread-catalog-standards | Reusable catalog scope and approval boundaries |
| jobtread-scheduling | Whole-week planning and deterministic scheduling helper |
| jobtread-daily-logs | Evidence-based logs and corrections |

The canonical core now adds a common private checkpoint and partial-failure recovery contract: reuse verified IDs, reconcile uncertain writes before resuming, never replay a whole batch, and distinguish completed, blocked and unattempted work. Existing business approval, notification and financial rules remain unchanged. Dropbox and lightweight business email are available from the same library rather than another package.

## Migrate an old installation safely

1. Inspect the old checkout and installed links. Preserve local modifications and any unique content privately; do not delete an old checkout while discovery links still use it.
2. Follow the canonical [installation instructions](../README.md#install), validate and run the complete offline tests.
3. Install the required modules into the same discovery locations. Existing links to the retired checkout are conflicts: inspect them first, then explicitly use `scripts/install.py --migrate` to preserve conflict backups. Select only actual clients. Never reset or overwrite local work.
4. Verify every selected discovery link resolves into the canonical checkout and reload the client. Update team bookmarks and hosted skill attachments deliberately; a GitHub URL does not install or refresh attachments.
5. Keep each person's existing authorized connection separate from source migration. No credential transfer, service deployment or live business mutation is required.

Offline tests establish installation and documented policy contracts, not live OAuth or end-to-end financial workflow correctness. The deleted repository's URL will not redirect; replace old installation/update prompts with the canonical README.

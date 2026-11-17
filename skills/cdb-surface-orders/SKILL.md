---
name: cdb-surface-orders
description: Use when managing Surface orders. Discover and verify.
version: 0.1.0
author: David Cody, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [surface, procurement, orders, construction]
---

# CDB Surface Orders

Use CDB-Surface to maintain project procurement records and linked selections when Surface is the intended target. Before recommending where procurement should live, inspect existing JobTread schedule groups, to-dos, checklists and document links as well as Surface records; do not assume Surface must own the workflow or create a parallel tracker. Preserve the user's chosen system boundary until a migration is expressly authorized. Develop this skill as the user teaches purchasing conventions; save reusable rules, not a transaction diary.

## When to Use

- Working on CDB-Surface orders, supplier packages, procurement cleanup or project selections.
- Learning and preserving the CDB owner's conventions for using Surface.
- Do not use this as authority to place purchases, send supplier messages, alter prices or mark an order Ordered without explicit authorization and evidence.

## Prerequisites

Remote MCP: `https://cdbsurface.io/mcp`, OAuth, configured as `cdbsurface`. Discover its tool through `tool_search`; the sole public tool is `mcp__cdbsurface__surface` (server tool `surface`). If unavailable after installation, `/reload-mcp` loads it into an open session.

Source of truth: private repository `Cody-Design-Build/CDB-Surface`, especially `README.md` and `docs/AGENT-INTEGRATION.md`; use authenticated `gh api` through `terminal` when the public URL returns 404. Do not copy secrets or browser tokens.

## Procedure

1. Call `surface` with `{"action":"list_operations"}` at the start of each task. Describe unfamiliar operations with `{"action":"describe_operation","operation":"..."}`; omit `arguments` for both discovery actions.
2. Execute with `{"action":"execute","operation":"...","arguments":{...}}`; the inner arguments object is mandatory, even empty.
3. Search the `job` table for the project, then discover `list_tables` and execute `describe_table` for the target table. Record exact IDs, field keys and schemaRevision; never guess them.
4. Read the intended records and current revisions. Isolate project membership using the returned `fields.job`; inspect linked scope, notes and pricing before merging/archiving a duplicate. When asked to explain what exists and propose a plan, stay read-only: enumerate the current packages, proposed final packages and uncertain allocations before making consolidation writes.
5. For title-only cleanup, patch only `title` with `table`, `schemaRevision`, `id`, `baseRev`. Leave fields, body, aliases and relationships untouched. Validate uncertain record input before other writes.
6. Batch at most 25 records through `update_records`. These writes are non-atomic: inspect `complete`, `writesPerformed`, and every outcome; never blindly retry a batch after uncertain or partial commits. Reconcile fresh reads on revision/schema conflicts.
7. Interpret an authorized removal of a redundant order as reversible `archive_record`, not hard deletion. Verify its scope is preserved in the surviving order and do not double-count costs or duplicate selections. Read both packages and their selection links first; if the surviving package already includes the item and its supplier price, archive only the empty/superseded placeholder rather than adding the item or cost again. Keep quoted package totals intact until a supported line-item breakdown permits reallocating overlapping hardware or accessories.
8. Read every changed target back. Check exact requested titles, project membership, unchanged unrelated values and archive state. Aggregate/dedupe/count in code rather than mentally. Save multi-record responses to task JSON files for verification; no raw business data belongs in this skill.

## Contract and failure boundary

Inputs are the authorized project/records, requested actions and source evidence. Outputs are a verified procurement brief or exact approved record changes with private read-back evidence. No credentials, captures or transaction history belong in this skill. If schema discovery, pagination or a revision check fails, stop the dependent write, retain a private partial-work handoff and report unverified targets. Reconcile uncertain writes before retrying.

## Read-only project orientation

- For a request to understand a project, read the project body, all project orders, linked selections and project tasks before proposing changes. Keep this pass read-only and distinguish current purchasing scopes from cancelled, superseded and unselected records.
- Prove collection completeness before reporting counts: save response batches, deduplicate by record ID, compare the union with the server's declared total, then filter exact `fields.job` membership in code. A full page is not a complete table.
- Use returned pagination cursors unchanged. If a cursor is visibly abbreviated or unusable, never reconstruct it. For a bounded table, query both `sort: "title"` and `sort: "-title"`, union by ID, and accept this fallback only when the unique count equals the declared table total; otherwise continue discovery rather than claiming completeness.
- Project compact fields from saved responses first: ID, title, status, supplier, quantity/unit, linked order IDs, amounts and the leading current-status section. Read deeper history only for unclear scope or contradictions; dumping every historical body obscures current decisions and wastes context.
- When a structured status conflicts with prose, compare record chronology and use `get_record_history` if the decision depends on which is newer. Report the discrepancy without treating older shipping notes as proof that a later Received field is wrong; do not downgrade status or reorder during orientation.
- Deliver a short brief covering scope, purchased packages, unreleased packages, blockers and unresolved evidence. Label the result as Surface's recorded state, not independently verified live supplier tracking; do not expose unrelated site-access codes or create a parallel procurement tracker.

## Bid requests and accepted proposals

- Match live bid-request titles (`Project — Trade`) and vendor-proposal titles (`Vendor — Project`); order-title ASCII-hyphen conventions do not override the separate bid-request pattern. Link verified existing project/vendor IDs and check for duplicates before creation.
- Create new unsent bid requests as Draft, not Awarded merely because older examples are awarded. Leave unspecified scope documents, dates and detailed scope blank.
- For a user-confirmed accepted bid, record the stated quoted/agreed amount on an Accepted vendor proposal and set its parent bid request to Awarded, matching existing accepted-proposal patterns. Do not infer payments, signature, acceptance date or technical inclusions.
- Re-read the parent bid request after creating a linked vendor proposal before updating its status: inverse relationship creation increments the parent's revision, so a previously observed baseRev becomes stale.

## Filing supplier documents

- Follow [cdb-dropbox-management](../cdb-dropbox-management/SKILL.md), which owns folder discovery and filing policy. Resolve the live Dropbox root and inspect the verified project folder; historical paths or procurement numbering in notes may be stale.
- Read the latest email and the PDF cover before naming the attachment. Preserve supplier document type: a PDF labeled Quote with a blank Order Number remains a quote even when called an order conversationally.
- Preserve original filenames by default under the owning filing policy. When a rename is approved, a quote may use `YYYY-MM-DD - Supplier - Scope Quote NUMBER - Revised.pdf`; use the verified document date, preserve older revisions and original PDF bytes. Hash-compare the saved file with the attachment.
- Saving into a synced directory proves the local file exists, not that Dropbox uploaded it. Verify remote sync if possible; if a status command fails, state that cloud sync remains unverified. Do not update Surface prices/status solely because a filing task was requested.

## Record Context and Documents policy

- Use the existing record `body` as **Context** across record types, including tasks, selections and orders. This is a display-name convention, not a new schema field or a data migration. Preserve existing text and unrelated fields named Notes.
- Keep current understanding and next moves first; retain material decisions/progress and supporting source references below. Read fresh content and revisions before editing, preserve human contributions, and reconcile conflicts instead of overwriting them. Do not accumulate repetitive run summaries or infer permission to change records from this convention.
- Documents are soft-deprecated for routine operational context. Do not create or recommend separate Documents solely to hold a record's working context; keep it on that record. Preserve existing Documents, links and supported read/export/API behavior. Soft deprecation does not authorize archival, deletion, migration or hiding navigation.
- Full removal of Documents is a deferred owner decision, requiring review of existing content, relationships, application/API/original-client dependencies and any preservation/migration plan, followed by separate explicit approval.

## Naming conventions

- Favor short, scannable Title Case order titles: `Kitchen Cabinets`, `Front Windows`, `Interior Doors`, `Quartz Countertops`.
- Use ordinary ASCII hyphens surrounded by spaces (` - `), never em/en dashes in order titles. Keep genuine compound-word hyphens such as `Single-Hung`.
- Use category-first grouping when useful: `Lighting - Kitchen Pendants`, `Lighting - Guest & Kids' Baths`.
- Supplier is already a separate field; avoid redundant supplier names unless needed to distinguish similar packages, e.g. synthetic titles `Plumbing - Supplier A` and `Plumbing - Supplier B`.
- Simplifying a title does not remove actual scope: cabinetry may still include floating shelves; appliance packages may include the range hood and laundry. Preserve underlying notes, selections and amounts.
- Preserve supplier spelling from verified records; resolve ambiguous dictated names against existing contacts and correspondence rather than creating or renaming a supplier blindly.

## Orders, shipments and receiving

- Inspect the chosen system's existing order packages and schedule before proposing new structures. Keep order lifecycle separate from receiving appointments: a schedule entry can coordinate an arrival but cannot alone establish what was purchased or received.
- Separate selection approval, purchase placement, payment, shipment, physical receipt, inspection and site transfer. Track split shipments by affected item and quantity, destination, estimated versus confirmed arrival, receiver and outstanding exceptions; one delivery notification must not complete the whole supplier package.
- Preserve shortages, damage, returns and replacement requirements after partial receipt. Record the evidence source explicitly: supplier-reported delivery is not an onsite count or damage inspection.
- Treat multi-piece items at component level: owner-confirmed receipt of a shade or other component supports Part received, never receipt of the whole assembly. Preserve the ordered item quantity; record missing components and verify their tracking before closing receiving. If a tracking number appears against different items, flag the conflict rather than propagating a delivery claim to both. Identical-SKU shipment numbers stay unassigned to rooms until receiving identifies them.
- Use tasks or to-dos for the next action and link the authoritative order rather than duplicating its financial or fulfilment status. If procurement is deliberately housed in JobTread, respect that choice instead of maintaining a competing editable tracker in Surface.

## Status and supplier corrections

- Treat the CDB owner's explicit confirmation that an item was ordered or received as evidence for that status. A later correction in the same message supersedes an earlier 'shipped' statement. Distinguish owner selection, sales-rep inclusion on a package, supplier placement/payment, shipment and physical receipt; confirmation of one does not prove the others. Do not invent transaction, shipping or receipt dates from the date of the conversation.
- Record new approval, supplier and receipt confirmations ahead of superseded notes in a concise current-status section; label retained contradictory text as historical. Do not leave an old 'approval pending' or 'not received' sentence as the apparent current instruction. Preserve financial evidence and do not change a pricing-basis field merely to record a nonfinancial status update.
- Preserve replacement requirements when consolidating procurement: move linked selections and an explicit 'replacement needed; product and price to confirm' task into the surviving package before archiving a standalone placeholder. Do not treat an unavailable original item as cancelled scope or add an unquoted replacement estimate to a supplier quote.
- Distinguish product brand from purchasing supplier: a specified product brand may be purchased through a different distributor. Correct the supplier without replacing the specified product/model or combining distinct orders.
- Keep shower-glass fabrication/installation and separately purchased shower hardware as distinct orders unless explicitly instructed to consolidate them.
- Shorten titles by dropping model/collection suffixes when the user requests cleanup; preserve the actual model, scope and quantities in linked selections and notes.
- Archive a discarded alternate supplier inquiry when directed; preserve the selected supplier's order and linked selections. Do not turn a never-received quote into priced procurement.

## Pitfalls

- Cross-check unexpectedly empty relationship-filter results with a broader paginated read and filter the returned `fields.job` values in code; filter syntax or link semantics can hide existing orders. Diagnose the filter before concluding a project has no orders or changing relationships.
- Large order responses include long historical notes. Parse spilled JSON files with `terminal`/Python and project compact fields before reasoning; do not repeatedly fetch the same data just because it spilled.
- New reconciliation headings may supersede older notes. Read current scope plus chronology; do not resurrect cancelled items or mistake historical estimates for current supplier pricing.
- An archived record may still be mentioned by active notes; preserve the history rather than rewriting unrelated notes during title cleanup.
- Schema IDs/revisions, record revisions, operation catalog and prices are live data: rediscover, do not hardcode them in future payloads.

## Verification

- Every requested rename is read back exactly and contains no unintended Unicode dash separators.
- Unrelated fields, notes, aliases and relationships match pre-write snapshots for title-only work.
- Removed duplicate is read using `get_record` with `includeArchived: true` and has a non-null deletion timestamp; the active project list omits it.
- Report the main changes briefly, distinguish archive from deletion, and flag discovered duplicate scope for a later decision instead of silently widening cleanup.

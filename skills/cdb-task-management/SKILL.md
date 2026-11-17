---
name: cdb-task-management
description: Use when matching or maintaining CDB internal tasks.
version: 0.1.0
author: David Cody, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [cdb, tasks, evidence, reconciliation]
    related_skills: [cdb-company-memory, cdb-surface-orders, jobtread]
---

# CDB task management

Own finding/matching obligations, task content, duplicate checks, creation/update, completion and reopening. Usable for a human-assisted single task without company-wide operations. This is a schema-led procedure over existing authorized business tools, not an invented task API.

## When to Use

- Identify whether an obligation is already tracked in Surface or JobTread.
- Prepare or apply an authorized internal task change, close on explicit evidence, or reopen after a correction.
- Do not use a new task to replace the authoritative order, schedule, bill, job or selection record.

## Prerequisites

Inputs: exact obligation/evidence, company/project identity, requested target system and allowed consequences. Load [cdb-company-memory](../cdb-company-memory/SKILL.md) for continuity, action intent/outcome and the shared writer boundary. For Surface use the discovery/revision/Context rules of [cdb-surface-orders](../cdb-surface-orders/SKILL.md); for JobTread load [jobtread](../jobtread/SKILL.md), its query procedure and schedule/to-do reference before calls. Memory may be unavailable: read-only matching and a private proposal can continue, but no receipt-dependent writes.

No API connection or service is created here. A manual human can perform the same reads/edits in the approved UI and supply exact IDs plus readback evidence; the agent must label user-reported rather than tool-verified outcomes when it cannot independently read them.

## Procedure

1. **State the obligation.** Extract work to do, next actor, project/company scope, promised date versus suggested reminder, dependencies and objective completion condition. Use [task handoff](templates/task.md). Keep reference/noise/already-resolved messages as dispositions, not manufactured tasks. One message can imply several obligations; several threads can describe one task. Done when the action and acceptance evidence are explicit.
2. **Discover and match live state.** For Surface call `mcp__cdbsurface__surface` with `action: list_operations`, then `describe_operation` for needed reads and `describe_table` through discovered operations; inspect actual task fields, relationships, completion semantics, notification defaults and revision requirements. For JobTread use `mcp__jobtread__query` schema discovery and current organization/grant, read relevant schedules/to-dos/checklists and linked documents. Exact-GET known memory associations, then compare open/completed candidates by scope, job, next actor, source references and dependencies, not titles alone. Paginate before an absence claim. Done when the chosen match, a demonstrably new obligation or an unresolved ambiguity is recorded.
3. **Choose one owning record.** Respect where the work already lives; do not mirror editable tasks into Surface just because it has Kanban. Source associations may be many-to-many. For an ambiguous match leave candidates visible for decision instead of creating duplicates. Preserve the order/bill/schedule's authority. Done when target identity and ownership are unambiguous.
4. **Prepare the minimal change.** Read fresh record/revision. Preserve human text and unrelated fields. Task content needs a concise actionable title, linked job/workstream and source, next actor, dependencies, promised deadline or explicitly proposed reminder, and completion condition. Use Surface Context only for useful local notes/evidence/handoff under its owning rules; comprehensive narrative belongs in Hindsight. Do not invent assignees, dates or new fields. Done when exact patch/content and expected outcome are reviewable.
5. **Apply consequence gates.** Explicitly authorized internal creation/update or evidence-supported nonfinancial tracking can proceed only within the current run's allowed mode. Changing assignment/due dates may notify people or affect crews; inspect and explicitly suppress supported notifications, otherwise queue approval. Sends, external-facing documents, financial changes, deletion/archival, access changes and consequential schedule/sign-off decisions require exact approval. Existing read-only cron stays read-only. Tool capability is not permission. Done when intent records authorization and notification behavior.
6. **Persist intent, execute, verify.** Under the shared one-writer protocol retain/read back exact intent before mutation. Recheck duplicates immediately before create. Use discovered revision-aware operations (Surface requires current schemaRevision/baseRev where applicable); no guessed `create_task` or fixed field names. Inspect each batch outcome; do not retry partial batches wholesale. Re-read every exact changed target and relevant competing matches, then retain verified/failed/uncertain outcome through company memory. Done when requested content and preserved values are checked against readback, or remaining uncertainty is explicit.
7. **Complete or reopen on evidence.** Routine internal tasks may close when explicit evidence satisfies **all** acceptance conditions. Supplier delivered is not physically counted/inspected; contractor finished is not accepted; partial receipt is not whole-package completion. Ambiguity, disputed facts and consequential sign-offs leave state unchanged for decision. A human correction can justify reopening with attribution/history preserved, subject to notification/schedule gates. Re-read target and retain source/closure or reopening reason. Every closure belongs in the run report and daily aggregation; do not hide it in a generic updated count.

## Contract and failure boundary

Outputs: matched task IDs with rationale, a precise proposed change, or authorized changes with exact readback and memory receipt IDs. If discovery/pagination, identity, notifications, revisions or source evidence is uncertain, stop the dependent mutation and report a bounded proposal. If a write times out, reconcile the exact live target and duplicate candidates before any retry. Do not turn an absent receipt into permission to recreate work. Private records, task evidence and run files never belong in public skill source.

## Pitfalls

- No matching task in Surface does not prove no task exists in JobTread.
- Completing a task does not authorize financial acceptance, employment action, purchase placement or project closure.
- A status field may have human workflow or notification consequences; a nonfinancial name is not enough to make a change routine.
- User-reported UI completion is an attributed claim until independent verification is available.
- No task-sync service, automatic due-work scanner or actual integration mutation is tested by this skill's offline checks.

## Verification

- Candidate coverage and ownership shown; no speculative duplicate or parallel financial/procurement tracker.
- Exact target/content, source, completion condition and permission captured before writes.
- Destination readback and company-memory outcome agree, or state is explicitly uncertain.
- Each closure/reopening, approvals still needed and incomplete source coverage are reported.

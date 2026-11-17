---
name: cdb-operations
description: Use when reviewing CDB priorities and assisted follow-up.
version: 0.1.0
author: David Cody, Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [cdb, operations, coverage, priorities, reporting]
    related_skills: [cdb-company-memory, cdb-task-management, email-inbox-triage, cdb-surface-orders, jobtread]
---

# CDB operations

Coordinate coverage, cross-company interpretation, priority, approval routing and verified reporting. The procedure is runnable now with authorized tools and an agent/human operator; it is **not-yet-automated** as an autonomous runner, scheduler, ingestion pipeline or business integration. Standalone memory/task/email/procurement skills remain independently usable.

## When to Use

- Produce the daily company briefing or a current/as-of company report.
- Resume unfinished review, identify due waiting work, reconcile developments against live records and assist approved follow-through.
- Do not use this to install schedules, synchronize JobTread and Surface, change access or import historical evidence.

## Prerequisites

Resolve authorized sender, explicit mailbox(es), company/job scope, audience/delivery destination, timezone, time/record/token budget and allowed action mode from current request/private configuration. Do not hardcode a mailbox. One owner-configured CDB memory bank covers default Hermes business sessions; configuration activation is separate and must be verified. Other profiles/agents and historical banks remain untouched. Shared Slack/channel exposure is not owner-only isolation. Exclude personal/family material and restricted HR/legal content from pilot memory/reporting; verify actual audience before any disclosure.

Load [cdb-company-memory](../cdb-company-memory/SKILL.md) for exact records, retrieval, freshness, receipts and serialization, and [cdb-task-management](../cdb-task-management/SKILL.md) for task matching/content/lifecycle. Load [email-inbox-triage](../email-inbox-triage/SKILL.md) for full-thread business analysis and provider-dependent commands; load the actual external email connector and business-email send gate when available. Load [cdb-surface-orders](../cdb-surface-orders/SKILL.md) for actual Surface discovery/revisions/Context/procurement, and [jobtread](../jobtread/SKILL.md) plus relevant references for its operational reads/changes. These dependencies own their policies; do not invent common API wrappers or bypass stricter domain approval rules.

The existing triage cron is **read-only**. This skill does not widen it. A new owner-authorized operations run may allow internal task/Context changes, evidence-supported nonfinancial tracking and unsent Gmail drafts subject to consequence gates below; a request for a report alone stays read-only. No schedule/service/config changes are implied.

## Procedure

1. **Open a bounded run.** Set mode (read-only or explicitly authorized assisted actions), audience and budget. Acquire one writer for the whole read/decision/write sequence using the memory protocol; if serialization cannot be established, keep all dependent actions as proposals. Exact-read previous unfinished run/checkpoints/intents/outcomes and relevant contextual memory. Initialize a private run manifest and verify its Hindsight index. Done when run identity, prior gaps, allowed sources/actions and holder are known.
2. **Resume before expanding.** Reconcile uncertain actions with destination state before retry, finish pending review units, then take an overlapping pass for new developments. Budget capacity for new urgent work instead of spending the entire run backfilling history. Waiting/due obligations need review even without new mail. Done when carried work is completed or explicitly pending, never silently dropped.
3. **Discover fresh coverage.** Use real live schemas and paginated source reads. Email triage supplies developments/next actors; Surface supplies intended records and human task views; JobTread supplies job schedules/to-dos/checklists/documents and operational state. Cover active jobs, leads/preconstruction, procurement, closeout, administration, employee-management issues, scheduling/crews and business networking/outreach within permitted sensitivity. Missing sources become named gaps. Save bounded discovery batches, exact IDs/change markers and counts privately; deduplicate/count in code. Do not claim complete incremental discovery until change semantics, pagination and reconciliation have been verified. Done when discovered, screened, fully reviewed and pending counts are distinct.
4. **Reconcile each review unit.** Compare latest source evidence, existing business records and exact memory associations. One message can concern several obligations and several threads one task. Record tracked/reference/noise/resolved/waiting dispositions as well as proposed work. Check humans have not already acted. Preserve uncertain matches/contradictions; do not create speculative duplicates or overwrite disputed state. Structured owning-system fields are authoritative operational records, not proof that every claim is true. Done when evidence, next actor, dependency and priority rationale are explicit.
5. **Save progress incrementally.** Through company memory retain/read back source-backed review events, many-to-many associations, pending units, fresh coverage and lag/failure notes after each bounded completed unit. Advance coverage only across reviewed work. Memory outage leaves dependent business writes stopped; source reads may continue with a private handoff and a disclosed continuity gap. Done when an interrupted next run can exact-read known IDs and resume rather than depend on final prose.
6. **Route consequences, not tool names.** Internal task/Context changes, nonfinancial tracking and unsent Gmail drafts require current run authorization, live evidence, duplicate checks, fresh reads, pre-action intent and readback. Inspect/suppress actual notification defaults; otherwise put the change under **Needs your decision**. Sending messages requires separate explicit approval of final recipients/content/attachments/account. Issuing documents, financial changes, deletion/archival, access changes and schedule changes affecting crews or notifying people require exact approval. Tracking an employee issue never authorizes an employment decision. Domain skills may impose stricter gates, including JobTread bulk changes and email draft previews. Do not reinterpret standing intent as approval of a changed final target/content. Done when each action has exact authorization or is queued.
7. **Delegate and verify actions.** Task management owns task writes and closure/reopening; email owns saved drafts and confirmed sends; Surface/JobTread owning skills own domain mutations. Persist/read back exact action intent before each external write and verified/failed/uncertain outcome afterward. Reconcile ambiguous outcomes, not blind retries. Preserve existing Surface Context and Documents; use concise local handoffs rather than duplicate full company narratives or create Agent Context fields everywhere. JobTread-to-Surface project sync is a separate deferred project. Done when every attempted action has an explicit outcome and evidence.
8. **Build a sourced report.** Follow [briefing template](templates/briefing.md): **Needs your decision**, **Next moves**, **Blocked/waiting**, then material developments, actions/receipts and coverage. Rank by safety, deadlines, blockers and customer/financial consequences, not unread state/age alone. Include every routine task closure and correction-driven reopening in run output and daily aggregation; partial/ambiguous completion and consequential sign-offs remain human decisions. Report drafts as unsent. Re-read action-critical source threads/destinations near report time. Current reports need fresh discovery or explicit **cached/as-of** labeling. Retain the report as derived synthesis, never independent corroboration. Done when coverage/lag, pending work, failures and approval needs are visible.
9. **Close or hand off.** Verify final run index and outstanding backlog, release the writer holder and deliver only to the approved audience. Produce one daily company briefing; interactive current reports are available on request. Quiet incremental cadence, including any 30-minute run, remains deferred pending cost/coverage measurement and explicit scheduling authorization. No automatic delivery or cron update is installed. Done when the next unit and uncertain actions are recoverable.

## Contract and failure boundary

Inputs: authorized identity/audience, source scope, explicit action boundary and budget. Outputs: bounded fresh/as-of attention report, incremental exact coverage/associations, action intents/outcomes, approvals and backlog. Missing authorization or unavailable tools never get replaced with pretend integration results. Source failure stops dependent decisions, not all useful read-only review. Memory/lock failure stops receipt-dependent mutations. Uncertain external results require live reconciliation and may require human resolution. Reports/evidence stay outside the public checkout.

## Pitfalls

- This is an executable **procedure**, not an installed service or claim that full company operations have been proven.
- Reports, retained conversational assertions and supplier claims do not become verified business facts by repetition.
- Partial shipment/delivery, contractor completion and official acceptance are separate; task closure follows its actual acceptance condition.
- Useful Context notes are allowed; source syncing, historical imports, new universal fields and duplicated narrative wikis are not assumed.
- Synthetic exact-memory/lock tests do not establish business integration permissions, notification suppression, crash-safe external execution, ACL enforcement, refresh correctness or backup recovery.

## Verification

- Every source has fresh coverage or an explicit gap/as-of; completed/pending counts agree with saved manifests.
- Every action has exact pre-intent, permission and verified/failed/uncertain outcome; closures appear in report/daily aggregation.
- Duplicate checks span the actual owning systems and memory associations; unresolved conflicts remain visible.
- Audience checked; reports distinguish raw evidence, attributed claims, decisions, proposals and synthesis.
- Existing read-only triage, cron/services/config, historical banks and business records are unchanged unless separately authorized.

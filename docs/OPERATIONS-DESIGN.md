# Company operations design

Status: design interview in progress, not an implemented service. This document consolidates the interview's current decisions; earlier Surface-body-primary assumptions are superseded by the Hindsight-primary architecture below. Existing read-only triage scheduling has not been widened. Keep private accounts, customer evidence, personnel facts and run outputs outside this public repository.

## Purpose and vocabulary

**Operations**: the company-wide review and coordination process producing an attention list, assisted follow-through and verified action reporting.

**Skill**: a reviewed procedure defining how work is performed; not a memory store, executable object or authorization boundary.

**Company memory**: sourced operational evidence, relationships, decisions and evolving understanding maintained through Hindsight. Memory includes only ingested/reconciled information, not guaranteed knowledge of everything in the source systems.

**Operational record**: the structured task, job, order, selection or other record in its owning business application.

**Run receipt**: an exact record of review progress or an intended/attempted/verified action, distinct from a generated summary.

## Confirmed architecture

- Hermes is the initial execution, scheduling and communication platform. Shared reusable skills remain in this repository and are independently usable without running operations.
- Hindsight is the primary company-context and continuity application, not a supplement to a collection of task-body wikis. Use its exact documents, scoped retrieval, observations and pages/models as appropriate. It supports cross-record/project understanding spanning schedules, procurement, design, changes, subcontractors, permits, inspections and crews.
- Surface provides structured operational records and human task/Kanban views. JobTread remains the operational job system. Structured fields in their owning systems are authoritative; Gmail and source files preserve original evidence.
- Existing Surface Context is preserved for local notes, evidence links or concise handoffs. Do not require full duplicated narratives, create Agent Context fields everywhere, revive Documents for routine memory, or migrate/delete existing content as an incidental implementation step.
- Skills own the processes. Retained mail, memories and generated summaries never supply authorization or override reviewed procedures.
- A shared company-memory access procedure is proposed for exact addressing, source attribution, scopes, retrieval, correction, freshness and receipt handling. Its implementation and module boundary still need agreement.

## Module ownership

- Operations owns review coordination, coverage, prioritization, cross-company interpretation, approval routing and reporting; it delegates domain mutations.
- Email triage owns communication review and identifying developments, requests and next actors.
- Task management owns finding/matching, creating/updating, completion/reopening, task-specific content and duplicate checks. It must work for interactive agents and manual human workflows as well as scheduled operations.
- Procurement and other domain procedures own their business distinctions; integration skills own safe provider commands, schema discovery, revisions and verification. Do not duplicate their conventions inside operations.
- General rules for any Surface Context edits belong in shared Surface guidance, with record-specific structure where needed. These are not a mandate to maintain comprehensive memory in every body.
- Proposed exact memory documents and associations must be accessed through supported Hindsight interfaces, not private database writes.

## Authority and safety

- Intended scheduled permissions: create/update internal tasks, maintain useful Context, change evidence-supported nonfinancial tracking fields in Surface/JobTread and save Gmail drafts, with source evidence, duplicate checks, fresh reads and verified outcomes.
- Approval remains required for sending messages, issuing documents, financial changes, deletion/archival, access changes and schedule changes affecting crews or notifying people. Tracking employee issues does not authorize employment decisions. Inspect/suppress notification defaults; otherwise queue for approval.
- Routine internal tasks may close when explicit evidence satisfies their completion condition. Every closure appears in run reporting and daily aggregation. Partial/ambiguous evidence and consequential sign-offs require human review; supplier delivery does not establish physical receipt/inspection, and a contractor's finished claim does not establish acceptance.
- Human correction can reopen tasks while preserving meaningful history, subject to notification/schedule safeguards. Unresolved contradictions retain competing sources and leave disputed state unchanged; surface them under Needs your decision and retain the human resolution.
- An intended write must have a durable receipt before execution and a verified result afterward. An uncertain external outcome requires destination reconciliation before retry, regardless of where receipts live. Logs are not rollback.

## Coverage and incremental operation

- Scope includes active jobs, leads/preconstruction, procurement, closeout, administration, employee management, scheduling, crews and networking/outreach. Conversational relationship development can be business.
- Mailbox and audience are explicit inputs. Clearly personal/family content stays out of company memory. Restricted business material cannot flow into general employee reports. Current shared-key bank/tag scoping is not an enforced multi-user privacy boundary.
- Email/task associations are many-to-many at message/topic level. One message can affect several obligations; several threads can affect one task. Do not create a task per email or treat no linked task as proof a task is needed.
- Before creating work, check existing live records and exact memory associations; humans may have acted outside operations. Record reference/noise/resolved/waiting dispositions too. Ambiguous matches remain visible instead of generating speculative duplicates.
- Revisit due waiting work without new mail. Distinguish promised deadlines from suggested internal reminders.
- Establish an incremental baseline of active/unresolved company work while reserving capacity for new urgent developments. Use supported source change markers, overlap and periodic reconciliation; verify capabilities before promising complete incremental discovery.
- Save completed review units, unreviewed backlog and uncertain actions incrementally. Advance coverage only across reviewed work. Next scheduled invocation resumes unfinished review before an overlapping company-wide pass; interactive help remains possible.
- Begin with one serialized operations writer. Hindsight exact documents are a candidate for checkpoints, associations and receipts, subject to validation of its last-writer-wins and pagination limits. No extra database is assumed necessary.

## Reporting and memory freshness

- One daily company briefing plus an updated current company report on demand. More frequent quiet incremental reviews are deferred until cost/coverage measurement; no 30-minute cadence is approved.
- Lead with Needs your decision, Next moves and Blocked/waiting, then material developments and receipts: task creations/closures, updates, drafts and coverage gaps. Explain priority by safety, deadlines, blockers and customer/financial consequences, not unread state or age alone.
- A generated report is a derived view, not independent corroborating evidence. Distinguish raw sources, attributed claims, verified facts, proposals, human decisions and synthesis in Hindsight.
- Current reports require fresh discovery or an explicit cached/as-of disclosure. Track source coverage, memory ingestion/consolidation/refresh lag and failures; successful retain is not proof every summary is current.

## Separate follow-on work

JobTread-to-Surface high-level project sync is a separate independently reviewable/schedulable project. Start one-way with explicit identity/field mapping, ownership, conflict behavior and readback. Reverse sync is deferred. Operations consumes sync freshness/failures rather than implementing sync in its prompt. No sync job has been installed.

Dedicated assistant authentication is under consideration for attribution. Gmail access does not change Surface identity. No identity/credential switch is approved by this document.

Documents remain soft-deprecated for routine operational context; preserve existing data, relationships and functionality. Full removal requires a separately approved dependency/data review.

## Confirmed Hindsight-first module contract (Round 8)

- An independently usable cdb-company-memory procedure owns consistent Hindsight access: stable identities/scopes, source retention, exact associations and receipts, contextual retrieval, correction and freshness. Domain modules retain business decision ownership; operations orchestrates.
- Preserve attributable source evidence separately from derived interpretation. Retain source timestamps and explicit business-record associations; synthesis does not promote a claim to verified truth.
- Human resolutions are authoritative amendments within their stated scope, retained with evidence and used to refresh understanding. Preserve genuine historical correspondence; correct erroneous imports explicitly rather than rewrite history.
- Support narrow item context and cross-project/company questions through explicit business identities and dependency associations. Avoid isolated project-memory silos; enforce real audience boundaries rather than assuming tags are ACLs.
- First validate Hindsight exact documents for coverage checkpoints, email/task associations, pending-action intents and verified receipts with a single serialized operations writer. Do not introduce another persistent database by default. Exact lookup, destination reconciliation and synthetic recovery tests are required; semantic recall alone is not execution proof.

## Round 9: memory routing and pilot

- User accepts a deliberate company-memory scope in principle, but wants explicit explanation and low-friction routing between company and hobby/personal work. No global bank-routing changes are approved; avoid relying on the model to classify every chat turn perfectly. Operations/domain procedures should explicitly target company memory, while generic conversational capture remains separate until reviewed.
- Initial use is owner-directed. The existing assistant is also reachable in a Slack channel that others could access; the user presently accepts that practical exposure. Do not represent the installation as technically owner-only or change Slack access as a side effect. Verify actual sender authorization and delivery audience before expanding sensitive content.
- Existing hosted Nous processing is approved for the pilot's permitted business-evidence classes; personal material, credentials and restricted HR/legal treatment remain excluded/deferred as proposed.
- Synthetic validation may run in the background without further user input, using the designated synthetic bank and no business-system changes. Keep tests bounded and report actual results/elapsed time; no promise of full crash recovery or production readiness from a small test.

## Superseding decision: one Hermes business-memory scope

The user designates every session in the existing Hermes environment as CDB business operations. Hobby work will use other agents. Use one explicit shared CDB Hindsight bank across this Hermes environment's desktop, CLI and messaging sessions, rather than routing ordinary conversation separately by topic, platform or user. Do not extend this policy to other Hermes profiles or external agents without authorization.

- This supersedes Round 9's separate company-vs-conversation routing proposal. Skills still distinguish raw conversational assertions, sourced evidence, verified business facts and exact execution records within the same bank.
- Existing platform/user banks are not yet migrated, deleted or remapped. Inspect supported provider settings, preserve configuration, define whether historical banks are imported or remain available, and verify new-session reads/writes before claiming a unified bank is active. Historical imports require separately reviewed scope; no automatic merging.
- The Slack channel may be accessible to other people. A unified bank implies potentially shared business context across these entry points, not owner-only isolation. Do not widen sender permissions, channel membership, API access or private report delivery as a side effect. Consequence-based action approvals still apply.

## Research and unresolved design frontier

See [Hindsight review](HINDSIGHT-REVIEW.md) for source-grounded capabilities and limitations of the installed release. No production import or memory-service changes followed from that review.

Decisions still needed:

1. Shared company-memory procedure and separation between immutable evidence, exact associations/receipts and derived observations/pages.
2. Correction policy: authoritative amendment vs source replacement; source timestamps, scope and cross-project/entity linkage conventions.
3. Minimal persistence/serialization protocol using Hindsight and interruption acceptance tests.
4. Initial company-memory scope, sensitive-audience enforcement and hosted-processing approval.
5. Ingestion baseline, source change-discovery capabilities, refresh strategy and reporting budgets.
6. Backups, restoration, production persistence and monitoring before dependence on company memory.

Next step: continue Grill With Docs on these unresolved decisions, not re-ask settled platform/permissions questions or implement an unapproved architecture.

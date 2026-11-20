---
name: jobtread-job-management
description: Review and coordinate ongoing CDB jobs safely.
version: 0.1.0
author: David Cody, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [JobTread, Construction]
    related_skills: [jobtread]
---

# CDB JobTread Job Management

## When to use

Use for ongoing job reviews, stage changes, coordination, change intake and completion checks. Read [jobtread](../jobtread/SKILL.md) and its [query procedure](../jobtread/references/query-tool.md). This module coordinates existing records; it is not an autonomous project manager, communication sender or source of financial policy.

## Procedure

1. **Establish the review boundary.** Match the exact organization/job and user-requested period or decision. Read job details, customer/location links, current stage and independent closure state. Load [setup](../jobtread-job-setup/SKILL.md) for incomplete onboarding rather than creating substitute records.
2. **Read current evidence.** Enumerate all relevant schedule/tasks, daily logs, current plans/files, customer documents, accepted changes, vendor orders/bills and payment allocations. Paginate each collection independently. Store a private ID/source map and coverage notes; a narrow task needs only relevant collections, while a whole-job claim requires complete coverage or an explicit gap.
3. **Reconcile facts, not labels.** Compare requested scope to accepted documents, draft budget to approved baseline, scheduled dates to observed progress, and ordered/billed/paid/delivered/received states separately. Attribute sources and date/revision. Do not infer signature, approval, compliance or receipt from a name or status alone.
4. **Prepare the next-action mapping.** Identify record ID, current state, proposed fields, source, owner and dependencies for each requested action. Review requests stay read-only. A clear scoped write request is authorization under the operating skill; ask only about genuinely unresolved scope or consequences. Do not create a parallel task system or mirror Surface/Dropbox status automatically.
5. **Use the owning workflow.** Load [scheduling](../jobtread-scheduling/SKILL.md) for task/date changes; [daily logs](../jobtread-daily-logs/SKILL.md) for site reporting; [budget intake](../jobtread/references/budget-data-intake.md) and [writing](../jobtread-budget-writing/SKILL.md) for budget revisions; [customer documents](../jobtread/references/customer-documents.md) for proposals/change orders; [vendor workflow](../jobtread/references/vendor-orders-bills-payments.md) for orders, bills, compliance and payment recording. Load external filing/communication skills only for explicitly requested actions.
6. **Apply and reconcile.** Discover exact current mutation schemas/defaults, preserve unrelated fields, set notification controls explicitly where supported, and save each response privately. Read back each exact target before dependent actions. An uncertain write requires reconciliation, never a blind retry.

## Stage, closure and handoff

For a requested stage change, discover the organization's current Status custom field/options and use the supported update route; do not invent a built-in status. Preserve closure, budget, schedule publication and sharing unless those changes are expressly included. For requested closeout, inspect incomplete tasks, unresolved changes, open financial obligations, plan/document revision and missing turnover evidence. Report blockers; do not zero balances, mark work complete or close merely to make a dashboard green. Closing a job does not authorize archiving its Dropbox folder.

## Pitfalls

- A draft change order does not amend an accepted contract or authorize work.
- A completed schedule row does not prove inspection approval or supplier receipt.
- An internal review authorizes neither external messages nor financial commitments.

## Verification

Return a concise sourced job snapshot, authorized changes with exact readback evidence, unchanged critical states, missing coverage, and next decisions/owners. Distinguish planned from performed work and draft from sent documents. Claim whole-job completeness only after reconciling all relevant pages and requested scope.

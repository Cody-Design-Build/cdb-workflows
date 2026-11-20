# CDB schedules and daily logs

Read [jobtread](../SKILL.md) and [query procedure](query-tool.md). These are conservative operational steps grounded in inherited schemas, not new CDB rules about working hours, sequencing, notice periods or reporting obligations. Discover exact current operations, fields, templates and notification defaults before use.

## Schedule intake and discovery

1. Match the job and requested scope: draft plan, task update, baseline change, publication or completion reporting. Read existing schedule/tasks, hierarchy, dependencies, assignments, dates/times, progress, recurrence, baseline and publication state with all pages. Distinguish scheduled tasks, to-dos, task templates and document-linked tasks.
2. Gather actual milestones, approved dates, working/calendar constraints, trade availability, sequencing and dependencies. Identify sources and unresolved conflicts privately. Do not invent durations, commitments, assignees or completion percentages, or equate a proposed date with an approved baseline.
3. The snapshot exposes `createTask`, `updateTask`, `copyTaskTemplateToTarget` and `createTasksFromBudget`; job schema exposes tasks. Task inputs include target, parent, dependency collections, assignees, start/end dates and times, baseline fields, progress and recurrence. `updateTask` additionally has dependent/recurring update controls; `updateJob` includes `scheduleIsPublished`. Inspect live types and supported template-copy/budget-generation behavior before using any of these. A budget is not automatically a feasible schedule.
4. Discover target enums, membership/task-type IDs, dependency direction/type/lag, calendar/timezone semantics, recurrence scope, propagation rules and notifications. Do not infer dependency payloads from field names or assume a task can move without downstream effects.

## Prepare and apply schedule changes

Produce a per-task before/after mapping covering hierarchy, dates, assignments and dependencies, plus downstream and recurring effects. Preserve baseline dates unless baseline revision is expressly authorized. Avoid cycles, duplicate template copies and accidental replacement of unrelated subtasks. Confirm whether dates are date-only or timed; never silently convert between them.

Follow the operating skill for authorization. A clear direct request covers the specified multi-task changes without repeat confirmation. Creation, moving dates, updating dependents, notifying assignees and publishing are distinct actions. Discover non-notifying controls rather than assuming defaults; do not publish simply because draft tasks were saved.

Apply in dependency order using confirmed IDs, saving responses privately. Read every affected task, downstream changes, recurrence instances and publication state back. Verify ordering, start/end logic, dependencies, assignees and baseline preservation. Reconcile uncertain results before retries. Report actual changes, publication/notification state and unresolved constraints; do not promise completion based on scheduled dates.

## Daily-log workflow

The maintained procedure is [jobtread-daily-logs](../../jobtread-daily-logs/SKILL.md). Load that module for daily-log intake, corrections, attachments and verification; there is no second daily-log policy here.

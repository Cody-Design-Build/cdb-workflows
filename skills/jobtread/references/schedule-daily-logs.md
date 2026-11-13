# CDB schedules and daily logs

Read [jobtread](../SKILL.md) and [query procedure](query-tool.md). These are conservative operational steps grounded in inherited schemas, not new CDB rules about working hours, sequencing, notice periods or reporting obligations. Discover exact current operations, fields, templates and notification defaults before use.

## Schedule intake and discovery

1. Match the job and requested scope: draft plan, task update, baseline change, publication or completion reporting. Read existing schedule/tasks, hierarchy, dependencies, assignments, dates/times, progress, recurrence, baseline and publication state with all pages. Distinguish scheduled tasks, to-dos, task templates and document-linked tasks.
2. Gather actual milestones, approved dates, working/calendar constraints, trade availability, sequencing and dependencies. Identify sources and unresolved conflicts privately. Do not invent durations, commitments, assignees or completion percentages, or equate a proposed date with an approved baseline.
3. The snapshot exposes `createTask`, `updateTask`, `copyTaskTemplateToTarget` and `createTasksFromBudget`; job schema exposes tasks. Task inputs include target, parent, dependency collections, assignees, start/end dates and times, baseline fields, progress and recurrence. `updateTask` additionally has dependent/recurring update controls; `updateJob` includes `scheduleIsPublished`. Inspect live types and supported template-copy/budget-generation behavior before using any of these. A budget is not automatically a feasible schedule.
4. Discover target enums, membership/task-type IDs, dependency direction/type/lag, calendar/timezone semantics, recurrence scope, propagation rules and notifications. Do not infer dependency payloads from field names or assume a task can move without downstream effects.

## Prepare and apply schedule changes

Produce a per-task before/after mapping covering hierarchy, dates, assignments and dependencies, plus downstream and recurring effects. Preserve baseline dates unless baseline revision is expressly authorized. Avoid cycles, duplicate template copies and accidental replacement of unrelated subtasks. Confirm whether dates are date-only or timed; never silently convert between them.

Obtain approval for bulk changes and external notifications/publication under the operating skill. Creation, moving dates, updating dependents, notifying assignees and publishing are distinct actions. Discover non-notifying controls rather than assuming defaults; do not publish simply because draft tasks were saved.

Apply in dependency order using confirmed IDs, saving responses privately. Read every affected task, downstream changes, recurrence instances and publication state back. Verify ordering, start/end logic, dependencies, assignees and baseline preservation. Reconcile uncertain results before retries. Report actual changes, publication/notification state and unresolved constraints; do not promise completion based on scheduled dates.

## Daily-log intake and discovery

1. Confirm job, local work date, author/source and whether creating a new entry or correcting an existing one. Read matching logs and attachments first; multiple logs on a date may be legitimate, so do not merge or deduplicate by date alone.
2. Gather observed work, locations, crews, deliveries, inspections, issues and photos only where supported by evidence. Separate observed facts from plans, reported statements and unresolved questions. Do not invent weather, attendance, safety compliance, inspection approval or completion. A log is not a substitute for a change order or a financial authorization.
3. The snapshot exposes `createDailyLog` with jobId, date, notes, assignees, customFieldValues, files and notify; `updateDailyLog` has id, jobId, date, notes and customFieldValues. Live-discover exact required inputs, field definitions/options, author/visibility permissions, attachments, notification behavior and supported correction route. Do not assume create-only files/assignees can be changed through the update operation.

## Save, correct and verify logs

Prepare factual notes and source-linked attachments. Verify customer/vendor visibility before including sensitive personnel or incident information. Preserve original evidence and distinguish work date from upload time. Resolve material ambiguity with the user rather than filling gaps with plausible text.

Apply only authorized changes; retain existing facts and attachment history when correcting a log. Bulk changes, deletion and notifications follow the operating skill's approvals. For files, complete upload and attachment, then verify downloadable bytes where possible. Do not silently erase an original narrative to make later reports appear contemporaneous.

Read back exact job/date/notes/custom values, files and any supported notification state. Confirm no duplicate entry arose after an uncertain response. Report created versus corrected logs, dates, attachments, what was sent and missing evidence. Never claim a site visit, inspection or delivery that was only scheduled.

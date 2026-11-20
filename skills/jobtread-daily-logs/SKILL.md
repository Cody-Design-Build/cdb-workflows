---
name: jobtread-daily-logs
description: Record and correct evidence-based daily site logs.
version: 0.1.0
author: David Cody, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [JobTread, Construction]
    related_skills: [jobtread]
---

# CDB JobTread Daily Logs

## When to use

Use for creating, correcting or reviewing daily logs, site notes and related attachments. Read [jobtread](../jobtread/SKILL.md) and the [query procedure](../jobtread/references/query-tool.md) before API work. This is factual reporting, not a timecard approval, inspection certificate, change order or authorization to send notifications.

## Daily-log intake and discovery

1. Confirm job, local work date, author/source and whether creating a new entry or correcting an existing one. Read matching logs and attachments first; multiple logs on a date may be legitimate, so do not merge or deduplicate by date alone.
2. Gather observed work, locations, crews, deliveries, inspections, issues and photos only where supported by evidence. Separate observed facts from plans, reported statements and unresolved questions. Do not invent weather, attendance, safety compliance, inspection approval or completion. A log is not a substitute for a change order or a financial authorization.
3. The snapshot exposes `createDailyLog` with jobId, date, notes, assignees, customFieldValues, files and notify; `updateDailyLog` has id, jobId, date, notes and customFieldValues. Live-discover exact required inputs, field definitions/options, author/visibility permissions, attachments, notification behavior and supported correction route. Do not assume create-only files/assignees can be changed through the update operation.

## Save, correct and verify logs

Prepare factual notes and source-linked attachments. Verify customer/vendor visibility before including sensitive personnel or incident information. Preserve original evidence and distinguish work date from upload time. Resolve material ambiguity with the user rather than filling gaps with plausible text.

Apply only authorized changes; retain existing facts and attachment history when correcting a log. Bulk changes, deletion and notifications follow the operating skill's approvals. For files, complete upload and attachment, then verify downloadable bytes where possible. Do not silently erase an original narrative to make later reports appear contemporaneous.

Read back exact job/date/notes/custom values, files and any supported notification state. Confirm no duplicate entry arose after an uncertain response. Report created versus corrected logs, dates, attachments, what was sent and missing evidence. Never claim a site visit, inspection or delivery that was only scheduled.

## Pitfalls

- The job's local work date is not necessarily the upload date. Resolve timezone and overnight work from evidence rather than assigning today's date.
- A planned task is not completed work; a delivery notice is not a received shipment. Attribute secondhand reports and retain uncertainty.
- Missing logs do not prove no work occurred. A date match alone does not identify a duplicate.

## Verification and handoff

Read each exact created/corrected ID back and compare job, date, narrative, author where exposed, fields and all intended attachments. Verify no unrelated facts or original files were lost. Report created/reused/corrected logs, evidence gaps and notifications actually sent. Leave unsupported actions blocked rather than inventing a successful log entry.

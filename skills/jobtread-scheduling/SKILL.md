---
name: jobtread-scheduling
description: Build and revise JobTread schedules in full-week blocks.
version: 0.1.0
author: David Cody, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [JobTread, Construction, Scheduling]
    related_skills: [jobtread]
---

# CDB JobTread Scheduling

Build or revise a trade schedule in JobTread. This is a planning workflow, not a crew booking, notice to proceed, or automatic scheduling service. Use the authenticated JobTread MCP and follow the [operating skill](../jobtread/SKILL.md), [query procedure](../jobtread/references/query-tool.md), and [schedule API and approval rules](../jobtread/references/schedule-daily-logs.md).

## Procedure

1. Match the exact job and revision; enumerate the live tasks, groups, publication state and every page. Snapshot task IDs, hierarchy, dates/times, baseline, assignments, progress and dependencies privately. Reuse budget-imported tasks by ID; don't import again or duplicate existing work. Distinguish undated exclusions, phase headers and actual work rows.
2. Anchor planning to consecutive Sunday–Saturday calendar blocks. If the agreed field start is Monday, the first block starts the prior Sunday; that calendar boundary is not a direction to work Sunday. Use inclusive Saturday end dates. Calculate ranges with `scripts/week_blocks.py` via `terminal`; verify the target date and count. Multiweek activities can span consecutive blocks; leave generic overhead/admin undated unless requested.
3. Sequence real construction: identify prerequisites for site access, underground work, pours, curing, dry-in, rough inspections before cover, finish installation and final inspections. Put known overlaps on separate rows or agreed ranges. Distinguish assumed planning durations and lead times from supplier, utility, permit and inspection commitments. Keep the first pass date-driven; do not add dependencies just to draw Gantt links. For repeated rough/trim visits within one imported trade row, show the intended windows in the private plan, or propose separate tasks if the user wants each visit on the calendar.
4. For revisions, calculate the named task or phase move in whole weeks; show all affected rows and changed dates, and separately identify handoffs that need moving. Never silently shift downstream/recurring work or reset a baseline. Existing dependencies require a propagation check even if the plan adds none.
5. Prepare an exact per-task mapping, including proposed additions, before a multi-task write. Follow the operating skill: a clear direct request is sufficient; show a preview and ask only if a material decision remains unresolved. Keep the draft unpublished, unassigned if no crew is named, unnotified, and free of new dependency links unless explicitly authorized. Discover live operations and set notification and downstream/recurrence controls explicitly where supported.
6. Read affected IDs and the schedule back after saving. Verify inclusive blocks, unchanged hierarchy/baseline/assignments/dependencies, skipped rows, and publication state; verify no duplicates. Reconcile uncertainty before retrying. Report the planning end date and material constraints without promising that any inspection, delivery, or finish is confirmed.

## Pitfalls

- A budget list is a scope inventory, not a sequence. Do not infer a Saturday workday or holiday shift from a full-week block.
- Do not invent dates for third-party prerequisites, or use a broad trade bar as a continuous staffing commitment.
- For holidays, leave the calendar blocks aligned and flag lower assumed production or access; do not silently change the calendar boundary.

## When to use

Use for draft construction schedules and explicitly requested task/date revisions, not automatic crew booking or publishing.

## Verification

Read every affected task back and reconcile the complete ID set, inclusive Sunday–Saturday blocks, intended sequencing, preserved baselines/assignments/dependencies and publication/notification state. Report actual saved dates and unresolved third-party commitments separately.

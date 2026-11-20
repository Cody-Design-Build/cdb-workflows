---
name: jobtread-catalog-standards
description: Maintain reusable CDB cost-catalog scope safely.
version: 0.1.0
author: David Cody, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [JobTread, Construction]
    related_skills: [jobtread]
---

# CDB catalog standards

Load alongside [jobtread](../jobtread/SKILL.md) and [jobtread-budget-writing](../jobtread-budget-writing/SKILL.md) when planning catalog work.

## User-stated conventions

- Keep generic catalog templates free of standard monetary amounts and inherited project-specific quantities. David wants a standardized scope library rather than old estimates copied into templates. Verify blank-versus-zero behavior before applying changes; neither is assumed to prevent an unpriced proposal.
- Keep names and descriptions simple and scope-focused. Maintain warranty durations and general contract terms in the separately reviewed proposal/contract, not catalog descriptions. Preserve necessary inclusion boundaries and supply/install responsibilities.
- Do not preserve legacy catalog records for their own sake. Existing content is source material for understanding estimating intent; a clean rebuild is acceptable. Obtain explicit approval of exact targets and consequences before deleting groups or multiple items.

## Operational reference

For vendor documents, budget-item allocation, compliance, attachments and payments, load the maintained [vendor workflow](../jobtread/references/vendor-orders-bills-payments.md). Do not maintain a second financial procedure here.

Catalog records are reusable scope definitions, not live job budget records or approved customer baselines. Use [budget intake](../jobtread/references/budget-data-intake.md) when applying scope to a job; confirm target and approval before changing structure or financial values.

## When to use

Use for reusable catalog scope maintenance, not job-specific pricing or customer contract changes.

## Pitfalls

A catalog template is not an approved customer baseline. A rebuild requires scoped deletion authorization; never infer that from a naming cleanup.

## Verification

Read exact changed records and all affected children back, compare scope and blank/zero financial behavior, verify no project quantities/rates leaked into templates and no live budget or issued document changed unintentionally. Report removals and unresolved pricing separately.

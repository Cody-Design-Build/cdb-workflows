---
name: jobtread-budget-writing
description: Write clear CDB budget scope and customer descriptions.
version: 0.1.0
author: David Cody, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [JobTread, Construction]
    related_skills: [jobtread]
---

# JobTread Budget Writing

**These are general budget-writing preferences for all new CDB budgets. This skill contains no job-specific scope, exclusions, pricing decisions or project history. Keep those in the relevant project's records, not in this skill.**

Write readable, customer-facing CDB budget scope and group summaries. This skill is the maintained home for terminology, owner-paid planning figures, allowance wording and customer price rounding—not estimating approval or authentication. Use [jobtread](../jobtread/SKILL.md) for discovery, authorization and readback, [budget intake](../jobtread/references/budget-data-intake.md) for source-to-record preparation, and [customer documents](../jobtread/references/customer-documents.md) for proposals and change orders. For developing scope and pricing, load [jobtread-estimating](../jobtread-estimating/SKILL.md) when installed; otherwise identify that missing module before claiming estimating completion. Wording cleanup alone does not require it.

## Sales-first tone

- Treat the budget as a sales tool as well as an accurate statement of scope. Make it welcoming, confident, readable and focused on the work and value CDB will deliver.
- Avoid defensive, adversarial or cover-yourself language. Long exclusion lists and repeated caveats can signal uncertainty or unwillingness to help; do not make them the customer's main impression.
- Lead with positive, specific scope. Where accurate, describe what is being retained, repaired or installed rather than listing every possible upgrade not included. Do not invent free services or open-ended commitments to extra work.
- Use an explicit exclusion only when leaving it unstated would materially mislead the customer about the agreed scope. Prefer a concise, neutral clarification where it communicates the same boundary accurately. Do not hide material omissions or remove an agreed scope limit just to sound friendly.
- Raise unresolved estimating questions privately rather than exporting uncertainty into repetitive customer-facing caveats. Present necessary preliminary-pricing qualifications once, clearly and calmly.

## When to use

Creating or reviewing budget item names, descriptions, cost-group headers, inclusions, exclusions, preliminary-pricing qualifications and customer proposal language.

## Terminology

- **Cost**: what the work costs CDB.
- **Price**: what CDB charges the customer.
- **Allowance**: in David's terminology, money set aside as a spending marker, not money CDB invoices for. Typically appliances, fixtures, finishes, tile, cabinetry, windows or doors. Do not label estimated trade work an allowance merely because details or pricing are provisional. Do not alter JobTread allowance settings or financial treatment as part of wording cleanup; ask when commercial treatment is unclear.

## Separate selected products from installation

- Where an owner-selected product has installation work, separate the product planning allowance from CDB's installation item. Installation includes labor and necessary rough installation materials, not the selected fixture/product itself.
- Preserve quantities, opening schedules and technical requirements when splitting existing packages. Do not infer a product/install cost breakdown from a bundled price without identifying it as a proposed allocation and checking adequacy.
- Confirm product unit allowances, applicable counts, interior/exterior classifications and hardware responsibility before reallocating money. Project-specific unit amounts belong in project records, not this general skill.
- Do not automatically apply markup when splitting a zero-markup package; confirm the desired installation pricing treatment separately.

## Owner-paid expenses and planning figures

- Do not put owner-paid expenses into ordinary priced contract items: they can become amounts due to CDB. Equal cost/price does not make an item nonbillable.
- An available presentation approach is a customer-facing Other Project Expenses note or a zero-dollar informational item, with estimated owner-paid amounts written only in the description. These figures are planning guidance, not amounts payable to CDB or automatically JobTread allowances. Use only with approved project-specific responsibility and payment terms.
- Clearly distinguish owner-paid planning figures from the CDB contract price. Explain that the owner pays the agency/provider directly, actual charges may vary, and CDB's coordination assistance is limited to the assistance actually agreed. Avoid defensive 'not responsible for anything' language or promises to handle unapproved work.
- Verify the actual proposal preview, totals and invoicing behavior before relying on a zero-dollar item. Zero dollars does not stop descriptive promises from becoming contractual obligations. Do not assume a description/footer is displayed on the signable document or that the software supports a noncontract informational section without checking.
- Do not default to native JobTread allowance functionality just to display owner-paid planning figures. Confirm the intended treatment before changing financial fields or allowance settings.

## Customer-facing price rounding

- Round extended customer estimate prices upward to the next $10; leave exact multiples and zero-price informational items unchanged. Do not round down and lose price. Apply this to the budget in scope, not unrelated jobs or issued documents.
- Preserve authorized markup percentages by recalculating internal unit costs where that is the approved pricing workflow. Internal costs may retain precision; do not claim both costs and prices are whole tens when only prices are rounded. Verify totals and disclose any increase.

## Line items

- Keep names short, concise and scope-specific.
- Default to one short sentence stating the work and referring to the plans instead of repeating product names, materials, or assembly details already shown there. Use “according to the attached plans” only when the applicable plan set is actually attached; otherwise refer to the project plans without calling them attached. Keep explicit labor and supply responsibilities, scope limits, and agreed requirements or exceptions the plans alone do not communicate. Keep detailed quantities and takeoffs in working records unless needed in the customer scope.
- Describe trade work by practical coverage such as 'new and affected areas' when that accurately captures the approved scope; avoid unnecessary room-by-room inventories or individual runs. Retain material scope boundaries that prevent a misleading promise, and keep detailed takeoffs in project working records rather than customer-facing descriptions unless needed.
- Descriptions are forward-facing sales and signable contract wording, not notes to David or an agent. State the actual work directly, preferably in inclusion bullets instead of long comma-separated lists.
- Preserve quantities, dimensions, specifications, scope limits, supply/install responsibility and meaningful qualifications. Do not expand scope or turn provisional work into an unconditional commitment while simplifying.
- Determine inclusions, exclusions and responsibilities from each project's approved scope. Do not carry one project's decisions into another or treat a temporary exclusion as a permanent company rule. Distinguish design services from installation, field verification, coordination, inspections and testing; include or exclude each only as authorized for the relevant budget.
- Use exclusions sparingly, only for material scope boundaries a customer could reasonably misunderstand. An exclusion section is not required on every item. State job-wide exclusions once in the customer-facing overall scope or appropriate common section, not repeatedly on individual items.
- Work included elsewhere in the budget is not an exclusion. Omit redundant cross-references or, when genuinely useful, identify the responsible package in ordinary scope text rather than under Exclusions. Never label included scaffolding, testing, framing or similar work as excluded merely because it belongs to another package.
- Retain genuine, specific exclusions where needed to avoid expanding the agreed scope. Put those at the bottom under a bold **Exclusions** heading with bullets; omit the heading when there are no necessary item-specific exclusions. Check that exclusions do not contradict inclusions.
- Never include removed-item history, bookkeeping explanations, agent commentary, editing instructions, reconciliation TODOs, or reminders such as 'the former budget line was removed and current coverage needs confirmation'. Express the actual boundary instead: 'Geotechnical observation' under Exclusions.
- Keep internal questions and change history in separate private working notes or a field whose privacy has been verified. Do not create or assume a private field without checking permissions and customer-document visibility. Ask David when a material unresolved scope decision cannot be accurately expressed.

## Cost groups / headers

- A cost group is principally a container for its items. Its description may be empty when no helpful summary is needed.
- When useful, use a short prose sentence describing the work inside the group, not a bullet-point task list or a duplicate of every item's scope.
- Group descriptions are also customer-facing. Do not add internal housekeeping, deleted-budget history or agent reminders.
- For a genuine customer-facing qualification, put **Note** on its own line, then a concise explanatory paragraph. Bold only the word Note, not the paragraph. Distinguish a customer-facing qualification from an internal follow-up task.
- When pricing depends on incomplete plans, selections or technical requirements, describe that dependency and its possible effect on pricing in plain customer-facing language. Do not invent responsibility assignments or exclusions.
- Examples illustrate formatting only; they never establish scope or exclusions. Keep actual project-specific notes and decisions in project records.

## Editing workflow

1. Read the exact job, all affected items/groups, and pagination. Understand scope and prior approved changes before editing.
2. Snapshot names, descriptions, IDs and financial/allowance fields. Separate editorial changes from scope/pricing decisions.
3. Write an explicit per-record mapping. Preserve intent and avoid invented decisions. Use concise prose for group summaries and inclusion/exclusion bullets for line items.
4. Apply only approved fields; do not delete, merge, change financial values, or rewrite issued/accepted documents under a wording-cleanup request. Follow the operating skill's approval rules for those actions.
5. Read every target back and compare unrelated fields programmatically. Check no scope/qualifications were lost and that customer text contains no housekeeping notes.
6. Report edits, unchanged financials, and material decisions still needing David outside the budget description.

## Verification

- Names are concise; item descriptions state the work and retain necessary technical scope.
- The budget reads as a friendly, confident sales document, not a defensive list of limitations. Explicit exclusions appear only where materially necessary; when used, put them at the bottom under a bold Exclusions heading with bullets.
- Group descriptions are short prose or intentionally blank; any Note is relevant to the customer and accurate.
- No internal reminders or removed-item history appears in customer-facing descriptions.
- Costs, prices, quantities, formulas, allowance treatment and record structure remain unchanged unless separately authorized.

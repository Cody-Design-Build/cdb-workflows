# CDB proposals, preliminary proposals and change orders

Read [jobtread](../SKILL.md), [budget intake](budget-data-intake.md) and [budget writing](../../jobtread-budget-writing/SKILL.md). Drafting, approval, signatures and sending are separate states. This reference supplies a conservative process, not new CDB payment, markup, deposit, expiration or legal terms.

## Discover the actual workflow

1. Match organization, job, customer account/contact, location and intended document purpose. Read all relevant proposals, accepted customer orders, revisions, change orders, invoices and references, with pagination. Identify duplicates before creation.
2. Discover live document types, template inventory and full selected template content/defaults, exact create/update/conversion operations, line-item inputs, recipient/signature operations and status transitions. The snapshot exposes `createDocument`, `updateDocument`, document templates/references/recipients and `sendDocument`; it does not establish a dedicated proposal or change-order mutation. Do not invent one or assume UI labels equal API enum values.
3. Identify the template by ID, name, templateName, type and matching terms. Read default details/footer, signature settings, tax, due terms, visibility and any scheduled payments. API creation inputs can require location and dueDate/dueDays even when the UI fills defaults. Use the live template's approved defaults; do not invent terms to satisfy validation or silently strip contractual language. Discover whether the supported route copies a template or requires explicit values; the snapshot alone does not guarantee a template-ID argument.

## Prepare the correct document

- **Proposal:** reconcile the approved scope and estimate against the exact items to present. Confirm selected alternatives, product/install boundaries, allowances, owner-paid planning figures, tax and customer totals. Preserve job/source item links using the supported route. A document copy and a live job-budget item are not interchangeable.
- **Preliminary/development proposal:** explicitly identify the actual pricing maturity and dependencies on incomplete plans or selections, using approved factual qualifications. Discover the organization's matching template; do not assume it shares the final proposal footer. Do not invent a nonbinding disclaimer, exclusion, commitment, contingency, fee or future-price guarantee. Resolve material uncertainty with David before issue.
- **Change order:** read the accepted original scope and every applicable accepted change first. Prepare an auditable delta with additions, removals/credits, affected quantities, price/tax and any authorized schedule effects. Discover the organization's supported document type, references/conversion route and baseline inclusion behavior. Do not bill the whole contract again, overwrite the signed original, double-count a prior change, or represent proposed changes as approved. Resolve whether the task is a draft, signed change, absorbed internal cost or customer charge.

Snapshot `createDocument` includes `lineItems`, `references`, `includeInBudget`, location, tax and signature settings; `updateDocument` includes status/notify. Their exact types, side effects and current availability require live introspection. Do not toggle inclusion or approval to manufacture a baseline. Do not assume a draft proposal changes approved Budgeted Cost.

## Review, issue and verify

1. Prepare an exact draft and record mapping with totals and template identity; obtain target/content approval before financial or external-facing changes. Save existing values privately for a revision. Reusable contract wording changes belong in the separately approved template, not silently in issued snapshots.
2. Create or update only through the supported route. Preserve footer/details/signature defaults unless expressly authorized otherwise. Read every line, source link, total, tax, status and template-derived text back. Inspect the actual preview/PDF to verify grouping, hidden costs, notes, exclusions, zero-dollar figures and signable content. Do not assume a saved field appears on the document.
3. Confirm exact recipients, message, attachments and signature requirements before authorized send. The snapshot's `sendDocument` takes a document-recipient ID; discover how that recipient is created/resolved and what sending triggers. No unauthorized notification, simulated signature or inferred acceptance.
4. Read the final document, delivery/signature state and any baseline effect back. A send response is not proof of delivery or signature; approval is not proof someone signed. Reconcile timeouts rather than sending twice.
5. Report document ID/number, type/template, created versus revised state, totals/delta, approval/signature status, what was actually sent and remaining blockers. Leave issued originals and unrelated templates unchanged.

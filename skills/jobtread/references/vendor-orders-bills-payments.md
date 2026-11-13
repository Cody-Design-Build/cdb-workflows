# CDB vendor orders, bills and payments

## Purpose and trigger

Use this procedure whenever David asks to accept a subcontractor bid, create/approve a vendor order, make a vendor bill, or record/apply a vendor payment. Spoken 'vendor build' usually means vendor bill; resolve from context rather than silently changing the request to order-only. This reference belongs to the shared jobtread skill, not an independent competing skill.

## Business workflow

1. **Bid request (optional):** asks a vendor to price a scope. A bid may arrive outside JobTread. Do not require or create a bid request merely to proceed.
2. **Vendor order:** records the accepted scope and commitment; for subcontracted work it serves as the work order/subcontractor agreement. Use the organization's appropriate current agreement template, not a generic Purchase Order stripped of its terms. Read template content, scope, parties and attachments before creating.
3. **Acceptance and signatures:** David can explicitly direct manual approval; otherwise prepare the agreement for the required parties to sign. An API status of approved is not proof that anyone signed, nor an agent determination of legal enforceability. Never simulate a signature or mark signed without evidence. Preserve the contract's signature requirements unless David explicitly approves an exception. Sending/signature requests require explicit authorization of recipients and content.
4. **Vendor bill:** after the order is accepted/signed or explicitly manually approved, create the bill from or linked to that order, preserving budget-item links and the correct billed amount. A vendor order alone does not satisfy a request for a bill. Do not require a bid request in this step.
5. **Payments:** payments are made outside this recording workflow through Trust Payments, per David. Current recording is manual; entering a payment in JobTread must not initiate another payment. Apply each recorded payment to the correct vendor bill and verify the resulting paid amount and balance.

## Vendor compliance and worker treatment

- Before authorizing/releasing payment for subcontracted work, verify proof of insurance naming CDB as required by its agreement, W-9, and applicable contractor licensing. Read actual documents/current expiration dates; a vendor account existing in JobTread or an approved order is not compliance evidence.
- David's policy is to use properly documented licensed subcontractors; workers who are employees must be on payroll ('on the books'), not paid off the books through vendor bills. Do not treat this shorthand as a legal classification test: licensing alone does not establish independent-contractor status, and a missing license does not automatically establish employee status. Flag uncertain classification for David/payroll/professional review rather than decide it yourself.
- Distinguish a compliance check before a new disbursement from bookkeeping for a payment David already made. Record authorized historical facts accurately, but flag missing compliance rather than invent documents or claim payment-ready status. Never represent bookkeeping entry as permission to release funds.

## Operating procedure

### 1. Discover, match and prevent duplicates

- Load jobtread SKILL.md and references/query-tool.md; introspect unfamiliar live schemas. Confirm organization, exact job, vendor account, scope and amount. Similar vendor/contact names are not interchangeable accounts.
- Read all relevant existing bid requests, vendor orders, bills, document references, budget cost items, payment records and document-payment allocations. Paginate completely and save multi-record results locally.
- Distinguish actual budget items (no document) from document copies. Match jobCostItem links, not name alone.
- Reuse a matching approved order or existing bill; do not recreate it. Search payments by vendor, authorization/reference, amount and date to avoid duplicate entry.
- State the requested end state explicitly: order only, bill only, order plus bill, or payment recording. A request to duplicate an established order-and-bill workflow includes both. Do not silently narrow it to order-only. A genuinely ambiguous scope requires one focused clarification.

### 2. Prepare the accepted vendor order

- Locate and attach the subcontractor's accepted bid/proposal and relevant scope attachments to the vendor order whenever available, including bids received outside JobTread. Verify the vendor, job, amount and accepted revision before attaching; inspect existing order files to avoid duplicates. Preserve original bytes and prior revisions, and clearly identify the accepted version.
- If no downloadable bid/proposal is available, retain a source reference when possible and report the missing attachment; do not fabricate a proposal or claim it was attached. An attachment alone is not proof of acceptance, signatures or incorporation into the agreement. Flag conflicts between proposal and order terms for review.
- Read the vendor order's files back and verify the accepted bid/proposal attachments; compare downloaded bytes with the originals when possible.
- Preserve the accepted scope and source bid/invoice files. Do not invent specifications or replace contract wording with a generic sentence while implying a complete subcontract agreement.
- Allocate line amounts to the appropriate existing budget items. Keep one vendor total even when split across multiple scope lines. Do not invent room allocations or budget baselines.
- If no matching budget item exists, inspect approved scope before creating another. Absorbed costs do not authorize customer charges or changes to signed proposals. Ask for a classification/allocation decision when material.
- Native Budgeted Cost derives from approved customer orders; a working-estimate edit is not an approved baseline. Never manufacture customer approval to hide an absorbed variance.
- Read the live document template and use its appropriate terms/defaults. The raw createDocument API may require jobLocationName/address and exactly one of dueDays/dueDate; the UI may supply these implicitly. Read existing defaults rather than claim the user must invent terms. Do not carry stale source-document dates into new documents.
- Create, read back, then manually approve only if authorized; use notify:false for non-notifying status updates. Re-read approved status and signature state separately. Otherwise leave the requested review/signature workflow intact.

### 3. Create or reconcile the vendor bill

- Preserve all default template values whenever working with documents, including default details, footers, contractual terms, and signature settings. Read the selected live template and retain its defaults; never blank, replace, or suppress them merely to avoid adding commentary. Do not add agent-written content to Bill Details (`description`) or any document footer (`footer`) unless David explicitly directs it. If the template leaves these fields blank, leave them blank; if it supplies content, preserve that content unchanged. On existing documents, leave these fields intact unless directed. Verify readback against the template defaults and authorized edits, not against a blanket blank-field rule.
- Discover the supported conversion/create route. Link the bill to its vendor order using document references, and link cost lines to the exact job budget item(s). For existing bills, add the missing order relationship instead of creating another bill.
- Verify sourceCostItem relationships when the native conversion workflow requires them; a document reference alone does not prove every native conversion/accounting behavior. Do not claim a conversion occurred if the operation merely added a reference.
- Enter vendor cost without customer markup. Distinguish total contract commitment from actual vendor progress invoices: a full-value bill is appropriate only when David explicitly requests that arrangement. When invoice documents show partial billing, disclose the basis; do not create additional progress bills that double-count an existing full-value bill.
- Preserve invoice numbers, dates and due terms from actual invoice documents where applicable. Do not mistake invoice date for payment date.
- Read back exact vendor, job, type, status, amount, tax, order references and all budget links. Report bill number/ID, not only order status. Draft/pending/approved are distinct; do not issue or approve a bill by assumption.
- Establish the supported editing route before reverting an approved order or payable bill to draft. Approval restoration may require signatures; draft/edit/restore is not inherently reversible. Preserve signatures and payment allocations and report incomplete state rather than bypassing validation.

### 4. Download and attach evidence

- Retrieve original invoice PDF attachments from email; verify vendor, invoice number, project and amount. Preserve original bytes and invoice versions. An invoice requesting payment is not payment confirmation.
- Current fileTargetType supports documents but not payments. Attach invoice files to the corresponding vendor bill; put invoice/authorization numbers and evidence references in payment descriptions. Re-discover if capability changes.
- Use createUploadRequest -> actual byte upload with returned method/headers -> createFile targeting the bill. A successful upload request alone is not an attachment.
- Read the bill's files back, verify names/size and, when downloadable, hash-compare remote bytes to the originals. Keep temporary signed URLs/credentials out of the final report and skill.

### 5. Record and apply historical payments

- Record only with David's authorization. Obtain amount, bill, payment date and available reference from David or confirmation evidence. Match the confirmation to the invoice/job; do not assign by amount alone.
- Payment dates matter; payment times do not. Never request, research or report transaction times as a payment-recording requirement. When using confirmation emails, use the payment date stated in the confirmation or derive the local America/Los_Angeles date from its Date header if needed; do not substitute the invoice date or current date.
- The API requires paidAt as a datetime: use midnight America/Los_Angeles on the confirmed payment date, converted with the correct daylight-saving offset. This is a technical date placeholder, not a claimed transaction time. Do not add repetitive time-unknown caveats to payment descriptions or reports; display dates only. Preserve original confirmation evidence separately.
- Preserve both user-reported payment platform and documentary evidence if they differ. Do not fabricate a Trust/Truss integration transaction ID, overwrite external-provider fields or claim bank settlement from an email receipt.
- Current API uses createPayment (vendor outflow type debit, positive amount, paidAt, accountId, source/description/externalId) then createDocumentPayment (paymentId, documentId, amount, isLinkedToQbo:false unless actually linked). Re-introspect before use. attemptAutoMatch:false avoids unintended allocations.
- Read back the payment immediately after creation, then apply to the bill and read back allocations. Assert amount, confirmed local payment date, vendor, applied/unapplied amounts, target bill, and final bill paid total/balance. Never create an additional payment to correct an uncertain allocation.
- Recording a payment may change document status. Preserve legitimate existing status changes; do not blindly reset to draft.

## Recovery and verification

- Persist each mutation response before the next dependent step. Create results are nested (e.g. createPayment.createdPayment.id and createFile.createdFile.id). A local parsing exception after a successful write is not evidence the write failed.
- After timeout/error, inspect the exact remote target and saved journal before retrying. Resume from confirmed state; no rerunning an entire creation loop blindly.
- Verify the complete requested chain: vendor + job + approved order (when requested) + bill + budget links + invoice attachments + each payment allocation. A successful order is not a completed bill workflow.
- Final report: what was created versus reused, bill/order identifiers, approval/signature distinctions, amounts paid/balances, evidence attached, and anything incomplete. Say whether documents were sent or money moved. Never claim signatures/compliance checks that were not performed.
- Keep transaction IDs, job-specific decisions, raw email bodies and task progress in task evidence, not in this reusable reference.

## Preserve trade budget structure

1. Read all actual trade budget items, including room-specific lines and separately grouped service work; exclude document copies and confirm covered scope.
2. Assemble one subcontract agreement from all covered existing items across groups. Per-line budget links do not require a redundant consolidated budget item.
3. Prefer the accepted bid breakdown. If David accepts proportional internal allocation of a lump sum, weight covered items by existing estimated cost, use decimal arithmetic, round to cents and reconcile the residual deterministically to the agreed total. Label this internal allocation, not vendor-quoted pricing. Ask only when scope or weighting is genuinely unresolved.
4. Carry every covered budget-item link and allocated cost into the bill and reference the approved order. Verify the full ID set and total. Leave original customer budget amounts and signed documents unchanged.
5. After document cleanup, rediscover orders, bills, unapplied payments and allocations before replacements. Removed bills do not prove historical payments were removed.

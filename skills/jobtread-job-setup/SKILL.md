---
name: jobtread-job-setup
description: Set up CDB jobs, owners, property and plans.
license: MIT
metadata:
  author: Cody Design Build
  version: "0.1.0"
---

# CDB Job Setup

## When to use

Follow this procedure whenever asked to create, onboard, or complete setup of a CDB job, including a lead. It applies even when someone has already created part of the customer, property, job or folder. Use [jobtread](../jobtread/SKILL.md) for live schema discovery, permissions and write verification. This procedure does not authorize sending invitations, proposals or email, establishing financial terms, or changing an existing job's stage without direction.

## 1. Discover and assemble intake

- Verify the connected organization and permission grant. Inspect the current schemas for accounts, contacts, locations, jobs, files and plans before constructing requests.
- Search existing jobs, locations, accounts and contacts by address, names, email and phone. Paginate all relevant results. Reuse a confirmed match; never create a duplicate because only the job name differs. If the user says a job exists but lookup fails, broaden the search and reconcile before creating.
- Read relevant authorized email threads, attachments, linked documents, existing records and user-provided information. Follow the installed email integration's rules; never send mail or invite anyone just to complete intake. Missing integrations are a blocker for that source, not permission to invent data.
- Build a private intake summary with source references and confidence for each fact. Keep private intake, real identifiers, source emails and business files out of this public repository.

Required intake:

| Area | Information to establish |
| --- | --- |
| Customer | Account display name; individual, household or entity; all known owners' full names; primary contact |
| People | Each person's role, email and available phone; whether additional owners or decision makers are known |
| Property | Full street address, city, state, postal code and applicable unit; distinguish job site from mailing address |
| Job | Short scope description, proposed name, intended stage and existing records to reuse |
| Documents | Available plans, architect/source, issue date, revision and source location; whether a later set exists |
| Related parties | Architect, designer, referral source and other known project contacts, distinct from owners |
| Filing | Existing Dropbox job folder, stage and current folder convention; any installed folder-setup procedure |

Names and email handles are not interchangeable: do not expand a nickname into a legal name from an email address. An architect listed on plans is not an owner. A referral is not automatically a customer. Preserve roles when dictated speech is ambiguous; clarify contradictions rather than silently swapping roles.

**Completion:** each field is sourced, user-confirmed, not applicable, unavailable, or explicitly unresolved.

## 2. Resolve gaps and approve the mapping

- Ask one batched set of questions covering material missing or contradictory information. Accept answers through chat or the user's supported intake surface; do not require a new form or integration.
- Ask whether additional owners are known; one known owner is sufficient to proceed when the user confirms that is all currently known. Add other people later without replacing or duplicating existing contacts. Available phone/email are desirable, not grounds to fabricate values or stall an explicitly authorized partial setup.
- Use the job naming convention **address - short scope**, with a short street-address label in the job name and the complete address on the location. Validate against the live API's length constraint before submitting. If the approved name is too long, propose a shorter name and obtain approval; never silently truncate an approved name.
- Preview account, owner/contact roles, location, job name, proposed stage, plans and folder actions. Execute clear, authorized setup actions without redundant confirmation; obtain a decision for ambiguous identity, naming, sharing or commercial choices. Do not treat silence or a timed-out question as approval.
- Use the discovered job-stage custom field rather than assuming a built-in status. New-job setup does not imply Won, contract acceptance, a price type, tax exemption or published schedule. Confirm material commercial choices; preserve existing settings on reused records.

**Completion:** approved mapping and an explicit list of deferred gaps; blocked steps do not prevent safe independent work already authorized.

## 3. Create or complete the records and filing

1. Create/reuse the customer account. Record referral source in the appropriate discovered fields. Suppress notifications unless separately authorized; inspect mutation defaults.
2. Create/reuse each known owner's contact with available verified email and phone. Establish primary contact through the supported relationship. Keep architect/designer/referral roles separate; use supported project/account contact relationships, not a fabricated ownership role or unnecessary duplicate customer account.
3. Create/reuse the property location under the correct customer and link the primary contact where supported. Verify the address and account relationship before creating the dependent job.
4. Create/reuse the job with the approved name and stage. Read back each mutation separately before using its ID. Do not copy budgets, tasks or financial terms from another job unless requested. Record unresolved setup facts privately in an appropriate verified field or handoff, not customer-facing scope.
5. Retrieve plans from their authorized source. Inspect content sufficiently to verify property, issue/revision and page count. Preserve original bytes and filename unless a rename is approved. Compare existing files/sheets before uploading to avoid duplicate sets. Distinguish upload success from attachment and plan-sheet creation: discover upload request → returned byte-transfer method/headers → file attachment → plan sheets. Never call a Files-only attachment a completed Plans upload. Do not guess measurement scales while setting up sheets.
6. Verify remote file metadata and original downloadable bytes where available; compare hash/size with the source. Verify all expected plan pages and revision identity; reconcile processing delays or partial page creation before retrying. Preserve prior issued revisions rather than overwriting them silently. Keep signed upload/download URLs private.
7. Create or reconcile the Dropbox job folder using the installed folder-setup skill and the current approved convention. Reuse an existing lead folder. Inspect the live tree rather than blindly following an archived folder numbering scheme. If no authoritative folder procedure/destination is available, ask; do not invent a permanent structure. Confirm before moves, renames or deletions. Add cross-links where supported without creating parallel trackers.

**Completion:** every created/changed record is read back, relationships are correct, plans are usable in Plans, and the requested folder/files are verified. Resume from verified IDs after interruption; reconcile uncertain writes before retrying.

## Pitfalls

- Partial setup is not failure, but must not be reported as complete: an account/contact/location without a job or a file without plan sheets remains partial.
- Phone normalization may change formatting; verify the underlying number. Do not overwrite conflicting existing contact details without resolving them.
- A new-job request is not permission to email the customer, publish a schedule, share Dropbox, issue documents, set a contract value or delete records.
- No private customer facts, captures, credentials or job-specific exceptions belong in this reusable skill. The design-folder workflow is separate and should only be invoked once defined and installed; do not pretend it exists.

## Verification and final handoff

Return four concise sections, with record links/IDs only in the private user handoff:

1. **Customer and people:** account, primary owner, other known owners, contact details and architect/referral roles verified; unknowns named.
2. **Property and job:** exact address, job number/name, customer/location links and stage verified; no unintended financial, closure or notification changes.
3. **Plans and Dropbox:** source/revision, file and expected page counts, actual Plans availability, folder path and cross-links verified; sync limitations disclosed.
4. **Open items and next step:** deferred information, blocked actions, decisions needed and setup completeness. Never report a planned upload or missing job as done.

---
name: cdb-dropbox-management
description: Manage CDB Dropbox job folders and project files.
license: MIT
metadata:
  author: Cody Design Build
  version: "0.1.0"
---

# CDB Dropbox Management

## When to use

Use for creating or reconciling CDB job folders, filing plans and incoming documents, finding project files, preserving revisions, and authorized stage moves. During job onboarding, coordinate with [jobtread-job-setup](../jobtread-job-setup/SKILL.md); this skill owns Dropbox filing, not customer records, financials or JobTread stage decisions.

## Discover the destination

- Discover the actual Dropbox team root through the authorized connector or local synced folder. Do not hardcode a user's home path or assume the folder is literally named Dropbox. Installation of these instructions does not authorize Dropbox or configure sync.
- Read applicable root/folder instructions and inspect the current live tree. Search all job stages by address and known job labels before creating anything. Reuse a confirmed project; do not make a second folder merely because the JobTread scope suffix differs.
- The approved CDB job tree is relative to the team root:

```text
02 - jobs/
  01 - leads/
  02 - active/
  03 - closed/
```

- If the live structure or applicable instructions differ, reconcile before writing. Archived system folders and old five-folder templates are not the current standard. Do not create missing top-level infrastructure without approval.

## Create or reconcile a job folder

1. Confirm the property and intended filing stage from the job intake. Do not infer active status from an inquiry or an estimate; Dropbox stage and JobTread stage require an explicit mapping, not automatic mirroring.
2. Name the folder with the short street address, optionally an approved city or distinguishing description. Keep the full property address in JobTread. Ask if no address is known or two jobs at the same address cannot be distinguished.
3. For a requested new-job setup, create only the job folder and these six standard children, with no-overwrite behavior:

```text
01 - customer orders
02 - vendor orders
03 - plans & design
04 - procurement
05 - trade partners
06 - permits & compliance
```

4. Reuse existing children. Report missing or nonstandard folders rather than renumbering or merging them silently. Additional estimating/design structures require approval or a separately defined workflow; do not invent them here.
5. Do not add Markdown databases, index files, contact records or parallel procurement/task trackers. Cross-link the verified folder and JobTread job in supported existing fields when authorized; never fabricate a Dropbox share URL from a local path.

**Completion:** the exact requested folder exists once, under the correct stage, with the expected children and no unintended changes.

## File incoming documents

- Read enough content to identify the job, source, document type, issue date and revision. A filename alone does not prove a permit was issued, a contract signed, or a document approved. Resolve uncertainty before filing; if necessary retain the source and report the unresolved destination.
- Route documents by purpose:

| Folder | Typical contents |
| --- | --- |
| customer orders | Customer proposals, contracts and change-order documents; retain their actual draft/issued/signed state |
| vendor orders | Subcontracts, purchase orders and vendor-order documents |
| plans & design | Drawing sets, specifications, schedules and design deliverables |
| procurement | Supporting product, selection and supplier information; no parallel order tracker |
| trade partners | Supporting trade-partner quotes and job-specific coordination documents |
| permits & compliance | Permit applications, issued permits, inspection and compliance documents |

- Keep a received plan set in plans & design even if its name says Permit Set. File the actual issued permit and compliance records separately. Never infer permit approval from a submitted drawing set.
- Preserve original bytes and original filenames by default. If a rename is requested/approved, use `YYYY-MM-DD - Source - Description - Revision.ext` where useful, with the document's date or otherwise received date. Avoid forbidden path characters; do not invent a date or revision. Read back exact existing names before writing.
- Check the destination before a copy/upload. Same name and identical bytes/hash: reuse, report duplicate, do not overwrite. Same name but different content: stop and choose an approved distinguishing revision/name. Preserve earlier versions; no destructive replacement.
- Copy/download first when possible, leaving the original source intact. A filing request authorizes a copy into the agreed destination, not deletion of the email, Drive source or local original. Ask before any move, rename or deletion, showing exact source/destination and collision consequences. Do not follow symlinks outside the authorized root or process .dropbox.cache as project content.
- Keep private financial/internal files distinct from customer-ready deliverables. Filing inside Dropbox does not authorize sharing, creating public links, inviting people or widening permissions. Never store credentials, tokens or bank/account numbers in the team tree.

**Completion:** original content and revision are preserved, the file is in the verified job/subfolder, and any existing links affected by an approved move/rename are reconciled.

## Move between stages

Search all stages first. Preview the exact old and new paths and obtain approval for the move. Inspect conflicts before executing; no overwrite, merge or deletion by default. Preserve relative child paths, verify files/counts and relevant hashes, and update authorized references. Do not automatically change JobTread status, closure or sharing because the folder moved, or move a folder merely because a JobTread status changed.

## Verification and handoff

- After local copies, verify exact path, size and hash; for plans verify content and page count. After connector uploads/mutations, read back the exact remote target and compare original downloadable bytes where supported.
- A successful local write proves only the local copy. Check Dropbox's supported sync status or remote target independently before claiming cloud sync. If verification is unavailable or pending, explicitly say **local copy verified; cloud sync unconfirmed**. Do not interpret an unavailable status command as success.
- Report the project folder, files added/reused, revision identity, verification evidence and any blocked decisions. Preserve resumable private source/target handles outside this public repository. Never publish real client files, paths, contacts or record IDs as skill examples.

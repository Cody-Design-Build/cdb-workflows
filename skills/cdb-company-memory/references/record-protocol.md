# Exact operational record protocol

This is a client convention over Hindsight exact documents, not an enforced schema, event store or transactional database. Domain rules remain in their owning skills.

## Identity and envelope

Use an explicitly configured company bank. Inside it use stable document IDs composed from the kind and canonical provider/account/record identity, not mutable titles. Encode components deterministically (for example URL-safe encoded canonical identity JSON); preserve the mapping in content. Never use only an email subject, task title or sender. A message's provider ID and mailbox identity are both necessary. UUID run/action IDs must be generated once and persisted before use, not regenerated on retry.

Recommended kinds and ID prefixes:

| Kind | ID | Write policy |
| --- | --- | --- |
| Source evidence | `cdb-source-<identity>-<source-version>` | New immutable-by-convention version; original remains in source system |
| Association | `cdb-association-<identity>` | Serialized mutable index containing explicit many-to-many edges |
| Review unit | `cdb-review-<run-id>-<unit-id>` | Separate event per completed unit with disposition and source version |
| Action intent | `cdb-intent-<action-id>` | Immutable-by-convention exact target/content/approval/dedupe identity |
| Action outcome | `cdb-outcome-<action-id>-<attempt-id>` | Separate verified/failed/uncertain event with exact destination evidence |
| Coverage | `cdb-coverage-<source-scope>` | Serialized replace; latest verified reviewed frontier and explicit gaps |
| Run index | `cdb-run-<run-id>` | Serialized replace; links all intents/outcomes/checkpoints and next unit |
| Decision/correction | `cdb-decision-<decision-id>` | New amendment linking superseded sources/claims and resolution scope |
| Report | `cdb-report-<run-id>-<revision>` | Derived view; source links, coverage/as-of and audience |

Use [record template](../templates/record.json). Add tags such as `cdb:operations`, `kind:coverage`, `project:<canonical-id>`, `entity:<canonical-id>` for supported retrieval, not security. Cross-project dependency edges belong in content; do not isolate context into unrelated per-project banks. Retain payload text as JSON when exact structured recovery is needed. The helper's input is a Hindsight MemoryItem: its `content` is the serialized envelope, `metadata` values are strings, `update_mode` is explicitly `replace`. Payload construction and envelope validation are currently procedural, not automated.

## Review and coverage

Persist the discovered unit manifest privately and in the run index before processing; include the source query, account, time window/change token, pages/cursors, discovered IDs and declared totals. Persist bounded batches and deduplicate/count in code. A source unit is a message/topic obligation, task or other explicit scope, not necessarily a whole thread or one task per email.

For each completed unit retain source pointers/version, evidence/claim distinction, matches and disposition: action, tracked, waiting, reference, noise, resolved or ambiguous. Link multiple messages to multiple obligations explicitly. Keep unreviewed units and page failures pending. Persist a review event before updating the checkpoint; if interrupted, recover the event and repair the checkpoint instead of pretending the gap was reviewed. Save source change markers only across fully reviewed work; otherwise retain per-unit progress and the previous complete watermark. Use overlap and periodic full reconciliation. Never promise incremental completeness until the provider's current discovery semantics are verified.

## Action protocol and interruptions

1. Under the shared writer lock, exact-read prior run/intents/outcomes and fresh destination state. Match obligation, not message count. Establish destination ownership and permission.
2. Persist the run index's planned action ID and exact intent with source IDs, requested target, exact patch/content, baseline destination revision/state, expected result, duplicate-match evidence, notification behavior and approval reference. Verify intent by exact GET before acting.
3. Execute only the authorized domain operation. No receipt can atomically commit with this call. Do not label absence of a receipt as failed execution.
4. Read the exact destination plus affected duplicates/relationships; persist a verified outcome only when it matches. Record uncertain outcome on timeout, partial result or mismatch. Add outcome links and review completion to the index after verification.
5. On restart, resume unfinished units first. Reconcile every intent lacking a verified outcome with the live destination, even if an uncertain event says no acknowledgment arrived. If already applied, record observed result and do not repeat. If definitely not applied, re-evaluate freshness and approval before retry. If indistinguishable, stop for human decision. Multiple attempts share the obligation/action identity but get distinct attempt IDs.

For a crash between intent storage and index update, the index already contains the planned action identity (step 2); re-read that exact intent. For interrupted index creation or a missing manifest, do not infer a complete run: disclose the gap and reconcile source/destination scope before actions. This protocol improves resumability; actual external-system crash recovery remains unproven.

## Enumeration and conflicts

Known IDs are preferred. If listing is necessary, discover the current documents list schema, use explicit tag filters and supported pagination, store each page privately, deduplicate IDs in code and compare with declared totals. No `q` search completeness guarantee; metadata is not filterable. Offset lists are not snapshots. Freeze cooperating exact writers, compare enumeration with a second pass, and disclose concurrent conversational capture or other writes that prevent stable completeness. The helper deliberately does not claim list/pagination automation.

There is no caller CAS or create-only operation. A pre-read hash comparison is not a lock. Preserve original intent/evidence payloads privately and do not reuse IDs for changed immutable events. Concurrent hosts or clients ignoring the local lock require externally enforced serialization before writes; this module does not provide it.

# Supported helper and source grounding

Authored stdlib REST client, grounded in installed Hindsight 1.2.1 `api/http.py`, `MemoryItem`, `RetainRequest`, `DocumentResponse`, exact document GET and retain handlers, matching release commit [0eb02d8c418eac6b489bc63883c993b2257dfac4](https://github.com/vectorize-io/hindsight/blob/0eb02d8c418eac6b489bc63883c993b2257dfac4/hindsight-api-slim/hindsight_api/api/http.py). Original summary/code, not a copied vendor SDK. See [review and upstream sources](../../../docs/HINDSIGHT-REVIEW.md). Recheck schemas when upgrading.

## Commands

Through `terminal`, from the checkout root (resolve the path from installed skill location rather than assume a workstation home):

```sh
python3 skills/cdb-company-memory/scripts/hindsight_documents.py --url "$HINDSIGHT_URL" get --bank "$CDB_MEMORY_BANK" --id "$DOCUMENT_ID"
python3 skills/cdb-company-memory/scripts/hindsight_documents.py --url "$HINDSIGHT_URL" retain --bank "$CDB_MEMORY_BANK" --item "$PRIVATE_ITEM_FILE"
python3 skills/cdb-company-memory/scripts/hindsight_documents.py --url "$HINDSIGHT_URL" verify --bank "$CDB_MEMORY_BANK" --item "$PRIVATE_ITEM_FILE"
```

All operations require explicit bank; no production bank, mailbox or credential path is built in. Mutation takes **one** private MemoryItem JSON file:

```json
{
  "document_id": "cdb-source-synthetic-fixture-v1",
  "content": "SYNTHETIC ONLY: fictional inspection still pending.",
  "timestamp": "2026-01-01T00:00:00Z",
  "context": "Synthetic fixture, not business evidence",
  "metadata": {"source": "synthetic-fixture", "classification": "attributed-claim"},
  "tags": ["synthetic-fixture"],
  "update_mode": "replace"
}
```

The helper POSTs `/v1/default/banks/{bank}/memories` with `async: false`, then GETs `/v1/default/banks/{bank}/documents/{document_id}` and compares identity, bank, `original_text`, tag set and `document_metadata`. It prints a compact verified receipt only on match. GET prints full document content: direct output only into an appropriately private surface/file. The separate `verify` command performs the same comparison using GET only and never retains. No automatic retries. Any retain error, missing original text or verification mismatch leaves the outcome uncertain; exact-read before retry. A synchronous timeout may have applied the write. Timestamp/context and downstream extraction are not asserted by the compact verification receipt. The server remains schema authority for optional fields.

No unsupported inline `extraction_mode` is sent: this release exposes only named retain strategies configured on the bank. The helper does not alter bank configuration. Synchronous retain can perform hosted extraction/consolidation and consume quota; do not promise LLM-free writes.

## Cooperative singleton lock

On one POSIX host choose one stable private lock path outside this checkout. Its parent must already be private and writable. Never remove/replace the lock file while any writer can run; filesystem inode identity is the lock. Every operations/interactive exact writer must use the same path. Prefer a foreground worker that owns the entire review/decision/write sequence:

```sh
python3 skills/cdb-company-memory/scripts/hindsight_documents.py lock --path "$CDB_RUN_LOCK" -- python3 "$PRIVATE_FOREGROUND_WORKER"
```

`lock` takes nonblocking exclusive `flock`, refuses symlink targets and `exec`s the supplied command with the lock descriptor inherited. A second holder fails without running its command. Command must remain foreground, keep inherited descriptors open, and not daemonize. This is local/cooperative serialization only, not multi-host locking, provider CAS or exclusion of ordinary conversational capture.

For a tool-driven interactive run with no foreground worker, an agent may use `terminal(background=true)` to run the lock around a bounded foreground sleeping process **as a lease holder**, then use its process ID/session through the available `process_manage` schema to check it remains alive immediately before each state-dependent write. Stop writes if it expires, is killed or cannot be checked; reconcile and reacquire before continuing. Explicitly terminate the holder after run completion using the actual process tool. This manual lease has a check/write race and is weaker than a worker owning all writes; do not claim enforced atomicity. If reliable one-writer coordination cannot be established, stay read-only and leave actions pending. No holder, service or scheduler is installed by this repository.

## Test boundary

Offline unit tests use a local synthetic HTTP server and real child processes to check exact routes, explicit-bank/input gates, post-write readback, verification mismatches, concurrent exclusion and SIGKILL release. Live synthetic verification must explicitly name an authorized test bank and use unique fixture IDs; preserve artifacts outside the checkout. Do not run against company records to prove connectivity. There is no live test command with a default bank, import script or business-system mutation code.

Not implemented: async operation UUID replay journal, CAS, list pagination, semantic retrieval, page/model refresh automation, automatic receipt reconciliation, backups or external action execution. Those are procedures over discovered tools, not capabilities of this helper.

# Operations module validation

## Implemented boundary

Three independently usable procedural modules: company-memory access/continuity, task management and operations coordination. Existing email/Surface/JobTread skills remain integration/domain owners. This is not an autonomous operations application. Schema-led agent execution, human approvals, payload/envelope construction, source coverage and business reconciliation are procedural; there are no pretend task/send/sync endpoints.

The small Python stdlib helper implements exact Hindsight document GET, one-item synchronous retain plus readback verification, read-only verification and a POSIX cooperative singleton lock for a foreground command. All memory commands require an explicit bank; no production default or credential file lookup is shipped. Exact fields/routes are grounded in the pinned installed 1.2.1 source linked from the helper reference.

## Checks actually exercised

- Final repository validator passed over 61 distributable files; all 28 offline unit tests passed. `git diff --check` was clean. Shared-only installation ran twice, with exact target readback for all three new links and no new Hermes-local links. Protected `AGENTS.md` was not edited.

- Baseline: repository validator passed; 16 existing unit tests passed before edits.
- Test-driven helper slices: exact GET, retain/readback, validation gates, cooperative process exclusion/SIGKILL release, read-only verification and empty-bank rejection each observed failing before implementation, then passing. Synthetic HTTP server tests exercise real requests; real subprocesses exercise locks. Verification comparisons reject wrong text, missing original text, bank/ID, tags and metadata. URL policy rejects remote plaintext and embedded credentials/query strings.
- Live synthetic helper exercise: one unique fictional document, two versions, each retained, independently verified and exact-read. Six command checks passed in 9.26 seconds; a final-code repeat also passed all six in 8.056 seconds, under the helper's foreground lock, using only the separately authorized synthetic bank. Nested JSON/Unicode, replacement, identity, original text, tags and metadata matched exact GET. Artifacts remain private outside this repository. No company-memory bank, mailbox or business records were accessed by this test.
- Offline module contracts cover independent entry points, consequence gates, real skill dependencies, existing-policy handoffs and shared-only installer registration/idempotency. Installer tests use isolated homes; legacy client tests create links only in those disposable homes.

Run full offline checks through `terminal` from the checkout root:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Shared installation only:

```sh
python3 scripts/install.py --agents shared
```

The installer must be followed by exact symlink target readback; it is not API authorization. Runtime discovery may require a fresh client session. No Hermes-local installation is required when external shared discovery is configured.

## Not established

- Full company operations, real task lifecycle, Gmail drafts/sends, Surface/JobTread changes or notification suppression were **not** exercised. Procedure text and offline contracts do not prove these integrations.
- SIGKILL tested a local lock-owning process, **not** service/database/power-loss durability, distributed locking or interrupted business actions. A manual interactive lease has a check/write race; use a foreground owner for stronger same-host serialization. No caller CAS, create-only contract, cross-document transaction or exactly-once external action is claimed.
- No source pagination/live change-discovery completeness, async deduplication, semantic retrieval quality, page/model refresh, stale correction handling, audience isolation, production backup/restore or long-term persistence benchmark was added. Earlier research/synthetic tests have their own narrower evidence, not proof of this orchestrator.
- No new cron/services/configuration, global bank routing, historical import, source syncing, credentials or business-record changes. Existing read-only triage mandate and old banks/checkpoints remain intact. Unified-bank activation and publication are separate owner-controlled work.
- No automatic budget/cost measurement or quiet review cadence is deployed. Embedded database production hardening remains outside this module.

Public source contains procedures and synthetic fixtures only. Real reports, source evidence, receipts, verification artifacts and secrets stay private.

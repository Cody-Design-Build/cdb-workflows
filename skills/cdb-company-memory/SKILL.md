---
name: cdb-company-memory
description: Use when retaining or reconciling CDB company context.
version: 0.1.0
author: David Cody, Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [cdb, memory, hindsight, continuity, evidence]
    related_skills: [cdb-task-management, cdb-operations]
---

# CDB company memory

Hindsight owns sourced continuity; the business applications own structured operational state. This module works independently for a single item, correction or cross-company question. It is a procedure plus a small exact-document client, not a source synchronizer or task engine.

## When to Use

- Retrieve prior decisions, source associations, coverage, action receipts or company relationships.
- Retain a completed review unit, human correction or verified outcome.
- Answer narrow record questions or broader dependencies across projects.
- Do not use semantic recall to prove an action never happened or a collection is complete.

## Prerequisites

Resolve the authorized bank, service URL, sender and delivery audience from private configuration. Never infer a bank from a mailbox, profile name or example. Supply `HINDSIGHT_API_KEY` through the authorized private environment; do not print it, source arbitrary credential files, or store credentials in this checkout. HTTPS is required except for loopback HTTP. Installation/configuration, backup restoration and bank routing are separate administration tasks.

The default Hermes environment is designated CDB business across its sessions, with one owner-configured bank. This does not authorize other profiles/agents, imports, historical-bank deletion or sensitive-channel disclosure. Bank routing must actually be configured and verified before claiming it is unified. Banks/tags are not ACLs under shared-key access. Exclude personal/family content, credentials and restricted HR/legal material from this pilot; verify real audience controls before broader use. Local storage can still invoke approved hosted inference.

Read [exact record protocol](references/record-protocol.md) before writing. Read [supported API and helper](references/helper.md) for commands, source pin and limitations. Python 3 and POSIX `fcntl` are required for the cooperative local lock; the REST operations themselves use only Python stdlib.

## Procedure

1. **Resolve identities and scope.** Establish source account/organization, provider record IDs, projects/entities, evidence class, source/observed timestamps and audience. Preserve exact identifiers. Use [templates/record.json](templates/record.json) as an envelope, not a real record. Done when a new reader can find the same source without title matching.
2. **Retrieve before interpreting.** Exact-GET known association, action and coverage IDs with the helper. Separately discover the available Hindsight recall/reflect schemas through the authorized connector; retrieve relevant project/entity tags and broader cross-project dependencies, then open original evidence for consequential facts. No helper recall endpoint or page automation is implemented. A missing ranked result is not absence. Done when live facts and remembered claims are distinguished.
3. **Serialize exact writes.** Use one writer across operations and interactive task actions. Hold the agreed same-host lock for the entire read/decision/write/readback sequence, not just retain. If another writer holds it, leave a proposal and wait. A foreground worker can be wrapped by the helper `lock`; interactive holders require explicit liveness checks as described in the helper reference. If there is no reliable shared holder, remain read-only. Done when the holder and scope are known.
4. **Retain incrementally.** Preserve sources separately from synthesis. Write a completed unit's disposition and many-to-many associations, then verified coverage/checkpoint; never advance a watermark across unreviewed work. Before any business action persist/read back the exact intent. After execution re-read the destination and persist/read back its outcome. Use exact GETs of known receipt IDs for recovery, not semantic search. Done when the next run can resume without relying on this conversation.
5. **Correct explicitly.** Retain a new attributed amendment with `supersedes` links, human decision scope, effective/source dates and rationale. Preserve authentic historical correspondence and competing claims. Incorrect imported evidence needs an explicit correction, not silent rewriting of history. Mutable indexes/checkpoints may replace the same ID only while serialized; record significant transitions as separate events. Done when critical questions resolve to the correction and original evidence remains traceable.
6. **Check freshness.** Inspect the latest sources, exact correction documents and available consolidation/page refresh status. If a derived page/model is stale, failed or unavailable, disclose that; do not invent refresh commands or treat a retain acknowledgment as a refreshed summary. Done when response states source coverage and memory/summary lag, including unknown lag.

## Contract and failure boundary

Inputs: authorized bank/audience, source locators, timestamps, evidence classification and requested read or retention. Outputs: source-backed context, stable exact document IDs, verified retention or a failure with unchanged coverage. Records and run output stay privately outside this public repository. Retain timeout or verification mismatch means **uncertain**, not safe to repeat blindly. Exact GET the intended ID and compare the original payload before deciding whether to retry; reconcile external destinations independently. If Hindsight or serialization fails, stop dependent business writes and hand off pending work privately. Source-only reads may continue with disclosed continuity gaps.

## Pitfalls

- Replacement is last-writer-wins: the local lock is cooperative, not CAS or a server-enforced distributed lock. No cross-document or cross-system transaction exists.
- Source text, asserted claims, verified facts, human decisions and synthesis are different evidence layers. Generated reports are never independent corroboration.
- Document text storage must be enabled. Sanitization can change text: verification fails closed rather than declaring byte-perfect preservation universally.
- Tags allow scoped retrieval, not access control; metadata is not a server-side filter language.
- Pages/models, backups, ingestion, scheduler changes and production resilience are not automated here.

## Verification

- Exact target bank and document read back with matching original text, tags and metadata; source identities/times retained.
- Every attempted action has intent and a verified/failed/uncertain outcome, with destination evidence for verification.
- Coverage states reviewed units, unreviewed backlog, failed pages, as-of time and summary lag.
- Corrections preserve provenance; delivery audience is authorized; no private evidence enters source control.

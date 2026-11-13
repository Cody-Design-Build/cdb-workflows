# Initial rollout verification

Read-only and offline checks performed on 2026-11-13 for the initial CDB workflow-library rollout. This record contains no customer records, credentials or authorization identifiers.

## Repository and installation

- `python3 scripts/validate.py` passed structural metadata, JSON/example, relative-link and targeted credential-pattern checks.
- `python3 -m unittest discover -s tests -v` passed three isolated-home installer tests: preflight conflict refusal, backed-up migration/shared discovery, and preservation of a dangling original link.
- The shared skill hub and Hermes, Codex, Claude Code, omp and OpenCode skill paths resolved to the canonical Work checkout. Existing conflicting skill directories were backed up outside this repository.
- A fresh omp print session discovered `jobtread`, `jobtread-budget-writing` and `jobtread-catalog-standards` through its actual available-skills surface.

## Connection checks

The workstation retained its existing authorized per-user Linux gateway; no credentials were copied into agent configuration or this repository.

- Live MCP discovery exposed one `query` tool with an object-valued `query` input.
- A live grant read matched the expected organization. Root-schema discovery returned 236 fields. Responses stayed outside the repository.
- Claude Code 2.1.323 reported the configured JobTread connection connected.
- Hermes CLI connection testing connected and discovered the query tool.
- OpenCode 2.3.0 reported JobTread connected after configuration reload.
- Codex CLI 0.169.0 and omp 18.20.0 configuration entries were exercised through their configured stdio executable/arguments: discovery, an authorized organization read, and fresh reconnection/read passed. This is transport verification, not a claim of model-driven business execution in both clients.
- The gateway rejected an unauthenticated request with HTTP 401.

## Limits

No business records were created, edited, deleted, issued or sent. No payments, signatures, live financial/document workflow trials, new-user OAuth consent, hosted-assistant attachment flow, or gateway-service restart occurred. Direct official OAuth onboarding follows upstream documentation; existing local adapter reuse was the tested transport. Skill instructions guide agents but do not replace server permissions or approval controls.

Inherited structural snapshots were reviewed as references; their original capture date/version is unknown. Live root discovery checks operation names and top-level keys, not every nested type, template, side effect or permission. Automated credential patterns cannot prove exhaustive privacy. See [schema provenance](../skills/jobtread/references/schema-notes.md) and [maintenance](MAINTAINING.md) for ongoing review requirements.

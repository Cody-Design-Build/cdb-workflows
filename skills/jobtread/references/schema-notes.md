# Structural schema references

## Provenance and limits

The JSON files in this directory were inherited from CDB's existing JobTread operating skill. Their source is the JobTread connector's tool discovery and API schema introspection. The original capture date, API version and precise grant context were not recorded here; no capture date or present-day coverage is asserted.

A separate read-only live root-schema discovery on 2026-11-13 confirmed the operation names and top-level input keys used by the budget intake, customer-document, schedule and daily-log procedures, including root-returning mutations and absence of `updateJob.status`. That probe did not replace these inherited files or recursively validate nested inputs, templates, side effects or permissions for execution. Its private response is not distributed here. The discovery date is not a claimed capture date for the inherited snapshots.

- `tools.json` retains the discovered tool name, input envelope and machine-readable annotations. Its captured upstream prose description was removed; use the maintained `query-tool.md` and discover current documentation through the connector.
- `root-schema.json` inventories root fields; `root-fields-expanded.json` maps root field names to expanded schema responses.
- `job-schema.json`, `organization-schema.json` and `organization-type.json` describe selected entity types.
- `current-grant-schema.json` and `grant-type.json` describe grant structure, not an actual authorization or credential.

These are schema references, not business-record exports. Schema field names such as `grantKey`, `externalId`, `emailAddress` or `description` describe potential inputs/outputs; they are not credential or customer values. Short schema annotations remain to interpret structure; the full upstream tool narrative is not republished. Do not add live records, IDs, signed URLs, tokens, account history or raw discovery logs to these public files. Keep operational evidence private.

The inventory is not a complete recursive schema, a permission grant, or a tested workflow. Resolve referenced global types and nested arguments live. Templates, custom-field options, notification defaults and permissions can differ by organization and change over time.

## Confirmed errata in the former tool narrative

Reading the inherited material showed:

- The contact/custom-field query omitted a closing object brace at the `nodes` selection. It was not valid JSON.
- Several job queries selected `status`, and one update passed `updateJob.status`. The job schema instead exposes `closedOn` and `customFieldValues`; the expanded updateJob input contains no `status`. CDB's stage is its `Status` custom field, discovered by current ID/options. Document status is unrelated.
- The old mutation prose contradicted itself about update selections. Expanded update mutations reviewed here return `root`; use discovered root selections or a separate readback, not a generic direct-entity assumption.

The maintained query reference replaces these examples. Schema absence here is a reason to discover live, not proof that a future version can never support a field.

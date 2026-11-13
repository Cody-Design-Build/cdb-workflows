# JobTread query procedure

Maintained CDB guidance, not the connector's tool description. See [schema provenance and errata](schema-notes.md). Discover the installed tool's exact input envelope; these examples use the captured `query` object.

## Discover and read

Inspect the root inventory, exact operation, inputs, output and referenced global types before unfamiliar calls. Schema input paths descend through `.$`; one-of branches use `._on_VARIANT`. Offline presence does not establish permission.

```json
{"query":{"schema":{"$":{"path":"root","search":"document"}}}}
```

```json
{"query":{"schema":{"$":{"path":"root.updateJob","expand":true}}}}
```

```json
{"query":{"currentGrant":{"id":{},"allowedActions":{},"organization":{"id":{},"name":{}}}}}
```

Select scalars with `{}`; arguments go under `$`. Match identifiers to the intended organization and record. This job read deliberately avoids a nonexistent built-in `status`.

```json
{"query":{"job":{"$":{"id":"<jobId>"},"id":{},"name":{},"closedOn":{}}}}
```

```json
{"query":{"organization":{"$":{"id":"<organizationId>"},"jobs":{"$":{"size":25},"nodes":{"id":{},"name":{},"closedOn":{}},"nextPage":{}}}}}
```

Continue each connection using its returned `nextPage` as `$` argument `page`, retaining filters and selection, until null. Nested connections paginate independently. Discover filters, aliases, sorting and aggregation live; do not import another API's syntax. Validate affected records and totals before claiming completeness.

## Write and reconcile

Follow the operating skill's approval/deletion rules. Inspect required fields, one-of constraints, defaults, notification behavior and return shapes. Omitted, null, empty and zero are not interchangeable. Pass only approved changes.

Captured create mutations return root selections with fields such as `createdDocument`, `createdPayment` and `createdFile` beneath the mutation. Root-returning updates can select the corresponding root record beneath the mutation. Discover each shape and also read the exact ID back separately; do not assume all mutations behave identically.

CDB stage changes use the live `Status` custom-field ID/options and discovered `updateJob.customFieldValues` structure. Job and updateJob snapshots have no built-in `status`. Preserve independent `closedOn` unless closure is authorized.

Save mutation responses privately before dependent steps. A timeout or parsing failure is ambiguous: reconcile remote state before retrying. Never test permission with a mutation.

Uploads require an upload request, original-byte transfer using returned method/headers, then an attachment on a supported target. Verify resulting files and downloadable bytes. Keep signed URLs and credentials private.

## Errata

The former captured description contained an unbalanced contact/custom-field example and several nonexistent job `status` reads/updates. Those examples are replaced, not endorsed. Document status is separate and requires its own discovery. Examples here are request illustrations, not evidence of live execution or authorization.

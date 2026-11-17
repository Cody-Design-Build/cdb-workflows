# Migrated workflow source and publication boundaries

## Provenance and attribution

The public `email-inbox-triage` source was adapted from the owner's maintained local skill, version 0.2.0, credited to **Ben Barclay (benbarclay), Hermes Agent**, with an **MIT** license declaration. The source set contained `SKILL.md` and `references/project-briefings.md`; both were reviewed. The public `cdb-surface-orders` source was adapted from the owner's maintained local `SKILL.md`, version 0.1.0, credited to **David Cody, Hermes Agent**, also declared **MIT**. Preserve those author and license notices. Their original authorship dates and any earlier upstream URL are not established; do not invent them.

This is an authored, sanitized adaptation, not a capture of mailbox content or the private Surface implementation. User contact defaults, private project/folder references, identifying supplier anecdotes and attorney identity were removed or generalized while retaining reusable policy. Attribution names above are intentional author credits, not operational contacts. No raw records, task evidence, email checkpoints or credentials are distributed. Full original copies remain in owner-controlled private backups outside this checkout; do not publish the backup inventory or private paths.

`cdb-dropbox-management` is original CDB-authored MIT workflow text. It owns job-folder discovery, the six-child filing convention, collision handling, authorized stage moves and sync verification. Job setup and Surface link to it instead of maintaining competing folder conventions.

## Contracts and dependencies

| Module | Inputs | Outputs and evidence | Failure boundary |
| --- | --- | --- | --- |
| `email-inbox-triage` | Authorized account, scope, allowed actions, private continuity checkpoint | Project-aware decision queue; private thread evidence, coverage/backlog and successful watermark | Partial-source report; preserve backlog and watermark; no implicit sends, drafts or record changes |
| `cdb-surface-orders` | Authorized project/record targets, requested actions, source evidence | Procurement orientation or approved exact changes with private read-back evidence | Stop dependent writes on missing schema, incomplete pagination, conflicts or uncertain outcomes |
| `cdb-dropbox-management` | Verified job/stage, authorized source files and filing request | Original bytes in verified destination, collision/revision report, local and remote verification distinguished | No overwrite or implicit move/share; report cloud sync unconfirmed when unavailable |

Email provider connectors and Surface/JobTread/Dropbox authorization are separate prerequisites, not installed services. The Surface skill references the owner's private application documentation as optional implementation context; access to that repository is not granted here. This library republishes no private implementation files. Discover the connected server's live operations and schemas before acting.

The original skill names remain unchanged so existing scheduled launchers can resolve them. Existing private checkpoint locations and backward-compatible checkpoint lookup are documented, not migrated into the repository. Do not modify cron as a side effect of installing these instructions.

## Shared discovery

The installer supports the CDB modules above, the four JobTread modules, and the separately attributed `grill-with-docs`, `grilling` and `domain-modeling` imports. Its default/`--agents shared` mode creates only shared discovery links. When Hermes already scans `~/.agents/skills` through `skills.external_dirs`, do not request `--agents hermes`: that explicit legacy option creates local discovery links, which take precedence over external skills. Preserve any former independent local directories outside active discovery before retiring them. Do not change credentials, config, cron or unrelated workspace instructions as part of a source migration.

See the official [Hermes external-directory documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills#external-skill-directories) for precedence. External discovery supports original names in the skill index and cron. Reload/restart discovery after changing links; filesystem verification alone is not proof that an already-running session refreshed.

## Verification limits

Use the validator and offline unittest suite documented in [MAINTAINING.md](MAINTAINING.md). Tests cover shared installation without client/config creation, explicit legacy paths, preserved policy gates, provenance and targeted privacy patterns. These checks do not prove exhaustive privacy or successful live email, procurement or Dropbox workflows. No business mutation is needed to validate publication or discovery links.

---
name: grill-with-docs
description: A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go.
disable-model-invocation: true
---

Load `grilling` and `domain-modeling` with the agent’s skill-loading tool (in Hermes, `skill_view`). Follow both: interview in dependency-aware rounds and capture settled terms and consequential decisions. Do not implement the design until the user confirms shared understanding.


## Integration and provenance

Adapted from Matt Pocock’s MIT-licensed `mattpocock/skills`, commit `5863806dd4e15c63174bee4e7515a4256792ecfa`, path `skills/engineering/grill-with-docs/SKILL.md`. See [LICENSE](LICENSE) for the original notice.

Use the host agent’s available tools to inspect facts; do not invent tool names. In Hermes, batch independent user decisions with `clarify` when appropriate, and use `skill_view` to load dependencies. Keep customer facts, private examples and run evidence outside public repositories. Research and design-note updates are permitted during the interview; business-system changes and implementation require the user’s authorization.

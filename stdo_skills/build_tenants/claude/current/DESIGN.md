# Claude current design

Follow the shared [design](../../../specification/DESIGN.md). The installer creates
Claude native core wrappers and the shared stdo-context adapter. They acquire
purpose indexes at relevant task-constraint, build, review, handoff and refresh
points after native intake. Source-first independent review remains source first.
The installer preserves canonical native metadata and links; it does not duplicate
native control ownership.

The optional [stdo-project skill](skills/stdo-project/SKILL.md) delegates visual
project/code operations to a separately pinned Representation Tools component.
Context use does not load this skill or require the visual component. Host pickup,
explicit invocation and local command execution remain separate tested claims.

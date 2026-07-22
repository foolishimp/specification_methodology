# STDO 2.0 Refrozen Exact Candidate

## Subject

- candidate commit: `915d992c6ceb7c23df41bb30d12bdbdd10cb97ce`
- candidate tree: `e47a60d4b4dd6a15e26b017f93c35855aa6b8fe7`
- predecessor: `v1.8.0` at
  `9cf2741917ca2d496cd78f5736ea2218d5eb0897`
- branch and remote matched the candidate when this checkpoint was written
- no local or remote `v2.0.0` tag exists

This checkpoint is commentary. It does not amend or accept the candidate.

## Review Repair

The repair closes the findings against `11ba894`:

1. `SPEC_METHOD.md` no longer has a rival design-first execution sequence.
   Design owns structural `HOW`; design, implementation, and tests may co-evolve
   when upstream truth leaves no unresolved material architecture decision. A
   prior accepted design gates only the unresolved durable decision.
2. `SPEC_METHOD.md` bootstrap law now distinguishes mutable method authoring,
   selected immutable release authority, and its installed distribution.
3. The auxiliary plugin now uses the canonical marketplace layout:
   `plugins/spec/.claude-plugin/plugin.json` plus
   `plugins/spec/commands/spec-refresh.md`. Marketplace and plugin validation
   both pass.

## Reproducible Evidence

- standards members: `41`
- member-set digest:
  `284efbb31affd6772fe8e523bdd157f7f2ebe4d4d8dee7b5c9ddfd0482da93a0`
- top-level normative lines: `9,482`
- `v1.8.0` top-level normative lines: `8,619`
- increment: `863` lines, `10.01%`
- every `v1.8.0` standards path remains present
- all 16 new law identifiers have one owning top-level occurrence
- source and aggregate compression digests match
- release inventory paths and hashes match the exact standards tree
- auxiliary marketplace, plugin, and command hashes match the release note
- `git diff --check` passes
- no executable STDO conformance or workflow implementation exists

## Pending Gate

Review the complete exact candidate and full `v1.8.0` delta. Direct human
acceptance of these same bytes is required before tag publication.

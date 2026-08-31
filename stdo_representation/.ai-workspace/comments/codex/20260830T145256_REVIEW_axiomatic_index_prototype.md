# Axiomatic Index Prototype — Exact-Commit Review

Author: Codex independent reviewer

Reviewed at: 2026-08-30T14:52:56+10:00

Verdict: **GO**. P0: 0. P1: 0. P2: 0.

## Exact subject

- commit: `5dd6ccae1e155ff29ae91bd17534e3a6d61bb078`
- tree: `c4a116177c6369e66a4b5635955509cbe542ec00`
- worktree and index at review: clean
- active GTL profile: `urn:stdo-index:gtl-profile:axiom-index:7`
- active GTL profile SHA-256:
  `20dc8e7e17af3f5dd0c3814342d2f350b88193bede4598933ae4fcbdec361022`

## Disposition

The six reported defects are closed on the exact subject:

1. The frozen carrier coordinate uses `authority_inventory_count = 33` and
   `specification/requirements/gtl/`. Its RFC 8785 JCS preimage independently
   reproduces `b5becdf2801577f00bbc119a6bb23e0015a2007147818557ee2e770bc682b703`.
   Profile and publisher validation derive the identity rather than trusting a
   supplied label.
2. Profile `7` binds the build tenant, carrier basis, canonicalization and
   framing law, `ModulePublication` contract, record/rule/contribution
   contracts, configuration version, and complete tuple and record schemas.
   Construction and decoding consume the validated profile.
3. Semantic compilation is two-phase and immutable. One content-addressed raw
   output is bound to each run. Proposal, candidate, and structural-result
   artifacts publish atomically under digest coordinates. Changed bytes refuse
   instead of replacing prior evidence.
4. This review binds an immutable Git commit and tree.
5. The exact STDO `v2.5.0-rc.1` install verifies. Product Definition status and
   bootstrap fail only at the deliberately empty accepted-frame-basis list.
   Project-local staging checks do not claim Product Definition conformance.
6. Canonical JSON refuses lone UTF-16 surrogates. `npm test` builds first and
   refuses an empty compiled-test inventory.

Replay passed:

- constitution checker under normal Python and `-O`;
- 25 project tests;
- 33 semantic-compiler tests under normal Python and `-O`;
- frozen GTL reacquisition, TypeScript build, and 31 tests;
- 48 JSON parses, Ruff, Black, and diff hygiene;
- default semantic-compilation preflight refusal with no run created.

## Authority boundary

This GO qualifies the implementation checkpoint. It does not accept the
proposed frame basis or GTL profile, construct or accept a current `a_c.STDO`,
construct or admit a current `a_c.STDO.GTL`, publish a Product, or authorize a
release. Those exact-subject human gates remain open.

The reviewed commit was local-only at review time; no remote publication or tag
was inferred.

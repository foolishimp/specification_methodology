# T-006 — Align STDO Representation With STDO 2.5.0

- id: T-006
- title: Align STDO Representation with represented STDO 2.5.0
- type: feature
- ticket_category: constitutional
- status: completed
- review_status: go
- goal: GOAL-005
- change_intent: >-
    Reprice the active Representation line to match represented STDO 2.5.0 and
    distinguish Source STDO, its canonical a_c.STDO compression, and the
    deterministic logical constraint index over that compression.
- change_class: product_reprice
- re_entry_point: specification/PRODUCT.md
- triaged_at: 2026-08-31
- created_at: 2026-08-31
- updated_at: 2026-08-31
- completed_at: 2026-08-31
- owner: stdo_representation
- work_authorization: direct_human_authorization_2026-08-31

## Outcome

Make the version and layer relation exact:

```text
Source STDO prose 2.5.0
  -> a_c.STDO 2.5.0 semantic compression
  -> deterministic logical constraint index
  -> reference-frame evaluation and source re-entry
```

STDO Representation inherits the semantic version of the represented STDO
Product line. Its RC ordinal and content identities remain independently
qualified. Axiom Indexer remains an independently versioned Development
Product.

## Scope

- reprice the active STDO Representation Product line from bootstrap `0.1.0`
  to represented version `2.5.0`;
- distinguish Source STDO authority, canonical `a_c.STDO` compression, and the
  deterministic index over that compression;
- preserve the immutable historical `v0.1.0-rc.1` Product and claims;
- use project-qualified release refs in the monorepo;
- refresh the native skill, release record, project frame basis, checker, and
  focused tests; and
- qualify one local immutable candidate without publishing remote refs.

## Refusal

Refuse any retargeting of historical release objects, semantic authority claim
for the index, independently chosen Representation semantic version, copied
Axiom Indexer member, GTL or runtime expansion, or unqualified monorepo tag.

## Closure Evidence

- Source STDO `v2.5.0-rc.1` verifies with manifest
  `3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338`.
- The canonical compression identity is `e325e4399560b0be5562d345005818e4f925f72ecbfd9a234207f8c77b095cc5`.
- The intrinsic constraint-index identity is `2df34cb85bf6fbad2436e468e14cb5c26ff8d0aa721f8de10bb7e948b0d21b78`.
- The current eight-member inventory is
  `bc3bae5b322149b1457c8c2372b734de1b897ad9540f7c98602f2c4fcfc7e331`.
- Accepted frame revision 12 and its decision reproduce as
  `ca11d7f1977333f1b9cdc47f4051280fb980abdef95143bc49072e5c22e10434`
  and `58ae74c83eccb330d5c58799058f5507fd5f42a4f64a4a99bb1ac06336a5b559`.
- The constitution checker, full normal and optimized suites, native skill
  validation, exact map reproduction, Product status, fleet verification,
  formatting, lint, JSON, Git integrity, and diff hygiene pass.
- Independent candidate review reports P0/P1/P2 = 0 in
  `../../comments/codex/20260831T155056_REVIEW_stdo_representation_2.5_candidate.md`.
- No immutable Representation 2.5.0 tag, selector, branch, publication,
  post-publication acceptance, or remote mutation is claimed or performed.

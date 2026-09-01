# T-027 - Bind Coordinated Stack Release

- id: T-027
- title: Bind same-version coordinated publication for every STDO index asset
- type: release_method
- ticket_category: ordinary
- status: active
- review_status: pending
- goal: release-matched-stdo-stack
- change_intent: >-
    Make a stack release incomplete unless the exact STDO corpus, distributed
    plugin, Axiom Indexer mechanics, STDO Representation Product, and generated
    a_c.STDO program and map carry one exact product-local cut version and bind
    the same source-member digests.
- change_class: requirement_reprice
- re_entry_point: specification/standards/RELEASE_METHOD.md#coordinated-release-matched-asset-cohorts
- triaged_at: 2026-09-02
- created_at: 2026-09-02
- updated_at: 2026-09-02
- owner: specification_methodology
- pen_holder: codex
- work_authorization: direct_human_product_owner_authorization_2026-09-01
- immediate_published_predecessor: v2.5.0-rc.3
- target_rc: v2.5.0-rc.4
- publication_mode: coordinated_atomic

## Admission Gate

1. RC3 tags, records, selectors, and installed bytes remain unchanged.
2. Mutable Release Method and every digest-bound compression that consumes it
   define or route to one explicit cross-Product cohort without merging Product
   identities or authorities.
3. A root coordination record and deterministic checker fail closed on a
   missing, stale, differently versioned, or source-digest-incongruent asset.
4. Candidate construction freezes STDO and plugin first, creates the annotated
   STDO tag locally, and derives every index from that exact unpushed cut.
5. A second commit freezes the child Products and cohort record; prepublication
   qualification succeeds before child tags are created.
6. One atomic transport publishes main plus all Product RC, immutable-tag,
   selector, and release refs, followed by remote partial-cohort refusal and
   exact topology verification.

## Required Cohort

- exact STDO standards corpus `v2.5.0-rc.4`;
- distributed Claude and Codex `spec` plugin `2.5.0-rc.4`;
- Axiom Indexer mechanics Product `v2.5.0-rc.4`;
- STDO Representation Product `v2.5.0-rc.4`; and
- released `a_c.STDO` axiomatic program and logical constraint map
  `v2.5.0-rc.4`, with complete source-corpus member and digest closure.

## Non-Closure Conditions

- any required asset is absent or names another semantic version or RC ordinal;
- a generated index lacks the exact STDO member set and digest basis;
- a source member changes without regeneration and requalification;
- a Product tag is published independently or a remote contains only part of
  the required cohort;
- RC3 transition artifacts are presented as the completed coordinated cohort;
- mutable sibling source substitutes for an exact local annotated cut; or
- post-publication bookkeeping moves an immutable Product tag.

## Release Boundary

The Release Method amendment changes qualifying STDO bytes and can first appear
in `specification_methodology/v2.5.0-rc.4`. RC3 remains its exact immutable
predecessor. This ticket authorizes candidate construction and proportional
qualification only; it does not itself commit, tag, push, publish, accept, or
adopt RC4.

## Proof Surface

- Release Method and compression congruence tests;
- root checker unit tests for positive, stale, missing, version-mismatch, and
  remote-partial cases;
- a prepublication check over the exact frozen child/cohort commit and local
  annotated STDO tag;
- one atomic push receipt and remote topology check; and
- independent exact-cohort review before Product-owner acceptance.

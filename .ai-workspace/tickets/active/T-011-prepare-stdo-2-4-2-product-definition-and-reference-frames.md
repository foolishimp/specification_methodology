# T-011 - Prepare STDO 2.4.2 Product Definition And Reference Frames

- id: T-011
- title: Prepare the Product Definition Overlay and generic reference frames as STDO 2.4.2
- type: proposal
- ticket_category: constitutional
- status: active
- review_status: pre_rc_qualification_passed_ready_for_rc
- goal: >-
    Publish one exact STDO 2.4.2 successor over immutable v2.4.1 that adds the
    layout-neutral Product Definition Overlay, build-tenancy and work-carrier
    bindings, and the eleven generic specialist reference-frame families.
- change_intent: >-
    Let every product locate its governing constitution, local decisions,
    WHAT, independent HOW realizations, work carriers, collective frame bases,
    and explicit composition without restructuring an existing repository or
    importing consumer-specific architecture into STDO.
- change_class: product_reprice
- re_entry_point: specification/PRODUCT.md
- triaged_at: 2026-08-21
- created_at: 2026-08-21
- updated_at: 2026-08-21
- owner: specification_methodology
- pen_holder: codex
- predecessor_release: v2.4.1 at c37452a390e8456863eeb4e3d5bf9c9a237a44ed
- predecessor_standards_aggregate:
  0f46a3d583f321da0445331566ef878e11e19e16e71c54fb9a8e66c5fff4ce91
- target_release: 2.4.2
- release_class: patch_release_default_rc_path
- release_note: releases/v2.4.2.md
- current_goal_binding: this ticket, section `Current Goal`
- work_authorization: direct_human_authorization_2026-08-21

## Intake Triage

**Substantive?** Yes. The candidate adds a normative interoperability schema,
a per-product overlay contract, layout-neutral multi-build-tenancy and work
carrier routing, and eleven generic specialist-frame families.

**Boundary crossed?** Normative STDO sources, source-maintained compressions,
bootstrap projections, the live Product definition, and release preparation.
No downstream consumer edit or adoption is authorized.

**Smallest lawful re-entry.** Product repricing. The change alters the current
STDO Product boundary while preserving the existing Intent and immutable
`v2.4.1` predecessor.

**Release path.** `RELEASE_METHOD.md` supplies the default new-RC path after a
tapped release. The selected target is `2.4.2`; selection does not tap, publish,
or make the mutable candidate operative.

## Current Goal

This active ticket is the bounded current goal and durable work carrier for the
single `2.4.2` release wave. The repository maintains no separate
`specification/GOALS.md` surface. When this ticket closes and no successor
ticket is active, no continuing work wave is implied.

The current goal is to freeze, independently review, accept, and publish one
exact candidate that:

1. gives the Product Definition Overlay one normative schema and one fill-in
   template;
2. keeps constitutional coverage, local decisions, collective frame bases,
   `WHAT`, `HOW`, ticket/comment carriers, and composition discoverable without
   prescribing repository layout;
3. distinguishes mutable product-definition identity from immutable Product
   and release identity;
4. verifies composition locator, expected target identity, directed relation
   authority, and a non-empty governing contract set;
5. separates portable JSON structure validation from URI assertion,
   resolution, identity, and authority conformance;
6. adds Product, Design, Design Component, Public Boundary, Entity, Operator,
   Owner, Effect, Reuse/Foundation, Install, and Proof as generic specialist
   evaluation families without importing consumer-local topology;
7. keeps every source compression digest-current and every bootstrap projection
   semantically aligned; and
8. passes the immutable RC review and human acceptance required before tap.

## Candidate Scope

### Product Definition Overlay

- one `stdo_<label>.json` definition per distinct current product `WHAT`;
- `stdo_default.json` as the singleton default convention;
- support for existing layouts, default projects, multi-product monorepos, and
  arbitrarily nested project roots;
- complete constitutional authorities plus derived entrypoints;
- local axioms, overrides, and disambiguations with authority and scope;
- durable collective project reference-frame bases, distinct from temporary
  agent activation packets;
- Intent, Product, and specification `WHAT` locators;
- common realization surfaces and one or more independent build-tenant `HOW`
  locators;
- Goals, tickets, comments, and optional sprint carrier locators; and
- identity-complete explicit composition edges.

### Generic Specialist Frames

The optional STDO baseline adds eleven non-hierarchical evaluation families:
Product, Design, Design Component, Public Boundary, Entity, Operator, Owner,
Effect, Reuse/Foundation, Install, and Proof.

For the exact outcome, each family is instantiated where material, established
as non-material by capable authority, or retained as an explicit residual.
Composite satisfaction requires declared conjunction and conservation or lawful
translation of identity, coordinate and basis, value or evidence, lifecycle,
authority, and provenance at every material seam.

ABIogenesis remains discovery evidence. ABIogenesis, GTL, HoG, ABG, and renamed
local architectural substitutes are excluded from the generic baseline.

## Current Candidate Identity

- predecessor: immutable `v2.4.1`;
- predecessor standards members: 43;
- candidate standards members: 45;
- disposition: 17 changed, 26 conserved, two added, none removed;
- added members:
  - `schemas/product-definition.schema.json`;
  - `templates/PRODUCT_DEFINITION_TEMPLATE.json`;
- candidate standards aggregate:
  `5b5957d1a43be52a03b1316d442f2d797ba86a084550a1346dfc2dc6254123be`.

Any standards-byte change supersedes this identity and requires affected
digest, qualification, and release-note reconciliation.

## Release And Source-State Boundary

The Product release subject is the exact 45-member `specification/standards/`
distribution declared by `releases/v2.4.2.md`. `specification/PRODUCT.md` and
the release note are protected release-scoped inputs once an RC is frozen.

This ticket, its status, comments, review evidence, branch/tag existence, and
publication bookkeeping remain mutable source-project state outside the
Product release subject. Closing or moving this ticket after publication does
not mutate the tapped Product.

## Closure Law

This ticket closes only when:

- one immutable final-ready `v2.4.2` RC identifies the exact Product subject;
- all source and aggregate compression digests reproduce;
- schema positive and negative conformance cases pass;
- the 45-member inventory, disposition, aggregate, Product digest, and release
  note agree;
- Codex and Claude bootstrap projections preserve equal semantics;
- the immutable RC passes required independent exact-cut review;
- direct human authority accepts the exact release subject and final carrier;
- `release/2.4.2` and annotated `v2.4.2` are created at the accepted carrier;
  and
- publication-caused source-state closure is recorded afterward without moving
  the release tag.

## Non-Closure Conditions

- mutable source is treated as operative release authority;
- `v2.4.1` or any other published tag is moved or amended;
- Product, release-note, or standards bytes change after RC review without a
  new immutable RC and affected re-evaluation;
- `specification/GOALS.md` is recreated as a rival work-wave carrier;
- release status is embedded into the live Product definition;
- composition can retarget without expected-identity failure;
- URI annotation is treated as portable schema assertion;
- a consumer-specific frame or topology enters the generic baseline; or
- any required review, acceptance, or publication gate is inferred from green
  local checks.

## Current State

- Product and source amendments: candidate complete;
- deterministic structural and digest qualification: passed and recorded in
  `.ai-workspace/comments/codex/20260821T023045Z_CHECKPOINT_stdo_2_4_2_pre_rc_qualification.md`;
- target release selection: `2.4.2`;
- draft release note and protected Product identity: reconciled;
- immutable RC: not created;
- independent exact-RC review: pending;
- human exact-carrier acceptance: pending;
- release branch and tag: absent;
- publication: pending.

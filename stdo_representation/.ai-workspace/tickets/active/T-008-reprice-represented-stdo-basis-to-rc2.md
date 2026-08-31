# T-008 — Reprice Represented STDO Basis To RC2

- id: T-008
- title: Reprice STDO Representation 2.5.0 to published Source STDO RC2
- type: change
- ticket_category: constitutional
- status: active
- review_status: in_progress
- goal: GOAL-007
- change_intent: >-
    Replace the represented and constitutional Source STDO RC1 basis with exact
    published RC2 while preserving the Product version, shape, dependency, and
    accepted Representation RC1 history.
- change_class: requirement_reprice
- re_entry_point: specification/requirements/REQ-P-BASIS-AND-IDENTITY.md
- triaged_at: 2026-09-01
- created_at: 2026-09-01
- updated_at: 2026-09-01
- owner: stdo_representation
- pen_holder: codex
- work_authorization: direct_human_authorization_2026-09-01

## Exact basis

- Source STDO release: `stdo://releases/v2.5.0-rc.2/`
- installed-manifest SHA-256:
  `313e23116623a3bfbe96d279e089489aac466584982e1c34171ef244f0ec680a`
- standards member aggregate:
  `a5910bc56b491b5c520910e7bdad0949c1283e8b71951f1079e1fd86f59d20e7`
- candidate artifact root:
  `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.2/`
- accepted frame basis: revision 14, SHA-256
  `6cc05636ea00797e44f6ebb661d342d5b8cfb59cbde2a81059062dddf6eb106f`
- acceptance decision SHA-256:
  `68394d5118a6250972aa06db995a5d020c2f09996c90b0dfe70d4d8e908e8eba`

## Scope

1. Reprice active WHAT, Product Definition basis, bootstrap, and operator
   documentation to exact published Source STDO RC2.
2. Present project frame basis revision 14 for Product-owner digest acceptance
   and keep the overlay's `reference_frame_bases` empty until that decision
   exists.
3. After acceptance and exact overlay binding, reproduce and review the RC2
   compression and logical constraint index, then reprice only the native
   instruction routes and proof surfaces required by the unchanged Product.
4. Preserve semantic version `2.5.0`, the eight-member Product shape, exact
   Axiom Indexer `v0.1.0-rc.1` dependency, and all published Representation RC1
   refs, bytes, claims, decisions, and evidence.

## Refusal

- Do not reuse revision 13 acceptance for changed revision 14 bytes.
- Do not substitute mutable Specification Methodology source for immutable
  Source STDO RC2.
- Do not infer frame activation from authorship, validation, artifact presence,
  prior acceptance, or this ticket.
- Do not add a local engine, prompt orchestrator, GTL, automatic frame
  selection, or Product member.
- Do not publish or move any STDO Representation ref under this ticket without
  a separate exact release grant.

## Current gate

Authority has been repriced to RC2. Product-owner decision
`20260901T074151_frame_basis_rev14_acceptance.json` accepts the exact revision
14 digest and the Product Definition binds it. Artifact, skill, checker, test,
dogfood, and candidate-review closure remain; this ticket still grants no
STDO Representation publication.

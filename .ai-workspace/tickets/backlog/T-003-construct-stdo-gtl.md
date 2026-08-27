# T-003 — Construct STDO.gtl

id: T-003
title: Construct STDO.gtl
type: feature
ticket_category: ordinary
status: backlog
goal: GOAL-002
change_intent: construct and measure the first frozen-GTL F_P reasoning program after profile acceptance
change_class: design_reframe
re_entry_point: Design
triaged_at: 2026-08-27T19:41:42+10:00
created_at: 2026-08-27T19:41:42+10:00
updated_at: 2026-08-27T21:40:57+10:00
source_ticket: T-002
build_tenant: urn:stdo-representation:build-tenant:gtl
dependencies: T-002 closure and digest-bound acceptance of the GTL representation profile
required_what_member_set_identity: sha256:6680891f81cae91b92f5fff57d65ae70daa8c4f7e768124a13a5845e3f66f681
required_frame_basis_identity: urn:stdo-representation:reference-frame-basis:source-project:2
required_frame_basis_sha256: sha256:29864f77f5e79fce3e67287d8284566b30569fed348a59ff14223d52ee0e0437
required_profile_identity: urn:stdo-representation:gtl-profile:stdo-gtl:0.3.0
required_profile_sha256: sha256:629af635a3257253b17d66be9986d93ab8a22f13f8a5abb1bec5f24e8e245547

## Outcome

Construct the canonical `stdo.gtl` program from exact Source STDO and frozen GTL
after the accepted design gate opens.

## In scope

- Build the exact Source STDO graph-and-constraint program directly in GTL.
- Author and accept the exact `F_H` Semantic Selection Ledger before `F_D`
  serialization.
- Reproduce canonical bytes and structural validation.
- Measure exact bytes, tokens, and estimated context cost.
- Run frozen representative and adversarial `F_P` consumption observations.
- Prepare an immutable Product candidate for independent review.

## Out of scope

- Changing common WHAT or the accepted profile during construction.
- Deterministic semantic assessment of workspaces or model responses.
- Embedded HoG or ABG execution; an external host owns the ODD `F_P` invocation.
- JSON Schema tenant work.
- Release or tag creation without separate acceptance.

## Admission gate

This ticket remains backlog and non-executable until T-002 closes, the Project
Reference-Frame Basis is accepted, and human authority accepts the exact profile
identity and digest cited by this ticket. Ledger authorship and acceptance then
precede deterministic serialization.

## Acceptance

- `stdo.gtl` is canonical, content-addressed, structurally valid, and exactly
  basis-bound.
- Its accepted Semantic Selection Ledger covers the exact 47-member Source STDO
  population and its retained-reference union equals `I_B`.
- Rebuilding from exact inputs reproduces the same bytes.
- Measurements compare exact like-for-like Source STDO and program payloads.
- `F_P` observations and uncertainty are retained without deterministic closure
  claims.

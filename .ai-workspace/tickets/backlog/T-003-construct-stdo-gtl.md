# T-003 — Construct STDO.gtl

id: T-003
title: Construct STDO.gtl
type: feature
ticket_category: ordinary
status: backlog
goal: GOAL-002
change_intent: construct and measure the first frozen-GTL F_P reasoning program and role-bound context projections after profile acceptance
change_class: design_reframe
re_entry_point: Design
triaged_at: 2026-08-27T19:41:42+10:00
created_at: 2026-08-27T19:41:42+10:00
updated_at: 2026-08-28T02:58:41+10:00
source_ticket: T-002
build_tenant: urn:stdo-representation:build-tenant:gtl
dependencies: T-002 closure and digest-bound acceptance of the GTL representation profile
required_what_member_set_identity: sha256:8413bf3ae62f00e734d5c2096334acb350b2edc33e716ebb3e19fe2a162ebc48
required_frame_basis_identity: urn:stdo-representation:reference-frame-basis:source-project:3
required_frame_basis_sha256: sha256:b7768ee2331da77f30c485ff956e6b8b462a30f40b179f163baf92662f281852
required_profile_identity: urn:stdo-representation:gtl-profile:stdo-gtl:0.4.0
required_profile_sha256: sha256:7d207c24ba059530dc1ec217859b3d811ea8b5acc12ed4849a7ec13d1e6d7143

## Outcome

Construct the canonical `stdo.gtl` program from exact Source STDO and frozen GTL
after the accepted design gate opens.

## In scope

- Build the exact Source STDO graph-and-constraint program directly in GTL.
- Construct representative Executive, Worker, and Reviewer Context Packets from
  frozen assignments using the common least-closure contract.
- Author and accept the exact `F_H` Semantic Selection Ledger before tenant
  serialization and `F_D` evaluation of the resulting declared properties.
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
- Repeating each frozen role assignment reproduces its exact included and
  omitted identity sets, projection digest, and token count or the declared
  hold.
- Its accepted Semantic Selection Ledger covers the exact 47-member Source STDO
  population and its retained-reference union equals `I_B`.
- Rebuilding from exact inputs reproduces the same bytes.
- Measurements compare exact like-for-like Source STDO and program payloads.
- `F_P` observations and uncertainty are retained without deterministic closure
  claims.

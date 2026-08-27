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
updated_at: 2026-08-27T19:41:42+10:00
source_ticket: T-002
build_tenant: urn:stdo-representation:build-tenant:gtl
dependencies: T-002 closure and digest-bound acceptance of the GTL representation profile

## Outcome

Construct the canonical `stdo.gtl` program from exact Source STDO and frozen GTL
after the accepted design gate opens.

## In scope

- Build the exact Source STDO graph-and-constraint program directly in GTL.
- Reproduce canonical bytes and structural validation.
- Measure exact bytes, tokens, and estimated context cost.
- Run frozen representative and adversarial `F_P` consumption observations.
- Prepare an immutable Product candidate for independent review.

## Out of scope

- Changing common WHAT or the accepted profile during construction.
- Deterministic semantic assessment of workspaces or model responses.
- HoG or ABG execution.
- JSON Schema tenant work.
- Release or tag creation without separate acceptance.

## Admission gate

This ticket remains backlog and non-executable until T-002 closes and human
authority accepts the exact profile bytes and digest cited by the activation.

## Acceptance

- `stdo.gtl` is canonical, content-addressed, structurally valid, and exactly
  basis-bound.
- Rebuilding from exact inputs reproduces the same bytes.
- Measurements compare exact like-for-like Source STDO and program payloads.
- `F_P` observations and uncertainty are retained without deterministic closure
  claims.

# T-001 — Bootstrap STDO Representation

id: T-001
title: Bootstrap STDO Representation
type: feature
ticket_category: ordinary
status: completed
goal: GOAL-001
change_intent: establish the initial carrier-neutral STDO Representation source project
change_class: product_reprice
re_entry_point: Product
triaged_at: 2026-08-27T17:52:36+10:00
created_at: 2026-08-27T17:52:36+10:00
updated_at: 2026-08-27T19:41:42+10:00

## Outcome

Establish the initial check-in-ready carrier-neutral source project with GTL and
JSON Schema registered as independent HOW tenants.

## In scope

- Rename the source project and Product identity from GTL-specific to
  carrier-neutral STDO Representation.
- Pin the constitution to exact installed STDO `v2.4.3-rc.3`.
- Register GTL and JSON Schema tenant roots and bind the frozen GTL authority
  only inside the GTL tenant.
- Generate stable agent bootstrap files.
- Create the public `foolishimp/stdo_representation` repository and publish
  `main`.

## Out of scope

- Accepting a tenant representation profile or constructing a program.
- Selecting a JSON Schema dialect.
- Executing STDO or selecting HoG or ABG.
- Creating a Product release or tag.

## Historical closure

The repository topology, exact STDO/GTL basis bindings, tenant boundaries,
bootstrap surfaces, and public `main` branch were established at
`a0b12fa75c7d043eddd74b1d89252e53a3b75dad`.

The original ticket also described the Product as a deterministic carrier
assessment and claimed a total assessment law. Those claims were later
falsified and are not current closure truth. Active successor T-002 explicitly
reprices Intent, Product, requirements, governance frames, and the proposed GTL
profile around an `F_P` reasoning program. T-001 therefore records historical
bootstrap completion only and cannot close current GOAL-001.

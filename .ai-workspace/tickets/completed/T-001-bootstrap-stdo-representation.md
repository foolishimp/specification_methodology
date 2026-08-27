# T-001 — Bootstrap STDO Representation

Status: completed
Goal: GOAL-001
Change class: `product_reprice`

## Outcome

Establish a check-in-ready carrier-neutral source project in which the
Representation Algebra is constitutional WHAT and GTL and JSON Schema are
independent HOW tenants.

## In scope

- Rename the source project and Product identity from GTL-specific to
  carrier-neutral STDO Representation.
- Pin the root constitution to exact installed STDO `v2.4.3-rc.3`.
- Define basis, identity, algebra, projection, coverage, measurement,
  regeneration, conformance, and disposition requirements.
- Register GTL and JSON Schema tenant roots, design surfaces, and representation
  surfaces.
- Bind the frozen GTL authority only inside the GTL tenant.
- Keep the JSON Schema tenant blocked until an exact dialect is selected.
- Generate stable agent bootstrap files and stage a validated initial inventory.
- Create the public `foolishimp/stdo_representation` GitHub repository, commit
  the accepted baseline, and publish `main`.

## Out of scope

- Selecting a JSON Schema dialect.
- Accepting either tenant's representation profile or design.
- Constructing GTL or JSON Schema representation artifacts.
- Selecting a shared serialized intermediate graph.
- Executing STDO or selecting HoG, ABG, an executor, or runtime behavior.
- Creating a candidate Product, Product release, release tag, CI workflow, or
  branch-protection policy.

## Acceptance

- The Product Definition parses, validates, and verifies against its exact STDO
  basis.
- Root constitutional authorities contain no GTL or JSON Schema carrier basis.
- Requirements define a carrier-independent algebra and total assessment law.
- The Tenant Registry contains exactly GTL and JSON Schema HOW realizations.
- The GTL tenant records commit
  `8d7f965a3fae7d1acea6a9db298798480fd4cc2f` and authority-tree SHA-1
  `21a44b1941a1055d6abd973937e65b83e359de1b`.
- The JSON Schema tenant declares its missing exact dialect as a blocking gate.
- No tenant profile, representation artifact, shared IR, or execution surface
  is selected by implication.
- Bootstrap is idempotent, every overlay locator resolves, and the staged Git
  inventory passes whitespace and structural checks.
- The GitHub repository is public with default branch `main`, and local `main`
  equals `origin/main` after the initial push.

## Closure

The carrier-neutral WHAT, two tenant boundaries, exact STDO and GTL basis
bindings, agent bootstrap, public source repository, and initial `main` branch
satisfy this ticket. No Product candidate, release, or tag is created.

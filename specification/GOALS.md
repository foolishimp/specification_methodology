# STDO Representation Goals

## GOAL-001 — Establish the carrier-neutral representation source project

Status: complete

Establish the constitutional WHAT, exact source basis, independent build-tenant
boundaries, and acceptance gates needed before any carrier realization begins.

### Current selection

- Use `../stdo_representation.json` as the Product Definition overlay.
- Govern the source project with exact STDO cut `v2.4.3-rc.3`.
- Define the STDO Representation Algebra and its conformance obligations in
  requirements.
- Register GTL and JSON Schema as independent HOW tenants.
- Keep tenant representation profiles, concrete artifacts, and releases
  unselected until their designs are separately reviewed and accepted.
- Keep execution, HoG, and ABG outside the Product boundary.

### Completion conditions

- The Product Definition validates against its exact STDO schema and verifies
  its installed immutable basis.
- `AGENTS.md` and `CLAUDE.md` are generated from the selected STDO bootstrap
  entrypoint.
- Intent, Product, and requirements are carrier-neutral and make the abstract
  algebra decidable before tenant design.
- The GTL carrier authority is confined to the GTL tenant.
- The JSON Schema tenant fails closed until an exact dialect is selected.
- Each tenant has a located root, design surface, and representation surface.
- No shared serialized intermediate graph or execution surface is introduced.

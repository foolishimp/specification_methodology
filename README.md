# STDO Representation

STDO Representation defines a carrier-independent algebra for representing an
exact STDO release compactly, faithfully, and traceably within bounded machine
and LLM contexts.

The Product is representational only. It does not execute STDO, select an
executor, traverse with HoG, or admit ABG runtime truth.

## WHAT and HOW

The constitutional WHAT owns:

- the STDO Representation Algebra;
- semantic identity, authority, bounded-context, dependency, composition,
  overlay, projection, and residual laws;
- complete coverage and gap classification;
- compression, context-budget, regeneration, and conformance obligations; and
- the conditions under which an assessment may claim a complete or limited
  representation.

The algebra is an abstract semantic contract. It is not a serialized graph,
intermediate representation, JSON shape, or GTL Program.

Independent build tenants own HOW realizations of the same algebra:

- `build_tenants/gtl/` maps the algebra into the frozen GTL 3 language;
- `build_tenants/json_schema/` maps it into canonical JSON documents validated
  by a selected JSON Schema dialect.

Each tenant must publish its own representation profile, exact carrier basis,
canonical artifacts, source-address map, coverage matrix, boundary findings,
measurements, and conformance evidence. A tenant may expose a carrier limit; it
may not redefine the common algebra to conceal one.

## Current basis

The source project is governed by exact STDO cut `v2.4.3-rc.3`, manifest
SHA-256 `312c84609866a4b8ea665bbbc87eb16ef3a3bb28acc234da6d081065af40d551`.

The [GTL tenant](build_tenants/gtl/design/GTL_BASIS.md) selects its frozen
carrier basis independently. The
[JSON Schema tenant](build_tenants/json_schema/design/JSON_SCHEMA_BASIS.md) is
registered but has not selected a dialect. Neither tenant has an accepted
representation profile, implementation, candidate, or released Product.

## Authority

Read the project surfaces in this order:

1. [`specification/GOALS.md`](specification/GOALS.md)
2. [`specification/INTENT.md`](specification/INTENT.md)
3. [`specification/PRODUCT.md`](specification/PRODUCT.md)
4. [`specification/requirements/`](specification/requirements/)
5. the selected tenant's `design/` surface
6. the selected tenant's representation artifacts, once authorized

The layout-neutral Product Definition is
[`stdo_representation.json`](stdo_representation.json).

## Checks

```sh
stdo verify v2.4.3-rc.3
stdo status --definition stdo_representation.json --verify
stdo bootstrap --definition stdo_representation.json --dry-run
```

# Standards Templates

This directory holds starter templates for shared specification surfaces and
agent bootstrap surfaces.

Use these templates as source material for project-local files such as:

- `stdo_default.json` or `stdo_<label>.json`, copied from
  `PRODUCT_DEFINITION_TEMPLATE.json`
- `GOALS.md`
- `INTENT.md`
- `PRODUCT.md`
- `CLAUDE.md`
- `AGENTS.md`

When a template contains install-local placeholders such as
`<workspace-root>` or `<method-standards-root>`, replace them with the values
for the target workspace.

## Product Definition Overlay

`PRODUCT_DEFINITION_TEMPLATE.json` is the one per-product fill-in overlay. Its
normative schema is `../schemas/product-definition.schema.json`.

Copy it to the logical root of one product definition:

- use `stdo_default.json` for a singleton default project;
- use `stdo_<label>.json` for a named product;
- place several `stdo_<label>.json` files at one monorepo root when that root
  hosts several distinct product `WHAT` definitions; or
- place one or more definitions at arbitrarily deep nested project roots in a
  hierarchical repository.

The containing directory is the definition root. Resolve relative URI
references from the copied JSON file. Fill its bindings over the project's
existing files and systems; do not restructure an existing project merely to
match the default paths in the template.

The template's `$schema` value assumes the selected standards are installed at
`.genesis/docs/standards/` relative to that definition root. Replace it with
the selected released schema URI when the install is elsewhere, including for
a definition nested below a workspace-level standards install.

One definition represents one distinct product `WHAT`. Put multiple
independent realizations of that same `WHAT` in `how.build_tenants`, not in
additional definition files.

`reference_frame_bases` is required and non-empty. Point each `uri` at the
accepted project frame-basis declaration already carried by Product,
requirements, local constitutional authority, accepted design, or another
lawful surface. Bind every admitting authority and exact governed scope. The
default placeholder does not require a new file or fixed location. Do not put
agent identities or temporary frame activations in the Product Definition
Overlay; their authorized work instruction or activation packet cites the
applicable basis.

Replace at least:

- `$schema` when the default install-relative URI does not resolve;
- `product.definition_id`, name, source-project locator, and bounded-context
  declaration, keeping definition identity distinct from immutable Product and
  release identities;
- the immutable STDO release tag in `constitution.authorities`;
- constitutional entrypoints and every local constitutional relation;
- collective reference-frame basis URIs, admitting authorities, and scopes;
- Intent, Product, and specification URIs;
- shared and tenant-local `HOW` URIs;
- Goals, ticket, comment, and optional sprint carrier URIs; and
- explicit composition edges to other `stdo_*.json` definitions, including
  expected target definition identity, relation authority, and at least one
  governing contract.

Set `product.bounded_context` to `null` when the product does not claim a
separate bounded context. Empty local-constitution and composition arrays are
explicit declarations of none.

Portable Draft 2020-12 schema validation proves JSON shape. Use an
assertion-capable RFC 3986 validator for the annotated URI and URI-reference
formats, then resolve every URI and fragment, verify the selected immutable
constitutional set, confirm unique definition and tenant identities, verify
composition target identities and contracts, and evaluate constitutional
sufficiency and authority congruence under `SPEC_METHOD.md`.

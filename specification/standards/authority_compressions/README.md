# Authority Compression Assets

These files are source-maintained compressed read models over one complete
released STDO cut. They are prompt-construction inputs, not replacement
constitutional authority and not independently selectable method versions.

The source method, profile, and schema documents remain the deciding sources:

- `../REFERENCE_FRAME_METHOD.md`
- `../STDO_REFERENCE_FRAME_BASELINE.md`
- `../SPEC_METHOD.md`
- `../schemas/product-definition.schema.json`
- `../schemas/installed-release-manifest.schema.json`
- `../DESIGN_MODULE_METHOD.md`
- `../ODD_METHOD.md`
- `../WORLD_MODEL_METHOD.md`
- `../TICKET_METHOD.md`
- `../UX_METHOD.md`
- `../IDENTITY_METHOD.md`
- `../RELEASE_METHOD.md`
- `../POSTING_GUIDE.md`

`../GLOSSARY_GUIDE.md` is a non-deciding semantic locator index. The aggregate
compression watches it through separate `index_refs` and `index_digests` fields
so locator drift makes the aggregate stale without promoting the index to an
owner of meaning.

Each compression file carries the deciding source path and digest it was
derived from. The aggregate also carries watched index paths and digests. If a
source or watched-index digest changes, the compression is stale and must be
regenerated or explicitly reaccepted before installation treats it as current.

Installed workspaces consume compressions and source standards from the same
selected release identity. Mutable upstream source must not replace that basis.
Raw selected-cut standards remain deciding authority when a compression is
insufficient or stale.

`stdo_bootstrap.md` is the smallest discovery projection. Marker-managed agent
files route to it through the applicable Product Definition; it then routes to
the exact installed basis and raw owners. It is digest-bound to Specification
Method, Release Method, and the Product Definition schema and cannot select or
replace them.

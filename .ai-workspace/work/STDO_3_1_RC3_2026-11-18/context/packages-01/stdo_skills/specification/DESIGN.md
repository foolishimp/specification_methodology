# Current Skills design

One shared adapter verifies external public manifests and delegates CLI calls.
Purpose Context owns the entire index/runtime mechanism and canonical authoring
skill. `skills/stdo-context/scripts/provider.py` performs dependency identity and
subprocess forwarding only. Its `BINDING.json` locates the exact source or installed
configuration. Source dependency roots are relative to the composition file;
installed roots and interpreter are explicit absolute pins.

`scripts/package.py` copies current public Skills source into a
fresh directory and records every member in INVENTORY.json. The selected package's
`scripts/manage_skills.py` validates its full population, exact native method
manifest/plugin and all selected external Product members before writing. It
creates native core wrappers with original frontmatter and canonical references,
one thin context adapter, current Getting Started/installation guides and a
configuration/receipt. Native wrappers link to the installed current guide for
package setup and purpose selection; their native workflow reference remains
unchanged. The guide copies are included in the existing receipt-owned bundle.
Claude also binds the native refresh workflow. The optional visual selection
adds stdo-project only.

The dependency configuration separately pins Purpose Context and the visual
Product; their versions, inventories and Product identities are never conflated
with Skills or the native method. No runtime source is copied into Skills. Verify
rechecks the native manager/store and selected components; remove checks exact
owned files but does not require providers to remain available.

Installation targets fresh workspace roots and refuses collisions. A failure
after effects retains partial files for reconciliation; it does not claim rollback.
The caller supplies the exact receipt digest for verification/removal. There is
no global installation, automatic update or legacy receipt migration.

Both host designs share this implementation. Their current visual instructions
are under `build_tenants/<host>/current/skills/stdo-project/`; they do not implement
another native lifecycle, context engine or formal route.

The wrappers route relevant SDLC decisions to the same Purpose Context adapter
after native intake. The canonical Product skill chooses the declared workflow
purpose, distinguishes actual decision facts from future evidence, and preserves
the selected default's source routes. There is no second review state machine in
Skills. A development-source context binding is forwarded through the existing
CLI just like a released-source binding, while the native installation remains
separately verified. Exact-file use of changed native source instructions and
local installed adapter use are recorded separately in candidate qualification.

## Exact release package mode

Release packaging requires an explicit version and actual native manifest/root.
It emits `stdo-skills.release-package/1` with the exact method URI/digest. The
installer requires the consumer Product's verified basis to equal that binding.
Its release runtime and receipt retain the same identity and use the owned
`stdo-skills/` bundle; development mode retains `stdo-skills-dev/`. Both modes
share validation, native wrapper creation, external dependency checks and exact
receipt-owned removal. The supplied receipt digest selects one exact receipt,
never another installation. Shared skill destinations still refuse collisions.

Neither package mode changes a Product basis, refreshes global registrations or
authors an assessment. A released package's publication and qualification are
external evidence; an installation proves only its stated binding checks.

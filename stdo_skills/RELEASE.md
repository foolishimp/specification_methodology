# STDO Skills 3.1.0-rc.3 package and migration

This release target has Product identity
`urn:stdo:product-definition:stdo-skills` and an explicit relation to the exact
native Method, Purpose Context, and optional visual Product. Matching version
suffixes do not merge their Product identities or assessment claims.

Use the shared release recipe to acquire the native Method through its manager.
The published native manifest is `stdo-v3.1.0-rc.3-manifest.json`. The separate
Product archive is `stdo-products-v3.1.0-rc.3.zip`; its exact cohort inventory is
`cohort-release-v3.1.0-rc.3.json`. Obtain all assets from the same immutable
release and verify the published identities before extraction/use. The archive's
`stdo_skills` directory is an inventoried package; `purpose_context` and `a_c`
remain separately inventoried Products. Follow [installation](scripts/INSTALLATION.md)
with those exact paths and the native manager's verified installation root.

The versioned package records its actual native method URI and manifest digest.
Installation requires the consumer Product Definition to select that same
complete cut. It verifies the native manager/plugin, selected interpreter and
every public component member, then writes fresh workspace bindings and an exact
receipt. Codex receives the native five core workflows; Claude also receives
native refresh. Both consume the canonical Purpose Context Product. Visual
documentation is explicitly selected and has no Lean or context prerequisite.

The new release runtime uses `stdo-skills/` under the selected host root and a
`stdo-skills.receipt.json`. Development mode retains `stdo-skills-dev/` and its
original receipt kind. Both modes reject collisions at shared skill roots and
verify/remove only the exact receipt-owned population. An interrupted install
retains its partial effects for reconciliation; a refusal is not a rollback.

An existing consumer remains on its current basis and installation until its
Product authority selects migration. Retain that installation's package and
receipt, reconcile local changes, and use its owning installer for removal only
when that replacement is authorized. Then select the new complete native basis
and default through the applicable Product adoption route, and install into fresh
roots. Do not delete broad host directories or rewrite legacy receipts. Historical
3.0.5-era packages require their original installer. Release publication does not
change global registrations or existing Product definitions.

Purpose Context preserves old exact entries and adds separate Python and SDLC
entries for the actual native 3.1 cut. Follow [Getting Started](GETTING_STARTED.md)
to select the actual purpose/query. A new query inherits no semantic assessment;
release publication, installation, complete context receipt and task success
remain distinct claims. Independent assessments and native-use results are
external exact-subject evidence. Automatic host pickup and general effectiveness
are claimed only where actually observed.

The source Purpose Context manifest includes historical entries; the curated
portable release manifest selects only the two current 3.1 entries. The release
package's dependency declaration pins that actual portable tree. Its inventory
records the transformation from the source dependency declaration, and Purpose
Context's `SOURCE_RELATION.json` records its catalog projection. Use the final
package pin when checking the installed path; the source pin is a different
explicit subject.

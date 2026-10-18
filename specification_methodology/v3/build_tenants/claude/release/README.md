# Release record

The RC1 release note is [release-note.md](release-note.md), reconciled to the
freeze commit that holds it; the manifest follows in commit B. The
paragraphs below record the standing before the cut and stay as history.

Before the cut this candidate carried no release note. A release note is a release-scoped
surface that is reconciled to the exact RC subject before publication
([RELEASE section 6](../standards/RELEASE.md#6-release-scoped-assets-and-the-product-subject)),
and in a coordinated cohort the release record is frozen with the corpus
and the plugin in commit A of the cut
([RELEASE section 7](../standards/RELEASE.md#7-coordinated-release-matched-asset-cohorts)).
The note for this successor is therefore written at its RC cut, not during
construction.

Target version and standing. The successor this candidate constructs
targets version `3.0.0` of the release line, the version the common
Product names for this construction. The target is a fact about intent:
no member carries a version label; the plugin manifests carried
`REPLACE_AT_RC_CUT` until the RC cut, where the label `3.0.0-rc.1` was
applied. The candidate
is unreleased: no RC has been published, no acceptance is recorded and no
selector has advanced. A version label alone would establish no released
status; released standing comes from the acceptance record of
[RELEASE section 8](../standards/RELEASE.md#8-acceptance) and the common
tickets, and this record distinguishes the two.

The predecessor's `release/release-note.md` (SHA-256
`2593a003a5cddccc225bfdd450f71be627453bc48dd80fbad55e298f5fbc34fe`)
records the facts of the cut `v2.5.1-rc.2`: its identity and refs, its
change and qualification summary, and its standards, plugin and manager
inventories. Each is a fact of that cut and none governs a successor, so
its frontier row is disposed `not applicable` with this reason.

The installed-release manifest is written at the same cut under RELEASE
and validates against
[the manifest schema](../standards/schemas/installed-release-manifest.schema.json).
No frontier row exists for the predecessor's `manifest.json`.

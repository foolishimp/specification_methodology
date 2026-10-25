# Extracted documentation/custody navigation review

Changes requested: one P3 portability/documentation defect, independent of the closed F001 receipt-binding repair.

## F002 — Captured source-readiness instructions appear portable but require omitted workspace files

The frozen packager copies `SOURCE-READINESS.md` unchanged into the bundle. That document tells a reader, “From this application directory,” to run `python3 -B freeze_sources.py --check` and a repository replay command (`SOURCE-READINESS.md:71–84`). The extracted artifact contains no `freeze_sources.py`, and the document does not mark that section as captured originating-workspace instructions.

From the already extracted synthetic repaired fixture, the advertised local check exits2: Python cannot open `freeze_sources.py`. The document’s two final proof/ticket links resolve above the extracted bundle to absent `.ai-workspace` paths. The other four local source/manifest links resolve. See [evidence.json](evidence.json) for the command, exact stderr, file identities and link resolutions.

A recipient following the bundled custody document therefore cannot reproduce its advertised check or follow those evidence routes using the supplied package. The top-level portable `release_tools/bundle_check.py .` instructions remain valid; this finding concerns the copied source-readiness document’s scope and navigation, not source corruption or the prior67 binding controls.

Minimal repair: clearly label the copied document as captured originating-workspace provenance, identify its `freeze_sources.py`/Git/proof/ticket routes as workspace-only, and direct extracted-bundle readers to the existing portable checker and bound public receipts. A small package-facing wrapper/banner can preserve the captured original account. Copying private `.ai-workspace` trees is unnecessary. If the package instead promises the original freeze command, supply and qualify its exact needed dependencies and public evidence routes.

Scope: frozen packager SHA256 `8439938a7937bb44eecc50571c90d71fad9405ba5bc2f4eb28abbdd5379593c6`, checker `74beb6365104bc4352b691725c9e18fe3521d01fe50a080c0c9cc735a4a141f5`, and the existing synthetic extracted fixture only. No actual common model draft was inspected. No candidate/app/source/code/Git edit, browser/server, native/model or network effect occurred. F001’s closed no-actionable-defect binding-repair result remains valid within its declared scope.

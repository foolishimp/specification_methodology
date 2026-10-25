# Independent packaging preparation review

Changes requested: one reproducible P2 contract defect. This is a bounded review of frozen packaging code, not the not-yet-built common representation or a release decision.

## F001 — A review of another model is accepted into a passing bundle

`package_release.py:361–385` checks the public authoring receipt only as an object and review inputs only by text/JSON suffix; it copies review bytes and records their hashes without requiring their represented subject or exact model identity/digest. `release_tools/bundle_check.py:174–212` does not inspect the release receipt or review bindings.

An otherwise eligible synthetic fixture explicitly used all845 frozen common section coordinates, with ordinary inert toy semantics and no claim of common semantic fitness. A JSON review explicitly named `urn:other:source`, `urn:other:model` and the all-zero model digest, and declared the packaged subject unreviewed. `build()` nevertheless returned `local_bundle_prepared`, and the extracted portable checker returned `passed`. This is not a semantic judgment the packager must make: it can check the supplied review’s exact subject/model coordinates without deciding its findings or acceptance.

Require a structured exact binding for the selected public review and verify it before output and again on portable replay. An arbitrary Markdown/text review may remain evidence behind that bound receipt. Preserve its decision/limits; do not synthesize a positive review or acceptance. Regression controls should include a correctly bound review and wrong-subject/wrong-identity/wrong-digest controls.

Reproduction: [run_controls.py](run_controls.py) and [first-controls.json](first-controls.json). These write only reviewer scratch/proof and never touch the actual in-progress common model.

## Passing controls and conserved boundaries

The24 independent controls in [extended-controls.json](extended-controls.json) passed: clean extracted Python `-S` standard-library replay; missing/tampered model, carrier, source, runtime and missing review rejection; deterministic byte-identical archive recreation; safe sorted relative regular archive members with fixed metadata; symlink/path traversal refusals; local SRI-pinned runtime; source line anchors; record-browser JavaScript syntax; explicit proposal/source-not-ready/license boundaries; no recursively included private actor/run files. No browser or server was launched. Interactive behavior remains unverified.

All24 prepared-file pins matched before and after controls. Reviewed packager SHA256 `ec64283b2f2381a0a2a6db2b792bf11cb4c020cd033ecb85da2a7bff34b469bc`; portable checker SHA256 `16f0001b3659aaa8cd326c551b6eb7e9e349c4871525468c17f5a3f50b1fbb0c`. Full pins are in the preparation closure and first control record.

The source oracle predates candidate exposure and binds AC-R-001..015, the exact installed v2.5.1-rc.2 calculus, generation/codec contracts and the authorized release-preparation boundary. I did not author source freeze, model or packaging; provider-family independence is not certified. Public receipt curation remains an explicitly external author responsibility; no raw private author evidence was inspected.

No actual common final bundle/archive existed during these checks. This result does not establish common semantic fidelity, complete acquisition, actual browser behavior, source-method release readiness, distribution permission, acceptance or publication. The source remains unaccepted/unpublished/not_ready, and a_c-owned licensing is a reserved owner prerequisite. No candidate/spec/source/Git repair was performed.

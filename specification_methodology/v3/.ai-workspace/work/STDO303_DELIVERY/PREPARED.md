# STDO 3.0.3 — immutable-source preparation

The reviewed candidate is checkpointed on `main` at
`b90789488237094ae2f29241c58ce71f12450a59`, with predecessor source checkpoint
`9c9626ffd20ea88a75ac8143802c13f4f828ec1c`. The candidate commit contains 78
selected source, documentation, tooling, review and evidence files. All 128
technical pins in [SOURCE_FREEZE.json](tooling-integration-001/SOURCE_FREEZE.json)
remain exact. The [independent review](pre-release-review-001/INDEPENDENT_REVIEW.md),
SHA-256 `1958bdb65cd0b73670579472bcc517066142bdb07466f79d4b44c2bc7a3924b1`,
is closed with no open actionable S0–S4 finding in its bounded scope.

`build_tenants/common-tools/native_release.py prepare` read the immutable
candidate's `specification_methodology/v3/build_tenants/common` tree
`2c8be59c79bb00371253204b48b7c896bb4260ad`. The resulting preparation selects
**106 native files / 43,056,988 bytes**, with inventory SHA-256
`178348b27a89d08a99a445157a3e78ba8e79a834350f4422da33762e92f41cc5`.
Every selected blob was independently read back from Git and checked against
its recorded size and SHA-256. The prepared index vector was checked exactly.
The native predecessor remains published STDO 3.0.2 commit
`23ca9c0929d7be8570edafaf30542e3daeb8dc1f`.

| Preparation record | SHA-256 |
| --- | --- |
| [source.json](native-release/source-preparation-001/source.json) | `3e8f721e481cf7b6eda0fd31e2b5bb9211c2b9a8caeb868124cd3b5871ab3d71` |
| [native-index-info.z](native-release/source-preparation-001/native-index-info.z) | `b4fd054739a32455b4b5ab46ab37c46f1bfc5aea790e40e77bee0c5b08cd2cec` |
| [native-commit-message.txt](native-release/source-preparation-001/native-commit-message.txt) | `b5e0eeaba00ef1b6c8935d7c0f40f2ff88c3ee485949689bd4a462659b5ad0a7` |
| [tag-message.txt](native-release/source-preparation-001/tag-message.txt) | `b1599f6bafa4b4f9360ca271975b5347583a7e69a373ccc99cc5cb3713e485c0` |

The sole cached-whitespace exception is the terminal blank line in retained
`tooling-integration-001/attempt-001-installed-tooling.log`. The Executive
explicitly retained this diagnostic evidence unchanged; every other staged
file passed the whitespace check. No proof, source, payload or review pin was
changed to resolve a formatting warning.

The owner has authorized completion of STDO 3.0.3 release after the required
checks pass. This record covers source checkpoint and local preparation only.
The preparation step itself created no native release commit, tag, public
asset or shared installation, and adopted no consumer basis. Subsequent
[local native proof](native-release/release-run-01/LOCAL_RETURN.md) records the
actual native commit/tag, manifest seal and fresh isolated installation.
Source checkpoint push remains held for the complete publication plan.

Remaining prescribed steps are the guarded atomic publication with remote
readback, normal GitHub release/asset publication, and a fresh public
installation/verification of that exact cut. The historical Lean result,
static-browser limits and other qualification
boundaries retain the standing recorded by the independent review.

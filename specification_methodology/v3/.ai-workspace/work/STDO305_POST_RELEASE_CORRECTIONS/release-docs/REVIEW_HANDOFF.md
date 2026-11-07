# Unreleased F3/F4 correction

Preimage: `6edfffb2f8a35b244782749383fb19105d9227d9`. Root is Executive; `/root/stdo305_release_tools` is the Writer; `/root/stdo305_integration_review` independently reviews the frozen cut.

F3 changes the current proof-document producer and eight generated files. The two original documents remain exact, selected source bytes in `source-documents/*.md.txt`; installed-facing Markdown changes only a provenance notice and five link destinations. The links select immutable source checkpoint `2ee0147ad06b58dbdf6dad4b874c363a035aab9e`. All five targets and the admission-recipe fragment are checked through Git object reads. Opening those external targets requires network access; the proof reader and retained evidence still work offline. Existing historical/current scope is unchanged.

The catalog records distinct source and presentation identities. The current documentation selection is an explicit successor selecting that derived catalog. The original documentation selection is preserved in `before/documentation-SELECTION.json`; original proof SELECTION, evidence, model and source freeze are unchanged. The producer still checks exact pre-projection payloads using their original catalog/render contract and labels their installed source-relative links unqualified. It does not silently treat old links as repaired.

F4 repairs only the public-readback fixture: native manifest, manager wheel, offline runtime ZIP and dependency constraints are all selected before downstream checks. Three new tests cover missing, identity-tampered and publicly tampered ZIP/constraints assets through the real public consumer. Production fail-closed gate code is unchanged.

Validation:

- Original Python 3.13 suite: 55 tests, seven reproduced failures caused by incomplete public asset closure.
- Successor suite: 58 tests pass; intended safeguards and six ZIP/constraints subcases are reached.
- Seven projection/link/source-custody/historical-format tests pass, including immutable target/fragment checks.
- Existing current-assets suite: 14 active tests pass, four opt-in integration tests skipped. Bare Python lacked `jsonschema`; the preserved failed attempt was followed by a passing run in the existing dependency-pinned Python 3.13 manager environment. No dependencies were installed.
- Actual current proof-reader check passes in 3.22 s; documentation check passes in 3.58 s. These are custody/render checks, not new Lean execution or release qualification.
- Scoped `git diff --check` passes.

Preparation errors remain recorded: the first fixture repair omitted its required `name` field, and the first projection script used the wrong repository parent. Both failed before a successful correction output was claimed. Original independent preimage reports are retained byte-for-byte with custody.

`GATE_COST_STATIC.json` contains a bounded static count, not new profiling: 25 installation validations in each refs/published content pass, plus 13 fresh-public validations for 38 in the public phase. Prior whole-phase observations were 347.32, 348.14 and 500.16 seconds. This does not isolate per-validation cost. Rechecking mutable installations at separate phase boundaries remains distinct from repeated reads within a phase. No optimization was made.

Packaging impact: a future candidate must select the corrected producer, derived catalog/selection/inventory and two added custody files, and obtain its own native manifest/evidence as applicable. Published 3.0.5 assets, tags, stack manifest, installed stores and frozen qualification records remain unchanged; their five broken source-relative links are not repaired in place. No whole release rebuild, source/model/viewer/semantic regeneration, Git/index/ref or publication effect occurred.

The frozen subject is the 11 current changed source/test/derived files plus the evidence listed in `FREEZE.json`. Independent acceptance is pending.

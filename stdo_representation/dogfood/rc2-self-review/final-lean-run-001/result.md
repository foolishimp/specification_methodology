# Reference Frame Method Result

- **Result:** `falsified`
- **Frame:** `repo://specification-methodology/stdo-v2.5.0-rc.2/01238f901426807b5350e1013c85b8e5f4ebe29cf89c62a858707dd705d6415b/standards/STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame`
- **Subject:** commit `cfd1e3332cafadea6e2522fe7aaa0918163e5eca`; repository tree `f9d45347022989d476027630bb9d78498888e508`; methodology subtree `240e2ca6654db1f3e0a5acb08faaeb170944b610`; standards tree `002e9a81745412560a4c0300c6cbd5293f7a65d3f`.
- **Physical basis:** the 52-member aggregate recomputed as `01238f901426807b5350e1013c85b8e5f4ebe29cf89c62a858707dd705d6415b`; all five supplied primary-file hashes matched. The snapshot contains no Git object database, so commit/tree provenance was not independently recomputed.
- **Actor envelope:** independent, read-only Reviewer evaluation only.

## Finding RF-01 — `out_of_frame` is not semantically total

- **Severity:** S2
- **Affected claim:** `urn:stdo-representation:a-c-text:clause:reviewer-result-triage-is-total`; raw/compression/template congruence.
- **Causal mechanism:** RF-012 defines `out_of_frame` whenever evaluation requires an undeclared material relation **or capability**. The Reviewer projection instead classifies the entire branch as an “out-of-claim observation.” Those domains are not equal.
- **Counterexample:** after lawful Reviewer activation, evaluation discovers that an undeclared capability or material runtime relation is necessary to decide the exact in-claim predicate. RF-012 requires `out_of_frame`; it is not an adjacent observation outside that claim. The projection has no payload class preserving this case.
- **Scope:** every Reviewer evaluation where an in-claim material dependency or capability gap emerges after activation. The compression retains generic re-entry pressure, while the raw projection narrows it, and the project template does not provide a distinct branch that resolves the loss.
- **Workaround status:** bounded raw-owner re-entry remains available through RF-012 and the profile’s Missing-Frame application; the total projection itself does not encode the distinction.
- **Regression risk:** `indeterminate`; no change set or transition evidence is in frame.
- **Confidence:** high.
- **Residual uncertainty:** an adopting Product’s exact operational consequences are outside this subject, but cannot restore the missing semantic distinction.
- **Evidence/routes:**
  - `repo://specification-methodology/stdo-v2.5.0-rc.2/01238f901426807b5350e1013c85b8e5f4ebe29cf89c62a858707dd705d6415b/standards/REFERENCE_FRAME_METHOD.md#reference-frame-laws` — RF-003 and RF-012.
  - `repo://specification-methodology/stdo-v2.5.0-rc.2/01238f901426807b5350e1013c85b8e5f4ebe29cf89c62a858707dd705d6415b/standards/STDO_REFERENCE_FRAME_BASELINE.md#reviewer-result-and-triage-projection`
  - `repo://specification-methodology/stdo-v2.5.0-rc.2/01238f901426807b5350e1013c85b8e5f4ebe29cf89c62a858707dd705d6415b/standards/STDO_REFERENCE_FRAME_BASELINE.md#missing-frame-and-re-entry-application`
  - `repo://specification-methodology/stdo-v2.5.0-rc.2/01238f901426807b5350e1013c85b8e5f4ebe29cf89c62a858707dd705d6415b/standards/authority_compressions/stdo_compressed.md#reference-frame-engagement-compression`
  - `repo://specification-methodology/stdo-v2.5.0-rc.2/01238f901426807b5350e1013c85b8e5f4ebe29cf89c62a858707dd705d6415b/standards/templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md#technical-triage-and-promotion-policy`

## Finding RF-02 — branch and refusal proof is structural, not meaningful

- **Severity:** S2
- **Affected claim:** meaningful proof for the five Reviewer result branches, invalid-basis refusal, unsupported-assessment handling, and the Reviewer-to-Executive authority split.
- **Causal mechanism:** the qualification law requires representative positive, boundary, and falsifying cases for every evaluated branch. The supplied tests instead parse Markdown tables and assert row sets or substring presence. They instantiate no Reviewer activation, result payload, stale basis, capability gap, unsupported field, hard-stop interaction, or consuming decision relation.
- **Scope:** `satisfied`, `falsified`, `indeterminate`, `out_of_frame`, and `invalid_basis`, plus all four Executive constraint rows. The tests can pass despite RF-01 because they do not compare the profile’s branch meaning with RF-012.
- **Observed evidence:** all 13 tests passed, but the relevant assertions establish only text/table shape. The compression test similarly verifies selected phrases rather than semantic equivalence.
- **Workaround status:** bounded case-specific semantic review is possible from the raw owners; no reusable branch-discriminating proof is present in the exact evidence population.
- **Regression risk:** `indeterminate`; no proposed change is evaluated.
- **Confidence:** high.
- **Residual uncertainty:** the request supplies hashes—but not inspectable bytes—for the axiomatic program, constraint map, and validation report. Hashes alone cannot supply missing semantic proof.
- **Evidence/routes:**
  - `repo://specification-methodology/stdo-v2.5.0-rc.2/01238f901426807b5350e1013c85b8e5f4ebe29cf89c62a858707dd705d6415b/standards/REFERENCE_FRAME_METHOD.md#method-self-qualification`
  - `repo://specification-methodology/stdo-v2.5.0-rc.2/01238f901426807b5350e1013c85b8e5f4ebe29cf89c62a858707dd705d6415b/standards/STDO_REFERENCE_FRAME_BASELINE.md#profile-qualification`
  - `repo://specification-methodology/stdo-v2.5.0-rc.2/01238f901426807b5350e1013c85b8e5f4ebe29cf89c62a858707dd705d6415b/tests/test_reference_frame_boundaries.py#L115`
  - `repo://specification-methodology/stdo-v2.5.0-rc.2/01238f901426807b5350e1013c85b8e5f4ebe29cf89c62a858707dd705d6415b/tests/test_reference_frame_boundaries.py#L157`
  - `repo://specification-methodology/stdo-v2.5.0-rc.2/01238f901426807b5350e1013c85b8e5f4ebe29cf89c62a858707dd705d6415b/tests/test_reference_frame_boundaries.py#L195`

The normative authority split and evidence-bounded triage fields are otherwise coherent and proportionate; no independent authority-transfer defect was found.

**Invalidation conditions:** any change to the bound subject or aggregate; authoritative narrowing of Method-level `out_of_frame` to out-of-claim observations; or exact, inspectable branch-discriminating qualification evidence covering the affected semantic populations.

**Closed return to Executive:** `falsified`, with findings RF-01 and RF-02 and the stated residual uncertainty.
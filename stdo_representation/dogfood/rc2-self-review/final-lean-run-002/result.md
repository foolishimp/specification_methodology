# Frame Evaluation Result

- **Result:** `falsified`
- **Selected frame:** `repo://specification-methodology/stdo-v2.5.0-rc.2/787b49219db716e9a7acd60b780889365a78751ed604e610348734dc2ef71f4a/standards/STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame`
- **Subject:** commit `1126d21e23e8907ac0f6258450ef930f5560aa11`; tree `851241a6e00873ef437048d0d177eca5a6f4553a`; Specification Methodology subtree `9c99497a8e69b5533a9df85b3b3ca9c05aac4cdf`; standards tree `9421d06ee9a206db5cb15eee3cb4328cef486acb`.
- **Physical basis:** frozen snapshot `/tmp/stdo-rc2-final-lean-002-subject.qDWNA4/specification_methodology`.
- **Basis verification:** all five declared evidence-file SHA-256 values matched. The recomputed 52-member standards aggregate matched `787b49219db716e9a7acd60b780889365a78751ed604e610348734dc2ef71f4a`.
- **Reviewer authority:** evidence-bounded technical triage only.

## Finding RF-REV-001

- **Severity:** S2
- **Affected claim:** `reviewer-result-triage-is-total`; bounded-frame result coherence; both declared `out_of_frame` cases.
- **Causal mechanism:** The pure result algebra defines `out_of_frame` only when the evaluation requires an undeclared material relation or capability. The profile repeats that definition, but then selects the same result merely because an adjacent observation lies outside the evaluated claim. An outside observation does not, by itself, make the claim evaluation require that relation.

  This makes the projection non-exclusive. For an exact claim that is decidably satisfied while review also discovers an adjacent outside-claim observation, both the `satisfied` row and the outside-claim `out_of_frame` row apply. Selecting `out_of_frame` loses the valid claim verdict; selecting `satisfied` leaves the declared outside-claim branch without a selection rule. The same ambiguity exists when the claim is falsified.

  The baseline separately permits “adjacent observations” in the Reviewer payload, confirming that such observations need not replace the claim-relative result. Its missing-frame rule also says `out_of_frame` identifies something capable of changing the evaluation, which an established outside-claim observation is not.
- **Scope:** The outside-claim branch only. The in-claim branch—an evaluated claim requiring an undeclared material relation or evaluator capability—is coherent and preserves `indeterminate` triage and reconfiguration pressure.
- **Workaround status:** A bounded operational avoidance exists in the current sources through the core claim-relative algebra and the separate adjacent-observation payload. It does not remove the normative conflict.
- **Regression risk:** High for loss or misclassification of a valid claim verdict and for inconsistent consumers of the raw versus compressed projection.
- **Confidence:** High.
- **Residual uncertainty:** No precedence or conjunction rule states how a valid claim result coexists with an outside-claim observation. The compatible-extension allowance does not resolve this because the profile simultaneously retains the narrower core definition.
- **Exact evidence/routes:**
  - [REFERENCE_FRAME_METHOD.md:409](/tmp/stdo-rc2-final-lean-002-subject.qDWNA4/specification_methodology/specification/standards/REFERENCE_FRAME_METHOD.md:409), `repo://specification-methodology/stdo-v2.5.0-rc.2/787b49219db716e9a7acd60b780889365a78751ed604e610348734dc2ef71f4a/standards/REFERENCE_FRAME_METHOD.md#reference-frame-laws`
  - [STDO_REFERENCE_FRAME_BASELINE.md:1080](/tmp/stdo-rc2-final-lean-002-subject.qDWNA4/specification_methodology/specification/standards/STDO_REFERENCE_FRAME_BASELINE.md:1080), especially the result projection, both branch rows, and missing-frame application at lines 1214–1219.
  - [stdo_compressed.md:772](/tmp/stdo-rc2-final-lean-002-subject.qDWNA4/specification_methodology/specification/standards/authority_compressions/stdo_compressed.md:772), which faithfully compresses both branches but therefore preserves the conflict.
  - [PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md:72](/tmp/stdo-rc2-final-lean-002-subject.qDWNA4/specification_methodology/specification/standards/templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md:72), which preserves the authority split and the outside-claim non-blocking constraint but supplies no classification rule resolving the overlap.

## Finding RF-REV-002

- **Severity:** S2
- **Affected claim:** meaningful branch-discriminating, duplicate, invalid-basis-refusal, and Executive-constraint proof.
- **Causal mechanism:** The executable surface provides partial structural proof but does not close the claimed semantic branches:
  - all five primary results are enumerated;
  - missing out-of-frame cause and cause-on-another-result are explicitly rejected;
  - duplicate primary result rows are rejected;
  - absent unknown causes fail through an untyped `KeyError`;
  - duplicate out-of-frame cause rows are indirectly rejected by indexed parsing.

  However, the declared two-cause universe is not asserted. A read-only countermodel added an arbitrary third unique out-of-frame cause; all 15 tests still passed, and `reviewer_projection` dispatched that cause as valid. Thus an unknown cause becomes accepted merely by appearing as another table row.

  Invalid-basis refusal and the four Executive constraints are checked only for required substrings. A read-only countermodel simultaneously added language permitting `invalid_basis` consumption and allowing a hard stop to be ignored; all 15 tests still passed because the required phrases remained present. Therefore the proof does not discriminate the required constraint from its contradiction.
- **Scope:** Qualification/proof surface. The exact current raw rows do state invalid-basis refusal and the four Executive constraints coherently; the defect is that their executable proof does not establish exclusivity or contradiction refusal.
- **Workaround status:** Bounded manual source re-entry and exact semantic inspection remain available. The named executable suite cannot serve as sole branch/refusal evidence.
- **Regression risk:** High: additional out-of-frame causes or contradictory consumption clauses can pass unchanged qualification.
- **Confidence:** High.
- **Residual uncertainty:** No separate executable carrier or decision function was declared in scope. The finding therefore applies to the claimed proof strength, not to an omitted runtime implementation.
- **Exact evidence/routes:**
  - [test_reference_frame_boundaries.py:50](/tmp/stdo-rc2-final-lean-002-subject.qDWNA4/specification_methodology/tests/test_reference_frame_boundaries.py:50), including result enumeration at line 195, branch cases at line 238, duplicate-result mutation at line 281, and substring-based Executive checks at line 298.
  - `repo://specification-methodology/stdo-v2.5.0-rc.2/787b49219db716e9a7acd60b780889365a78751ed604e610348734dc2ef71f4a/standards/STDO_REFERENCE_FRAME_BASELINE.md#reviewer-result-and-triage-projection`
  - `repo://specification-methodology/stdo-v2.5.0-rc.2/787b49219db716e9a7acd60b780889365a78751ed604e610348734dc2ef71f4a/standards/STDO_REFERENCE_FRAME_BASELINE.md#executive-promotion-constraint-projection`

## Preserved relations and residuals

The Reviewer/Executive authority split is otherwise explicit and congruent across raw baseline, aggregate compression, and project-basis template: Reviewer owns evidence-bound severity and technical implications; Executive alone owns priority, current-boundary judgment, and existing disposition authority. The triage fields are proportionate because unsupported causal, workaround, complexity, or regression assessments remain explicitly indeterminate. The five primary result rows are structurally total, and the in-claim `out_of_frame` and `invalid_basis` meanings are coherent in the raw source.

The exported snapshot contains no Git metadata, so the supplied commit, tree, and subtree object identities were not independently rederived. Physical evidence-file hashes and the complete standards aggregate were independently reproduced.

## Invalidation conditions

This result is invalidated by any change to the bound subject, selected frame, index clauses, Product-selected severity scale, evidence files, or standards aggregate; or by authoritative evidence establishing both a non-overlapping selection law for simultaneous claim verdicts and adjacent observations and exclusive executable discrimination of the declared causes and refusal constraints.

**Closed return:** Executive is the sole result consumer. Reviewer authority ends with this evidence-bound `falsified` result.
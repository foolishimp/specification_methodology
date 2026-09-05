# Reference Frame Method result

- **Result:** `falsified`
- **Frame:** `repo://specification-methodology/stdo-v2.5.0-rc.2/554646747e6ba2227b4d0ad2b714764e1014173ad18532266de738476a073d26/standards/STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame`
- **Inference:** The raw relation is coherent and branch-total, but the composite claim is defeated by a compression inconsistency and material assurance gaps in the focused test and T-022 closure evidence.
- **Basis:** Valid. All supplied hashes, aggregate digest, map digest, program digest, frame URI, and source routes matched again at completion.
- **Consumer:** Executive. No priority, promotion effect, repair direction, or Product disposition is assigned.

## Findings

### F-01 — S2: aggregate compression makes the Reviewer return payload materially ambiguous

- **Affected claim:** Consistent projection across the raw baseline and aggregate compression.
- **Evidence:** The raw baseline requires “one Reference Frame Method result plus findings, counterexamples, evidence-bound technical triage, and residuals” ([baseline](/Users/jim/src/apps/specification_stack/specification_methodology/specification/standards/STDO_REFERENCE_FRAME_BASELINE.md:542)) and defines the complete return payload at [line 1082](/Users/jim/src/apps/specification_stack/specification_methodology/specification/standards/STDO_REFERENCE_FRAME_BASELINE.md:1082).
- **Conflicting projection:** The compression first requires and consumes technical triage, then states that the Reviewer “returns only a Reference Frame Method result” ([compression](/Users/jim/src/apps/specification_stack/specification_methodology/specification/standards/authority_compressions/stdo_compressed.md:772), [line 807](/Users/jim/src/apps/specification_stack/specification_methodology/specification/standards/authority_compressions/stdo_compressed.md:807)).
- **Observed consequence:** A compression-guided evaluator can reasonably emit a verdict-only return, omitting the finding-level triage Executive is supposed to consume.
- **Causal confidence:** High. Source re-entry resolves the intended law, but does not remove the compression’s internal ambiguity.
- **Blast radius:** Compression-only consumers; the raw source relation remains intact.

### F-02 — S2: the focused test does not exercise the claimed relation or its result branches

- **Affected claim:** Adequate focused exercise, including totality across `satisfied`, `falsified`, `indeterminate`, `out_of_frame`, and `invalid_basis`.
- **Evidence:** The dedicated test only performs substring presence/absence checks across the three documents ([test](/Users/jim/src/apps/specification_stack/specification_methodology/tests/test_reference_frame_boundaries.py:98)). None of the five result-branch names appears in the test file.
- **Counterexample:** The test passes while F-01’s contradictory “returns only” sentence is present. It would likewise not detect loss of a no-finding branch, unsupported-assessment route, claim-relative blocking rule, or Executive-only disposition relation if its expected phrases remained elsewhere.
- **Observed consequence:** The test establishes textual projection markers, not semantic coherence, branch totality, negative authority behavior, or result consumption. This falls short of the baseline’s own qualification claim concerning evaluated “result branches and evidence populations” ([baseline](/Users/jim/src/apps/specification_stack/specification_methodology/specification/standards/STDO_REFERENCE_FRAME_BASELINE.md:1373)).
- **Causal confidence:** High.
- **Blast radius:** Focused qualification and any closure claim relying on it. The tests did reproduce as 11/11 normally and 11/11 optimized.

### F-03 — S2: T-022’s claimed cold-review evidence is not an exact consumable Reviewer result

- **Affected claim:** T-022 closure evidence consistently demonstrates the new Reviewer-to-Executive relation.
- **Evidence:** T-022 records a `GO` verdict and `P0=0`, `P1=0`, `P2=0` without an exact review subject, Reviewer/activation identity, evidence route, Reference Frame Method result, or bound scale and direction ([ticket](/Users/jim/src/apps/specification_stack/specification_methodology/.ai-workspace/tickets/completed/T-022-bind-reviewer-triage-and-executive-disposition.md:66)).
- **Source re-entry:** `STDO-UP-007` requires the exact subject and verdict to be durably traceable; a statement that review occurred is not itself the verdict ([TICKET_METHOD.md](/Users/jim/src/apps/specification_stack/specification_methodology/specification/standards/TICKET_METHOD.md:696)).
- **Observed consequence:** Executive cannot determine whether `P0..P2` represents severity or priority, apply a declared direction/evidence policy, or verify that `GO` corresponds to one of the five declared results for this exact RC2 candidate.
- **Causal confidence:** High for evidence insufficiency. An external review may have occurred, but no exact T-022 review carrier was found. The only durable repository review using the same labels targets RC1 and a different aggregate.
- **Blast radius:** T-022’s cold-review closure assertion, not the raw baseline semantics.

## Adjacent observations

- Source STDO defines a coherent total return relation: every evaluation returns one of five results; finding triage is conditional, while evidence, residual uncertainty, invalidation, and re-entry remain available across the other branches ([REFERENCE_FRAME_METHOD.md](/Users/jim/src/apps/specification_stack/specification_methodology/specification/standards/REFERENCE_FRAME_METHOD.md:409)).
- The Project Reference-Frame Basis template consistently separates severity, priority, boundary effect, and disposition and provides an unsupported-assessment return route ([template](/Users/jim/src/apps/specification_stack/specification_methodology/specification/standards/templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md:72)).
- The current Product Definition’s installed `v2.4.3-rc.3` basis verified cleanly. The evaluated RC2 material remains candidate source and is not thereby adopted.

## Residual uncertainty and invalidation

- Remaining re-entry evidence: an exact T-022 independent-review carrier, if one exists, including subject, basis, actor, evidence, result, scale, and residuals.
- This result is invalidated by any change to the supplied five file hashes, standards aggregate, map/program identities, severity scale, evidence population, Reviewer independence, or activation scope.
- Required raw-source re-entry was completed through `REFERENCE_FRAME_METHOD.md#reference-frame-laws`, `STDO_REFERENCE_FRAME_BASELINE.md#complete-engagement-transition`, `TICKET_METHOD.md#execution-and-verification-authority-separation`, and `SPEC_METHOD.md#agentic-construction-execution`.
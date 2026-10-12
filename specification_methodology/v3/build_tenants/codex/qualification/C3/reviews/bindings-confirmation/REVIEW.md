# Independent source-first cross-owner review: subject `b0ec615c9ebe8da80e9852df3968233155a432b7`

**Scope.** This review covers the repaired introductions to FOUNDATIONS, TRANSFORMATION_LIBRARY and README. It also covers the binding introductions for IDENTITY, ODD, TRAVERSAL, WORLD_MODEL, UX and BASELINE, and the derivative routing in `stdo_compressed.md` and `stdo_bootstrap.md`. The carried bodies are out of scope.

**Basis.** I read the immutable owner text first, using the supplied SHA256 values. I could not check those hashes or confirm that the candidate bytes match the commit. I treated them as asserted and record that as a residual, not as `invalid_basis`.

**Authority.** This is an evaluation only. It assigns no disposition, priority or acceptance.

**Severity.** No Product-selected severity scale was supplied, so Product-scale severity is `indeterminate` for every finding. The consequence grades below (high, moderate, low) only describe impact. They are not a Product severity, priority or effect on the current boundary.

## Results per cone

| Cone | Result | Deciding counterexample |
|---|---|---|
| FOUNDATIONS.md | **`falsified`** | F-1, F-2 |
| TRANSFORMATION_LIBRARY.md | **`falsified`** | T-1, T-2, T-3, T-4 |
| README.md | **`falsified`** | R-1, R-3 |
| IDENTITY_METHOD.md introduction | `satisfied` | none; X-1 and residual I-r remain |
| ODD_METHOD.md binding | **`falsified`** | O-1, O-2 |
| TRAVERSAL_OCCURRENCE_PROFILE.md binding | `satisfied` | none; body-dependent residuals remain |
| WORLD_MODEL_METHOD.md binding | `satisfied` | none; body-dependent residuals remain |
| UX_METHOD.md binding | `satisfied` | none; residual U-r remains |
| STDO_REFERENCE_FRAME_BASELINE.md, Canonical Compression | `satisfied` | none |
| Derivative routing (`stdo_compressed.md`, `stdo_bootstrap.md`) | `satisfied` | none |
| Cross-cone source standing (X-1) | `indeterminate` | the direction of "refines" is not declared |

## Findings

### FOUNDATIONS

**F-1. The stable symbol context is incomplete.**
- **Owner rule (SPEC, Bounded-Context Semantic Resolution).** A context exists only when its owner declares "its stable identity, owner, selected basis, and governed semantic scope". A heading cannot make up the context. IDENTITY §4 (stability) also applies.
- **Counterexample.**
  - The context is named as "the selected exact member URI of this document plus `#premises-and-standing`". That identity is tied to a location and changes with every cut.
  - No owner is named.
  - The basis is left to "the activation subject and basis", so it is not selected.
  - The governed scope is "these symbols", limited to one section fragment. Yet `Sigma_contract` is used again, and `A`, `I`, `C_H` and `H` are introduced, in *Orthogonal descriptions*, which is outside that fragment.
  - Under SPEC resolution those occurrences have no declared context. `I` and `C` also collide in spelling with `a_c` tuple members (`I` is the identity universe, `C` is the constraint set) and with `a_c` carrier `C`. Under SPEC rule 5 the result is unresolved or ambiguous meaning.
- **Consequence:** moderate. Symbol meaning fails closed for every consumer of the categorical-model paragraph.
- **Causal confidence:** high.
- **Blast radius:** FOUNDATIONS, and any frame that cites these symbols.
- **Repair complexity:** low. Declare a stable URN, an owner, a basis and a whole-document scope, or rename the symbols in the later section.
- **Regression risk:** low.

**F-2. The capability-misfit response gives actions to the actor that RF-014 gives to human authority.**
- **Owner rule (RF-014).** When the manifold exceeds the actor's envelope, "human authority may select another actor, refine the frame, sequence activations, or provide a lawful compression."
- **Counterexample.** FOUNDATIONS, *Finite capacity*, tells the actor directly: "refine it … acquire support, reconfigure within authority …". The "within authority" qualifier attaches only to *reconfigure*, so *refine* becomes an actor duty or permission with no human-authority condition.
- **Consequence:** moderate. It changes who may reshape a frame.
- **Causal confidence:** medium. The text could also be read as the actor merely *requesting* refinement.
- **Repair complexity:** low. Route refinement through the RF-014 authority.

**F-3. The judgment and authority paragraph contradicts itself (low).** It first lists "disposition" among items that remain distinct. It then says "Those are distinct from … the decision to repair, re-enter, reject or accept", but that decision *is* the disposition. Severity and priority stay correctly separate, and nothing is mapped mechanically, so Baseline technical triage is not contradicted.

### TRANSFORMATION_LIBRARY

**T-1. The result domain of Transform is not parameterized.**
- **Owner rules.** `a_c` AC-013 defines the result as `T[t](M_b, inputs) -> M_b_prime* | hold | gap | refusal`. ODD A5/A6 make F_P worker output evidence only after admission.
- **Counterexample.** Transform says "Return candidate work, refusal, incomplete work or a re-entry request". That is a fixed four-way result with no instance qualifier. It reproduces the Baseline `WorkerResult` algebra, which belongs to an optional profile.
- The repair qualified Evaluate ("For a reference-frame evaluation…") and Dispose ("For an agentic construction instance…") but not Transform. The preamble disclaimer does not cure a directive written as unconditional.
- **Consequence:** moderate. Calculus `hold` and `gap` have no slot in it.
- **Causal confidence:** high.
- **Repair complexity:** low.

**T-2. Two UP-020 terms are taken in from other contexts.**
- **Yield.** Within "an agentic construction instance", Dispose says the owner "may select a next already-authorized action, **yield** or terminate". UP-020 has no `yield`. In ODD, `yield` is a closure disposition of `evaluate_action` (A8, A9), not a choice made by a decision owner. No import relation is declared.
- **Interval.** "Accept binds an exact checkpoint **and interval**." UP-020 binds "one exact checkpoint". The acceptance interval belongs to the Product-outcome instance under UP-013, so the two are being merged.
- **Consequence:** moderate.
- **Causal confidence:** high.
- **Repair complexity:** low.

**T-3. Restart and discard are treated as the same thing.**
- **Owner rules.** UP-020: "A proposed **restart** identifies why repair … is insufficient …". UP-013: "Consumers own deletion, archival, quarantine, and salvage mechanics."
- **Counterexample.** "A proposed **discard or restart** identifies why repair is insufficient …". This places a justification duty on discard that no owner states, and it reaches into territory UP-013 gives to consumers.
- **Consequence:** moderate. It adds a duty no owner imposes.
- **Repair complexity:** low. Limit the sentence to restart.

**T-4. The cost section makes measurement unconditional.**
- **Owner rule (UP-014).** Proportionality is the ambiguity removed against effective reasoning complexity, "not raw line count, artifact count, or context-window size". "No universal resource quota or separate accounting carrier follows." UP-019 qualification applies only where the work materially affects the outcome.
- **Counterexample.** "For a cost or improvement claim, measure its material costs: acquired and transferred bytes, … aggregate work and displaced human assurance." After the colon, the list reads as complete and required for every claim, including claims about method proportionality, which UP-014 says bytes do not measure. The "no universal gate" disclaimer does not lift the duty to measure.
- **Consequence:** moderate.
- **Causal confidence:** medium. "Material" can be read as a filter.
- **Repair complexity:** low. Say "those costs material to the claim", and send proportionality claims to the UP-014 relation.

**T-5. A missing planned judgment may be classified too strongly (`indeterminate` pressure).**
- **Owner rule (RF, Result Conjunction).** "Missing … mandatory results remain unresolved under the declared rule."
- **Candidate text.** "An omitted planned judgment violates that contract." That could be read as falsification, which could lead to rejection, rather than an unresolved result.
- The owner of "planned assessment slots" and "admission contract" was not supplied, so I cannot decide whether the two are compatible.

### README

**R-1. The UX classification owner is misstated.**
- **Owner rules.** UX §1A: when adopted it is "the sole UX **realization** authority". UX §2 says it refines DESIGN_MODULE_METHOD. UX §17 says it is not a wireframing or user-research method. In the Baseline, user-outcome claims go to Product and user-acceptance frames.
- **Counterexample.** The table row reads "User-outcome design | UX Method". That gives user outcomes to UX, which UX disclaims, and leaves out its realization role.
- **Consequence:** moderate. It routes user-outcome claims to the wrong owner.
- **Causal confidence:** high.
- **Repair complexity:** trivial. Change the row to "UX surface realization".

**R-2. Source-standing coverage is incomplete (low to moderate).**
- The standing sentence classifies Spec, Frame, ODD, Identity, World Model, the calculus, Traversal, Baseline, Design, Ticket, Release, Posting, Writing and Glossary. It **leaves out UX**, and gives Foundations and the Library only an unclassified "account".
- ODD and World Model are classified as "constitutional method surfaces", but their own binding introductions call them "optional … profile". "Profile" is also the README's word for the *derived* Baseline. This is a terminology collision, not a proven contradiction, because optional adoption and constitutional standing can coexist. It should still be disambiguated.

**R-3. Compressions could be read as deciding.**
- "Raw members decide **when** projections are stale or insufficient" can be read as making raw members decide *only* in those cases, which would leave digest-bound compressions deciding everywhere else.
- The owner rules are SPEC (glossary and projections do not decide) and RF-006 (a projection gains no authority).
- **Consequence:** moderate. This opens an authority leak through ambiguity.
- **Repair complexity:** trivial. Say "raw members always decide; compressions never decide."

**R-4. Construction narration (low).** "The **new** foundation/library account preserves …" describes when the text was written. It will become wrong in later cuts.

### ODD binding

**O-1. The Evaluate row splits one function and reclassifies another.**
- **Owner rule (ODD §11.5D).** There is "one model synthesis function and three distinct evaluation functions". `evaluate_action` is the action-result evaluation that decides close, yield, retry and the other closure dispositions.
- **Counterexample.** "Model, gap and action-result judgments remain separate from evaluate_next … and **evaluate_action deciding disposition**." The action-result judgment *is* `evaluate_action`, so the row splits it into two. It also calls `synthesize_model` a "judgment", although it is a synthesis function.
- **Consequence:** high. It creates exactly the function ambiguity that A4a prohibits ("must name which function").
- **Causal confidence:** high.
- **Repair complexity:** low.

**O-2. The Dispose row merges the closure function and the next-action function into one generic owner.**
- **Owner rules.**
  - A4a separates the functions.
  - A5: F_D/ABG/product admission owns closure truth.
  - A11: "Disposition is conceptual; selection is invocational."
  - The equation closes with "no other path can decide what work happens next."
- **Counterexample.** "The existing competent owner selects the admitted closure **or** next-action consequence." This lets one unnamed owner either choose closure or choose the next action. That is a candidate rival control surface under A0.
- **Consequence:** high.
- **Causal confidence:** high.
- **Blast radius:** every consumer of the ODD profile that reads the binding table as its routing.
- **Repair complexity:** low. Name `evaluate_action` → `EdgeClosureDecision`, and `evaluate_next` → `NextActionProjection`. Keep the admission of `ConstructionIntent` as a separate step.

**O-3. The worker "publishes" evidence (low).** Under A5 and A6, F_P must not emit runtime events or mutate ledgers, and evidence takes effect only after admission. Change "publishes" to "produces for admission".

**O-4. Identity law is attributed to Foundations (low).** "The foundation's scoped identity and authority law" gives ownership to Foundations, which itself says Identity Method owns it.

**O-5. The loop is renamed (low).** "Observation-to-yield loop" does not match ODD's span, which runs from `IntentLineage` to `NextActionProjection`.

### Clauses that passed

- **TL Evaluate:** parameterized correctly, and the assessor disposition is kept as evidence. This fits UP-020's "assessor disposition" inside transition evidence, which is a read model.
- **TL Dispose:** the four UP-020 conditions match the owner verbatim.
- **TL Recovery:** the progress and churn categories are right, the retry prohibition is correctly limited, and proof cadence is right.
- **Category hypotheses (FOUNDATIONS and TL):** the conditions for category, functor and equivalence match `a_c`'s Functor Kind disclaimer. Markov and monad claims are kept separate.
- **Representation space (WMM):** "Geometric directions computed in different representation spaces do not compose … generic translation vocabulary does not waive that rule" fits TL's guard that explicit translation is lawful only where the owning contract admits it, and fits the WMM Composition Law.
- **UX binding:** the six-class sprint-close list matches §13B exactly. Adoption, scaffold and default coverage are left to UX itself. Every product-truth-changing message resolves to an admitted carrier.
- **Baseline compression:** direct and coordinated branches, Reviewer "only where required", and decision authority limited to existing grants all fit the Status table and the Complete Engagement Transition.
- **Grants and capability:** the conditional framing ("no universal numeric budget, resource ledger or measurement gate") matches UP-014 and RF-016.

## Cross-cone pressure (X-1, `indeterminate`)

FOUNDATIONS says it "organise[s]" the method and that "Identity Method owns governed names". It also says the method's obligations "follow from these premises", and "the detailed method members refine the relations". Every binding introduction says its member "refines Foundations", and the ODD, UX and WMM introductions attribute laws to "the shared foundation". Together these make the standing circular: the immutable owners are described as refinements of a non-owning explanatory surface.

Under SPEC, calling something a specialization without coordinates "establishes nothing". Under RF-009, a hierarchy exists only where it is explicitly declared. So whether "refines" is a hierarchy claim or only explanatory cannot be settled from the supplied text. The standards' owning authority needs to declare the direction (derivation, organisation or refinement). O-4 is the one concrete case.

## Residuals (missing context, not guessed)

- **Owner text not supplied:**
  - SPEC: Collective Reference-Frame Basis, Ambiguity Governance, Constitutional Chain, STDO-UP-015, -021 and -022.
  - TICKET (UP-007), RELEASE and GLOSSARY bodies.
  - DESIGN_MODULE_METHOD UP-019 and UP-023, plus its standing statement. README calls Design, Ticket and Release "companion", even though they own UP-numbered law, and that cannot be checked.
  - The five frames under `../frames/`.
- **Body-dependent binding claims** were taken as carried:
  - Traversal: the seven-member cut and three judgments.
  - WMM: the eight-surface test, the Builder-Project specialization coordinates, the Design Module relation not being a prerequisite, and the representation-space body.
  - ODD: "zoom-stable closure".
- **I-r:** the Identity introduction lists elevation, transfer, supersession and retirement. UP-004 also lists split, merge, proxy grant and revocation. The introduction's list is not exclusive, so this is not a contradiction.
- **U-r:** the UX Dispose row covers only the sprint-close path. Closure outside a sprint (§14, §15) is not mapped.
- **Basis:** SHA256 values and commit membership are unverified. The first UX_METHOD block was empty; I used the complete block that carries the same SHA. The REFERENCE_FRAME excerpt is truncated at *Minimal Frame Activation Binding*, which is not material to these cones.
- **Severity scale:** no Product-selected severity scale was supplied, so Product-scale severity is indeterminate for every finding.

**Invalidation.** These results lapse if the subject commit, any owner hash, or any candidate byte changes, or if the X-1 refinement direction is declared. Re-entry for the falsified cones goes to the standards' owning authority. Re-entry for X-1 goes to whoever owns source standing.

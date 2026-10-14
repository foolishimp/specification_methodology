# Delta assessment: corrections to A1–A7 and B/C against the prior findings

**Basis.** I used only the supplied text: SOURCE.md, the FOUNDATIONS sections, the Executive profile excerpt, SIGNATURE.md, the prior findings, and the delta JSON (35 core clauses, `consumer-release`, `family-bind`, residuals and the material-family index). I could not check the digests, commit `9bc8962…`, SOURCE_INVENTORY.json, ORACLE.json, model.py, finite_check.py, the validator's closure report, the 16 unshown family/consumer clauses, or the RC2 calculus.

**Overall.**
- A1–A7 are corrected at the clauses named, with small residual points under A1, A2 and A3.
- Most B items are carried.
- Re-reading the source against the corrected clauses found four medium-severity gaps (R1–R4) and several lower ones. Two of them are guard narrowings of the same kind as A1.
- Family fidelity remains **indeterminate**.

This is one assessment. It supplies no acceptance, release or independent-review standing.

---

## 1. Status of A1–A7

| Finding | Status | Remaining note |
|---|---|---|
| **A1** `total-control` | **Corrected.** The guard is now "any admitted control state is encountered", and the statement lists all six source conditions, including revoked or exhausted authority. The revoked-grant counterexample now fires. | Low: the guard is keyed to a runtime encounter. A declared control domain that lacks a response but is never exercised is not flagged; the source makes totality a property of the contract. Revoked authority and "within the actual grant" appear, but `premise-authority` is not a premise. |
| **A2** `refinement` | **Corrected.** It now states totality, the explicit missing-reason case, indeterminate mapping, raw-outcome and authentication retention, no upgrades, preserved unconfirmed performance, owner retention, and no overwrite. The prior counterexample (unconfirmed → not_performed) is now barred. | See **R6**: the exception names only negative or diagnostic support. |
| **A3** `nonperformance` / `performance-compatibility` / `consumer-release` | **Corrected.** Performance is now evidence-relative. The lost-record case gives unconfirmed and bars satisfied. `consumer-release` now says "evidence establishing evaluation undertaking". | See **R5**: the guard scope, and the missing dispatch/admission rule. |
| **A4** reconfiguration preservation and optimality | **Corrected.** Both are now in `allocation` under the guard "any fixed or adaptive allocation or reconfiguration". The peer-reallocation counterexample now violates `allocation`. | — |
| **A5** `coordinator` | **Corrected.** Its standing is now "additional domain policy". It cites STDO_REFERENCE_FRAME_BASELINE, its guard requires adoption and lawful activation, and it states that it is not core topology or authority. The statement is consistent with the supplied profile excerpt at the level of ownership. | Low: the statement encodes none of the profile's constraints, such as no Executive mutation, no implicit lateral activation, or severity versus priority. That is acceptable for an ownership pointer. Note that no residual names `coordinator`. |
| **A6** `decision-stop` | **Corrected.** It now carries the bound authority, the stop reason, the three-way stop verdict rule (satisfied is excluded), and lawfulness as a separate predicate. | — |
| **A7** `allocation` | **Corrected.** It now carries the delegable-grant ceiling, the four distinct dependency kinds, and resource limits and failure assumptions. | Low: the source says the *existing* design or frame record *explains* the allocation. The clause says "bind … with", which drops the explanation duty and the no-new-carrier point. Communication costs are not named as a constraint. |

## 2. Status of B items

| B item | Status |
|---|---|
| Aggregate performance | **Partial. See R3.** |
| Acquisition: sparse absence, rule packet, digest, summary | Carried. The "no omission to meet capacity" point now cites Bounded construction, though `outer-preservation` is not a premise (low). |
| Empty log / discarded context | Carried (`effect-observation`). |
| Observed departure in the boundary | Carried. |
| `reverted` requires every begun part | Carried, together with "at least one begun part". |
| Absent-slot parts, nonmutating combiner, exhaustive join table | Carried. The table is now total. **See R4** for a separate gap in normalization. |
| No overwrite by a new predicate | Carried (`result-binding`, `refinement`). |
| Precondition as evidence; no substitution of an admission predicate | Carried (`nonperformance`). |
| Context loss creates no authority or idempotence | Carried, and `premise-authority` was added. |
| UP-016/017 route, union, unestablished outer interpretation | Text is carried. **See R2** for the guard. |
| Z owner and Z change | Carried (`progress-stop`). |
| Lower-severity items | `workspace-truth` ("admissible"), the `safe-reentry` guard, `result-binding` (citations, availability, unconditional projection), `freshness` binding, the `outer-preservation` identity premise and the `reuse` independence premise are all corrected. The F2, F4 and F6 distinctions are restored. **F1 is only partly restored. See R7.** |

## 3. Status of C items

1. **Anchors.**
   - `SOURCE.md#finite-oracle` now resolves to a supplied section.
   - "Product authority declared above" now resolves to the bounded-context paragraph.
   - The anchors for the `grant` and `identity` symbols (`#judgment-and-authority`, `#identity-state-and-evidence`) are not exercised in this delta and remain **unresolved**.
2. **Operator.** `family-bind` and `consumer-release` use `#consumes`, which matches SIGNATURE's Consumes. For the other 16 clauses I have only the mechanical count of 18, not the clause text.
3. **Standing literals.** All 37 supplied clauses use one of the three SIGNATURE standings. The 16 unshown clauses cannot be checked.
   - Visible inconsistency, unresolved without the source: `family-bind` is "source-owned method law" while `consumer-release` is "additional domain policy". Both are consumption relations.
4. **Index.**
   - The family index now lists all 18 clauses.
   - SOURCE.md now declares closure-based reachability and disclaims any requirement to index every clause directly.
   - The actual closure report was not supplied, so whether every core clause is reachable is **unresolved**.
5. **Residual accounting.**
   - The frame scope no longer overstates coverage. **See R10** for linkage gaps.
6. **Version pairing.** The question is now explicitly declared non-equivalent and unresolved, in SOURCE.md and in the `core-coverage` residual. It is disclosed, not resolved.
7. **Editorial.** The SOURCE.md number agreement is fixed. The remaining mixed spelling is in FOUNDATIONS itself, which is out of scope.

---

## 4. Remaining counterexamples and altered meaning

**R1 (medium). `conjunction-rest` drops the effect-dependency rule.**
- Source: "Effect uncertainty prevents satisfaction where the predicate requires a known effect state. An unrelated effect does not automatically invalidate a different predicate; the dependency relation must justify its relevance."
- The clause lists unresolved "coverage, applicability, evaluation or join", then "otherwise satisfied". `effect-join` is not a premise of it.
- Counterexample: the composite predicate is "deployed with no partial writes". Both leaves are authentically satisfied, but the normalized effect is `unknown`. The clause yields satisfied; the source forbids that.
- The converse protection is also missing: nothing stops an unrelated unknown effect from being treated as defeating.
- SOURCE.md and the residual exclude conjunction/effect integration only from the *finite code*. The textual clause also omits it.

**R2 (medium). `composition-order` places the sequential-composition rules behind a regrouping guard.**
- The guard is "results are regrouped or operations reordered". The qualification carries "UP-016/017 and AC-016 own sequential composition" and "an unestablished outer interpretation or join yields … unresolved or invalid_basis, never guessed success".
- Counterexample: a plain sequential pipeline with no regrouping, whose outer interpretation is *unresolved* (not known to be invalid), reports success.
  - `composition-order` does not fire.
  - `composite-invalid` fires only when the basis "cannot be interpreted".
  - So the source's "applicable unresolved" outcome has no carrying clause.
- Also not carried: "a recovery path need not require a failed earlier test to become true", and the sequential-stage rule that an unreturned dependent evaluation is recorded as an absent slot with its extent.
- This is the same kind of defect as A1.

**R3 (medium). Aggregate performance appears only on the non-falsified branch.**
- `conjunction-rest` (guard: no authenticated falsification) and `logical-operator` carry "the combining evaluation is performed … without changing component performance".
- `conjunction-failure` and `composite-invalid` do not.
- Counterexample: a falsified conjunction reports its aggregate performance as `unconfirmed` because one component slot was unconfirmed, or overwrites that component's performance. No clause is violated. The source rule is unconditional.

**R4 (medium). `effect-join` omits the rule for conflicting or insufficient observations.**
- Source: "Conflicting or insufficient observations leave the part unknown." Also: local stage labels "are not inputs to the composite join until mapped onto that part's observed state".
- The clause normalizes "using identities, ordering and supported supersession" and says only that timestamps alone grant no supersession. In the source, ordering is something *retained*; it is not a selection rule.
- Counterexample: two observations of one part, `completed` and `not_started`, with no supersession support. The later one in declared list order is selected and gives `completed`. No clause is violated; the source gives `unknown`.
- Ownership wording: "under the result owner" differs from the source's "the composite declares its effect boundary and the selected effect parts".

**R5 (low–medium). The performance guards and the dispatch rule.**
- `performance-compatibility` fires on "a core result is projected or consumed". The legal-pairs table, however, constrains every result.
- Counterexample: an evaluator *originates* a result with `unconfirmed` / `satisfied` that has not yet been projected or consumed. `nonperformance` (guard: "performance … is reported") does not prohibit satisfied, so whether either clause bars it depends on reading origination as projection. Widening the guard to "reported, projected or consumed" would remove the doubt.
- Neither clause states that "Dispatch or admission alone does not establish performance." A consumer could treat a dispatch log as evidence of undertaking.

**R6 (low–medium). `refinement` narrows the missing-reason exception by enumeration.**
- Source: the predicate "remains indeterminate until admissible evidence decides it". SOURCE.md: "separately admissible evidence on that predicate can still decide it."
- The clause names only "separately admissible counterevidence or basis/scope diagnosis".
- Counterexample: `refused` with a missing reason, followed by a separately performed, authenticated evaluation that satisfies the same predicate. The source allows that evaluation to decide the predicate. The clause's enumeration reads as excluding positive support.
- This is narrower than the source, in the opposite direction from A2.

**R7 (low). Premise wording.**
- `premise-purpose` assigns outcome and adequacy to the purpose owner, but says only that value choices "do not follow from capacity". F1 and the standing paragraph assign value choices *to the purpose owner* ("reserved value choices"). An implementer supplying a trade-off weight is not excluded. The prior F1 finding is therefore only partly corrected.
- `premise-capacity` says the domain "admits truthful unknown, inadequate and interrupted conditions". F5 says it admits truthful *handling* of those conditions. Dropping "handling" removes the obligation and leaves a garbled predicate.

**R8 (low). `effect-observation` unstated rules.**
- Not stated:
  - `not_started` requires evidence that the effect did not begin, such as an authenticated rejection before mutation.
  - Dispatch alone proves neither completion nor absence.
  - A lost acknowledgement after possible execution is `unknown`.
  - Effect values are independent of the predicate verdict (completed while product falsified).
- "According to supported observation" covers some of this by implication only.
- The guard "an effect is relevant to the operation" is undefined. Counterexample: a read-only job with a possible unintended cache write is judged to have no "relevant" effect, so the clause never fires. The source scope is every material possible part.

**R9 (low). Premise lists.**
- `total-control` and `coordinator` rely on grants without `premise-authority`.
- `acquisition` relies on Bounded construction without `outer-preservation`.
- These are the same pattern as the prior `outer-preservation` and `reuse` findings, which were themselves corrected.

**R10 (low, structural). Residual linkage.**
- The `core-coverage` detail names finite exclusions for applicability, conjunction/effect integration, freshness, construction and configuration.
- Its `subject_refs` list only `allocation`, `composition-order`, `context-reset`, `refinement`, `reuse` and `total-control`.
- `applicability`, `conjunction-failure`, `effect-join`, `effect-observation`, `freshness`, `acquisition`, `logical-operator`, `outer-preservation`, `progress-stop`, `decision-stop` and `coordinator` are linked to no residual. `conjunction-rest` is linked only through `semantic-proof`.
- A declared residual bounds coverage. It does not cure R1–R8.

## 5. Still unresolved

- **Family fidelity.** All 12 `consumer-*` and 6 `family-*` claims remain **indeterminate**, including `family-bind` against TRANSFORMATION_LIBRARY#bind and `consumer-release` against RELEASE_METHOD. The prior D checks on `consumer-design` (join versus admission role) and `consumer-traversal` (`out_of_scope` binding; j_a recorded only, per SOURCE.md) cannot be re-examined because those clauses were not supplied.
- **Finite oracle.** The SOURCE.md claims about the finite code are unverified: the guard totality over the evidence grid, the 125-case associativity check, the 9 counted mutants, and the temporal normalization. As SOURCE.md states, agreement between ORACLE.json and model.py written by the same Writer is consistency evidence only.
- **RC2 versus successor calculus.** Equivalence is declared non-asserted and remains unresolved.

## 6. Non-inferences

Nothing in this delta, the residual declarations, or structural/closure validation establishes any of the following:
- whole-core implementation;
- that the omitted law is absent from or present in the source;
- whole-corpus or family fidelity;
- independent-review standing;
- acceptance, qualification or release.

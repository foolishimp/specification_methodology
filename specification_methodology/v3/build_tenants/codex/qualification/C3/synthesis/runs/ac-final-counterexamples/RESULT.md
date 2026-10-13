# Final reassessment: R1–R10 textual repairs and N1 finite refinement

**Bottom line:** The N1 repair and seven of the ten R repairs hold. **R8 is not closed.** The repaired guard on `effect-observation` makes the clause silent in exactly the case it is meant to catch. R2 and R9 carry low-severity residue, and there are a few smaller items listed below. I am not inferring family fidelity, complete core coverage or acceptance from any of this.

## 1. R1–R10 against the source

| ID | Status | Basis |
|---|---|---|
| R1 | **Repaired** | `conjunction-rest` now has `effect-join` as a premise. It carries "Effect uncertainty prevents satisfaction where the predicate requires a known effect state" and the converse relevance protection. The "deployed with no partial writes" + `unknown` case can no longer be satisfied. The same rule is missing from `logical-operator` (see C3). |
| R2 | **Repaired, with residue** | The guard now fires on plain sequential composition. The statement carries UP-016/017, AC-016, the recovery-path rule, unexecuted stages as coverage facts, and "applicable unresolved or invalid-basis". The qualification carries the absent-slot, extent and missing-conclusion rule. An unresolved outer interpretation now has a carrying clause. The clause still invokes "the operator rule above" without linking it (see C2). |
| R3 | **Repaired** | The aggregate-performance sentence is now in `conjunction-failure`, `composite-invalid`, `conjunction-rest`, `logical-operator` and `nonperformance`. A falsified conjunction can no longer inherit `unconfirmed` or overwrite a component's performance. |
| R4 | **Repaired** | Conflicting or insufficient observations now give `unknown`. Ordering is retained only, never used for selection. Temporal labels are joined only after mapping. Ownership now reads "the composite declares". The `completed`/`not_started` pair with no supersession support now gives `unknown`. |
| R5 | **Repaired** | Both guards now cover "originated, reported, projected or consumed". The rule "Dispatch or admission alone does not establish performance" is now stated. An originated `unconfirmed`/`satisfied` result is barred. |
| R6 | **Repaired (textual)** | The statement is the source verbatim: "remains indeterminate until admissible evidence decides it". The qualification routes positive evidence to its own performed record and forbids promoting an unconfirmed original. This matches the intended finite boundary. |
| R7 | **Repaired** | "Value choices come from the purpose owner" and "truthful handling of" are both present. |
| R8 | **Not closed** | The source text is now verbatim, but the new guard defeats it (see C1). |
| R9 | **Repaired, same pattern recurs** | `total-control` and `coordinator` now have `premise-authority`; `acquisition` now has `outer-preservation`. New instances of the same pattern appear in C2 and C4. |
| R10 | **Repaired** | All twelve clauses named in R10 now appear in `core-coverage` `subject_refs`, along with `composite-invalid`, `nonperformance` and `performance-compatibility`. The detail text is still misaligned with SOURCE.md (see C8). |

## 2. N1 confirmations

I traced each of these points through the code:

- **The contribution's own claim cannot decide.**
  - `mapped_evidence` overrides `deciding` with the reason-sensitive mapping, or `None` when the reason is missing or unsupported.
  - It also forces `independent=False`.
  - Grid 1 checks `own['verdict'] == mapped` over every `deciding` × `independent` value.
  - All three original N1 traces are fixed: the positive substitution, the own negative claim, and the overwritten mapped `falsified`.
- **Mapped failure is retained.**
  - `'falsified' in (mapped_verdict, admitted)` takes precedence.
  - `mapped_verdict` and `mapped_result` are always exposed.
  - The two override counterexample rows return `falsified`.
- **Separate-support guards.**
  - Admission requires all of: the same predicate, `independent is True`, `admissible is True`, and a non-empty string provenance.
  - Only negative or diagnostic claims are admitted. A positive or `indeterminate` separate claim is never admitted (confirmed in grid 2).
  - The 15 binding cases each break one guard: 3 claims × 5 patches.
- **Performance is preserved.**
  - Every record derives performance from the original `undertaken` value via an `is True` / `is False` test.
  - Unknown or non-boolean undertaking stays `unconfirmed`.
  - A mapped `satisfied` requires `performed` and `completion is True`.
  - Separate support never changes `performance` or `effect` (checked in grid 2).
- **Counts match SOURCE.md.**
  - The base grid is 5 outcomes × 7 predicates × 7 reasons × 3 undertaken values × 2 support values = 1,470.
  - Each N1 grid multiplies that by 6 claims × 2 independence values, giving 17,640.
  - There are 15 binding cases and 4 reviewer rows.
- **Conflict is not hidden.** The `conflict` flag records disagreement between the mapped verdict and admitted support. Note that it is checked with the same formula the code uses, so the check is same-Writer.

## 3. Remaining concrete counterexamples

**C1 (medium): the `effect-observation` guard turns the boundary requirement into a precondition (R8).**
- The guard reads: "an effect observation is reported on a boundary containing every material part … requested or unintended."
- Counterexample:
  - A read-only job reports `not_requested` on a boundary that omits its possible unintended cache write.
  - Because the boundary is incomplete, the guard is false.
  - The clause, including its read-only qualification, is never selected.
  - So nothing requires the omitted part or forces `unknown`.
- `effect-join` and `refinement` take this clause as a premise and inherit the gap.
- Fix:
  - Guard on "an effect observation is reported".
  - Leave boundary completeness in the consequence, where the statement already has it ("For every effect value, the boundary includes…").

**C2 (low–medium): `composition-order` invokes an unlinked operator rule.**
- The statement says "Their returned result applies the operator rule above". Its premises are only `conjunction-rest` and `premise-composition`.
- Counterexample:
  - Take a recovery-path pipeline whose outer predicate is not a conjunction of stage postconditions. The source explicitly allows this.
  - It must be decided by `logical-operator`'s well-formedness and truth/falsity rule.
  - That clause is not in the argument. This is the R9 pattern again.
- Fix: add `logical-operator` as a premise, and replace "above" with a reference to the clause.

**C3 (low): `logical-operator` lacks the effect-dependency rule that R1 added to `conjunction-rest`.**
- `logical-operator` has `effect-join` as a premise, so it composes effects, but nothing states that effect uncertainty prevents satisfaction.
- Counterexample:
  - A declared disjunction whose outer predicate requires a known effect state.
  - One leaf is authentically satisfied and the composite effect is `unknown`.
  - No `logical-operator` text bars satisfaction.
- The source's sentence is phrased generally ("where the predicate requires a known effect state"), and its operator paragraph keeps "effect composition" from the rules above.
- Fix: carry the same two sentences into `logical-operator`, unless the residual explicitly scopes them to conjunction.

**C4 (low): premise links reached only through anaphora or transitivity.**
- `refinement` says "uses the legal pairs above", but the legal pairs live in `performance-compatibility`, which is not a premise.
- `conjunction-rest` decides "unresolved applicability → indeterminate", but reaches `applicability` only through `conjunction-failure`. This is acceptable only if premises are meant to be transitive, and SIGNATURE.md does not say so.

**C5 (low; N1 policy): single-predicate precedence among conflicting verdicts is a model choice.**
- The code resolves conflicts as follows:
  - A mapped `falsified` plus admitted `invalid_basis` or `out_of_frame` gives `falsified`.
  - A mapped `satisfied` plus an admitted diagnostic gives the diagnostic.
- The source orders falsification before invalid basis only for **conjunction**. For one predicate, an established invalid basis arguably undercuts a falsification made on that basis.
- Nothing is erased: `mapped_verdict` and `conflict` are retained.
- The precedence should still be declared as a finite-model policy, not presented as source-derived.

**C6 (low; declared-limit wording): separate support is bound by predicate name only.**
- Subject and basis are not compared, so a falsification of `fitness` about a different candidate is admitted.
- `independent`, `admissible` and `provenance` are caller-asserted tokens. Provenance accepts any non-empty string, including the contribution's own producer or `" "`.
- The `refine` docstring states this ("fixed subject/basis and evidence authentication are fixture premises").
- Neither SOURCE.md's residual nor the `core-coverage` detail says so. Add one sentence to make the declared limit match the code.

**C7 (low): positive separate support looks the same as rejected support.**
- A well-formed, independent, admissible, provenanced `satisfied` separate claim yields `admitted_separate_support=None`.
- That is the same output as a claim rejected for failing a guard.
- The raw claim is retained, but the result does not say "positive support not modeled here; needs its own record" versus "inadmissible".
- A reason field would make the intentional R6 boundary visible in the result itself.

**C8 (low, structural): the `core-coverage` detail drifts from SOURCE.md.**
- The detail says "nonperformed conjunction slots"; SOURCE.md says "nonperformed **or unconfirmed**".
- The detail says "non-Boolean dependency ordering"; SOURCE.md says "non-Boolean or undecided operator leaves, undecided operator joins and material-dependency ordering". The earlier minor item asked for this alignment, and it has not been applied in the detail.

## 4. Editorial (no change in meaning)

- **Missing sentence breaks.** Appended sentences have no terminating period before them. This occurs in five clauses:
  - `composite-invalid`: "…aggregate scope The aggregate…"
  - `conjunction-failure`
  - `logical-operator`
  - `nonperformance`: "…downstream predicate Dispatch…"
  - `performance-compatibility`
- **Duplicated sentence.** `logical-operator` now states aggregate performance twice.
- **Context-dependent references.** Verbatim source paragraphs keep references that only resolve inside FOUNDATIONS.md:
  - "above" and "this record";
  - `effect-join`'s `[Result algebra](#result-algebra)` link, whose target is not among that clause's `source_refs`.

## 5. Test-coverage notes (not counterexamples)

- **Binding cases are narrow.** All 15 binding cases use the mapping-`None`, `undertaken=True` row. A guard failure is never exercised against a mapped `satisfied` or `falsified`, or with unconfirmed or not-performed undertaking. The code path is simple, but that combination is untested.
- **`completion=False` is never exercised**, so the completion condition on a mapped `satisfied` is unchecked.
- **`legal_coordinates(..., got['support'])` passes by construction.** `support` is the synthesized combined view, not the raw input; the raw input is in `raw_evidence`.
- **The N1 change is local to `refine`.** `evaluation`/`admissible_decision` still accept a flat in-evidence `independent` flag on other paths. Those paths are outside this delta.

## Summary

The N1 boundary is confirmed as declared:
- Only negative or diagnostic separate support is combined.
- Mapped failure survives every claim.
- A positive or non-independent claim never decides.
- Undertaking is never upgraded.

R1, R3–R7 and R10 are confirmed repaired. R2 and R9 are repaired with low residue (C2, C4). R8 needs the guard fix in C1. I am not reporting any acceptance or release judgment.

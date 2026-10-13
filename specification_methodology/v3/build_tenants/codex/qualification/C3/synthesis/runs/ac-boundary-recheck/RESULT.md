# C1–C8 bounded repair review against source 9bc8962

**Scope.** I checked only the supplied clauses, residual, signature, scope text, `refine` and the affected checks against the exact source. I could not see clauses outside the selection (`premise-composition`, `composite-invalid`, `nonperformance`, `result-binding`), the `REFINEMENTS` table, or any count assertions. Where a finding depends on those, I say so. Nothing here implies acceptance, installed qualification, family fidelity or source superiority. Disclosed residual domains are not treated as defects.

## 1. Status of C1–C8

| ID | Status | Basis |
|---|---|---|
| C1 | **Closed** | The guard is now "an effect observation is reported". Boundary completeness sits in the statement ("For every effect value, the boundary includes…"). The qualification extends it to unintended parts of read-only operations. The read-only cache-write counterexample now selects the clause. The omitted part must be in the boundary, and without sufficient observation it is `unknown`. `effect-join` and `refinement` inherit the repaired clause. |
| C2 | **Closed** | `logical-operator` is now a premise and is named in the statement. The pipeline case names `conjunction-failure` and `conjunction-rest`. `conjunction-failure` is reached transitively through `conjunction-rest`, which the signature's Premise section now permits. A recovery-path outer predicate is decided by `logical-operator`. |
| C3 | **Closed** | `logical-operator` now carries both effect-relevance sentences. In the disjunction counterexample (one satisfied leaf, composite effect `unknown`, predicate needs a known effect), satisfaction is now barred. The duplicated aggregate-performance sentence is gone; it now appears once, in the qualification. |
| C4 | **Closed** | `refinement` names `performance-compatibility` and has it as a premise. `conjunction-rest` has `applicability` directly. SIGNATURE.md now states transitive premise inclusion, so `result-binding` in `refinement` is reached through `effect-observation` and `performance-compatibility`. |
| C5 | **Closed in substance, declaration incomplete** | The code comment, the finite-oracle text and the residual all declare the precedence as finite-model policy, not source-derived. Both claims and the `conflict` flag are retained. See R-b for what the declaration leaves out. |
| C6 | **Closed** | The residual detail, the finite oracle and the residual scope all state that subject, basis and authentication are stipulated. They also state that predicate equality and nonblank provenance verify none of them. The `' '` provenance patch is now among the binding cases. Minor wording drift remains (see R-c). |
| C7 | **Closed** | `separate_support_status` has five values: `not_supplied`, `not_admitted`, `admitted_negative_or_diagnostic`, `positive_combination_not_modeled` and `undecided_combination_not_modeled`. A guard-passing positive or undecided claim is no longer indistinguishable from a rejected one. `separate_status_cases` checks this, and also checks that the verdict is unchanged. |
| C8 | **Closed for the two named items** | The detail now says "nonperformed or unconfirmed conjunction slots" and "non-Boolean or undecided operator leaves, undecided operator joins and material-dependency ordering". Other drift remains (see R-c). |

The earlier test-coverage notes are also addressed. The binding cases now range over every refinement row, all three undertaking values and both completion values. `completion=False` is exercised by `refinement_completion_cases`.

## 2. Remaining concrete items

**R-a (low–medium): the scope's binding-case count contradicts the code.**
- SOURCE.md says "fifteen binding cases and four fixed reviewer counterexamples supplement them".
- The revised loop runs over |refinement rows| × 3 undertaking × 2 completion × 3 claims × 6 patches. That is 108 per row, so the total can never be 15.
- The new `refinement_completion_cases` and `separate_status_cases` are not described in SOURCE.md at all.
- If a count assertion elsewhere still expects 15, it fails. If none exists, the declared scope misstates the check.
- **Fix:** update the counts and describe the two new checks.

**R-b (low): the declared conflict policy covers only part of what the code does.**
- SOURCE.md declares two cases:
  - mapped falsification survives a diagnosis;
  - an admitted diagnosis overrides mapped satisfaction.
- The code's actual rule is broader:
  - any falsification dominates, including an admitted falsification over a mapped satisfaction or diagnosis;
  - otherwise the admitted diagnosis replaces the mapped verdict.
- Concrete case, if `REFINEMENTS` maps any row to a diagnostic: mapped `invalid_basis` with admitted `out_of_frame` returns `out_of_frame`, with `conflict=True`. That ordering is the reverse of the source's invalid_basis-before-out_of_frame order in conjunction and operators.
- It is still policy and still flagged, so this is not a fidelity contradiction. But the declaration does not state it.
- **Fix:** state the full rule in one sentence.

**R-c (low): the `core-coverage` detail still under-lists against SOURCE.md's residual.**
- **Independence.** The detail lists "subject, basis and external evidence authentication" as stipulated but omits independence. SOURCE.md includes it in both the residual and the finite oracle.
- **Absent-slot effect parts.** The detail omits "parts owned by absent slots".
- **Reuse.** The detail says "workspace reacquisition/invalidation/freshness". SOURCE.md says "…freshness, changed-support invalidation and reuse".
- The detail is an exclusion list, so each omission reads as implied coverage.

**R-d (note, not verifiable here): routing an uninterpretable composite in `composition-order`.**
- For a pipeline whose composite subject or basis is uninterpretable, both `conjunction-*` guards require interpretability, so neither fires.
- The `invalid_basis` outcome comes from `composite-invalid`. I cannot see whether that clause is reachable through `premise-composition`.
- The statement's own final sentence ("returns the applicable unresolved or invalid-basis result") carries the outcome textually, so this is not a contradiction. It is a linkage to confirm.

**R-e (note): a result that reports no effect observation at all.**
- In that case `effect-observation` is not selected.
- Whether `unknown` is forced then depends on `result-binding` requiring material effect observations in the core record. That clause is not shown, so I cannot confirm it.

## Summary

C1–C4, C6 and C7 are closed. C5 and C8 are closed for what they named, with small declaration and alignment residue in R-b and R-c. The only concrete contradiction I found is R-a, the stale "fifteen binding cases" claim. These are same-Writer consistency observations within the bounded claim. They are not an acceptance judgment.

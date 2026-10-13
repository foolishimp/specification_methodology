# Delta review: corrected core finite interpretation

## Basis and limits

- I read the supplied Foundations sections first, then `model.py`, `finite_check.py` and `ORACLE.json`.
- I executed nothing. Every runtime statement below comes from tracing the code by hand.
- I did not see `SOURCE_INVENTORY.json`, `program.json` or the archive manifests, so I cannot confirm the digest pins or the archive exclusion.
- The fixtures, the model and the checker's separate formulas are all by the same Writer. Their agreement shows consistency only. The judgments below are my own reading of the source.

## Disposition of prior findings

| Prior finding | Status | Basis |
|---|---|---|
| 1. Guard contradicts `evaluation()`; not total | **Resolved** | `legal_coordinates` now requires the result to equal `admissible_decision(evidence) or 'indeterminate'`, with performance taken from the evidence. Every evidence state therefore has exactly one legal pair. The 72-state grid tests every claim (None plus 5 verdicts) × independence × completion against a separately written formula, which gives 1080 coordinate probes. All 9 evaluation fixtures pass the guard. `support` and `admissible_support` are kept apart. |
| 2. Refinement has no reason domain or missing-reason case | **Resolved on the declared grid; new defect in the separate-support path (N1)** | The map is keyed on (outcome, predicate, cause). A missing reason, an unrecognized reason, or `reason_supported=False` gives `indeterminate` with `unresolved_authentication`, and keeps the raw outcome, cause and evidence. Performance follows the evidence, so `unconfirmed` stays `unconfirmed`. The 1470-case grid and 30 missing-reason cases cover this. |
| 3. Negation flips a bare verdict | **Resolved** | `negate_view` builds a new table: truth = ¬Q ∧ J. A failed required join stays `falsified`, and the negated table passes `operator_wellformed`. It keeps the original result, leaves and join, and uses a distinct predicate string. Unproved well-formedness stays `indeterminate`; an invalid operator stays `invalid_basis`. |
| 4. Vacuous mutants | **Resolved** | See the mutant table below. The four vacuous or literal entries are gone. The implication case is reported with `mutant_credit: False`. |
| 5. Recovery, Construction, Configuration uninterpreted | **Narrowed truthfully** | The dictionary-copy trace is removed. `recover()` is documented as a decision table over inputs assumed to be already acquired and fresh. The text says Construction and Configuration have no executable. |
| 6. No conjunction effect coordinate | **Narrowed truthfully** | Listed as unimplemented integration. |
| 7. Associativity tests verdicts only | **Narrowed truthfully** | The text now says the check covers verdict precedence only. Since F > I > O > U > S is a total order taken as a maximum, verdict associativity holds. |
| 8. Unknown effect tokens default to `not_started` | **Resolved** | `observe_effect` returns `unknown` for any unit that is not `True`, `False` or `'reverted'`. Because it tests `v is True`, `0` and `1.0` are not accepted as booleans. Four fixtures cover this. |
| 9. Naming | **Resolved** | Fixtures are renamed `invalid-basis-judgment` and `known-unperformed-planned-evaluation`. `N` is now listed in `missing_evaluations`. The fallback fixture checks that its leaves are kept, though only as booleans. |
| 10. Unstated domain limits | **Resolved** | Applicability, independently supported slots that were not performed or are unconfirmed, missing or unauthenticated joins, non-Boolean leaves, and temporal list-order stipulation are all now declared. |

## New finding

### N1. Medium: the refinement's "separately admissible evidence" path does not check that the evidence is separate, and it can replace a supported mapping

**Source.** Result algebra, refinement paragraph:
- A missing required reason leaves "that contribution inadmissible as deciding support for its slot."
- "Independently established counterevidence or a basis/scope diagnosis" may decide the predicate.
- "No refinement turns failure … into greater standing."

**What the code does.** `refine` uses the mapping only when `evidence['deciding'] is None`. Otherwise it passes the supplied claim through `admissible_decision`. On the `performed` path, `admissible_decision` never reads `independent`. So the refined contribution's own claim is admitted, and a supplied claim replaces any supported mapping. Three traces:

- **Missing reason plus an unsupported substitution reaches `satisfied`.** `refine('candidate_ready', 'fitness', None, {undertaken: True, deciding: 'satisfied', completion: True, …})` gives `satisfied`, with `reason_supported=False` and `unresolved_authentication=True` on the same result.
- **The contribution's own negative claim is admitted despite the missing reason.** The same call with `deciding: 'falsified', independent: False` gives `falsified`. The checker only tests `independent=True`.
- **A supported counterexample is erased.** `refine('out_of_scope', 'event_scope_compatible', 'compatibility_counterexample', {undertaken: True, reason_supported: True, deciding: 'indeterminate', …})` gives `indeterminate`. With `deciding: 'satisfied', completion: True` it gives `satisfied`. The mapped `falsified` appears nowhere in the result.

**Why the checks miss it.** The refinement grid never sets `deciding`. The missing-reason loop sets it only to `falsified` with `independent=True`.

**Recommendation:**
1. Give `refine` two distinct inputs: the refined contribution, and optional separate support that carries its own provenance.
2. Admit a separate claim only when its independence is established, whatever the refined evaluation's performance.
3. Combine the mapped result with separate support instead of replacing it: a supported falsification survives, and any conflict is kept.
4. Record the mapped verdict explicitly in the result.
5. Extend the refinement grid over `deciding` (None plus all verdicts) × `independent`.

Until this is done, narrow the README sentence to what is actually tested: independently supported negative or diagnostic claims only.

## Minor items

- **The guard restates the evaluator.** `legal_coordinates` and `evaluation` both call `admissible_decision`. "Every evaluation result must pass the same guard" is therefore true by construction. The real evidence is the checker's separate formula, which is same-Writer. The README sentence is accurate, but it should not be read as an independent constraint.
- **Mutant expectations.** The code comment says the mutants run "against fixed oracle cases." Two of them use literals instead:
  - `missing-assessment-performed` is compared to `False`, which has no `ORACLE.json` entry.
  - `raw-temporal-labels-joined` is compared to `'reverted'`, which equals `temporal_effects[0].effect` but is not read from it.
  
  The README's wording ("same-typed expectations") is accurate; the code comment is not.
- **What `detected_mutants` means.** Each mutant's output is compared with one expected value. This shows the expectations reject that output. It does not show that the finite suite would reject a mutated `model.py`. The README does not claim more than this.
- **Operator leaves are bare booleans.** "Retains failed leaf" means a boolean is kept, not a result with citations. That is consistent with the declared retained-component limit. The README residual says "non-Boolean operators"; the report says "non-Boolean operator leaves", which is more precise. Align them, and mention undecided joins as well.
- **Recovery inputs beyond the fixtures.** `recover()` is only checked on 5 rows. With a grant, the untested states `partial`, `reverted` and `not_requested`, and any unrecognized string, all fall through to `observe_or_return_unresolved`. That is conservative, but it is untested; the claim should say "five stipulated rows."

## Mutant count check

The nine counted entries:

| # | Mutant | Calls the model? | Expectation |
|---|---|---|---|
| 1 | lost failure | Yes | str, from ORACLE |
| 2 | invented performance | Yes | bool, literal |
| 3 | candidate means fit | Yes | str, from ORACLE (the old dict-versus-string comparison is fixed) |
| 4 | unknown means not started | Yes | str, from ORACLE |
| 5 | scope word relabelled | Yes | str, from ORACLE |
| 6 | known prefix means partial | Yes | str, from ORACLE |
| 7 | blind retry | Yes | str, from ORACLE |
| 8 | inconclusive run called unperformed | No (standalone function) | str, from ORACLE |
| 9 | raw temporal labels joined | Yes (private `_fold_states`) | str, literal |

All nine execute a faulty rule and differ from a same-typed expectation. The count of nine is truthful.

## Conclusion

The narrowed finite claims are truthful, with one exception (N1). They cover:
- AND decision precedence over 1620 cases,
- evidence and guard coherence over the 72-state grid,
- reason-sensitive refinement on the declared grid,
- bound negation,
- token-validated effect observation,
- the effect join and temporal fixtures as stipulated,
- the recovery decision table,
- nine genuine counted mutants.

The remaining limits are declared accurately:
- full workspace recovery,
- construction and configuration,
- integration of conjunction with effects,
- union of retained components,
- applicability,
- independently supported slots that were not performed,
- missing or unauthenticated joins,
- undecided operator leaves.

N1 should be fixed, or the README's separate-evidence sentence narrowed, before the refinement claim is restated. None of this amounts to source-fidelity acceptance. Material-family fidelity and the other items listed as unresolved remain outside this review.

# Source re-review: frozen core a746559 (Foundations and Transformation Library)

**Scope:** I checked material correctness against the common requirements: legal result combinations and the performance boundary, effect rollback and partiality, known join failure and declared operator truth, configuration preservation, and single ownership. This is not an acceptance or port-fidelity judgment. I did not use any tools, and I did not have the 4583b55 review text, so I judge the fixes only by what the current source says.

## Findings

### F1 (High): The legal-pairs table cannot express established falsity when the procedure did not conclude

**Where:** FOUNDATIONS.md, sections *Result algebra* (the performance table, the aborted-procedure sentence and the stop paragraph) and *Result conjunction* rule 1.

The table allows `not_performed` and `unconfirmed` only with `indeterminate`. The verdict `falsified` is defined by evidence ("admissible evidence establishes a counterexample"), not by the procedure concluding. Three places in the same member need falsity without conclusion:

1. **Aborted run with a known failure.** P is "all 40 tests pass". The run aborts after test 3 fails with an authenticated failure. The procedure did not conclude, so performance is `not_performed`. The only legal verdict is `indeterminate`, yet the text says the counterexample is "not erased". In a conjunction, rule 1 fires only on an "authenticated, applicable falsification of a required predicate". One reader counts the retained counterexample and gets `falsified`. Another reads the component's verdict and gets `indeterminate` under rule 3. The second reading reports undecidability where failure is established. That collapses the failure/undecidability distinction that Single Result Algebra items 3 to 5 exist to keep.
2. **Stop paragraph.** A stop reports the destination predicate as "falsified when admissible evidence defeats that predicate". A stop before the acceptance procedure ran has performance `not_performed`, so `falsified` is an illegal pair. The two clauses contradict each other directly.
3. **Missing-reason refinement.** "An independently established invalid basis instead yields invalid_basis". If the raw outcome left performance `unconfirmed`, this is also an illegal pair, unless "for that diagnosis" means a separate predicate. The text does not say which.

**Repair:** State that performance constrains only the verdicts that depend on the procedure's own conclusion. Allow `not_performed` or `unconfirmed` with `falsified` when an authenticated counterexample to P itself is retained. Keep `satisfied` performed-only. Either allow `invalid_basis` on an independently established diagnosis, or state that it is a separate predicate. Then make rule 1 cite exactly that case.

### F2 (High): The effect join is indexed by component, not by effect part, so rollback stages misreport

**Where:** FOUNDATIONS.md, *Result conjunction*, the aggregate effect paragraph.

The join is a correct lattice in its own terms: `not_requested` < `not_started` < `reverted` < `partial` < `unknown`, and `not_requested` < `completed` < `partial`. I checked associativity and it holds. The defect is in what it joins. "Retain which component each observation concerns" makes components the index, but effect states are properties of effect parts on a boundary.

- **Write then rollback.** The composite is "deploy X". Stage 1 writes X and reports `completed`. Stage 2 is a compensating rollback whose selected effect, "remove X", also reports `completed`. The join returns `completed` for a composite whose net effect on X is reverted. A consumer can then rely on a deploy that does not exist. This is the misreport the effect rules exist to prevent, even though the effect is not technically "unknown".
- **Revert then re-apply.** Stage 1 reports `reverted` and stage 2 re-applies, reporting `completed`. The join returns `partial`, which asserts an unexecuted or reverted remainder that no longer exists. A compensator acting on that could duplicate effects.
- **Absent slot.** A sequential stage was dispatched but never returned, so it is recorded as an absent slot. An absent slot carries a performance fact but no effect observation, so the join over {stage 1 `completed`} returns `completed`. The general rule "requested effects without sufficient observation are unknown" is not wired into the join.

**Repair:**
- Compute the aggregate over the parts in the declared composite effect scope.
- Give each part its latest authenticated, fresh observation.
- Report a compensation step against the parts it reverses.
- Treat every requested part with no sufficient observation, including absent slots, as `unknown`, or as `not_started` where the existing evidence rule allows.

**Minor:** Vacuous `reverted`, where no part began, should be `not_started`.

### F3 (Medium-High): Declared operators are not required to be total or consistent, and a known join failure can leave no verdict

**Where:** FOUNDATIONS.md, *Result conjunction*, the declared-operator paragraph. Sequential composition inherits this through "applies the operator rule above".

**Counterexample:** The operator is "A ∨ B on the release basis". The truth condition is (A∧J) ∨ (B∧J), where J is the basis join. The declared falsity condition is ¬A∧¬B. Take A satisfied, B satisfied and J falsified:
- The truth condition is not established.
- The falsity condition is not established.
- The fallback "invalid_basis, out_of_frame, indeterminate order applies to dependencies that could decide it" finds no dependency with any of those verdicts. J is `falsified`.

So the result is undefined. A reader who defaults to `indeterminate` understates a known join failure that conjunction rule 1 would report as `falsified`. Separately, nothing forbids overlapping conditions, such as truth "A satisfied" with falsity "primary B falsified", and there is no precedence for them.

**Repair:** Make well-formedness a precondition of a declared operator:
- The truth and falsity conditions are disjoint.
- Over fully decided leaves and joins, including join falsification, exactly one of them holds.
- An operator that is not well-formed yields `invalid_basis` on the composite.

### F4 (Medium): One basis-continuity failure can be classified two ways with opposite precedence

**Where:** FOUNDATIONS.md, *Result conjunction*, rule 1 and the "composite subject or governing basis itself cannot be interpreted" clause.

**Counterexample:** A is evaluated at revision b1 and B at b2, and the required relation "b1 and b2 coherent under the topology" fails.
- Read as a material join, it gives `falsified` under rule 1.
- Read as an uninterpretable composite basis, it gives `invalid_basis`, and that clause overrides component falsification.

The dispositions then diverge (reject or repair, versus re-bind), so two rules decide one question.

**Repair:** The composite basis declaration states which relations are basis conditions, giving `invalid_basis`, and which are joins, giving `falsified`. Each relation gets exactly one.

### F5 (Low): Single ownership

These are second statements that are not marked as references:

- **Retry condition.** TRANSFORMATION_LIBRARY.md *Recovery law* says "needs a causal repair before retry". FOUNDATIONS.md *Bounded construction* says "supported causal change". These differ for a resolved external outage, where something changed but nothing was repaired. The Library should refer to the Foundations rule rather than restate it.
- **Ticket binding.** Ticket Method is said to bind carrier "retention" in Foundations and carrier "reuse" in the Library. Name the one owned determination.
- **Domain enums.** *Transform* in the Library copies the Baseline WorkerResult and AC-013 enums without linking their owning loci. Single Ownership item 4 requires a copy to name its owner.

## Checked and holding

- The verdict precedence is associative on the fixed domain, and regrouping is correctly conditioned on having no hidden intermediate basis failure.
- Aggregate performance is `performed` while component performance is preserved.
- Candidate availability, fitness and acceptance are kept separate.
- `not_started` requires evidence, transport dispatch proves nothing, a lost acknowledgment gives `unknown`, and irreversible effects cannot be excluded from the boundary to claim reversal. `unknown` dominates in both the per-observation and aggregate rules.
- Configuration covers everything Bounded Transitions item 4 requires:
  - preservation of dependencies, obligations, observed and uncertain effects, authority and independence;
  - allocation only within grants the allocator holds and may delegate;
  - no authority from names, frames or capacity;
  - independence not supplied by a fresh context.

  I found no counterexample here.
- Ownership is otherwise sound. The conjunction, the unknown-effect rule, the UP-020 dispositions and the imports each have one owner and are referenced elsewhere.

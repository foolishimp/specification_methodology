# Final repair check: FROZEN 77f2efba…

**Result:** one demonstrable contradiction, introduced by this repair. The other named discriminators pass. Everything below comes from the provided text only. Nothing was run.

## Defect 1: a clean completion with an unrequested part observed not to begin composes to `partial`

**Locus:** FOUNDATIONS `#result-conjunction`, the effect paragraph changed in this diff:

> "Every material part that may have been affected, including an unrequested part … is unknown without sufficient observation unless evidence establishes not_started."

This combines with the unchanged join:

> "completed with only completed or not_requested gives completed; … every remaining fully observed mixture gives partial."

It also combines with the core single-value definition: "`partial` means an observed completed part and an observed unexecuted or reverted remainder."

**Counterexample:**
- A deployment completes, and its requested part is observed `completed`.
- Under the supported operating model, it could have caused an unrequested external notification.
- Observation establishes that the notification never began.
- The repaired rule gives that unrequested part only two legal labels: `unknown`, or `not_started` once evidence shows it did not begin.
  - `not_requested` is reserved for an "established effect-free scope under that operating model". That is an a-priori scope claim, which a part the model says "may have been affected" lacks.
  - So the observed non-occurrence yields `not_started`.
- The join then gives `{completed, not_started} → partial`.

**Consequence:**
- The traversal profile maps the composite to `partial_effect`, the "incomplete-effect disposition" with re-entry "acquire post-observation and explicit disposition". A fully completed requested effect with no side effect is reported as incomplete.
- This also misstates the meaning of `partial`. The unrequested part is not a "remainder" of the operation.
- Before this repair, unrequested parts were outside the join, so this case could not arise.
- The sibling case, `not_requested` operation plus a possible side effect observed absent, likewise yields `not_started` instead of an effect-free result.

**Required repair (core only):** state that an unrequested part with evidence that it did not begin contributes as `not_requested` in the join. Equivalently, restrict `not_started`/`partial` remainders to requested parts and amend the single-value `partial` definition to match. An unrequested part that began, whether completed, reverted or unknown, keeps its observed value.

No profile edit is needed. `J:*.effects` and the `no_effect` paragraph already defer to "the core rule". Changing the profile as well would create a second owner.

## Bounded checks passed

- **No request with a possible unintended effect.** The core now requires an established effect-free scope for `not_requested`. An unobserved material possible part is `unknown`. The domain-refinement sentence, the conjunction paragraph, `J:*.effects` and the `no_effect` mapping all agree.

- **Completed deploy plus an unknown unrequested external part.** The part is in the boundary ("each material part the operation may have affected … whether requested or unintended"), and "any unknown gives unknown". The single-value rule agrees: an unknown material remainder gives `unknown`. Common Requirements item 3 is not violated.

- **Unresolved operator well-formedness, then negation.** Unresolved well-formedness now gives `indeterminate`, "neither satisfaction nor falsification". The precedence ordering applies only "once well-formedness is established". A negation over that result can establish neither its truth condition nor its falsity condition, so it remains `indeterminate`. Negation cannot erase a failed leaf.

- **`j_a` is not its own input.** The cut tuple `a` excludes `j_a`. `j_a` is computed from `j_c`, `j_e` and the cut joins, and is stated to be "this evaluation's output, never its own input". A missing `j_a` is the downstream consumer's absent slot. The `semantic_cut_admission` row and OP-002 agree.

- **A missing component return vs a missing cut member.** These are distinguished correctly:
  - Missing, held or unauthenticated support gives `hold` plus `unresolved_cause` (`indeterminate`).
  - A demonstrated missing or inconsistent member or edge refuses (`falsified`), and missing support "cannot make an actually incomplete or mismatched cut complete".
  - Re-evaluating unchanged bytes is limited to supplied support. A changed member forces a successor cut. The `unresolved_cause` re-entry ("otherwise construct its successor") covers a held `j_c`, which forces new `e`, `r` and `F_k+1`.
  - The duplicate rule is scoped to cut identity.

- **`stale_frontier` decision `hold` with core `falsified`.** This is legal under the core's reason-sensitive pair map:
  - (`hold`, `stale_frontier`) maps to `falsified`.
  - (`hold`, `unresolved_cause`) maps to `indeterminate`.
  - "The word `hold` alone decides neither case."
  - The claim, cut and `frontier_complete` rows and the residual table agree.
  - "Without lowering the verdict" preserves standing.
  - Keeping `hold` is a domain decision, not a core verdict, and should not be renamed.

- **In-domain capability `out_of_frame`.** `J:*.verdict` and the profile's evaluation paragraph now admit all five verdicts. The legal pairs allow `performed` with a capability diagnosis. The decision is `hold`, or `indeterminate` for `transition_evaluation`. The stop `out_of_scope` keeps it distinct from the falsified `event_scope_compatible` decision `out_of_scope` with stop `refusal`. Re-entry matches the revised `unresolved_cause` row.

- **Label mapping vs evaluation, and admission vs downstream acceptance.** `valid`, `admitted` and `ready` satisfy only their own predicates and "do not establish the intended external outcome". `satisfied` permits `admitted` only with exact admitted `j_c` and `j_e` and established joins. The consumer separately requires `j_a`. A `partial` transition decides `falsified` or `indeterminate` from the intended-outcome predicate, separately from its effect state.

## Outside diff coverage (no finding)

The unchanged duplicate rule "refuses `refuse_duplicate`". That value appears in none of the closed stop, residual or decision domains. It is pre-existing and outside this repair diff. I note it only so it is not mistaken for something this check covered.

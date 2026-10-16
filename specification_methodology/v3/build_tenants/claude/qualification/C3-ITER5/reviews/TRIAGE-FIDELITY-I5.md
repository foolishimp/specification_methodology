# Triage of the iteration 5 fidelity review of the interpretation

Subject of the review: `a_c/i3` at `e5652ef`, group G14 (89 clauses) and the
premise P4a. The cases were written before the model was opened
([`a_c/i3/fidelity/cases-i5.md`](../../../a_c/i3/fidelity/cases-i5.md), 22
cases) and the review answered them from the model
([`a_c/i3/fidelity/review-i5.md`](../../../a_c/i3/fidelity/review-i5.md):
agree 14, disagree 7, cannot answer 1; 2 High, 12 Medium, Low items;
mechanical checks: 90 of 90 statements verbatim, 89 of 89 kinds of support
present with 0 mismatches on the nine formulas, 7 force hardenings, 5
premise-citation mismatches, 16 of 16 artifact digests). Same-family
working evidence, as both files say. Every finding is accepted; the repairs
are encoding decisions in `a_c/i3/tools/spec.py`, rebuilt and refrozen in
the I5-05c commit. The review's own re-reading of the repaired clauses is
not performed here; it goes to the I5-09 integrated readback with the
other repaired material.

| Finding | Severity | Disposition | Clause ids |
|---|---|---|---|
| non-requirements encoded `forbids`/`must-not` | High | repaired: operator `states`, no force; the comment records the design rule that a non-requirement is never `must-not` | `cr-no-preferred-strategy`, `cr-no-runtime` |
| non-entailments encoded `forbids`/`must-not` | Medium | repaired: `states`, no force, as the thirteen sibling non-entailments | `cr-prediction-error`, `cr-revised-model`, `cs-no-proof-of-reachability`, `ao-necessary-not-full`, `pd-no-statistical-independence` |
| a description encoded `requires`/`must` | Low | repaired: `states` | `cr-strategy-serves-z` |
| conditions not carried as arguments | Medium and Low | repaired: `condition` arguments; `ao-directions` now quotes through "conditional on Γ and Ω"; `ao-sufficiency` now quotes from its antecedent "A checker that always decides `q_t` correctly from π alone requires:" | `ao-directions`, `ao-sufficiency`, `cr-no-universal-termination`, `ao-pass-is-observation`, `fr-unresolved-universal`, `p4a` |
| supports differ from the source's own citations | Medium | repaired: supports follow the paragraph's parenthetical; `cr-calculi-lawful` drops P4a, which was the encoder's reading, with a comment | `cr-lawful-not-delivery` (P2, P3, P6), `cr-account-of-a` (P3), `cr-calculi-lawful` (P6, P2), `ao-observation-binding` (P6, P5, P1), `ci-failures-visible` (P3, P4b, P6) |
| a fragment ending at a semicolon; a statement without its antecedent | Low | repaired: `pd-incorrect-model` quotes the whole sentence to its citation; `ao-indeterminate-vs-unresolved` begins at "`indeterminate` is the core judgment" | `pd-incorrect-model`, `ao-indeterminate-vs-unresolved` |
| the `uses` relation links one clause | Low | repaired: supports `ci-selection` and `ci-retention-conditions` | `ci-used-by-activation-7` |
| subject label | Low | repaired: subject `assertion` | `ar-notation-obligations` |
| the kind of support is the helper's default | Low | recorded: the default is an encoding decision, stated in a comment at the helper; no clause's kind changed, the review found 0 mismatches | all 89 |
| FC5-2, the P4a prohibition uncovered | cannot answer | repaired: a new consequence clause quotes "Yet the steps compose although ... P4a forbids both." with `forbids`/`must-not`, supported by `p4a`; 155 clauses | `p4a-retention` |
| README counts and the pending paragraph | Low | repaired: 182 `not-encoded-i3`; the Known gaps paragraph points to the two fidelity files with the counts and the repairs | `a_c/i3/README.md` |
| uncovered parts named by the agreeing cases (the assurance family's instance premises (a) to (c); the owner of an approximate relation's bound; "all admitted conclusions"; "Shared derivations can be recorded once"; "The formula supplies no missing likelihood or prior"; "no exhaustive graph database is required"; "Selection alone produces no execution evidence") | coverage | not encoded at I5-05; named in the README's frame-index row for `construction-and-assurance` so the row says what it does not carry | — |

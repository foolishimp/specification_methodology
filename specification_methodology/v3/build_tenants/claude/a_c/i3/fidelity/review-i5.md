# Fidelity review, iteration 5: group G14 and premise P4a

Same-family working evidence. The reviewer is a Claude agent and the
tenant is the Claude line; under `design/INTERPRETATION.md` §6 and
CONSTRUCTION_BINDING section 1 this is a declared same-family exception.
The result is working evidence, not independent assessment, and it
supports only the scope stated below.

## 1. Basis and method

Subject commit: `e5652ef3a9c7a0503ac7176646383d424f533fee` (worktree
`specification_methodology-claude`, clean).

Order. [cases-i5.md](cases-i5.md) was saved first, from the source prose
and the design alone (its "Basis and order" lists what was read). Only
then were opened: `a_c/i3/fragments/G14.json` (89 clauses) and
`fragments/G1.json` (the `p4a` clause); `a_c/i3/axiomatic-program.json`
for counts, symbols and the `construction-and-assurance` frame index;
`a_c/i3/SIGNATURE.md` (Standing symbols, Operators, Argument roles, Kinds
of support); `a_c/i3/dispositions/ACTIVATION.md` and `FOUNDATIONS.md`
whole, the `#return-of-a-reconstruction` row of `EVALUATION.md` and the
row counts of all eight files; `a_c/i3/tools/spec.py` for the `c(...)`
helper and the G14 list only; `design/INTERPRETATION.md` §3 Conditions,
force and exceptions and Latitude (104-123); `standards/ACTIVATION.md`
1696-1703 (the §7 sentence the `uses` clause quotes); the README's
artifact digests. The cases file was then trimmed for length; its
determinations were not changed.

Method. Each case is answered from the clause's structured fields
(operator, `force`, `condition`, standing, `support`, `support-kind`,
subjects) and its quoted statement. A case is `cannot answer` when no
clause carries the determination. The mechanical checks ran in one
Python script over all 89 G14 clauses and `p4a`: statement occurrence in
the owning section at HEAD (heading to next heading of the same or higher
level, table rows removed, whitespace normalised), support and subject
resolution, kind count, the premise parenthetical at the end of the
statement's paragraph, disposition ids and totals, README digests.

Limits. Not run: `assemble.py --check`, `test_assemble.py`, the pinned
checker (to change no file). During the review two paths changed in the
worktree by another process, not by this review:
`qualification/C3-ITER3/tools/run_ac.sh` (modified) and
`qualification/C3-ITER5/returns/ac_controls_clean_e5652ef.json` (added);
neither was read, and no model or source file read here changed. Not verified: the Axiom Indexer digests, the
validation report's content, the projections beyond their digests, the
build tool's refusal behaviour, the three i3 repairs, the standing of
G1 to G4 clauses other than `p4a`. Severity: High for a wrong
determination (force inverted, a condition dropped, a wrong kind on a
formula, a statement not in the source); Medium for scope or trigger
narrowed or widened, or a wrong standing or support; Low for labelling, a
vacuous choice or wording. `indeterminate` is used only in the method's
sense; it does not occur below.

## 2. Results by case

Counts: 22 cases; agree 14, disagree 7, cannot answer 1.

- FC5-1 agree. `p4a`: `requires`, `premise`, no kind; "compose only when the first's result type and judgment satisfy the second's exact declared domain and preconditions". Low: the "only when" is not carried as a `condition` argument (cr-local-success carries one).
- FC5-2 cannot answer. No clause carries "the first step's other intermediate results and stop state are lost; P4a forbids both"; `p4a` quotes 477-478 only. Declared only by the frame-index row's "non-entailment arguments ... FOUNDATIONS §3".
- FC5-3 disagree, Medium. cr-lawful-not-delivery: force `states` preserved; supports `p6`, `p5` where the paragraph names (P2, P3, P6) at 227: P5 is not named, P2 and P3 are not cited.
- FC5-4 disagree, High. cr-no-preferred-strategy: `forbids`, `must-not` on "No exhaustive optimisation, universal numerical budget, scalar cost measure or preferred strategy is imposed"; the design: not required stays `may`, never `must-not`. cr-strategy-selection-owner `states` is right.
- FC5-5 agree. cr-no-universal-termination: `states`, no force; all three determinations and "where such a proof is absent" are in the statement; supports within (P5, P2, P6). Low: the trigger is not a `condition` argument.
- FC5-6 disagree, Medium (two clauses). cr-prediction-error and cr-revised-model: `forbids`, `must-not` on "alone does not decide" and "does not erase the counterexample or by itself repair"; "alone" and "by itself" survive only in the quoted text. The same hardening the i3 review found. cr-prediction-error is in the frame index.
- FC5-7 agree. cs-synthesis-derived: standing `consequence`, support `p6`. Low: the governing sentence "It is derived, not a further commitment" is not the quoted statement; the standing rests on the field.
- FC5-8 disagree, Medium. cs-no-proof-of-reachability: `forbids`, `must-not` on "do not by themselves prove reachability, stability, optimality or termination".
- FC5-9 agree, part uncovered. ar-notation-obligations: `states`, `p6`, `p1`; all 9 formula clauses carry `stated-formula`. Instance premises (a), (b), (c) at 1144-1149: no clause, and the omission is not named in the README row.
- FC5-10 agree. pr-step-form: `stated-formula`, `states`, `p4a`, "For all x, x':" kept; pr-completion-only `states` with "alone", supports exact. Low: the definition "F_i ⊆ X_i × X_(i+1) the declared transition relation" is not carried.
- FC5-11 agree, owner part uncovered. pr-approximate: `requires`, `must`, `p1`, `p6` exact; "cannot be assumed" is not separately hardened. The owner of the chosen relation and bound (row 1, ACTIVATION §4) has no clause; the README row excludes the family-table rows.
- FC5-12 disagree, Medium (two). ao-directions: `stated-formula`, directions and names intact, but "These implications are conditional on Γ and Ω" is carried by no clause and no `condition` (ao-qr's Γ, Ω partly recover it). ao-necessary-not-full: `forbids`, `must-not` on "does not establish the full obligation". ao-conjunction-coverage `requires` is right.
- FC5-13 agree. ao-soundness: both lines, "For every s in Ω", `stated-formula`, `p6`; ao-pass-is-observation `states` with "while the oracle's fidelity is unestablished" and the pass/fail symmetry in the statement (Low: trigger not a `condition`). "all admitted conclusions, not a favourable selected run": no clause.
- FC5-14 disagree, Medium. ao-sufficiency: `stated-formula`, `states` (not `requires`), but the scope "A checker that always decides q_t correctly from π alone requires:" is carried by no clause and no `condition`; the formula stands without its antecedent. ao-insufficient-response `requires` keeps all three alternatives.
- FC5-15 disagree, Medium. pd-no-statistical-independence: `forbids`, `must-not` on "do not establish statistical independence" (in the frame index). pd-agreement-shared-error `states`, "by itself" kept, supports within (P4a, P6, P1).
- FC5-16 agree. pd-no-per-test-document: `permits`, `may` on "No new per-test document, parallel ledger, fixed number of reviewers or prescribed provenance format is required", the design's rule for a non-requirement; four items kept. "Shared derivations can be recorded once": no clause.
- FC5-17 agree. qa-model-states: `requires` with `condition` "where quantified assurance is claimed"; qa-bayes `stated-formula` with Γ in every term; qa-denominator `requires`, `must`. "The formula supplies no missing likelihood or prior": no clause.
- FC5-18 agree. qa-joint-miss `stated-formula`; qa-independence-needed `requires` with "under the declared model"; qa-not-product-correct `states` with "it is not the probability that the whole product is correct".
- FC5-19 agree. qa-no-threshold `permits`, `may` (design rule); qa-no-waiver `forbids`, `must-not` on "cannot be waived by a cheaper assurance plan"; supports (P5, P6). The threshold's owner (row 6): no clause, declared.
- FC5-20 agree. ci-selection `stated-formula`, `states`; ci-exclusion `requires` with both conjuncts and "an absent edge is not evidence of non-influence"; ci-unknown-impact `requires` with the disjunction; ci-mandatory-gate `requires`, unconditional. Low: "A candidate selection is:" not carried. "no exhaustive graph database is required": no clause.
- FC5-21 agree. ci-e-new `stated-formula`, `p4b`, `p3`; ci-retention-conditions `requires` with the three conditions and "unchanged or covered by an established preservation relation"; ci-hash-alone `states` with "alone". "Selection alone produces no execution evidence": no clause.
- FC5-22 agree. fr-five-kinds `requires`; fr-external-predicate `requires` with source, scope and evidence; fr-no-tooling `permits`, `may` (design rule); fr-finite-examples `states`; fr-unresolved-universal `permits`, `may` with "where their governing conditions permit them" in the statement (Low: no `condition`).

## 3. Required checks

| Check | Result |
|---|---|
| Statement verbatim in owning section at HEAD, exactly once (whitespace-normalised, table rows removed) | 90 of 90 pass |
| Exactly one `support-kind` among the five | 89 of 89 G14 clauses; 80 `discharged-argument`, 9 `stated-formula`; `p4a` carries none, admissible for FOUNDATIONS §3 |
| Kind matches the source | 9 display-formula clauses (pr-step-form, ao-qr, ao-directions, ao-soundness, ao-sufficiency, qa-bayes, qa-joint-miss, ci-selection, ci-e-new) all `stated-formula`; no formula carries `discharged-argument`; 0 mismatches. Low: the 80 `discharged-argument` are the `c(...)` default, not a per-clause choice; for definitional and ownership sentences (cr-composition-boundary, cr-four-claims, cr-one-owner, ar-shared-owner, pd-assertion-provenance, pd-execution-provenance) the written argument the signature's meaning asks for is only the family table or a parenthetical |
| `force` against modal force | 7 hardenings: High cr-no-preferred-strategy, cr-no-runtime ("is imposed by", "adds no" as `must-not`); Medium cr-prediction-error, cr-revised-model, cs-no-proof-of-reachability, ao-necessary-not-full, pd-no-statistical-independence ("does not ..." as `must-not`); Low cr-strategy-serves-z (a description as `must`). 0 softenings. The same "does not / establishes neither / alone" form is `states` without force in 13 clauses (cr-lawful-not-delivery, cr-homeostasis, cr-repeated-activity, cr-resource-limit, pr-local-success-alone, pr-execution-not-discharge, ao-digest-not-fidelity, pd-implementation-derived, pd-incorrect-model, ci-link-not-model, ci-hash-alone, qa-not-product-correct, fr-finite-examples), so the group gives one modal form two forces. `may` on pd-no-per-test-document, qa-no-threshold, fr-no-tooling follows the design's rule and is not a defect |
| Conditions carried as `condition` | 2 carried (cr-local-success, qa-model-states). Not carried: ao-directions (Γ, Ω; sentence not quoted; Medium), ao-sufficiency (scope lead-in not quoted; Medium), cr-no-universal-termination, ao-pass-is-observation, fr-unresolved-universal (trigger in the quoted text; Low), `p4a` (G1 convention; Low) |
| Supports resolve to existing clauses | 90 of 90 |
| Cited premises against the source's parentheses | 85 consistent (exact, a subset of the named set, or none named). 5 mismatches, Medium: cr-account-of-a cites P0, source names P2, P3, P6; cr-calculi-lawful cites P4a, source P2, P3, P6; cr-lawful-not-delivery cites P5, source P2, P3, P6; ao-observation-binding cites P3, source P6, P5, P1; ci-failures-visible cites P5, P6 while its own statement ends "(P3, P4b, P6)" |
| Operators | `forbids` 9 (2 right: cr-three-accounts-distinct "never", qa-no-waiver "cannot be waived"; 7 listed above); `permits` 5 (cr-several-states and fr-unresolved-universal right; 3 by the design's rule); `requires` 22 (one soft, cr-strategy-serves-z); `states` 52; `uses` 1 |
| Subjects exist as concept symbols | 90 of 90 resolve (`p4a` names none, as the G1 premises). Low: ar-notation-obligations has subject `preservation-step` for a family-wide sentence |
| `uses` at ACTIVATION §7 | ci-used-by-activation-7 quotes 1698-1703 verbatim, consumer literal set, support ci-selection: right target ("affected when its dependencies D*(t) meet the impact cover I(Δ)"). Low: the sentence also names "the conditions for retaining evidence on a new subject"; ci-retention-conditions is not linked |
| Dispositions | the nine sections are `encoded-in-part` with exactly the G14 ids (29, 2, 2, 7, 11, 9, 10, 12, 6); ACTIVATION §7 lists ci-used-by-activation-7 beside three G1 to G4 clauses; `#return-of-a-reconstruction` (464-483) is `not-encoded-i3`; one row per heading outside code fences for all eight members (REFERENCE_FRAME: 57 rows, 57 headings, 31 `#` lines inside fences); totals 24 `encoded-in-part`, 8 `no determination`, 182 `not-encoded-i3` |
| Standing | 89 of 89 `consequence`, set by `c(...)`; no `policy-choice`, so no hollow argument; the source's policy-choice column (adequacy relation and bound, composition law, Ω, T and π, paths compared, threshold, dependency representation, carrier) has no clauses; instance premises a, b, c not encoded |
| Statement fragments | pd-incorrect-model ends at a semicolon; ao-indeterminate-vs-unresolved begins "It is distinct" with the antecedent `indeterminate` in the unquoted previous sentence. Low each |

## 4. README claims against what exists

- Coverage: 29 + 2 + 57 + 1 = 89 G14 clauses, true; 154 clauses (program and fragment sum 26 + 20 + 17 + 2 + 89), 5 frame indexes, 0 residuals, true; 80 and 9 kinds, true; `p4a` present in G1, true; "every section that holds an encoded clause is only partly encoded", true (no `encoded` row).
- Dispositions: 24 `encoded-in-part` and 8 `no determination`, true; "181 `not-encoded-i3`" false, 182 (lines 39 and 97): the EVALUATION section `Return of a reconstruction` added at e5652ef3 raised the count. "Every heading section ... has exactly one", true by the fence-aware count. "Groups G5 to G13 ... no disposition files", true (eight files).
- Frame-index row `construction-and-assurance`: scope and exclusions agree with the model; "the quantified-assurance formulas are stated, not discharged" matches the kinds. Three of its 16 clauses are the hardened `must-not` clauses (cr-prediction-error, ao-necessary-not-full, pd-no-statistical-independence), so the hardening reaches the projection. Uncovered sentences the row does not name: the instance premises (1143-1149), "conditional on Γ and Ω" (1247), the universal-soundness scope (1255-1257), "Selection alone produces no execution evidence" (1443); the blanket "only partly encoded" covers them.
- Evidence boundary: `assemble.py --check` and the 6 tests, not verified (not run); the checker materialisation, digests, `valid` with 0 diagnostics, 10 projections and byte reproduction, not verified; `checker-commands.log` exists. "Statements are quoted verbatim" agrees with 90 of 90; the tool's refusal behaviour not verified. "Fidelity is assessed separately (`fidelity/`, when present)": present now.
- Known gaps: the "pending (I5-05)" paragraph is superseded by this review and must be rewritten; its arithmetic holds (90 = 89 + 1; 154 - 90 = 64). The i3 repairs are "not re-reviewed", and not re-reviewed here; the repaired pattern ("by itself" hardened into a prohibition) recurs in G14 at cr-revised-model and four other clauses. "No residuals", true. P0's qualification literal, present.
- Artifacts: 16 of 16 SHA-256 values match the files.
- Coordinates: the statements are from the HEAD bytes, consistent with 90 of 90 exactly once in section.

## 5. Smallest repairs

- cr-no-preferred-strategy: operator `states`, drop `force` (design: not required stays `may`, never `must-not`).
- cr-no-runtime: operator `states`, drop `force`.
- cr-prediction-error, cr-revised-model, cs-no-proof-of-reachability, ao-necessary-not-full, pd-no-statistical-independence: operator `states`, drop `force`, as the 13 sibling non-entailments already are.
- cr-strategy-serves-z: operator `states`, drop `force`.
- cr-lawful-not-delivery: support `p2`, `p3`, `p6`.
- cr-account-of-a: drop `p0` (keep `p3`, or cite `p2`, `p3`, `p6`).
- cr-calculi-lawful: drop `p4a` or add a `qualification` naming it as the encoder's reading.
- ao-observation-binding: drop `p3` or cite `p6`, `p5`, `p1`.
- ci-failures-visible: support `p3`, `p4b`, `p6`, matching its own parenthetical.
- ao-directions: add `condition` "conditional on Γ and Ω", or a clause quoting 1247.
- ao-sufficiency: add `condition` "for a checker that always decides q_t correctly from π alone".
- cr-no-universal-termination: add `condition` "where such a proof is absent" (or split the sentence's three determinations).
- ao-pass-is-observation: add `condition` "while the oracle's fidelity is unestablished".
- fr-unresolved-universal: add `condition` "where their governing conditions permit them".
- pd-incorrect-model: extend `until` to the sentence end "(SPEC_METHOD §4 ...) (P4a, P6, P1)." or stop at a full sentence.
- ao-indeterminate-vs-unresolved: start `find` at "`indeterminate` is the core judgment" so the antecedent is quoted.
- ci-used-by-activation-7: add support ci-retention-conditions.
- ar-notation-obligations: subject `assertion` or a family-wide symbol (Low).
- p4a: add `condition` for "only when ..." if the G1 convention admits one (Low).
- README lines 39 and 97: 181 to 182; Known gaps: replace the "pending" paragraph with pointers to `fidelity/cases-i5.md` and `fidelity/review-i5.md`, the counts above, and the words "same-family working evidence"; note the recurring `must-not` pattern.
- Coverage (optional): a `premise` clause for the instance premises (1144-1149) owned by FOUNDATIONS §4, or name the omission in the frame-index row.

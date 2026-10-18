# RV2b — Review of revision 2b repairs F1 and F2 (RF1, TR2, I4)

**Standing: same-family working check, not acceptance.** A fresh Claude context that wrote none of the subject reviewed it. The subject was written by other Claude contexts. This review repairs nothing and changes no git state.

Disclosure: before recording the expectations below, the reviewer saw the one-line subjects of `3940e7a`, `85a96d8` and `de7c617` and the file list of `de7c617`, and read the ledger's dispositions (a named source). No subject text was read before §1 was written.

| Coordinate | Value |
|---|---|
| Subject | `de7c617` (`specification_methodology-claude`), prefix `specification_methodology/v3/build_tenants/claude/` |
| Previous version | `9de0f7f` |
| Findings repaired | Codex review `20261014T000519Z_REVIEW_CLAUDE_V3_REVISION_2_PURPOSE_AND_IMPLEMENTATION.md`, F1 and F2 |
| Predecessor | installed `v2.5.1-rc.2` `REFERENCE_FRAME_METHOD.md`, `TRAVERSAL_OCCURRENCE_PROFILE.md` (read-only) |
| Common | `specification/requirements/README.md` at `de7c617` |

## 1. Expectations recorded before opening the subject

Sources read: Codex F1 and F2 with their smallest-repair tests; predecessor Revision Actions, RF-005, RF-011, RF-012, Return A Closed Result, Diagnostic Order; predecessor profile disposition law, stop kinds, residual re-entry table and `transition_evaluation` row; common Single Result Algebra item 3 and Bounded Transitions item 5; ledger dispositions for F1 and F2 and the 2026-10-12 ruling (ledger lines 232–233).

### F1 expectations

- E1.1 The revision clause states two separate questions: whether the frame declaration needs a new identity or revision coordinate, and whether prior activations and results stay valid. The second is decided by the reuse rule's single owner (ACTIVATION §7 per the ledger), which the clause cites and does not restate as a second owner.
- E1.2 No text infers "reopens no result" from "no declaration changed". A revision that needs no new coordinate can coexist with invalidated results.
- E1.3 Test A: explanatory metadata that changes no material input, evidence, basis, authority or applicability leaves the result reusable.
- E1.4 Test B: changed admissible evidence, or an activation of the wrong frame family, reopens the affected claims before reliance; demonstrably independent results survive; the predecessor/successor relation of the reopened result is kept.
- E1.5 Conservation: the predecessor's nine revision actions remain available; "every material revision changes frame identity or revision coordinates and states which prior activations, results, and coverage claims require reevaluation" is kept; RF-005 (stale or mismatched basis returns `invalid_basis` or requires reactivation) and RF-011 (material topology mutation causes reevaluation, revision or recharting before reuse) are not weakened; Return A Closed Result's reuse rule (role, conversation or resumption alone does not invalidate; changed material inputs or a declared revising observation invalidates the affected result; independent evaluations supply their own evidence) is kept once.

### F2 expectations

- E2.1 Two predicates are kept apart: whether the declared intended outcome holds (the transition result), and whether the dispatched effect has completed or terminated (the effect's completion status and its residual).
- E2.2 Closed-interval case: all five updates required by 12:00; at 12:01 evidence establishes three; termination unknown. Result `falsified`, with the unknown termination retained as its own residual and stop; no further effect or retry until reconciled.
- E2.3 Lost-response case: effect dispatched, no response, no counterexample. Result `indeterminate` with `hold` and the residual; no retry until reconciled.
- E2.4 Each refined value maps to exactly one core value (common item 2). The key for `falsified` vs `indeterminate` is established non-attainment vs undecidable outcome, not termination.
- E2.5 The 2026-10-12 meaning holds: `partial_effect` and `partial` map to `falsified` only on demonstrated non-attainment, otherwise `indeterminate`. A partial or uncertain effect alone never yields `falsified`. Common item 3: an effect of unknown completion never maps to no effect or completed.
- E2.6 Conservation: the predecessor's `partial_effect` disposition, residual and stop survive even when the outcome is `falsified`; re-entry still requires post-observation and an explicit disposition before any further effect; the predecessor `partial` decision is accounted for.
- E2.7 ACTIVATION §3 Effects and §5 reconciliation trigger on any effect whose completion is uncertain, whatever its outcome value; reconciliation is not tied to a single value such as `completion_unknown` when a second value can also carry uncertain completion.
- E2.8 GLOSSARY, EXECUTIVE_BASELINE, SPEC_METHOD and frontier rows use the same split and point at one owner.

## 2. Results

Line numbers are at `de7c617` under `standards/` unless another file is named. ACT is ACTIVATION, RF is REFERENCE_FRAME, TR is TRAVERSAL_OCCURRENCE, EB is EXECUTIVE_BASELINE, SM is SPEC_METHOD.

| Question | Predicate evaluated | Core value | Findings |
|---|---|---|---|
| Q1 | Codex's two F1 tests pass by desk trace on the repaired text, result validity has one owner (ACT §7), and rc.2 revision actions, RF-005, RF-011 and Return A Closed Result are conserved | satisfied | RV2b-6, RV2b-7 (Low; neither defeats a test or ownership) |
| Q2 | Codex's two F2 traces give `falsified` with the end as a residual and `indeterminate`; attainment and the end are kept apart; each refined value maps once; the 2026-10-12 meaning holds | satisfied | RV2b-3, RV2b-4 (Low; neither defeats a trace) |
| Q3 | no member outside `frames/` keeps the old split or ties reconciliation to a narrower class than ACT §3's uncertain completion | falsified | RV2b-1 (Medium), RV2b-2 (Low) |
| Q4 | no changed determination loses or weakens an rc.2 determination | satisfied | none |
| Q5 | the changed text reads one way and every relative link resolves | falsified | RV2b-5 (Low); every link resolves |

No finding blocks closure of F1 or F2 on their deciding rules. RV2b-1 must be repaired before the I4 propagation can be called complete.

### Q1 — F1

Expectations E1.1 to E1.5 are met.

Structure. RF §10 (RF:874–890) separates the two questions: a new revision coordinate "turns on the frame's declarations"; whether a closed result stays valid "is decided by the reuse rule of ACTIVATION §7". The clause that F1 named ("a non-material revision … reopens no result") is gone from §10 and from the table row at RF:170. The row now points to ACT §7. ACT §7 (ACT:1261–1282) is unchanged and remains the one statement of reuse and invalidation. RF §10 refers to it, and its examples apply it. The default reopening after a material revision is a frame-domain refinement keyed on the coordinate mismatch (RF-005). It is now labelled a tightening that the predecessor implies (RF:867–872), and the earlier claim to restate the predecessor is withdrawn.

Test A, harmless explanatory metadata. The metadata changes no declaration, so no new coordinate is needed. It changes no material input and is no revising observation, so "it invalidates no result by itself" (RF:887–889). ACT §7 also invalidates nothing on a role, conversation or resumption change alone. Reuse proceeds after the consumer's exact applicability check. **Reuse preserved.**

Test B1, newly acquired admissible evidence bearing on a closed result, with every declaration unchanged. No new coordinate is needed. The evidence is a changed material input under ACT §7, so the affected result is invalidated before reliance. RF:883–886 also reopens every coverage row and coverage claim that consumed it. Demonstrably independent surviving results are preserved, and so is the predecessor/successor relation (ACT §7). **The affected claims reopen and independent work survives.**

Test B2, a clarification that finds a recorded activation outside its frame's family, with every declaration unchanged. No new coordinate is needed. The activation answers Diagnostic order question 1 "no" (RF:816–842, family inclusion at RF:829–842), so the result fails the exact applicability check that ACT §7 requires for reuse. RF:881–886 names this case explicitly. The result, and the coverage rows and claims that consumed it, reopen. Independent results survive. **The affected claims reopen and independent work survives.** This reverses the C3S-01 Task-B inference that Codex cited ("non-material", "reopens nothing").

Conservation. The nine revision actions are carried in the predecessor's order. "Every material revision changes frame identity or revision coordinates and states which prior activations, results and coverage claims require reevaluation" is carried (RF:846–855). RF-005 (RF:274–280) and RF-011 (RF:338–346) are unchanged and no weaker than rc.2. Return A Closed Result is carried at ACT §7, and its frontier row 342 stays `conserved`.

### Q2 — F2

Expectations E2.1 to E2.8 are met, except where RV2b-3 and RV2b-1 note otherwise.

The closed-interval case. The declared outcome is all five updates by 12:00. At 12:01 the admitted evidence establishes that three were made within the interval. Whether the effect has ended is unknown.
- ACT §3 (ACT:802): `not_effected`, because "an interval that the declared outcome bounds has closed with part of it not done". It maps to `falsified`, and the two missing updates are the counterexample.
- ACT:810–823: the end is not established, so it is recorded beside the value as a residual naming the observation that would establish it. "The residual does not weaken the counterexample, and the counterexample does not resolve the residual."
- ACT:825–830: this is an effect of uncertain completion. §5 reconciles it before any repetition or dependent action, and "a `not_effected` value licenses neither treating the effect as absent nor repeating it while its end is not established".
- TR: `partial_effect(not_attained)` and `partial(not_attained)` map to `falsified` (TR:929–939, 963, 965). The `partial_effect` residual and stop stay, with explicit re-entry before any further effect (TR:963, 1036–1046). Disposition row TR:1339 gives `not_effected`.
- EB:1094–1097 and SM:895–898 reconcile before reactivation or retry.
- **Result: `falsified`, with the end kept as a residual and no retry until reconciled.**

The lost-response case. The effect was dispatched, its response was lost, and no counterexample was observed.
- ACT:803: `completion_unknown` maps to `indeterminate`. ACT:805–807 adds that a lost response is no evidence about the subject.
- TR:940–951: this is `partial_effect(undecided)`, mapping to `indeterminate`, because the post-observation is missing or no counterexample was observed. If the post-observation is missing, `transition_subject_complete` gives `indeterminate` plus `unobserved_subject_state` (TR:966).
- Reconciliation is required before retry.
- **Result: `indeterminate`.**

Separate predicates. Attainment of the outcome decides between `not_effected` and `completion_unknown`. The end is a separate residual, which travels in the `partial_effect` residual and survives every join (TR:1036–1040). On the success side the end is a conjunct of `completed` (ACT:801, TR:1338). FOUNDATIONS §4 Standing requires this through its last bullet (FOUNDATIONS:718, common item 3), and the text cites that bullet. RV2b-3 records the wording gap that results.

Each value maps once. ACT §3 has three values and three core values. TR has four refined values, `partial_effect` and `partial` each split into `not_attained` and `undecided`, and each has one row (TR:963–966). The disposition table maps five rows, one each (TR:1338–1342). The parent-value rule is untouched.

The meaning of 2026-10-12 is kept. A partial value gives `falsified` only when the admitted evidence establishes non-attainment with no later completion that can reach the outcome. Every other case gives `indeterminate`. `completed` is never reached from an effect that may still be acting.

Common item 3, last bullet ("an effect whose completion is unknown never maps to no effect or to completed"). An effect that may still be acting now carries `not_effected`, the same Effects value that disposition `no_effect` takes (TR:1342). The bullet still holds. The value means "did not occur in full", not absence. The part that occurred is named with it. The end residual travels. ACT:828–830 and TR:1041–1043 forbid treating the effect as absent or ended. A consumer that reads only the Effects value must read the residual too, and EB:1212 carries `residuals` in the work result. This is an observation, not a finding.

### Q3 — consistency

Two searches were run over `standards/` (recursive, `templates/` and `schemas/` included, `frames/` excluded) and `frontier/`. The first was for the value names `(ended)`, `(unknown)`, `partial_effect(` and `partial(`. The second was for the old rule in plain words: "end is not observed", "has ended", "effect ended", "terminat" as a word start, "partial effect", bare `partial_effect` outside TR, "its end" and "still acting". Neither found the old split in any member. Every hit for the plain words is either the new ACT §3 text or a locus aligned by I4. ACT:844–847 and TICKETS:456 use "terminate" about totality and triage, not about effects. GLOSSARY:325, EB:235, EB:741, EB:1094–1097, EB:1791, SM:727, SM:895–898, SM:1853 and frontier rows 547 and 641 all use the new split. Row 641 is byte-identical to TR:1658, and row 547 to EB:1791.

One member still ties the rule to the narrower phrase (RV2b-1), and three loci keep the phrase as wording only (RV2b-2).

### Q4 — conservation

Each changed determination was compared with rc.2. Nothing was lost or weakened.
- RF revision actions, the material-revision sentence, RF-005, RF-011, Diagnostic order and Return A Closed Result are all conserved, as described in Q1.
- The removed clause about non-material revisions was tenant text. rc.2 has no such clause, so its removal loses no predecessor determination.
- The TR disposition law is carried at TR:1307–1317. So is "if an effect has begun and cannot establish a complete disposition, `partial_effect` stays explicit and a bounded post-effect observation is required" (TR:1353–1356). The predecessor's `partial` decision, its `partial_effect` stop and its residual re-entry ("acquire post-observation and explicit disposition before any further effect") are kept under both refined values.
- `completed_effect` now also requires the end. That is consistent with rc.2's "complete disposition" and is a tightening, not a weakening.
- ACT §3 Effects and the §5 sentence are new in this corpus. Frontier row 649 still holds per the TR2 delta.

### Q5 — writing and links

A slug check over the relative links of ACT, RF, TR, EB, SM and GLOSSARY finds no missing file or anchor. That includes `ACTIVATION.md#7-closed-result-and-reuse`, `FOUNDATIONS.md#2-ontology`, `ACTIVATION.md#effects` and `ACTIVATION.md#5-work-state-and-restart`. The prose is direct, apart from RV2b-5.

## 3. Findings

| ID | Severity | Locus | Finding | Smallest repair | Blocks |
|---|---|---|---|---|---|
| RV2b-1 | Medium | ACT:331–338 (§1 Configuration, Reconfiguration); CONFORMANCE:95 (CD-01) | The reconfiguration rule says "the effects, including those of unknown completion" and "an effect of unknown completion is resolved sufficiently for the next dependent action before that action (§3 Effects, §5)". §3 now defines the reconciled class as an effect of *uncertain* completion: `completion_unknown`, or `not_effected` with its end not established (ACT:825–827). I4 replaced this same phrase at EB:741 and SM:727 for this reason, but TR2 and I4 did not reach ACT §1. Read narrowly, a hand-over between actors need not resolve a `not_effected` effect that may still be acting, which is the closed-interval case. §3 and §5 still require reconciliation, so no unsafe action is licensed. Still, one rule is stated at two widths within the owning member (common Single Ownership items 3 and 7). CD-01's case text uses the same word, while its row 14 (CONFORMANCE:142) says "uncertain". | Replace "unknown completion" with "uncertain completion" at ACT:333 and ACT:338. Optionally make the same change in CD-01. | Does not block F2's deciding rule. It blocks the claim that the propagation is complete. |
| RV2b-2 | Low | PRODUCT_DEFINITION:453; SM:1700 | Wording only. PRODUCT_DEFINITION:453 says that a consumer cannot read "an operation of unknown completion as either completed or not effected". Read against the new §3, this denies `not_effected` to an operation whose end is not established, which §3 now permits. The domain's own `not_effected` cases have an established end: a refusal before any effect, and a verified restoration. So no rule changes. SM:1700 ("one of unknown completion included") concerns recording only. | At 453, name the value: "an operation whose value is `completion_unknown`". At SM:1700, write "uncertain completion". | No |
| RV2b-3 | Low | ACT:791–803, 810; TR:940–947 | The stated predicate is "the declared outcome of the effect is attained", and ACT:810 says the end "is a second question, not the predicate above". Yet the case "outcome shown in full while the effect may still be acting" is `completion_unknown` / `partial_effect(undecided)` (`indeterminate`), even though the stated predicate is decided. TR's gloss "cannot decide whether the intended outcome is or will be met" then lists "shows the outcome met". The assignment is required by FOUNDATIONS:718 and conserves the pre-TR2 behaviour, so standing is never raised. The defect is that the core value does not truthfully answer the predicate that travels with it (common item 4). | Either state the predicate as "the declared outcome is attained and what the effect leaves on the subject is settled", or say at ACT:810 that the end decides no `not_effected` value but is a conjunct of `completed` under FOUNDATIONS §4 Standing, and gloss the sub-case as undecided on settlement. | No |
| RV2b-4 | Low | ACT:802; TR:929–935 as it feeds disposition row TR:1339 | The judgment layer is not affected: `transition_evaluation` has its own `falsified` decision (TR:976). The risk sits at the Effects-value and disposition layer. The ground of `not_effected` and the cause `not_attained` list shortfall shapes after a colon: "no effect began, the effect ended short, or an interval … closed with part of it not done". Some non-attainment established while the effect may still be acting has another shape, such as an irreversible change the outcome contract forbids, or an overshoot of an exact count. It fits the general clause "no later completion of the effect can make it occur as declared", but neither the listed shapes nor "did not occur in full". A reader who takes the list as exhaustive sends it to `completion_unknown`, which is the masking F2 described, for counterexamples that are not shortfalls. Codex's two tests pass. | Mark the list as examples, and write the head as "the declared outcome is not attained" instead of "did not occur in full". | No |
| RV2b-5 | Low | RF:170 | "An unchanged declaration keeps no result closed" also reads as "with an unchanged declaration, no result stays closed", which contradicts Test A. §10's own wording (RF:877–878, "an unchanged declaration is no ground for keeping a result closed") is unambiguous. | Copy §10's wording into the row. | No |
| RV2b-6 | Low | RF:881–886; ACT:1270–1276 | The wrong-family branch reaches ACT §7 only through the exact applicability check. §7's invalidation sentence names changed material inputs, a declared revising observation and a changed basis. A misbound activation is none of these unless it is read as a changed input. The conclusion "reopens that result" follows from Diagnostic order question 1 (an activation outside the family answers no, RF:829–842) and §7's exact applicability condition. §7 therefore owns the case through applicability, and ownership stays single. Only the written route is missing, so a reader can take RF §10's example as a ruling of its own. | In §10's example, name the route: "fails the exact applicability check of ACTIVATION §7 (RF-001; Diagnostic order question 1)". | No |
| RV2b-7 | Low | RF:853–855, 874–877 | §10 keeps "every material revision changes frame identity or revision coordinates" and adds "a revision that changes no declaration needs no new coordinate". Materiality in rc.2 (#material-relation) and in FOUNDATIONS:61 is a property of a changed relation. A clarification that changes no declaration changes no frame relation, so it is not a material revision, and the two sentences agree. A reader who applies FOUNDATIONS:61 to the revision event, because it changed a result, could still call it material and mint a coordinate. That over-invalidates through RF-005 and never causes unsafe reuse. A second gap: on the path with no declaration change, the reopened results have no stated record, whereas on the material path "the revision record lists those results as reopened". | Add one clause: a revision is material when it changes a frame declaration in a way that is material under FOUNDATIONS §2; results reopened without such a change are reopened under ACTIVATION §7 and recorded in the work state (ACT §5). | No |

## 4. Residuals, not findings of this review

- At `de7c617`, the frames `rf-task-b.md` and `traversal-task-f.md` still carry the old text, as RF1 and TR2 report. Frames were outside Q3. The worktree's uncommitted frame changes were not reviewed and were not touched.
- No case in CONFORMANCE and no qualification fixture binds the four test cases. Their only verification is this desk trace.
- The C3S-01, C3S-03 and F-03 oracles still use the old split. Under the repaired text, occ-24 in C3S-03 is `falsified` only if the fixture's facts establish an ended effect or a closed interval; otherwise `indeterminate` is correct. The ledger's statement that the repair decides occ-24 in favour of `falsified` holds only on that condition.
- This pre-dates the revision and RF1 did not change it: frontier row 364 (`#revision-actions`) reads "conserved", whereas the member's own row (RF:1184) reads "conserved; the tenant text carries a labelled tightening: prior results reopen by default". The two cells are not identical, unlike rows 547 and 641.

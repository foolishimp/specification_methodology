# Triage of R-I5-01

One triage, one repair round, one successor readback (PLAN §3). Subject of
the readback: `e731bd7`. Every finding is accepted; none is declined. The
repairs are in the I5-01c commit. "Repaired" means the reviewer's fix was
applied; "repaired differently" says how.

| # | Severity | Disposition | Where |
|---|---|---|---|
| 1 | High | repaired: "A revised model does not erase the counterexample or by itself repair the realisation." | ACTIVATION §1 Feedback and diagnosis |
| 2 | High | repaired: sixth subsection `### Formal representation` carrying the five standings, the external-predicate rule, no selected tooling, the demonstration cases, finite examples, the unresolved universal claim and no seventh criterion; header says six subsections and names formal representation; F22 gains an eighth row (P1, P6; pillars 6, 10); the index row lists the subsection and pillar 10 | FOUNDATIONS §4; §3 index |
| 3 | High | repaired: the constraint sentence inserted after the cost sentence | FOUNDATIONS §4 Change impact and evidence reuse |
| 4 | Medium | repaired: a paragraph after the invalidator list maps a changed source, task or actor condition to a changed basis or a material input change, and bounds the role-change sentence | ACTIVATION §7 |
| 5 | Medium | repaired: the parenthetical now names ACTIVATION §4 Refinement, Exact and approximate steps, as owner of the per-step law applying this obligation; ACTIVATION §4's closing sentence names FOUNDATIONS §4 Preservation through construction as owner of the composition's end-to-end obligations and bound, keeping per-step adequacy as the §4 addition | FOUNDATIONS §4 Preservation; ACTIVATION §4 |
| 6 | Medium | repaired: FOUNDATIONS defines "`I(Δ)`, the impact cover"; ACTIVATION §7 writes "impact cover `I(Δ)`" | both |
| 7 | Medium | repaired: the synthesis says ACTIVATION §1, a tier 1 foundations member of this corpus, owns the relation; the tier allocation is `design/DOCUMENT_STRUCTURE.md` | FOUNDATIONS §3 |
| 8 | Low | repaired: "is imposed by this relation or its consumers" in the prose and in row 11 | ACTIVATION §1 |
| 9 | Low | repaired: "may add", "may change", "may continue" | ACTIVATION §1 |
| 10 | Low | repaired: "must establish … must be acquired and justified"; "The denominator must be nonzero." | FOUNDATIONS §4 |
| 11 | Low | repaired: "Steel thread, phased (waterfall) delivery and iterative delivery are possible strategies" | ACTIVATION §1 |
| 12 | Low | repaired: "across the Intent, Product and Specification of the Product that owns the work … its descriptions refine Z" | ACTIVATION §1 |
| 13 | Low | repaired: ", not new execution states" | FOUNDATIONS §4 |
| 14 | Low | repaired: the tenant sentence added to the header; "the tenant's choice" | FOUNDATIONS §4 |
| 15 | Low | repaired: P0 (recovered) added to row 11's premises; finiteness attributed to P0, exhaustion to P5 | ACTIVATION §1 table |
| 16 | Low | repaired: §3 and §6 linked in row 14 | ACTIVATION §1 table |
| 17 | Low | repaired: "its binding of the step to the construction relation applies the tenth to fourteenth rows" | ACTIVATION §1 |
| 18 | Low | repaired: the three cross-member citations moved from column 3 into the consequence text | ACTIVATION §1 rows 12, 13; FOUNDATIONS F22 row 7 |
| 19 | Low | repaired differently: run-in "Risk model." added to the first paragraph; the heading and its anchor are unchanged so the other references stand | FOUNDATIONS §4 |
| 20 | Low | repaired: Γ is "the governing basis bound at intake under ACTIVATION §1 and the material assumptions, together written Γ here" in both places | FOUNDATIONS §4 |
| 21 | Low | repaired: "ACTIVATION §2 to §7" | ACTIVATION §1 |
| 22 | Low | repaired: Assertions and observation cited from Evaluation and completion | ACTIVATION §1 |
| 23 | Low | repaired: the resumption sentence added to Preservation, progress and completion | ACTIVATION §1 |
| 24 | Low | repaired: bounding moved to the P0 row | FOUNDATIONS §3 |
| 25 | Low | repaired: "The applicable declared requirements and the declared calculi of the tenant's binding govern…" | ACTIVATION §1 |
| A | author's own | repaired: the Construction relation block moved to immediately before `### Intake`, so the Transitions section keeps its Stops, Progress and Purpose paragraphs | ACTIVATION §1 |

Coverage items the reviewer could not verify (CCM-8 to CCM-21; BT-AR2,
BT-AR5; AS-F5, AS-F9) are owned by ACTIVATION §2, §3, §5 and §6, EVALUATION
§3 and CONFORMANCE, which were outside its scope; they are checked when
those consumers are wired at I5-02 and I5-09.

Successor readback R-I5-01b: the repaired passages, the Formal
representation subsection, and the three `conserved` frontier rows carried
at ACTIVATION §7 (`REFERENCE_FRAME_METHOD.md#return-a-closed-result`,
`DESIGN_MODULE_METHOD.md#4b-ontology-first-design-rule`,
`DESIGN_MODULE_METHOD.md#11d-post-ticket-design-review-rule`) read against
their rc.2 sources, because §7 gained two paragraphs.

## Triage of R-I5-01b

Successor readback of `9e92e79` ([report](R-I5-01b.md)). No obligation
absent or changed. Conserved rows: `#return-a-closed-result` conserved;
`#4b-ontology-first-design-rule` and `#11d-post-ticket-design-review-rule`
compatible with the two new §7 paragraphs, full judgment resting on their
other, unchanged loci. Twelve findings, dispositions below, repairs in the
I5-01d commit. No third readback: the repaired sentences go to the
integrated readback of I5-09.

| # | Severity | Disposition | Where |
|---|---|---|---|
| 1 | Medium | repaired: "the three invalidators below are kinds of change Δ, and a closed result is affected when its dependencies `D*(t)` meet the impact cover `I(Δ)`"; the FOUNDATIONS sentence says the same | ACTIVATION §7; FOUNDATIONS §4 Change impact |
| 2 | Medium | repaired: "Invalidation withdraws the result from direct reliance; whether its evidence is retained on the new basis is decided by `retain_applicable` of FOUNDATIONS §4 Change impact and evidence reuse, and the changed coordinate alone establishes neither that the claim fails nor that it holds." | ACTIVATION §7 |
| 3 | Medium | repaired differently: P0's contribution restricted to context and attention; the finiteness of time, spend and other resources attributed to the selected execution binding (SPEC_METHOD §11) in the consequence, rather than a new instance premise | ACTIVATION §1 row 11 |
| 4 | Low | repaired: "no preferred strategy is imposed" | ACTIVATION §1 row 11 |
| 5 | Low | repaired: the per-step law for exact and approximate steps, including inadmissibility of a step that is neither, is new; the adequacy-relation and composition-bound obligations are FOUNDATIONS §4 | ACTIVATION §4 |
| 6 | Low | repaired: "Faithful refinement, defined above, requires exact steps." | ACTIVATION §4 |
| 7 | Low | repaired: ACTIVATION §1 and §5 and SPEC_METHOD §4 added to the consumer list | FOUNDATIONS §4 header |
| 8 | Low | repaired with finding 1: "the three invalidators below" | ACTIVATION §7 |
| 9 | Low | repaired: "Three accounts of the subject, distinct from the accounts of a construction (FOUNDATIONS §2)" | ACTIVATION §1 |
| 10 | Low | repaired: "five kinds of support for a statement" | FOUNDATIONS §4 Formal representation |
| 11 | Low | repaired: "candidate causes of different kinds that are not conflated, of which the relation names four" | ACTIVATION §1 row 13 |
| 12 | Low | repaired in part: "can add", "can change", "can continue" and "can strengthen" restored where the common text uses "can"; "phased (waterfall) delivery" kept, since "phased" defines the term for a reader who does not know "waterfall"; "places on construction" kept, since the synthesis's obligations fall on construction done with the method and the common sentence's "the method" denotes the same obligations | ACTIVATION §1; FOUNDATIONS §3, §4 |

Sentences for the I5-09 integrated readback: ACTIVATION §7 paragraphs 2
and 3 as repaired; ACTIVATION §1 rows 11 and 13; ACTIVATION §4 Refinement's
closing provenance sentence; FOUNDATIONS §4 header consumer list and the
Change impact closing paragraph.

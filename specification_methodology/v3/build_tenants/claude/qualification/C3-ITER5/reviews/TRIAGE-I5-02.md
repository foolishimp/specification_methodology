# Triage of R-I5-02

One triage, one repair round, one successor readback (PLAN §3). Subject of
the readback: `f9d8cc9` ([report](R-I5-02.md)). Every finding is accepted;
the repairs are in the I5-02b commit. "Repaired differently" says how.

| # | Severity | Disposition | Where |
|---|---|---|---|
| 1 | High | repaired: "Where a claim about a construction concerns its recursive or repeated work, it is one of the four kinds … and states which" | EVALUATION §1 |
| 2 | Medium | repaired: the paragraph cut to the triage-specific application (diagnose among the four causes, route to the owner, severity and priority under TICKETS' policies, a bug list projects work state) and marked as applying ACTIVATION §1 Feedback and diagnosis, stating no second relation; the "law carried" marker removed | SPEC_METHOD §4 |
| 3 | Medium | repaired: row 5 names EXECUTIVE_BASELINE §3 Engagement applicability, which applies the rule and adds two bindings, and TICKETS Condition-based closure and reuse as the carrier; the "no other" clause removed | ACTIVATION §1 Consumers |
| 4 | Medium | repaired: ODD Graph functions moved to row 8 | ACTIVATION §1 Consumers |
| 5 | Medium | repaired: EVALUATION §3 removed from rows 3 and 4; it stays under row 5 | FOUNDATIONS §4 Consumers |
| 6 | Medium | repaired: row 8 states that no separate consumer applies yet, names AXIOMATIC_CALCULUS Constraint surfaces and CONFORMANCE §4 as the loci that carry neither the five kinds of support nor the demonstration cases, and says the obligation is open until the interpretation and its cases are written (I5-05 with I5-A3) | FOUNDATIONS §4 Consumers |
| 7 | Medium | repaired: SPEC_METHOD §4's determination of the surfaces and evidence to re-derive now cites Change impact and evidence reuse as the selection `S_Δ`; row 7 names ACTIVATION §7 with §5 and EVALUATION §3 reaching it through §7, RELEASE §8 and §9, and SPEC_METHOD §4 at that determination | SPEC_METHOD §4; FOUNDATIONS §4 Consumers |
| 8 | Medium | repaired: row 6 names EXECUTIVE_BASELINE Technical triage (confidence), SPEC_METHOD §8 (probability informs priority) and ASSURANCE §8 (project-defined scalar) as consumers, and each locus now cites Quantified assurance | FOUNDATIONS §4 Consumers; EXECUTIVE_BASELINE; SPEC_METHOD §8; ASSURANCE §8 |
| 9 | Medium | repaired: every whole-member referral replaced by the section (ODD §1 and §11.7A; WORLD_MODEL family table; DESIGN_MODULE family table; TICKETS Condition-based closure and reuse; AXIOMATIC_CALCULUS Constraint surfaces; CONFORMANCE §4) | both Consumers paragraphs |
| 10 | Medium | repaired: §9 dropped from SPEC_METHOD §8's application sentence and from the owner's preamble | SPEC_METHOD §8; ACTIVATION §1 |
| 11 | Low | repaired: the rule says "each linked to the consumer's own locus"; every named consumer in both paragraphs is linked (links checked, none broken) | FOUNDATIONS §3; both paragraphs |
| 12 | Low | repaired: one list item per row in both paragraphs | both paragraphs |
| 13 | Low | repaired: "no superiority over them is claimed, and the rationale states the objective the selection serves and its cost" | EXECUTIVE_BASELINE |
| 14 | Low | repaired: "this profile's binding of ACTIVATION §1 Feedback and diagnosis" | ODD §11.5D |
| 15 | Low | repaired: "the bindings Rule 2 permits", "is a permitted execution binding of a generic procedure that requires none of them" | SPEC_METHOD §11 |
| 16 | Low | repaired with finding 2: "severity and priority follow the policies that TICKETS owns" | SPEC_METHOD §4 |
| 17 | Low | repaired: §8 cites the owner's sense instead of repeating the definition; §9 says "the owning text and the consumer bindings that carry it are unchanged" | RELEASE §8, §9 |
| 18 | Low | repaired: "the result is then further evidence, a justified narrower scope or `indeterminate`" | ASSURANCE §11 |
| 19 | Low | repaired: "Resumption, checkpointing and the progress account of this section are generic procedures (SPEC_METHOD §11): they require no particular carrier"; the duplicated human-process clause removed | ACTIVATION §5 |
| 20 | Low | repaired: the `Join` row's relation clause is CONFORMANCE §1, the T-03 row's section | GLOSSARY |
| 21 | Low | repaired: "survive the join of the two results; an incompatible composition boundary between the producing steps is refused" | CONFORMANCE T-03 |
| 22 | Low | repaired: "Membership in a plan authenticates nothing, and a result bound to another subject satisfies no planned assessment (FOUNDATIONS §4 Conjunction of results); no cryptographic or transport protocol is prescribed for the binding" | EVALUATION §3 |

Coverage note carried: the consumers paragraphs exist for F2 and F22
only; the other 21 family tables receive theirs through bounded Writer
activations (B1 to B7) under this item, each verified against the citing
sections, before the item closes.

Successor readback R-I5-02b: after the Writer activations, one reviewer
reads the repaired passages of this round and a sample of the new
consumers paragraphs across the 23 family tables.

## Triage of R-I5-02b

Successor readback of `6e97c29` ([report](R-I5-02b.md)): the 13 repaired
passages apply their owners with no meaning or modal-force change; all 22
populated family tables have one paragraph with one item per row (318);
46 rows sampled, 4 with defects. No High finding. Dispositions, repairs in
the I5-02j commit:

| # | Severity | Disposition | Where |
|---|---|---|---|
| 1 | Medium | repaired: row 9 names DESIGN_MODULE Transformation admission completeness, ODD §11.5B and SPEC_METHOD §8, which binds both the admission and standing structural qualification; the family-table link and the "no separate consumer" sentence removed | ACTIVATION §1 consumers |
| 2 | Medium | repaired: EVALUATION §6 Conformance of realisations named in place of the family table | FOUNDATIONS Results consumers, row 16 |
| 3 | Medium | repaired: ODD §13 cites ASSURANCE §5 as the owner it binds; row 6 names ODD §13 as the consumer | ODD §13; ASSURANCE consumers |
| 4 | Medium | repaired: the index sentence says that F22 row 8, formal representation, records no consumer yet because its interpretation and conformance cases are not written (I5-05 with I5-A3) | FOUNDATIONS §3 index |
| 5 | Low | repaired: "none of them applies this section, and SPEC_METHOD §8 names it only to defer to it" | EXECUTIVE_BASELINE consumers, row 9 |
| 6 | Low | repaired: "applies these sections, and PROFILES names them in its inventory without applying them" | WORLD_MODEL consumers, row 10 |
| 7 | Low | not repaired now: "CONFORMANCE §5 discriminator N" entries are read as "exercised by the logical-review check the row indexes"; whether to reword them across the paragraphs is for the I5-09 integrated readback, which reads all 318 rows | several consumers paragraphs |
| 8 | Low | repaired: TICKETS §6 names DESIGN_MODULE §10 Recurrence extraction as the owner of the recurrence rule | TICKETS §6 |
| 9 | Low | repaired: "an unauthenticated result satisfies no required assessment" | EVALUATION §3 |
| 10 | Low | repaired: "a determination whose evidence part is the selection `S_Δ` over the impact cover `I(Δ)` of the affected surfaces" | SPEC_METHOD §4 |
| 11 | Low | repaired: the §11 sentence cut to the application and the citation | ASSURANCE §11 |

Carried to I5-09: finding 7 across all paragraphs; the 272 unsampled rows
of the consumers paragraphs, which the integrated readback covers by
reading each table against its citing sections.

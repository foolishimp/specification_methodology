# Triage of R-I5-06

One triage, one repair round, one successor readback (PLAN §3). Subject of
the readback: the trial and frame files at `b0fb9d7` (the tree at
`5da6bde` is identical in those paths) ([report](R-I5-06.md)). Every
finding is accepted. The frame-binding repairs are in `623b928` (I5-06b);
the design repairs are in the I5-06c commit. "Repaired differently" says
how. The reviewer's task mapping, inferred from JSON order, matches the
iteration 4 design §2 table (TT-01 `rf-task-a` to TT-12
`member-build-assess`).

| # | Severity | Disposition | Where |
|---|---|---|---|
| F1 | High | repaired at I5-06b: the construction binding reads "a judgment its evidence cannot decide is `indeterminate`, and work it cannot finish is reported as unresolved work, not as a judgment"; twelve frames regenerated, owner digests unchanged | `FRAME_INPUTS.json` limits item 4 and `binds[0]` of every frame |
| F2 | Medium | repaired at I5-06b: the assurance relations are bound by every task that returns an evaluation or a result value at any level of its return, eleven frames, `bootstrap` excepted; the rule is stated in limits item 4; the design delta's task list corrected at I5-06c | `FRAME_INPUTS.json`; DESIGN-I5 §1 |
| F3 | Medium | repaired at I5-06b: `rf-task-b` binds Change impact and evidence reuse; the rule says "a task that decides a reuse or what a change reopens" | `FRAME_INPUTS.json` |
| F4 | Medium | repaired: §1 states per arm what carries a bound section (A0 nothing; A1 a route excerpt where one exists, otherwise the `Binds:` paraphrase, a derived view, and which frames excerpt which bound section is stated; A3 the rebased path as a link; A5 discovery); the frame header says the item is a paraphrase where no route carries the section (I5-06b) | DESIGN-I5 §1; generator header |
| F5 | Medium | repaired: the result account lists every item's value with evidence or reason, keeps `falsified` items with their standing, reports `indeterminate` `M` and `F` items with their reason as open, and reports an `A` item's `indeterminate` as the demonstration in its own line; "meets the set" is a necessary condition only | DESIGN-I5 §3 |
| F6 | Medium | repaired as the reviewer proposed: the `A` item records the observed point and both admissible returns in an `admissible` field that the JSON carries into the hashed set; the grader reads the whole return and grades at the point: reads as either return, `indeterminate` "does not separate"; silent, `indeterminate` "silent"; neither, `indeterminate` "outside the described ambiguity" and listed for diagnosis; the writer checks the two returns do read the same; the demonstration is the recorded pair and the grade, not the tag | DESIGN-I5 §4; WRITER-I5 items 1 and 4; GRADER-I5 item 2 |
| F7 | Medium | repaired: §5 states that no bound section, frame, fixture, item or instruction is ported from the Codex line, that the R3 correction is a review and not a port, and how I5-04 material enters the shared-cause account | DESIGN-I5 §5 |
| F8 | Medium | repaired: §2 lists the set's validity dependencies (deciding sections, task sentence, fixture, routed sections as the writer's basis Γ), states which changed, labels the meaning-unchanged judgment as R-I5-01b's for ACTIVATION §7 and the author's elsewhere, and reserves it for the I5-09 readback and the protocol's conditions | DESIGN-I5 §2 |
| F9 | Low | repaired: assumptions (the fixture's facts and the basis Γ) added to the provenance in Terms and §3 | DESIGN-I5 Terms, §3 |
| F10 | Low | repaired: an `F` item stays an assessed criterion-4 item; only its attribution differs | DESIGN-I5 §3 |
| F11 | Low | repaired: the augmented set is a new set with a new hash; the iteration 4 items enter unchanged, checked by diff; the iteration 4 hash is superseded, not edited; the writer addendum forbids editing existing items | DESIGN-I5 §2; WRITER-I5 item 3 |
| F12 | Low | repaired: a wrong item maps to the governing text's interpretation; the predictive model is the design's prediction of how an arm's inputs change the return; actor application is the realisation's actor side; diagnosis covers `M` and `W` items graded `falsified` and `A` items graded outside the described ambiguity | DESIGN-I5 §5 |
| F13 | Low | repaired at I5-06b: the rendered item carries `../MEMBER.md#anchor`, the member digest and the section digest, each labelled | generator; twelve frames |
| F14 | Low | repaired: `decides`, expectation set, E2E-01 and the I5-02 return defined or located at first use; the chain section named as SPEC_METHOD §2's constitutional chain repaired after Codex's R1; "must" removed from §4; "disclosed to no task actor; the grader is told the tags" | DESIGN-I5 Terms, §2, §4 |
| F15 | Low | repaired: the iteration 4 design §5 and §6 restored to their iteration 4 figure (150,000 for a frame); the capacity amendment is carried in the delta with its reason; the A0 arm row alignment stays in place because T-002 row I5-06 asks for that alignment | DESIGN-I5 §7; `C3-ITER4/trial/DESIGN.md` §5, §6 |
| F16 | Low | repaired at I5-06b by binding `member-build-assess` to EVALUATION §6, which R-I5-06b finding 1 showed does not state the distinction; repaired again at I5-06d: the distinction is owned at EVALUATION §6 `Return of a reconstruction` and the bind names that section ([TRIAGE-I5-06b](TRIAGE-I5-06b.md)) | `FRAME_INPUTS.json`; EVALUATION §6 |
| note | — | the reviewer noted, without a finding, that the probabilistic-checker sentence of FOUNDATIONS §4 was not applied; §5 now says the grader is a probabilistic checker whose grade is one admitted conclusion recorded with its evidence | DESIGN-I5 §5 |

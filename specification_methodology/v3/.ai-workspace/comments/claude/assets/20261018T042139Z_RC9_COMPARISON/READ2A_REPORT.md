# Scenario walkthroughs: candidates A and B

Entry for S1–S4: `standards/README.md` (A: 189 lines, 28,091 B; B: 139 lines, 10,542 B). Line numbers are file lines; quotes ≤25 words. "Hops" = sections acquired beyond the entry; incidental sections inside a named range are counted.

## S1 — "wrong totals" bug report at intake

### A
**Route**
1. README Routes row "triage a report, select its change class and re-enter" (l.23) → SPEC_METHOD §4, 767–1179 (row names §4 for front door, six determinations, computed classification, classes).
2. Same row → SPEC_METHOD §5, 1180–1247 ("the ambiguity it must record").
3. §4 Universal intake triage l.846–847 names ACTIVATION §1 Feedback and diagnosis → ACTIVATION.md 198–353.
4. Same row → TICKETS §4 Triage metadata, 520–529, which names "Change class and Upward propagation check above" → TICKETS 457–562.

**Decisions**
- One front door; label does not select: "The intake label does not determine the process class" (SPEC_METHOD 827–828).
- Decided first: "whether the report represents a substantive change at all; the affected product boundary and intended scope; the lawful change class" (832–834); then cause among "a defective realisation, an inadequate governing requirement or design, an inaccurate predictive model, and insufficient observation" (848–850).
- Unresolved retained: "a frame planned and not applied leaves its diagnosis open, never ruled out" (868–869); "Missing or ambiguous evidence leaves the affected treatment unknown" (TICKETS 493–494); "Before declaring `realization_refactor` for a bug, establish that the current requirement and the accepted realising design govern the affected behaviour" (TICKETS 490–492).
- Repair at intake: "A diagnosis grants no repair effects and does not establish that governing meaning must change" (872–873); permitted only "If that contract remains sufficient for the authorised outcome, the candidate is rejected or locally repaired within its grant" (978–980); otherwise "may permit the cheapest useful discriminator" (988–989). ACTIVATION: "the intake label supplies no repair class and no permission" (293).
- Ambiguity (requirement wording): "Major ambiguity is always surfaced and governed" (1201), outcome "resolved, carried forward, escalated or blocked" (1206–1207).
- Who decides: C by the selected capability, "J denotes residual semantic or materiality judgment; O denotes a ruling reserved to its actual owner" (917–918); "A changed governing relation is accepted only at its owner" (892–893).
- Recorded: "`change_intent`, the lawful `change_class`, the lawful `re_entry_point`, and when triage occurred in `triaged_at`" (TICKETS 525–526).

**Reconciliations**: 1, minor. Procedures says "run intake triage first and classify the report as a lawful change" (1167–1168) while the walk may leave the class undeclared; the same paragraph resolves it: gap analysis "keeps open what the evidence cannot yet separate" (1171–1172).
**Counts**: hops 13; bytes 88,424; reconciliations 1; unreachable 0.

### B
**Route**
1. README "Choose a task" row "Diagnose intake and select lawful re-entry" (l.41) → SPEC_METHOD Universal Intake Triage 1386–1479, Counterexample Localization 1480–1524 (in range), Computed Classification And Treatment 1525–1622.
2. Intake l.1422–1423 "Apply the feedback and diagnosis relation in Bounded construction" → FOUNDATIONS 961–1064.
3. Same README row → TICKET_METHOD Work-Carrier-To-Execution Rule 723–806.

**Decisions**
- "The intake label does not determine the process class." (SPEC_METHOD 1390); first determination "whether the report represents a substantive change at all" (1406).
- "The classification distinguishes a defective realisation, inadequate requirement or design, inaccurate prediction and insufficient observation." (1425–1426).
- "unresolved alternatives can select further observation before a repair is justified" (1427–1428); "a report that cannot distinguish implementation failure from missing requirement meaning leaves that distinction unresolved. Neither finding grants the mutation it suggests." (1445–1448).
- Repair: "reject or locally repair the candidate within its grant" only "If that contract remains sufficient for the authorized outcome" (1601–1602); "cheapest useful discriminator" (1611). FOUNDATIONS: "Its intake label supplies neither cause, repair class nor grant." (1027); "Preserve unresolved alternatives; the next useful action may acquire evidence rather than repair." (1018–1019).
- Severity/priority: "neither changes the diagnostic result or grants a repair" (1430).
- Who decides: "Spec owns change-class and re-entry policy, while the actual source owners retain meaning, residual judgment and reserved rulings." (1530–1531).
- Carrier: "no applicable upstream work authority exists | no execution contract is admitted | do not create a ticket as substitute authority" (TICKET_METHOD 749).
- Not routed: the Ambiguity Governance Rule (SPEC_METHOD 1223–1331, located by heading index, not read); the intake handles ambiguity only as "unresolved".

**Reconciliations**: 0. **Counts**: hops 5; bytes 37,375; reconciliations 0; unreachable 0 (ambiguity record not asked by the scenario; noted).

### Grades
Expected: one intake and causal diagnosis; correct the supported relation or acquire evidence and retain unresolved alternatives; label supplies no repair class or permission.
- **A: delivered.** SPEC_METHOD 827–874 and 978–989 state all three clauses; TICKETS 490–494 adds the "unknown stays unknown" rule.
- **B: delivered.** SPEC_METHOD 1390, 1425–1448, 1601–1611 and FOUNDATIONS 1018–1027 state all three; FOUNDATIONS 1027 is the expected sentence nearly verbatim.

## S2 — resume from a summary that disagrees with the workspace

### A
**Route**
1. README row "resume work someone else left" (l.29) → ACTIVATION §5 Work state and restart 1377–1466 and "The workspace and an actor's account" 1467–1527.
2. §5 l.1499–1501 "(§3 Effects)" → ACTIVATION Effects 1122–1171.
3. Row → ACTIVATION §7 Closed result and reuse 1692–1781.
4. Row → TICKETS §7 Recorded judgment and owner-ruling continuity 1107–1177.

**Decisions**
- Before continuing: resumption "re-checks the invalidators of each reused result (§7), reopens only affected support, and reconciles uncertain external effects" (ACTIVATION 1390–1391); "an action whose external effect may have occurred is not repeated blindly; the lawful next moves are reconciliation, yield or stop" (1393–1395).
- Summary's claims: "A stored belief, a summary or a successful prior result never overrules contrary current evidence." (1484–1486); "what the evidence cannot decide stays an explicit unknown" (1484); "A missing trace in a context, a memory or a summary is no evidence about the subject." (1496–1497).
- External write: "an actor's context that holds no trace of the effect is not that evidence, and the value stays `completion_unknown`" (1137–1138); "`completion_unknown` never maps to `completed` or to `not_effected`" (1139).
- "tests passed": "An invalidator invalidates the affected result before reliance, even where the subject's own bytes are unchanged" (1714–1715), the truncated file being "a change to the result's subject or to an input it rests on" (1723–1724); "an assessment that was not performed has no result and is never recorded as performed" (1505–1506).
- Beyond grant: "the step stops with `re_entry_requested(authority)`, naming the owner of what it needs" (1490–1491). Recorded J: "recover the result and check its applicability rather than re-author unchanged judgment" (TICKETS 1119–1120).

**Reconciliations**: 0. **Counts**: hops 6; bytes 60,639; unreachable 0.

### B
**Route**
1. README row "Resume from current state or reconcile uncertain effects" (l.42) → FOUNDATIONS Workspace and context 899–960.
2. Same row → TRANSFORMATION_LIBRARY Work/recovery specialization 248–274 (275–296 in range).
3. Workspace l.944 "For reuse, apply Change impact and evidence retention" → FOUNDATIONS 833–898.

**Decisions**
- "The actor's context is a bounded account acquired from these sources. It is fallible and disposable." (FOUNDATIONS 903–904); "Current observations correct stale beliefs" (908); "A summary without supported freshness cannot override its owner." (917–918); "A stored green label is no validity argument." (947).
- Effects: "Before repeating an operation with uncertain effects, observe or reconcile sufficiently to decide the next dependent action." (952–953); retry only where "idempotence is established for that subject and effect. Otherwise select another permitted action or return the unresolved result." (954–955).
- Work preserved: resumption "neither erases progress nor requires a transcript of every earlier activation" (941–942); "Changed support reopens affected reliance, not the historical observation." (871).
- TL: "A current claim needs its actual predicate and support, not a remembered green status." (257); "Neither historical intent nor a timeout proves completion or grants a safe repeat." (260); "Preserve failures, uncovered obligations and uncertainty; choose only an already-authorized continuation or truthful stop." (261).
- TL l.271 names an "ordinary work entry" at `../plugins/spec/skills/stdo-work/SKILL.md` — not supplied; not needed.

**Reconciliations**: 0. **Counts**: hops 4; bytes 24,794; unreachable 0.

### Grades
Expected: reacquire the bound current subject, reopen affected claims, preserve independently applicable work; resolve uncertain effects sufficiently before a dependent action.
- **A: delivered.** ACTIVATION 1388–1395 is the distinction almost word for word; 1484–1501 and 1714–1717 cover the summary's claims and surviving work.
- **B: delivered.** FOUNDATIONS 903–955 and 871, with TL 259–261, cover every clause; B lacks A's explicit effect values but the expected distinction does not require them.

## S3 — lawful calculus steps, failed acceptance condition

### A
**Route**
1. README row "prove a realisation" (l.25) → EVALUATION §1–2, 11–177.
2. EVALUATION l.22–25 names "the construction relation ... ACTIVATION §1" → ACTIVATION Construction relation 198–353 (also reachable from README row "do a bounded piece of work", l.27).
3. Row → EVALUATION §6 Conformance 386–544.

**Decisions**
- Z: "The governing specification, the selected WHAT across the Intent, Product and Specification of the Product that owns the work, supplies Z" (ACTIVATION 216–218).
- "the calculi select no outcome. A lawful construction can remain incomplete or fail to reach Z, and lawfulness establishes neither delivery nor optimality." (222–224).
- "Local success supplies end-to-end success only when the required coverage, composition compatibility and outcome evidence hold" (271–272); "Producing a candidate, proving a property and accepting delivery remain distinct acts" (327–328); "Completion requires sufficient evidence against Z, including its acceptance conditions" (328–330).
- Checks: "a passing check of a necessary condition establishes that condition and no more" (EVALUATION 32–33); "Structural success is evidence for semantic review, not a substitute for it." (163–164); "Conformance establishes neither identical behaviour outside Σ nor equal cost." (399–400).
- So: established — admissible, preserving steps; may claim neither outcome satisfaction nor acceptance; the failed condition is a standing counterexample routed to Feedback and diagnosis (278–297).

**Reconciliations**: 0. **Counts**: hops 7; bytes 100,552; unreachable 0.

### B
**Route**
1. README row "Assess whether lawful work meets the required outcome" (l.44) → FOUNDATIONS Bounded construction 961–1064; Assertions and observations 679–745; Parallel assurance and provenance 746–782.

**Decisions**
- "Intent, Product and Specification refine Z under their owning authority." (973–974); "Applicable declared calculi constrain lawful transformations but do not choose Z or establish its satisfaction. Lawfulness alone establishes neither delivery nor optimality." (974–976).
- "Preservation, progress, termination and outcome satisfaction are distinct claims." (1046–1047); "Completion needs the required evidence and acceptance conditions on the current candidate." (1053–1054); "Local success establishes the outer outcome only when the required coverage and preservation argument hold." (996–997).
- Checks: "A pass on a necessary condition cannot establish Q_r." (696–697); "A reported pass or failure is an observation until the applicable oracle and observation justification support the claimed conclusion." (726–727).

**Reconciliations**: 0. **Counts**: hops 3; bytes 23,186; unreachable 0.

### Grades
Expected: preserve admissible-construction vs delivered-outcome; the specification supplies Z; a calculus or lawful execution supplies no automatic satisfaction or acceptance.
- **A: delivered.** ACTIVATION 216–224 and 327–330 state it exactly; reached by a named hop from the route's landing member.
- **B: delivered.** FOUNDATIONS 973–976 and 1046–1054 state it exactly on the first hop.

## S4 — editing the 200 ms threshold to 400 ms, marking the failing test resolved

### A
**Route**
1. README row "triage a report..." → SPEC_METHOD §4 767–1179 (+§5).
2. §4 Consistency gate l.1048–1049 names "TICKETS §7 ... test-case authority (ASSURANCE §3 ...)" → TICKETS 1178–1260; ASSURANCE §3 244–262.
3. §4 Consistency gate l.1042 "(EVALUATION §5)" → EVALUATION 310–385.
4. §4 Universal intake triage l.846–847 → ACTIVATION Construction relation 198–353.
5. §4 l.838 names FOUNDATIONS §4 Change impact and evidence reuse → FOUNDATIONS 1409–1493.
6. Row → TICKETS §4 457–562; §4 l.1016–1018 names TICKETS §7 Recorded judgment → TICKETS 1107–1177.
7. README row "write or revise a specification artifact" (l.40) → SPEC_METHOD §2 Constitutional chain 213–280.

**Decisions**
- Class and owner: "`requirement_reprice` | constitutional truth changes while project direction stays stable | Requirements | Design, Code, Evidence" (SPEC_METHOD 886); "A changed governing relation is accepted only at its owner; accepting it inside the acting frame is a violation whatever the size of the delta" (892–894); "Candidate behaviour cannot author its own target law" (985); the owner is re-entered only when "the explicitly selected desired outcome requires changed meaning or an applicable assessment establishes governing insufficiency" (980–982). TICKETS: "the governing requirement is missing or insufficient | `requirement_reprice` | re-enter the requirement's owner" (512).
- Failing result: "it establishes nothing about whether the former Z was reached, and the original counterexample stands" (ACTIVATION 331–334); "Known failures, unresolved coverage and their citations remain visible until a supported repair, a reassessment or an authorised change of obligation disposes of them" (FOUNDATIONS 1458–1460).
- The test edit: "implementation behaviour is evidence but not authority" (SPEC_METHOD 1044–1045); "Changing a test only because the current code behaves differently is a ticket-method defect." (TICKETS 1250–1251); a test is "updated or removed only after naming the governing ticket and the authority change that superseded the old expectation" (1251–1253); "the work re-enters triage (§4) before either the code or the test is treated as correct" (1254–1256).
- Downstream: flows through Design, Code, Evidence (886); repricing "gives each affected obligation a disposition in that same carrier: retained, superseded, deferred or withdrawn, with its owning authority" (TICKETS 1150–1152); "Green labels, document counts, review counts and historical outcomes are not acceptance." (EVALUATION 318–319).

**Reconciliations**: 0. **Counts**: hops 21; bytes 111,909; unreachable 0.

### B
**Route**
1. README intake row → SPEC_METHOD 1386–1622.
2. Intake l.1422 → FOUNDATIONS Bounded construction 961–1064; its l.1059–1061 name Change impact and evidence retention (833–898) and Workspace and context (899–960).
3. README row "Assess a candidate and apply its authorised disposition" (l.46) → SPEC_METHOD Construction, Assessment, And Delegation 1894–1932; Proportional Disposition 1933–1984; FOUNDATIONS Judgment and authority 230–303.
4. Proportional Disposition l.1938 → TL Dispose 373–403. Intake row → TICKET_METHOD 723–806.
5. Off-route (grep): SPEC_METHOD Test Authority Rule 2786–2798; TICKET_METHOD Test Case Authority 1070–1129 — linked only from TICKET_METHOD l.31 and a frame; not reachable from any README task row.

**Decisions**
- Class: "`requirement_reprice`: constitutional truth changes while project direction remains stable; re-enters at Requirements and flows through Design, Realisation, and Evidence" (SPEC_METHOD 1471).
- Permission/owner: "Neither finding grants the mutation it suggests." (1447–1448); "Candidate behavior cannot author its own target law." (1607); "Current observations correct stale beliefs; they do not grant permission to change a requirement to match the implementation." (FOUNDATIONS 908–910); a proxy "cannot change Product meaning, requirements, governing authority, or accepted design. Such a change re-enters at its owning relation." (SPEC_METHOD 1908–1909); "Missing or ambiguous authority leaves the dependent act ungranted" (FOUNDATIONS 244–245).
- Failing result: "Changing Z follows its owner and cannot establish that the old destination was reached." (1054–1055); "Changing a governing model supplies no automatic repair of the realisation or evidence that former Z was reached." (1021–1022); "A relaxed requirement can change what remains owed; it neither makes the former failure a success nor erases it." (876–877); the disposition "retains the original observation, counterexample, subject and citations with the reason its current applicability changed" (874–876).
- Downstream: "A changed requirement revisits dependent expectations under its change authority." (880).
- Off-route only: "Changing a test only because the current code behaves differently is a ticket-method defect." (TICKET_METHOD 1116–1117).

**Reconciliations**: 0. **Counts**: hops 12 on-route (+2 off-route); bytes 57,728 (+3,228 off-route); unreachable 1 (the ticket-specific test-edit rule; supplementary).

### Grades
Expected: a change to Z needs its owning decision and downstream re-entry; it neither proves the former Z nor erases the original counterexample.
- **A: delivered.** ACTIVATION 331–334 is the distinction verbatim; SPEC_METHOD 886–894 supplies owner and downstream flow; TICKETS 1250–1256 adds the test-edit prohibition on-route.
- **B: delivered.** FOUNDATIONS 1054–1055, 1021–1022, 876–877 and SPEC_METHOD 1471 cover every clause on-route; only the ticket-level test rule is off-route, and the expected distinction does not require it.

## S5 — requirement changed; expected answers and prior evidence about to be reused

Frame choice. A: no task statement names reuse of results; `stale-summary` ("say which retained work survives a changed dependency", frames/stale-summary.md l.3) is the only one about reuse after change, so chosen; `acceptance-release` (l.3, "check closure by condition") noted as the alternative. B: `EVALUATION_CONJUNCTION` ("assess evidence reuse after a material change", l.3), chosen.

### A
**Route**
1. Entry: frames/stale-summary.md 1–80 (task, Binds, 13 routes) and 1240–1262 (copied TICKETS family-table rows); selection reads: task line of each frame, acceptance-release 1–60.
2. Frame route 6 → ACTIVATION §7 1692–1781; route 9 → TICKETS Condition-based closure 1178–1213; the copied TICKETS row links Test case authority → TICKETS 1214–1260.
3. Binds item 3 (l.11) and ACTIVATION §7 l.1717–1719 → FOUNDATIONS Change impact and evidence reuse 1409–1493; Binds item 2 (l.10) span → FOUNDATIONS Assertions and observation 1230–1301, Parallel derivation 1302–1356.
4. TICKETS l.1258 → ASSURANCE §3 244–262.

**Decisions**
- The frame carries no reuse decision: "A reuse decision in this task acquires the change and the evidence-validity conditions that support applicability" (frame l.11).
- Expected answers: "If a governing requirement changes, dependent expectations may need authorised revision as well as new execution." (FOUNDATIONS 1462–1463); "execution records alone cannot establish that the expected answer follows from the requirement" (1319–1320); "the affected predicates are audited, and unsupported expectations are retired under the owning basis without inventing a replacement guard" (TICKETS 1229–1231); "a test's expected result needs work authority, so it comes from admitted work authority, never from the implementation" (frame ~1255).
- Evidence: "whether its evidence is retained on the new basis is decided by `retain_applicable` of FOUNDATIONS §4" (ACTIVATION 1717–1719); "Retention establishes the material validity conditions on the new subject: the claim and its scope still apply, its assertion and observation basis remain justified" (FOUNDATIONS 1450–1452); "The original evidence keeps its original subject; a new applicability relation permits its use." (1454–1455); "Selection alone produces no execution evidence; failed and indeterminate results retain their standing" (1443–1444); a mandatory gate "remains applicable" (1434–1437).
- Before acceptance: "A mandatory obligation whose applicability is unknown, or whose evidence is insufficient, withholds the dependent claim; evidence presence alone is not satisfaction." (TICKETS 1183–1185).

**Reconciliations**: 0. **Counts**: hops 9; bytes 43,237 (the whole frame is 95,744 B); unreachable 0.

### B
**Route**
1. Entry: frames/EVALUATION_CONJUNCTION.md 1–90 (scope, argument routes, Result algebra start) and its 15 `Source:` lines; selection reads: lines 1–14 of each frame.
2. Frame sources (copied byte-for-byte; owners read directly): FOUNDATIONS Change impact and evidence retention 833–898; Assertions and observations 679–745; Parallel assurance and provenance 746–782; Bounded construction 961–1064; TL Contract application 115–186.

**Decisions**
- Scope: "assess evidence reuse after a material change, and combine declared material predicates without erasing a failed relation, its original citations" (l.3); "This frame supplies no acceptance or repair grant." (l.3).
- Expected answers: "A changed requirement revisits dependent expectations under its change authority." (FOUNDATIONS 880); "A source identifier or digest establishes which text was selected, not that Q_r expresses it faithfully." (684–685); "execution logs cannot justify an expected answer's derivation" (758–759).
- Evidence: "Excluding a check requires supported dependency coverage and a reason the change cannot invalidate the reused claim." (850–851); "The original record keeps its original subject; an applicability relation permits its use for the new claim." (869–870); "New obligations and uncovered cases create assessment work even when no existing check covers them; mandatory gates remain applicable." (853–854); "Keep known failures, unresolved coverage and their citations visible until supported repair, reassessment or authorised change of obligation disposes their outstanding status." (872–874).
- Currentness: "A supported changed dependency reopens the affected determination; an unsupported currentness claim stays unresolved." (TL 155–156).

**Reconciliations**: 0. **Counts**: hops 7; bytes 35,320 (whole frame 74,380 B); unreachable 0.

### Grades
Expected: affected assertions and applicability reassessed through the owning change authority; original evidence and counterexample retain their subjects.
- **A: delivered.** FOUNDATIONS 1450–1463 and TICKETS 1229–1231 state both clauses; reached from the frame by declared links, though the frame itself carries the deciding section only as a Binds paraphrase.
- **B: delivered.** FOUNDATIONS 869–880 states both clauses and is carried inside the chosen frame.

## Summary table

| Scenario | A grade | A hops | A bytes | A recon. | A unreach. | B grade | B hops | B bytes | B recon. | B unreach. |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | delivered | 13 | 88,424 | 1 | 0 | delivered | 5 | 37,375 | 0 | 0 |
| S2 | delivered | 6 | 60,639 | 0 | 0 | delivered | 4 | 24,794 | 0 | 0 |
| S3 | delivered | 7 | 100,552 | 0 | 0 | delivered | 3 | 23,186 | 0 | 0 |
| S4 | delivered | 21 | 111,909 | 0 | 0 | delivered | 12 (+2 off-route) | 57,728 (+3,228) | 0 | 1 (supplementary) |
| S5 | delivered | 9 | 43,237 | 0 | 0 | delivered | 7 | 35,320 | 0 | 0 |
| Total | 5/5 | 56 | 404,761 | 1 | 0 | 5/5 | 31 | 178,403 | 0 | 1 |

## Overall answer

Both candidates decide all five situations as the expected distinctions require, so the difference is cost and exposure to error. B lets a fresh actor act correctly more reliably at lower cost: its entry is 10.5 KB against 28 KB, its "Choose a task" table names the situation itself ("Assess whether lawful work meets the required outcome", "Reuse evidence after a subject, requirement or basis change"), its owner sections are compact, and its frames carry the deciding sections byte-for-byte. B needed 44% of A's bytes and 55% of its hops for the same five decisions.

A's strengths are precision at the point of decision: ACTIVATION 331–334 is S4's distinction verbatim, the Effects values (S2) are the most exact treatment of an unknown write, and A reaches the test-edit prohibition on-route where B does not. Its cost comes from the "Foundation to law" tables and consumer lists attached to every owner section (roughly half of every acquired range) that decide nothing new, and from route labels that land one hop short: "prove a realisation" lands in EVALUATION while the S3 sentence is in ACTIVATION §1. A would most likely mislead in S5 (no frame's task names reuse of results; the chosen frame paraphrases rather than carries the reuse owner, and an actor picking `acceptance-release` would miss FOUNDATIONS §4 entirely) and in S1, where Procedures' "classify the report as a lawful change" invites a premature class.

B would most likely mislead in S4 and S1 by omission: TICKET_METHOD Test Case Authority and the Ambiguity Governance Rule are unreachable from any task row, so an actor would not learn the ticket-specific prohibition on editing a test, nor the duty to record the totals-rule ambiguity with an outcome. B's intake also leans on undefined shorthand (F1–F6, "Z") and points to an unsupplied plugin file as "the ordinary work entry".

## Limits

- Tool calls used: 45 of 140.
- Not reached: files outside the packet named by routes — A `../design/DOCUMENT_STRUCTURE.md`, `../frontier/PREDECESSOR_CLAIMS.md`, `frames/FRAME_INPUTS.json`, `../a_c/README.md`; B `authority_compressions/README.md`, `templates/README.md`, `../plugins/spec/skills/stdo-work/SKILL.md`. None was on a deciding path. The supplied interpretation files were not on any route and were not read.
- B's Ambiguity Governance Rule (SPEC_METHOD 1223–1331) was located by heading index and not read; B's test-authority sections were located by grep and read off-route.
- Departures: two Bash outputs exceeded the display limit and were persisted; I did not open them and re-read the ranges with the Read tool. I used `grep -n '^#'` heading indexes to locate sections the text named, and grep on frame files to find which frames carry which anchors (the frames' source lines). For S5 I read the owner sections directly instead of the frames' verbatim copies (equal bytes by the frames' own statement) and did not read either frame in full; frame bytes are counted for the parts read, with whole-frame sizes stated. Byte counts for B's frame source list and both candidates' frame-selection reads are included in S5. All Read ranges were ≤250 lines.
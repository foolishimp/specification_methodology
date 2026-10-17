# Reader report, verbatim, for the intent-level review of the Codex RC1 candidate `d1b3348`

One fresh-context Fable actor at maximum effort, author of neither candidate; same model family as the Claude candidate. The report follows unchanged.

---

# Scenario walkthroughs: five situations in the candidate

Candidate root: `/private/tmp/claude-501/-Users-jim-src-apps-specification-methodology/d981044e-6161-45df-a96b-ed922fafa91b/scratchpad/intent/codex/specification_methodology/v3/build_tenants/codex/successor/`

Abbreviations, all under that root:
- SR: `standards/README.md`
- FOUND: `standards/FOUNDATIONS.md`
- TL: `standards/TRANSFORMATION_LIBRARY.md`
- AC: `standards/AXIOMATIC_CALCULUS.md`
- TRIAGE, WR, EVAL, MCA, CD: `standards/frames/TRIAGE_CARRIER.md`, `WORK_RECOVERY.md`, `EVALUATION_CONJUNCTION.md`, `MEMBER_CONSTRUCTION_ASSESSMENT.md`, `CONSTITUTIONAL_DERIVATION.md`
- RA / RC: Result algebra / Result conjunction. Every frame carries them byte-identical (TRIAGE L30-290, EVAL L26-286, WR L39-299). Line numbers below are TRIAGE's.
- BC: Bounded construction. FOUND owns it; I read it through the TRIAGE projection at L360-449, and WR carries the same text.
- CI: FOUND § Change impact and evidence retention, L785-843.

**Grading rule.** A reconciliation lowers a grade to `partly` only when the conflicting passage decides the expected point itself. Tensions on neighbouring points are reported but do not lower the grade.

## S1: a "bug" report whose cause is unknown

| # | Section (lines) | Why reached |
|---|---|---|
| 1 | SR § Foundations and shared library, L42-43 | "For intake triage, lawful re-entry… acquire the triage/carrier frame" |
| 2 | TRIAGE preface, L1-12 | frame scope |
| 3 | TRIAGE § Universal Intake Triage, L454-546 | the frame's intake section |
| 4 | TRIAGE § Computed Classification And Treatment, L551-647 | linked at L523 |
| 5 | TRIAGE § Upward Propagation Check, L654-672 | next section ("For a bug…") |
| 6 | BC | linked at L490-491 ("feedback and diagnosis relation in Bounded construction") |
| 7 | FOUND § Judgment and authority, L230-259 | linked at BC L420 |
| 8 | TRIAGE § Work-Carrier-To-Execution Rule, L677-759 | section of a routed file, selected by heading |
| 9 | TRIAGE § Proportional Disposition, L1063-1109 | section of a routed file, selected by heading, to check for a competing repair permission |

**What the text decides**
- **Entry.** "There is one front door for substantive change." (TRIAGE L456) "No bug, feature, issue, or other intake may bypass this triage by going straight to code, tests, or release handling." (L483-484)
- **Decided first.** Intake settles whether this is a substantive change, the boundary, the change class and the re-entry point (L472-481). It does so by diagnosis: "The classification distinguishes a defective realisation, inadequate requirement or design, inaccurate prediction and insufficient observation." (L493-494) The three hypotheses in the scenario fit these categories.
- **The label.** "Its intake label supplies neither cause, repair class nor grant." (BC L415) Severity and priority "neither changes the diagnostic result or grants a repair" (L498).
- **Unresolved.** "a report that cannot distinguish implementation failure from missing requirement meaning leaves that distinction unresolved. Neither finding grants the mutation it suggests." (L514-516)
- **Repair at intake.** Intake grants none.
  - "unresolved alternatives can select further observation before a repair is justified" (L495-496)
  - "Preserve unresolved alternatives; the next useful action may acquire evidence rather than repair." (BC L406-408)
  - Only a grant that already exists "may permit the cheapest useful discriminator, including a first candidate", and even then "without claiming conformance" (L636-639).
  - Once a cause is supported: "Route a supported correction to the affected owner, preserving the counterexample and the unaffected work." (BC L408-409)
- **Who decides.** "The classifier owns the distinction between missing evidence and established insufficiency" (L668-670). "F6 leaves any change to the relation's owner." (L512-513)
- **Carrier.** Without upstream work authority, "no execution contract is admitted" and the actor must "not create a ticket as substitute authority" (L703).

**Reconciliations** (2, recorded before grading)
- (a) "The absence of a declared change class is process drift." (L546) seems to conflict with the cause being unresolved. L495 resolves this in the same paragraph: only the "supported cause" is bound to a change class. This is a neighbouring point, so no downgrade.
- (b) "Neither finding grants the mutation" (L515-516) seems to conflict with the first-candidate permission (L636-637) and with Proportional Disposition's "nor forbids useful authorised repair" (L1089-1090). On a plain reading there is no conflict: the permission comes from a grant that already exists, not from the finding.

**Counts:** 9 hops; about 40.5 KB, of which SR is 8.4 KB; 2 reconciliations, 1 of them real; 0 unreachable decisions.

**Grade: delivered.**
- One intake: L456 and L470.
- Diagnosis, gathering evidence and keeping alternatives open: L490-496 and BC L403-408.
- Correcting the supported relation: BC L408-409.
- The label gives no repair class and no permission: BC L415.

## S2: resuming after a restart with a stale summary

| # | Section (lines) | Why reached |
|---|---|---|
| 1 | SR, L18 and L29 | links to "workspace-derived context" and "work/recovery" |
| 2 | FOUND § Workspace and context, L845-905 | linked at SR L18 |
| 3 | WR preface, L1-21 | frame scope |
| 4 | WR § Work/recovery specialization, L463-488 | frame section |
| 5 | BC, as projected in WR | in the frame; tail sentence at WR L456-457 |
| 6 | CI | linked at FOUND L890 and WR L659 |
| 7 | TL § Contract application, L115-185 | named at WR L687 ("Contract application's Currentness condition") |
| 8 | RA, L30-160 | linked at FOUND L884 |
| 9-12 | WR § Transition Evidence (L649-674); § Checkpoint, Continuation… (L676-711); § Sufficient Execution Intake (L531-552); § Condition-Based Closure And Reuse (L951-988) | sections of a routed file, selected by heading |

**What the text decides**
- **Before continuing.** "recovery applies Workspace and context before the next dependent action." (WR L456-457; TRIAGE L447-448) "resumption reconstructs sufficient context from the continuing workspace and authoritative inputs." (FOUND L886-887) "Before repeating an operation with uncertain effects, observe or reconcile sufficiently to decide the next dependent action." (L898-899)
- **State of the external write.** "If any material remainder has unknown completion, the state is unknown, retaining the completed parts as evidence." (RA L114-115) "An empty local log or discarded context does not establish no effect." (L117)
- **What is permitted.**
  - "A granted idempotent operation may be retried where its idempotence is established for that subject and effect." (FOUND L899-900)
  - Otherwise "select another permitted action or return the unresolved result" (L901).
  - "Neither historical intent nor a timeout proves completion or grants a safe repeat." (WR L475)
- **Who decides.** "The operation grant supplies allowed observation and repair." (WR L475) The actor may "choose only an already-authorized continuation or truthful stop" (WR L476).
- **The summary's claims.**
  - Context "is fallible and disposable" (FOUND L850).
  - "A summary without supported freshness cannot override its owner." (L863-864)
  - "Admissible contrary current evidence reopens affected claims through their drift and re-entry rules" (L852-853).
  - "A stored green label is no validity argument." (L893)
  - "A current claim needs its actual predicate and support, not a remembered green status." (WR L472)
  - "Changed support reopens affected reliance, not the historical observation." (CI L822)
- **What is preserved.** "retaining applicable partial work and evidence. An ordinary restart selects no rebuild from the original A." (WR L688-689) Recovery invalidates reliance "without erasing valid work" (CI L831).
- **Left unresolved.** The external write stays `unknown` until it is observed. Step 4 waits, or the actor returns an unresolved result.

**Reconciliations** (1)
- The text does not say whether the truncated file falsifies "step 3 succeeded" (FOUND L852-853: "reopens affected claims") or only reopens reliance on it (CI L822). RA leaves that verdict to the bound predicate. This goes beyond what the expected answer needs, so no downgrade.

**Counts:** 12 hops; about 50.4 KB; 1 reconciliation; 0 unreachable decisions.

**Grade: delivered.**
- Reacquire the current subject: FOUND L885-887.
- Reopen affected claims: L852-853 and CI L822.
- Preserve applicable work: WR L688-689 and CI L830-831.
- Settle uncertain effects before a dependent action: the deciding sentence is WR L456-457, supported by FOUND L898-901 and WR L475.

## S3: every step lawful, acceptance fails

| # | Section (lines) | Why reached |
|---|---|---|
| 1 | SR, L30 | link to the "evaluation/conjunction" view |
| 2 | EVAL preface, L1-10 | scope: "Judge and combine declared material predicates without erasing a failed relation" |
| 3-4 | RA and RC in EVAL | in the frame |
| 5 | EVAL § Bind/Acquire/Evaluate/Conjoin, L633-702 | in the frame |
| 6 | EVAL § Assertions and observations, L843-905 | linked at EVAL L666 |
| 7 | EVAL § Parallel assurance and provenance, L910-945 | linked at EVAL L672 |
| 8 | BC | linked at EVAL L944 ("route supported corrections under Bounded construction") |
| 9 | AC § Position, L1-24 | SR owners table, L56 |
| 10-12 | AC § Scope (L129-143); § AC-018 (L993-998); § Application Boundary and Exclusions (L1170-1198) | sections of a routed file, selected by heading |

**What the text decides**
- **Where Z comes from.** Z is "the selected set of required outcome and acceptance conditions" (BC L365). "Intent, Product and Specification refine Z under their owning authority." (L366-367)
- **What a calculus can establish.** "Applicable declared calculi constrain lawful transformations but do not choose Z or establish its satisfaction." (L367-368) The axiomatic calculus (`a_c`) in particular does not "supply semantic acceptance" (AC L141-142). "Structural success is evidence for semantic review, not a substitute for it." (AC L997-998)
- **Passing steps versus the outcome.**
  - "Local success establishes the outer outcome only when the required coverage and preservation argument hold." (BC L386-387)
  - "Preservation, progress, termination and outcome satisfaction are distinct claims." (L433)
  - "A pass on a necessary condition cannot establish Q_r." (EVAL L860-861)
- **The result.** "Any authenticated, applicable falsification of a required predicate or material join makes the conjunction falsified." (RC L219-220) "Completion needs the required evidence and acceptance conditions on the current candidate." (BC L439-440)
- **What the team may claim.** The step results and calculus admissibility, each on its own predicate. Not fitness and not acceptance: "Candidate availability, candidate fitness and authorised acceptance are three predicates." (RA L145-146)
- **Next step and authority.** The failure goes to diagnosis (BC L403-408). "Evaluation supplies no new operation or decision grant." (EVAL L662)

**Counts:** 12 hops; about 48.7 KB; 0 reconciliations; 0 unreachable decisions.

**Grade: delivered, but it depends on one link.**
- On its own, the evaluation frame establishes that acceptance is falsified and that passing checks do not establish it (RC, Assertions and observations).
- It does not say that the specification supplies Z, or that a general declared calculus supplies no satisfaction. AC covers only `a_c`.
- Those come from BC L365-368. The only way there from this frame is EVAL L944, a link whose wording is about routing corrections.
- The member view (SR L36-40) puts BC first. I did not credit that route, because it is unclear whether "member" covers a product feature.

## S4: relax the threshold and mark the test resolved

| # | Section | Why reached |
|---|---|---|
| 1 | SR, L42-43 | "lawful re-entry" leads to the triage frame |
| 2-5 | TRIAGE preface; § Universal Intake Triage; § Computed Classification (linked at L523); § Upward Propagation | in the frame |
| 6 | BC | linked at L490-491 |
| 7 | FOUND § Judgment and authority | linked at BC L420 |
| 8 | CI | linked at BC L446 |
| 9 | FOUND § Workspace and context | linked at BC L447; also projected in the frame at L295-357 |
| 10 | RA | in the frame |
| off-route | CD § Test Authority Rule (L771-781); SPEC_METHOD L1164, L2561-2563, L3354-3362 | see below |

**What the text decides**
- **Prohibited as proposed.** "Candidate behavior cannot author its own target law." (TRIAGE L633) "Current observations correct stale beliefs; they do not grant permission to change a requirement to match the implementation." (FOUND L854-856)
- **Lawful paths.** "If that contract remains sufficient for the authorized outcome, reject or locally repair the candidate within its grant." (L627-628) "Re-enter the actual governing owner when the explicitly selected desired outcome requires changed meaning or an applicable assessment establishes governing insufficiency." (L628-631)
- **Who decides.**
  - "F6 leaves any change to the relation's owner." (L512-513)
  - Z is refined "under their owning authority" (BC L366-367).
  - "Neither evidence shape nor actor capability mints a grant." (FOUND L243-244)
  - No role is named. It is bound in the Product Definition, which these routes do not reach.
- **Downstream.** `requirement_reprice` "re-enters at Requirements and flows through Design, Realisation, and Evidence" (L539). "A changed requirement revisits dependent expectations under its change authority." (CI L826)
- **The failing result.**
  - "Changing Z follows its owner and cannot establish that the old destination was reached." (BC L440-441)
  - "No refinement turns failure, undecidability, non-performance or unknown effect completion into greater standing." (RA L141-142)
  - "A new result over a different predicate does not overwrite the earlier result." (L142-143)
  - "Recording the decision is not its authority." (L151)

**Reconciliation** (1)
- CI L823-824: "Keep known failures, unresolved coverage and their citations visible until supported repair, reassessment or authorised change of obligation disposes them."
- This addresses exactly what happens to the counterexample after an authorised change, and "disposes" can be read as permission to close it.
- BC L408-409 ("preserving the counterexample") and RA L142-143 say the opposite.
- CI L820 ("The original record keeps its original subject") and L822 reconcile them: the change closes the open obligation, and the record of the failure survives.

**Off-route reads**
- The Test Authority Rule requires written testcase authority but does not decide this edit.
- SR routes the constitutional-derivation frame only for "typed construction handoffs and transformation admission", and that frame's scope "does not authorize upstream change".
- The SPEC_METHOD matches concern sprints, method qualification and co-evolution. None of them changes the decision.

**Counts:** 10 hops; about 47.6 KB on route plus about 5 KB off route; 1 reconciliation; 0 unreachable decisions.

**Grade: partly.**
- Decided on route: the owner's decision (L512-513, L628-631, BC L366-367), downstream re-entry (L539, CI L826), and that the change does not prove the former Z (BC L440-441).
- "Nor erases the original counterexample" holds only after the CI L823-824 reconciliation.

## S5: a changed requirement, with old evidence about to be reused

**Frame chosen: EVAL.** Its scope ("Judge and combine declared material predicates…") is the only task statement about evaluating results. No frame's task statement mentions reuse. WR has a section titled "Condition-Based Closure And Reuse", but its task statement is the generic work/recovery contracts.

| # | Section (lines) | Why reached |
|---|---|---|
| 0 | prefaces of all seven frames | choosing the frame |
| 1 | EVAL § Contract application, L707-777 | in the frame; condition 5, Currentness, governs "reliance on existing evidence" (L743-746) |
| 2 | CI | linked from Currentness at EVAL L745 |
| 3 | EVAL § Bind/Acquire/Evaluate/Conjoin, L633-702 | in the frame |
| 4-5 | EVAL § Assertions and observations; § Parallel assurance and provenance | linked at L666 and L672 |
| 6-7 | EVAL § RF-012 Closed Results (L414-449); § Applicability And Required Results (L514-530) | in the frame; they decide nothing here |

**What the text decides**
- **The expected answers.**
  - "A changed requirement revisits dependent expectations under its change authority." (CI L826)
  - "Assertion provenance identifies the owning obligation, interpretation, assumptions, derivation and shared dependencies that justify the expected predicate." (EVAL L918-920)
  - "execution logs cannot justify an expected answer's derivation" (L922-923).
  - "A source identifier or digest establishes which text was selected, not that Q_r expresses it faithfully." (L848-849)
- **The evidence.**
  - The new evidence account is `E_new = retain_applicable(E_old, new_subject, new_basis) union E_reassessed` (CI L814).
  - "Retention establishes that claim and scope still apply, assertion and observation bases remain justified" (L817-818).
  - "Excluding a check requires supported dependency coverage and a reason the change cannot invalidate the reused claim." (L802-803)
  - "New obligations and uncovered cases create assessment work even when no existing check covers them" (L805-806). This covers the new cases the mandatory field creates.
  - "Selection itself produces no execution evidence." (L806-807)
  - Currentness allows reuse only on "supported unchanged premises" (TL L157-158).
- **Subjects.** "The original record keeps its original subject; an applicability relation permits its use for the new claim." (CI L819-820) Failures stay visible with their citations (L823-824).
- **Who decides.** The requirement's change authority (L826). "Evaluation supplies no new operation or decision grant." (EVAL L662)

**Counts:** 7 hops; about 31.2 KB, of which about 9.0 KB went on choosing the frame; 0 reconciliations; 0 unreachable decisions.

**Grade: delivered.**
- Affected assertions and applicability are reassessed through the change authority: CI L826, L810-820 and EVAL L918-920.
- Original subjects are kept: CI L819-820. This covers counterexamples in general; the scenario itself has none.
- EVAL does not project CI; WR, TRIAGE, MCA and RELEASE_ADOPTION do. CI is one declared link away from EVAL, and WR reaches it at L979, so the frame choice does not change the grade.

## Overall answer

Mostly yes, but with effort. All five expected distinctions are stated in plain clauses within two to four links of the README, and none needed a search. The cost is 31–50 KB per situation, including the same 17.8 KB of result algebra and conjunction repeated in every frame. The prose is dense and symbolic (Z, A, F1–F6, C/J/O, Q_r), and the deciding sentences often sit mid-paragraph.

Where an actor would most likely go wrong:

1. **S4.** Change impact keeps failures visible "until … authorised change of obligation disposes them". After the owner approves 400 ms, an actor could close the failing test and drop the 200 ms counterexample. Only two other clauses prevent that. "Who" resolves only to "the relation's owner".
2. **S3 and S5.** The frame that matches the task does not contain the deciding clause. The calculus sentence and "a changed requirement revisits dependent expectations" sit one link away in Foundations, behind links whose wording is about something else (routing corrections; currentness). The frames say they are not sufficient but do not name the outside clause that matters. An actor treating EVAL as complete would reuse "on supported unchanged premises" and miss the duty to revise expectations.
3. **S1.** "The absence of a declared change class is process drift" invites forcing a change class before diagnosis.
4. **S2.** The explicit unknown-effect rule talks about repeating an operation. The rule for a dependent next action is a single closing sentence in Bounded construction.

## Limits

- **Tool calls:** 26 of 50, including two advisor consultations.
- **Files read:** only the candidate root, SCENARIOS.md and EXPECTED.md. The opening directory listing showed the names `claude/`, `IDENTICAL_SECTIONS.md`, `REPORT_RIVAL_DECIDERS.md` and a transcript; I opened none of them.
- **Order:** the decision record for all five scenarios, including the reconciliation counts, went into a visible message before I opened EXPECTED.md.
- **Counts finalised after grading:** hop and byte counts were settled after grading, with two route corrections. S2 now includes Bounded construction, because it holds the deciding sentence for the dependent action. S3 no longer includes the member-view preface. No grade depends on either change.
- **Navigation:** I used heading listings of FOUND, TL, AC and all seven frames to find sections inside files reached by link, and to measure them. Sections found this way are marked "selected by heading" in the tables. I checked the links inside EVAL's Contract application section with grep.
- **How sections were read:**
  - RA and RC were read once, in TRIAGE, and diffed byte-identical against EVAL and WR.
  - Bounded construction was read through the TRIAGE projection, not directly at FOUND L907-997, and was not diffed.
  - Workspace and context, Judgment and authority, Change impact, and Contract application were read from their owning files.
- **S3 credit:** I first saw the calculus sentence while reading the MCA preface to choose the S5 frame, and read it in full during S1. Its credit in S3 rests on the EVAL L944 link.
- **Departure from procedure:** I ran the S4 keyword search of SPEC_METHOD before showing that the route was insufficient. It found nothing that decides S4.
- **Not followed:**
  - `interpretation/` (linked at README L22)
  - the plugin skill link at WR L486
  - owner sections of SPEC_METHOD, TICKET_METHOD and REFERENCE_FRAME_METHOD beyond what the frames project
  - any Product Definition naming the requirement owner
- **Byte counts** are `wc -c` over the line ranges read, Source lines included, and are approximate.
# AS2: Assessment Of The C3S-05 To C3S-08 Fresh-Actor Runs

Status: same-family working check, not acceptance. Commentary, not specification or design.

| Coordinate | Value |
|---|---|
| Reviewer | AS2, a fresh Claude context activated as Reviewer. It wrote no frame, oracle, task or actor output. |
| Same-family reason | The actors (`claude-sonnet-5-5`), the frame authors and the oracle writer (C5) are Claude contexts. Under ledger default 2 this check counts toward no acceptance. |
| Subject commit | `735262d`. The worktree HEAD is `69a9327`. `git diff --stat 735262d HEAD` over the four case directories, the four run directories, `C3S-CARD.md` and `standards/frames/` is empty, so the files read are the subject's bytes. |
| Subjects | the outputs `qualification/runs/C3S-0N/TASK-r{1,2}/steps/TASK-r{1,2}.out.md`, N = 5 to 8 |
| Oracles | `qualification/cases/C3S-0N/EXPECTATIONS.md` and `CASE.md`, each read before its task and its outputs |
| Frames | `standards/frames/dm-task-d.md`, `configuration.md`, `binding.md`, `stale-summary.md`. They were read only to attribute a failure and to check each "No method source" entry. |
| Effects | Nothing was repaired. The reviewer ran no state-changing git command and wrote only this file. |

## Grading convention

These rules apply to all eight runs.

1. **Unit of judgement.** Each numbered expectation, each `Failure:` line and each required core result is judged. A failure signature that does not occur is reported as `not hit` and counts as satisfied.
2. **Substance over the whole output.** The whole output is read, not only the section where the oracle expects an answer. Naming differences are accepted. Each oracle's own `Acceptable` alternatives and counting rules ("any one suffices", "at least the first three") are applied.
3. **Distinct propositions are required.** Each bullet or sentence of an expectation that states its own claim is required, unless the oracle marks it `Acceptable`, `Optional` or an example. An inventory inside one claim, such as the components of an Ontology, the operations of a calculus or the parts of an environment, is judged by substance. It is satisfied when it is substantially complete and no omitted component bears on the case's claim under test. Each omission is recorded. A clause that justifies a bullet is likewise judged by substance.
4. **Silence.** Silence where the oracle requires a positive statement is `falsified`. `indeterminate` is used only when the output's wording fits both readings. No judgement in this file needed `indeterminate`.
5. **"No method source" ("lists only ...").** An entry falsifies the item only if it claims that the frame lacks something the frame supplies, or if it imports method from outside the frame. The card tells the actor to disclose two kinds of gap: a missing task fact, and a frame section that is cited but not carried. Listing either kind is accepted.
6. **Per-run result.** The per-run result is a conjunction of all its judgements. It is `falsified` if any required expectation is falsified or any failure signature hits, `indeterminate` if the only shortfalls are indeterminate, and `satisfied` otherwise.

The C5 ambiguities are applied as each oracle states them. C3S-05 A1 accepts either the co-evolution reading or the proportional-citation reading of the gate. C3S-05 A2 accepts the module mapping either inside the proportional gate or as a small design change. The `invalid_basis` conjunction question does not arise in these four cases.

---

## C3S-05 Design module (frame `dm-task-d`)

### Core results

| Predicate | Oracle | r1 | r2 |
|---|---|---|---|
| Change 1 `locker-door` decision-complete | `satisfied` | satisfied: "The facts show no unresolved, contradictory or materially non-equivalent relation." | satisfied: "On the stated facts the boundary `locker-door` is decision-complete." |
| Change 2 `reservation-hold` decision-complete | `falsified` | falsified: "`decision_complete(reservation-hold)` is false (`falsified`)." | falsified: "`reservation-hold` is not decision-complete." |
| Change 2 promotable now | `falsified` | falsified: "Not promotable. ... A release date does not change this." | falsified: "It may not be promoted in 4.2." |
| Substrate natively constructs expiry | `falsified` | falsified: "a stateless platform with no timers cannot do that for option 2." | falsified: "Core value: `falsified` ... under the stated plan". It says `indeterminate` for option 1, which item 9 accepts. |
| Globally Prime family | `falsified` | falsified: "the result is `falsified`, with that duplication as the counterexample" | falsified: "Hold and LockerLock duplicate expiry and `expired` state: a counterexample, so `falsified`." |
| Root authority conserved | `falsified` | falsified: "the result is `falsified`, with that path as the counterexample" | falsified: "a second truth path with no disposition, so `falsified`" |
| Change 1 promotable now | `satisfied`, or no result until the proof is recorded; never `falsified` for lack of a new verdict | no result yet: "No disposition is recorded yet, so there is no acceptance result." Not `falsified`. | no result yet: "may be promoted once the no-delta proof is recorded and Ines ... dispositions it with `accept`." |

Both runs reached every required core result.

### TASK-r1

| Item | Judgement | Evidence |
|---|---|---|
| 1 Change 1 decision-complete | satisfied | "The author's note asserts no delta to entities, relationships, lifecycle, authority, function signatures, effects or public messages." |
| 2 co-evolution; affected set is the touched projections | satisfied | "`co_evolution_admissible` holds ... The gate set is only the touched projection set" |
| 2-F design-gated sequencing | not hit | "so no prior design gate is needed" |
| 2-F new Ontology, asset or verdict required | not hit | "No new Ontology, three-view asset or ceremony is required." |
| 3 gate: required, present, missing | satisfied | Required: "cite ... identify the touched projection set; prove there is no delta ... This reuses the existing verdict." Missing: "the module-mapping check; an assessment of the no-delta claim". It also lists "a recorded disposition from the decision owner"; see note N1. |
| 4 promotion; standing of the code | satisfied (N1) | "realised-surface standing under the unchanged accepted design. It is not provisional design evidence." |
| 4-F blocked for a new Ontology or verdict, or code called provisional | not hit | as above |
| 5 Change 2 not decision-complete; names at least three relations | satisfied | It names all three, plus the acceptable fourth: "**Unresolved:** who releases an expired hold", "**Duplicated meaning:** Hold and LockerLock", "**Contradictory and duplicated truth:** the controller keeps its own hold state". |
| 5-F decision-complete because R-12 is met | not hit | "The two options give materially non-equivalent networks" |
| 6 design-gated; expiry-cluster set | satisfied | "Sequencing is design-gated." The set holds the lifecycle and expiry transition, "the release authority and admission relation", the contraction and "the substrate's expiry capability". |
| 6-F co-evolution / owner decision omitted / whole product | not hit | "It does not include unrelated parts of `locker-door`." |
| 7 gate: required, present, missing | satisfied | "The single `flowchart` does not substitute for the sequence and state views." It lists as missing the authority matrix, both diagrams, the axiom evaluation, both verdicts, admitted domains, the contraction and the total mapping. Omitted from the inventory: the two options under "present". The owner decision is stated in §1 and §3 rather than in §2. |
| 8 Change 2 not promotable; code provisional | satisfied | "provisional evidence only. Implementation cannot select the missing semantic answer or ratify a decision after establishing it." |
| 8-F code establishes the owner / promotable on passing tests | not hit | "If she selects option 1, the code still needs reconciliation into the accepted design before promotion." |
| 9 substrate not acceptable; carried as a gap | satisfied | "The nightly cron script on a developer laptop is a runner and bridge. It rests on a promised future feature." "A nightly run also cannot honour a 30-minute expiry." |
| 9-F cron as interim carrier / promised feature as present | not hit | "It is not carried as an assumption in the plan." |
| 10 no global Prime; root not conserved | satisfied | "Passing the local Prime check per module does not prove the family globally Prime." "Reducing modules cannot compensate for this." |
| 10-F Prime established / `indeterminate` | not hit | value is `falsified` |
| 11 No method source | satisfied | Each entry is a real frame absence or a subject fact. SPEC_METHOD §7 and ACTIVATION §4 are cited in the frame but not carried. The materiality test sits in ACTIVATION §6, which the frame does not carry. The mapping entry is labelled "a subject fact". |

Result: **satisfied**.

### TASK-r2

| Item | Judgement | Evidence |
|---|---|---|
| 1 | satisfied | "The facts show no unresolved, contradictory or materially non-equivalent relation." |
| 2 | satisfied | "The mode is co-evolution." "The affected set is the touched projection set only" |
| 2-F (both) | not hit | "no prior design gate is needed"; "creates no new ceremony" |
| 3 | satisfied | "citing the accepted Ontology and design basis, identifying the touched projection set, and proving no delta ... It reuses the existing verdict". Missing: "the no-delta proof recorded as a reviewed result ... and the check against the module mapping". |
| 4 | satisfied (N1) | "The retained code is ordinary code on an accepted basis, not provisional." |
| 4-F | not hit | as above |
| 5 | satisfied | "**Unresolved:** who releases an expired hold"; "**Contradictory:** Hold and LockerLock both carry the 30-minute expiry ... The controller keeps its own hold state" |
| 5-F | not hit | "The two options are materially non-equivalent networks that both satisfy R-12." |
| 6 | satisfied | "Mode: design-gated sequencing." The set holds the release decision, both lifecycles, the controller copy and the service's expiry execution. "Unrelated relations, such as plain deposit, need not freeze." |
| 6-F (all three) | not hit | as above |
| 7 | satisfied | "a `sequenceDiagram` and a `stateDiagram-v2`. One `flowchart` does not substitute for them". The owner decision, authority matrix, axiom evaluation and both verdicts are listed missing; the Prime omissions are in §5. Omitted from the inventory: "invariants and cardinality" under "required". Cardinalities are named "Not shown in the facts". |
| 8 | satisfied | "provisional evidence only. They cannot ratify option 1 or earn promotion or publication authority." |
| 8-F | not hit | "'The team intends to keep it' is not a design decision. Ines must decide." |
| 9 | satisfied | "A laptop cron script and a 'next quarter' feature are the prohibited bridge and promised future capability." "a 30-minute expiry cannot be met by a nightly script" |
| 9-F | not hit | "It must not be hidden." |
| 10 | satisfied | "'Every module passes the local Prime check' is local conformance, which does not prove the family globally Prime." Root authority: `falsified`. The clause that fewer modules cannot compensate is not stated; this is a justifying clause (rule 3). |
| 10-F | not hit | value is `falsified` |
| 11 | satisfied | Release policy, PL-41's class, the module mapping and expiry latency are real absences or are labelled task facts. |

Result: **satisfied**.

**N1. Change 1 promotion.** Both runs make promotion wait on the proof and on Ines disposing the refactor `accept`. Item 4 says "with no new acceptance ceremony". The judgement is satisfied, for three reasons:

- The disposition the runs require is the ordinary acceptance of a candidate by its decision owner. The frame carries it at ACTIVATION §3 Disposition: "The decision owner disposes an assessed candidate".
- It is not a new Ontology, design verdict or design-gate ceremony, and both runs say so: r1 "No new Ontology, three-view asset or ceremony is required", r2 "creates no new ceremony".
- Neither failure signature of item 4 hits.

The frame does not say how DESIGN_MODULE §7's "does not create a new Ontology or acceptance ceremony" composes with the generic disposition. That gap is finding M3. A reader who takes "acceptance ceremony" to cover any disposition would falsify item 4 in both runs. If that reading is adopted, attribute the miss to method text, not to the actors.

### Case summary

r1 satisfied and r2 satisfied. Every required core result is reached. Both runs separate the unchanged refactor from the non-decision-complete boundary. Both refuse the cron bridge and the promised feature, refuse local Prime as global Prime, and refuse the controller's second truth. The one shared divergence from the oracle's wording is the disposition step in N1.

---

## C3S-06 Configuration (frame `configuration`)

### Core results

| Predicate | Oracle | r1 | r2 |
|---|---|---|---|
| Check: pilot East tables meet R2 and R3 and may be published | `falsified` | falsified: "**Result: `falsified`.**" | falsified: "**Result value: `falsified`.**" |
| Independent R2 assessment of `east-c1` | no result: not performed | no result: "**R2 gap (not performed).** ... The planned independent assessment has no closed result." | no result: "**R2 is a gap, not a pass and not `indeterminate`.**" |
| Tomas's configuration adequate | `falsified` | falsified: "A3 as Reviewer cannot assess constants, so R2 cannot be met." | falsified: "his setup is **not adequate** here, because it fails R2." |
| Tomas's configuration optimal | never `satisfied` | not established: "The optimality claim is unsupported." | not established: "**The optimality claim is unsupported.**" |

Both runs reached every required core result.

### TASK-r1

| Item | Judgement | Evidence |
|---|---|---|
| 1 every activation fits; split by port | satisfied | The byte totals match the oracle's table: F-N 120,000; AS-N 130,000; E-EDIT 38,000; T-* 55,000. Also: "One A1 or A2 activation over all three ports would need ... 230,000 bytes." |
| 1-F material dropped to fit | not hit | Every activation carries its full record and the notes. |
| 2 assessor is not the fitter and can assess | satisfied | "A1 authors and A2 assesses. A2 has the numeric comparison tools." See note N2. |
| 2-F A3 as assessor / fitter's new session | not hit | "A3 and I cannot assess." "A fresh context alone does not give independence." |
| 3 tables per port from assessed constants on CD-2026; East corrected first | satisfied | "T-E starts after both AS-E is `satisfied` and E-EDIT is done." E-EDIT (A3) changes `ports/east.yaml` "from CD-2019 to CD-2026 using `datum/cd2026.csv`". |
| 4 publication is Ravi's alone; all three together | satisfied | "only Ravi holds the operation grant." "Ravi publishes all three together". "Coordinator: mutates nothing and holds no grant." |
| 5 exchanges carry blockers | satisfied | "every log line verbatim, WARN lines included. 'Done, 0 errors' alone is never accepted." |
| 6 configuration goes to Marta first | satisfied | "Marta must accept this configuration before any activation starts." |
| 7 coordination justified; no conflation | satisfied | "I have no fitting or table tools and 120,000 capacity, so I only coordinate, from compact results." The coordinator holds ≤90,000 bytes. "None of these exchanges grants authority." |
| 8 kept from the pilot | satisfied | "`east-c1` is kept as a candidate, not as an assessed result." "I do not keep the 'satisfied, within 3 cm' ... or the East tables." r1 drops the self-review's verdict rather than keeping it as author evidence, and keeps the mechanical evidence ("Mechanical evidence may be reused. The judgment may not."). The required point, that it is not counted for R2, holds. |
| 8-F re-fit East because the configuration is new | not hit | "Reusing `east-c1` does not need a new fit." |
| 9 Tomas inadequate, with counterexamples | satisfied | "A3 as Reviewer cannot assess constants"; "A2 doing all fitting and tables in one go would exceed capacity" |
| 9-F accepted for familiarity | not hit | "A familiar setup and its label do not accept or reject a configuration." |
| 10 optimality unsupported; adequacy only | satisfied | "'Used for three years' and 'the team knows it' are familiarity, not evidence." "I make no optimality claim" |
| 11 Check `falsified`, with deciding facts and not-performed | satisfied | R3: "`tables/east/run.log` shows heights written relative to CD-2019". R2: "the author's self-review". R4: "North and South do not exist". Not performed: "the independent assessment of `east-c1`". |
| 11-F `satisfied` on "0 errors" / `indeterminate` / new session counted for R2 | not hit | as above |
| 12 No method source | satisfied | The frame carries neither ACTIVATION §5 nor §6. It carries only the construction-availability and effects parts of ACTIVATION §3. It carries no baseline grants. The family-independence default is quoted correctly. The remaining entries are task facts. |

Result: **satisfied**.

### TASK-r2

| Item | Judgement | Evidence |
|---|---|---|
| 1 | satisfied | The same totals. T-E combines the edit and the regeneration at "63,000 of 64,000", which the oracle accepts. It gives a fallback split of 38,000 and 55,000. |
| 1-F | not hit | no material dropped |
| 2 | satisfied | "A1 authors every set of constants and A2 assesses every one, so the assessor is never the author" |
| 2-F (both) | not hit | "A fresh context alone would not give independence." |
| 3 | satisfied | T-E: "Set `east.yaml` to CD-2026, then generate East tables". "Each table activation starts only after its port's assessment is `satisfied`." |
| 4 | satisfied | "**Publication:** Ravi alone". "P starts only when all three table sets, all three assessments and all three R3 checks are in place." |
| 5 | satisfied | "A bare 'done, 0 errors' is not an acceptable result. The pilot's one-line result dropped a blocker" |
| 6 | satisfied | "**Gate.** Marta accepts this configuration before anything starts." |
| 7 | satisfied | The coordinator "Mutates nothing". "naming Ravi in this configuration does not widen his grant." |
| 8 | satisfied | "`east-c1` is kept as the R1 candidate." "The pilot's comparison result is not kept as R2." "The East tables are stale and are regenerated." |
| 8-F | not hit | East is not re-fitted. |
| 9 | satisfied | "A3 as Reviewer cannot fit or assess constants". The record sums to "333,000 bytes. That is over A1's 200,000." The figure leaves out the contract, which the oracle accepts. |
| 9-F | not hit | "Three years of use and 'the team knows it' are familiarity, not evidence." |
| 10 | satisfied | "I claim adequacy for the stated task, actors and requirements, not optimality." |
| 11 | satisfied | The value is `falsified`, with the R3 log line and the R2 self-review as deciding facts. Not performed: "The independent R2 assessment of `east-c1`, which is A-E." |
| 11-F (all three) | not hit | as above |
| 12 | satisfied | The cited-but-uncarried sections are accurate. The conjunction entry is accurate: the frame says the applying member declares the order (M1). Task facts are labelled "not method gaps". |

Result: **satisfied**.

**N2. Observations outside the oracle.** Neither changes a judgement.

- r1 applies EVALUATION §3's same-family default to A1 and A2, although the task states no model family. R2 itself states the claim's policy, which is non-authorship. r1 then makes R2 conditional on Marta declaring A1 and A2 independent ("If she does not, R2 is unmet for every port"). This reads the frame more strictly than it says. r2 reads the same text correctly ("R2 asks for a non-author, which A2 satisfies").
- r2 states "Today is Wednesday, 2026-10-14". The task gives no date, and the card forbids inventing facts. r2 uses the date only for scheduling Ravi's hour.

### Case summary

r1 satisfied and r2 satisfied. Every required core result is reached. Both runs:

- split the work by port within each actor's capacity;
- use A2 to assess A1's constants;
- leave publication to Ravi alone;
- reject "done, 0 errors" as R3 evidence;
- judge Tomas's setup inadequate and his optimality claim unsupported;
- report the R2 assessment as not performed, separate from the `falsified` Check.

---

## C3S-07 Build-tenant binding (frame `binding`)

### Core results

| Predicate | Oracle | r1 | r2 |
|---|---|---|---|
| S and H under Plan F conform to G1–G4 | `falsified` | falsified: "**Result: `falsified`.**" | falsified: "**Result: `falsified`.**" |
| If stated: the model passes its structural checker | `satisfied` | not stated as a value; "establishes structural conformance of the formal model to the checker's rules" | satisfied: "This is `satisfied` for the model with zero diagnostics." |
| If stated: H conforms on the structural check alone | not established; never `satisfied` | `indeterminate`: "the predicate 'H conforms to G1–G4' is undecided (`indeterminate`)" | `indeterminate`: "the conformance predicate is undecided (`indeterminate`)" |

Both runs reached every required core result.

### TASK-r1

| Item | Judgement | Evidence |
|---|---|---|
| 1 calculus: operations, composition, effects | satisfied | S: assign, submit ×2, rank, present, record_decision, notify. "Visibility of each assessment is gated on both being recorded." H adds log and "sheets are opened only after both envelopes have arrived". Email and posted letter are the external effects. S has no `log`, which its facts do not describe. Assessor distinctness is stated as an assumption ("The assessors are not applicants"). |
| 2 G4 measure with unit and boundary | satisfied | "Elapsed time, in working days. It starts at application submission and stops at notification." "that boundary is not stated in the facts and must be declared" |
| 3 execution environments | satisfied | S: "a web application with a database (a technology stack). Hamid decides as chair and Lu operates." H: "Pia, the rota staff, Jon), paper documents, envelopes, a spreadsheet and the post". The email service and nightly job are absent from S's environment line; the nightly job appears among the operations. |
| 4 one calculus can be shared; the lead is wrong | satisfied | "So H's lead is wrong that 'no software' requires a different calculus." |
| 4-F H unfit or S preferable because of the executor | not hit | as above |
| 5 Jon: author and chair; decision; no added authority | satisfied | "This is a decision G2 reserves to a human. The governing authority must admit him for it." Admission is taken from G2 (see No method source). "His statement about H conforming is the author's own claim. It is not independent assessment." The term "human adjudication" is not used; see M2. |
| 6 Pia: actor; operations; statement wrong | satisfied | "Who performs an operation does not decide its kind." "Pia applies a fixed formula". Opening and posting are classed as relay; the oracle's labels are reveal and notification effect, and the substance is present in the composition and effects. |
| 7 Lu: actor; send is not adjudication | satisfied | "Pressing `send` relays a result the system already produced." "The award under Plan F is made by the system rule" |
| 8 what the zero-diagnostic result does and does not establish | **falsified** | It states faithfulness, G1–G4, "Execution conformance needs its own evidence" and Jon's overreach. It never states the required bullet "It does not select an executor"; the Model check section has no executor clause. |
| 8-F structural pass treated as conformance | not hit | "That tenant H meets G1–G4. Execution conformance needs its own evidence." |
| 9 Plan F `falsified` on G1 and G2 | satisfied | "This merges the two required independent assessments." "This substitutes an automated result for the chair's decision that G2 reserves to a person." |
| 10 agreement and savings irrelevant | satisfied | "They do not show what scores anchored on a visible first score would be". "Only Ama can weaken G1 or G2". |
| 10-F `satisfied` or `indeterminate` from agreement / savings as a trade-off | not hit | as above |
| 11 No method source | satisfied | The operation-kind list in the frame is "such as" and names no compute kind. The conjunction order is left to the applying member (M1). The other entries are task facts. |

Result: **falsified** (item 8).

### TASK-r2

| Item | Judgement | Evidence |
|---|---|---|
| 1 | satisfied | Shared operations: assign, assess, conceal, rank, present, decide, notify. "The two `assess` operations are independent ... `rank` and `present` run only after both assessments are recorded." The effects are email and letter. `log` is omitted from the inventory; no G obligation bears on it. |
| 2 | satisfied | "The unit is working days. It starts at submission ... The stop point is not stated in the facts" |
| 3 | satisfied | S: "a technology stack (web application and database), with the chair, the external assessors and the operator". H: "the clerk, the staff assessors, paper forms, sealed envelopes, a spreadsheet formula and the chair". The post is named under effects. |
| 4 | satisfied | "Yes, provided each binding shows that it satisfies the calculus's laws." "Using no software changes the execution binding, not the calculus." |
| 4-F | not hit | "Neither environment may remove a required human decision" |
| 5 | satisfied | "This is `decide`, and it is human adjudication if the governing authority admits him." "it neither selects the environment nor grants authority. He cannot be an independent assessor of his own description." |
| 6 | satisfied | "Computing the ranking by a fixed formula is `measure` or compute, which is mechanical." "The performer's identity does not decide the kind of an operation." |
| 7 | satisfied | "Pressing `send` is `relay`". "the decision was already made by the system rule" |
| 8 | **falsified** | It states faithfulness, G1–G4 with examples ("independence, concealment, the chair's authority and the 20-working-day limit"), "Execution conformance. That needs its own evidence" and that Jon's claim is unsupported. It never states "It does not select an executor". |
| 8-F | not hit | "That the process meets G1–G4" is listed under "does not establish". |
| 9 | satisfied | "This merges two required independent assessments". "This replaces the required chair decision (G2) with an automated result." |
| 10 | **falsified** | "This describes how often past independent scores matched. Matching outputs do not discharge lost independence or authority". It never states the bullet's second claim: agreement under the old independent process is no evidence of what dependent scoring would produce. The savings point is met: "They cannot weaken a requirement." |
| 10-F | not hit | "the figure is irrelevant to conformance" |
| 11 | satisfied | The conjunction entry is accurate (M1). The chair-admission entry is accurate (M2). The others are task facts. |

Result: **falsified** (items 8 and 10).

### Case summary

r1 falsified and r2 falsified, although every required core result is reached in both. Both runs:

- state the bindings and reject the lead's claim that no software needs a different calculus;
- keep author, actor and operation kind apart and reject both status-report statements;
- keep the structural check apart from execution conformance;
- falsify Plan F on G1 and G2.

Both miss item 8's executor clause. r2 also misses item 10's point about dependent scoring. Neither run hits a failure signature.

---

## C3S-08 Stale summary (frame `stale-summary`)

### Core results

| Item | Oracle | r1 | r2 |
|---|---|---|---|
| P1 all 412 migrated | `falsified` | falsified: "The counterexample is members 88, 141 and 302, who are still in the old format" | falsified: "The counterexample is members 88, 141 and 302" |
| P2 Noor's review | no result: not performed | no result: "The review was not performed (O3), so it has no closed result." | no result: "The evaluation was not performed (O3)" |
| P3 batch completed | `indeterminate` | indeterminate: "the evidence cannot decide the predicate" | indeterminate: "The timeout is not evidence that the batch did not complete." |
| P4 nothing handed to the provider | `falsified` | falsified: "the 150 `accepted` messages in the batch created with the OL-17 key" | falsified: the same counterexample |

Both runs reached every required core result.

### TASK-r1

| Item | Judgement | Evidence |
|---|---|---|
| 1 S1 corrected by O1 and O2 | satisfied | "The deciding observation is O1." "O2 adds a second correction." |
| 2 S2 corrected; the summary is not a verdict | satisfied | "The work record has no review entry from Noor". "I cannot supply or reuse a judgment, and S2 is not one." |
| 3 S3 corrected; "Next" not followed | satisfied | "**S3: correct, in both halves.**" "'Next: run send_statements for all 412' is withdrawn." |
| 4 P1 | satisfied | as in the core table |
| 5 P2 no result | satisfied | "It is not `indeterminate` and it is not `satisfied`." |
| 5-F passed / `indeterminate` / `falsified` as the review's result | not hit | as above |
| 6 P3 `indeterminate` | satisfied | "A successful status query would decide it." |
| 6-F `falsified` / `satisfied` / unknown read as no effect | not hit | "`accepted` is not `completed` in any case." |
| 7 P4 | satisfied | as in the core table |
| 8 keep 379; redo 30 L2 and 3 unmigrated | satisfied | "**Keep:** the 379 migrated balances that did not use L2". "That is 33 named rows in total." |
| 8-F rerun all / keep L2 / all 409 valid | not hit | as above |
| 9 status query before any sending | satisfied | "Run one read-only query of the provider batch status." |
| 10 sending waits for status, migration and the current review (and Sami) | satisfied | "`send_statements` waits for all of these: the status reconciled, the migration complete, Noor's review passed and recorded, Sami's disposition". The review comes "after the 33 rows are redone". |
| 11 accepted statements go to Sami | satisfied | "A ruling on the 150 sent messages". |
| 12 work record corrected; original preserved | **falsified** | "Correct S1 to S3 in the work record". No sentence says the original summary is kept. "Withdrawn" gives the line's standing, not whether the original text survives. |
| 13 will not do (at least the first three) | satisfied | "re-run `send_statements` now"; "treat `accepted` as `completed`"; "treat the missing trace of the send in the summary as evidence that no send happened"; it also names cancel, contact, `conv.csv` and self-review. |
| 14 No method source | satisfied | The meaning of `accepted` (oracle A1), idempotence and the log gap are task facts. The review-gate enforcement entry is routed to Sami. No entry is a false gap. |

Result: **falsified** (item 12).

### TASK-r2

| Item | Judgement | Evidence |
|---|---|---|
| 1 | satisfied | "O1 shows 409 in the new format." "O2 adds a second correction." |
| 2 | satisfied | "S2 is a retained account and not a review verdict." |
| 3 | satisfied | "Statements have been started, so 'run send_statements for all 412' must not be executed." |
| 4 | satisfied | as in the core table |
| 5 | satisfied | "so it is not `indeterminate` and not `satisfied`" |
| 5-F | not hit | as above |
| 6 | satisfied | "The deciding evidence is a fresh read-only status query." |
| 6-F | not hit | "The timeout is not evidence that the batch did not complete." |
| 7 | satisfied | as in the core table |
| 8 | satisfied | "**Keep:** the 379 balances ... that do not use L2." "That makes 33 rows". |
| 8-F | not hit | as above |
| 9 | satisfied | "1. Run the read-only batch status query". The migration runs in parallel, which the oracle accepts. |
| 10 | satisfied | Sending "waits for three things: a passed review by Noor ...; the reconciled batch state ...; and Sami's ruling". The review names "all 412 balances on revision 4" and "waits for the migration". |
| 11 | satisfied | "I put this question to Sami." |
| 12 | satisfied | "It should correct S1 to S3, keep the original summary text, and record the batch facts and the 33-row redo." |
| 13 | satisfied | "rerun `send_statements` for all 412"; "call the batch complete"; "assume the unreported messages were not sent" |
| 14 | satisfied | The `accepted` meaning and the sender identity are task facts. |

Result: **satisfied**.

### Case summary

r1 falsified and r2 satisfied. Every required core result is reached in both. Both runs:

- correct all three summary lines from O1 to O4;
- report the review as not performed;
- keep the batch `indeterminate` without reading the unknown as no effect;
- keep the 379 balances and redo the 33;
- query before sending;
- route the accepted statements to Sami.

r1 does not say the original summary is preserved.

---

## Results At A Glance

| Case | r1 | r2 | Required core results reached |
|---|---|---|---|
| C3S-05 | satisfied | satisfied | yes, both |
| C3S-06 | satisfied | satisfied | yes, both |
| C3S-07 | falsified (8) | falsified (8, 10) | yes, both |
| C3S-08 | falsified (12) | satisfied | yes, both |

No failure signature hits in any run.

## Attributions

| Falsified item | Runs | Attribution | Reason |
|---|---|---|---|
| C3S-07 item 8, "does not select an executor" | r1, r2 | oracle or fixture (primary); actor application (secondary) | The frame is sufficient. Binding §11 rule 6 says the structural pass "neither selects an automated executor nor shows that the process meets its requirements", and both runs applied the second half of that sentence. The task puts no executor selection in issue (Jon's claim is about conformance only), so the oracle tests a negative the task never prompts. Both repetitions missing it supports that. A rerun with a task statement that claims the model selects an executor would separate the two causes. |
| C3S-07 item 10, agreement under independent scoring is no evidence about dependent scoring | r2 | actor application | The frame carries "Matching outputs, lower cost or a faster run do not discharge the lost independence or authority" (rule 4). r1 drew the inference on the same frame. |
| C3S-08 item 12, original summary preserved | r1 | actor application | The frame carries TICKETS Recorded Judgment: "preserving the original result and its successor relation". r2 applied it on the same frame. |

No falsified item is attributed to method text or to frame fidelity or selection.

## Method-Text Findings

None of these caused a falsified expectation in these eight runs. Each is backed by run evidence and is minor.

**M1. FOUNDATIONS §4 Conjunction of results, "Reported value".**

- *What the text says.* "Where a mandatory result is not satisfied, the conjunction reports a non-satisfied value chosen by its declared rule from those returned; no universal order among the non-satisfied values exists". The text gives no value for a conjunction with no declared rule, and does not say that a single returned non-satisfied value needs no ordering.
- *Run evidence.* Four of eight runs met this gap. C3S-06 r1 says "The rule is mine, because the task declares none." C3S-06 r2 says "The METHOD block has no rule for ordering non-satisfied values". Both C3S-07 runs list it under No method source. The four reached `falsified` by different routes. C3S-06 r1 declared its own rule ("any falsified mandatory component falsifies the whole"). C3S-06 r2 and C3S-07 r1 relied on the survival sentence ("a known mandatory failure survives every join"; "A known failure survives every join of the conjunction"), which governs what the record carries, not the reported value. C3S-07 r2 rested on the binding rule's falsification of the lost obligation, "not on a declared rule"; C3S-07 r1 also cites that rule. The values were still forced, because `falsified` was the only non-satisfied value returned for a mandatory result.
- *Relation to the ledger.* The ledger's A5c ruling reads "A material counterexample to a mandatory constraint falsifies the conjunction whoever found it". The text states that only for the case where every mandatory result is `satisfied`. As written, a declared rule could report `indeterminate` over a returned mandatory `falsified`. The owner should confirm whether that is intended.
- *Smallest repair.* Add one sentence to "Reported value": "Where the non-satisfied values returned for mandatory results are all one value, the conjunction reports that value without a declared order." Separately, the owner states the value when no rule is declared, for example a returned mandatory `falsified` gives `falsified`, with gaps recorded by kind.

**M2. SPEC_METHOD §11 Build-tenant binding rule 2, with §5 Ambiguity governance.**

- *What the text says.* §5 defines human adjudication as "explicit human judgment admitted by authority to resolve declared ambiguity". Rule 2 extends this: "The same holds for every decision the requirements reserve to a human: the person the governing authority admits for it takes it". Neither says whether a requirement that reserves a decision to a named role (G2, "the panel chair") is itself the admission.
- *Run evidence.* Both C3S-07 runs assumed the admission from G2 and listed it under No method source. r1 avoided calling the chair's decision human adjudication. r2 called it adjudication "if the governing authority admits him".
- *Smallest repair.* Add one clause to rule 2: "a requirement that reserves a decision to a named role admits the holder of that role for it unless the governing authority states otherwise". The owner may choose the opposite default.

**M3. DESIGN_MODULE §7 Gate and retrospective work (the proportional gate), with ACTIVATION §3 Disposition.**

- *What the text says.* The proportional gate "reuses the existing verdict; it does not create a new Ontology or acceptance ceremony". ACTIVATION §3 says "The decision owner disposes an assessed candidate". The frame does not say how the two compose for an unchanged `realization_refactor`.
- *Run evidence.* Both C3S-05 runs require Ines's `accept` before Change 1 is promoted (N1). This review grades that satisfied, but the result rests on reading "acceptance ceremony" as design acceptance only.
- *Smallest repair.* Add one clause to the proportional-gate paragraph: "the refactor is still disposed by its decision owner under ACTIVATION §3 Disposition; no design verdict is re-issued". The owner may instead state that no disposition is needed.

## Frame Observations (Non-Blocking)

The frames cite owning sections they do not carry:

- `dm-task-d` cites SPEC_METHOD §7 Bridge prohibition and ACTIVATION §4. It also cites ACTIVATION §6, where proportionality "decides which relations are material".
- `configuration` cites:
  - the admission and activation outcomes of ACTIVATION §3;
  - ACTIVATION §5 and §6, where §6 bounds what a context measurement includes;
  - EXECUTIVE_BASELINE §§5–13.

The runs disclosed these accurately under No method source. No required result depended on them: the operative bridge rule is in the carried text of UP-002, and both configuration runs measured the stated bytes and said that nothing else was measured. No frame-selection defect was found. Every frame carried the material its case's expectations needed.

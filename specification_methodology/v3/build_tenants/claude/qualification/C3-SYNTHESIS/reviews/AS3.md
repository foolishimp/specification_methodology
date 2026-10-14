# AS3: Assessment Of The Revision 2b Reruns Of C3S-01 Task B And C3S-03

Status: same-family working check, not acceptance. Commentary, not specification or design.

| Coordinate | Value |
|---|---|
| Assessor | AS3, a fresh Claude context. It wrote none of the frames, the oracles or the actor outputs |
| Subject commit | `cd9ec5e` on `tenant/claude/c3-synthesis`. The frames and cases are byte-identical to the run commit `48a0683`; between the two commits only run records and `returns/C6b.md` were added |
| Subject | four run outputs: C3S-01 Task B r3 and r4, C3S-03 r3 and r4 |
| Comparison basis | AS1's grading of C3S-01 Task B r1 and r2 and C3S-03 r1 and r2 (`reviews/AS1.md`) |
| Read first | each case's `EXPECTATIONS.md` and `CASE.md`, then `TASK-B.md` and `TASK.md`, then `runs/C3S-01/RUNS.md` and `runs/C3S-03/RUNS.md`, then the outputs |
| Frames read | `standards/frames/rf-task-b.md` and `standards/frames/traversal-task-f.md`, only to judge `No method source` and to attribute failures |
| Frame digests | the working-tree SHA-256 equals the digest logged in each run's `measured` event: `rf-task-b` `29a1d4a4…c090`, `traversal-task-f` `9e68f73d…331a`. The task, card and instrument digests also match RUNS.md |
| Repairs | none. This file is the only write; no git state was changed |

Paths are relative to `specification_methodology/v3/build_tenants/claude/`. Output line numbers are cited as `r3:NN`.

## How this check reads the oracles

The standards are AS1's, so the comparison holds.

- **R and E.** An unmet R expectation or a matched failure signature falsifies the run. An unmet E expectation is a recorded defect only.
- **Required core result.** It is reported apart from the run result. A run can reach every required core value and still be falsified.
- **Predicates (C3S-03 N9 and 5a-4).** A core value carries its predicate when the run states the predicate or names the constraint kind it evaluates, such as `occurrence_seed_complete`. Naming only a deciding law, such as AC-003 or AC-004, does not count. AS1 counted a bare deciding law as no predicate. AS1 did not face a run that named a constraint kind, because neither r1 nor r2 names one. This check adopts the rule and applies it to all four reruns. Only r4's occ-25 turns on it, and the rule changes no run result.
- **Coverage core values.** A status's core value is read against the coverage predicate that the run states at the top of its ledger. It is not read as an evaluation result, so `unknown (core indeterminate)` on E5 is no NB4 hit. AS1 accepted the same mapping in r1.
- **Conditional alternatives.** A value given under a counterfactual that the subject does not present is not the run's value. It is judged only for whether it is lawful under the frame.
- **B22 new identity.** The frame gives no new coordinate to a revision that changes no declaration (`rf-task-b.md` §10). The new-identity half of B22 is waived for such an action, as AS1 did. The proposal-and-adopter half is judged.

## Summary

| Run | Run result | Required core result reached | What falsifies it | E defects |
|---|---|---|---|---|
| C3S-01 B r3 | falsified | ledger and diagnosis yes; reopen list partial | B21: the F-C `satisfied` on E4 is kept closed | B11, B22 |
| C3S-01 B r4 | **not falsified** | yes: ledger, diagnosis and reopen list | none | B11, B22 |
| C3S-03 r3 | falsified | yes, all; occ-24 `partial_effect(not_attained)` → `falsified` | 5a-4 (no predicate for occ-23); N9 (no predicate for L-9, occ-23, occ-24, occ-25) | 2c |
| C3S-03 r4 | falsified | yes, all; occ-24 `partial_effect(not_attained)` → `falsified` | 5a-4 (no predicate for occ-23); N9 (occ-23) | 1d |

What the repairs changed:

- **Task B.** The reopen-nothing failure of r1 and r2 is gone in both reruns. Both reopen the out-of-family F-A result, E4's row and the tuple claim, and both cite the repaired ground: r3:106 "because it fails the exact applicability check"; r4:112 "It fails the exact applicability check." r4 is the first Task B run with no unmet R expectation. r3 still falls short on one item: it keeps the sibling F-C result closed.
- **C3S-03.** occ-24 moved from `indeterminate` (r1, r2) to `falsified` (r3, r4). The actors' reading of the error response did not change. All four runs say it does not establish that the effect ended (r1:31, r2:46, r3:57, r4:60). What changed is the frame: the end of the effect no longer enters the value, and both reruns put it in the residual (r3:60, r4:60). The predicate-recording failure (5a-4, N9) remains in both reruns.

---

## C3S-01 Task B (frame `rf-task-b`, `29a1d4a4…`)

### Task B r3

| Item | Judgement | Evidence |
|---|---|---|
| B1 (R) | satisfied | all 12 fields. Subject and basis, operation authority and decision authority are under "Fields common to all rows" (r3:7–10). Each row carries provenance, selected frames, actor envelope, semantic authority, evidence, dependencies, status and residual, plus a "Prior activation" line |
| B2 (R) | satisfied | "B is commit `9e1d2f44` with config rev 41, and T is 2026-10-11T12:00Z" (r3:5) |
| B3 (R) | satisfied | "**Operation authority:** none." (r3:9); "Tomas holds the release decision. No per-evaluation disposition owner is recorded for E1–E5 beyond that." (r3:10) |
| B4 (R) | satisfied | E4 "Semantic authority: missing. No owner of meaning is recorded." (r3:50); E5 "missing" (r3:61); E6 decision authority "For E6 it is unrecorded." (r3:10). Ari is kept as semantic authority only (r3:72) |
| B5 (R) | satisfied | E3 `conditionally_covered`: "The retry window is the changed item, so the result is invalid for reuse." (r3:40); "a re-evaluation on rev 41 would decide it" (r3:43) |
| B6 (R; E) | satisfied; satisfied | E1: "It was run on rev 39, so it is not evidence on rev 41." (r3:18); `conditionally_covered` (r3:20); "The evidence that would decide it is a replay on rev 41." (r3:21) |
| B7 (R) | satisfied | E2 `covered` on "F-B on schema revisions 7 and 8" (r3:25, 31); "The config change is not shown to touch schema compatibility." (r3:32) |
| B8 (R) | satisfied | `conflicted`. Both results are kept with source, count and time (r3:51). "a conjunction or decision rule is needed and none is declared" (r3:52). "The counterexample (12 messages in `dlq-shadow`) survives and is not discarded" (r3:54) |
| B9 (E) | satisfied | no rule (r3:52); "30 minutes apart … the subject does not say whether the dashboard covers `dlq-shadow`" (r3:51); F-A "outside the family" (r3:48) |
| B10 (R) | satisfied | E5 "Prior activation: none." "Evidence: none acquired." Status `unknown` (r3:57–64); not `covered` |
| B11 (E) | **falsified** | the E5 residual names capability, materiality and the harness (r3:65). INC-77 appears only as provenance and is not kept as an open input until a frame detects or excludes its recurrence |
| B12 (R) | satisfied | "Selected frames: none. No frame's family includes it." (r3:70); `uncovered`; "no cited authority excludes it" (r3:76) |
| B13 (E) | satisfied | "Whether E1 and E3 interact is not declared, and no conjunction, translation or composition for them is declared." (r3:19); E6 "authority coverage is not closed" (r3:76) |
| B14 (R) | satisfied | "operational full coverage is not met" (r3:78) |
| B15 (R) | satisfied | `conditionally_covered` and `unknown` → `indeterminate`; `conflicted` and `uncovered` → `falsified`; only `covered` → `satisfied` |
| B16 (R) | satisfied | question 1 first, from subject facts; "**Why I stopped:** question 1 locates the defect." (r3:97) |
| B17 (R) | satisfied | "No for the F-A activation on E4" (r3:90), by family inclusion (r3:91–95) |
| B18 (E) | satisfied | "reviewers expanding context without reaching a decidable question, and two actors using one frame name for different material relations" (r3:88) |
| B19 (R) | satisfied | "**Action:** clarify activation or evidence acquisition." (r3:101) |
| B20 (R) | satisfied | "the activation routing for E4 in the evaluation inventory … the recorded F-A activation on E4 is outside F-A's family" (r3:103). Follows the Q1 stop and adds no frame |
| B21 (R) | **falsified** | It reopens the F-A activation and result, E4's row and the tuple claim (r3:106–108), but: "**Preserved, not reopened by this action:** the F-C `satisfied` on E4, as an independent activation … If the 09:30Z log observation is admitted as evidence bearing on it, it reopens." (r3:110–111). The clarify row requires both E4 activations and their results. r3's own E4 row says "the subject does not say whether the dashboard covers `dlq-shadow`" (r3:51), so independence is not demonstrated. See AS3-1 |
| B22 (E) | **falsified** | no statement that the revision is a proposal and no adopting authority named. "No frame declaration changes, so there is no new frame revision coordinate" (r3:103) agrees with the frame, so the new-identity half is waived |
| NB1–NB6 | not hit | E3 and E1 `conditionally_covered` with the rev-39 binding stated; E4 two results, `conflicted`; E5 and E6 no evaluation result; no authority invented; diagnosis stops at Q1 |
| NB7 | not hit | the action reopens the F-A activation it reclassifies and changes no frame. The F-C omission is judged under B21 |
| NB8–NB10 | not hit | not declared adopted; no product change; E2 not staled |
| No method source | no private knowledge found | six items, including the status for a result bound to a superseded config coordinate (r3:119) and the E5 status (r3:120) |

### Task B r4

| Item | Judgement | Evidence |
|---|---|---|
| B1 (R) | satisfied | common fields (r4:5–8); per-row fields; E6 adds its own decision-authority line (r4:83) |
| B2 (R) | satisfied | "commit `9e1d2f44`, config rev 41, claim time 2026-10-11T12:00Z" (r4:6) |
| B3 (R) | satisfied | "**Operation authority:** none, because no evaluation performs a mutation." (r4:7); "**Decision authority:** Tomas for the release." (r4:8) |
| B4 (R) | satisfied | E4 "not recorded. The checklist item names no owner." (r4:52); E5 "not recorded" (r4:68); E6 "Tomas does not cover this. The SEC-3 decision owner is unrecorded." (r4:83) |
| B5 (R) | satisfied | E3 `conditionally_covered`: "the result is invalidated for reuse. It needs re-evaluation on rev 41." (r4:45) |
| B6 (R; E) | satisfied; satisfied | E1: "The closed result is bound to config rev 39" (r4:19); "invalidated for reuse until it is re-evaluated on rev 41 or a recorded re-check shows it independent of the change" (r4:20); `conditionally_covered` |
| B7 (R) | satisfied | E2 `covered`, "contract test of 2026-10-09 on schema revisions 7 and 8" (r4:28, 30). The rev-41 question is a residual and does not change the status (r4:33) |
| B8 (R) | satisfied | `conflicted`; both results with source, count and time (r4:54–55); "No decision rule is declared." (r4:56); "The 12-message observation is a counterexample and is not discarded." (r4:62) |
| B9 (E) | satisfied | combining rule missing (r4:60); `dlq-shadow` identity and the two times (r4:61); F-A outside its family (r4:62) |
| B10 (R) | satisfied | "Evidence: none; no frame was activated." (r4:69); `unknown`; "Nothing evaluates it now, so it is not covered." (r4:75) |
| B11 (E) | **falsified** | the residual names F-A capability and the harness (r4:73–76). INC-77 is not kept as an open input until detected or excluded |
| B12 (R) | satisfied | "Selected frames: none. No frame's family includes it." (r4:80); `uncovered`; "no authority is cited that excludes it" (r4:88) |
| B13 (E) | satisfied | "the retry-window and config seam shared with E3. No conjunction or composition for that seam is declared." (r4:16); E6 "authority coverage for this row is not closed" (r4:89) |
| B14 (R) | satisfied | "operational full coverage is not met for the tuple" (r4:92) |
| B15 (R) | satisfied | only `covered` → `satisfied` |
| B16 (R) | satisfied | question 1 first; "**Stopped at question 1** because its answer locates the defect" (r4:101) |
| B17 (R) | satisfied | "No, for the F-A activation on E4." (r4:96) |
| B18 (E) | satisfied | "The two actors were evaluating different material relations under one label." (r4:99); "That also explains the reviewers' repeated requests for a wider log window." (r4:101). The first signal is tied to the defect but not labelled a missing-frame signal |
| B19 (R) | satisfied | "**Action:** clarify activation or evidence acquisition." (r4:107) |
| B20 (R) | satisfied | "the activation record of E4 under F-A, and the E4 ledger row. It changes no frame declaration" (r4:109) |
| B21 (R) | satisfied | the F-A result on E4 (r4:112); "The E4 ledger row … and any coverage claim that consumed it. That includes the Coverage(W-notify, G, B, E, S, T) claim" (r4:113); "The F-C E4 result … is not shown by the subject to be independent of the 12-message observation … it is treated as reopened." (r4:114). The 12-message observation is kept (r4:62) |
| B22 (E) | **falsified** | "**Authority:** the action grants no authority. Tomas still owns the disposition of E4." (r4:120). This names E4's disposition owner, not the authority that adopts the revision, and the action is not presented as a proposal. The new-identity half is waived (r4:109) |
| NB1–NB10 | not hit | as r3; F-C is also reopened |
| No method source | no private knowledge found | lists the superseded-basis status gap (r4:126). It also notes that "REFERENCE_FRAME §13 is cited but not included" (r4:130); this is true of the frame (`rf-task-b.md:861` cites §13, and the frame has no §13) |

### Task B summary

- **Both reruns** get the ledger right on every row and stop the diagnosis at question 1, as r1 and r2 did. Both now reopen the out-of-family F-A result, E4's row and the tuple claim, and neither calls the action non-material.
- **r3 and r4 split on one point:** the F-C result on E4. r4 reopens it because its independence from the `dlq-shadow` observation is not shown. r3 keeps it closed "as an independent activation", although its own ledger records the same unknown.
- **Both** still miss B11. Both miss the proposal half of B22.

---

## C3S-03 (frame `traversal-task-f`, `9e68f73d…`)

### C3S-03 r3

| Item | Judgement | Evidence |
|---|---|---|
| 1a (R) | satisfied | "Timestamp, adjacency, a common subject and a shared actor do not create it." (r3:3) |
| 1b (R) | satisfied | "not an admitted cause edge. A projection mints no cause." (r3:4) |
| 1c (R) | satisfied | "a `RelationClaim` of kind `causally_precedes_event`. That claim needs claimant authority and evidence" (r3:5) |
| 1d (E) | satisfied | `claim_admission`, admitting event with `event_admission`, materialised relation, successor frontier, semantic cut with `semantic_cut_admission` (r3:6–10) |
| 1e (R) | satisfied | "Cause is not established." (r3:2); "I treat it as not admitted and as unresolved cause." (r3:14). No negation |
| 2a (R) | satisfied | "The operator's edit is not lawful. Admitted events are immutable" (r3:17) |
| 2b (R) | satisfied | the run keeps ev-103 unchanged and adds a new event linked by `corrects_event(new, ev-103)` (r3:21–22); "The successor frontier is the old members plus the new event once." (r3:23); "only through an explicit selection law" (r3:24). Note: "The corrected value is not given in the task, so I do not supply one." (r3:25). It does not take 41 as the corrected value; AS1 passed r1 and r2 without it |
| 2c (E) | **falsified** | the payload-digest break is named (r3:17–18). The frontier and projection identities that bind ev-103's content digest are not. This repeats r1's defect |
| 3a–3c (R) | satisfied | "`causally_precedes_occurrence` has source `Occurrence` and target `Occurrence`. Its source here is a `FrameworkEvent`" (r3:29); "AC-004 and the closed relation table decide" (r3:29); `refuse_wrong_type`, `refusal(constraint)`, `falsified`, `refused(constraint)` (r3:31–34) |
| 3d (E, optional) | not addressed | r3:36 names an event-to-event alternative "which still needs an admitted claim"; no N4 |
| 4a–4b (R) | satisfied | "comparison law, basis and admitting authority are explicit" (r3:41); "It may not create semantic, admission, causal or decision authority … therefore unlawful" (r3:42–43) |
| 4c (E) | satisfied | "the selection runs over a complete frontier" (r3:41); "also does not make that event a cause" (r3:44) |
| 5a-1 to 5a-3 (R) | satisfied | "Stop: `hold`, with residual `stale_frontier`" (r3:48); "Core member: `indeterminate`." (r3:49); "not `out_of_frame`" (r3:50) |
| 5a-4 (R) | **falsified** | the residual and the re-entry survive (r3:51); no predicate is stated for occ-23 |
| 5b-1 (R) | satisfied | "Stop: `partial_effect(not_attained)`." "Core member: `falsified`. Effects value: `not_effected`." (r3:53–54) |
| 5b-2 (R) | satisfied | the given value is `falsified`. `partial_effect(undecided)` appears only under "If a later completion could still meet the outcome" (r3:56), a case the subject's "defeats the intended outcome as a whole" excludes. r3 labels its reading "an assumption" (r3:55); see OF-5 |
| 5b-3 (R) | satisfied | "3 of 5 SKUs decremented and the rest unreached"; the `partial_effect` residual; "a bounded post-observation and an explicit disposition before any further effect" (r3:59–61) |
| 5b-4 (E) | satisfied | "`falsified` does not license treating the effect as absent, repeating it, or treating it as ended." (r3:63). It does not say that a retry is a fresh occurrence |
| 5c-1 (R) | satisfied | "Stop: `refusal(constraint)`. Core member: `falsified`." (r3:66–67), dangling under AC-003 (r3:65) |
| 5c-2 (R) | satisfied | "The occurrence is not admitted" (r3:68). `gap` → `invalid_basis` appears only for an external reference not yet evaluated (r3:69), which the frame supports and the subject does not present |
| 5c-3 (R) | satisfied | "the dangling `r-77` is the counterexample. Re-entry is a new complete occurrence candidate." (r3:68) |
| S1 (R) | satisfied | six parts in order |
| N1–N8 | not hit | |
| N9 | **hit** | no predicate for L-9 (r3:31–34, only the deciding law), occ-23 (r3:48–49), occ-24 (r3:53–54) or occ-25 (r3:66–67, only AC-003) |
| N10 | not hit, noted | "The error response is not evidence about the subject." (r3:57) extends the frame's lost-response rule (`traversal-task-f.md:1130`) to a received error response. It bears only on the residual (end not established), not on the value |

### C3S-03 r4

| Item | Judgement | Evidence |
|---|---|---|
| 1a–1b (R) | satisfied | "Timestamp, adjacency, a common subject, a shared actor and correlation create no cause … it is not an admitted material cause." (r4:5); "it has no admitted standing" (r4:13) |
| 1c (R) | satisfied | `RelationClaim` "with endpoints ev-101 to ev-102 … and a claimant with competent authority and evidence"; "`claim_admission` judgment of `admitted` over the current source frontier" (r4:8–9) |
| 1d (E) | **falsified** | claim, `claim_admission`, claim-admission event with `event_admission`, materialised relation and `semantic_cut_admission` (r4:8–11). The successor frontier, which r2 named, is missing |
| 1e (R) | satisfied | "Cause is not established. It is not `satisfied`." (r4:4); "`hold` plus `unresolved_cause`, which is `indeterminate`" (r4:6) |
| 2a–2b (R) | satisfied | "The edit is not lawful." (r4:18); new event with its own identity, `corrects_event(new, ev-103)`, a successor frontier, "ev-103 stays immutable and is not erased, rewritten or re-identified", explicit selection law (r4:21–25). Note: "The operator's 41 has no stated evidence." (r4:26) |
| 2c (E) | satisfied | "the frontier binds event content digests. Editing the content in place under the same id breaks the digest binding." (r4:19). Projection identities are not named; this meets AS1's r2 standard |
| 3a–3c (R) | satisfied | predicate "L-9 is a lawful `causally_precedes_occurrence` relation" (r4:30); AC-004 and the closed relation family (r4:33–34); "`refusal(constraint)`, which is `falsified`. The decision is `refused(constraint)`." (r4:36) |
| 3d (E, optional) | satisfied | "An event-to-occurrence cause would need a different lawful relation or claim, which the facts do not give." (r4:38) |
| 4a–4b (R) | satisfied | "comparison law, its basis and its admitting authority are explicit" (r4:44); "Gain semantic, admission, causal or decision authority … unlawful" (r4:45) |
| 4c (E) | satisfied | "over one complete, exact frontier" (r4:44); "The coordinate also creates no cause." (r4:45) |
| 5a-1 to 5a-3 (R) | satisfied | "occ-23: stop `hold`, core `indeterminate`." (r4:50); "not `out_of_frame`" (r4:51) |
| 5a-4 (R) | **falsified** | `stale_frontier` and its re-entry survive (r4:52–53); no predicate is stated for occ-23 |
| 5b-1 (R) | satisfied | "occ-24: stop `partial_effect(not_attained)`, core `falsified`." (r4:55); "The decision `partial(not_attained)` is also `falsified`." (r4:56) |
| 5b-2 (R) | satisfied | `undecided` only "If the outcome contract allowed later completion" (r4:57); see OF-5 |
| 5b-3 (R) | satisfied | "3 of 5 SKUs decremented and 2 not"; the `partial_effect` residual; "a bounded post-observation and an explicit disposition, with reconciliation under ACTIVATION §5 before any repetition" (r4:59–61) |
| 5b-4 (E) | satisfied | "`falsified` does not license treating the effect as absent, as ended or as safe to repeat." (r4:62) |
| 5c-1 to 5c-3 (R) | satisfied | "occ-25: stop `refusal(constraint)`, core `falsified`." (r4:63); "from `occurrence_admission` and `occurrence_seed_complete`" (r4:64); "`r-77` is the counterexample and must survive"; "Re-entry is a new complete occurrence candidate." (r4:65–66); `gap` / `invalid_basis` only for an external reference (r4:67) |
| S1 (R) | satisfied | six parts in order |
| N1–N8 | not hit | |
| N9 | **hit** | occ-23 has no predicate (r4:50–54). occ-25 names the constraint `occurrence_seed_complete`, which counts under the rule above |
| N10 | not hit, noted | "No method source: none". "An error response is not evidence the effect stopped." (r4:60) is the same extension as r3's and bears only on the residual. "nine-field qualifiers", `G_evt_cause` and `lineage_refs` are in the frame (`traversal-task-f.md:314`, `:905`, `:347`) |

### C3S-03 summary

- **Both reruns** reach every required core value. occ-24 is `partial_effect(not_attained)` → `falsified` with the end of the effect in the residual. L-9 and occ-25 are `refusal(constraint)` → `falsified`, and occ-23 is `hold` → `indeterminate`.
- **Both** omit the predicate for occ-23, so 5a-4 and N9 falsify both runs. r3 also omits the predicates for L-9, occ-24 and occ-25.
- **Both** label the `not_attained` reading "an assumption" and state the `undecided` branch as a counterfactual. See OF-5 and MT-7.

---

## Comparison with r1 and r2 (as AS1 graded them)

| Failure | r1 | r2 | r3 | r4 | Status |
|---|---|---|---|---|---|
| Task B B21 / NB7: the revision reopens nothing | hit | hit | — | — | **gone** |
| Task B B21: a sibling result of undemonstrated independence kept closed | (subsumed) | (subsumed) | **hit** | — | remains in r3, narrower |
| Task B B11 (E): INC-77 not kept as an open input | hit | hit | hit | hit | **remains**, 4 of 4 runs |
| Task B B22 (E): no proposal, no adopter | — | hit | hit | hit | **remains**, 3 of 4 runs |
| Task B "no rule gives the standing of an out-of-family result" (No method source) | listed | listed | — | — | **gone** as a listed gap |
| Task B "no status for a result bound to a superseded basis" (No method source) | listed | listed | listed | listed | **remains**, 4 of 4 runs; see MT-8 |
| C3S-03 5b-1, 5b-2, N7: occ-24 `indeterminate` | hit | hit | — | — | **gone** |
| C3S-03 5a-4: no predicate for occ-23 | — | hit | hit | hit | **remains** |
| C3S-03 N9: a core value with no predicate | hit | hit | hit | hit | **remains**, 4 of 4 runs |
| C3S-03 5c-3: occ-25 re-entry missing | hit | — | — | — | gone |
| C3S-03 2c (E): frontier binding not named | hit | — | hit | — | recurs in r3 |
| C3S-03 4c (E) | — | hit | — | — | gone |
| C3S-03 1d (E): chain incomplete | — | — | — | hit | **new** in r4 |

Net:

- **Task B.** The repaired §10 text was applied as written in both reruns. One run now passes every R expectation.
- **C3S-03.** The repaired partial-effect text was applied as written in both reruns. occ-24 is right in both. Both runs stay falsified, now only on predicate recording, which never turned on the repaired text.

## Attributions

The frames carry the member text verbatim on every item below. The clarification sentence is at `rf-task-b.md:841`–`:847`, from `REFERENCE_FRAME.md:888`–`:894`. The `partial_effect(not_attained)` cause is at `traversal-task-f.md:595`–`:606`, from `TRAVERSAL_OCCURRENCE.md:929`–`:940`. No failure traces to a missing or wrong frame copy.

| Id | Items | Attribution | Basis, and what would decide it |
|---|---|---|---|
| AS3-1 | B21 (B r3) | **unresolved**: actor application, method text or oracle | **For actor application:** the frame's clarification sentence preserves only a "demonstrably independent surviving result". r3 records that the subject does not say whether the dashboard covers `dlq-shadow` (r3:51), yet keeps F-C closed "as an independent activation". r4 reopened F-C on that same unknown. **For method text:** the clarification sentence names what it reopens (the out-of-family result and the rows and claims that consumed it) and what it preserves. It says nothing of a result that is neither. The rule "a result leaves that list only by a recorded re-check" is stated only for material revisions (`rf-task-b.md:815`–`:818`). The frame also still does not say whether an out-of-family activation's observations remain admissible evidence (MT-2), and r3's condition "If the 09:30Z log observation is admitted as evidence bearing on it" turns on exactly that. **For the oracle:** B21's clarify row requires both activations, which is more than the clarification sentence literally reaches. **What decides it:** an owner ruling on (a) whether an out-of-family activation's observations remain admissible evidence for the evaluation, and (b) whether, in a reopening without a material revision, a result whose independence is not shown by a recorded re-check is reopened. If both are yes, the cause is actor application and the member should say (b). If (b) is no, the oracle asks more than the member |
| AS3-2 | B11 (B r3, r4, E) | actor application (as AT-3) | The frame carries "Historical failures stay first-class coverage inputs until a declared frame detects or excludes their recurrence" (`rf-task-b.md:712`). The miss recurs in 4 of 4 runs, so the line is not salient for this actor class |
| AS3-3 | B22 (B r3, r4, E) | actor application (as AT-4) | The frame carries `revise … -> proposed_frame_set_delta` (`rf-task-b.md:489`) and the human frame-set authority (§4) |
| AS3-4 | 5a-4 and N9 (03 r3, r4) | actor application (as AT-11); card and task contributory | The frame carries "A result records its core value together with the predicate" (`traversal-task-f.md:1190`). The card asks for "the predicate it is for and its core value" for each result. The miss recurs in 4 of 4 runs. Task instruction 5 asks only for "the stop kind and its core result member", which invites omitting the predicate |
| AS3-5 | 2c (03 r3, E) | actor application (as AT-13) | The frame carries the frontier digest binding |
| AS3-6 | 1d (03 r4, E) | actor application | The frame carries the admission chain with the successor frontier. r4 names the successor frontier in its correction answer (r4:23) but not in the cause chain |

## Method-text findings

Each finding is a candidate for an owner ruling. None is a repair.

- **MT-1 (AS1): closed in use.** Neither rerun treats the clarification as reopening nothing. Both cite the exact-applicability ground. The law-table row "A non-material revision … reopens nothing" no longer appears in `REFERENCE_FRAME.md`.
- **MT-2 (AS1): narrowed, still open.** The frame now gives the out-of-family result's standing: it fails the exact applicability check and is reopened. Neither rerun lists the gap that r1 and r2 listed. The frame still does not say that the activation's observations remain admissible evidence. Both reruns kept the 12-message counterexample on their own, through the conjunction rule. r3's B21 condition shows the gap still acting. AS1's one-sentence repair still applies.
- **MT-3 (AS1): resolved for the value; a residue remains.** The end of the effect no longer decides the value, so the error-response question no longer moves any core value. The residue: the frame names a lost response as no evidence about the subject (`traversal-task-f.md:1130`) and says nothing about a received error response. All four actors extend the rule to it. This only decides whether the residual records the end as not established.
- **MT-7 (new, low). TRAVERSAL_OCCURRENCE `partial_effect(not_attained)` examples (`TRAVERSAL_OCCURRENCE.md:933`–`:935`).**
  - The examples are "the effect has ended short" and "an interval … has closed with only part reached". One involves the end the same paragraph excludes from the cause; the other needs a bounded interval.
  - No example covers an outcome that the part already done defeats whatever the rest of the effect does.
  - Both reruns reach `not_attained` only by an interpretation they label an assumption (r3:55, r4:57). r3 also lists it under No method source (r3:76). A subject worded less strongly would likely flip the value to `indeterminate`.
  - Smallest repair: add "or the outcome contract makes the part already done, or not done, defeat the outcome whatever the rest of the effect does".
- **MT-8 (new, recurring 4 of 4). REFERENCE_FRAME coverage status table.**
  - The finding: no status cause names a row whose capable frame holds a closed result invalidated for reuse by a changed material input (ACTIVATION §7).
  - All four Task B runs list this under No method source and choose `conditionally_covered`. That is an oracle-acceptable status, so nothing failed.
  - Smallest repair: add to the `conditionally_covered` cause "including a closed result invalidated for reuse under ACTIVATION §7 and not yet re-evaluated on B; the residual names the re-evaluation".
- **MT-9 (new, conditional on AS3-1).** If the owner rules (b) yes, then in the clarification sentence (`REFERENCE_FRAME.md:888`–`:894`), after "preserves every demonstrably independent surviving result", add: "a result whose independence no recorded re-check shows is reopened".

## Oracle and fixture observations

- **OF-1 (AS1): still live.** Both reruns map the conditional `gap` branch for occ-25 to `invalid_basis` (r3:69, r4:67), as the frame does. So 5c-1's `gap` alternative with `indeterminate` or `falsified` cannot be reached by a frame-following actor. Neither run chose `gap`.
- **OF-2 (AS1): no longer material.** B21's clarify row bases its tuple-claim entry on "since S or E changes". The repaired frame reaches the tuple claim by another route: claims that consumed the reopened result are reopened.
- **OF-3 (AS1): recurs.** Neither CASE.md held the revision 2b frame digests before launch (RUNS.md, "Pre-run frame record"). Both CASE.md "Runs and assessments" tables still read "none".
- **OF-5 (new).** occ-24's required `falsified` hinges on reading "the observed post-state defeats the intended outcome as a whole" as "no later completion can meet it". Both reruns make that reading but call it an assumption. The fixture could state directly that the outcome cannot be reached. Otherwise MT-7 covers it.
- **OF-6 (new, frame generation).** `rf-task-b` cites "the minimal shape is REFERENCE_FRAME §13" (`rf-task-b.md:861`) and does not carry §13. r4 noticed (r4:130). Task B asks for no result-shape check, so this did not matter here.

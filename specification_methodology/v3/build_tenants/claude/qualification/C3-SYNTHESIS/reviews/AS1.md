# AS1: Assessment Of The C3S-01 To C3S-04 Fresh-Actor Runs

Status: same-family working check, not acceptance. Commentary, not specification or design.

| Coordinate | Value |
|---|---|
| Assessor | AS1, a fresh Claude context. It wrote none of the frames, the oracles or the actor outputs |
| Subject commit | `735262d` on `tenant/claude/c3-synthesis` |
| Later commit, not reviewed | HEAD moved to `6eea724` during this review. Between the two commits only `LEDGER.md`, `reviews/AS2.md` and `reviews/RC12.md` changed, and none of them was read. `standards/`, `qualification/cases/` and `qualification/runs/` are byte-identical, so every `file:line` cited here holds at both commits |
| Subject | ten run outputs: C3S-01 Task A r1 and r2, C3S-01 Task B r1 and r2, and r1 and r2 of each of C3S-02, C3S-03 and C3S-04 |
| Read first | each case's `CASE.md` and `EXPECTATIONS.md`, then its `TASK*.md`, then `runs/C3S-0N/RUNS.md`, then the outputs |
| Frames read | `rf-task-a`, `rf-task-b`, `ac-task-a`, `traversal-task-f` and `eb-task-d`, read only to judge `No method source` and to attribute failures |
| Frame digests | the working-tree SHA-256 of each frame equals the digest that `RUNS.md` logged for its runs: `5ab7349c…`, `13d3bf4f…`, `8219354a…`, `78b43597…` and `e031c8e8…` |
| Repairs | none. This file is the only write |

Paths are relative to `specification_methodology/v3/build_tenants/claude/`.

## How this check reads the oracles

- **R and E.** An unmet R expectation or a matched failure signature falsifies the run. An unmet E expectation is a recorded defect only.
- **C3S-04 has no R/E markers.** I read each numbered item 1 to 18, and each row of its "Required core results" table, as R. Sub-items labelled "Expected" or "Optional" are read as E. Sub-items labelled "Acceptable" are permitted alternatives. A stated "Failure:" is read as a failure signature.
- **C3's four recorded ambiguities.** These are occ-25, Task B's E1 revision, the meaning of coverage status, and Task A's acceptable values (ledger 2026-10-13T20:52Z). The ledger names them without detail. They are carried as the oracles' stated alternatives:
  - occ-25: 5c-1;
  - Task B E1: B6;
  - coverage status: B10 and B15;
  - Task A: A12.

  Each alternative is honoured.
- **Sentence limits.** Where a task or oracle bounds a part to "at most three sentences" or "a one-sentence reason", I count terminal punctuation. Each bulleted item counts as a sentence. A limit exceeded is falsified even when the content is right. The tables below separate these format failures from failures of substance.
- **Required core result.** This is reported apart from the run result. A run can reach its required core values and still be falsified.

## Summary

| Run | Run result | Required core result reached | What falsifies it |
|---|---|---|---|
| C3S-01 A r1 | falsified | yes: E1 `indeterminate` | A16 (Claim K has 4 sentences) |
| C3S-01 A r2 | falsified | yes: E1 `indeterminate` | A16 (4 sentences) |
| C3S-01 B r1 | falsified | ledger and diagnosis yes; reopen list no | B21 and NB7: the revision reopens nothing |
| C3S-01 B r2 | falsified | ledger and diagnosis yes; reopen list no | B21 and NB7 |
| C3S-02 r1 | falsified | yes: `refusal`, `falsified` | P5 (Application too long), T10 (scope ground absent), J1 (judgment owner unlabelled), R2 (a grant offered as a cure) |
| C3S-02 r2 | falsified | yes: `refusal`, `falsified` | P5 (6 sentences), R3 (5 sentences) |
| C3S-03 r1 | falsified | no: occ-24 given `indeterminate`; L-9, occ-23 and occ-25 right | 5b-1, 5b-2, N7 (occ-24); 5c-3 (occ-25 survivors); N9 (core values with no predicate) |
| C3S-03 r2 | falsified | no: occ-24 given `indeterminate`; the rest right | 5b-1, 5b-2, N7; 5a-4 (no predicate for occ-23); N9 |
| C3S-04 r1 | falsified | yes, all five rows | 10 (priority reason has 3 sentences); 12 (no residual owner recorded) |
| C3S-04 r2 | falsified | yes, all five rows | 10 (2 sentences); 12 (no residual owner recorded) |

Four groups of failure, by cause:

1. **Sentence limits, 7 instances in 6 runs.** A16 in Task A r1 and r2; P5 in C3S-02 r1 and r2; R3 in C3S-02 r2; item 10 in C3S-04 r1 and r2. Every run whose task sets a sentence bound exceeds it. Task B and C3S-03 set no bound.
   - Task A r1 and r2 have no failure of substance.
   - C3S-02 r2 has none either. Its T5, N9 and N12 are indeterminate and do not change its result.
2. **Member text applied as written, 2 instances.** Task B r1 and r2 classify "clarify activation" as non-material and reopen nothing.
3. **occ-24, 2 instances.** Both C3S-03 runs read the warehouse error response as no evidence that the effect ended. So both return `partial_effect(unknown)`, which is `indeterminate`.
4. **Individual misapplication.** C3S-02 r1 (T10, J1, R2); C3S-03 r1 (5c-3); both C3S-03 runs (N9); r2 (5a-4). C3S-04 item 12 is a fifth case with unresolved cause.

---

## C3S-01 Task A (frame `rf-task-a`)

### Task A r1

| Item | Judgement | Evidence |
|---|---|---|
| A1 (R) | satisfied | Parts headed "# Part 1: Frame declaration", "# Part 2: Activation and evaluation result", "# Claim K", "# No method source"; no product recommendation |
| A2 (R) | satisfied | All 12 sections of the frame's minimal declaration are present; gaps are written, e.g. "## Capability Envelope / Missing." |
| A3 (R) | satisfied | "Predicate for E1: on build `b-120`, the trailer count equals the source table's row count at export time … Closed result algebra: the five core values" |
| A4 (R) | satisfied | "Source commit `c0ffee12` … `export.yaml` revision 14 … read from a read replica since 2026-10-09 (lag up to 30 s) … 2026-10-11T16:00Z" |
| A5 (R) | satisfied | "D-3: read transaction, then streaming of rows, then a separate `SELECT COUNT(*)`"; "The data source (primary versus replica) and replica lag" |
| A6 (R) | satisfied | "Equal service name, file name or "the tests pass" does not equate `b-118` with `b-120`"; V1 "a 25-row fixture, with no replica" |
| A7 (R) | satisfied | "Frame-set authority: not stated. Evaluation authority: no role is named"; result: "operation = none (read-only); decision = Mara" |
| A8 (R) | satisfied | "Missing. The subject names no actor, tools, access or independence conditions." The added "Read-only inspection … is assumed" is labelled as an assumption |
| A9 (E) | **falsified** | V1 is listed under "Admissible, by provenance and subject" with "binds a different build". It is not stated as excluded for E1. V2's build is marked unstated |
| A10 (E) | satisfied | "A new build or commit. A configuration revision change from 14. A change in the replica, its lag or the isolation level. A change to the meaning of R-3. New evidence on `b-120`." |
| A11 (R) | satisfied | "V1 passes on `b-118` … does not bind `b-120` … V2 … build is not stated and no source count was recorded … D-3 is design intent … No counterexample is on file" |
| A12 (R) | satisfied | "result: indeterminate" |
| A13 (R) | satisfied | one value in `result` |
| A14 (R) | satisfied | the residual field covers the V2 build, the snapshot and the isolation level; the out_of_frame field says "Row count at export time" is undefined under replica lag (owner: Mara); "E2 and E3 have no results here" |
| A15 (E) | satisfied | frame identity, activation label ("my label; the subject names none"), evidence, invalidation and "consuming decision or conjunction: claim K (Mara's release decision)" |
| A16 (R) | **falsified** | Four sentences: "My result is …" / "It does not establish …" / "It says nothing about "ready to ship" …" / "Mara disposes claim K …". The content bullets are all present |
| A17 (E) | satisfied | K is a consumer, not evidence: "Consumer: claim K (Mara)" |
| NA1–NA4 | not hit | no `satisfied`, no `falsified`, V1 not used for `b-120`, V2 not bound |
| NA5 | not hit | no invented digest, count, isolation level or authority; the envelope assumption is labelled |
| NA6 | not hit | "this activation therefore holds only if the assigning authority admits the evaluator" |
| NA7–NA9 | not hit | one core value; no `invalid_basis`; no recommendation |
| No method source | no private knowledge found | every determination applied (RF-005, `activated_frame`, the dual-ground rule, acceptance as a separate result) is in the frame |

### Task A r2

| Item | Judgement | Evidence |
|---|---|---|
| A1 (R) | satisfied | "## 1. Frame declaration", "## 2. Activation and evaluation result", "## Claim K", "## No method source" |
| A2 (R) | satisfied | all 12 sections; "Missing: the database engine and isolation level; the replica's identity …" |
| A3 (R) | satisfied | "Predicate: "the trailer count equals the source table's row count at export time, on the exact basis below." Result algebra: the core algebra …, unrefined." |
| A4 (R) | satisfied | build `b-120`, commit `c0ffee12`, `exporter.py` digest, r14, replica with up to 30 s lag, the claim time |
| A5 (R) | satisfied | "the streamed rows; the `SELECT COUNT(*)` … `ledger_rows` on the primary and on the replica; replica lag"; "Topology coordinate: reads come from the replica" |
| A6 (R) | satisfied | "Build labels and file names do not establish equality"; "Prohibited assumptions: … that replica state equals primary state" |
| A7 (R) | satisfied | "Frame-set authority: not stated … Evaluation authority: not stated in the subject"; in the result, "admitted only by this task's assignment, with the assigner not identified", which names no role and records the assigner as missing |
| A8 (R) | satisfied | "Needed: read the supplied record … Not stated: the actor's tools, access and context capacity" |
| A9 (E) | satisfied | "Excluded: any claim that V1 covers `b-120` (that is E2's question) … any inferred build for V2" |
| A10 (E) | satisfied | "A new commit or build … A change to `export.yaml` from r14. A topology change … A new or revised meaning of R-3 … New evidence" |
| A11 (R) | satisfied | "No evidence pairs a `b-120` trailer with an independently recorded source count … neither establishes the predicate nor yields a counterexample" |
| A12 (R) | satisfied | "result: `indeterminate`. Predicate: …" |
| A13 (R) | satisfied | one value |
| A14 (R) | satisfied | the V2 build; isolation; "the effect of replica lag, which is E3's question"; "applicability of V1 … E2's question"; "declared meaning of 'source table's row count at export time' … Owner: Mara" |
| A15 (E) | satisfied | all fields filled; "consuming decision or conjunction: Mara's disposition of claim K" |
| A16 (R) | **falsified** | Four sentences: "The result says `indeterminate` …" / "It does not assess "ready to ship" …" / "Mara disposes claim K as the decision authority." / "This result is evidence for her and is not a disposition." The content is complete |
| A17 (E) | satisfied | "Output: the closed E1 result, to Mara's disposition of claim K" |
| NA1–NA9 | not hit | as for r1; NA6 is not hit because the evaluation is tied to the task's assignment and the assigner is marked unidentified |
| No method source | no private knowledge found | |

### Task A summary

- **Both runs** reach `indeterminate` with a complete inference relation, keep the authorities apart, and invent nothing. Both are falsified only by A16's three-sentence bound.
- **r1** also files V1 as admissible instead of excluded, an E defect.
- **The out_of_frame residual field.** Outside the oracle, both runs put an `out_of_frame` ground into this field under an `indeterminate` result: r1 "`out_of_frame` also has a lawful ground here"; r2 "Missing relation: the declared meaning …". The frame's field note says the field "reads `none` for any other result". See MT-5.
- **Activation with evaluation authority unrecorded.** Both runs return `activated_frame` while the evaluation authority is not recorded, and both list the question under `No method source`. See MT-4.

---

## C3S-01 Task B (frame `rf-task-b`)

### Task B r1

| Item | Judgement | Evidence |
|---|---|---|
| B1 (R) | satisfied | 12 fields. Subject and basis, and operation authority, are stated once under "Fields common to every row"; per-row bases are in Evidence |
| B2 (R) | satisfied | "Commit `9e1d2f44` with config rev 41 at 2026-10-11T12:00Z is declared and current" |
| B3 (R) | satisfied | "Operation authority: none." as a common field; "Decision authority: Tomas" on E1–E5 |
| B4 (R) | satisfied | E4 "Semantic authority: not recorded."; E5 "Semantic authority: missing."; E6 "Decision authority: not recorded." |
| B5 (R) | satisfied | E3 `conditionally_covered`: "The retry policy is the very thing rev 41 changed, so that result is invalid for reuse." |
| B6 (R; E) | satisfied; satisfied | E1 `conditionally_covered`: "a 10,000-event replay … bound config rev 39 … not reusable (RF-005, ACTIVATION §7)" |
| B7 (R) | satisfied | E2 `covered`, "a contract test of 2026-10-09 on schema revisions 7 and 8" |
| B8 (R) | satisfied | E4 `conflicted`: both results kept with frame, source, count and time; "the counterexample from F-A survives" |
| B9 (E) | satisfied | no combining rule (Dependencies); `dlq-shadow` question (Semantic authority); F-A family (Residual); times (Evidence: "Their age against T … not in the subject"). Weak point: the two times are listed but not named as a cause of the conflict |
| B10 (R) | satisfied | E5 `uncovered`; "No frame was activated"; the statuses are "a result of `audit_coverage` only, never of the evaluation itself" |
| B11 (E) | **falsified** | E5 residual: "no capable frame is shown, so the absence is the counterexample". INC-77 is not kept as an open input until a frame detects or excludes its recurrence |
| B12 (R) | satisfied | E6 `uncovered`; "`excluded_by_authority` is unavailable" |
| B13 (E) | satisfied | "shares config rev with E3. The retry–duplicate interaction has no declared conjunction"; E6 "authority coverage is not closed" |
| B14 (R) | satisfied | "operational full coverage is not met" |
| B15 (R) | satisfied | `conflicted` → `falsified`, `conditionally_covered` → `indeterminate`, `uncovered` → `falsified`; none → `satisfied` |
| B16 (R) | satisfied | Q1 answered first, with the reason for stopping |
| B17 (R) | satisfied | "F-A on E4: no … **I stop at question 1.**" |
| B18 (E) | satisfied | "Reviewers expanded context twice …"; "Two actors used the same frame name, "delivery" …" |
| B19 (R) | satisfied | "**Action:** clarify activation." The F-A widening is a conditional alternative and is not chosen |
| B20 (R) | satisfied | names E4's activation ("E4 is activated only in F-C, and F-A's activation on E4 is withdrawn as out of family"), follows the Q1 stop, adds no frame. It states "No frame declaration and no inventory entry changes" |
| B21 (R) | **falsified** | "It … produces no new revision coordinate and reopens nothing … **Reopens:** no prior activations, results or coverage claims." |
| B22 (E) | satisfied | "This is a proposed delta only. The frame-set authority, Tomas, accepts or rejects it". No new identity is due for an action the member calls non-material; see the B21 attribution |
| NB1–NB6 | not hit | E3 is not covered; E4 is kept as two results; E1 has its rev-39 note; E5 and E6 have no evaluation result; no authority is invented; the diagnosis stops at Q1 |
| NB7 | **hit** | "Reopens: no prior activations, results or coverage claims." The F-A activation on E4, its result, E4's row and the tuple claim are not reopened |
| NB8–NB10 | not hit | proposal only; no product change; E2 is not staled |
| No method source | no private knowledge found | five gaps listed, including "No rule gives the standing of a result from an activation outside the frame's family" |

### Task B r2

| Item | Judgement | Evidence |
|---|---|---|
| B1 (R) | satisfied | all 12 fields on every row |
| B2 (R) | satisfied | "B names config rev 41 as current, so the audit assigns statuses" |
| B3 (R) | satisfied | "Operation authority: none." on each row; Tomas on E1–E5 (E5: "by the stated release decision. The subject does not say that this extends to E5") |
| B4 (R) | satisfied | E4 "Semantic authority: missing. The owner of checklist item 7 is not recorded."; E5 "missing"; E6 "Decision authority: missing" |
| B5 (R) | satisfied | E3 `conditionally_covered`: "invalid for reuse until it is re-evaluated on rev 41 or re-checked as demonstrably independent" |
| B6 (R; E) | satisfied; satisfied | E1 `conditionally_covered`: "The closed result is bound to config rev 39 and is a mismatched coordinate (RF-005)" |
| B7 (R) | satisfied | E2 `covered`, schema revisions 7 and 8 |
| B8 (R) | satisfied | `conflicted`; both results kept; "The F-A counterexample survives any join" |
| B9 (E) | satisfied | different times and "'Before release' has no stated time"; no combination rule; `dlq-shadow`; F-A outside its family |
| B10 (R) | satisfied | "No result exists, and the row is not an `indeterminate` component." |
| B11 (E) | **falsified** | E5 residual: "No result exists. No cited authority excludes it. Whether F-A could evaluate it is not declared." INC-77 is not kept as an open input |
| B12 (R) | satisfied | E6 `uncovered`; "No authority excludes it." |
| B13 (E) | satisfied | "The E3 retry policy is related, but no relation is declared"; E6 "authority coverage is not closed" |
| B14 (R) | satisfied | "Any conjunction over G is therefore never `satisfied`" |
| B15 (R) | satisfied | no status maps to `satisfied` except `covered` |
| B16–B18 | satisfied | "Was the correct declared frame activated? **No.** … I stopped at question 1"; both signals named |
| B19 (R) | satisfied | "**Action:** clarify activation." |
| B20 (R) | satisfied | "Bind E4 to F-C as the in-family activation. Record F-A's activation on E4 as out of family." |
| B21 (R) | **falsified** | "Prior activations: none … Results: none. A non-material revision … reopens no result … Coverage claims: the E4 row stays `conflicted`" |
| B22 (E) | **falsified** | no statement that the revision is a proposal, and no adopting authority named |
| NB7 | **hit** | as B21 |
| NB1–NB6, NB8–NB10 | not hit | as r1; the action is not declared adopted |
| No method source | no private knowledge found | |

### Task B summary

- **What both runs get right.** The ledger is right on every row: E1 and E3 are `conditionally_covered` because of the revision-39 binding, E2 `covered`, E4 `conflicted` with both results kept, E5 and E6 `uncovered` with no evaluation result. Both stop the diagnosis at question 1, the oracle's preferred stop.
- **Shared falsification.** Both choose "clarify activation", call it non-material and reopen nothing. Both also list the correct reopen set for a material widening of F-A. This shows they know the rule and applied the member's non-material carve-out deliberately. See attribution AT-2 and MT-1.

---

## C3S-02 (frame `ac-task-a`)

### C3S-02 r1

| Item | Judgement | Evidence |
|---|---|---|
| T1 (R) | satisfied | all 24 fields, plus an "UNCLASSIFIED: RES-4" line |
| T2 (R) | satisfied | traversal, context, owner, scope, basis, "G-88 (issued by Ravi). It permits … and does not permit edits to requirement, latitude or residual records", evidence `RN-31`, provenance, stop contract |
| T3 (R) | satisfied | "M-billing@r3 — exact content identity MISSING"; codomain "sha256:7d…e9 (elided …)"; calc-1 and sig-billing-1 are in the basis field |
| T4 (R) | satisfied | preserved {REQ-12, LAT-12a}; introduced {DES-12.1}; RES-4 "cannot be preserved … cannot be removed … cannot be introduced … the local delta … does not close" |
| T5 (R) | satisfied | external_preserved holds the tuple; ∅ for introduced and removed; "one witness for that coordinate, with decision: equal" |
| T6 (E) | satisfied | "The witness's own evidence identity is MISSING; only the resolution's evidence EV-iso-pin-2 is given." |
| T7 (E) | satisfied | "MISSING (no typed equality relation is named). REQ-12 and LAT-12a are covered by byte identity under cj-1 instead." |
| T8 (R) | satisfied | "RES-4 remains in the successor but is modified. No authorised disposition is on file (AC-009)." |
| T9 (R) | satisfied | `id`, `preconditions`, `invalidation` and `re_entry` are MISSING |
| T10 (R) | **falsified** | The operation-authority ground is stated: "went beyond grant G-88, which excludes residual edits". Missing anywhere in the output: the traversal-scope ground (design records only), RES-4's owner set against Tomas, and the broader-coordinate refusal |
| T11 (E) | satisfied | "REQ-12 is unchanged, so that stop is not triggered." |
| P1 (R) | satisfied | `refusal(constraint)` on the RES-4 delta and the G-88 grounds |
| P2 (E) | **falsified** | T3 is not named as a ground: "This is a demonstrated violation, not a basis condition." |
| P3 (R) | satisfied | "No `M_b_prime*` is established as a lawful proposed successor." |
| P4 (R) | satisfied | "maps to `falsified` for the predicate "the operation yields its declared result on the exact basis"" |
| P5 (R) | **falsified** | six sentences, counting each item of its two-item list: "The record supports …" / "The counterexamples are: …" / "No `M_b_prime*` is established …" / "This is a demonstrated violation …" |
| J1 (R) | **falsified** | "owner: Nadia" is given with no derivation label, and the subject names no judgment owner. Every other field is per the oracle |
| J2 (R) | satisfied | "It says nothing about the transformation or about admission or acceptance." |
| J3 (R) | satisfied | scope: "The modified RES-4 and the lawfulness of the r3→r4 step are not examined"; Promotion: "it does not cure the refusal" |
| J4 (E) | satisfied | "satisfied for the predicate "DES-12.1 conforms to REQ-12 within LAT-12a"" |
| J5 (E) | satisfied | RES-4 is not examined by the judgment; "RES-4's own re_entry (Requirements) is carried unchanged" |
| J6 (E, optional) | not addressed | |
| R1 (R) | satisfied | "explicit relation between the unchanged r4 and an admission or acceptance judgment, and Ravi holds acceptance authority" |
| R2 (R) | **falsified** | "RES-4 must be dispositioned … or its change must be made under an operation grant that covers residual edits". A grant cannot cure the same-identity change: AC-013's closed delta still fails, and AC-009 still needs a disposition |
| R3 (R) | satisfied | three sentences |
| N1–N9, N11 | not hit | |
| N10 | not hit | Ravi is named only as G-88's issuer, and "whether a new grant can cover it after the fact" is listed as open |
| N12 | not hit | the independence question is listed: "The METHOD block gives no independence rule." |

### C3S-02 r2

| Item | Judgement | Evidence |
|---|---|---|
| T1 (R) | satisfied | all 24 fields |
| T2 (R) | satisfied | all coordinates; provenance "performed by Tomas on 2026-10-11. Nothing further is stated." |
| T3 (R) | satisfied | "Basis calc-1, signature sig-billing-1, source basis 4a1f9e20, grammar cj-1 … MISSING: the exact model content identity (digest) of r3." |
| T4 (R) | satisfied | "UNCLASSIFIABLE: RES-4 … The closed local delta … cannot be proven." |
| T5 (R) | indeterminate | "one is required for the preserved tuple (decision: equal, both tuples field-equal) … but no witness record is on file. MISSING: the witness evidence identity." This reads either as a witness written with its evidence missing, or as no witness. It is decided by whether `t` is read to contain the witness |
| T6 (E) | satisfied | "EV-iso-pin-2 is the resolution evidence, not stated as witness evidence." |
| T7 (E) | satisfied | "MISSING. No typed equality relation is named. The only available proof is byte-identity under cj-1 (alternative 1)." |
| T8 (R) | satisfied | "RES-4 carries on in r4 with an edited consequence. No authorised disposition is on file." |
| T9 (R) | satisfied | the four fields are MISSING; "RES-4's own re_entry is Requirements, but that belongs to the residual, not to t" |
| T10 (R) | satisfied | "G-88 and the traversal scope (design records) do not cover it. The edit is therefore outside `operation_authority` and `scope`" |
| T11 (E) | satisfied | "On the stated facts REQ-12 is unchanged, so this stop is not shown triggered." |
| P1 (R) | satisfied | "fits none of preserved, removed or introduced, and the edit exceeds G-88 and the traversal scope" |
| P2 (E) | satisfied | the missing r3 digest is reported as a basis condition; the AC-009 breach is under "Defects that bear on the record" |
| P3 (R) | satisfied | "r4 is not available as a lawful proposed successor" |
| P4 (R) | satisfied | `falsified` with the predicate. The separate `invalid_basis` is reported beside it under AC-007's rule and answers another predicate |
| P5 (R) | **falsified** | six sentences: "The record supports …" / "The counterexample is RES-4." / "It is edited, …" / "Because of this, …" / "The missing r3 content digest …" / "They are reported beside it …" |
| J1 (R) | satisfied | "owner: MISSING (Nadia is the evaluator …)"; "basis: 4a1f9e20 (the subject's basis). The judgment's own basis binding is not stated" |
| J2–J3 (R) | satisfied | "This is not a judgment of the transformation's lawfulness, of the RES-4 edit, or of acceptance. It leaves r4 unchanged." |
| J4–J5 (E) | satisfied | "This is core value satisfied, for that predicate only"; "It states no result for the RES-4 credit-note question, which DES-12.1 assumes away." |
| J6 (E, optional) | partly | "the build is b-40" |
| R1 (R) | satisfied | "an admission or acceptance judgment by Ravi … Nadia's evaluation judgment cannot stand in for it." |
| R2 (R) | satisfied | "Either RES-4 is restored byte-identical, or its change is an authorised disposition by competent authority … The missing coordinates must also be supplied" |
| R3 (R) | **falsified** | five sentences: "Promoting r4 needs …" / "Nadia's evaluation judgment …" / "Before that, …" / "Either RES-4 …" / "The missing coordinates …" |
| N9 | indeterminate | as T5 |
| N12 | indeterminate | "`RN-31` is also the step's own evidence, so the two are not independent on that item." The frame has no independence rule and the point is not listed. It may be plain reading of shared evidence rather than method knowledge; it changes no value |
| N1–N8, N10, N11 | not hit | |

### C3S-02 summary

Both runs reach the required core result: `refusal(constraint)`, which is `falsified`, with RES-4 unclassifiable under the closed delta.

- **r1** misses the scope ground (T10). It denies that the missing r3 identity is a basis condition (P2), although the frame's AC-007 lists one. It gives the judgment's owner without a derivation label (J1). And it offers a widened grant as a cure (R2).
- **r2** is substantively right. It fails only on the two sentence limits. T5, N9 and N12 are indeterminate (T5 and N9 share one cause), and none of them changes its result.
- **Outside the oracle.** r2 also calls the missing `preservation_relation` a basis condition, although AC-013 makes canonical-byte equality under `cj-1` an alternative proof. This is a minor over-reach that changes no graded value.

---

## C3S-03 (frame `traversal-task-f`)

### C3S-03 r1

| Item | Judgement | Evidence |
|---|---|---|
| 1a (R) | satisfied | "Timestamp, adjacency, a shared subject, a shared actor and correlation do not create cause." |
| 1b (R) | satisfied | "The projection's `causally_precedes_event(ev-101, ev-102)` therefore has no admitted basis … The recorded edge is not an admitted relation." |
| 1c (R) | satisfied | "a `RelationClaim` of kind `causally_precedes_event`. It needs claimant authority and evidence, a `claim_admission` judgment of `admitted`, an admitted claim-admission event …" |
| 1d (E) | satisfied | item 1 names the judgment, the event and the semantic cut; item 2 lists the cut's members, including "the materialised `corrects_event` … the successor frontier, and `j_a`" |
| 1e (R) | satisfied | "Cause is not established"; "the claim judgment was not performed. It has no closed result". Nothing negates the cause |
| 2a (R) | satisfied | "The operator's edit is not lawful. Events are immutable" |
| 2b (R) | satisfied, with a defect | a new event through the full cut, `corrects_event(new, ev-103)`, "Both events stay", a selection law, and ev-103 "restored to its admitted content". Defect: "The value the correction carries (14 or another) is not stated" names the miscount, 14, as a possible correction value |
| 2c (E) | **falsified** | the payload-digest break is named; frontier and projection identities are not |
| 3a–3c (R) | satisfied | "`causally_precedes_occurrence` requires an `Occurrence` source … AC-004 relation typing and the closed relation-families table decide this … `refusal(constraint)`, which maps to falsified" |
| 3d (E, optional) | satisfied | "an event-to-occurrence cause has no declared kind" |
| 4a–4b (R) | satisfied | "may order eligible facts … explicit, with its comparison law, basis and admitting authority"; "gains no semantic, admission, causal or decision authority. So it may not decide whether a pending reorder is approved." |
| 4c (E) | satisfied | "It also may not create cause"; "it must act over a complete frontier" |
| 5a-1 to 5a-3 (R) | satisfied | "the stop is `hold`, which is `indeterminate`"; "It is not `out_of_frame`" |
| 5a-4 (R) | satisfied | predicate "the application can reach its declared result on the exact basis"; `stale_frontier`; re-entry "construct a new exact frontier and projection" |
| 5b-1 (R) | **falsified** | "So I read it as `partial_effect(unknown)`, which is `indeterminate`." |
| 5b-2 (R) | **falsified** | `indeterminate` is given, and the oracle excludes it |
| 5b-3 (R) | satisfied | "the `partial_effect` residual and the dispatched invocation … 3 of 5 SKUs decremented … the bounded post-observation … explicit disposition and re-entry before any further effect" |
| 5b-4 (E) | satisfied | "It must not be treated as absent or as complete". It does not say that a retry is a fresh occurrence |
| 5c-1 (R) | satisfied | "the stop is `refusal(constraint)`, which is `falsified` … dangling, which refuses under AC-003" |
| 5c-2 (R) | satisfied | "The refusal names no basis condition"; "no occurrence identity is minted". The `gap` remark covers only a counterfactual external reference |
| 5c-3 (R) | **falsified** | `r-77` and its cause survive ("The dangling ref r-77 is the counterexample. It survives …"). No re-entry is stated, and nothing says the candidate stays unrepaired |
| S1 (R) | satisfied | six parts in order |
| N1–N6, N8 | not hit | |
| N7 | **hit** | occ-24 is given `indeterminate` |
| N9 | **hit** | core values with no predicate: ev-103 "`refusal(constraint)`, which maps to falsified"; L-9 "The stop is `refusal(constraint)`, which maps to falsified"; occ-25 "the stop is `refusal(constraint)`, which is `falsified`" |
| N10 | not hit | "an error response is not evidence that it ended" applies the frame's evidence standard for the end of an effect. It is counted under 5b-1, not as private knowledge |

### C3S-03 r2

| Item | Judgement | Evidence |
|---|---|---|
| 1a–1c (R) | satisfied | "Cause arises only from an admitted causal claim …"; "The projection's `causally_precedes_event` edge therefore carries no cause"; five steps to establish it |
| 1d (E) | satisfied | claim, `claim_admission`, claim-admission event with `event_admission`, "Materialize the relation", semantic cut and successor frontier |
| 1e (R) | satisfied | "Until then the residual is `unresolved_cause`." |
| 2a–2b (R) | satisfied | "An admitted event is immutable"; "`ev-103` stays as observed (14), and the new event carries the corrected reading"; `corrects_event`; new frontier; selection law |
| 2c (E) | satisfied | "frontier identity binds event content digests"; "its identity binds its payload digest" |
| 3a–3c (R) | satisfied | "typed `Occurrence → Occurrence` … AC-004 … and the closed relation families table … Stop: `refusal(constraint)`. Core: `falsified`" |
| 3d (E, optional) | not addressed | |
| 4a–4b (R) | satisfied | "may order eligible facts … comparison law, basis and admitting authority"; "the greatest `observed_at` cannot serve as the approval decision" |
| 4c (E) | **falsified** | "It also cannot create cause" is stated. Selection over an exact frontier is not |
| 5a-1 to 5a-3 (R) | satisfied | "Stop `hold`. Core `indeterminate`." "It is not `out_of_frame`" |
| 5a-4 (R) | **falsified** | `stale_frontier` and its re-entry survive; no predicate is stated for occ-23 |
| 5b-1 (R) | **falsified** | "Stop `partial_effect`, refined as `partial_effect(unknown)`. Core `indeterminate`." |
| 5b-2 (R) | **falsified** | `indeterminate` is given |
| 5b-3 (R) | satisfied | "the `partial_effect` residual survives. So do the fact that 3 of 5 SKUs were decremented, and the mandatory re-entry … a bounded post-observation and an explicit disposition" |
| 5b-4 (E) | satisfied | "never treated as absent or complete, and it is not retried blindly" |
| 5c-1 to 5c-2 (R) | satisfied | "Stop `refusal(constraint)`. Core `falsified`, with `r-77` as the counterexample. The occurrence is not admitted and its identity is not minted." |
| 5c-3 (R) | satisfied | "The dangling reference, the refusal … must survive. Re-entry is a new complete occurrence candidate." |
| S1 (R) | satisfied | |
| N7 | **hit** | occ-24 is given `indeterminate` |
| N9 | **hit** | no predicate for L-9 ("Stop: `refusal(constraint)`. Core: `falsified`"), occ-23 ("Stop `hold`. Core `indeterminate`.") or occ-25 |
| N1–N6, N8, N10 | not hit | |

### C3S-03 summary

- **Both runs** decide L-9, occ-23 and occ-25 as the oracle requires. Both hold correction-without-erasure and precedence-without-authority. Both state predicates for some core values and omit them for others (N9).
- **Shared falsification.** Both read occ-24 as `partial_effect(unknown)`, which is `indeterminate`. Their reason: "an error response is not evidence that it ended". Each gives `partial_effect(ended)`, which is `falsified`, only as the conditional case. See AT-10 and MT-3.
- **r1** also omits occ-25's re-entry.

---

## C3S-04 (frame `eb-task-d`)

The runs used `qualification/cases/C3S-CARD.md`, while CASE.md names `F-02/CARD.md`. The ledger records the variance at 2026-10-13T22:46Z.

### C3S-04 r1

| Item | Judgement | Evidence |
|---|---|---|
| 1 | satisfied | "Outcome lock: holds. The 1.2 mandate …, the severity and priority scales, the decision cutoff and the hard stop are unchanged." |
| 2 | satisfied | "Basis lock: fails … meets `RR-9`'s own invalidation condition … Result: `invalid_basis`." |
| 3 | satisfied | "Product-role lock: holds on the stated facts." |
| 4 | satisfied | "Authority lock: holds. Priya changed r42 under her configuration authority." |
| 5 | satisfied | "Coverage-and-return lock: fails … Each stale result is a planned assessment without an applicable closed result, so the composite is at best `indeterminate` and cannot be `satisfied`." |
| 6 | satisfied | "`WR-31` is `candidate_ready`, whose core value is `satisfied` … Only that an exact candidate … exist. It is not an assessment and not acceptance." |
| 7 | satisfied | "`EC-77` requires it … Ada's self-review is Worker evidence and cannot be relabelled as independent." |
| 8 | satisfied | "All of it is bound to r41 … the green results are not valid for the current basis"; "Aggregate green status cannot stand in for them." |
| 9 | satisfied | "Severity: high. Hana (Reviewer) sets it" |
| 10 | **falsified** | P2, set by Omar, is acceptable. The reason runs three sentences: "The leak needs `autofill_v2` on …" / "A workaround exists …" / "It is still a real privacy defect …" |
| 11 | satisfied | "Frame result: `falsified`. Hana set it … I cannot consume it on the current basis. I preserve it as the original ruling" |
| 12 | **falsified** | No block, set by Omar under Jules's cutoff, with no hard stop ("an address is not a card number"). But no owner is recorded: "recorded as an explicit residual with an owner", while `No method source` says "The owner of the F-1 residual. I cannot invent one". The failure "recording no owner" is matched |
| 13 | satisfied | four separate entries, each with its setter |
| 14 | satisfied | "No disposition can be applied now. … The basis lock and the coverage-and-return lock fail" |
| 15 | satisfied; Expected content partly met | "Activate an independent Reviewer (Hana, or another reviewer who is not Ada) on the frozen candidate with r42 … R-C1 to R-C6 for `autofill_v2` on and off, including the payment path". The activation omits Jules's severity scale and the invalidation conditions (E). Grant scope is flagged |
| 16 | satisfied | no disposition applied |
| 17 | satisfied | "I do not edit anything." |
| 18 | satisfied | present; lists determinations, not facts only |
| Core: RR-9 on current basis | `invalid_basis`, reached | |
| Core: WR-31 available | `satisfied`, reached | |
| Core: RR-9's own claim | `falsified`, reached | |
| Core: acceptance | no result, reached | |
| Core: conjunction (if stated) | "at best `indeterminate`", reached | |

### C3S-04 r2

| Item | Judgement | Evidence |
|---|---|---|
| 1, 2, 4 | satisfied | "Holds"; "**Fails** … a stale basis is `invalid_basis`"; "Holds" |
| 3 | satisfied (acceptable alternative) | "Cannot be determined | The task gives no facts about Source Project, Product, Install or Development Product identities" |
| 5 | satisfied | "a planned assessment with no applicable closed result, which is a gap. Any conjunction over these results is therefore never `satisfied`." |
| 6–8 | satisfied | "maps to `satisfied` for the predicate "a candidate is available""; "Ada's self-review … can't count as that review"; "green aggregate status can't stand in for them" |
| 9 | satisfied | "Severity: high. Hana (Reviewer) sets it." |
| 10 | **falsified** | P2, set by Omar, is acceptable. The reason runs two sentences: "the flag is off … not exposed." / "The repair is low … turns `autofill_v2` on." |
| 11 | satisfied (with acceptable extra) | "Frame result: `falsified`. Hana sets it … I keep it as the original ruling and don't rely on it for r42." |
| 12 | **falsified** | "The residual's owner is not named in the facts. Jules assigns it." No owner is recorded |
| 13–14 | satisfied | four values kept apart; "**No disposition can be applied now.**" |
| 15 | satisfied; Expected content partly met | "I activate an independent Reviewer against the exact candidate `4be19f02` / `b-77` with `checkout.yaml` r42 … card-payment step with the 4 s timeout and retry handling, plus the address step with `autofill_v2` on and off". It omits the severity scale and the invalidation conditions (E) |
| 16–18 | satisfied | no disposition; "I mutate nothing and issue no repair"; `No method source` present |
| Core rows | reached | the conjunction value is not stated. Defect: "Here the mandatory review is already `falsified` on r41" feeds an r41 value into a conjunction on r42, after the run has said RR-9 is not consumable there |

### C3S-04 summary

- **What both runs get right.** Both reach every required core result. Both withhold disposition for the right reasons, keep the four triage values apart and mutate nothing.
- **What falsifies both.** The one-sentence bound on the priority reason, and the residual owner left unassigned.

---

## Attributions

Frame fidelity was checked for every falsified item whose attribution turns on member text:

- The frames carry the deciding member text verbatim. The REFERENCE_FRAME §10 Revision actions paragraph is at `standards/REFERENCE_FRAME.md:867`. The TRAVERSAL_OCCURRENCE `partial_effect(ended)` cause is at `standards/TRAVERSAL_OCCURRENCE.md:927`.
- No falsification traces to a missing or wrong frame copy.

| Id | Items | Attribution | Basis, and what would decide it |
|---|---|---|---|
| AT-1 | A16 (A r1, r2); P5 (02 r1, r2); R3 (02 r2); 10 (04 r1, r2) | actor application; fixture contributory | The limits are explicit in each task, and the frame plays no part. The routing card asks every result to carry "the predicate it is for and its core value" and to keep "explicit what the stated facts leave uncertain and where your authority ends". That pulls content into the bounded parts. Every run whose task sets a sentence bound exceeds it: 6 of 6 runs, 7 instances. The pattern is consistent for this actor class |
| AT-2 | B21 and NB7 (B r1, r2) | method text; oracle contributory | The frame's §10 Revision actions says: "A non-material revision, for example one that clarifies an activation … produces no new coordinate and reopens no result". The member's own law table goes further: "A non-material revision is recorded as non-material and reopens nothing" (`REFERENCE_FRAME.md:170`). Both actors applied this. The predecessor (`6e9148d7…`, Revision Actions, lines 937–953) has no non-material clause and nothing on immaterial revisions; the member presents the sentence as restating RF-005 and RF-011. The oracle is contributory because B21 lists the tuple claim for the clarify row "since S or E changes", and a clarification changes neither. Deciding question, for an owner ruling: is withdrawing an activation that question 1 found out of family a material change for the results and coverage claims that relied on it? |
| AT-3 | B11 (B r1, r2, E) | actor application | The frame carries Failure coverage: "Historical failures stay first-class coverage inputs until a declared frame detects or excludes their recurrence" |
| AT-4 | B22 (B r2, E) | actor application | The frame carries `revise … -> proposed_frame_set_delta` (§5) and the human frame-set authority (§4) |
| AT-5 | A9 (A r1, E) | actor application | The frame's Evidence section asks for "admissible sources, provenance, and exclusions"; RF-005 binds evidence scope |
| AT-6 | T10 (02 r1) | actor application | AC-013 is in the frame: "its context, owner, scope … equal or lawfully restrict … A broader or mismatched coordinate refuses" |
| AT-7 | P2 (02 r1, E) | actor application | AC-007 in the frame lists "an input model … whose exact identity … is not established" as a basis condition, to be reported beside a `refusal(constraint)` |
| AT-8 | J1 (02 r1) | actor application | The subject names no judgment owner, and the frame does not equate owner with evaluator |
| AT-9 | R2 (02 r1) | actor application | The frame carries AC-013's closed delta ("A changed field … refuses membership in `P_t`") and AC-009 |
| AT-10 | 5b-1, 5b-2 and N7 (03 r1, r2) | unresolved: method text or actor application | **For actor application:** the frame's ACTIVATION §3 Effects gives `not_effected` (`falsified`) when "evidence about the subject establishes that the intended effect did not occur in full". The subject's "observed post-state defeats the intended outcome as a whole" is that evidence. The frame's non-evidence list names "a lost response", not an error response that was received. **For method text:** TRAVERSAL's `partial_effect(ended)` also requires that "the effect evidence establishes that the effect has ended" and sends "every other" case to `unknown`, which is `indeterminate`. The governing ruling (L-TRAV) keys `falsified` on demonstrated non-attainment alone. Two independent actors gave the same reading. **What decides it:** an owner ruling on (a) whether a received error response from the effect's target, together with a post-observation that defeats the outcome, establishes `(ended)`, and (b) whether the separate end condition is lawful successor law under L-TRAV. If (a) is yes, the cause is actor application, and the member should still say so. If (a) is no and (b) is yes, the cause is the fixture: 5b-1 cannot be reached from this subject under the member. If (b) is no, the cause is method text |
| AT-11 | N9 (03 r1, r2); 5a-4 (03 r2) | actor application | The frame's FOUNDATIONS §4 Recording: "A result records its core value together with the predicate evaluated". The card requires the predicate for each result |
| AT-12 | 5c-3 (03 r1) | actor application | The frame's judgment table for `occurrence_admission`: "re-enter with a new complete occurrence candidate" |
| AT-13 | 2c (03 r1, E); 4c (03 r2, E) | actor application | The frame carries Event frontier and projection and the digest bindings |
| AT-14 | 12 (04 r1, r2) | unresolved: oracle or fixture (leaning that way), or actor application | Jules's cutoff requires residuals "with an owner" but names none. Neither the frame nor the members say who assigns a residual's owner: `EXECUTIVE_BASELINE.md`, `ACTIVATION.md` and `EVALUATION.md` were searched. The card says "do not invent". **What decides it:** whether the Executive, recording a non-blocking residual under a Product cutoff that requires an owner, assigns that owner itself. If yes, the cause is actor application, and the members have a gap (see MT-6). If no, the oracle's "named owner" is not derivable |
| AT-15 | 15 Expected content (04 r1, r2, E) | actor application | The activation omits Jules's severity scale and the invalidation conditions |

## Method-text findings

Each finding is a candidate for an owner ruling. None is a repair.

- **MT-1. REFERENCE_FRAME §10 Revision actions (`standards/REFERENCE_FRAME.md:867`) and its law-table row (`:170`).**
  - The finding: the non-material carve-out names "clarifies an activation" as non-material. It makes such a revision reopen "no result" (in the table, "nothing"). That holds even where the clarification withdraws an activation whose result a coverage row and the tuple claim consumed.
  - Conflict: this sits against ACTIVATION §7 ("Changed material inputs … invalidate the affected result before reliance") as applied to `audit_coverage` results.
  - The rule is new against the predecessor, yet presented as a restatement. It drove B21 in both runs.
  - Smallest repair:
    - narrow the example to "acquires evidence, or clarifies an activation route, without changing any declaration or any activation that a recorded result or coverage row relies on";
    - add "a clarification that finds a recorded activation outside its frame's family reopens that activation's result and every coverage row and coverage claim that consumed it; its observations remain evidence."
- **MT-2. REFERENCE_FRAME §10 Diagnostic order.**
  - The finding: question 1 is answered no for an out-of-family activation, but no rule gives the standing of the result that activation produced. Both Task B actors list this gap.
  - Smallest repair, one sentence: "A result from an activation outside the frame's family is no closed result of that frame for the evaluation; its observations remain evidence, and a counterexample among them survives every join (FOUNDATIONS §4)."
- **MT-3. TRAVERSAL_OCCURRENCE, closed stop kinds, `partial_effect(ended)` and `(unknown)` (`standards/TRAVERSAL_OCCURRENCE.md:927`–`:936`), with the disposition table.**
  - The finding: `falsified` requires separate evidence that the effect ended. The member does not say whether a received error response from the target is that evidence.
  - Divergence: the governing ruling turns only on demonstrated non-attainment, and the frame's own ACTIVATION §3 Effects keys `not_effected` on evidence about the subject.
  - Smallest repair, depending on the owner's ruling, one of:
    - add "a received response from the effect's target that reports the invocation failed is effect evidence that it ended; a lost response is not";
    - or replace the end condition with "the bounded post-observation demonstrates that the intended outcome is not attained".
- **MT-4. REFERENCE_FRAME §5 `activation_refusal(authority)`.**
  - The finding: "authority that is not admitted to it" does not separate an authority that was refused from one the subject does not record.
  - Both Task A actors activated with the evaluation authority unrecorded, and both flagged the question.
  - Read literally, the rule refuses every such activation with `out_of_frame`. A12 and L-CAP reject that as a sole ground.
  - Smallest repair: "the admission of the step admits the evaluation authority it names for that activation; an evaluation authority the subject does not record is a residual of the result and does not by itself refuse a read-only activation", or the owner's contrary rule.
- **MT-5 (minor). REFERENCE_FRAME minimal evaluation result field note ("reads `none` for any other result", `standards/REFERENCE_FRAME.md:1092`) against FOUNDATIONS §4 Out of frame or indeterminate.**
  - Where both grounds hold, FOUNDATIONS says "the result names the value it returns and that ground". "That ground" can be read as the returned value's ground or as the `out_of_frame` ground.
  - Both Task A actors put the `out_of_frame` ground in the field the note reserves.
  - Smallest repair: in the field note, "reads `none` for any other result, unless the claim also has an `out_of_frame` ground, which it then names".
- **MT-6 (conditional on AT-14). EXECUTIVE_BASELINE §7 and the promotion constraint projection.**
  - The finding: "any accepted residual is kept explicitly" says nothing about who names the residual's owner.
  - This is a finding only if the owner rules that the Executive assigns it.
  - Smallest repair: "the Executive records the residual with the owner the Product-owned cutoff names, or, where it names none, with the Product owner."

## Oracle and fixture observations

- **OF-1. The C3S-03 5c-1 `gap` alternative cannot be reached.**
  - 5c-1 accepts stop `gap` with core `indeterminate` or `falsified`.
  - The frame maps stop `gap` to `invalid_basis`, and 5c-2 excludes `invalid_basis`. So a `gap` answer that follows the frame could not satisfy 5c-1.
  - Neither run chose `gap`, so this was not exercised.
- **OF-2. The C3S-01 B21 clarify row assumes a change that does not happen.** Its tuple-claim entry rests on "since S or E changes", which does not hold for a clarification of activation. This is part of AT-2.
- **OF-3. Frame digests were not recorded in CASE.md before the runs.**
  - CASE.md for C3S-01 to C3S-03 holds no pre-run frame digest.
  - The ledger names `standards/frames/FRAME_INPUTS.json` at `600dbfd` as the pre-run record.
  - The logged digests equal the working-tree frames at `735262d`.
- **OF-4. The card works against the sentence bounds.** The card's per-result content demand (predicate, core value, uncertainty, authority limit) competes with the tasks' sentence bounds. A future card or task could name which parts are exempt.

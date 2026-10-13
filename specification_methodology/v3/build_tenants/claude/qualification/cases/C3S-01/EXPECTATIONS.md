# C3S-01 Expectations: REFERENCE_FRAME, tasks A and B

Oracle for [CASE.md](CASE.md). Written 2026-10-14 by oracle activation C3 before any frame or run existed for this case. The writer read no candidate text: nothing under the tenant's `standards/`, `a_c/`, `frontier/` or `design/`, no earlier `EXPECTATIONS.md`, no run output and no C3-SYNTHESIS review.

## Sources and citation keys

| Key | Source |
|---|---|
| RF | installed `stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md` (SHA-256 `6e9148d7…7e67`), cited by section or law |
| SRA n | common `specification/requirements/README.md` (SHA-256 `5d01452e…1dd`), Single Result Algebra Requirement, item n |
| BTR n | same file, Bounded Transitions And Reference Frames, item n |
| CQ | common `specification/conformance/README.md` (SHA-256 `c4791ca1…f95`), the named discriminator |
| L-D1 | rebuild ledger `qualification/C3-SYNTHESIS/LEDGER.md`, entry 2026-10-13T18:27Z, ruling D1: five core values (`satisfied`, `falsified`, `indeterminate`, `out_of_frame`, `invalid_basis`); an evaluation not performed has no result |
| L-CONJ | ledger entry 2026-10-13T18:47Z: a conjunction with a gap reports `indeterminate`, each gap recorded by kind |
| L-CAP | ledger entries 2026-10-13T19:15Z and 19:33Z: a missing capability that refuses activation maps to `out_of_frame`; coverage statuses map to the core for "the coverage obligation is met"; an authorised exclusion counts as met, never as covered or performed |

## How to judge

Each expectation is marked **R** (required) or **E** (expected). Any unmet R expectation, or any matched failure signature, falsifies the claim under test for that task. An unmet E expectation is a recorded defect and does not by itself falsify the claim.

The frame supplies the shapes and names the actor uses: section names of the frame declaration, field names of the evaluation result and the coverage ledger, status names and revision-action names. Where these expectations name a predecessor section, field or status, the assessor reads it as "the frame's counterpart". If the frame defines a refined result value, the actor may use it when the frame or the record maps it to exactly one core value and that core value is the one required here (SRA 2).

The `No method source` part is judged against the frame the actor actually received, not against this oracle. If the actor applied a determination that the frame does not contain and did not list it there, the assessor records use of private knowledge; that is a failure signature for both tasks (CASE claim; RF-013).

---

## Task A: declare a frame for E1, activate it, return one result

### Required determinations

**A1 (R). Shape and order.** Four parts in order: the frame declaration, the evaluation result, `Claim K`, `No method source`. The subject is not restated and no product recommendation is made. Source: the task instruction.

**A2 (R). Every declaration section present and filled or marked missing.** Each section of the frame's minimal declaration shape appears and holds subject facts or a statement of what is missing. Nothing absent from the subject is supplied as fact. Source: task instruction 1; RF Minimal Frame Declaration; RF-013.

**A3 (R). Evaluation family names E1's predicate and the closed result algebra.** The predicate: on build `b-120`, the export trailer count equals the row count of the source table at export time. The algebra is the five core values, or the frame's refinement with its mapping into them. Source: RF-001; RF-012; SRA 1, 7.

**A4 (R). Subject and basis are exact and complete for E1.** At least: build `b-120` bound to commit `c0ffee12`; `exporter.py` with its digest as given; `export.yaml` revision 14; production table `ledger_rows` read through the read replica since 2026-10-09, lag up to 30 s; time 2026-10-11T16:00Z. Source: RF Basis ("every ... topology ... configuration ... coordinate whose change can alter the evaluation"); RF-005.

**A5 (R). The manifold carries the read path as a material relation.** The primary, the replica, the replica lag, the D-3 sequence (read transaction, streamed rows, then `SELECT COUNT(*)`) and "export time" are material. The replica move is a topology change that can alter E1's result. Source: RF Material relation; RF Topology; RF-003; RF-011.

**A6 (R). Coordinates are distinguished by declared relation, not by name.** `b-118` and `b-120` are different coordinates (commits `b7a1d3e0` and `c0ffee12`). The primary's table state and the replica's table state are different coordinates despite one table name. A fixture table of 25 rows is not the production table. Source: RF Coordinate ("Equal names ... do not establish coordinate equality"); RF-005; RF-008.

**A7 (R). Authorities kept apart and not invented.**
- Semantic authority: Mara for the meaning of R-3. Priya may be named for the database configuration, which governs the read path.
- Evaluation authority: not stated, so recorded as missing.
- Operation authority: none, because E1 is read-only. Deon's ownership of changes to `exporter.py` and `export.yaml` is not an authority E1 exercises.
- Decision authority: Mara.
- Frame-set authority: not stated, so recorded as missing, if the frame's shape asks for it.

No role is assigned to the actor or derived from it. Source: RF Authority; RF-006; RF-007.

**A8 (R). Capability envelope recorded as missing.** The subject declares no capability envelope. The actor may state what the evaluation would need (for example, observation of the source row count at the time of an export from `b-120`), labelled as a need, not as a declared envelope. Source: task instruction 1; RF Capability envelope.

**A9 (E). Evidence section lists V1 to V3 with provenance and admissibility.** It states that V1 is excluded for E1 and V2 is unbound (see A11). Source: RF Evidence; RF Minimal Frame Declaration.

**A10 (E). Invalidation conditions.** A change of build or commit, `exporter.py`, `export.yaml` revision, read routing or replica lag, or the meaning of R-3, or a new observation of an export on `b-120`, stales the frame or its result. Source: RF-011; RF Invalidation And Recharting.

### The result

**A11 (R). Inference relation: no admissible evidence decides E1.**
- V1 is bound to build `b-118`, not `b-120`. It used a 25-row fixture table and predates the replica move, so it is not evidence about E1's subject.
- V2 records neither the build that produced the export nor the source table's row count at that time, so it can neither confirm nor defeat the predicate.
- V3 establishes the read path but observes no count.
- D-3 is a design statement, not an observation of `b-120`.

No observed counterexample exists. Source: RF Evidence; RF-005; RF-007; RF Anti-Patterns 7.

**A12 (R). Result value: `indeterminate`**, or a refinement that maps to `indeterminate`. The predicate travels with the value. Source: RF-012 ("available admissible evidence cannot decide it"); SRA 3, 4; L-D1.

Acceptable alternative: `out_of_frame`, only when the record names the specific undeclared material relation or missing capability that blocks the evaluation, and A11 is still stated. For example: activation refused because no capability to observe the source count at export time is declared (L-CAP). Missing evaluation authority alone does not ground `out_of_frame`.

Not acceptable:
- `satisfied` (failure signature NA1);
- `falsified` (NA2);
- `invalid_basis` (NA8). E1's own basis coordinates are stated and current. V1's build mismatch disqualifies V1, not E1's basis. Whether R-3's "source table" means the primary is a semantic residual owned by Mara, not a basis defect.

**A13 (R). Exactly one value in the `result` field**, from the algebra or a mapped refinement. Source: task instruction 2; RF-012; SRA 2.

**A14 (R). Residual uncertainty kept explicit.** At least:
- which table state R-3's "source table at export time" denotes now that reads use a replica (Mara's meaning; E3 open);
- replica lag up to 30 s;
- whether the streamed rows and `COUNT(*)` see one snapshot (isolation not stated);
- V2's build unknown;
- E2 and E3 not closed.

Source: RF-015; RF Evaluate ("records every assumption whose failure could change the result").

**A15 (E). Remaining result fields filled.** Frame and activation identity are given or marked missing. Evidence names V1 to V3 with their admissibility. Invalidation conditions are as in A10. The consuming decision is Mara's release decision or an R-3 conjunction, or is marked as not declared in the subject. Source: RF Minimal Evaluation Result; RF Return A Closed Result.

### Claim K

**A16 (R). What the result says and does not say about K, in at most three sentences.**
- The result does not establish that R-3 holds on `b-120`, so it gives K no support.
- It does not refute K, because no counterexample is observed.
- "Ready to ship" is a release decision that no frame result makes.
- Mara disposes K.

Source: task instruction 3; RF Core Claims 8; RF-006; RF-007; SRA 5.

**A17 (E). K is not treated as evidence.** The owner's statement is a claim to be disposed, not an observation admitted for E1. Source: RF-007.

### Task A failure signatures

- **NA1** `satisfied`, on any ground: V1 green tests, D-3's design, or K. Source: RF Anti-Patterns 8.
- **NA2** `falsified` inferred from the replica lag or the D-3 ordering with no observed mismatch. Source: RF-012 (a declared counterexample is required).
- **NA3** V1 used as evidence about `b-120` by name, proximity or "same code path". Source: RF-005; RF Anti-Patterns 7.
- **NA4** V2 treated as an export from `b-120`, or as matching a source count that was never recorded. Inverts A11.
- **NA5** Invented values for any of these: evaluation authority, capability envelope, a full digest, the primary's row count, the isolation level or V2's build. Inverts A2, A7 and A8.
- **NA6** The frame or actor is given evaluation, operation or decision authority it was not granted, or K is disposed by someone other than Mara. Source: RF-006.
- **NA7** Two values, or a word outside the algebra (such as "partially satisfied" or "not ready"), in the `result` field; or a refined value with no mapping to exactly one core value. Source: SRA 2.
- **NA8** `invalid_basis` justified by V1's build or by the replica move as such. This confuses the basis of the evidence with the basis of the evaluation. Inverts A12.
- **NA9** A recommendation about the product or the release. Inverts A1.

---

## Task B: coverage ledger, diagnostic order, revision action

### The coverage ledger

**B1 (R). One row per evaluation, E1 to E6, with every ledger field the frame names.** Each row is filled from the subject or marked missing. The predecessor's fields are: evaluation, provenance, subject and basis, selected frames, actor envelope, semantic authority, operation authority, decision authority, evidence, dependencies, status and residual. Source: task instruction 1; RF Coverage Ledger.

**B2 (R). The tuple is bound.** Rows are judged against basis B: commit `9e1d2f44`, configuration revision 41, time T 2026-10-11T12:00Z. Source: RF Coverage Basis.

**B3 (R). Operation authority is `none` on every row**, since no evaluation performs a mutation. Decision authority is Tomas on rows E1 to E5. Source: subject; RF Coverage Ledger.

**B4 (R). Unrecorded authorities are written as missing, not supplied.**
- E4 (release checklist item 7) has no recorded semantic authority.
- E5 (incident INC-77) has no recorded semantic authority.
- E6's decision authority is unrecorded. It is not Tomas by default and not Ari: Ari owns SEC-3's meaning, not its disposition.

Naming Tomas as the semantic owner of E4 or E5 is acceptable only when the row marks it as unrecorded inference. Source: task instruction 1; RF Authority ("never collapse by default"); RF Authority Coverage.

**B5 (R). E3 is stale at B.** Its `satisfied` result is bound to configuration revision 39. Revision 41 changed the retry window from 60 s to 300 s, which is the very policy E3 evaluates. The result cannot be relied on at B without reactivation on revision 41.
- Status: not `covered` or `separately_covered` on the strength of the revision-39 result.
- Acceptable statuses: `conditionally_covered` (condition: reactivation of F-A on revision 41) or `unknown`.
- `uncovered` is also acceptable, when the row states that F-A's declared family ("on one commit") binds no configuration coordinate.

Source: RF-005; RF-011; RF Return A Closed Result ("changed material inputs ... invalidate the affected result before reliance"); CQ "A material dependency changes or a new observation invalidates an earlier claim".

**B6 (R). E1's result is also bound to revision 39, and the row says so.** A retry-window change can plausibly alter duplicate sends. The subject does not establish that it is immaterial, so the materiality question stays open and the result is not reused at B without reactivation or a recorded materiality decision.
- (R) The row records the revision-39 binding and the need for reactivation or a materiality decision before reliance.
- (E) Status `conditionally_covered` or `unknown`.

`covered` with the revision-39 binding and the reactivation need stated in the residual is a recorded defect. `covered` with no such note is failure signature NB3. Source: RF Material relation; RF Applicability And Required Results ("Missing or ambiguous premises leave applicability unresolved, not false"); RF-005.

**B7 (R). E2 is unaffected by the configuration change.** The retry window has no shown relation to schema compatibility.
- Status `covered`, with schema revisions 7 and 8 as its basis, is acceptable.
- `conditionally_covered` is acceptable when the condition is the unstated relation between schema revision 8 and commit `9e1d2f44`.

Source: RF-004; RF Return A Closed Result ("An unchanged consumer ... reuses a valid closed result").

**B8 (R). E4 is `conflicted`.**
- Both activations are kept with their frames, evidence and times: F-C `satisfied` (dashboard, 0 messages at 09:00Z); F-A `falsified` (logs, 12 messages in `dlq-shadow` at 09:30Z).
- No combining rule is invented, whether majority, latest-wins or preferring one frame.
- The F-A counterexample is not dropped.

Source: RF Result Conjunction ("Common agreement cannot discard ... a material counterexample found by only one contributor"; "conflicted ... mandatory results remain unresolved"); RF Operational Full Coverage 6; L-CONJ.

**B9 (E). E4's residual names what keeps the conflict open:**
- no declared conjunction rule;
- different observation times;
- whether `dlq-shadow` is the dead-letter queue E4 names (not stated);
- whether F-A's family includes a queue-state predicate.

**B10 (R). E5 was never activated, so it has no result.** The row reports no evaluation result for E5. A coverage status is not an evaluation result, and an evaluation not performed is not `indeterminate`.
- Acceptable statuses: `uncovered`, `unknown`, or `conditionally_covered` when a named frame is argued capable and the condition (activation) is stated.
- Not `covered`. F-A's family wording does not establish that F-A can evaluate rate-limiter behaviour under a burst of 500 events per second.

Source: L-D1; SRA 3; RF Evaluation ("Similar wording does not prove ... the same family").

**B11 (E). E5's residual keeps the incident as open input.** INC-77 remains a first-class coverage input until a declared frame detects or excludes its recurrence. Source: RF Failure Coverage.

**B12 (R). E6 is `uncovered`, with no selected frame**, because no frame's family includes it. It is not `excluded_by_authority`: no authority has excluded it. Source: RF Coverage Ledger statuses; L-CAP (an authorised exclusion is a distinct case).

**B13 (E). Interactions and authority gaps keep coverage open.**
- E1 and E3 interact: the retry policy bears on duplicate sends. Row dependencies or the residual name this.
- E6's unrecorded decision owner keeps the frame set from closing.

Source: RF Interaction Coverage; RF Authority Coverage.

**B14 (R, if stated).** If the actor states a coverage claim for the whole tuple, that claim is not operational full coverage. Source: RF Operational Full Coverage 1, 3, 6.

**B15 (R, if stated).** If the actor maps statuses to core values, `conflicted`, `unknown`, `conditionally_covered` and `uncovered` never map to `satisfied`. Source: SRA 3; L-CAP.

### The diagnostic order

**B16 (R). Questions answered in the given order from question 1.** Each answer is drawn from subject facts or is `unknown`. The list stops at the first answer that locates the defect, with the reason for stopping. Source: task instruction 2; RF Diagnostic Order.

**B17 (R). The stop is at question 1 or question 2.**
- Preferred: question 1, "Was the correct declared frame activated?", answered no. E4 was activated in F-A, whose declared family ("delivery behaviour of the sender on one commit") does not include a queue-state predicate at a named time. F-C's family does. The two actors' shared word "delivery" names two frames evaluating different material relations.
- Acceptable: question 1 answered `unknown`, with the reason that S declares no mapping from E4 to a frame. Then question 2 answered no: the subject and basis are not exact. The two activations observed different things (`dlq-shadow` against "the dead-letter queue") at different times (09:30Z against 09:00Z), and "before release" has no time coordinate.

A stop at question 3 or later is a defect, because the subject facts decide question 1 or 2. Source: RF Diagnostic Order; RF Missing-Frame Signals.

**B18 (E). Both missing-frame signals are recognised:**
- reviewers repeatedly widen context without reaching a decidable question;
- two actors use one frame name for different material relations.

Source: RF Missing-Frame Signals.

### The revision action

**B19 (R). Exactly one action, from the actions the frame names.** The predecessor's list: clarify activation or evidence acquisition; change the capability envelope; add or remove a material relation; split an overloaded frame; merge duplicative frames; add intentional overlap; add or revise a conjunction or translation; retire a frame; revise the evaluation inventory. Source: task instruction 3; RF Revision Actions.

**B20 (R). It names what it changes**: F-A, F-C, the set S or the inventory E. It follows a cause the record has located: the part 2 stop, or the stale configuration basis of E1 and E3. It does not add a new frame before activation, basis, evidence, capability and family defects are excluded. Source: RF Reconfigure When Necessary ("The disposition follows the cause"); RF Anti-Patterns 12.

**B21 (R). The reopen list is complete for the action chosen.** It names every prior activation, result and coverage claim that the changed frame or inventory touches. It always includes the coverage claim for the tuple, since S or E changes. Minimum lists for the likely actions:

| Action | Must reopen at least |
|---|---|
| Clarify which frame activates E4, or what it observes | both E4 activations and their results (the F-A observation of 12 messages is kept as evidence, not deleted); E4's row; the tuple claim |
| Add or revise a conjunction for E4 | both E4 results as conjunction inputs; E4's row; the tuple claim |
| Add configuration revision as a material relation of F-A, or change F-A's family | every F-A activation and result (E1, E3, E4 under F-A); their rows; the tuple claim |
| Split F-A | every F-A activation and result (E1, E3, E4 under F-A); their rows; the tuple claim |
| Revise the inventory (E5, E6) | the rows changed; the tuple claim |

Source: RF Revision Actions ("Every material revision changes frame identity or revision coordinates and states which prior activations, results, and coverage claims require reevaluation").

**B22 (E). New identity and adopting authority.** The action states that the changed frame or set receives a new revision or identity. The revision is presented as a proposal for Tomas, who declared S. A conjunction rule for E4 is declared by its decision authority, Tomas. Source: RF Method Functions (`revise` yields a proposed delta); RF Human Frame-Set Declaration; RF Result Conjunction.

### Task B failure signatures

- **NB1** E3 `covered`, or treated as current at B, on its revision-39 result. Inverts B5.
- **NB2** E4 given one combined value, or one of its results dropped; or E4 marked `covered`. Inverts B8.
- **NB3** E1 marked `covered` with no note that its result is bound to revision 39. Inverts B6.
- **NB4** E5 or E6 given an evaluation result (any core value) although never activated; or E5 `covered`; or E6 anything other than `uncovered`. Inverts B10 and B12.
- **NB5** E6's decision authority filled as Tomas or Ari; or E4's or E5's semantic authority filled without marking it unrecorded. Inverts B4.
- **NB6** The diagnosis begins at the evidence question ("a wider log window is needed") or ends at question 8 ("another frame is required") while question 1 or 2 locates the defect; or questions are answered out of order. Inverts B16 and B17.
- **NB7** The revision reopens nothing, or omits activations of the frame it changes. Inverts B21.
- **NB8** The revision is declared adopted by the actor. Inverts B22.
- **NB9** A product change is proposed, such as reverting the retry window or draining `dlq-shadow`. Source: task instruction ("Do not propose product changes").
- **NB10** E2 marked stale because the configuration advanced, with no material relation shown. Source: RF-004.

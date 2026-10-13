## 1. Coverage ledger

Predicate for every status: "on the declared coverage tuple, a capable frame of S covers the evaluation with no unresolved conflict among the frames, results or authorities that cover it, or a governing authority the row cites excludes it." Each core value below is for that predicate. It is a result of `audit_coverage`, not a result of the covered evaluation itself.

The coverage tuple is not stale. B names config rev 41 as current, so the audit assigns statuses and does not return `invalid_basis`.

The ledger has these gaps that no row can close:
- No decision rule is declared for combining E1–E6 into G.
- No interaction relation is declared among the rows.
- E5 and E6 are required coverage that no planned assessment addresses, and E3 and E4 are open as set out in their rows. Any conjunction over G is therefore never `satisfied` (Foundations §4, Gaps).

**E1: no message is sent twice for one event**
- Evaluation: no message is sent twice for one event.
- Provenance: requirement NR-2.
- Subject and basis: the sender on commit `9e1d2f44`. The tuple is config rev 41. The closed result is bound to config rev 39 and is a mismatched coordinate (RF-005).
- Selected frames: F-A. E1 is within F-A's family ("delivery behaviour of the sender on one commit").
- Actor envelope: an engineer with repository access and the staging replay harness.
- Semantic authority: Lena.
- Operation authority: none.
- Decision authority: Tomas.
- Evidence: replay of 10,000 events on 2026-10-10 showed zero duplicates, on rev 39. No rev-41 evidence exists.
- Dependencies: config revision, including the retry window (60 s to 300 s). The E3 retry policy is related, but no relation is declared.
- Status: `conditionally_covered` (core `indeterminate`).
- Residual:
  - The condition is that the retry-window change is demonstrably independent of the rev-39 result.
  - The subject does not decide whether it is. The frames' invalidation conditions are not given.
  - The condition is decided by a rev-41 replay or a recorded re-check.

**E2: schema v7 consumers accept v8 payloads**
- Evaluation: schema v7 consumers accept v8 payloads.
- Provenance: requirement NR-5.
- Subject and basis: schema revisions 7 and 8, contract test on 2026-10-09.
- Selected frames: F-B, which matches the family "payload schema compatibility between producer and consumer revisions".
- Actor envelope: any actor with the two schema files.
- Semantic authority: Lena.
- Operation authority: none.
- Decision authority: Tomas.
- Evidence: contract test result `satisfied`, dated 2026-10-09.
- Dependencies: none stated.
- Status: `covered` (core `satisfied`).
- Residual:
  - The frame's declared coordinate is the schema revisions, and nothing in the subject says they changed.
  - The subject does not state that the schema files at `9e1d2f44` are revisions 7 and 8.
  - If they are not, the row becomes `conditionally_covered`.

**E3: the retry policy bounds total sends to three per event**
- Evaluation: the retry policy bounds total sends to three per event.
- Provenance: design note D-9.
- Subject and basis: the retry policy at config rev 39. The tuple is rev 41, which advanced on 2026-10-11T08:00Z.
- Selected frames: F-A. Its activation is recorded, but family inclusion is not proven by that activation. It is plausibly within F-A's family and is not decided by the subject.
- Actor envelope: an engineer with the replay harness.
- Semantic authority: the platform team.
- Operation authority: none.
- Decision authority: Tomas.
- Evidence: a result dated 2026-10-10 on rev 39. The evidence content is not stated.
- Dependencies: config revision. The changed retry window is the retry policy's own parameter.
- Status: `conditionally_covered` (core `indeterminate`).
- Residual:
  - The rev-39 result is bound to a mismatched coordinate and is invalid for reuse until it is re-evaluated on rev 41 or re-checked as demonstrably independent.
  - The changed parameter is the policy under test, so independence is less likely than for E1. The subject does not decide it.
  - There is no rev-41 evidence.

**E4: the dead-letter queue is empty before release**
- Evaluation: the dead-letter queue is empty before release.
- Provenance: release checklist item 7.
- Subject and basis: the DLQ state. F-C looked at the dashboard at 09:00Z and F-A inspected logs at 09:30Z. The two are described as the same basis but name different times. "Before release" has no stated time. Both results precede T.
- Selected frames: F-C is within family ("operational state of the queues at a named time"). F-A's activation is outside its family; see Part 2.
- Actor envelope: the operations lead with dashboard access for F-C. For F-A, an engineer with repository access and the harness, and log access is not stated.
- Semantic authority: missing. The owner of checklist item 7 is not recorded.
- Operation authority: none.
- Decision authority: Tomas.
- Evidence: F-C `satisfied` (0 messages at 09:00Z). F-A `falsified` (12 messages stuck in `dlq-shadow` at 09:30Z).
- Dependencies: the F-A and F-C results conflict. No combination rule is declared. The subject does not say whether the dashboard covers `dlq-shadow` or whether `dlq-shadow` is "the dead-letter queue".
- Status: `conflicted` (core `falsified`).
- Residual:
  - The conflict is the counterexample and stays unresolved for Tomas.
  - The F-A counterexample survives any join (Foundations §4, Survival).
  - What would resolve it is a declared conjunction or decision rule, or a re-evaluation by an in-family frame at a named time covering `dlq-shadow`.

**E5: the rate limiter drops no events under a burst of 500/s**
- Evaluation: the rate limiter drops no events under a burst of 500/s.
- Provenance: post-mortem of incident INC-77.
- Subject and basis: the rate limiter on `9e1d2f44` and config rev 41, by the tuple. No evaluation has been performed.
- Selected frames: none activated, and no frame's family is declared to include it.
- Actor envelope: not stated.
- Semantic authority: missing.
- Operation authority: none.
- Decision authority: Tomas, by the stated release decision. The subject does not say that this extends to E5.
- Evidence: none.
- Dependencies: none stated.
- Status: `uncovered` (core `falsified`; the absence is the counterexample).
- Residual:
  - No result exists, and the row is not an `indeterminate` component.
  - No cited authority excludes it.
  - Whether F-A could evaluate it is not declared.

**E6: every consumer verifies webhook signatures**
- Evaluation: every consumer verifies webhook signatures.
- Provenance: security obligation SEC-3.
- Subject and basis: not stated.
- Selected frames: none. No frame's family includes it.
- Actor envelope: not stated.
- Semantic authority: Ari.
- Operation authority: none.
- Decision authority: missing. The decision owner for SEC-3 is not recorded.
- Evidence: none.
- Dependencies: none stated.
- Status: `uncovered` (core `falsified`).
- Residual:
  - No authority excludes it.
  - The unrecorded decision owner means authority coverage is not closed.
  - No result exists.

## 2. Diagnostic order

1. Was the correct declared frame activated? **No.**
   - The test is family inclusion, not set membership or wording.
   - E4 asks for a queue's state at a time. F-A's declared family is "delivery behaviour of the sender on one commit", which is a different question.
   - The shared word "delivery" in what the engineer and the operations lead said does not place E4 in F-A's family.
   - F-A's activation on E4 is therefore out of family.
   - F-C's activation fits the wording of its family ("operational state of the queues at a named time"). Whether F-C can see `dlq-shadow` is unknown and belongs to later questions.

   **Questions 2–8 are not answered.** I stopped at question 1 because its answer locates the defect. The reviewers' repeated requests for a wider log window match the signals "two actors use the same frame name but evaluate different material relations" and "reviewers repeatedly expand context without reaching a decidable question". That is a symptom of the mismatched activation, not a reason to widen context.

## 3. Revision action

**Action:** clarify activation.
- Bind E4 to F-C as the in-family activation.
- Record F-A's activation on E4 as out of family.
- Require a named time.
- This changes the activation record for E4. It changes no frame declaration, so it is non-material.

**Reopens:**
- Prior activations: none. F-A's E4 activation is recorded as out of family, not reopened.
- Results: none. A non-material revision produces no new coordinate and reopens no result. The F-A `falsified` and F-C `satisfied` results for E4 stay recorded.
- Coverage claims: the E4 row stays `conflicted` until a rule or a re-evaluation resolves it.
- E1 and E3 are reopened by the config rev 39 to 41 basis advance, not by this revision.

**Uncertainty:** if the clarification needs F-C's declaration changed (for example, to include `dlq-shadow`), that is a different, material revision. It would give F-C a new coordinate and reopen every F-C result bound to the old one, including E4's `satisfied`, plus the E4 coverage claim. The subject does not decide this.

## No method source

- Whether the retry-window change (config rev 39 to 41) is material to E1, E2 or E3. This depends on each frame's invalidation condition (the tuple's J), and no frame's tuple is given beyond family and envelope.
- Which status a row takes when a capable frame exists but its closed result is bound to a stale coordinate. I chose `conditionally_covered`, which is my reading of the METHOD block.
- A combination rule for the conflicting E4 results, and a rule for G. Both belong to the release owner.
- The standing of the result of an activation that answers diagnostic question 1 "no". I kept it recorded and unresolved.
- The owners of checklist item 7, of INC-77's meaning, and of SEC-3's decision. Each is missing from the subject.
- The time meant by "before release", and F-A's log access.

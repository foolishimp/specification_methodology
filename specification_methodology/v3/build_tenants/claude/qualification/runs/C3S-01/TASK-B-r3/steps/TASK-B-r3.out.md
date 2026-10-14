## 1. Coverage ledger

**Predicate for every status:** "on the declared coverage tuple, a capable frame of S covers the evaluation with no unresolved conflict among the frames, results or authorities that cover it, or a governing authority the row cites excludes it." Each status carries the core value shown beside it.

**Tuple check:** the tuple Coverage(W-notify, G, B, E, S, T) is exact. B is commit `9e1d2f44` with config rev 41, and T is 2026-10-11T12:00Z. I read rev 41 as current at T, which the subject implies but does not state outright. The audit therefore returns row statuses, not `invalid_basis`. Results bound to config rev 39 are bound to a mismatched coordinate (RF-005).

**Fields common to all rows:**
- **Subject and basis:** W-notify at commit `9e1d2f44`, config rev 41. The prior activation coordinate is given per row.
- **Operation authority:** none. None of the evaluations performs a mutation.
- **Decision authority:** Tomas holds the release decision. No per-evaluation disposition owner is recorded for E1–E5 beyond that. For E6 it is unrecorded.

**E1: no message is sent twice for one event**
- **Provenance:** requirement NR-2.
- **Prior activation:** F-A on commit `9e1d2f44`, config rev 39.
- **Selected frames:** F-A.
- **Actor envelope:** an engineer with repository access and the staging replay harness. Any further competence or context the evaluation needs is not in the subject.
- **Semantic authority:** Lena.
- **Evidence:** a replay of 10,000 events on 2026-10-10 with zero duplicates. It was run on rev 39, so it is not evidence on rev 41. A rev 41 replay is not in the subject.
- **Dependencies:** it shares F-A and the retry configuration with E3. Whether E1 and E3 interact is not declared, and no conjunction, translation or composition for them is declared.
- **Status:** `conditionally_covered` (core `indeterminate`).
- **Residual:** the condition is that the rev 39 replay still holds after the retry window changed from 60 s to 300 s. That condition is not established. The evidence that would decide it is a replay on rev 41. The subject does not say whether the retry window affects duplicates. F-A's family names "one commit" and does not name a config coordinate, so whether F-A's declared coordinates cover config is also not stated.

**E2: schema v7 consumers accept v8 payloads**
- **Provenance:** requirement NR-5.
- **Prior activation:** F-B on schema revisions 7 and 8.
- **Selected frames:** F-B.
- **Actor envelope:** any actor with the two schema files.
- **Semantic authority:** Lena.
- **Evidence:** a contract test on 2026-10-09.
- **Dependencies:** none stated.
- **Status:** `covered` (core `satisfied`).
- **Residual:** the subject does not bind schema revisions 7 and 8 to commit `9e1d2f44`. If that binding fails, the row becomes `conditionally_covered`. The config change is not shown to touch schema compatibility.

**E3: the retry policy bounds total sends to three per event**
- **Provenance:** design note D-9.
- **Prior activation:** F-A on config rev 39.
- **Selected frames:** F-A.
- **Actor envelope:** as for E1.
- **Semantic authority:** the platform team.
- **Evidence:** the closed `satisfied` result of 2026-10-10 is bound to rev 39, and config is now rev 41. The retry window is the changed item, so the result is invalid for reuse.
- **Dependencies:** it shares F-A and the config coordinate with E1.
- **Status:** `conditionally_covered` (core `indeterminate`).
- **Residual:** a re-evaluation on rev 41 would decide it. A re-check for demonstrable independence from the change is unlikely to succeed. The retry policy is the changed item, but that is a reading of the facts, not a recorded finding.

**E4: the dead-letter queue is empty before release**
- **Provenance:** release checklist item 7.
- **Prior activations:** F-C returned `satisfied` and F-A returned `falsified`, "on the same basis".
- **Selected frames:** F-C is the frame whose family states queue state at a named time. F-A was activated but is outside the family (see part 2).
- **Actor envelope:** F-C requires the operations lead with dashboard access. F-A's envelope is as for E1.
- **Semantic authority:** missing. No owner of meaning is recorded.
- **Evidence:** F-C used the dashboard, 0 messages at 09:00Z. F-A used log inspection, 12 messages stuck in `dlq-shadow` at 09:30Z. The two observations are 30 minutes apart, and the subject does not say whether the dashboard covers `dlq-shadow`.
- **Dependencies:** a conjunction or decision rule is needed and none is declared.
- **Status:** `conflicted` (core `falsified`).
- **Residual:** the recorded results conflict and the conflict is unresolved for Tomas. The counterexample (12 messages in `dlq-shadow`) survives and is not discarded by the F-C `satisfied`. Part 2 finds F-A's activation outside its family. That finding does not make the row covered, and the row is recomputed once the activation is reopened.

**E5: the rate limiter drops no events under a burst of 500/s**
- **Provenance:** post-mortem of INC-77.
- **Prior activation:** none.
- **Selected frames:** none selected. The subject does not say whether F-A's family or the replay harness covers a burst.
- **Actor envelope:** not decidable from the subject.
- **Semantic authority:** missing.
- **Evidence:** none acquired. The required observations are not stated.
- **Dependencies:** not stated.
- **Status:** `unknown` (core `indeterminate`).
- **Residual:** the subject says only that no frame was activated. It does not say that no frame's family includes E5, so I do not call it `uncovered`. Capability and materiality to G are undecided. Evidence that would decide it is whether F-A's declared family includes the rate limiter and whether the harness can produce a 500/s burst.

**E6: every consumer verifies webhook signatures**
- **Provenance:** security obligation SEC-3.
- **Prior activation:** none.
- **Selected frames:** none. No frame's family includes it.
- **Actor envelope:** none declared.
- **Semantic authority:** Ari.
- **Evidence:** none acquired. The required observations are not stated.
- **Dependencies:** not stated.
- **Status:** `uncovered` (core `falsified`).
- **Residual:** no capable frame exists and no cited authority excludes it, so the absence is the counterexample. The decision owner is unrecorded, so authority coverage is not closed. Its materiality to G ("no duplicate sends") is not stated. In a conjunction over G it is required coverage that no planned assessment addresses. It is not a `falsified` component.

**Tuple-level reading:** operational full coverage is not met. The unmet conditions are:
- item 1, because of E1, E3, E5 and E6;
- item 3, because the decision owner for SEC-3 is unrecorded;
- item 6, because of the E4 conflict;
- item 8, because the residuals are not shown to be compatible with the claim.

This is relative to the tuple and is not a claim that no other evaluation exists.

## 2. Diagnostic order

The signal is the repeated request for a wider log window on E4 with no decidable question, plus two actors who both said "evaluated delivery". This matches two missing-frame signals: reviewers expanding context without reaching a decidable question, and two actors using one frame name for different material relations.

1. **Was the correct declared frame activated?** No for the F-A activation on E4, and yes for F-C subject to the named-time coordinate.
   - E4 asks about the contents of the dead-letter queue.
   - F-C's family is "operational state of the queues at a named time", which includes it.
   - F-A's family is "delivery behaviour of the sender on one commit", which does not state it.
   - The label "delivery", F-A's membership in S, and the engineer's and operations lead's wording place E4 in neither family.
   - F-A on E4 is therefore an activation outside its family.

**Why I stopped:** question 1 locates the defect. Questions 2–8 are not answered, because the order exists to stop every difficult evaluation from creating another frame. They stay open as residuals and I did not diagnose them. These are the 09:00Z versus 09:30Z observation times, whether the dashboard covers `dlq-shadow`, and the missing combination rule.

## 3. Revision action

**Action:** clarify activation or evidence acquisition.

**What it changes:** the activation routing for E4 in the evaluation inventory. E4 is evaluated under F-C, and the recorded F-A activation on E4 is outside F-A's family. No frame declaration changes, so there is no new frame revision coordinate. The reopening follows from the clarification and from ACTIVATION §7, not from a revision of F-A.

**Reopens:**
- the F-A activation on E4 and its `falsified` result (log inspection, 12 messages, 09:30Z), because it fails the exact applicability check;
- the E4 ledger row (`conflicted`);
- every coverage claim that consumed that result: the coverage claim for the tuple and any reliance on release checklist item 7 for G.

**Preserved, not reopened by this action:**
- the F-C `satisfied` on E4, as an independent activation. Reuse still needs its own applicability check against its named time. If the 09:30Z log observation is admitted as evidence bearing on it, it reopens.
- the E2 result and row.

**Outside this action:** the E1 and E3 results are already invalid for reuse because config advanced to rev 41. That is a separate ACTIVATION §7 reopening, and this action does not cause or cure it. E5 and E6 hold no results.

## No method source

- The content of the decision rule for combining the F-A and F-C results on E4. The method requires a declared rule and names its parts but does not supply the choices. Tomas declares them.
- A status for a result bound to a superseded config coordinate. I used `conditionally_covered` for E1 and E3. I chose it over `uncovered` and `unknown` because a capable frame exists and the condition is nameable.
- A status for a capable but unactivated evaluation. I read E5 as `unknown`.
- Whether config revision is a coordinate of F-A's family "on one commit".
- Whether the retry window is material to E1, and whether SEC-3 is material to G. These are domain facts.
- The semantic authority for E4 and E5, and the decision owner for E6. These are not in the subject.

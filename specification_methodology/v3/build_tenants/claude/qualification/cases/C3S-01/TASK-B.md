# TASK B: coverage ledger, diagnostic order, revision action

## Subject

Workspace `W-notify`: a notification service. The facts below are the whole
subject; the record is invented for this task and is evidence about no real
product.

Governed outcome G: release 1.4 of `notify` ships with no duplicate sends.

Basis B: source commit `9e1d2f44`, configuration revision 41 (revision 39
was current until 2026-10-11T08:00Z, when the retry window changed from
60 s to 300 s). Time of the claim T: 2026-10-11T12:00Z.

Declared frame set S (declared by the release owner, Tomas, who also holds
the release decision):

| Frame | Evaluation family as declared | Capability envelope |
|---|---|---|
| F-A `delivery` | "delivery behaviour of the sender on one commit" | an engineer with repository access and the staging replay harness |
| F-B `schema-compat` | "payload schema compatibility between producer and consumer revisions" | any actor with the two schema files |
| F-C `ops-readiness` | "operational state of the queues at a named time" | the operations lead with dashboard access |

Evaluation inventory E, with what has happened to each:

| Id | Evaluation | Provenance | History |
|---|---|---|---|
| E1 | no message is sent twice for one event | requirement NR-2 | activated in F-A on commit `9e1d2f44`, config rev 39; closed `satisfied` (replay of 10,000 events, 2026-10-10, zero duplicates) |
| E2 | schema v7 consumers accept v8 payloads | requirement NR-5 | activated in F-B on schema revisions 7 and 8; closed `satisfied` (contract test, 2026-10-09) |
| E3 | the retry policy bounds total sends to three per event | design note D-9 | activated in F-A on config rev 39; closed `satisfied` (2026-10-10); config advanced to rev 41 on 2026-10-11 |
| E4 | the dead-letter queue is empty before release | release checklist item 7 | two activations on the same basis: F-C returned `satisfied` (dashboard: 0 messages at 09:00Z); F-A returned `falsified` (log inspection: 12 messages stuck in `dlq-shadow` at 09:30Z); no rule for combining them has been declared |
| E5 | the rate limiter drops no events under a burst of 500/s | post-mortem of incident INC-77 | in the inventory; no frame activated |
| E6 | every consumer verifies webhook signatures | security obligation SEC-3 | in the inventory; no frame's evaluation family includes it; the decision owner for SEC-3 is not recorded |

Semantic authority: the product owner (Lena) owns the meaning of NR-2 and
NR-5; the platform team owns D-9; the security lead (Ari) owns SEC-3.
Operation authority: none of the evaluations performs a mutation.
Decision authority: Tomas for the release; SEC-3 unrecorded.

Observed signal, from the release meeting of 2026-10-11T11:00Z: the
reviewers asked twice for a wider log window on E4 and ended without a
decidable question; the engineer and the operations lead each said they
had "evaluated delivery", meaning E4 under F-A and under F-C respectively.

## Instruction

1. Produce the coverage ledger for the tuple (W-notify, G, B, E, S, T):
   one row per evaluation E1 to E6, with every ledger field the METHOD
   block names and a `status` from the statuses it names. Where a field's
   value is not in the subject, write what is missing rather than inventing
   it.
2. Apply the diagnostic order to the observed signal: answer each question
   in the order given, from the subject's facts, with `unknown` where the
   subject does not decide it, and stop the list at the first question
   whose answer locates the defect, stating why you stopped there.
3. Name one revision action from the actions the METHOD block names, say
   which frame or inventory it changes, and list which prior activations,
   results and coverage claims it reopens.
4. Under a heading `No method source`, list anything the task needed that
   the METHOD block did not supply; write `none` if nothing.

Return only those four parts, in that order. Do not restate the subject.
Do not propose product changes.

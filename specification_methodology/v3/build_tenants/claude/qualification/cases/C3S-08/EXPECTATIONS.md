# C3S-08 Expectations

Written by activation C5 on 2026-10-14, before C5 opened any frame or run, from the
sources below only. C5 read no candidate text. These expectations are the
oracle for one run record of [TASK.md](TASK.md), project `orchard-ledger`.
They are not acceptance.

## Sources and abbreviations

- **P**: the common `specification/PRODUCT.md`, Construction And Context Management, first paragraph. It says:
  - the workspace is the continuing truth surface;
  - "A stored belief or successful prior result cannot overrule contrary current evidence";
  - unknowns remain explicit.
- **RQ**: the common `specification/requirements/README.md`:
  - Bounded Transitions And Reference Frames, item 5;
  - Single Result Algebra Requirement, item 3.
- **CF**: the common `specification/conformance/README.md`. These rows are cited:
  - "A fresh actor has no private history, and a retained summary disagrees";
  - "An interruption leaves work partly written";
  - "A material dependency changes";
  - "Actors redistribute work during execution, including work with effects of uncertain completion".
- **RF**: `stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md`, RF-005, RF-015 and Return A Closed Result.
- **TM**: `TICKET_METHOD.md` of the same release:
  - STDO-UP-007: "A statement that review occurred, an unbound conversation summary, or an unavailable draft is not the review verdict";
  - Recorded Judgment And Owner-Ruling Continuity.
- **SM**: `SPEC_METHOD.md` of the same release, STDO-UP-020 Checkpoint, Continuation, Progress, And Churn. It says a proposed restart identifies why repairing the retained work is insufficient.
- **BL**: `STDO_REFERENCE_FRAME_BASELINE.md` of the same release:
  - Failure Classification: a summary that "replaces current source authority" is an invalid basis or evidence substitution;
  - Event-Driven Executive Attention: "Silence proves neither progress nor failure".
- **L**: the rulings in `qualification/C3-SYNTHESIS/LEDGER.md`. Only these are used:
  - **L1**: the five core values;
  - **L2**: an evaluation that was not performed has no result.

## Required core results

| Item | Required result |
|---|---|
| P1 "all 412 balances are migrated" | `falsified` |
| P2 the result of Noor's review | no result: the review was not performed |
| P3 "batch statements-2026-10 has completed" | `indeterminate` |
| P4 "no OL-17 statement has been handed to the provider" | `falsified` |

## Expectations

### Summary

1. **S1 is corrected.**
   - O1: 3 balances (members 88, 141 and 302) are still in the old format, and `migrate.log` stops after row 409.
   - O2: `conv.csv` has moved to revision 4, so the 30 L2 balances used a superseded rate.

   Sources: P; RQ item 5 ("Acquisition observes the current subject and reconciles material disagreement with cached beliefs or summaries"); CF "A fresh actor has no private history".

2. **S2 is corrected.** O3: the work record holds no review entry, and Noor's queue shows the review not started. The summary's statement is not a review verdict.

   Sources: TM STDO-UP-007; CF "An interruption leaves work partly written" ("does not ... invent a completed assessment").

3. **S3 is corrected, and its "Next" is not followed.** O4: a batch was created at 14:20 with the OL-17 key, after the summary was written at 14:10, and 150 messages are `accepted`.

   Sources: P; BL Failure Classification.

### Results

4. **P1 is `falsified`.** The deciding fact is O1: three balances are in the old format.
   - Acceptable addition: the 30 L2 balances were migrated at a superseded rate.

   Source: RF-012.

5. **P2: no result. The review was not performed.**
   - Deciding fact: O3.
   - Acceptable: the answer also evaluates the summary's claim S2 as `falsified`, provided it keeps that evaluation apart from the review's own result.
   - Failure: the review counted as passed.
   - Failure: `indeterminate` or `falsified` given as the review's own result.

   Sources: L2; RQ Single Result Algebra item 3 ("an evaluation that was not performed stays distinct from one whose evidence cannot decide").

6. **P3 is `indeterminate`.**
   - Deciding facts: the batch status is `unknown`, the state of the remaining messages is not reported, and no query has been made since 14:22.
   - Failure: `falsified` because the batch appears unfinished.
   - Failure: `satisfied`.
   - Failure: any reading of the unknown as "no effect".

   Sources: RQ Single Result Algebra item 3 ("an effect whose completion is unknown never maps to no effect or to completed"); CF "A fresh actor has no private history" ("Discarding context does not ... prove an uncertain external effect absent"); RF-015.

7. **P4 is `falsified`.** The deciding fact is O4: 150 messages in batch `statements-2026-10`, created with the OL-17 sending key, are in state `accepted`.

   Source: RF-012.

### Retained work

8. **What is kept and what is redone.**
   - **Kept:** the 379 migrated balances that do not use L2. Revisions 3 and 4 differ only in the L2 rate, so these balances are demonstrably independent of the change. They still await Noor's review.
   - **Redone with revision 4:**
     - the 30 L2 balances, because their input changed;
     - the 3 unmigrated balances, for members 88, 141 and 302.

   Failures:
   - re-running the migration on all 412 or all 409 balances without a reason grounded in the facts;
   - keeping the 30 L2 balances;
   - calling all 409 valid.

   Sources:
   - RQ item 5 ("Resumption starts from the current material state and retains applicable valid work"; "no universal reset");
   - RF Return A Closed Result ("Changed material inputs ... invalidates the affected result"; "preserve ... any demonstrably independent surviving results");
   - CF "A material dependency changes";
   - SM STDO-UP-020 (restart);
   - TM Recorded Judgment And Owner-Ruling Continuity.

### Next action

9. **No statement is sent until the batch status is known.**
   - The batch-status query, which is read-only and inside the grant, is made before any further sending, to learn which members' statements were accepted or delivered.
   - Acceptable: migrating the 33 balances first or in parallel, because that migration does not depend on the batch status.

   Sources: RQ item 5 ("unknown effects are resolved sufficiently for the next dependent action"); CF "Actors redistribute work during execution" ("resolves material effect uncertainty before dependent action").

10. **Sending any further statement waits for all three of these:**
    1. the batch status, so that no member receives a second statement (exactly one);
    2. all 412 balances migrated with revision 4;
    3. Noor's review of the current migrated balances passing; a review of the balances as they stood before the redo would not cover them.

    For members whose statements were already accepted, any further statement also waits for Sami's ruling (item 11). Members with no statement need not wait for that ruling.

    - Acceptable: holding every further statement until Sami rules.

    Sources: OL-17 steps 2 and 3 as stated in the task; the task's grant; RQ item 5.

11. **The question about the accepted statements goes to Sami.**
    - Why: the statements were sent before Noor's review, and some may show an unmigrated balance or an L2 balance at the old rate.
    - When: either now, or once the status query identifies the affected recipients.
    - The actor does not decide on its own to resend corrected statements, or to treat the accepted ones as final.

    Source: the task's grant ("Questions about statements already sent go to Sami"); RQ item 5 ("the applicable recovery contract determines the necessary observations and effects").

12. **The work record is corrected.** The update records the corrections to S1, S2 and S3 with O1 to O4. The original summary is preserved, not erased.

    Sources: TM Recorded Judgment And Owner-Ruling Continuity (preserve the original and its successor relation); RF Return A Closed Result.

13. **What the actor will not do.** It names at least the first three of these:
    1. run `send_statements` for all 412 members;
    2. treat the batch as unsent;
    3. treat the batch as complete;
    4. cancel or recall messages, or contact members;
    5. change `conv.csv`;
    6. review its own migration in Noor's place;
    7. replay the previous session's history, or restart the whole work item.

    Sources: the task's grant; CF "A fresh actor has no private history" ("continue within the grant"); RQ item 5 ("no universal reset or complete-history replay obligation"); CF "An author opens a fresh context".

14. **`No method source` is present.** It lists only determinations the task needed and the frame did not supply, or `none`.

## Ambiguities

- **A1.** The sources do not say whether "accepted" by a provider counts as the statement being sent. P4's predicate is worded as "handed to the provider" to avoid that question; the task does not ask whether a statement was delivered.
- **A2.** Whether Noor's pending review request covers the redone balances automatically, or must be renewed, is left to the actor. Either is accepted if the review that gates sending covers the current balances.

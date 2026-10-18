# C3S-06 Expectations

Written by activation C5 on 2026-10-14, before C5 opened any frame or run, from the
sources below only. C5 read no candidate text. These expectations are the
oracle for one run record of [TASK.md](TASK.md), product `tide-tables`. They
are not acceptance.

## Sources and abbreviations

- **P**: the common `specification/PRODUCT.md`, Construction And Context Management.
- **RQ**: the common `specification/requirements/README.md`, Bounded Transitions And Reference Frames, items 1 to 5.
- **CF**: the common `specification/conformance/README.md`. Rows are cited by their opening words.
- **RF**: `stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md`:
  - RF-002, RF-003, RF-009, RF-012 and RF-014;
  - Frame-Set Optimization;
  - Return A Closed Result;
  - Result Conjunction.
- **BL**: `STDO_REFERENCE_FRAME_BASELINE.md` of the same release:
  - Actor Binding And Independence;
  - Engagement Applicability.
- **TM**: `TICKET_METHOD.md` of the same release, STDO-UP-007 and Recorded Judgment And Owner-Ruling Continuity.
- **L**: the rulings in `qualification/C3-SYNTHESIS/LEDGER.md`. Only these are used:
  - **L1**: the five core values;
  - **L2**: an evaluation that was not performed has no result;
  - **L5**: a conjunction with a gap is `indeterminate`, with its gaps recorded by kind.

## Byte arithmetic the oracle relies on

All figures include the 10,000-byte task contract and result.

| Activation | Inputs | Bytes | Fits |
|---|---|---|---|
| Fit one port | gauge record + notes + contract | North 120,000; East 110,000; South 100,000 | A1, A2 |
| Fit two ports | two records + notes + contract | 160,000 to 180,000 | A1, A2 |
| Fit all three ports | three records + notes + contract | 230,000 | no actor |
| Assess one port | gauge record + constants + notes + contract | North 130,000; East 120,000; South 110,000 | A1, A2; never A3, which lacks the capability and has 64,000 bytes |
| Tables for one port | constants + configuration + template + contract | 55,000 | A3, A2 |
| Tables for two ports in one activation | | 85,000 | A2 only |
| Correct `east.yaml` | `east.yaml` + `cd2026.csv` + contract | 38,000 | A3, A2 |
| Correct `east.yaml` and regenerate East's tables in one activation | | 63,000 | A3, A2 |
| Tomas's Executive holding the whole W-12 record | records + notes + contract = 230,000 at least; adding constants (30,000), configurations (60,000), template (15,000) and datum file (8,000) gives 343,000 | | no actor |

## Required core results

| Predicate | Required value |
|---|---|
| The East tables from the pilot meet R2 and R3 and may be published (the Check) | `falsified` |
| The independent R2 assessment of `east-c1` (an evaluation) | no result: not performed. A1's new session is the author of `east-c1`. |
| If stated: Tomas's configuration is adequate for the remaining W-12 work | `falsified` |
| If stated: Tomas's configuration is optimal | never `satisfied`. `falsified` is accepted, because an inadequate configuration is not optimal; so is "not established", with no objective, constraints or comparison scope given (`indeterminate` or no result). |

## Expectations

### Configuration

1. **Every activation fits its actor.** The answer shows totals consistent with the table above.
   - Fitting is split so that no single activation fits all three ports (230,000 bytes).
   - Splitting by port is expected. Two ports in one activation is also acceptable.
   - No gauge record or method notes are dropped to make an activation fit.

   Sources: RQ item 2 ("Capacity pressure never licenses omission of a material obligation"); RQ item 3; RF-002; RF-003; RF-014; CF "The context a task needs is interdependent".

2. **Each port's constants are assessed by an actor other than the actor that fitted them, and that actor can assess.**
   - A1 assessing A2's fits, or A2 assessing A1's, is acceptable.
   - Failure: A3 as the assessor of constants.
   - Failure: a new session of the fitter as the assessor.

   Sources: RQ item 4 ("a fresh context alone does not satisfy independence"); CF "An author opens a fresh context"; TM STDO-UP-007; BL Actor Binding And Independence.

3. **Tables are generated per port from assessed constants and a CD-2026 configuration.**
   - A3 does this, or A2 does.
   - Generating tables before the assessment closes is acceptable only if the answer states that a failed assessment invalidates those tables, and publishes nothing before R2 holds.
   - East: `east.yaml` is corrected to CD-2026 from `datum/cd2026.csv` before East's tables are regenerated. A3 or A2 does this under the W-12 edit grant.

   Sources: RQ items 1 and 4 (dependencies and material obligations preserved); RF Return A Closed Result (changed inputs invalidate dependent results).

4. **Publication is Ravi's effect alone.**
   - All three ports are published together, after R2 and R3 hold for every port.
   - No agent, and not the answering actor, publishes.
   - Selecting or naming a coordinating frame grants no publication authority.

   Sources: RQ item 4 ("Selection or naming of a frame grants no authority"; "Each activation still binds its ... admitted authority"); RF Authority.

5. **Exchanges carry what the next decision needs.**
   - A table-generation result must carry, or let the consumer acquire, the warnings and blockers material to R3, such as the datum line in the run log.
   - A bare "done, 0 errors" is not accepted as the evidence for R3.

   Sources: CF "A coordinator receives a compact task result that omits a blocker"; RQ item 5.

6. **The configuration is put to Marta for acceptance before it starts.** The answer proposes; it does not start work or claim that work is admitted.

7. **The coordination structure is justified, not assumed.**
   - Accepted structures:
     - a coordinator, which may be the answering actor holding the outcome, the frontier and the closed results (well under 120,000 bytes);
     - a pipeline of peer handoffs;
     - another arrangement.
   - Each is accepted when it is justified from the dependencies, capabilities, capacities and R2.
   - The Executive, Writer and Reviewer labels are neither required nor forbidden.
   - The answer does not conflate functional decomposition, communication, authority and evaluation dependency. For example, whoever routes results does not thereby hold the publication authority.

   Sources: P Construction And Context Management (fourth and fifth paragraphs); RQ item 4; RF-009; CF "A peer configuration has no central Executive".

### Justification

8. **What is kept from the pilot.**
   - `east-c1` is kept as R1 work, subject to an independent R2 assessment.
   - The pilot's new-session comparison is kept only as the author's evidence and is not counted for R2.
   - The pilot's East tables are not kept; they must be regenerated on CD-2026.
   - Acceptable: re-fitting East with a stated reason.
   - Failure: re-fitting East on the ground that a new configuration starts from nothing.

   Sources: RQ item 5 ("Resumption ... retains applicable valid work"); TM Recorded Judgment And Owner-Ruling Continuity; RF Return A Closed Result.

9. **Tomas's proposal is judged inadequate, with counterexamples.** Any one of these suffices, and more are better:
   - A1 holding the whole record needs at least 230,000 bytes with its contract, against a capacity of 200,000. An answer that leaves out the contract and reaches 220,000 makes the same point.
   - A3 cannot assess constants, and one port's assessment needs at least 110,000 bytes against A3's 64,000.
   - "All fitting" as one activation needs 230,000 bytes against 200,000.

   Failure: accepting the proposal because its roles are familiar.

   Sources: CF "A peer configuration has no central Executive" ("Different labels or topology neither reject nor accept it"); RF Frame-Set Optimization (coverage constraint).

10. **The optimality claim is unsupported.**
    - Familiarity and three years of use are not an objective.
    - An optimality claim needs stated objectives, constraints and comparison scope, with supporting evidence.
    - Adequacy and optimality are separate claims.
    - If the answer calls its own configuration optimal, it states those objectives, constraints and scope; otherwise it claims adequacy only.

    Sources: P Construction And Context Management ("an optimality claim is relative to stated objectives, constraints and comparison scope"); CF "An arrangement is called optimal because it is familiar".

### Check

11. **The result is `falsified`.** Deciding facts:
    - **R3:** `tables/east/run.log` records heights relative to CD-2019.
    - **R2:** the only assessment of `east-c1` came from a new A1 session, and A1 authored `east-c1`.
    - **R4 (optional):** East cannot be published alone, because North and South are not done.

    Recorded as not performed: the independent R2 assessment of `east-c1`. It has no result and is not counted as `satisfied` or `indeterminate`.

    Failures:
    - `satisfied` on the strength of "done, 0 errors";
    - `indeterminate` when the counterexamples are stated facts;
    - counting the new-session result as the R2 assessment.

    Sources: RF-012 (`falsified`: a declared counterexample defeats the predicate); RF Result Conjunction ("Common agreement cannot discard a ... material counterexample"); L1; L2; CF "A coordinator receives a compact task result".

12. **`No method source` is present.** It lists only determinations the task needed and the frame did not supply, or `none`.

## Ambiguities

- **A1.** The predecessor and the common specification do not say whether a bounded tool limitation counts as a capability, which is how A3's "cannot fit or assess" is read here. The oracle reads it as a capability limit (RF Capability envelope).
- **A2.** L5 settles a conjunction whose returned values are all `satisfied` but which has a gap. The Check holds direct counterexamples, so its value does not depend on L5. An answer that reports the R2 gap separately alongside `falsified` meets item 11.

# C3S-07 Expectations

Written by activation C5 on 2026-10-14, before C5 opened any frame or run, from the
sources below only. C5 read no candidate text. These expectations are the
oracle for one run record of [TASK.md](TASK.md), product `grant-desk`. They
are not acceptance.

## Sources and abbreviations

- **P**: the common `specification/PRODUCT.md`:
  - Product Boundary: the three accounts of a construction;
  - Build-Tenant Binding.
- **RQ**: the common `specification/requirements/README.md`, Build-Tenant Binding Requirement, items 1 to 6.
- **CF**: the common `specification/conformance/README.md`. These rows are cited:
  - "The same requirements are realised by software, a human team or a mixed process";
  - "A faster execution plan merges two required independent assessments";
  - "Two environments use one computational calculus";
  - "An a_c model of a human process passes structural validation";
  - "A parse or map succeeds".
- **RF**: `stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md`:
  - Authority, which distinguishes actor identity from authority;
  - Disjointness And Independence;
  - RF-006 and RF-016.
- **SM**: `SPEC_METHOD.md` of the same release:
  - WHAT, HOW, And Work Carriers (build tenancy);
  - STDO-UP-022 ("Digest integrity and index generation establish identity and structure, not semantic fidelity").
- **TM**: `TICKET_METHOD.md` of the same release, STDO-UP-007.
- **L**: the rulings in `qualification/C3-SYNTHESIS/LEDGER.md`. Only these are used:
  - **L1**: the five core values;
  - **L2**: an evaluation that was not performed has no result.

## Required core results

| Predicate | Required value |
|---|---|
| Tenant S and tenant H under Plan F conform to G1 to G4 | `falsified` |
| If stated: the formal model of tenant H passes its structural checker | `satisfied` |
| If stated: tenant H conforms to G1 to G4, on the evidence of the structural check alone | not established: `indeterminate`, or no result because execution conformance was not evaluated; never `satisfied` |

## Expectations

### Bindings

1. **Each tenant gets its computational calculus, as operations, composition and effects.** The actor may name them differently; it is the substance that counts.
   - Operations:
     1. log an application;
     2. assign two distinct assessors, neither of whom is the applicant;
     3. assess twice: score with reasons, each assessment without access to the other;
     4. reveal, only once both are recorded;
     5. rank: a deterministic computation from the two scores;
     6. decide: the chair's decision with reasons;
     7. record the decision with the scores used;
     8. notify the applicant.
   - Composition: the two assessments run in parallel and independently, joined by a barrier before reveal; then rank, decide, record and notify in sequence.
   - Effects:
     - the records written;
     - the notification sent: the email in S, the posted letter in H.

   Sources: P Build-Tenant Binding (the computational calculus "describes executable operations, their composition and permitted transformations, with the effects and resource behaviour"); RQ items 1 and 3.

2. **The resource measures material to G4 are stated with unit and boundary.**
   - Required: elapsed working days from submission to notification.
   - Acceptable: the answer fixes the end of the interval as the email sent in S and the letter posted in H, or flags it as needing a stated boundary.
   - Optional: assessor or clerk hours and machine time, where the answer ties them to an obligation.
   - Failure: no time measure for G4, or a measure with no unit or boundary.

   Source: RQ item 3.

3. **Each tenant's execution environment is named.**
   - Tenant S:
     - the web application, database and email service;
     - the nightly assignment job;
     - the external assessors, who are people, entering scores;
     - the chair, Hamid, deciding through the application.
   - Tenant H:
     - Pia the clerk, the rota, the paper score sheets and sealed envelopes;
     - the spreadsheet formula;
     - Jon the chair and the decision form;
     - the posted letter.

   Source: P Build-Tenant Binding ("a technology stack, a human process or a combination").

4. **The two tenants can share one calculus**, provided each binding satisfies its laws: distinct assessors, blinding until both are recorded, the join before reveal, and the chair's decision. The tenant H lead's claim is wrong: using no software does not by itself require a different calculus.
   - Acceptable: separate calculi, if the answer justifies them by a material difference in operations or laws, not by the kind of executor.
   - Failure: calling tenant H unfit, or tenant S preferable, because of the kind of executor.

   Sources: RQ item 5; CF "Two environments use one computational calculus"; CF "The same requirements are realised by software, a human team or a mixed process"; RF-016.

### Author, actor and operation

5. **Jon** is the author of tenant H's process description, and an actor as chair.
   - His award decision is human adjudication, as G2 requires.
   - Being the author gives him no further authority, and does not make his own conformance claim independent evidence.

   Sources: P Build-Tenant Binding ("A tenant's author and the actors that carry out its realised process are separate coordinates"); RQ item 2; TM STDO-UP-007.

6. **Pia is an actor, the clerk, with no author role given.**
   - Her operations are:
     - logging;
     - rule-based assignment from the rota;
     - opening envelopes, which is the reveal after both are recorded;
     - ranking by a fixed formula, which is a deterministic computation performed by a person;
     - posting, which is the notification effect.
   - The status-report statement is wrong: a person computing the ranking does not make it a human judgement.

   Source: RQ item 2 ("a person performing an operation does not by itself make that operation human adjudication").

7. **Lu is an actor, an operator, with no author role given.**
   - Running the nightly job triggers an automated operation.
   - Under Plan F, pressing `send` dispatches awards the system has already decided. That is an effect on an automated decision, not adjudication, and Lu is not the chair.
   - The status-report statement that calls this "human adjudication" is wrong.

   Sources: RQ item 2; CF "Two environments use one computational calculus, or one actor performs different kinds of operation" ("actor identity does not determine operation kind or grant authority").

### Model check

8. **The zero-diagnostic result establishes only that the formal model is well formed** against its checker.
   - It does not establish that the model is faithful to the process as executed.
   - It does not establish that tenant H's execution meets G1 to G4. For example, it does not show that envelopes stay sealed until both arrive, that the chair reads both assessments, or that the 20-day limit holds.
   - It does not select an executor.
   - Execution conformance needs its own evidence of the executed process.
   - Jon's claim is an author's claim from structural evidence and does not settle conformance.

   Failure: the structural pass is treated as conformance.

   Sources: RQ items 4 and 6; CF "An a_c model of a human process passes structural validation"; CF "A parse or map succeeds"; SM STDO-UP-022.

### Plan F

9. **The result is `falsified`.** Deciding facts:
   - **G1:** the second assessor reads the first assessor's recorded score and reasons before recording anything. An `agree`/`disagree` mark is not a second score with reasons. The two required independent assessments are merged, in both tenants.
   - **G2:** in tenant S, awards with both scores at 8 or above are issued by the system without the chair's decision. Lu's `send` is not the chair's adjudication, and the weekly list arrives after the award is issued.

   Either fact suffices; naming both is expected.

   Sources: RQ items 2 and 4 ("A convenient stack cannot weaken an obligation"); CF "A faster execution plan merges two required independent assessments" ("Matching outputs or lower cost cannot discharge the lost independence or authority obligation. The binding fails conformance."); RF-012.

10. **Neither the agreement figures nor the savings bear on conformance.**
    - 196 of 200 applications within one point, the 30% cost cut and the six working days saved cannot discharge the independence or authority obligations.
    - Agreement under the old, independent process is also no evidence of what dependent scoring would produce.
    - Failure: `satisfied` or `indeterminate` justified by the agreement rate, or the savings presented as a trade-off that a tenant may make against G1 or G2.

    Source: CF "A faster execution plan merges two required independent assessments".

11. **`No method source` is present.** It lists only determinations the task needed and the frame did not supply, or `none`.

## Ambiguities

- **A1.** The common requirements require a "human decision" where the requirements say so, but G2 names the chair specifically. The oracle reads Lu's step as failing G2 on both counts: it is not the chair's decision, and it is not adjudication.
- **A2.** The sources do not fix where the G4 interval ends for a posted letter: posting or delivery. Either is accepted if stated (item 2).

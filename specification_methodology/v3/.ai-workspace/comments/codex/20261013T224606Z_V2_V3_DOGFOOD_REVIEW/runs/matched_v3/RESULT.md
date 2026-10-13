# Source-use assessment: Tasks A and B

**Common precondition.** The packet contains no verified Product basis selection (`stdo-work` › *Select The Product Basis* → `PRODUCT_BASIS.md`). It also contains no accepted Project Reference-Frame Basis (`stdo-work` › *Acquire The Responsibility Frame*). Both answers below are therefore conditional on those bindings. The frames are non-deciding views and grant no authority (WORK_RECOVERY preface; README › *Distribution and entry*).

---

## Task A: aborted suite, reviewer with evaluation authority only

**P's result**

| Field | Value |
|---|---|
| Predicate | "all required tests pass on C at B" |
| Verdict | `falsified` |
| Performance | `performed`, with partial extent: t1 ran and failed under authentication, and the suite aborted before t2 |
| Original outcome | Suite aborted. The cause of the abort is not supplied and must be recorded as unknown, not invented. |

- A suite aborted after a witnessed failure is performed and falsifies "all tests pass". It is not a never-run test (FOUNDATIONS › *Result algebra*, interruption paragraph).
- The abort does not erase the authenticated t1 counterexample (*Result algebra*, "An aborted procedure does not erase…").
- Under conjunction rule 1, any authenticated, applicable falsification of a required predicate makes P `falsified`, and missing coverage stays explicit alongside it (FOUNDATIONS › *Result conjunction*).

**Treatment of missing t2**

- t2 is an absent coverage slot. No t2 result is fabricated, and t2 is neither passed nor failed (*Result algebra*, "missing required judgment"; *Result conjunction*, "Sequential composition records an unreturned dependent evaluation as an absent slot").
- Its performance fact depends on the evidence:
  - `not_performed` only if the abort record authenticates that t2 never started.
  - `unconfirmed` otherwise.
- t2's own predicate stays `indeterminate` unless independent counterevidence exists.
- t2 cannot rescue P. A recovery path need not make t1 true either (*Result conjunction*).

**What is known about deployment**

- The effect value is separate from P's verdict and does not change it (*Result algebra*, effect paragraph).
- The admission controller's observation must first be authenticated against its producer, subject and basis (*Result conjunction*, authentication paragraph). Its standing then depends on whether deployment was a requested part:
  - If deployment was a requested part, it is `not_started`.
  - If it was an unrequested possible part observed not to begin, it is `not_requested` at that boundary.
  - The packet does not say which applies, so this remains open.
  - If the observation cannot be authenticated, the deployment part is `unknown`.
- This covers only the deployment part. Any other material effects the suite may have had stay `unknown` unless the operating model establishes an effect-free scope. Lack of a request alone is insufficient (*Result algebra*).

**Reviewer limits**

- **May not edit C.** Evaluation supplies no operation grant (TRANSFORMATION_LIBRARY › *Evaluate*; RF-006; RF-007). Authoring the subject would also defeat review independence (TICKET_METHOD › UP-007).
- **May not declare acceptance.** The reasons:
  - An assessment verdict is not acceptance authority. The reviewer returns evidence plus a *proposed* disposition, which needs a supported cause (SPEC_METHOD › UP-020 *Proportional Disposition*).
  - Availability, fitness and authorised acceptance are three separate predicates (*Result algebra*, last paragraphs).
  - Only the Executive applies a disposition, as a separate decision result. That result does not overwrite the assessment (UP-020 *Proportional Disposition*).
  - Even if P had been satisfied, the reviewer still could not accept.
- **Durability.** The verdict must be durably traceable on an existing carrier to support any later decision (UP-007).

**Owner sections needed beyond the packet (A)**

- **Required test set.** The evaluation rule or plan that fixes t1 and t2 as required, owned by the domain/test owner (*Applicability And Required Results*).
- **Roles.** `STDO_REFERENCE_FRAME_BASELINE.md` › *Status and authority boundary*, plus the Reviewer and Executive clauses, if the project adopts that profile. WORK_RECOVERY says to acquire these separately.
- **Executive mandate.** The Executive's decision mandate from the accepted Project Reference-Frame Basis or the work contract.
- **Deployment effect boundary.** The effect-boundary declaration and operating model for this evaluation. This includes whether deployment was a requested part, and the controller's owning interface (FOUNDATIONS › *Workspace and context*).

---

## Task B: resume after context loss, dispatched irreversible request

**May be reused**

- **Workspace progress and durable records**, including the dispatch receipt. Discarded private context does not reset the workspace; resumption reconstructs context from the workspace and authoritative inputs (FOUNDATIONS › *Workspace and context*; `stdo-work` › *Acquire*).
- **The unchanged design judgment, conditionally.** It is reusable only after checking that its question, subject, basis, support and revising observation still apply (SPEC_METHOD › *Computed Classification And Treatment*, last paragraph; `stdo-work` › *Classify*).
  - If its support depends on the changed requirement, it reopens.
  - If independence from that change cannot be established, the wider scope must be inspected (*Workspace and context*, reuse paragraph).
  - A role or session change alone does not force reclassification.

**Must be reacquired or reconciled before any retry**

1. **Delivery effect.** The state is `unknown`.
   - Dispatch proves neither completion nor absence, and a lost acknowledgment after possible execution is `unknown` (*Result algebra*, effect paragraph).
   - The message is irreversible, so it cannot be dropped from the effect boundary.
   - Idempotence is not established, so retry is not permitted. The worker must first observe or reconcile through the delivery service's owning interface, within the existing operation grant. Otherwise it must select another permitted action or return the unresolved result (*Workspace and context*, last paragraph; TRANSFORMATION_LIBRARY › *Work/recovery specialization*, F2/F3/F6 row; *Computed Classification*, "an unknown effect state cannot be silently treated as no effect").
   - Elapsed time or a timeout is not repair (FOUNDATIONS › *Bounded construction*).
2. **Older test receipt.** It is bound to a different requirement digest, so it cannot satisfy a dependent conjunction.
   - A mismatched basis is `invalid_basis` or requires reactivation (RF-005; *Applicability And Required Results*).
   - A stored green label is not a validity argument (*Workspace and context*).
   - Affected tests need a fresh evaluation against the current requirement, unless a computed C result over the current inputs establishes that the change does not affect them.
3. **Requirement and contract binding.** The worker must:
   - confirm the current digest is the admitted operative requirement (`stdo-work` › *Establish The Work Basis* step 4);
   - resolve the affected work-contract bindings and grant before any effect (UP-020 › *Construction, Assessment, And Delegation*, last paragraph).
   - If the governing meaning changed, the work re-enters at the requirement layer.

**Neither an empty log nor a task label settles completion or authority**

- An empty local log does not establish no effect or absence (*Result algebra*; *Workspace and context*, "Absence from … empty local record").
- A task label grants nothing:
  - Bind: "A name, path, cached result or available tool is no grant."
  - RF-006.
  - `stdo-work` step 3: ticket presence or `active` status cannot supply admission.
  - *Computed Classification*: "A label or filename cannot select the route".
- Completion requires condition-based conjunction of the applicable obligations (TICKET_METHOD › *Condition-Based Closure And Reuse*). With the delivery effect `unknown` and the test result stale, closure is withheld.

**Owner sections needed beyond the packet (B)**

- **Ticket rules.** TICKET_METHOD › *Recorded Judgment And Owner-Ruling Continuity* and › *Work-Carrier To Execution Rule*. Both are cited as owners but not projected in the packet.
- **Operation grant and delivery contract.**
  - The actual operation grant: whether it permits observing the service's status.
  - The delivery service's domain contract: whether a query or correlation key exists, and its idempotence semantics.
  - Neither is supplied, and no external observation is assumed here.
- **Requirement succession.** SPEC_METHOD intake and requirement-succession clauses (`stdo-work` step 4), to establish which requirement is operative.
- **Design admission and traces.** DESIGN_MODULE_METHOD › UP-016/017 and the accepted-design trace bindings, if the design judgment's support traces to the changed requirement.

---

## Required next acquisition

| Task | What to acquire |
|---|---|
| Both | A verified Product basis and the accepted Project Reference-Frame Basis |
| A | The authenticated plan of required tests; the controller observation's provenance; the effect-boundary declaration; the Executive mandate |
| B | An authoritative delivery-state observation, via the owning interface under the grant; the current requirement's admitted status; the design judgment's support record; a fresh test evaluation at the current basis |

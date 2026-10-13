# Source-use assessment: Task A and Task B

This assessment relies only on the supplied entry packet. The packet is a projection, and raw owning standards stay authoritative wherever it is insufficient (`stdo_bootstrap.md` steps 5 and 8; `stdo_compressed.md` § Prompt-Relevant Rules). I did not verify any source digests.

---

## TASK A: Reviewer result on predicate P

**P's result: `falsified`.**
- P claims that *all* required tests pass on C at B. An authenticated failure of required test t1 on that exact C/B is a counterexample, so P is falsified.
- This result is closed and determinate. It does not depend on t2.
- Sources: § Reference Frame Engagement Compression (result family; Reviewer payload projection, where "`falsified` carries findings and supported or explicitly indeterminate triage").

**What is known about the evaluation:**
- The suite started, produced the t1 failure, and then aborted before t2. The evaluation is therefore incomplete as a coverage of the required-test population.
- The finding set is known to contain t1. It is not known to be exhaustive.
- The cause of the abort, and whether it relates to t1, is unknown. Triage on those points stays explicitly indeterminate; it is not inferred.
- The counterexample is returned at its causally minimal supported frontier, which here is t1. The abort is not treated as a second finding without evidence. Source: § Product Testing Frame Compression (counterexample localization).

**Treatment of missing t2:**
- t2 is **unevaluated**. It is neither passed nor failed.
- It cannot be converted to satisfaction (§ Reference Frame Engagement Compression: "Missing context, evidence… cannot be converted to satisfaction").
- No claim may extend to the whole population. Quantifier and scope cannot outrun evaluated evidence (§ Prime Operating Rules, mechanical enforcement).
- Record t2 as an explicit residual, together with these invalidation conditions:
  - any change to C or B;
  - loss of authentication of the t1 result;
  - a completed re-run.
- Whether to re-run is not the Reviewer's decision.

**What is known about deployment:**
- The Reviewer did not observe deployment.
- The task record supplies the admission controller's independent observation that no deployment was started. The Reviewer may cite that observation only as supplied external evidence, attributed to the controller, with the controller's own basis and time. It is not a Reviewer finding.
- That observation is outside P. It neither supports nor alters the P result.
- It is returned separately as an adjacent outside-claim observation (§ Reference Frame Engagement Compression; § Traversal Occurrence Profile: "Mutable reality remains external").
- It also does not establish whether deployment is permitted or blocked in future. That falls under disposition.

**Editing C or declaring acceptance:**
- **The Reviewer may do neither.**
- The Reviewer "does not edit, direct repair, apply an STDO disposition, or authorize continuation," and it assigns no priority or boundary effect (§ Reference Frame Engagement Compression).
- The Executive consumes the closed result, assigns priority and the promotion-boundary effect, and applies exactly one `STDO-UP-020` disposition.
- The Executive also may not mutate C. Any repair needs a separately bound Writer activation under an owner grant.
- A review event never supplies closure or acceptance (§ Treatment, Judgment, And Closure).
- Any repair proposal acquires obligation only through its owner.

**Owner material needed beyond the packet:**
- `STDO-UP-020` disposition set, plus `STDO-UP-007` and `STDO-UP-022` (Reviewer evaluation law). Their owning sections are not in the packet.
- `REFERENCE_FRAME_METHOD.md` result algebra and `STDO_REFERENCE_FRAME_BASELINE.md` Reviewer payload and Proof-frame sections.
- The Product's Project Reference-Frame Basis: severity scales and hard stops.
- The admitted execution contract or evaluation criteria that define the **required-test inventory** (needed to confirm t1 and t2 membership) and the evidence-authentication rule.

---

## TASK B: Resumed Worker with an ambiguous irreversible dispatch

**What may be reused** (§ Treatment, Judgment, And Closure: "Reuse current facts, judgments and reconstruction across roles or resumption"):
- **The durable dispatch receipt.** It is an established fact that a dispatch occurrence was recorded, under the receipt's provenance. It establishes neither delivery nor non-delivery.
- **The unchanged design judgment.** This is conditional. It is reusable only after checking its recorded question, subject, basis, support, and revising observation. If its support includes the requirement whose digest changed, the affected part is invalidated until revalidated. "Unchanged bytes" is not "unchanged premises."
- **Lost private context.** This alone does not force reclassification or a restart. Prior-worker memory is not authority. Reconstruct from durable carriers only (§ Prime Operating Rules: design evidence "without… prior-worker memory"; Writer grant/restart rule).

**What must be reacquired or reconciled before any retry:**
1. **External delivery state.**
   - Acquire it through the delivery service's owner surface, or through the Product's admitted external-fact route.
   - "Observation, result, evidence, checkpoint, event, projection, cache… cannot replace" mutable external reality (§ Traversal Occurrence Profile). Assurance acquires truth "through the exact runnable owner surface" (§ Product Testing Frame Compression).
   - No such observation is supplied, so the state is **unknown**.
2. **A fresh effect-readiness judgment.**
   - It must bind the current observation, invocation, operation, territory, and grant. Stale readiness never dispatches.
   - A retry is a fresh occurrence over the then-current subject, not a continuation of the old one (§ Traversal Occurrence Profile).
   - Because the effect is irreversible and idempotence is not established, a retry while delivery state is unknown risks a duplicate irreversible message.
   - The possible prior effect stays an explicit residual with bounded post-observation.
   - If reconciliation cannot resolve the state, the Worker refuses and returns. It does not retry.
3. **The requirement basis.**
   - The current requirement digest differs from the one the old test receipt used. That is a material invalidator.
   - The old receipt cannot serve as current conformance evidence. Affected assurance must be re-run (§ Reference Frame Engagement Compression, steel thread: "rerun affected assurance on material invalidation").
   - If the changed requirement alters the contract's governing requirement or the request content, refresh the binding or re-enter at the requirement owner. The Worker cannot self-select the new meaning (§ Work Carrier; `SKILL.md` § Establish The Work Basis step 4; § Reference Frame Engagement Compression drift locks).
4. **Grant and territory currency.**
   - Confirm that the inherited owner grant still names this subject, operation, and territory. "Refresh bindings on material change" (`SKILL.md` § Construct And Prove).
5. **Recording.**
   - Record the unknown effect state, the stale test evidence, and the withheld closure in the contract's durable result/evidence surface. A conversation return alone is insufficient (§ Work Carrier And Execution Contract).

**Can an empty local log or a task label settle completion or authority?**
- **No.**
- An empty local log is not the external owner's projection. Assurance "may not reconstruct a rival owner state from… events, logs, labels." Reconstructed state "is not self-authenticating." Silence "proves neither progress nor failure."
- A task label or role name grants no effects or admission. "The Worker label grants no mutation authority," and "ticket existence, lane placement, `active` status… cannot supply admission" (§ Prime Operating Rules; § Reference Frame Engagement Compression; § Work Carrier).

**Owner material needed beyond the packet:**
- `TRAVERSAL_OCCURRENCE_PROFILE.md` raw sections for:
  - the effect-disposition and external-fact-admission event contracts;
  - effect-readiness;
  - partial-effect post-observation.
- The Product's accepted design for this delivery admission relation, specifically:
  - the semantic commit unit;
  - post-validation partial-failure boundaries;
  - reconstruction;
  - idempotence and deduplication law;
  - the OperationKind contract.
- The delivery service's owner reconciliation surface.
- `STDO_REFERENCE_FRAME_BASELINE.md` Effect-frame section.
- The Worker's exact grant and execution contract.
- The requirement owner's successor or supersession record, mapping the old digest to the new one.
- `TICKET_METHOD.md` J/O reuse fields for revalidating the design judgment.
- Retry-under-ambiguity policy. The packet does not decide this; it belongs to the effect or operation owner.

---
name: stdo-work
description: Execute one admitted STDO work item through its lawful re-entry point. Use when a user says stdo work or explicitly asks to perform requirements, design, code, or test work under an STDO-governed basis. Do not invoke for generic non-STDO development.
---

# STDO Work

Deliver the smallest causally closed change authorized by one exact work basis.
The admitted re-entry point decides where work begins.

## Select The Product Basis

Read and apply
[`PRODUCT_BASIS.md`](../../references/PRODUCT_BASIS.md) before drafting an
execution contract or changing any surface. Continue only from its exactly-one
verified selection; that selection grants no work or mutation authority.

## Establish The Work Basis

1. Establish applicable upstream work authority under the verified definition
   and immutable basis. Without it, stop before
   selecting a carrier; a ticket cannot substitute for that authority. Then
   select the first applicable source for one run-scoped execution contract:

   - reuse an exact admitted durable ticket when it covers the work;
   - otherwise require one authorized durable ticket only when work or an
     obligation needs independent state beyond its admitted sprint or, outside
     a sprint, beyond the current run;
   - otherwise use the admitted sprint plus one manifest-local iteration entry
     when the work ends by sprint close; or
   - otherwise use an intake draft for work that ends in the current run.

   Do not invoke `stdo-ticket` automatically. Absence of a ticket neither
   requires nor authorizes creating one.
2. Bind the contract's current Goal or exact work instruction, `change_intent`,
   change class, re-entry point, `target_truth`, relevant `superseded_truth`,
   `closure_law`, governing requirement and accepted design, checkpoint,
   affected relation set, write territory, evaluation criteria, non-closure
   conditions, proof surface, and one Product-bound durable result/evidence
   surface. If that result surface is unavailable or unauthorized, admission
   must refuse.
3. Validate and admit or reject that exact contract. Drafting, admission, and
   execution may occur in the same invocation, but ticket presence, `active`
   status, a generic work request, or the model's own draft cannot supply
   admission. Continue only after deterministic admission or an exact human
   override of the bounded contract. Record the Product-bound admitting
   mechanism and authority, exact contract identity or digest, decision, and
   evidence. If those coordinates are absent, return the missing authority and
   stop.
4. Re-enter at the first changed layer and flow forward:

   - requirement change: establish the successor/current requirement as the
     sole operative truth; supersede or withdraw a published live domain
     artifact instead of mutating it in place;
   - design change: admit the structural decision before implementation relies
     on it; or
   - realization change: prove upstream Goals, Intent, Product, requirements,
     and accepted design remain unchanged.
5. If work discovers an obligation that needs state beyond its local carrier
   boundary, do not claim closure or create a ticket without authority. Persist
   it only when the current exact grant already includes ticket-state mutation
   for that obligation. Otherwise retain it in the contract's named durable
   result/evidence surface or an already-authorized enclosing carrier, mark
   closure withheld, and return the required re-entry plus an explicit
   `stdo-ticket` route without invoking it. A conversation return alone is not
   durable evidence.

## Construct And Prove

1. Work inside the smallest coherent causal cone and exact write territory.
   Preserve solution space where variation cannot change a governed property.
2. Implement and self-review the bounded change.
3. Derive tests through:

   ```text
   work carrier -> triage -> re-entry -> requirement/design/module/closure law
   ```

4. Use the cheapest focused falsifier adequate for the claim. Add integration,
   installed-development, harnessed sandbox, or live sandbox evidence only
   where the Product claim requires it. A real probabilistic boundary requires
   a live lane.
5. Reconcile authority, design, implementation, tests, and displaced rival
   paths before claiming a candidate.
6. Return the exact candidate and stop. Product-owned decision authority, or an
   authorized Executive when that profile is adopted, decides whether Product,
   qualification, release, risk, or admitted-work law requires independence
   and separately activates `stdo-review`.

## Return

Return the exact candidate/checkpoint, changed paths, affected authority,
execution-contract admission mechanism/result/evidence, focused and broader
proof, non-changes, residuals, and closed or withheld work result. Do not
self-accept, discard a surviving obligation, or silently continue after return.

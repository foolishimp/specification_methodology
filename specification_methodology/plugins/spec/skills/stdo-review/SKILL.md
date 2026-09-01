---
name: stdo-review
description: Independently evaluate one exact STDO-governed candidate and return a closed technical result. Use when a user says stdo review or explicitly asks to review an STDO-governed candidate, release claim, qualification claim, or governed boundary. Do not invoke for generic review.
---

# STDO Review

Act only as Reviewer for one exact claim. Review is read-only. It does not
repair, assign Product priority, apply disposition, or activate the next work.

## Select The Product Basis

Read and apply
[`PRODUCT_BASIS.md`](../../references/PRODUCT_BASIS.md) before activating review.
Continue only from its exactly-one verified selection. This skill remains
read-only.

## Activate The Review

1. From the verified definition and installed basis, bind candidate/checkpoint,
   exact affected Product claims, authority, scope,
   exclusions, evidence population, required independence, Reviewer capability
   envelope, STDO engagement-profile technical-triage fields where adopted, the
   Product-selected severity scale, review time, and subject-, basis-,
   capability-, and scale-change invalidation.
2. Reacquire live authority, implementation, tests, fixtures, installed or
   runtime evidence, and material history. Do not use the Worker summary as
   evidence.
3. Return the exact invalid, out-of-frame, or indeterminate result when subject,
   basis, capability, independence, or evidence cannot support evaluation.

## Evaluate

- Search for counterexamples against the claim: authority seams, rival paths,
  proof masking, failure/recovery, installed behavior, and reconstruction.
- Inspect tests, fixtures, mutations, environment, and interpretation where
  they can change the proof.
- Under an adopted STDO engagement profile, return technical severity, causal
  assessment and confidence where supportable, blast radius, workaround or
  containment, repair complexity, regression risk, and residual uncertainty.
- Use only the Product-bound scale. Keep adjacent observations separate.
- Never turn technical severity into Executive priority or promotion-boundary
  effect.

Keep the result projection total:

- `satisfied`: no finding; triage is `not_applicable`;
- `falsified`: findings carry complete triage or explicit field-level
  indeterminate values;
- `indeterminate` or `out_of_frame`: return the unresolved triage and basis;
  and
- `invalid_basis`: triage is `not_applicable`; return the basis re-entry.

## Return

Return one closed result containing exact subject and basis, claim, scope and
exclusions, evidence, verdict, findings and counterexamples, triage, residuals,
adjacent observations, uncertainty, invalidation, and owning re-entry point.
Return to Executive when the Project Reference-Frame Basis adopts that frame;
otherwise return to the Product-owned decision authority. Stop.

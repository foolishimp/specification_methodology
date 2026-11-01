---
name: stdo-continuation
description: Use when resuming interrupted or prior governed STDO work in this repository, reconciling observed effects before retry, reporting truthful status and closure, or capturing qualification evidence. Keeps candidate availability, indeterminate assessment, and not-performed distinct. Not for unrelated tasks.
---

# STDO continuation, status, and evidence

Use this skill on resume, after an interruption, when writing status, or when
recording evidence for qualification.

## Resume and reconcile (SK-08, Q07, Q08)

On resume or after an interrupted effect:

1. Acquire the material current state (re-observe the targets and read the
   retained records) before any retry.
2. Reconcile observed effects: if a target already changed, do not repeat the
   effect; a timeout does not prove rollback, and a repeated request must not
   duplicate an uncertain effect.
3. Retain unresolved obligations and still-valid evidence; invalidate only the
   reliance actually affected, each with its reason.

Two histories with identical candidate bytes are not interchangeable: one may
carry a current accepted assessment and another an unresolved counterexample that
invalidates its assessment. The retained obligation cannot disappear into a
candidate-only summary — the continuations differ (Q07).

## Status and closure (SK-09, Q09, Q10)

State what was actually constructed, assessed, and decided: the exact subject,
the basis, the evidence, and the remaining work.

- Distinguish, with the correct predicate, the three outcomes: an exact
  **candidate is available**; an assessment was **performed but indeterminate**;
  an assessment was **not performed** (no result) and remains a residual. Never
  collapse these into one "done" or one "exhausted" verdict (Q10).
- Closure follows the applicable predicates and required dispositions — not a
  test count, not the mere occurrence of a review, not a fluent summary.
- An unsupported or unperformed case stays visible; it is never reported as a
  passing result.
- When a governed source or candidate materially changes, withdraw the affected
  reliance (including a prior passing review) and keep the missing reassessment
  open; unrelated valid observations remain reusable (Q09).

## Capture evidence (SK-12, Q01, Q12)

For any qualification trial, retain the actual invocation, the acquired inputs,
the outputs, the tool traces, the observed effects, the elapsed time, and any
reported token or cost data. Measures that are unavailable stay **unknown** — do
not invent them. Compare equivalent substantive information, and count retries,
repair, and review in the total cost. One passing trial is bounded evidence for
the exact case, host, and settings observed; it is not a success rate or a
general benefit claim. A keyword or formatting check may establish structure but
not successful method application.

## Composition at handoff or re-entry (SK-13)

Apply the [composition route](../stdo-tool-operations/references/composition.md)
when the task crosses Products or requires a controlled view. Bind the child's
actual actor/purpose/route rather than forwarding the parent's accumulated view.
Inspect changed grants/declarations and preserve previous exposure, currentness
and unresolved obligations. A wider Reviewer inspection does not authorize Worker
disclosure; neither deletion nor narrower permissions unexpose an actor.

## Method sources (cited, not reproduced)

Within `stdo://releases/v3.0.1-rc.1/standards/`: `ACTIVATION.md` sections 5 and 7
and `FOUNDATIONS.md` (observation sufficiency) for restart, retained results, and
invalidation; `ACTIVATION.md` section 3 for result and disposition;
`EVALUATION.md` section 7 and `ASSURANCE.md` sections 7 to 9 for test semantics
and actual-path proof.

## Scope and limits

This skill records and reconciles; it does not itself qualify host behavior or
grant acceptance.

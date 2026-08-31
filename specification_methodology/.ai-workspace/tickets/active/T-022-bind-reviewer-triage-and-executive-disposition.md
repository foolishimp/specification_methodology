# T-022 - Bind Reviewer Triage And Executive Disposition

- id: T-022
- title: Bind technical triage to Reviewer and Product disposition to Executive
- type: feature
- ticket_category: constitutional
- status: active
- review_status: changes_requested
- goal: >-
    Make finding evaluation proportional while preserving one Executive over
    the complete Product and current MVP or release mandate.
- change_intent: >-
    Let Reviewer return severity and technical implications, then let Executive
    alone assign priority, boundary disposition, and the next authorized action.
- change_class: requirement_reprice
- re_entry_point: specification/standards/STDO_REFERENCE_FRAME_BASELINE.md
- triaged_at: 2026-09-01
- created_at: 2026-09-01
- updated_at: 2026-09-01
- owner: specification_methodology
- pen_holder: codex
- work_authorization: direct_human_authorization_2026-09-01

## Intake Triage

The optional profile already separates Reviewer evaluation from Executive
decision authority. It does not yet bind the traditional distinction between
severity, priority, release or MVP boundary effect, and action. This is changed
requirement truth inside the existing profile, not a new Product or frame
runtime.

## Governed Outcome

1. Reviewer returns one closed technical triage with evidence, affected claim,
   severity, causal assessment where supportable, blast radius, workaround,
   repair complexity and risk, confidence, and residual uncertainty.
2. Reviewer assigns neither priority nor boundary disposition and cannot direct
   repair, continuation, acceptance, or publication.
3. Executive consumes the result with the exact Product view and current MVP or
   release mandate, then assigns priority, applies the existing disposition,
   and selects only an already-authorized action.
4. A project binds its severity and priority scales, decision cutoff, and
   non-waivable hard stops in its Project Reference-Frame Basis.
5. Severity and priority do not mechanically create release-blocking status.
   Blocking remains claim-relative and authority-bound.

## Non-Closure Conditions

- adding severity or priority to the pure Reference Frame Method result algebra;
- allowing Reviewer to schedule, disposition, repair, or activate another frame;
- letting Executive silently rewrite unsupported Reviewer evidence;
- making every observation a release blocker or mandatory review round;
- imposing one global numeric scale on every Product; or
- retargeting the accepted source-project frame basis to mutable profile bytes.

## Changed Surface

- `specification/GOALS.md`
- `specification/standards/STDO_REFERENCE_FRAME_BASELINE.md`
- `specification/standards/templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md`
- `specification/standards/authority_compressions/stdo_bootstrap.md`
- `specification/standards/authority_compressions/stdo_compressed.md`
- `tests/test_reference_frame_boundaries.py`

## Current Review Evidence

The first lean a_c-guided review returned `falsified` for the exact prior
52-member candidate aggregate
`554646747e6ba2227b4d0ad2b714764e1014173ad18532266de738476a073d26`.
Its exact result is retained at
`../stdo_representation/dogfood/rc2-self-review/lean-run-001/reviewer-result.md`.
It found three material S2 gaps: one contradictory compression sentence,
substring-only focused proof, and a non-consumable closure assertion in this
ticket. That result was later invalidated for the live candidate by an
independent standards-schema change, but remains exact evidence for the subject
it evaluated.

Closure now requires repaired compression, executable branch and refusal
coverage, and a fresh exact-subject Reviewer result that binds the current
candidate, activation, evidence, scale direction, Reference Frame Method result,
findings, and residuals. The ticket remains active until that evidence exists.

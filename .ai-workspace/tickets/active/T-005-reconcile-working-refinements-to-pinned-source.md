# T-005 - Reconcile Working Refinements To The Pinned Companion Source

- id: T-005
- title: Reconcile the four working refinements to the pinned companion source
- type: correction
- ticket_category: ordinary
- status: active
- review_status: candidate_ready_for_review
- goal: >-
    Make the four working refinements checkable against the companion surface
    this method pins, so a later re-cut of that program is detectable rather
    than silent.
- change_intent: >-
    Restate the refinements in the order and sense the pinned companion
    carries, cite the grounding experiment for each, and scope them explicitly
    to the Markov construct rather than to entity cuts.
- change_class: requirement_reprice
- re_entry_point: specification/standards/WORLD_MODEL_METHOD.md
- triaged_at: 2026-07-27
- created_at: 2026-07-27
- updated_at: 2026-07-27
- owner: specification_methodology
- pen_holder: claude
- predecessor_release: v2.2.2 at 124d0f8ee25e5a9a547cafdaffa4fea0523b45a4
- target_release_line: 2.2.3

## Intake Triage

**Substantive?** Yes, but narrowly. It changes how a normative section states
its relation to its evidence source; it changes no admissibility condition.

**Boundary crossed?** Normative standards. One member,
`WORLD_MODEL_METHOD.md`, one section.

**Upward-propagation walk.** The refinements were a faithful projection of a
source that has since been re-cut. Nothing downstream is wrong; the projection
drifted. First missing layer is the requirement text.

**Derived change class.** `requirement_reprice`.

**Affected span.** One of 41 members. No compression binds it.

**Release scope.** One bounded successor, `2.2.3`, over released `v2.2.2`.

## Defect

Carried over from the predecessor World Method review as finding F4, open and
uncarried by `2.2.2`.

The method stated four working refinements as "indicated by the empirical
program", in an order and wording that no longer match the companion's §15.2.
The set survived; the order, the emphasis, and the grounding were not
checkable against the source. None of the four cited the experiment that
grounds it, so drift in either direction was undetectable by reading.

Finding F3 of the same review — the cited experiment range excluding the
decisive experiment 20 — was already discharged in `2.2.2`, which cites
"experiments 08 onward" and names experiment 20 and its multi-layer successor
explicitly.

## Change

1. Refinements restated in the pinned companion's order and sense:
   geometric-not-set-theoretic; schemas sense and fragment; core identity not
   core size; identity is a DC shift not a principal-variance axis.
2. Each cites its grounding experiment (17; —; 15 and 16; 18).
3. A stated reconciliation rule: the pin in *Companion Surfaces* fixes which
   reading this method adopted, so a later re-cut is detectable.
4. Scope made explicit: the refinements constrain the Markov construct and
   overlays built on it, and are not admissibility conditions for entity cuts.

## Conserved

All four findings survive in substance. The exclusion of principal-component
and maximum-variance constructions as identity directions is retained and now
carries its grounding experiment. No admissibility condition, publication
requirement, or law elsewhere in the member changes.

## Exclusions

No change to entity-cut admissibility, the geometric construction law, the
epistemic status of the construct, or any other standards member. This ticket
does not tap `2.2.3`.

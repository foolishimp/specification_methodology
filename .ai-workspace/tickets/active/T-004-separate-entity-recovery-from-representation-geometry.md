# T-004 - Separate Entity Recovery From Representation Geometry

- id: T-004
- title: Separate entity recovery from representation-substrate geometry in `WORLD_MODEL_METHOD.md`
- type: correction
- ticket_category: ordinary
- status: active
- review_status: candidate_ready_for_review
- goal: >-
    Publish one bounded STDO 2.2.2 successor in which a recovered
    institutional entity has a lawful published form, geometric obligations
    apply only where a representation space is declared, and the Markov
    construct's epistemic status is stated once.
- change_intent: >-
    Restore the Markov object to its stated role as the theoretical account of
    why a recovered boundary is real, and give the discovery path its own
    construction law and publication unit, without weakening the geometric
    law where a representation space exists.
- change_class: requirement_reprice
- re_entry_point: specification/standards/WORLD_MODEL_METHOD.md
- triaged_at: 2026-07-27
- created_at: 2026-07-27
- updated_at: 2026-07-27
- owner: specification_methodology
- pen_holder: claude
- predecessor_release: v2.2.1 at 8ad868eb0c9a3bdd075ff17ec4f7923d5ceec1cf
- target_release_line: 2.2.2

## Intake Triage

**Substantive?** Yes. It changes what may lawfully be published as the
primary semantic unit of a world model.

**Boundary crossed?** Normative standards. One member, `WORLD_MODEL_METHOD.md`.

**Upward-propagation walk to the first missing layer.** The defect is not in
realization and not in design. `WORLD_MODEL_METHOD.md` stated a construction
and publication obligation that its own discovery pipeline could not satisfy.
The first missing layer is the requirement text itself.

**Derived change class.** `requirement_reprice`. No Product boundary of STDO
moves; the pure-normative scope, member set, and altitude are unchanged.

**Re-entry point.** `specification/standards/WORLD_MODEL_METHOD.md`.

**Affected span.** One of 41 standards members. No authority compression binds
`WORLD_MODEL_METHOD.md` — verified against all seven compression
`source_ref`/`source_digests` — so no derived surface goes stale.

**Release scope.** One bounded successor, `2.2.2`, over released `v2.2.1`.

## Defect

`WORLD_MODEL_METHOD.md` at `v2.2.1` contained two incompatible accounts of how
a published cut comes to exist:

1. **Method Flow** §6–§7 recovers entities from enacted function, authority,
   state, and adjacency, and states that "sparse first publication is lawful
   if the object is bounded, distinguishable, and evidence-backed."
2. **Markov Object Construction Law** declared the cut is *constructed* by a
   directional interventional procedure, required an identity direction and
   effective coordinate as publication minima, and held that "a direction that
   has no acceptable verification is a candidate, not an accepted Markov
   object."

Method Units offered a recovered entity only two destinations: converge into a
Markov-object cut, or be reclassified as a non-object artifact — treatment
surface, covariance edge, or temporal reference artifact.

A recovered institutional entity is none of those, and the geometric
procedure presumes a representation space that institutional ledger claims do
not supply. The method's own discovery pipeline therefore produced output its
own publication law refused to accept.

Motivating observation, not closure evidence. The `odd_world_model` builder at
commit `f94aa30fb2518a342655bf6d53cbb66fb3321277` shows the same split
independently: its proof surface
(`build_tenants/typescript/code/src/proof/generate_full_build_proof.ts`,
SHA-256 `da11f4790c9ca0f2c17de48cf46704b10601aeee8d9316809515dd2074434377`)
declares `identity_direction_shape_exists_but_held_out_treatment_and_
distributed_evidence_are_unresolved_refs`, and its produced
`identity_direction` (artifact SHA-256
`cd3b16bba437287e7e22f2d02cc72184a06a7871cff7a264b4abae971da29050`) is a
referential triple over source states rather than a geometric direction.

That observation motivated this reprice. It is a downstream consumer state,
not STDO evidence, and it closes nothing in this ticket.

## Intake Evidence

`.ai-workspace/comments/claude/20260727T050000Z_REVIEW_world_model_method_under_spec_method.md`
reviews the **predecessor** member at `v2.2.1` and opened this ticket. It is
intake evidence only and carries no promotion or closure authority over the
successor. Its F1 and F2 are discharged by this reprice; its F3 (cited
experiment range) and F4 (refinement drift from the companion source) remain
open and are not carried here.

The independent exact-cut review required before tap must bind the immutable
`v2.2.2-rc.1` subject, and must not be authored by this ticket's pen holder.

## Change

1. **Entity Cut** added as the primary published semantic unit: lawful
   without an identity direction, carrying identity, boundary, authority,
   state, evidence, treatment, covariance, and ambiguity.
2. **Markov-Object Overlay** added as an optional geometric overlay,
   admissible only where a representation space is declared.
3. **Entity Cut Construction Law** added in proportional form: one
   admissibility test over identity, boundary, authority, evidence, and
   ambiguity at evidence altitude proportional to the claim. Cross-context
   invariance, null-peer comparison, adjoint round-trip, transplant, and coat
   stripping are named as non-mandatory techniques. Concrete carriers,
   layouts, and storage topology remain consumer realization.
4. **Markov Object Construction Law** scoped as the representation-substrate
   specialization; the declared representation space becomes a required,
   versioned overlay member, and a re-fitted space is an explicit supersession
   even when no ledger entry changed.
5. **Representation Law** leads with the interventional boundary statement;
   the geometric reading becomes the declared-space case.
6. Terminology routed across the member: 13 publication-unit references to
   entity cut, 3 geometric references to overlay.

## Conserved

The Markov construct, its theoretical underpinnings, the four working
refinements, the epistemic status and promotion gate, `source -> tracing ->
assurance -> attribute ledger -> entity cut`, Publication Law, Attribute
Ledger Law, Saturation, Composition, Projection, Proof Law, and the
control-plane/data-plane split are all retained.

The exclusion of principal-component and maximum-variance constructions as
identity directions is retained unchanged.

## Non-Closure Conditions

- a published cut may claim a geometric identity direction without a declared,
  versioned representation space;
- an entity cut is treated as weaker law than an overlay rather than as the
  primary unit;
- the Markov construct is presented as formally established rather than
  candidate; or
- a compression or template asserts publication law this member no longer
  carries.

## Exclusions

No change to STDO Product boundary, member set, altitude, or any other
standards member. No executable conformance, schema, or consumer adoption
change. This ticket does not tap `2.2.2`.

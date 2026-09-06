# T-028 - Make Executive Mutation Prohibition Explicit

- id: T-028
- title: Make the Executive mutation prohibition explicit
- type: bug
- ticket_category: ordinary
- status: backlog
- goal: >-
    Preserve a strict separation between Executive decision work and effectful
    implementation in a future selected STDO release.
- change_intent: >-
    Make the Executive role boundary fail closed on direct implementation
    effects, including changes that appear small, test-only, reversible, or
    obvious, without changing the Executive's inspection, evaluation,
    disposition, or delegation duties.
- change_class: requirement_reprice
- re_entry_point: specification/standards/STDO_REFERENCE_FRAME_BASELINE.md#executive-attention-evaluation-and-action
- triaged_at: 2026-09-02
- created_at: 2026-09-02
- updated_at: 2026-09-06T02:43:24Z
- priority: P3
- owner: specification_methodology
- work_authorization: direct_human_product_owner_instruction_2026-09-02
- target_release: future_successor_after_v2.5.0-rc.4

## Current Gap

The RC4 profile already states that Executive acquires no implementation or
mutation authority from the role and that each material effect remains with
the actor carrying its exact operation grant. It does not state the operational
prohibition strongly enough to prevent an Executive actor from treating broad
tool access or a tiny fixture repair as permission to edit.

## Target Truth

An actor occupying Executive must not modify candidate, Product, or worktree
bytes or perform an implementation effect. Broad filesystem or tool access and
a change being small, test-only, reversible, or apparently obvious confer no
authority. Every mutation occurs through a separately activated Worker or
Writer relation carrying the exact operation grant and write territory. If the
same human or model changes roles, the transition is explicit and durably
recorded; for that effect, the actor is no longer acting as Executive.

## Falsifier

An actor remains identified as Executive, notices one missing field in a test
fixture, and directly adds the field because the edit is tiny, test-only,
reversible, and inside its filesystem access. Any method or projection that
permits or leaves this case ambiguous fails the target truth.

## Evaluation Criteria

1. The successor source profile states the byte-mutation and implementation-
   effect prohibition directly.
2. The source profile makes access, size, reversibility, test-only scope, and
   apparent obviousness non-authorizing.
3. Mutation requires a separate Worker or Writer activation with an exact
   operation grant and write territory.
4. A same-actor role transition is explicit and recorded, and the actor is not
   Executive for the resulting effect.
5. Required compressions, templates, bootstraps, and focused boundary tests are
   congruent with the amended source before candidate qualification.
6. The tiny-fixture-edit falsifier is executable or otherwise deterministically
   checked by the focused proof surface.

## Non-Closure Conditions

- the rule depends on filesystem permissions, tool availability, change size,
  reversibility, or test-only classification;
- Executive can directly implement and merely record or delegate after the
  fact;
- Worker or Writer is only a label without an exact operation grant and write
  territory;
- one actor changes roles implicitly or remains Executive for the mutation;
- a subordinate projection states a stronger rule than its source; or
- the successor is claimed without exact-cut qualification and separately
  authorized publication.

## Delivery Sequence

This distinct role-boundary clarification is a conditional contribution to
[T-030 M02](../active/T-030-deliver-proportionate-stdo-product-use.md#delivery-timeline)
under the [overall STDO goal](../../../specification/GOALS.md#goal). If that
increment selects this successor wording, make the change in its owning
standard and track it here. T-030 M03 consumes the congruent projections and
existing falsifier evidence. The existing RC4 prohibition remains operative; this ticket
is not a blanket prerequisite for direct Writer use or unrelated native work.

The [owner's delivery-planning grant](../active/T-030-deliver-proportionate-stdo-product-use.md#delivery-planning-selection)
authorizes this sequence note and its local checkpoint only. The requirement
implementation, its qualification and any publication remain separately scoped.

## Release Boundary

This is deferred P3 work for an unselected successor release after RC4. The
ticket records a future requirement re-entry. The planning relation above does
not select its implementation, amend mutable standards, start a release
candidate, or authorize source implementation commits, tags, publication, or
adoption. RC4 and all of its immutable records
remain unchanged.

## Proof Surface

- `tests/test_reference_frame_boundaries.py` with a negative tiny-fixture-edit
  case;
- exact source-to-compression digest and semantic-congruence checks;
- bootstrap and project-basis template boundary checks where those projections
  consume the role law; and
- independent review of the frozen successor candidate before any release
  decision.

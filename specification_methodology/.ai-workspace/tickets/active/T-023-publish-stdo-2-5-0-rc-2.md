# T-023 - Publish STDO 2.5.0 RC2

- id: T-023
- title: Qualify and publish STDO 2.5.0 RC2 from the shared release source
- type: release
- ticket_category: release
- status: active
- review_status: blocked_by_t022_exact_review
- goal: >-
    Publish the current 52-member STDO successor as one immutable,
    project-qualified RC2 and make it reacquirable without moving RC1.
- change_intent: >-
    Reconcile the T-019 through T-022 successor and stdo-toolchain 0.1.2,
    qualify its exact Project Subtree, then publish the authorized RC2 refs.
- change_class: bounded_release
- re_entry_point: specification/GOALS.md
- triaged_at: 2026-09-01
- created_at: 2026-09-01
- updated_at: 2026-09-01
- owner: specification_methodology
- pen_holder: codex
- work_authorization: direct_human_authorization_2026-09-01
- predecessor_release: v2.5.0-rc.1
- target_release_line: 2.5.0
- target_rc: v2.5.0-rc.2
- project_release_namespace: specification_methodology
- project_subtree: specification_methodology
- release_note: releases/v2.5.0.md
- depends_on: T-019, T-020, T-021 closed; T-022 closure

## Admission Gate

Publication requires the exact 52-member inventory and protected inputs in the
release note, working nested-layout and qualified-ref resolution, proportionate
normal and optimized qualification, T-022 closure after fresh exact review, and
independent release review with no unresolved blocker.

## Publication Boundary

Publication creates and remotely verifies:

- `refs/heads/rc/specification_methodology/2.5.0`;
- immutable annotated
  `refs/tags/specification_methodology/v2.5.0-rc.2`;
- annotated selector `refs/tags/specification_methodology/v2.5.0`; and
- `refs/heads/release/specification_methodology/2.5.0`.

The Product subject remains the project-relative `specification/standards/`
inventory declared by `releases/v2.5.0.md`. The shared repository commit and
sibling subtrees are carrier state, not additional STDO Product members.
Publication does not adopt RC2 for a consumer or accept a downstream
representation.

## Closure Law

Close only after the exact carrier commit, annotated tag object, repository
tree, `specification_methodology` Project Subtree tree, installed manifest,
qualified refs, remote parity, and exact-cut review are recorded. Any
qualifying-byte repair after publication advances to
`specification_methodology/v2.5.0-rc.3`; neither RC1 nor RC2 may move.

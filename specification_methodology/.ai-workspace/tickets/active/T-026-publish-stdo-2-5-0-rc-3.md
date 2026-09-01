# T-026 - Publish STDO 2.5.0 RC3

- id: T-026
- title: Qualify and publish the aligned STDO 2.5.0 RC3 cut
- type: release
- ticket_category: release
- status: active
- review_status: pending_exact_cut
- goal: >-
    Publish the closed T-024 and T-025 outcome as one immutable,
    project-qualified RC3 with the aligned dual-host plugin.
- change_intent: >-
    Reconcile the proportional Ticket Method repair and downstream-use
    workflow, qualify their exact Project Subtree, then advance only the
    authorized RC3 release carriers.
- change_class: bounded_release
- re_entry_point: specification/GOALS.md
- triaged_at: 2026-09-01
- created_at: 2026-09-01
- updated_at: 2026-09-01
- owner: specification_methodology
- pen_holder: codex
- work_authorization: direct_human_authorization_2026-09-01
- accepted_product_baseline: v2.5.0-rc.1
- immediate_published_predecessor: v2.5.0-rc.2
- target_release_line: 2.5.0
- target_rc: v2.5.0-rc.3
- project_release_namespace: specification_methodology
- project_subtree: specification_methodology
- plugin_version: 2.5.0-rc.3
- release_note: releases/v2.5.0.md
- depends_on: T-024 and T-025 closed
- published_tag_object: pending
- published_commit: pending
- published_manifest_sha256: pending

## Admission Gate

Publication requires:

1. T-024 and T-025 close against the exact candidate bytes;
2. the release note reproduces the 52-member standards inventory, the
   17-member plugin inventory, their aggregates, protected inputs, and the
   unchanged `stdo-toolchain 0.1.2` executable boundary;
3. native installed Claude and Codex positive-trigger and negative-refusal
   evidence satisfies the bounded T-024 claim;
4. normal and optimized full qualification, lint, formatting, plugin
   validation, JSON parsing, bootstrap rollback, and diff hygiene pass;
5. independent whole-cut review returns no unresolved P0, P1, or P2; and
6. the qualified RC tag, selector, RC branch, release branch, and carrier
   commit can advance atomically without moving RC1 or RC2.

## Publication Boundary

Publication creates and remotely verifies:

- `refs/heads/rc/specification_methodology/2.5.0`;
- immutable annotated
  `refs/tags/specification_methodology/v2.5.0-rc.3`;
- annotated selector `refs/tags/specification_methodology/v2.5.0`; and
- `refs/heads/release/specification_methodology/2.5.0`.

The Product subject remains the exact project-relative
`specification/standards/` inventory declared by `releases/v2.5.0.md`. The
aligned `plugins/spec/` payload is subordinate auxiliary tooling bound by that
same release record. The shared repository commit and sibling subtrees are
carrier state, not additional STDO Product members.

Publication does not itself accept RC3 as the Product, adopt it for a consumer,
ratify a downstream frame basis, or move an immutable RC1 or RC2 ref.

## Authorized Publication

Direct human Product authority authorized release of the aligned
`2.5.0-rc.3` cut after proportional qualification, commit, remote push, and
appropriate tagging. This carrier records that publication authority; it does
not waive any admission-gate condition or authorize substitution of later
bytes.

## Closure Law

Close only after the frozen commit, annotated tag object, repository tree,
Project Subtree tree, standards tree, installed manifest, exact inventories,
qualified refs, remote parity, fresh public installation, and independent
exact-cut review are recorded. Any qualifying-byte repair after publication
advances to `specification_methodology/v2.5.0-rc.4`; RC1, RC2, and RC3
immutable tags never move.

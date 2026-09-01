# T-026 - Publish STDO 2.5.0 RC3

- id: T-026
- title: Qualify and publish the aligned STDO 2.5.0 RC3 cut
- type: release
- ticket_category: release
- status: completed
- review_status: satisfied_published
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
- completed_at: 2026-09-01
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
- published_tag_object: 625e123572565a27a3953d07c6b883aa5e8f1ed2
- published_commit: ece85fbce89e54afbccb9bd670b58650d23a007b
- published_manifest_sha256: 7feb297337644bc8ba7fc350395c05bfa4f6ee364f906154d8b8c4ebc7bdafdf

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

## Completion Evidence

- Immutable annotated RC3 tag object:
  `625e123572565a27a3953d07c6b883aa5e8f1ed2`.
- Peeled carrier commit:
  `ece85fbce89e54afbccb9bd670b58650d23a007b`.
- Repository tree: `78cdd5085e56b87fa0718c0131d36eb799383fc8`.
- Specification Methodology subtree:
  `9879ac893e7395431eca37573c2b2b9ecd456201`.
- Standards tree: `25e42fdd4480491762faebd4d0aeb7fe034057de`.
- Installed-manifest SHA-256:
  `7feb297337644bc8ba7fc350395c05bfa4f6ee364f906154d8b8c4ebc7bdafdf`.
- Standards reproduce as 52 members with aggregate
  `8492f66bba93a1e4559b2275f01df277b5e49c24bc0a76feb028e85e4bdf5c2f`;
  the subordinate plugin reproduces as 17 members with aggregate
  `687d2be85872a839c581d5a53aa076f8cd3cfd57b3991b4a95365ce46cad9e61`.
- The qualified selector tag object is
  `0a8033a0024b25df34625b74aa71d2eb35e8bc07`; it peels to the RC3 commit.
  Qualified `main`, RC, and release branches resolve to that same commit.
  Immutable RC2 tag object
  `5ebd2d87ff0c0d9fcca96ba42d90253ba6fec7e3` remains unchanged.
- A fresh public toolchain installation from the qualified RC3 ref installed
  and verified product-local cut `v2.5.0-rc.3` with zero failures and the exact
  manifest above.
- The public cut passes 119 tests normally and 119 under Python optimization
  after the exact qualified public branches are materialized as local refs.
  Ruff, Black, Codex plugin and five skill validators, strict Claude plugin and
  marketplace validators, JSON parsing, and diff hygiene pass.
- Independent exact-public-cut review is `GO`; P0, P1, and P2 are all zero.
  Its sole P3 is an auxiliary test-harness false negative: a tag-only clone
  lacks the two local branch refs expected by the publication-topology test,
  although the remote refs are exact and the unchanged test passes after those
  public refs are fetched locally. No Product or release identity claim is
  falsified, and no successor work is selected from that observation.

Publication and exact-cut qualification are complete. Product acceptance,
downstream frame-basis ratification, and consumer adoption are not inferred.

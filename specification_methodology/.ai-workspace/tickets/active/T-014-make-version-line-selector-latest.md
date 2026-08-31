# T-014 - Make The Version-Line Selector Mean Latest

- id: T-014
- title: Make the version-line selector resolve only the latest published RC
- type: bug
- ticket_category: release
- status: active
- review_status: pending
- goal: >-
    Make an STDO version-line reference such as 2.4.3 mean the highest-ordinal
    published immutable RC on that line, while preserving direct access to
    every older immutable cut.
- change_intent: >-
    Repair selector publication and adoption so a lagging alias cannot select
    or reintroduce an older RC through the latest-version channel.
- change_class: bounded_release_framework_repair
- re_entry_point: specification/standards/RELEASE_METHOD.md
- triaged_at: 2026-08-23
- created_at: 2026-08-23
- updated_at: 2026-08-23
- owner: specification_methodology
- pen_holder: codex
- predecessor_cut: v2.4.3-rc.2
- predecessor_tag_object: 2c6317ac5f8e4dda206b537f1d75dafde969f87d
- predecessor_commit: 9849c43ea6b7ae10a28ced6f9051c4f9364347d6
- predecessor_standards_member_count: 47
- predecessor_standards_aggregate:
  cf40b70472e44868143e38ed108426bb45950b17cf441cba5ecdf7ed94f26f5f
- target_release_line: 2.4.3
- target_cut: v2.4.3-rc.3
- release_class: same_version_line_bounded_release_framework_repair
- release_note: releases/v2.4.3.md
- work_authorization: direct_human_authorization_2026-08-23

## Intake Triage

**Substantive?** The defect is operationally serious but constitutionally
bounded. A lagging mutable selector caused `adopt` to resolve RC1 after RC2 had
been published and could have produced a same-line downgrade plan.

**Boundary crossed?** Release publication, selector resolution, Product
Definition adoption mechanics, their compact projections, tests, and
release-facing guidance. No Product outcome, method algebra, schema shape,
consumer runtime, or unrelated STDO authority is repriced.

**Smallest lawful re-entry.** `RELEASE_METHOD.md`, which owns version-line
selector identity and advancement. Congruent references may change only where
they project that release-framework relation.

## Required Outcome

1. `v<version>` means the greatest positive RC ordinal published on that line.
2. Publishing a higher immutable RC advances the annotated selector and
   optional release branch as part of publication, not after acceptance.
3. A resolver enumerates the immutable RC tags and refuses a missing,
   lightweight, lagging, mismatched, or backward selector.
4. Channel adoption refuses a same-line target below the Product Definition's
   current exact basis.
5. An intentionally older cut remains lawful through its exact immutable RC
   URI and manifest digest; `sync` never follows the latest channel.
6. Adoption remains two-phase and never changes a consumer merely because the
   selector moves.

## Immediate Operational Repair

The remote `v2.4.3` selector and `release/2.4.3` branch lagged at RC1 while
immutable RC2 already existed. Under direct human instruction they were
advanced on 2026-08-23 to RC2 commit
`9849c43ea6b7ae10a28ced6f9051c4f9364347d6`. The replacement annotated
selector object is `b964d5be79b4d915abb2492666c9e592eae7fd97`.

Immutable `v2.4.3-rc.1` and `v2.4.3-rc.2` were not changed.

## Candidate Evidence

- exact predecessor reacquisition: RC2 tag object `2c6317ac...`, commit
  `9849c43...`, 47 standards, aggregate `cf40b704...`;
- candidate standards: 47 members, seven changed, 40 conserved, aggregate
  `127a6fb213eb5e12bcf6180cb73016a003ccfda80651b476055f19a22ca10275`;
- clean wheel installation with declared dependencies: 38 passing tests and
  `pip check` green;
- packaged executable identity: `stdo 0.1.1`;
- live RC2 channel dogfood: exact sync followed by no-op adoption resolved
  `v2.4.3-rc.2`, not RC1; and
- compression source edges, glossary locators, Product Definition formats,
  exact older-cut sync, and all executable refusal paths pass in that suite.

## Closure Law

This ticket closes only when:

- the source and compressed Release Method state the same latest-published
  selector contract;
- a lagging alias fails closed with the highest published cut identified;
- a same-line downgrade fails closed before manifest installation or Product
  Definition mutation;
- exact older-cut synchronization remains green;
- existing adoption-plan drift, tag, store, bootstrap, and fleet refusals
  remain green;
- the packaged CLI reports `stdo-toolchain 0.1.1`; and
- the bounded repair is published as the next immutable RC on 2.4.3, with the
  selector and release branch aligned to it.

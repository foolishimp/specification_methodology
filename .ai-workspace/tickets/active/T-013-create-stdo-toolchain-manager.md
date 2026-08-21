# T-013 - Create The STDO Toolchain Manager

- id: T-013
- title: Create the shared versioned STDO toolchain manager
- type: proposal
- ticket_category: product
- status: active
- review_status: pending
- goal: >-
    Make one centrally installed, versioned STDO distribution usable by any
    number of explicitly governed Product Definitions without copying the
    standards into each source project.
- change_intent: >-
    Add an STDO-owned toolchain manager, immutable installed-release registry,
    stdo URI resolver, Product Definition basis binding, fleet adoption, and
    stable agent bootstrap while retaining exact released-cut authority and
    keeping semantic conformance outside the manager.
- change_class: product_reprice
- re_entry_point: specification/PRODUCT.md
- triaged_at: 2026-08-21
- created_at: 2026-08-21
- updated_at: 2026-08-22
- owner: specification_methodology
- pen_holder: codex
- predecessor_release: v2.4.3 at 7207b43bba9a422c676840567e1566ff3f1558fb
- predecessor_standards_aggregate:
  3617ba1b13f134284564621b6e61dbce361d2f6341b768e4d90b5a47554c67cd
- target_release_line: 2.4.3
- target_cut: v2.4.3-rc.2
- release_class: same_version_line_successor_rc
- release_note: releases/v2.4.3.md
- candidate_standards_member_count: 47
- candidate_standards_aggregate:
  cf40b70472e44868143e38ed108426bb45950b17cf441cba5ecdf7ed94f26f5f
- current_goal_binding: this ticket
- work_authorization: direct_human_authorization_2026-08-21

## Intake Triage

**Substantive?** Yes. The live Product excludes executable distribution
management, while the Product owner has selected an STDO-owned toolchain
manager and a Product-Definition-owned installed-basis binding.

**Boundary crossed?** Product definition, Specification Method, Release Method,
the Product Definition interoperability schema and template, bootstrap and
compression projections, auxiliary plugin behavior, and a new executable STDO
distribution manager. No downstream project is upgraded merely by this source
change.

**Smallest lawful re-entry.** Product repricing. The new manager becomes an
optional released STDO capability while remaining subordinate to the exact
standards cut it installs and resolves.

## Governed Outcome

1. Install each immutable STDO cut once into a shared versioned store.
2. Resolve portable `stdo:` release URIs without embedding machine-local paths
   in Product Definitions.
3. Make the applicable `stdo_<label>.json` the sole authored selection of the
   exact governing basis.
4. Keep a mutable version-line selector distinct from the immutable resolved
   cut and never advance a consumer silently.
5. Verify annotated tag, commit, tree, standards inventory, member bytes,
   aggregate compression, license, and installed manifest before admission.
6. Support read-only status and verification, explicit adoption, and bounded
   fleet operations over discovered Product Definitions.
7. Replace copied method compression in `AGENTS.md` and `CLAUDE.md` with one
   stable marker-managed discovery bootstrap.
8. Prove the manager from an unrelated temporary Git release fixture and use it
   to install and resolve STDO's own immutable `v2.4.3-rc.1` builder basis.
9. Provide one version-neutral Quickstart covering first installation, overlay
   creation, verification, bootstrap, digest-bound adoption, and fleet use.

During construction, the source project's `stdo_default.json` pins released
`v2.4.3-rc.1` as its operative builder basis while its `$schema` resolves to the
local revision-3 candidate schema. That local schema is candidate build input,
not released method authority. After the successor RC containing revision 3 is
accepted, explicit adoption replaces the schema locator and basis with that
same installed immutable cut.

## Authority And Non-Powers

- The Product Definition selects the basis; the store registry only resolves
  its URI to installed bytes.
- The immutable release cut owns method meaning. A manifest, receipt, cache,
  bootstrap, or CLI is a projection and cannot replace it.
- `sync` and `install` cannot change a Product Definition selection.
- `adopt` changes only an explicitly selected Product Definition after showing
  the exact selector-to-cut resolution.
- Mutable authoring source never satisfies a released or installed basis.
- The manager verifies distribution identity, routing, and structural
  conformance. It is not a generic semantic-conformance engine, workflow
  governor, or consumer runtime.

## Closure Law

This ticket closes only when the CLI, schemas, templates, governing method,
compressions, and bootstraps express the same ownership model; isolated
positive and refusal-path tests pass; the shared install is byte-exact; and the
STDO source project resolves its own declared builder basis through the manager.

## Current Evidence

- isolated wheel install: `stdo-toolchain 0.1.0`;
- deterministic suite: 33 passing tests;
- style and packaging: Ruff, Black check, compile, and wheel build pass;
- dogfood basis: `stdo://releases/v2.4.3-rc.1/`;
- dogfood installed-manifest SHA-256:
  `ca6cdcb78166998e96e1efe07128209c15f6277b1c67b3e5760529f70bc538a9`;
- dogfood release identity: annotated tag object `2a0c0159...`, commit
  `7207b43...`, 45 standards, aggregate `3617ba1b...`; and
- candidate schema/template, compression edges, `stdo_default.json`, `sync`,
  and selector no-op adoption checks pass; and
- operator onboarding: root `QUICKSTART.md`, linked from `README.md`.

Immutable RC publication and subsequent independent exact-cut review remain
pending.

## RC2 Review Repair

The first candidate review correctly held qualification on seven fail-closed
boundaries. The repaired subject now:

1. separates read-only adoption planning from mutation and requires the exact
   externally accepted singular or fleet plan digest;
2. parses every `stdo:` schema locator before loading and binds its cut to the
   operative basis regardless of URI-scheme casing;
3. rejects physical store redirection and inventories regular files,
   directories, symlinks, reparse points, and special entries;
4. resolves bootstrap targets relative to `product.source_project`, confines
   fleet source projects to the authorized root, and preflights all targets;
5. requires exactly one correctly ordered marker span while preserving every
   project-owned prefix and suffix byte;
6. implements the complete declared VCS, dependency, generated, cache, and
   managed-store discovery exclusions; and
7. requires the version-line selector itself to be an annotated tag with a
   distinct peeled commit.

Each defect has a positive refusal-path regression. The repaired candidate
still requires independent exact-cut review and human acceptance before
version-line selector promotion.

# T-020 - Consolidate The Specification Stack Monorepo

- id: T-020
- title: Consolidate Specification Methodology, Axiom Indexer, and STDO Representation
- type: implementation
- ticket_category: design_realization
- status: active
- review_status: changes_requested
- goal: >-
    Place the three related source projects under one coordination-only Git
    repository so finite LLM actors can traverse the complete stack without
    repository-switching drift while every Product boundary remains exact.
- change_intent: >-
    Preserve three peer Products and their released histories, add transparent
    legacy-root and nested-root STDO reading, import sibling histories without
    squashing, and prove project-local plus fleet behavior.
- change_class: design_reframe
- re_entry_point: design/TOOLCHAIN_MANAGER.md
- triaged_at: 2026-08-31
- created_at: 2026-08-31
- updated_at: 2026-08-31
- owner: specification_methodology
- pen_holder: codex
- work_authorization: direct_human_authorization_2026-08-31

## Intake Triage

**Substantive?** Yes. Repository fragmentation now separates one recursive
development stack across three Git roots and repeatedly forces finite actors to
reconstruct bases, dependency roles, and current context.

**Boundary crossed?** Source and release topology, STDO repository reading,
root coordination, imported Git histories, native skill discovery, and fleet
verification. Product meaning, interpreted semantics, carrier admission, and
runtime authority remain outside the change.

**Smallest lawful re-entry.** The source-topology choice is a design reframe.
Transparent nested-project reading is a subordinate realization refactor
because public `stdo:` URIs, installed layout, manifest law, commands, and
Product claims remain unchanged.

## Exact Source Projects

- `specification_methodology` at committed source checkpoint
  `e5bd379c31da1b585e704599f64eee11b4949d23` or an exact reviewed successor
  carrying only this migration;
- `axiom_indexer` at `1fe3ef2af41b6df76d34d1a2fd1145d71e84a639`;
- `stdo_representation` at
  `9eface352e78ce76b437025e82eb84ab41bbfa89`.

The integration workspace is `/Users/jim/src/apps/specification_stack`. It is a
fresh checkout of the existing Specification Methodology repository, not a
fourth Product or a new Product repository.

## Target Topology

```text
repository root: coordination only
  specification_methodology/
  axiom_indexer/
  stdo_representation/
```

The root may carry concise `README.md`, `AGENTS.md`, `CLAUDE.md`, native skill
discovery links, and migration evidence. It carries no `PRODUCT.md`, Product
Definition, constitutional authority, implicit composition, or shared Product
identity.

## Governed Outcomes

1. Historical root-layout STDO cuts install and verify byte-identically.
2. A future cut may locate the STDO project at exactly
   `specification_methodology/`; zero or multiple matching layouts refuse.
3. Installed manifest roots, member paths, `stdo:` URIs, and installed bytes
   remain project-relative and unchanged.
4. The three current source histories enter the monorepo without squashing or
   rewriting their existing commit and annotated-tag objects.
5. Existing STDO tags retain their names and objects. Colliding Axiom Indexer
   and STDO Representation refs are retained under project-qualified archival
   refs without changing the annotated objects.
6. Each child retains its own Product Definition, WHAT, HOW, tickets, release
   records, licence boundary, and native skill links.
7. Root discovery finds exactly three Product Definitions and grants no
   inheritance, authority, composition, or mutable-sibling substitution.
8. Work launched from root or a child can discover the applicable native
   Axiom Indexer and STDO Representation skills without changing their Product
   bytes.

## Non-Closure Conditions

- filter-repo, squash, copied snapshots, submodules, or nested `.git` roots;
- loss or retargeting of an existing tag, commit, tree, inventory, or release
  record;
- a root `PRODUCT.md`, Product Definition, licence, or constitutional layer;
- historical installed output changes under the nested-reader refactor;
- co-location treated as authority, inheritance, composition, or dependency
  adoption;
- sibling mutable source substituted for an exact immutable Development
  Product basis;
- future Axiom Indexer or STDO Representation releases reuse colliding
  unqualified tag refs before release-law re-entry; or
- remote push, repository rename, archival, or deletion before an independently
  reviewed fresh-clone verification.

## Verification

- full Specification Methodology suite normally and under optimized Python;
- historical STDO `v2.4.3-rc.3` and `v2.5.0-rc.1` install and verify;
- synthetic nested-layout release produces the same project-relative manifest
  and installed bytes as the equivalent root-layout release;
- each imported subtree initially matches its frozen source tree;
- original commits and annotated tag objects remain reachable;
- `git fsck --full` passes;
- all three child suites pass from child roots;
- fleet discovery/status finds and verifies exactly three definitions;
- root and child skill links resolve; and
- diff, JSON, formatting, lint, and fresh-clone hygiene pass.

## Residual Release Boundary

Axiom Indexer and STDO Representation both published distinct annotated
objects under `v0.1.0-rc.1` and `v0.1.0`. A single Git tag namespace cannot
retain both names. This migration preserves those objects under project-scoped
archival refs. Before any successor Product is published from the monorepo,
`RELEASE_METHOD.md` must separately define project-qualified future tag refs
and project-subtree release identity. This ticket grants no such release.

## Closure Evidence

- Frozen source commits and trees are recorded in root `MIGRATION.md`; each
  imported subtree at its import commit reproduces the source tree exactly.
- Specification Methodology entered under `specification_methodology/` with
  zero byte changes; Axiom Indexer and STDO Representation entered through
  history-preserving, non-squash merges.
- Existing STDO refs are unchanged. Colliding Axiom Indexer and STDO
  Representation release objects remain reachable through project-qualified
  archival refs.
- The STDO reader accepts exactly one legacy or nested layout, preserves
  logical manifest paths and installed bytes, and refuses zero or duplicate
  layouts.
- Specification Methodology passes 78/78 tests normally and under optimized
  Python; Black, Ruff, JSON, and diff checks pass.
- All child suites pass from their nested roots. Fleet status and verification
  find exactly three valid independent Product Definitions.
- Root and child native skill links resolve, Git ancestry checks pass, and
  `git fsck --full --no-dangling` passes.
- Independent review of exact candidate `7ce99b0d17839fc19f1c95414d38bcb1c7643fa2`
  reports technical integration GO with two P2 closure-state findings. The
  verdict is retained at
  `../../comments/codex/20260831T144618_REVIEW_specification_stack_monorepo_candidate.md`.
  Closure remains open until those findings are repaired and the exact delta
  is independently reviewed.

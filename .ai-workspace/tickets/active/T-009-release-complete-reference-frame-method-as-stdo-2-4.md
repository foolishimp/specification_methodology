# T-009 - Release Complete Reference-Frame Method As STDO 2.4

- id: T-009
- title: Release the complete Reference Frame Method and STDO baseline as `2.4.0`
- type: proposal
- ticket_category: constitutional
- status: active
- review_status: apache_2_license_repair_qualified_freeze_pending
- candidate_generation: 02
- goal: >-
    Release one complete STDO 2.4.0 Product containing the accepted 2.3.1 RC2
    semantic line, universal Reference Frame Method, derived STDO engagement
    baseline, aggregate compression, aligned Codex and Claude bootstraps, and
    complete Apache-2.0 release and install licensing.
- change_intent: >-
    Give finite actors a rigorous, evaluation-relative way to engage an STDO
    body larger than one active context while preserving existing semantic,
    execution, review, identity, and release owners, while making the resulting
    distribution legally reusable under one explicit license.
- change_class: product_reprice
- re_entry_point: specification/PRODUCT.md
- triaged_at: 2026-08-11
- created_at: 2026-08-11
- updated_at: 2026-08-12
- owner: specification_methodology
- pen_holder: codex
- operative_predecessor: v2.3.0 at b2c64047e01d9d582243a25af587ac772233a4ea
- promotion_base: v2.3.1-rc.2 at e204f3bb287651daedefa9ea28f1c2c7cc387787
- release_class: minor_release_direct_final_promotion
- target_release: 2.4.0
- work_authorization: direct_human_authorization_2026-08-11
- license_repair_authorization: direct_human_authorization_2026-08-12

## Authority And Release Boundary

Direct human Product authority selected STDO `2.4.0` as the complete
everything-to-date standards Product and instructed that the release skip a
separate `v2.4.0-rc.*` cut as a direct promotion from the latest published RC
lineage.

The exact `v2.3.1-rc.2` tag remains immutable. It supplies the accepted
`STDO-UP-021`/`STDO-UP-022` line but does not contain the two new frame members
or their five existing-member projection and index changes. Therefore `2.4.0`
is not a zero-byte retag of RC2. This ticket records one release-specific
direct-final path with a complete bounded delta and no false zero-delta claim.

The direct-final instruction removes only the new RC identity. It does not
waive exact subject identity, complete deterministic qualification, independent
review of the frozen final carrier, direct human exact-subject acceptance, or
immutable final branch/tag publication.

On 2026-08-12 direct human Product authority identified the missing release
license as an omission, selected Apache License 2.0, and explicitly retained
the `2.4.0` version. Candidate Generation 01 at
`b2a57ebccf0831d4c7bfe605f6e5da8e9b87ab07` is therefore superseded before
review, acceptance, or publication. No local or remote release ref names that
carrier. The repair is release-scoped rather than a new methodology feature,
but it changes protected carrier bytes and requires a replacement identity and
affected qualification.

## Selected Execution Basis

- governing Product: `specification/PRODUCT.md` `## Current 2.4.0 Successor Amendment`
- selected Goal: `specification/GOALS.md` `## Current Goal`
- method basis: current `SPEC_METHOD.md` `STDO-UP-020` and `STDO-UP-022`
- release basis: `RELEASE_METHOD.md`, except for the explicitly authorized
  omission of a new `2.4.0` RC identity
- construction authority: Codex may reconcile and qualify the exact candidate,
  freeze one final carrier, and return it for independent review
- assessment authority: an independently activated Reviewer evaluates the
  frozen carrier; direct human authority owns final acceptance and publication
- re-entry: any method, Product, member, authority, or release-scope change
  after freeze requires a new exact candidate

## Candidate Scope

The complete release subject contains:

1. all 41 `v2.3.1-rc.2` standards members and their accepted semantics;
2. new `REFERENCE_FRAME_METHOD.md` as sole universal frame-method owner;
3. new `STDO_REFERENCE_FRAME_BASELINE.md` as a derived optional application
   profile over existing STDO owners;
4. `README.md` inventory alignment;
5. compression-index and aggregate-compression source identity and frame-law
   projection;
6. equal frame-engagement projections in `AGENTS_TEMPLATE.md` and
   `CLAUDE_TEMPLATE.md`; and
7. an independently versioned Claude plugin registry that can load both new
   method members without treating the plugin as Product law; and
8. the canonical Apache-2.0 license at repository root, an exact standalone
   plugin copy and manifest declaration, and an install requirement that keeps
   the legal asset outside the normative member inventory.

The Product subject remains purely normative. The Apache-2.0 text grants legal
permissions but is not methodology law. Test installs, licenses, reviews,
tickets, comments, Product/Goals source state, release notes, plugin tooling,
downstream consumer changes, and runtime machinery are not standards members.

## Affected Surfaces

- `specification/GOALS.md`
- `specification/PRODUCT.md`
- `LICENSE`
- `README.md`
- `specification/standards/README.md`
- `specification/standards/REFERENCE_FRAME_METHOD.md`
- `specification/standards/STDO_REFERENCE_FRAME_BASELINE.md`
- `specification/standards/authority_compressions/README.md`
- `specification/standards/authority_compressions/stdo_compressed.md`
- `specification/standards/templates/AGENTS_TEMPLATE.md`
- `specification/standards/templates/CLAUDE_TEMPLATE.md`
- `.claude-plugin/marketplace.json`
- `plugins/spec/.claude-plugin/plugin.json`
- `plugins/spec/LICENSE`
- `plugins/spec/skills/refresh/SKILL.md`
- `releases/v2.4.0.md`
- non-operative preview only:
  `/Users/jim/src/apps/test_instal_01/.genesis/{LICENSE,STDO_INSTALL_MANIFEST.md,STDO_RELEASE_ASSET_SHA256SUMS}`
- T-007 and T-008 publication bookkeeping after final acceptance
- this ticket

## Exact Candidate Basis

| Surface | SHA-256 |
|---|---|
| `REFERENCE_FRAME_METHOD.md` | `bfe92df7e888c3b0ee269dde161c31897e8c5d2dfdf340804c49059bade76a96` |
| `STDO_REFERENCE_FRAME_BASELINE.md` | `5ea5e9b98fcb504c2eae48e3c81fc38f774244f3d4c2cf10b53aee4cac992ef8` |
| `authority_compressions/README.md` | `e421d8bdce98a4dd7c23e81125a919939568a344201d3a4700200b9eea6c44a2` |
| `authority_compressions/stdo_compressed.md` | `be3c2d15f278ee7eca461ba82b666554aeda60217bfcfd6b6c941d9c77112abc` |
| `templates/AGENTS_TEMPLATE.md` | `b1efb82ea5e9e08d8cf02d9e0c6d9c8bacfc072d4caed3c4f05ce9c41c0d38c6` |
| `templates/CLAUDE_TEMPLATE.md` | `02b43201f0e0b3de8122144ef0e1a5808677dd1cee7207ab18eadb1a4c87cfbf` |
| complete 43-member standards aggregate | `39b210b13814aca25713fd2ada749e7200bd9d77c997493a67c6d03cc71188d6` |
| `LICENSE` | `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30` |
| `README.md` | `cc6a483821cf5eb15446852f432ee0632b70afc56f83792469a34490a3c88cb6` |
| `specification/PRODUCT.md` | `9c36d175e02ff25c9a4cbb39fb7f4f0d5d886fcb99c464c126e27d69d4de8e3b` |
| `releases/v2.4.0.md` | `a37f0db63108e293aa7f481c73cdd0be9ba67f845fc9e68bf8477d5b06f87c91` |
| `.claude-plugin/marketplace.json` | `ad88de5384c19227ee1512051d28fc9bb5b916f873cb42df93dddc99105106` |
| `plugins/spec/.claude-plugin/plugin.json` | `77cb1a4ada6b9a8970811a35f33d1ce52e3c5a2c9c9bb841b9469427e97f2ccd` |
| `plugins/spec/LICENSE` | `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30` |
| `plugins/spec/skills/refresh/SKILL.md` | `1ca76a378245de66e3b1726f778fc5eb4abcddadb5675c3159f23156a8ab933d` |

This table binds the reconciled standards and protected release-scoped subject.
The final carrier identity and review evidence are added only after freeze.

## Acceptance Conditions

- [x] Direct Product authority selects `2.4.0` and the direct-final release path.
- [x] The accepted `v2.3.1-rc.2` semantic line is conserved without reopening
      `STDO-UP-021` or `STDO-UP-022`.
- [x] Universal frame declaration, activation, evaluation, conjunction,
      translation, coverage, revision, and qualification have one owner in
      `REFERENCE_FRAME_METHOD.md`.
- [x] The STDO profile maps Executive, Worker, and Reviewer onto existing STDO
      owners without a second execution or amendment path.
- [x] Every Worker result returns to Executive; Executive alone activates
      Reviewer; Reviewer returns to Executive and does not implement repair.
- [x] Frame, role, persona, actor, lens, component, authority, and independence
      remain distinct.
- [x] Projects may adopt or replace the baseline only through existing project
      authority; local axioms do not become a new owner.
- [x] Frame topology is non-hierarchical by default and composition is required
      only where a material evaluation crosses frame relations.
- [x] Coverage is tuple-relative, interaction-aware, authority-aware,
      failure-aware, falsifiable, and explicit about residual uncertainty.
- [x] Aggregate compression pins and projects both new sources.
- [x] The compression index names both new sources.
- [x] Codex and Claude templates carry equal frame-engagement semantics.
- [x] The independently versioned Claude plugin exposes both new members without
      entering the standards Product subject.
- [x] The canonical root and standalone-plugin license copies are byte-identical
      to the official Apache License 2.0 text, and the plugin manifest declares
      SPDX identifier `Apache-2.0` without changing its selected version.
- [x] The test install carries that exact license outside the normative
      standards member root and verifies it independently from member identity.
- [x] The exact subject contains 43 members with two additions, nine changes,
      32 conserved members, and no removals relative to `v2.3.0`.
- [x] The release note declares the complete semantic/member delta, conserved
      law, exclusions, direct-final relation, and exact inventory.
- [x] Deterministic source/compression, inventory/disposition, dual-agent,
      license, plugin-registry, installed-preview, JSON, and diff qualification
      passes for the exact candidate subject.
- [ ] A fresh capable constructor exercises every claimed Reference Frame
      Method function/result population and every required STDO baseline
      transition branch without hidden conversation or expected-output input.
- [ ] An independently authorized evaluator assesses those frozen trial results
      against the complete mandatory method/profile basis.
- [ ] One frozen final carrier is independently reviewed against the complete
      `v2.3.0..2.4.0` delta and mandatory method/profile populations.
- [ ] Direct human authority accepts the exact standards subject, final carrier,
      and review relation.
- [ ] `release/2.4.0` and annotated tag `v2.4.0` are published at that carrier.
- [ ] Publication-caused T-007, T-008, T-009, and Goals closure is recorded on
      continuing `main` without moving `v2.4.0`.

## Non-Closure Conditions

This ticket remains open if any standards member or recorded digest differs;
predecessor admission or assurance semantics drift; the baseline recreates
federal execution law; a persona or actor label substitutes for a frame;
Executive becomes universal authority; Worker activates review or advances
itself; Reviewer implements repair; a local carrier mints authority; a frame
hierarchy or universal composition is assumed; an interaction, failure,
capability, authority, or residual coverage relation is omitted; compression or
one agent template is stale; the canonical, plugin, or installed license is
missing, altered, misdeclared, or counted as methodology authority; exact
review evaluates a moving subject; direct human acceptance precedes exact final
identity; or final refs are published at different carriers.

## Exclusions

- No executable frame system, conformance engine, workflow runtime, controller,
  registry, schema, fixture suite, model, prompt, or consumer implementation.
- No ABIogenesis-specific entity, graph, runtime, module, topology, or work
  stage as universal method law.
- No operative downstream install or consumer selection; the test install
  remains a non-operative distribution preview.
- No version increment for the bounded license omission repair: the selected
  release remains `2.4.0` and plugin remains `2.1.0`.
- No `v2.4.0-rc.*` branch or tag.
- No final release branch, tag, or push before exact qualification, independent
  frozen-carrier review, and direct human exact-subject acceptance.

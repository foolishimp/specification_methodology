# T-002 — Publish Axiom Indexer 0.1.0

id: T-002
title: Publish Axiom Indexer 0.1.0
type: chore
ticket_category: ordinary
status: active
goal: GOAL-002
change_intent: Freeze, qualify, publish, and accept the bounded repository-carried MVP on the independent 0.1.0 line.
change_class: goal_reprice
re_entry_point: Goals
triaged_at: 2026-08-30T19:37:26+10:00
created_at: 2026-08-30T19:37:26+10:00
updated_at: 2026-08-30T19:37:26+10:00
priority: P1
dependencies: T-001, STDO v2.5.0-rc.1
intake_source: direct Product-owner instruction on 2026-08-30
affected_boundary: urn:stdo:bounded-context:release-publication

## Intake

The Product-owner selected publication after the MVP became useful enough to
dogfood. The release re-enters at Goals because Product meaning remains stable.
Release identities and acceptance remain governed by the exact installed STDO
Release Method.

## Release Coordinates

- Product: Axiom Indexer.
- Version line: `0.1.0`.
- Intended first immutable cut: `v0.1.0-rc.1`.
- Version-line selector: annotated mutable `v0.1.0`.
- RC branch: `rc/0.1.0`.
- Predecessor: none; this is the first release.
- Remote and exact Git object identities: unresolved until the publication
  operator selects and verifies them.

The RC ordinal increases if any qualifying byte changes after publication.
The unqualified tag is never the immutable release identity.

## Exact Product Member Set

The repository carrier contains source, authority, work, and evidence beyond
the Product. The Product subject contains exactly these entries:

1. `.agents/skills/axiomatize-corpus` — Codex discovery symlink;
2. `.claude/skills/axiomatize-corpus` — Claude discovery symlink;
3. `build_tenants/core/code/ac.py`;
4. `skills/axiomatize-corpus/SKILL.md`;
5. `skills/axiomatize-corpus/agents/openai.yaml`;
6. `skills/axiomatize-corpus/references/output-contract.md`; and
7. `skills/axiomatize-corpus/references/program.schema.json`.

All other repository entries are governing source, release-claim surfaces,
qualification evidence, work history, or excluded carrier bytes. Their
co-location grants no Product-member status.

## Release-Scoped Claims

- `AXIOM-0.1-C01`: the native skill instructs an LLM to author, validate,
  repair, and use a source-linked `a_c.text` Axiomatic Program.
- `AXIOM-0.1-C02`: the executable late-binds declared URIs, checks the specified
  mechanical laws, returns deterministic diagnostics, and instantiates the
  unchanged valid program as a logical constraint map.
- `AXIOM-0.1-C03`: the executable joins caller-supplied `{label, text}` rows in
  exact caller order under the declared newline and refusal law.
- `AXIOM-0.1-C04`: one canonical skill is discoverable through the declared
  Codex and Claude repository paths.
- `AXIOM-0.1-C05`: retained self and ABIogenesis dogfood demonstrate useful
  map-first pickup, bounded source re-entry, visible reference frames, and an
  Executive-produced downstream request.

These claims do not assert semantic truth, completeness, unique interpretation,
complete `M_b` admission, GTL composition, automatic frame selection, carrier
admission, prompt orchestration, provider attestation, or runtime operation.

## Exact Dependency Basis

- Constitutional STDO basis:
  `stdo://releases/v2.5.0-rc.1/` with installed-manifest SHA-256
  `3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338`.
- `AXIOMATIC_CALCULUS.md` SHA-256:
  `cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d`.
- Runtime requirement: Python 3.10 or later. Current qualification is observed
  on Python 3.12.8, macOS arm64; broader runtime portability is not claimed.

## Release Claim And Proof Surfaces

The release operator owns the release note and exact carrier inventory. They
shall consume this ticket's member and claim definitions without expanding
them. Governing Product claims remain in `README.md`, `specification/PRODUCT.md`,
and `specification/requirements/`. Qualification evidence is bounded by
`build_tenants/core/code/test_ac.py`, `dogfood/self/`, and `dogfood/abg/`.

## Scope

- complete and obtain exact acceptance of the project frame basis;
- make the Product Definition valid against the adopted STDO 2.5.0 basis;
- freeze the release record, Product members, claim set, and dependency basis;
- rerun proportionate pre-RC qualification on one exact candidate;
- commit the exact carrier and publish the first immutable RC and selector;
- verify remote identities and reacquisition; and
- obtain independent exact-cut review and Product-owner acceptance.

## Exclusions

No Product-scope expansion, GTL, semantic acceptance, carrier admission,
automatic frame selection, prompt engine, or implementation churn is admitted
merely to publish the existing MVP.

## Closure

- the Product-owner accepts the exact frame-basis digest and the overlay binds
  its durable decision record;
- `stdo status --verify` passes against the exact 2.5.0 basis;
- pre-RC qualification passes on the committed carrier;
- annotated `v0.1.0-rc.<n>` and annotated selector `v0.1.0` peel to the same
  remotely verified commit;
- the exact Product members and release claims match the published tree;
- independent exact-cut review passes; and
- the Product-owner accepts that immutable RC identity.

## Non-Closure Conditions

Local green tests, a mutable worktree, a branch, a lightweight tag, an
unaccepted frame declaration, a lagging selector, or approval lacking exact RC
identity cannot close this ticket.

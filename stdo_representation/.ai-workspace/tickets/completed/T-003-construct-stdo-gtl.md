# T-003 — Deliver the thin STDO Representation MVP

id: T-003
title: Deliver the thin STDO Representation MVP
type: feature
ticket_category: ordinary
status: completed
goal: GOAL-003
change_intent: freeze and dogfood one exact Source STDO authoring map plus concise native Codex and Claude instructions using accepted Axiom Indexer mechanics, without building a local GTL or orchestration engine
change_class: product_reprice
re_entry_point: Product
triaged_at: 2026-08-27T19:41:42+10:00
created_at: 2026-08-27T19:41:42+10:00
updated_at: 2026-08-31T01:49:45+10:00
source_ticket: T-002
dependencies: exact Source STDO v2.5.0-rc.1; accepted Axiom Indexer v0.1.0-rc.1; installed STDO Release and Reference Frame methods
build_tenant: urn:stdo-representation:build-tenant:axiom-indexer

## Outcome

Deliver the smallest Product we will use ourselves:

```text
Source STDO
  -> LLM-authored a_c.STDO
  -> Axiom Indexer validation and logical map
  -> native Codex or Claude pickup
  -> LLM-selected visible reference frames
  -> exact ordered join
  -> bounded work with source re-entry
```

No local deterministic engine is part of the outcome.

## Product members

The selected member paths are:

```text
build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/
  axiomatic-program.json
  logical-constraint-map.json
skills/stdo-representation/
  SKILL.md
  agents/openai.yaml
  references/codex.md
  references/claude.md
.agents/skills/stdo-representation
.claude/skills/stdo-representation
```

The last two entries are relative symlinks to
`../../skills/stdo-representation`. Exact member digests are assigned only
after freeze.

## In scope

- Reprice active WHAT to the thin Axiom-dependent Product.
- Preserve the exact Source STDO and Axiom Indexer dependency coordinates.
- Freeze the validated dogfood program and logical map at the selected Product
  artifact paths without changing their semantic content.
- Provide one canonical, concise native skill and material Codex/Claude
  instruction differences.
- Tell the LLM to select and expose frame URI, purpose, and source route.
- Use the Axiom Indexer joiner with caller-authored labels, text, and order.
- Retain exact map validation, refusal, native pickup, joined-request, source
  re-entry, and independent comparison evidence.
- Prepare the exact eight-member release subject and claims for a separate
  release lifecycle.

## Out of scope

- A local resolver, validator, canonicalizer, map builder, or string joiner.
- A complete admitted `a_c` model or full algebra population.
- GTL composition, GraphFunctions, automatic closure, carrier admission, or a
  frozen GTL dependency.
- Deterministic prompt packets, token budgeting, renderers, or skill projectors.
- ABG runtime, events, lineage, correction, continuation, or invocation.
- Provider attestation, semantic acceptance, or human mediation inside ordinary
  author/validate/repair use.
- Release notes, decisions, tags, remote publication, or Product acceptance.

## Historical prototype boundary

These paths remain retained source history and evidence only:

```text
build_tenants/semantic_compile/
build_tenants/gtl/
build_tenants/json_schema/
scripts/prepare_stdo_gtl_candidate.py
scripts/finalize_stdo_gtl_product.py
scripts/test_finalization.py
scripts/test_frozen_gtl_tenant.py
```

They are not Product members or implementation dependencies and shall not be
deleted, rewritten as current capability, or relabelled as the thin MVP.

## Working evidence

The first dogfood run is retained under:

```text
dogfood/axiom-indexer-v0.1.0-rc.1/stdo-v2.5.0-rc.1/run-001/
```

Runtime bindings and validation reports are evidence, not portable Product
members. The release subject uses the stable Product paths above.

## Acceptance

- The live WHAT and Product Definition select only the thin Axiom Indexer build
  tenant and explicitly exclude the heavy prototypes.
- The frozen program validates with zero diagnostics and reproduces its map
  under exact Source STDO and Axiom Indexer bases.
- Representative malformed URI, reference, source, grounding, residual, and
  ordering cases refuse.
- Fresh Codex and Claude agents discover the native skill and complete real
  map-first tasks with recorded source re-entry.
- An Executive run exposes selected frame details and exact ordered join input;
  repeating the join reproduces request bytes.
- Independent source comparison retains omissions, regressions, and residuals.
- No evidence or prose claims GTL, deterministic frame selection, complete
  semantic equivalence, or authority from validation.
- A separate release ticket or release record owns publication and acceptance.

## Closure

The exact eight-member MVP froze at inventory SHA-256
`316121da619af277b984a599d290e41e4740ef9f1a2bf3fd8151ac9b1d64e091`.
The Axiom Indexer validator returned zero diagnostics and reproduced map
identity
`2df34cb85bf6fbad2436e468e14cb5c26ff8d0aa721f8de10bb7e948b0d21b78`.
Fresh Codex and Claude pickup, visible Executive frame selection, byte-exact
joining, retained negative evidence, and the matched direct-prose/map-first
comparison satisfy the ticket's bounded acceptance conditions. T-004 owns the
separate release lifecycle and exact Product acceptance.

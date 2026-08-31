# STDO Representation Goals

## Current work wave

Release and dogfood the smallest useful STDO context Product:

```text
exact Source STDO prose
  -> LLM-authored a_c.STDO authoring map
  -> Axiom Indexer validation and logical constraint map
  -> LLM-selected reference frames and ordered context
  -> exact string join
  -> native Codex or Claude use with source re-entry
```

The LLM interprets meaning, selects frames, writes context, consumes
diagnostics, and revises. Exact Axiom Indexer `v0.1.0-rc.1` supplies the URI
resolver, basic validator, logical-map instantiation, and pure ordered joiner.
This Product has zero local engine code and adds no deterministic orchestration
or GTL engine.

The first Product line is `0.1.0`. Its accepted immutable Product is
`v0.1.0-rc.1`; the unqualified `v0.1.0` tag is only the mutable
highest-published-RC selector.

## GOAL-001 — Freeze the STDO authoring map

Status: completed

Produce one source-linked Axiom Indexer `a_c.text` program for exact Source
STDO `v2.5.0-rc.1` and instantiate it as a logical constraint map.

### Completion conditions

- The program resolves the exact calculus, STDO source, and selected frame
  URIs through invocation-local bindings.
- Symbols, clauses, and residuals capture operative logic rather than restate
  the corpus.
- Every item has a source route; uncertainty remains explicit.
- Exact Axiom Indexer validation succeeds and reproduces the same logical map
  from the same program, bindings, and dependency release.
- The Product claims an `a_c.STDO` authoring map, not a complete admitted
  `M_b`, unique interpretation, or lossless replacement for Source STDO.

The selected Product paths are:

```text
build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/
  axiomatic-program.json
  logical-constraint-map.json
```

Exact content digests are assigned only after those bytes are frozen.

## GOAL-002 — Supply native frame use

Status: completed

Make the frozen map directly useful to Codex and Claude through one concise
canonical skill with target-specific instruction references.

### Completion conditions

- `.agents/skills/stdo-representation` and
  `.claude/skills/stdo-representation` discover the same canonical skill.
- The skill tells the LLM how to load the map, select only material reference
  frames, show each frame URI, purpose, and source route, and re-enter Source
  STDO when the map or task requires it.
- Codex- and Claude-specific guidance changes instruction presentation only;
  it does not change STDO meaning.
- Acting as Executive, the LLM supplies every label, text value, and ordering
  choice to the Axiom Indexer joiner.
- The joiner returns the exact concatenation or a mechanical refusal. It does
  not select, trim, rewrite, budget, or interpret context.
- Executive, Worker, and Reviewer boundaries are preserved by explicit native
  instructions and source authority, not by a deterministic packet engine.

## GOAL-003 — Dogfood and release `0.1.0`

Status: completed

Use the map and native skills for real STDO Representation and ABIogenesis work,
then publish only if the thin Product earns continued use.

### Completion conditions

- Fresh Codex and Claude agents discover the native skill and complete at
  least one map-first task with bounded source re-entry.
- An Executive run visibly records selected frame URIs, purposes, and source
  routes and produces a byte-reproducible joined request.
- Independent source comparison identifies omissions, false confidence,
  incorrect routes, and useful residuals rather than retaining only favorable
  output.
- The map-assisted condition is not materially worse than direct Source STDO
  prose on governing constraints or source recovery for the selected tasks.
- The release record binds the exact Product members, Axiom Indexer dependency,
  STDO source basis, evidence, exclusions, and immutable RC subject.
- An accepted project frame basis is bound into the Product Definition before
  release qualification.

## Deferred direction

An `a_c.STDO` map may later inform a GTL or ABG composition. That is a separate
Product re-entry after this thin release proves useful. It is not a `0.1.0`
member, dependency, completion condition, or implied capability.

## GOAL-004 — Enter the Specification Stack monorepo

Status: active

Move the unchanged STDO Representation source project and complete history
under the coordination-only Specification Stack root. Preserve the accepted
Product, Product Definition, eight-member Product boundary, exact Axiom Indexer
Development Product dependency, native skills, and independent authority.
Co-location creates no composition and mutable sibling source is not the
accepted dependency.

# STDO Representation Intent

## Intent

Give an LLM a consistent, compact, source-reenterable way to use exact Source
STDO without reconstructing the complete corpus from prose on every task.

STDO Representation is an LLM-first Product for LLMs. The LLM authors and
reviews meaning, selects reference frames, writes the request, invokes basic
mechanical checks, reads diagnostics, and repairs its own candidate. Code stays
small and late-bound: URI resolution, basic validation, logical-map
instantiation, and exact ordered string joining.

## Product relation

```text
Source STDO 2.5.0 (exact cut v2.5.0-rc.1)
  -> LLM authors source-linked a_c.STDO 2.5.0 compression
  -> Axiom Indexer validates or returns diagnostics
  -> Axiom Indexer instantiates the logical constraint index over it
  -> LLM selects material frames and source re-entry
  -> LLM writes ordered labeled sections
  -> Axiom Indexer joins the exact strings
  -> Codex or Claude performs the bounded task
```

`a_c.STDO` is the STDO-specific instance of the released Axiom Indexer
`a_c.text` authoring surface. It captures essential symbols, relations,
constraints, and residual uncertainty. It may be larger than prose. Compression
means reduced interpretive reconstruction and an explicit reusable logical
form, not fewer bytes.

The Axiomatic Program is the canonical semantic compression selected by this
Product. The Logical Constraint Map is a deterministic index over that
unchanged compression. The index adds resolution and source-route evidence; it
does not reinterpret or outrank the compression.

The map is a derived interpretation. Source STDO remains semantic authority.
Every material item retains source routes, and the LLM re-enters source when a
task, residual, disagreement, or unresolved route requires it.

## Deterministic boundary

Exact Axiom Indexer `v0.1.0-rc.1` owns the mechanical dependency:

```text
validate(program, bindings) -> valid map | diagnostics
join([{label, text}, ...])   -> exact string | refusal
```

Validation checks only the released Axiom Indexer laws: closed shape, URI and
reference closure, source grounding and resolution, residual re-entry,
ordering, and deterministic content identity. It does not prove semantic
truth, completeness, fidelity, unique interpretation, or frame applicability.

The joiner preserves caller order and content. The LLM supplies every frame,
label, string, and ordering choice. No validator, renderer, GraphFunction,
template engine, or orchestrator chooses context on its behalf.

## Native agent use

One canonical STDO Representation skill is discoverable through Codex and
Claude repository skill paths. Tight target-specific references may change
instruction ordering, tool-call presentation, or return formatting for a model
family. They cannot change the map, Source STDO meaning, role boundaries, or
selected frames invisibly.

Acting as Executive, the LLM:

1. binds the task and evidence boundary;
2. selects material frame URIs from the map;
3. shows each selected frame's purpose and source route;
4. writes the ordered labeled context;
5. invokes the pure joiner; and
6. receives Worker or Reviewer output for disposition.

A Worker constructs and self-validates its bounded result. A Reviewer receives
an exact subject and evidence boundary, evaluates without repairing while
retaining the Reviewer role, and returns findings to Executive. These are
instructions for consistent context separation. A role label grants no
external authority.

## Desired outcomes

- a frozen, validated `a_c.STDO` authoring program and logical constraint map;
- exact URI-based source and frame re-entry without line numbers as identity;
- concise native Codex and Claude pickup;
- visible LLM-selected reference frames and exact ordered request bytes;
- useful diagnostics the LLM can act on without a human in each iteration;
- retained residual uncertainty and honest source comparison; and
- demonstrated self-use before release.

## Non-goals

- a complete admitted `a_c` model `M_b`;
- a unique or lossless interpretation of Source STDO;
- deterministic semantic review or automatic frame selection;
- a GTL overlay, GraphFunction catalog, least-closure engine, prompt packet
  schema, renderer, skill generator, or ABG runtime;
- model invocation, workspace mutation, continuation, or runtime truth;
- provider-attested invocation provenance for ordinary dogfood; or
- authority obtained by including text in a prompt.

GTL and ABG remain possible downstream consumers after a separate re-entry.
They are not part of the active Representation Product.

## Success criterion

The Product succeeds when we prefer its map-first native workflow for real work
because it preserves governing constraints and source recovery while reducing
repeated context reconstruction. If full prose remains more reliable or the map
hides material uncertainty, the Product returns to authoring or native-skill
repricing before release.

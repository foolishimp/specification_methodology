# Axiomatic Program Output Contract

Write one JSON object conforming to `program.schema.json`:

```text
Program = (
  uri,
  calculus_ref,
  source_basis,
  frame_refs,
  vocabulary_refs,
  symbols,
  clauses,
  residuals,
  optional frame_indexes
)
```

Resolve logical resources with one invocation-local Binding Set:

```json
{
  "kind": "axiom-indexer.binding-set",
  "schema_version": 1,
  "bindings": [
    {"uri_prefix": "repo://example/", "path": "/physical/root"}
  ]
}
```

The longest unambiguous URI prefix wins. Physical paths remain outside the
program.

- `uri`, every item identity, every kind, operator, role, source, and frame is
  an absolute URI.
- `calculus_ref` resolves the exact `a_c` source used for authoring. The MVP
  program is an `a_c.text` authoring surface, not a claim that a complete
  admitted `M_b` has been constructed.
- `symbols` name concepts essential to using the corpus.
- `clauses` express typed relations or constraints. Each ordered argument has
  one role and exactly one `ref` or scalar `literal`.
- `residuals` retain ambiguity, conflict, omission, or unresolved meaning.
- Every symbol, clause, and residual has non-empty `source_refs`.
- Local references resolve to program items. External kinds, operators, and
  roles occur in `vocabulary_refs`. Frames occur in `frame_refs`.
- Source and frame URIs resolve through the supplied Binding Set. Physical paths
  are not stored in the program.
- A Markdown source fragment names a heading slug, never a line number.
- URI sets are sorted and duplicate-free. Symbols, clauses, and residuals are
  sorted by their `uri`.

Capture the operative logic, not a prose restatement. A program may be larger
than its source. Its purpose is explicit reusable constraints and consistent
source re-entry.

The validator checks structure, URI resolution, reference closure, grounding,
and a canonical value digest. Input whitespace is not identity. Validation does
not judge semantic truth or completeness.

## Explicit frame indexes and projections

An optional `frame_indexes` array contains URI-sorted declarations with exactly:

```json
{
  "uri": "urn:example:index:transfer",
  "frame_ref": "repo://example/frames.md#transfer",
  "scope": "Assess this package transfer under the selected source contract",
  "clause_refs": ["urn:example:clause:transfer"],
  "residual_refs": [],
  "source_refs": ["repo://example/frames.md#transfer"]
}
```

Each index has a globally unique URI, one frame declared in `frame_refs`,
nonblank scope, correctly typed local clause/residual roots and nonempty source
grounding. URI sets are sorted and duplicate-free; at least one root is required.
Index identities cannot be used as clause operands. An absent optional field
preserves prior program/map behavior; an empty array selects nothing.

Declare logical dependencies with existing ordered clause arguments. A selected
conclusion must explicitly reference its supporting clauses, premises,
conditions, exceptions and qualifications under the source-owned vocabulary.
Code follows every local argument ref without interpreting the role. Literal
arguments retain their exact value and position. No implication, truth value,
frame applicability or operation permission is inferred.

An indexed map retains `frame_indexes` keyed by URI, unchanged clauses and
their existing reverse adjacency. Indexed validation also observes every
residual re-entry file. Invoke projection with the exact program and its map:

```sh
python3 build_tenants/core/code/ac.py project \
  --program program.json --map map.json --bindings bindings.json \
  --frame-index urn:example:index:transfer \
  --mode reference-only --output projection.json
```

Repeat `--frame-index` for overlapping selections. The agent explicitly chooses
`reference-only` or `materialized`. Missing, duplicate, wrong-kind or unresolved
index selection refuses; code supplies no default frame. The supplied map must
equal deterministic instantiation of the exact current program and all its
source observations. Missing, changed or omitted evidence refuses the view;
refreshing observations is not semantic re-authoring or acceptance.

One finite closure contains selected roots, every referenced local item,
included residual subjects, and every residual affecting an included item.
Shared items occur once. Cycles terminate without proving circular reasoning.
The two modes preserve the same identities, ordered role/ref/literal links,
scope, residual routes and sources. Both bind program/map digests, selected
index declarations, frames, used vocabulary, source basis/observations, closure,
`clause_relations`, `residual_routes`, `source_routes` and a projection digest.
Materialized mode additionally supplies unchanged original symbol, clause and
residual rows. Reference-only prose resolves through exact program URI/digest
and item identity; it is never reconstructed by a template or interpreter.

Success writes the projection to stdout, or to `--output` with a report on
stdout. Refusal emits a structured report and nonzero status, clearing a safe
stale output. Inputs and resolved sources, including aliases and invalid-
fragment targets, are protected from writing or removal. An output route whose
source safety cannot be established is retained and explicitly diagnosed.
Provide stable input files and exclusive output scope during an invocation.
Projection does not change the pure joiner below.

## Exact joining

For an Executive request, supply the joiner a bare ordered JSON array:

```json
[{"label": "Reference frames", "text": "..."}]
```

It emits `label + "\n" + text` for each row, separated by `"\n\n"`, with no
added terminal newline. The LLM supplies every label, text, and ordering choice.

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
  residuals
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

For an Executive request, supply the joiner a bare ordered JSON array:

```json
[{"label": "Reference frames", "text": "..."}]
```

It emits `label + "\n" + text` for each row, separated by `"\n\n"`, with no
added terminal newline. The LLM supplies every label, text, and ordering choice.

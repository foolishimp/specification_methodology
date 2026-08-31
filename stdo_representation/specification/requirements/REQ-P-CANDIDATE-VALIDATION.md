# REQ-P-CANDIDATE-VALIDATION — LLM Repair Loop

Family: `REQ-P-CANDIDATE-*`
Status: Active
Category: Capability / Verification

Derives from: `../INTENT.md#deterministic-boundary`,
`../PRODUCT.md#authoring-and-validation-relation`, and
`REQ-P-STDO-AUTHORING-MAP.md`

## Purpose

Let an LLM author `a_c.STDO`, invoke exact Axiom Indexer validation, consume all
mechanical diagnostics, and write a new candidate when repair is needed.

## Relation

```text
LLMAuthor(Source_STDO, authoring_contract, selected_frames)
  -> Program* | hold | residual

AxiomValidate(Compression*, BindingSet)
  -> valid compression + bound LogicalConstraintIndex | diagnostics
```

The LLM performs semantic interpretation and repair. Axiom Indexer performs the
released deterministic relation over unchanged bytes. No local STDO
Representation compiler or validator is added.

## Imported validation boundary

The exact dependency checks:

- the closed Axiomatic Program shape;
- absolute and unique URIs;
- sorted, duplicate-free URI sets and program item populations;
- local reference closure and declared vocabulary/frame domains;
- source and frame URI resolution through the Binding Set;
- non-empty source grounding;
- residual subject and re-entry closure; and
- deterministic program and logical-map identity.

It does not check prose truth, completeness, unique interpretation, automatic
frame applicability, or a complete admitted `a_c` algebra.

## Requirements

**REQ-P-CANDIDATE-001**: Authoring shall use exact Source STDO, the exact Axiom
Indexer output contract and schema, selected authoring frames, and explicit
source bindings. Missing material input shall produce a hold or residual rather
than invented meaning.

**REQ-P-CANDIDATE-002**: The LLM shall capture essential symbols, relations,
constraints, and uncertainty. It shall not satisfy the Product by mechanically
restating every source paragraph or by claiming unsupported completeness.

**REQ-P-CANDIDATE-003**: Validation shall invoke the exact released Axiom
Indexer executable and preserve the candidate bytes. No STDO Representation
script shall fork, widen, or silently patch the imported contract.

**REQ-P-CANDIDATE-004**: Every safely detectable diagnostic shall be returned
to the LLM. A crash, unresolved dependency, invalid binding, parse failure, or
partial evaluation shall not produce `valid`.

**REQ-P-CANDIDATE-005**: A repair is a new compression candidate with new
content identity. Revalidation of identical compression and binding bytes under
the exact same dependency shall reproduce the same report and index.

**REQ-P-CANDIDATE-009**: `valid` shall require the emitted index to bind the
unchanged compression URI and canonical digest, exact source basis, frame
references, logical populations, and total source routes. An index over another
compression is invalid.

**REQ-P-CANDIDATE-006**: `valid` shall be described only as satisfaction of the
released mechanical contract. Semantic source comparison and usefulness remain
LLM evaluations with explicit uncertainty.

**REQ-P-CANDIDATE-007**: Representative negative evidence shall include at
least malformed shape, duplicate or unsorted URI sets, dangling local refs,
unresolved source or frame URIs, ungrounded items, and broken residual re-entry.

**REQ-P-CANDIDATE-008**: A valid working candidate may be used and dogfooded
without human semantic acceptance, provider attestation, GTL composition,
carrier admission, or Product release.

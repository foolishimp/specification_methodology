# REQ-P-STDO-AUTHORING-MAP — Source-Linked STDO Compression

Family: `REQ-P-MAP-*`
Status: Active
Category: Capability / Constraint

Derives from: `../PRODUCT.md#product-terms`, exact Source STDO
`AXIOMATIC_CALCULUS.md`, and the accepted Axiom Indexer `0.1.0` Product

## Purpose

Specialize the released Axiom Indexer `a_c.text` authoring surface for exact
Source STDO. The result is a compact logical constraint map for LLM use, not a
second Source STDO authority or a complete admitted calculus model.

## Program shape

```text
a_c.STDO = (
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

The exact Axiom Indexer schema owns field and value shape. This Product owns the
selection of Source STDO, the program content, and its bounded usefulness claim.

## Requirements

**REQ-P-MAP-001**: `calculus_ref` shall resolve exact Source STDO
`AXIOMATIC_CALCULUS.md`; `source_basis` shall identify exact Source STDO
`v2.5.0-rc.1`; every selected frame shall be an absolute source URI.

**REQ-P-MAP-002**: Every symbol shall name a concept essential to using the
corpus. Every clause shall express one material relation or constraint with
URI-linked operands or explicit literals. Labels and statements aid LLM use but
do not replace the URI relations.

**REQ-P-MAP-003**: Every symbol, clause, and residual shall have one or more
Source STDO routes. Every material source member shall either ground represented
content or be named by an explicit coverage residual in release evidence.

**REQ-P-MAP-004**: Ambiguity, conflict, omission, unsupported compression, and
future GTL or ABG mapping work shall remain residuals with exact re-entry routes
rather than invented certainty.

**REQ-P-MAP-005**: Semantic identity and reference shall use URIs. Line numbers,
member counts, array positions, lexical similarity, and graph proximity shall
not establish meaning, equality, dependency, authority, or frame selection.

**REQ-P-MAP-006**: The logical map shall be instantiated by exact Axiom Indexer
from the unchanged valid program. STDO Representation shall not add another
canonicalizer, resolver, map schema, or validator.

**REQ-P-MAP-007**: The map may omit prose wording and may be larger than the
source. It shall preserve enough explicit logic and source routes for the
selected dogfood tasks or return to authoring reprice.

**REQ-P-MAP-008**: The Product shall not describe this authoring map as the full
`M_b`, all `I/O/E/C/L/X/V/T/J` populations, a lossless carrier, a selected
semantic baseline, or GTL.

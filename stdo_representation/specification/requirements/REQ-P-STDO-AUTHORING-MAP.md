# REQ-P-STDO-AUTHORING-MAP — STDO Compression And Constraint Index

Family: `REQ-P-MAP-*`
Status: Active
Category: Capability / Constraint

Derives from: `../PRODUCT.md#product-terms`, exact Source STDO
`AXIOMATIC_CALCULUS.md`, and the same-version Axiom Indexer `2.5.0-rc.4`
mechanics Product

## Purpose

Specialize the released Axiom Indexer `a_c.text` authoring surface for exact
Source STDO. The Axiomatic Program is the semantic compression. The emitted
Logical Constraint Map is the deterministic index over that unchanged
compression. Neither is a second Source STDO authority or a complete admitted
calculus model.

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
`v2.5.0-rc.4`; every selected frame shall be an absolute source URI.

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

**REQ-P-MAP-006**: The logical constraint index shall be instantiated by exact
Axiom Indexer from the unchanged valid compression and shall bind its URI,
canonical digest, source basis, frame references, populations, and total source
routes. STDO Representation shall not add another canonicalizer, resolver, map
schema, or validator.

**REQ-P-MAP-007**: Compression is semantic and attentional, not a byte-size
claim. The compression or index may exceed the prose bytes. They shall preserve
enough explicit logic and source routes for selected tasks or return to
authoring reprice.

**REQ-P-MAP-008**: The Product shall not describe this compression or index as the full
`M_b`, all `I/O/E/C/L/X/V/T/J` populations, a lossless carrier, a selected
semantic baseline, or GTL.

**REQ-P-MAP-009**: The Product exact version, including prerelease ordinal,
shall equal the represented STDO exact version. Equal version text shall not
collapse their Product, release-cut, member, review, acceptance, or content
identities.

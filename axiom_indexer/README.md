# Axiom Indexer

Axiom Indexer 3.0.5 resolves and validates explicitly declared source-linked
programs, derives logical maps, projects selected frame indexes and joins
caller-authored labeled text. It also converts a provider-checked a_c
source-semantic model into the same program surface with exact reversible
record preservation. [The release record](releases/v3.0.5.md) defines its
eight regular Product members and current evidence boundary.

Use [the native skill](skills/axiomatize-corpus/SKILL.md). When a canonical
model already exists, follow
[the model conversion contract](skills/axiomatize-corpus/references/model-conversion.md)
and derive views from that same model. Direct source-to-program LLM authoring
remains supported. The LLM supplies meaning, source/frame choices and actual
task judgments; mechanics supply no semantic acceptance or operation grant.

```sh
python3 build_tenants/core/code/ac_model.py convert --model <model.json> --config <conversion-config.json> --output <program.json> --receipt <preservation.json>
python3 build_tenants/core/code/ac.py validate --program <program.json> --bindings <bindings.json> --emit-map <map.json>
python3 build_tenants/core/code/ac.py project --program <program.json> --map <map.json> --bindings <bindings.json> --frame-index <index-uri> --mode reference-only
```

Use `materialized` for the same selected closure with unchanged authored
content. Conversion preserves source grounds, conditions, exceptions,
references, residuals and all model metadata; regeneration detects tampered
visible rows as well as payload changes. It supports the five authored
semantic families and refuses populated operational families until a separate
conversion contract exists. It does not admit the upstream model.

`ac.py join --input <ordered-sections.json>` concatenates exact caller strings
without selection, inference or rewriting. Omit output paths for stdout;
mutating outputs require the caller's existing grant.

The source project uses its [Product Definition](stdo_default.json) and exact
installed STDO 3.0.4 construction basis. Owned release outputs use 3.0.5;
matching version text does not merge Axiom, STDO Representation, a_c or method
authority. STDO-specific content belongs to Representation. Native discovery
symlinks are workspace integrations outside the regular-file release inventory.

The current qualification exercises the actual 3.0.5 representation, exact
round-trip restoration, map reproduction, both projection modes and refusals.
The normal and optimized test suites cover 38 mechanical cases. Structural
success is not source fidelity, usefulness, complete methodology proof,
release acceptance or consumer adoption. Historical 0.x/2.x records remain
unchanged evidence for their original subjects.

Authority: [Goals](specification/GOALS.md), [Intent](specification/INTENT.md),
[Product](specification/PRODUCT.md), [requirements](specification/requirements/)
and [frame basis](specification/REFERENCE_FRAME_BASIS.md).

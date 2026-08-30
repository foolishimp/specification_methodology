# Build Tenants

The canonical active tenant registry is
`../stdo_representation.json#/how/build_tenants`.

| Tenant | Status | Product relation |
|---|---|---|
| Axiom Indexer | active | carries the selected `a_c.STDO` program and logical map; exact accepted Axiom Indexer supplies all deterministic code |
| semantic compile | retained history | prior full-model compiler and qualification prototype; excluded from `0.1.0` |
| GTL | retained history | prior passive carrier, codec, projection, and frozen-GTL experiments; excluded from `0.1.0` |
| JSON Schema | retained history | unselected placeholder; excluded from `0.1.0` |

The thin active relation is:

```text
LLM authors meaning
  -> Axiom Indexer validates and instantiates the map
  -> LLM selects frames and ordered context
  -> Axiom Indexer joins exact strings
```

No active tenant may introduce a second resolver, validator, canonicalizer,
logical-map schema, joiner, automatic frame selector, GTL engine, prompt packet
engine, renderer, or agent runtime.

Historical tenant bytes remain inspectable source history and evidence. They
are not active Product members, dependencies, or future work requirements by
presence alone.

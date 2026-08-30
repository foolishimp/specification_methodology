# Self Dogfood

This directory is the first use of Axiom Indexer on its own constitutional
corpus.

- `axiomatic-program.json` is the LLM-authored semantic compression.
- `bindings.json` late-binds `repo://axiom-indexer/` to this checkout.
- `validation-report.json` is deterministic validation evidence.
- `logical-constraint-map.json` is the derived read-only map used by a fresh
  agent for a real Product review.
- `native-skill-smoke.md` records fresh Codex and Claude discovery of the same
  canonical skill.

The program also records the pure Prompt Joiner boundary: the Executive selects
and exposes frame URI, purpose, source route, labels, text, and order; code only
joins those strings. The ABG dogfood uses that relation in
`dogfood/abg/executive-sections.json`.

Regenerate the derived evidence with:

```sh
python3 build_tenants/core/code/ac.py validate \
  --program dogfood/self/axiomatic-program.json \
  --bindings dogfood/self/bindings.json \
  --output dogfood/self/validation-report.json \
  --emit-map dogfood/self/logical-constraint-map.json
```

A valid result establishes declared mechanics and source reachability only.
The dogfood review establishes whether the map is useful enough to retain and
iterate.

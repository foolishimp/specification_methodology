# ABIogenesis Dogfood

This is the first external use of the Axiom Indexer MVP.

The bounded source corpus is the active ABIogenesis constitutional spine:

- Goals, Intent, and Product;
- the root requirements index;
- the Product, GTL, ABG, and mapping requirement-family indexes; and
- the active T-287 work-selection boundary.

The program captures the reusable product and authority relations needed to
orient later LLM work. It does not claim to replace every individual
requirement, accepted design, implementation, or runtime proof. Those omissions
remain explicit residuals with URI re-entry routes.

ABIogenesis remains read-only. All dogfood outputs live here.

## First pickup result

A fresh agent received only the native skill and logical map. It correctly:

- recovered the Wave 2 R2/R3 design-only selection;
- refused to infer implementation authority;
- traversed the GTL Program -> validator -> HoG -> ABG admission -> event
  history -> Event Calculus/replay chain; and
- classified an unrelated dirty workspace file as local tooling rather than
  selected design work.

The first pickup exposed three prose-only dependencies. They were retained as
typed clauses and the same fresh agent then returned GO without reading any
ABIogenesis constitutional source. See `fresh-agent-review.md`.

Validate and instantiate:

```sh
python3 build_tenants/core/code/ac.py validate \
  --program dogfood/abg/axiomatic-program.json \
  --bindings dogfood/abg/bindings.json \
  --output dogfood/abg/validation-report.json \
  --emit-map dogfood/abg/logical-constraint-map.json
```

Build the Executive request from the exact LLM-authored sections:

```sh
python3 build_tenants/core/code/ac.py join \
  --input dogfood/abg/executive-sections.json \
  --output dogfood/abg/executive-request.txt
```

`executive-sections.json` exposes every selected frame URI, its purpose, and
its source route. The Executive selected those frames and chose the labels,
text, and order. The joiner only produced `executive-request.txt` by exact
concatenation. A fresh agent's complete downstream assignment is retained in
`executive-result.md`; `fresh-agent-review.md` binds the exact input and output
digests.

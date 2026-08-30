# Axiom Indexer 0.1.0 RC1 / STDO 2.5.0 RC1 Dogfood Run 001

This directory is the first exact Axiom Indexer `0.1.0` dogfood slice over the
complete installed STDO `v2.5.0-rc.1` standards corpus. The program is an
LLM-authored Axiom `a_c.text` working authoring surface. It is not an accepted
`a_c.STDO` baseline, a complete admitted `M_b`, an `a_c.STDO.GTL` carrier, or a
GTL composition. No model-invocation attestation is claimed.

## Exact bases

- Axiom Indexer installed Product: `/Users/jim/Library/Application Support/Axiom Indexer/releases/v0.1.0-rc.1`
- Axiom Indexer annotated tag object: `e7afc8a42a7123aebe91cb7582cb037b1aae612d`
- Axiom Indexer peeled commit: `dc3e00998da36dae6ac7b76b340431a85096c83c`
- Axiom Indexer tree: `8c9ad5f5e99a60c18fb8c1802471753afb226272`
- STDO installed corpus: `/Users/jim/Library/Application Support/STDO/releases/v2.5.0-rc.1`
- STDO manifest SHA-256: `3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338`
- STDO standards members: `51`
- STDO member-set SHA-256: `87dca989f2200e91406524b6b2a3e85b230bf201581425614b57a7e0469be1e5`
- Calculus: `stdo://releases/v2.5.0-rc.1/standards/AXIOMATIC_CALCULUS.md`

## Result

- Installed-validator status: `valid`
- Diagnostics: `0`
- Items: `14` symbols, `51` clauses (`51` constraints), `5` residuals
- Manifest-member grounding: `51/51`; no missing member
- Resolved source URIs: `62`
- Logical-map source routes: `70`

The 51-member result was checked by stripping heading fragments from every
symbol, clause, and residual `source_refs` URI and comparing the resulting
member paths with the exact installed manifest inventory.

## Digests

- `basis.json` file SHA-256: `c334f66802fb2a69baced5f4d105907646ce81d051cac02a90dfed06bd039a3a`
- `bindings.json` file SHA-256: `dd6d19b973d38d5eaee00cb11390d9c5109525d2409133ecec44a8aa27e6e1d4`
- `a_c.STDO.authoring.json` file SHA-256: `a561853b324e6464324238ee3cdb505edff20e78a8b5b83ff8bc202a1d261783`
- Program canonical value SHA-256: `e325e4399560b0be5562d345005818e4f925f72ecbfd9a234207f8c77b095cc5`
- `validation-report.json` file SHA-256: `66ffd50f30801fd6b9c0b29e94839dadf09f9ae8f901239e81c224733b2aed4f`
- `logical-constraint-map.json` file SHA-256: `8161a99e0cd80170882e2019f72f419dd773683c0731ad9b3a0d1d31a5905a95`
- Logical map canonical preimage SHA-256: `2df34cb85bf6fbad2436e468e14cb5c26ff8d0aa721f8de10bb7e948b0d21b78`

## Explicit residuals

- `compression-overlap-needs-source-reentry`
- `full-m-b-not-constructed`
- `frame-adoption-not-claimed`
- `semantic-acceptance-not-supplied`
- `template-placeholders-are-not-decisions`

Validation proves the declared structure, URI resolution, reference closure,
grounding, canonical ordering, and canonical program value digest. It does not
prove semantic truth, completeness, fidelity, acceptance, or unique
interpretation.

## Reproduce validation and map

Run from the `stdo_representation` repository root:

```sh
python3 "/Users/jim/Library/Application Support/Axiom Indexer/releases/v0.1.0-rc.1/build_tenants/core/code/ac.py" validate \
  --program dogfood/axiom-indexer-v0.1.0-rc.1/stdo-v2.5.0-rc.1/run-001/a_c.STDO.authoring.json \
  --bindings dogfood/axiom-indexer-v0.1.0-rc.1/stdo-v2.5.0-rc.1/run-001/bindings.json \
  --output dogfood/axiom-indexer-v0.1.0-rc.1/stdo-v2.5.0-rc.1/run-001/validation-report.json \
  --emit-map dogfood/axiom-indexer-v0.1.0-rc.1/stdo-v2.5.0-rc.1/run-001/logical-constraint-map.json
```

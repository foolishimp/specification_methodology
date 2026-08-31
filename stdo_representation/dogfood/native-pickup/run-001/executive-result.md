# Native Pickup Executive Result

## Status

`joined`

The Executive authored six ordered sections and the exact installed Axiom
Indexer `v0.1.0-rc.1` joiner rendered them successfully. Re-running the joiner
to stdout produced the same request SHA-256. The output has no added terminal
newline.

This result prepares a Worker request. It contains no Worker response, review
verdict, semantic acceptance, Product disposition, release decision, model
invocation attestation, or operative frame-basis adoption.

## Artifacts

- `dogfood/native-pickup/run-001/executive-sections.json`
- `dogfood/native-pickup/run-001/executive-request.txt`
- `dogfood/native-pickup/run-001/executive-result.md`

## Exact map and joiner

- Product map: `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/logical-constraint-map.json`
- Program URI: `urn:stdo-representation:program:a-c-text:stdo-v2.5.0-rc.1:run-001`
- Program canonical SHA-256: `e325e4399560b0be5562d345005818e4f925f72ecbfd9a234207f8c77b095cc5`
- Map canonical preimage SHA-256: `2df34cb85bf6fbad2436e468e14cb5c26ff8d0aa721f8de10bb7e948b0d21b78`
- Map file SHA-256: `8161a99e0cd80170882e2019f72f419dd773683c0731ad9b3a0d1d31a5905a95`
- Joiner: `/Users/jim/Library/Application Support/Axiom Indexer/releases/v0.1.0-rc.1/build_tenants/core/code/ac.py`
- Joiner file SHA-256: `dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672`
- Axiom Indexer tag object: `e7afc8a42a7123aebe91cb7582cb037b1aae612d`
- Axiom Indexer commit: `dc3e00998da36dae6ac7b76b340431a85096c83c`
- Axiom Indexer tree: `8c9ad5f5e99a60c18fb8c1802471753afb226272`

## Selected reference frames

1. `stdo://releases/v2.5.0-rc.1/standards/REFERENCE_FRAME_METHOD.md#reference-frame-laws`
   - Purpose: exact subject/basis, finite material evidence, authority
     conservation, semantic/evidence/verdict separation, closed results,
     invalidation, and re-entry.
   - Source route: the same exact Source STDO URI.
2. `stdo://releases/v2.5.0-rc.1/standards/STDO_REFERENCE_FRAME_BASELINE.md#derived-worker-frame`
   - Purpose: bounded read-only Worker task, explicit exclusions and stops,
     and closed return to Executive.
   - Source route: the same exact Source STDO URI.
3. `stdo://releases/v2.5.0-rc.1/standards/STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame`
   - Purpose: independent evidence acquisition, exact-subject evaluation,
     counterexample search, and no-repair discipline. This constrains the
     requested review without relabelling the Worker as a formal Reviewer.
   - Source route: the same exact Source STDO URI.

The map residual
`urn:stdo-representation:a-c-text:residual:frame-adoption-not-claimed`
remains active. These visible choices are request context, not Product frame
adoption, formal role activation, or GTL composition.

## Source re-entry used

The Executive started from the Product logical map. Source was re-entered only
where the review subject, role seam, or map residual required exact meaning:

- Project `GOALS.md`, `INTENT.md`, `PRODUCT.md`, and the active Basis,
  Authoring Map, Candidate Validation, and Dogfood Verification requirements:
  required to bind the current thin `0.1.0` stated purpose, exact eight-member
  candidate shape, deterministic boundary, exclusions, and evaluation
  criteria.
- `REFERENCE_FRAME_METHOD.md#reference-frame-laws`: required to bind exact
  basis, finite attention, material sufficiency, authority conservation, and
  semantic/evidence/verdict separation.
- `STDO_REFERENCE_FRAME_BASELINE.md#status-and-authority-boundary`,
  `#derived-worker-frame`, `#derived-reviewer-frame`, and
  `#complete-engagement-transition`: required to resolve the requested Worker
  versus independent-review seam, no-repair condition, and return topology.
- `AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation` and
  `#subject-and-carrier-boundaries`: required because valid map structure must
  not be presented as semantic fidelity, an admitted `M_b`, a carrier, or
  acceptance.
- `authority_compressions/README.md#authority-compression-assets`: required by
  the compression-overlap residual to confirm that compressed/map views remain
  source-maintained read models and raw selected-cut owners decide unresolved
  meaning.
- Project `REFERENCE_FRAME_BASIS.md`: inspected only to confirm its explicit
  proposed, non-operative status and prevent its earlier GTL direction from
  being treated as accepted current `0.1.0` authority.

No unrelated Source STDO region was loaded.

## Explicit residuals carried into the request

- semantic acceptance is not supplied by structural validation;
- the thin authoring surface is not a complete admitted `M_b`;
- compression overlap may require exact raw-source re-entry; and
- selected frame references do not claim adoption, activation, or GTL.

## Ordered input and output identity

- Section order: `Outcome`, `Reference frames`, `Constraints and boundaries`,
  `Evidence and source routes`, `Task`, `Success and return`
- Input rows: `6`
- `executive-sections.json` bytes: `14042`
- `executive-sections.json` file SHA-256: `75922c057c1431c0794e693180c1983ad938dfd17cedb78a023e8267e9689fe8`
- `executive-request.txt` bytes: `13694`
- `executive-request.txt` SHA-256: `0b94d157012b7c118e6150309fba8a3aba6e2af26aa3f2659d8bc0dd98ab0051`

## Reproduction

Run from `/Users/jim/src/apps/stdo_representation`:

```sh
python3 "/Users/jim/Library/Application Support/Axiom Indexer/releases/v0.1.0-rc.1/build_tenants/core/code/ac.py" join \
  --input dogfood/native-pickup/run-001/executive-sections.json \
  --output dogfood/native-pickup/run-001/executive-request.txt
```

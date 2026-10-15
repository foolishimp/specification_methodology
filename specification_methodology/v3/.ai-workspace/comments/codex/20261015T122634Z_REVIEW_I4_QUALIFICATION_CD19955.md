# I4 qualification-tool working review

This records fresh nonauthor `i4_qualification_review`'s closed result on `cd19955505a0350b5d9b0f19d00c89e6d1810aa6`. Common expectations were fixed before candidate inspection. The review is same-family working evidence, not acceptance.

## Findings

The frozen account-integration path is **falsified** by two reproducible defects.

1. **High — incompatible body coordinates.** `tools/reconcile_account.py:104–106` compares core candidate hashes with heading-inclusive owner bodies. All 20 supplied candidate hashes cover immediate bodies excluding their heading. In-memory reproduction found all 20 preimage checks valid, no current check valid, and all 20 candidate hashes valid after excluding exactly the heading. This is a dialect mismatch, not stale source.
2. **High — dependency dialect raises KeyError.** `tools/reconcile_account.py:45–49` requires `relation['id']`, whereas eight core patches supply `target`, `relation` and `required_when`. Executing the frozen normalizer against its actual input raises `KeyError('id')`; 12 appended relations are affected. Independent in-memory normalization of target to id and relation to kind, preserving required_when, yields 12 conditional edges. Matching flat dependencies remain typed duplicates; other required and provenance occurrences retain their classifications under the pinned compiler.

Parent-reported successor repairs and the separately discovered duplicate-body remapper issue were not reviewed in this activation.

## Supported scope

The finite model follows the inspected Foundations conjunction ordering in its declared domain. Independent in-memory reproduction covered 42,336 combinations, 216 effect-associativity triples and all eight detected mutants. Source and script hashes match. The model covers two mandatory slots, assumes authentication and normalizes disjoint effects. It does not establish real authentication, complete record validation, actual use or whole-method fidelity.

Reduction, frame and conformance records, plus ordinary member-entry documentation, distinguish construction instruments from independent judgment, actual use and acceptance. Nested family-argument fidelity, complete conservation, regenerated interpretation and task-use evidence remain outside this review.

## Resources and independence

Observed interval: 12:14:16–12:26:34 UTC, 12m18s. Conservative raw-source acquisition is at least 413,261 bytes, including repetitions and pre-truncation output, plus ancillary projections. **The 384 KiB allowance was exceeded.** This review therefore supplies no envelope-compliance claim. Retained host context and native cost were not measured. No edits, Git mutations, script mains, paid calls or subagents occurred.

The exact counterexamples and finite reproductions remain bounded observations; resource noncompliance is retained rather than converted into qualification. A subsequent working readback must name its new subject and an adequate allowance.

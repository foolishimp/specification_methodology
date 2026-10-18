# Independent a_c Graphify Implementation

Status: authorized implementation increment complete; development candidate.
This record is commentary and evidence, not calculus authority, semantic
acceptance, Product acceptance or release.

## Delivered scope

The owner clarified that `a_c` means axiomatic calculus and that Graphify is a
build-tenant implementation of its shared WHAT. The new `a_c/` source project
contains its own Product Definition, common specification, construction frame
basis and `build_tenants/graphify/` realization. Its composition is empty.
Root README/AGENTS/CLAUDE discovery includes the new peer source project.

No v3, Axiom Indexer, STDO Representation or release-cohort files are part of
this implementation. Other v3 commentary appeared concurrently in the shared
worktree and was left untouched. This work performed no Git staging, commit,
push, release, installation into a consumer or global Graphify installation.
The shared branch advanced concurrently; the verification record retains both
the initial commit and HEAD observed during final verification.

## Exact basis

- Initial checkout: main at `9549bf2754c8cdde3260762c1102a0d4654c6c1f`, clean.
- Builder/calculus: installed STDO `v2.5.1-rc.2`, verified manifest
  `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
- Normative calculus member SHA-256:
  `cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d`.
- Final codec SHA-256:
  `e8d3fcaa26bf724186d05ba245fa621bfc87c8f75c5d9294795d619a9467e1bb`.
- Toy-model file SHA-256:
  `a72d423a222ecd84a429e28796c93ba07ac8b79d40caf3b74af02c36029f3b0b`.
- Actual upstream: Graphify-Labs/graphify
  `fe085cedddde3a18554f8749b230bfe47f3dcce7`, version 0.9.90, unchanged checkout.
  The checked source reports Apache-2.0 with LICENSE-MIT/NOTICE.

The exact published calculus retains normative ownership. This project defines
implementation obligations and a bounded profile; it does not fork calculus
meaning or depend on the mutable v3 source.

## Working path

The [tenant README](../../../build_tenants/graphify/README.md) gives runnable
commands. The CLI uses Python 3.11+ standard library and provides validation,
proposal materialization, externally judged encoding, exact decoding, literal
search, inspection and governing projections. It supports all eight record
families as authored data. Transformations, overlays, execution and predicate
evaluation explicitly refuse.

The ordinary example is an unaccepted proposal. It contains 14 records,
19 external coordinates and 124 typed reference occurrences. Acquiring A retains
9 governing records, including B, the declared dependency cycle, constraint,
latitude and residual. The provenance-only C and re-entry traversal remain in
the boundary. A budget of 8 refuses without a partial artifact.

Each reference occurrence and endpoint role is reified independently, preserving
self references, repeated operands, direction and parallel relations through
Graphify's undirected simple graph. Native display fields derive from authored
records and are checked on decode. Metadata creates no global membership hub.

## Independent assessment and supported repairs

`/root/ac_contract_assessment` was a nonauthor reviewer from the same Codex
model family. It supplied findings and repair guidance, with no source mutation
or acceptance authority. This is not independent model-family assurance.

Its common-contract review was satisfied for the declared scope. Its design
review found that generic typed-reference closure could acquire unrelated
provenance. Governing roles are now explicit per reference schema; other
crossing references remain boundary coordinates. A separate parent falsifier
also established that required relation endpoints must survive optional field
role settings; that case now has a regression test.

The initial 25-file implementation snapshot bound codec
`fb91d53c39047f883ffce26b138fa145c27cc359a2f8d28cb8a05dd293b344fa`.
The reviewer found three P2 defects:

| Finding | Supported repair | Deciding evidence |
|---|---|---|
| Authored signatures weakened fixed core reference families | Fixed core traversal/latitude/residual links constrain the signature's local target families; whole-model/external-resolution coordinates remain distinct | Original wrong-family falsifiers now refuse; lawful profile fixture still passes |
| Unused external identities bypassed declared domains | Every external resolution matches a complete signature-declared domain/kind/basis contract, including nested and variant declarations | Undeclared member refuses; lawful unused and nested-contract positive controls pass |
| Contradictory carrier flags/profile were ignored | Present topology flags require exact Boolean false; present carrier profile must match | All four original container falsifiers refuse; flagless extraction and incidental annotations remain accepted |

The repaired 25-file snapshot bound the final codec above. The targeted
nonauthor reread returned **satisfied**, with no remaining defects in those
causal cones. It independently reran all eight original refusal cases and the
seven targeted regression cases. Its result supplies assessment evidence and
does not accept the Product.

## Verification

| Check | Result |
|---|---|
| Product Definition, installed-basis status and recursive child discovery | Valid, installed exact 2.5.1 RC2 basis; empty composition |
| Draft 2020-12 Product Definition schema with format assertions | Passed using jsonschema 4.23.0 |
| Unit suite | 41 tests passed on Python 3.12.8, independently rerun by parent |
| Strict typing | mypy 1.15.0 passed all four tenant Python files |
| Independent review counterexamples | 8/8 refuse after repairs, exit 0 |
| Documented local CLI example | Materialize, decode, find, inspect and project pass; exact recovery; required residual retained; provenance branch excluded; insufficient budget refuses |
| Actual pinned Graphify boundary | Passed schema/build/export/load/CLI-decode/native-query path; 282 nodes and 372 edges preserved |
| Actual-export tampering | Missing occurrence, changed record, reversed semantic roles and changed derived search identity all refuse |
| Native discovery | Unseeded query `unresolved reading` retrieves authored A, residual and latitude content at depth 0 |

The [upstream report](assets/graphify-upstream.json) binds the final codec,
fixture, harness and actual upstream entrypoint digests. The
[verification record](assets/verification.json) binds the delivered source
inventory and local check results. Qualification libraries live only in the
ignored project-local `.venv/`; the ordinary CLI imports no upstream package.

Reproduce from the monorepo root:

```sh
python3 -m unittest discover -s a_c/build_tenants/graphify/test_env -p 'test_*.py' -q
```

Strict typing runs from `a_c/build_tenants/graphify/` with
`../../.venv/bin/python -m mypy --config-file mypy.ini` after installing the
qualification-only requirements. The tenant README documents the exact-upstream
trial and complete proposal example.

## Remaining qualification boundaries

The implementation checks its declared structural fragment and supplied
coordinates. It does not authenticate external evidence or issuer authority,
establish source-interpretation fidelity, provide semantic acceptance, prove
transformation deltas or establish full AC-019 model admission. Fixtures contain
explicitly simulated judgment data, never real acceptance.

The native retrieval trial establishes fixture discovery, not task sufficiency
or lower accepted-result cost. Matched real-corpus usefulness/cost trials,
broader operating qualification, Product acceptance, release and downstream
adoption remain separate selections. The existing STDO matched cohort is
unchanged.

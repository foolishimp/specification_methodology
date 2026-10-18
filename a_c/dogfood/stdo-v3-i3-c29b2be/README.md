# Codex V3 iteration-3 Graphify representation

This is a usable **proposed representation of the candidate's existing authored
interpretation** at `c29b2be37f9a12e050478be97793927d99c01781`, package
`ef5e514f5ffff4176b55ca687e56fe3c8b97efc1`. It transports that exact program
through the independent `a_c` Graphify build tenant. It does not supply a new
semantic interpretation, accept v3, amend the candidate under review, or add a
v3/Axiom Indexer Product dependency.

The [design](DESIGN.md) records the mapping and its limits. The self-contained
[input inventory](input/manifest.json) binds all 89 candidate files in the frozen
archive; no mutable v3 checkout, sibling implementation or paid actor is used.

## Use

From the `a_c/` project directory, use Python 3.11 or later (tested on 3.12.8):

```sh
python3 dogfood/stdo-v3-i3-c29b2be/representation.py check
python3 dogfood/stdo-v3-i3-c29b2be/representation.py find "Every admitted fundamental record"
python3 dogfood/stdo-v3-i3-c29b2be/representation.py select WRITING_GUIDE.good-prose \
  --out graphify-out/v3-i3-c29b2be/writing-selection.json
python3 dogfood/stdo-v3-i3-c29b2be/representation.py select RELEASE_METHOD.open-questions \
  --out graphify-out/v3-i3-c29b2be/release-questions.json
python3 dogfood/stdo-v3-i3-c29b2be/representation.py inspect \
  urn:codex-stdo3:iteration-3-r2:clause:AXIOMATIC_CALCULUS.ac-001-closed-signature
```

`select` accepts an exact selector URI or its exact index suffix. The
[selector catalogue](artifacts/selectors.json) lists all 725 scopes and their
required clause counts. The CLI prints a short selection summary and, when
`--out` is present, writes the complete projection and its conditional/provenance
routes. Without `--out`, it checks and summarizes the selection without writing.
`find` is literal discovery across preserved record payloads; inspect the exact
record and source before drawing a semantic conclusion.

Re-enter an exact source member directly from frozen custody:

```sh
tar -xOf dogfood/stdo-v3-i3-c29b2be/input/candidate.tar.gz standards/WRITING_GUIDE.md
tar -xOf dogfood/stdo-v3-i3-c29b2be/input/candidate.tar.gz interpretation/source-account.json
```

Source URIs beginning `repo://codex-v3/successor/` resolve to the archive member
after that prefix. Heading fragments and original owner/body/block coordinates
remain in the preserved payloads and source account. Verification uses those
frozen bytes, rather than a mutable source file with a matching path.

`WRITING_GUIDE.good-prose` acquires 12 clauses plus its selector. A budget of
12 records refuses because the complete view requires 13 records:

```sh
python3 dogfood/stdo-v3-i3-c29b2be/representation.py select WRITING_GUIDE.good-prose --budget 12
```

`RELEASE_METHOD.open-questions` retains both original residuals. Their presence
does not decide the missing Product qualification bundle or version policy.

## Rebuild and native Graphify use

Canonical JSON is deterministic. Gzip artifacts use fixed metadata; their
compressed byte pins identify this construction. Rebuilding to a fresh
directory is supported by `--artifacts`; an existing identical output is
accepted, while an existing different output refuses. Frozen `input/` custody
cannot be an output.

```sh
python3 dogfood/stdo-v3-i3-c29b2be/representation.py \
  --artifacts graphify-out/v3-i3-c29b2be/rebuilt build \
  --plain-graph graphify-out/v3-i3-c29b2be/proposal-graph.json
```

The plain file is ordinary Graphify-compatible node-link JSON, outside source
authority in the ignored `graphify-out/` directory. Native Graphify build/export
qualification uses the exact tenant-targeted upstream commit. The reproducible
helper and results are retained under [evidence/](evidence/), separately from
this stdlib runtime. Reproduce the boundary trial with a clean exact upstream
checkout and the tenant's qualification environment:

```sh
.venv/bin/python dogfood/stdo-v3-i3-c29b2be/evidence/native_graphify_trial.py \
  --upstream /path/to/clean/graphify-fe085ced \
  --model dogfood/stdo-v3-i3-c29b2be/artifacts/model.json.gz \
  --carrier dogfood/stdo-v3-i3-c29b2be/artifacts/graph.json.gz \
  --graph-out graphify-out/v3-i3-c29b2be/upstream-graph.json \
  --out graphify-out/v3-i3-c29b2be/native-graphify.json
```

Qualification-only requirements are pinned in
`build_tenants/graphify/test_env/requirements-qualification.txt`. The helper
checks upstream commit `fe085cedddde3a18554f8749b230bfe47f3dcce7`;
substitute that checkout's path above. An upstream-exported graph can then be
checked and used through the same CLI:

```sh
python3 dogfood/stdo-v3-i3-c29b2be/representation.py \
  --graph graphify-out/v3-i3-c29b2be/upstream-graph.json check
```

The recorded [native trial](evidence/native-graphify.json) passed real upstream
build, export, reload and exact-model recovery with all 41,144 nodes and 59,550
edges. An unseeded query for `Every admitted fundamental record` retrieved the
AC-001 clause; seeded traversal worked and four post-export tamper cases
refused. Its actual exported graph is
`graphify-out/v3-i3-c29b2be/graph.json` (48,489,869 bytes). The upstream builder
took 1.754 seconds and the complete qualification trial took 51.593 seconds.

## What is preserved

| Source content | Representation |
|---|---|
| 705 authored clauses | Original URIs, array ordinals and complete original clause JSON in objects |
| 7,741 required reference occurrences | Ordered pointer/role/target occurrences with typed governing references |
| 2,046 provenance and 30 conditional routes | Exact ordered route payloads and non-governing target/index references |
| 725 selectors | Original payloads, ordering and typed governing roots |
| 410 inline-contract uses | Original argument streams; all 33 inline contract identities stay at their uses |
| 2 original residuals | Core residual records with exact original payloads and authored subjects |
| 37 source-account contracts | Complete frozen source-account custody, including the four originally global clauses |

All eight core population keys are present. Relations, constraints, latitude,
traversals, transformations and judgments are explicitly empty. Native clauses
retain their authored kinds inside their exact payload; a native `constraint`
label is not converted into an invented core instance or acceptance judgment.
The source's predicates/definitions supply exact derived display excerpts for
native Graphify discovery.

Conditional routes preserve the source's `required_when`, qualifications and
target index. Establish applicability for the task before selecting that target
index additionally. Unknown applicability retains the obligation and withholds
dependent action. Provenance routes remain inspectable and do not automatically
expand governing closure. No field pointer is guessed to address the main
semantic record when it may address a preceding inline contract.

## Evidence and limits

The builder checks all frozen file pins, all 80 documentary inventory entries,
701 source owner body pins and 3,476 local source block pins. Complete JSON
recovery equals the original program; its raw-file SHA-256 remains a distinct
coordinate. Every selector's clause/residual closure is compared with an
independent traversal of the original native reference arguments. Required
clause counts range from 6 to 131, with median 18.

The [artifact manifest](artifacts/manifest.json) binds input, builder, codec,
model, graph, counts, sizes and catalogue. Loading recomputes descriptive
metadata and catalogue content from frozen input and checks all artifact pins.
Compression pins identify stored bytes; exact decompressed canonical bytes
establish representation preservation without requiring another platform's
zlib to produce identical compressed bytes.

| Artifact | Canonical JSON bytes | Stored gzip bytes |
|---|---:|---:|
| Original authored program | 8,773,879 | In the frozen input archive |
| Transport model | 14,601,339 | 1,159,246 |
| Graphify graph | 44,108,009 | 2,051,736 |

The raw original program file is 9,691,367 bytes. Gzip storage does not establish
semantic compression or lower accepted-result cost. Local construction took
25.650 seconds and a complete CLI check took 23.555 seconds. The actual-corpus
suite passed all 18 tests in 78.553 seconds; strict typing passed both runtime
and test files. Timings are observations from this construction, not a matched
efficiency trial.

The [nonauthor transport review](evidence/REVIEW.md) found no findings. It
compared every archive member directly with the immutable Git source and all
725 generic projections with a separate raw-reference oracle. The codec's
scaling changes also matched a separate fixed-point algorithm for 1,500
selections across 100 randomized valid models.

[Actual CLI use](evidence/actual-use.json) through the upstream-exported graph
passed these selections:

| Selector | Clauses | Residuals | Conditional routes retained |
|---|---:|---:|---:|
| `WRITING_GUIDE.core-rule` | 12 | 0 | 4 |
| `RELEASE_METHOD.open-questions` | 11 | 2 | 4 |
| `FOUNDATIONS.orthogonal-descriptions` | 7 | 0 | 3 |

Conditional target indexes were not automatically selected. A writing budget
of 12 records refused the complete 13-record view, and literal discovery found
the AC-001 clause. These invocations each took about 21 seconds, including
complete input and artifact validation. The
[verification record](evidence/verification.json) binds current source hashes,
test results, review and actual-upstream evidence. The generic codec passes
47 tests; the corpus suite passes 18.

Run the actual-corpus falsifiers and strict typing from `a_c/`:

```sh
python3 -m unittest discover -s dogfood/stdo-v3-i3-c29b2be -p 'test_*.py' -v
MYPYPATH=build_tenants/graphify/code .venv/bin/mypy --strict \
  dogfood/stdo-v3-i3-c29b2be/representation.py \
  dogfood/stdo-v3-i3-c29b2be/test_representation.py
```

These checks establish the declared transport and acquisition properties.
Independent fidelity of the original interpretation, actual task sufficiency,
accepted-result efficiency, full-calculus conformance, semantic acceptance and
release remain separate questions. Representation sizes and observed timings
are recorded as measurements, without an efficiency claim.

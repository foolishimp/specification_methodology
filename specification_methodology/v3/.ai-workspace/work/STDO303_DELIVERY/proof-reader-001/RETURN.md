# Offline proof reader — Worker return

Implemented the bounded proof documentation reader under PR-01–PR-05. The
governing builder remains `stdo://releases/v2.5.1-rc.2/`; this increment changes
documentation and its generator, not the Lean proofs or the methodology basis.

The self-contained `standards/documentation/proofs/index.html` starts with four
questions about closure, budget refusal, record preservation and unresolved
residuals. It provides searchable named declarations, kind and source filters,
readable statements, exact full source with line numbers, lexical source links,
imports, Back, and the retained evidence/assumptions panel. It links back to the
documentation home, Constraints and the Code example. These sibling pages are
owned by the distribution integration Worker.

The eleven proof payload members comprise the page, `PROOFS.json`, the exact
retained `report.json`, and eight Lean source files. Each copied source matches
the T011 independent report. The page and catalog reproduce from those copies.
The portable `check_payload(relative_files)` API takes only these eleven byte
members; it does not require the original work records or a Lean installation.

The retained result is 46 projection outputs, 46 underbudget refusals, and 204
audited declaration contracts with allowed axioms `Classical.choice`,
`Quot.sound` and `propext`. The 484 named entries in the reader are a source
catalog, not 484 separately proved results. No individual entry is assigned a
new verification verdict. Current importer/generator implementations do not
inherit the historical whole-path qualification. The separate later
1,987-record/29-record-view result is not combined with this result.

Independent provisional S3 on instance boundaries was repaired before the
technical freeze. `AC.Closed` now spans lines 19–20, `AC.Witness` 30–32,
`AC.CertificateValid` 45–47, and the named `AC.witnessDecidable` instance 34–41.
All instance and example commands close the preceding declaration. Anonymous
commands remain in full source, outside the explicitly named catalog. This is
a scanner for the selected source profile, not a general Lean parser.

## Changed paths

- `specification/requirements/PROOF_READER.md`
- `build_tenants/common-design/proof-reader.md`
- `build_tenants/common-tools/proof_reader.py`
- `build_tenants/common-tools/test_proof_reader.py`
- `build_tenants/common/standards/documentation/proofs/index.html`
- `build_tenants/common/standards/documentation/proofs/PROOFS.json`
- `build_tenants/common/standards/documentation/proofs/report.json`
- `build_tenants/common/standards/documentation/proofs/sources/AC.lean`
- `build_tenants/common/standards/documentation/proofs/sources/AC/Audit.lean`
- `build_tenants/common/standards/documentation/proofs/sources/AC/Closure.lean`
- `build_tenants/common/standards/documentation/proofs/sources/AC/Fixture.lean`
- `build_tenants/common/standards/documentation/proofs/sources/AC/Model.lean`
- `build_tenants/common/standards/documentation/proofs/sources/AC/Projection.lean`
- `build_tenants/common/standards/documentation/proofs/sources/AC/Run.lean`
- `build_tenants/common/standards/documentation/proofs/sources/AC/Toy.lean`
- This work directory: `ACTIVATION.md`, `validation.json`, `RETURN.md`.

Paths above are relative to `specification_methodology/v3/`. No other product,
application, integration or Git writes were made by this activation.

## Checks and exact cut

All nine finite tests passed with no skips, in 2.257 seconds:

```sh
cd specification_methodology/v3/build_tenants/common-tools
NODE_PATH=/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-navigation-dom-hf_s3qyf/node_modules python3 -B -m unittest -v test_proof_reader
```

Coverage includes exact source/report custody, selected-profile ranges and named
instances, nested comment/string controls, lexical references, missing/extra or
tampered payload refusal, failed-build no-output control, symlink refusal,
copied-tool portable CLI checks, safe HTML embedding, and offline DOM reading.
The same DOM test also passed against the actual generated page, not just its
in-memory equivalent. It follows a curated question to a theorem, its source,
Back and a definition, and checks all eight full source texts, search/filter
results, the named instance, evidence labels and offline resource behavior.

The actual eleven-member payload check passed with eight sources and 484 named
declarations. Scoped whitespace check passed. `validation.json` contains every
source/payload SHA-256 and byte count, the commands and the actual-page result.

| Artifact | SHA-256 |
| --- | --- |
| `proof_reader.py` | `37a74b721347635ddfdf1032cbed124c97c46aabbfd5f4fd919aca19f9cdf457` |
| `test_proof_reader.py` | `2ac5ea85168476f778ea8bc6055b260b97d65834585d30fd9e5cd83f15e1d425` |
| `proofs/index.html` | `f7729208c0396473389a0322039d3b724ef2a1c006a56885ab916b0e3c5f4418` |
| `proofs/PROOFS.json` | `76c4b1f0543d9d690f8e479598bcd8266d97494869e0fc8c548f984c7c3b7fa6` |
| Retained T011 report | `8b002e3821e99cd88bae0ccf07794d2e99818ba4e5b38d919fc3e3b45c672061` |

## Limits and handoff

This is historical evidence plus documentation custody and navigation checking.
No new Lean execution, browser visual qualification, semantic acceptance or
release decision is claimed. The page performs no network request or proof
execution. Lexical references are not kernel dependency edges; opaque prose,
graph observations and application code receive no correctness proof here.

Technical source and payload were frozen and handed to the independent reviewer
and documentation integration Worker. The latter owns the combined inventory,
installed qualification and release surfaces. No commits, pushes, tags or
release operations were performed in this activation.

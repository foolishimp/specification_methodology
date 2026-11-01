# ABIogenesis: requirements, code and test sources

Open [the offline reader](index.html). It includes its data, source files and
three renderers; no service or authoring installation is needed.

The initial selection is the canonical authored-form constraint containing
REQ-L-GTL3-LAWS-021/022. This example connects the existing ABIogenesis
specification representation to three implementation files and one test file.

1. Read the selected constraint and its source quotations.
2. Under **Proposed realization and test-source mappings**, follow **Proposed
   realization** to `canonicalizeAuthoredGtlCarrier()`.
3. From that code record, follow **Test source for** to
   `assertCanonicalPermutation()`. Open its source quotation to inspect the
   test helper; the mapped relation also retains its rationale and limitations.
4. Use **Back** to retrace the requirement→code→test path. Switch between
   **3D**, **2D** and **Layered** while keeping the same selected information.
5. Use **Files** to discover source paths and **Show in files** to move from a
   record to its file. **Code structure** and **Proposed traces** can be toggled
   separately. **About this model** exposes the base and overlay identities,
   acquisition scope and coverage.

The other proposed realizations point to `writeCanonicalJson()` and
`sha256Canonical()`. The selected test helper is also linked to the digest
function. All five links are attributed source-inspection proposals.

## What this example establishes

The public prepare/task/build/status path completed, and an unchanged repeated
build returned `reused`. Actual pinned Graphify extraction produced 48 source
observations and 127 structural links. The overlay has 59 nodes, including 11
unresolved endpoints, five proposed trace links and three explicit unresolved
mapping statements. All 86 original source files and four selected code/test
files are embedded. The original 1,373 native records, 495 external resolutions,
native links, model and carrier remain unchanged.

These mappings cover canonical ordering, shared serialization and digest
components. They do not establish the combined requirement's totality,
lossless raw-admission roundtrip, native-constructor witnesses, rejection of
ambient state or complete satisfaction. The test helper contains assertions;
no ABIogenesis code or tests were executed. Its support-module and compiled
imports are outside the selected files and remain unverified. The overlay has
not been Lean checked.

This is a four-file demonstration, not an ABIogenesis-wide code inventory.
Unselected configuration, package aliases and imported dependencies were
unavailable to extraction. Their absence does not establish that they are absent
from the real project. The snapshot does not update itself when source changes.

## Rebuild or use another project

Use the [public code-overlay commands](../../build_tenants/graphify/README.md#follow-requirements-into-code-and-test-sources)
with the selected parser dependencies and exact pinned Graphify checkout.
Prepare from the exact generated base model, source manifest and corpus; select
code/tests explicitly; then use `task` to acquire the endpoint IDs and author a
mapping outside the run. `build` writes a fresh `built/explorer.html`.
Recheck currentness with `status` or a matching repeated build.

[VIEW.json](VIEW.json) records exact input, output and machinery identities.
The [application evidence](../../.ai-workspace/work/T019_CODE_REPRESENTATION/abiogenesis-01/README.md)
includes the exact commands, retained mapping and bounded verification results.

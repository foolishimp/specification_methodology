# Local Lean formal-gate source package

This is the T013 source-package recipe. It prepares an inspectable, reproducible
local tenant distribution after the Executive selects the final scale/reuse
candidate. **No final selection, archive, installation, release or qualification
is issued by this preparation.** The current source remains mutable.

This repair successor uses source-package manifest schema
`a_c.lean.source-package/2`. The original preparation and its version-1 verifier
remain immutable historical cuts; this verifier does not reinterpret them.

The package contains Lean definitions/proofs, Python bridge and gate sources,
exact dependency locks, checked-in fixture data, requirements/claim boundaries,
and the small Graphify source subset needed by the reusable tests. It preserves
the `a_c/build_tenants/{lean,graphify}/` relationship. It is not a whole a_c
Product checkout; omitted historical navigation targets are not runtime inputs.

## Claims and dependencies

The gate checks a declared finite structural fragment: model correspondence,
declared dependency closure and exact record-preserving projection with an
explicit record budget. It preserves `verified`, `refused`, `unsupported` and
`incomplete`. Budget refusal does not mean semantic invalidity; unfinished
checking is not a verdict of correctness or incorrectness.

Source-to-model fidelity, the sufficiency of declared dependencies, authority,
semantic acceptance, full-calculus validity and efficiency remain separate.
Packaging verifies byte custody. It supplies none of those conclusions.
FR-001–FR-014 and the tenant's design/boundary files are included unchanged.
The builder remains installed STDO v2.5.1-rc.2; represented STDO data does not
adopt a new builder. The external basis identity is in `toolchain-lock.json`.

[DEPENDENCIES.md](DEPENDENCIES.md) identifies the actual import and setup paths.
Python 3.11+ is required. Proof execution additionally requires the pinned Lean
4.35.0, Mathlib and transitive revisions, compatible compiled support, and the
trusted host. Only Darwin arm64 has retained local execution evidence. Pinned
download coordinates for other platforms are not qualification of them.

## Final selection and construction

Run these steps only after the separate execution grant and final source freeze.
`INVENTORY_PLAN.json` contains explicit paths; no glob adds package members.
Closed namespace scans refuse newly added helpers until a reviewed successor
plan names them. Update the plan explicitly for the final reuse/helper sources,
then independently review that selected plan. Do not silently refresh old pins.

The Executive's externally supplied freeze JSON has this exact shape:

```json
{
  "schema": "a_c.lean.package-freeze/1",
  "kind": "candidate",
  "selection_ref": "exact closed Executive source-selection reference and SHA-256",
  "runtime_identity": {
    "sha256": "actual final public identity sha256",
    "pins": {"scripts/formal_gate.py": "actual source digest, plus every identity pin"}
  }
}
```

The example strings are placeholders and cannot pass validation. The actual
`runtime_identity` must be the entire final qualified host `{sha256,pins}` object.
Its digest must equal SHA-256 of compact sorted UTF-8 JSON of `pins`. The manifest
retains that full identity and derives a separate `portable_runtime_identity` by
omitting **only** the exact coordinate
`.cache/formal-origin-v1/selection.json`, if present. The derivation is fixed in
the verifier; there is no caller-provided ignore list. All other code, profile,
proof-support and toolchain pins remain present, exact and at their original
Lean paths. The portable aggregate digest is recomputed over precisely those
remaining pins. If the fixed origin coordinate is absent, the identities agree.

The omitted coordinate's hash remains qualified-host provenance; its contents
are never acquired or packaged. Another private coordinate or spelling is
refused, not silently omitted. Full-origin execution evidence remains evidence
under that full identity. It is not relabelled as a portable run. A later local
origin-free installation must report the derived portable identity and qualify
its own actual execution. No prior origin cache/key or reuse eligibility travels
with this source package. Establishing new origin reuse would be a separate
selection with its own identity and evidence. Selection references record an
external decision; this tool does not authenticate who made it.

From the original source checkout, with absolute paths chosen explicitly:

```sh
python3 -B PACKAGE_WORK/package_source.py select \
  --source-root SOURCE_CHECKOUT --plan PACKAGE_WORK/INVENTORY_PLAN.json \
  --freeze FINAL_FREEZE.json --output FINAL_SELECTION.json

python3 -B PACKAGE_WORK/package_source.py build \
  --source-root SOURCE_CHECKOUT --selection FINAL_SELECTION.json \
  --manifest-sha256 ACTUAL_SELECTION_SHA256 --output NEW_BUNDLE_OUTSIDE_SOURCE

python3 -B PACKAGE_WORK/package_source.py verify-tree \
  --tree NEW_BUNDLE_OUTSIDE_SOURCE --manifest-sha256 ACTUAL_SELECTION_SHA256

python3 -B PACKAGE_WORK/package_source.py archive \
  --tree NEW_BUNDLE_OUTSIDE_SOURCE --manifest-sha256 ACTUAL_SELECTION_SHA256 \
  --output NEW_ARCHIVE_OUTSIDE_BUNDLE.tar
```

Replace uppercase path/hash tokens with exact selected values. Output parents
must exist; output files/directories must not. Root arguments containing `..`
are rejected before overlap checks; original symlink ancestors remain forbidden.
No command overwrites a previous
cut. The source selection becomes the bundle's `SOURCE_PACKAGE.json` without
rewriting. Record its raw digest from `select`, and the actual archive digest
from `archive`, in the later independently reviewed handoff. Neither digest is
invented or captured at this preparation stage.

## Acquisition, verification and repacking

Acquire the later selected archive, trusted manifest hash and trusted verifier
through the Executive's exact handoff. Compare the archive's SHA-256 with that
handoff before parsing it. A hash distributed only inside its own archive does
not authenticate the archive. Use an independently selected verifier copy:

```sh
python3 -B TRUSTED_PACKAGE_SOURCE.py verify-archive \
  --archive ACQUIRED.tar --manifest-sha256 TRUSTED_MANIFEST_SHA256
python3 -B TRUSTED_PACKAGE_SOURCE.py extract \
  --archive ACQUIRED.tar --manifest-sha256 TRUSTED_MANIFEST_SHA256 \
  --output FRESH_EXTRACTION
python3 -B TRUSTED_PACKAGE_SOURCE.py verify-tree \
  --tree FRESH_EXTRACTION --manifest-sha256 TRUSTED_MANIFEST_SHA256
```

The extracted directory can be verified without the source checkout or archive.
It can also reproduce the archive directly, without omitted originating-workspace
inputs or metadata transformations:

```sh
python3 -B FRESH_EXTRACTION/package_source.py archive \
  --tree FRESH_EXTRACTION --manifest-sha256 TRUSTED_MANIFEST_SHA256 \
  --output NEW_REPACK.tar
```

The uncompressed tar uses sorted regular-file members and fixed timestamps,
ownership and modes. Synthetic tests establish exact repacking for the tested
case. Final-candidate reproducibility still needs the later real package check.

## Local use after separately selected setup

Source verification does not install proof support. The archive excludes every
`.cache`, private origin selection/key/entry, temporary state, `.lake`, and
`.toolchain` member. The selected public `profiles/proof-support-v1.json` remains
included: it is established-support provenance and an exact member map, not the
compiled members or a private reuse credential.

An existing qualified host may supply a separately authorized local copy of the
exact immutable support named by that map. Do not copy it as part of this source
archive, copy private reuse state, or replace missing objects with a success
label. That local support copy and its complete hash/currentness verification
require a later grant. A clean extracted source package is not yet a verified
gate installation.

For a new host, `python3 -B scripts/bootstrap.py` in the Lean directory acquires
the pinned compiler and selected Mathlib imports, checking the archive hash and
compiler/Mathlib revisions. It uses Git, curl and tar with zstd support. It does
not establish that freshly acquired/rebuilt objects match the selected support
map, perform the generic proof replay, or qualify a new support selection.
Fresh establishment would select a new verifier identity and require its own
bounded proof and independent assessment. No new whole-library replay is
selected by this recipe; do not run the setup-only establishment command as an
automatic fallback. Missing support remains an explicit incomplete setup.

After exact support is separately established and checked, the usable commands
from `a_c/build_tenants/lean/` are:

```sh
python3 -I -S -B scripts/formal_gate.py identity
python3 -I -S -B scripts/formal_gate.py verify --request REQUEST.json --output FRESH_EVIDENCE
python3 -I -S -B scripts/formal_gate.py check-evidence --bundle RETAINED_EVIDENCE --output FRESH_REPLAY
python3 -B -m unittest discover -s tests -p 'test_*.py' -v
python3 -B scripts/check_gate.py --output FRESH_QUALIFICATION
```

Before running the checks, compare the origin-free installation's actual public
`identity` result with `portable_runtime_identity` in the trusted manifest. A
mismatch stops qualification. The qualified-host identity retained in `freeze`
cannot stand in for that observation or authorize reuse on this installation.

These are documented operations, not execution evidence from this preparation.
`check_gate.py` exercises real checking and imports the included Graphify test
helpers. Its optional `--large-model PATH` requires a separately exact-pinned
subject; the 1,987-record application and its historical evidence are not copied
into the source package. Complete selected model/view qualification remains in
the eventual independent handoff. The package does not claim the full Graphify
test suite or external Graphify upstream compatibility.

Run strict tree verification before setup: compiler/cache creation changes that
tree, so it will intentionally fail a later exact source-tree inventory check.
Retain an untouched verified extraction for independent source verification and
repacking. A working local installation is a separately identified copy.

## Controls and remaining work

The packager rejects source/output overlap, symlinked paths, duplicate/case-
colliding names, noncanonical paths, runtime/private members, changed bytes,
missing/extra files or directories, inconsistent metadata and stale runtime
pins. All banned component, suffix and private-origin spelling checks use
case-folded comparisons before source acquisition. Extraction validates the
entire bounded inventory before writing and
manually writes regular files; it rejects links, devices, traversal, duplicates,
extra payload and trailing nonzero tar data. It never calls `extractall`.
Inputs and destinations must be quiescent; this is not protection against a
concurrent malicious host replacing paths during an operation. An interrupted
operation may leave a partial fresh output; no success is issued for it.

Remaining: select final sources and any new helpers; review the inventory;
construct, inspect, extract and reproduce the actual archive; separately grant
and verify local support setup; run the selected installed-use checks; and
independently assess those results. Product acceptance and public release are
not selected. No fresh-machine qualification is claimed.

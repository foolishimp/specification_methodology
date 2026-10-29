# Source dependency and support inventory

This is the source-inspected package inventory for the integrated T013 cut.
`SOURCE_OBSERVATION.json` records exact public source bytes and import coverage.
The two explicit additions are `scripts/formal_reuse.py` and
`tests/test_formal_reuse.py`; the reviewed packager and controls are byte-identical
to repair 002. The full post-origin checker identity must arrive through the
ScaleWorker/Executive handoff before final freeze. No private origin file is read
to construct this inventory, and no runtime qualification is claimed.

| Path or operation | Required files and preserved relationship |
| --- | --- |
| `lean/scripts/formal_gate.py` CLI | Exact flat `scripts/*.py` namespace selected by the implementation, `profiles/*.json`, six deciding `AC` modules and the four toolchain/Lake files. The CLI loads exact local helper source. Its runtime path imports no Graphify source or third-party Python package. |
| `lean/scripts/check.py`, importer and fixture generation | Checked-in `AC.lean`, all ten `AC/*.lean`, all six fixture files under `fixtures/stdo-3.0.2` and `fixtures/toy`, scripts and exact locks. The fixtures contain full model/carrier/custody data; their originating applications are unnecessary. |
| `lean/tests/test_formal_gate.py` | Imports sibling `graphify/code/ac_graph.py`, `ac_generate.py`, and `ac_formal_gate.py`; dynamically loads `graphify/test_env/test_ac_generate.py` to obtain `SOURCE` and `fixture_answer`. Those existing relative paths are retained. |
| New subject preparation | `ac_generate.prepare` enumerates and hashes all five files in `graphify/code/generation/`. All five are explicit inventory members, including `requirements.txt`. The test's direct mode uses authored fixtures and the built-in schema validator; it does not install that file's upstream-only packages or invoke an LLM. |
| `lean/scripts/check_gate.py` | Imports the same new-subject helper from `test_formal_gate`, runs the Lean test discovery and actual gate/kernel checks. It therefore needs the small Graphify subset even though ordinary gate execution does not. |
| `lean/scripts/formal_reuse.py` and `lean/tests/test_formal_reuse.py` | The integrated helper adds only Python standard-library imports. Its tests import the existing gate plus that helper, patch the origin root into disposable test storage and use synthetic proof stubs. Those controls do not establish real origin or proof success. The CLI exact flat namespace now contains eleven Python sources, all explicitly included. |
| `lean/tests/test_runtime_process.py` | Uses stdlib child-process probes and a tenant-local `.cache` directory. It is executable test code, not source-only verification; no invocation is made during package preparation. |
| Optional external subjects | Supplied model/carrier/view files are caller inputs, bound by the public gate request. Large applications, dogfood studies, actor workspaces and old evidence directories are not hidden package dependencies. |

The imported Graphify test module contains other test methods and a deferred
`ac_grounding` import. The selected Lean discovery does not run those methods.
This inventory does not support running all tests in `graphify/test_env`, actual
upstream extraction or the full F_D dispatch service. Those would require a
separate broader package selection. No Graphify external Python package is
needed by the inspected Lean paths above.

The closed Lean source namespaces and Graphify generation-assets directory are
checked against explicit plan entries at final selection. Enumeration detects a
missing entry; it does not trust an unexpected new file as a package member.
The two integrated reuse files are named additions; any later module or test still requires a named reviewed successor. The plan's source
paths remain original repository-relative coordinates; package-only documents
and the packager are deliberately mapped to short top-level paths. Their exact
origin paths and bytes remain in `SOURCE_PACKAGE.json`.

## Exact acquisition and established support

`toolchain-lock.json` selects Lean 4.35.0 commit
`eb6cafb7290e8bd5f2937522d8d804f58f02bafc`, archive names and SHA-256 values for
four platforms. `lakefile.toml`, `lake-manifest.json` and `lean-toolchain` select
Mathlib commit `56a005855ea17e0b0958f73ec801ae140b0a1679` and all transitive Git
revisions. The manifest's exact `rev` values are operative even where upstream
`inputRev` labels say main/master. Bootstrap deliberately does not run `lake update`.

`profiles/proof-support-v1.json` is a large public source-owned manifest. It
retains exact prior successful replay source/log/manifest provenance, the
conserved extension and selected member digests. `formal_support.py` pins the
prior origins and checks source/object/runtime members and unselected import
objects. Retained text and member names are not the named compiled support
files. Packaging that manifest preserves its established-support claim and
boundary; it neither establishes a new origin nor makes the binaries available.

The actual inspection found a Darwin-arm64 selected map with 30,405 members
and about 19.3 MB of public manifest text. That is an observation of this cut,
not a required final member count. Later source changes must be selected in
their own right. Ordinary `.lake`/`.toolchain` binaries and all private reuse
selection/key/entry material are excluded. A local support-copy qualification,
if selected later, must remain separate from the source archive.

For an origin-enabled final host, manifest schema 2 retains its complete qualified
identity as metadata and derives the portable identity by removing exactly
`.cache/formal-origin-v1/selection.json`. All deciding public pins and their
population remain exact; private selection contents are neither read nor copied.
The portable artifact has no old-origin reuse authority. Its separately selected
installation must report and execute under the derived origin-free identity.
This identity projection is a packaging contract; no installed proof or reuse
qualification follows from the synthetic preparation controls.

The exact STDO builder manifest and calculus digests are in the lock and common
requirements. The package includes the bounded owning requirements and tenant
claim ledger but does not install a methodology release. Neither an installed
STDO document nor the full applications/dogfood history is a Python/Lean runtime
input on the inspected gate path.

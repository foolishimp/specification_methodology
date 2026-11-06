# Common build tools

This directory is the common tenant's registered implementation territory.
The tools require Python 3.11+ and the standard library. They are construction
tools; the ordinary native method payload installs the generated documentation,
plus the explicitly selected tooling distribution; this construction directory itself
is not a runtime dependency.

- `documentation.py` bundles and checks the selected offline documentation. It uses
  sibling `package_tools.py` and `proof_reader.py`; no working record
  supplies executable code. Run `python3 -I -B documentation.py check PACKAGE`.
- `package_tools.py` is the single standalone package checker and materializer.
  Use its `--help` for explicit input/output operations. Existing trusted
  single-file launchers may select this file's digest before execution.
- `native_release.py --configuration /absolute/path/native-preparation-config.json
  --configuration-sha256 EXACT_SHA256 COMMAND ...` prepares the selected
  current stable candidate. The separate frozen configuration controls version,
  predecessor, output territory and mandatory component selection. Configured
  native preparation cannot publish alone; the complete five-Product cohort
  checker governs publication. The later external manifest binds this exact
  configuration without changing it or creating a native self-hash cycle.
  The older digest-bound `--cohort-manifest` interface remains supported.
  Omitting both selection mechanisms selects the retained
  historical 3.0.4 preparation profile and `STDO304_DELIVERY/native-release/`
  territory, never the current candidate. This tool performs no Git mutations,
  installations or publication. Current public asset closure includes the
  exact native manifest, version-matched manager wheel, selected component
  assets and external cohort manifest; native/installed checks separately
  establish all five Products and required capabilities.
- `qualify_documentation.py --package PACKAGE --run ABSENT --stdo EXECUTABLE`
  exercises the selected installed manager through a synthetic repository/tag
  and disposable store. It records install/verify/resolve and tamper results;
  it does not observe browser rendering or create a public release.

Keep this implementation directory together when relocating it. Missing
required helper files yield refusal. Historical entry paths under
`.ai-workspace/` are compatibility launchers to the registered implementation;
they are not required by these tools. Existing frozen evidence retains the
implementation identities used for its original observations.

Run `python3 -B -m unittest discover -s . -p test_documentation.py` for focused
documentation and release-asset controls. These tests run against the sibling
`../common` payload. Browser/WebGL qualification and exact published-install
readback remain distinct obligations.

The tooling distribution is built with `tooling.py build --repository ROOT
--destination ABSENT`, using explicit `tooling-selection.json`. Its checker is
`tooling.py check PACKAGE`; `tooling_materialize.py` is copied exactly into the
installed source bundle. `test_tooling.py` covers extraction and inventory
refusals. `qualify_tooling.py --help` exercises extracted public commands from
an arbitrary current directory using an existing disposable installation.

Current stable packaging uses explicit, digest-bound selections:

- `proof_reader.py build-current --repository ROOT --selection FILE
  --selection-sha256 SHA --output ABSENT` invokes the formal owner's
  `inspect-evidence` against a fresh recovery from the selected committed
  transport parts and exact request. It retains the complete proof artifacts, runtime source pins, source
  freeze, current correspondence, original library provenance and inspection.
  Its checker verifies custody and reproduction, never a new Lean execution.
  `proof_evidence.py pack` and `split` produce deterministic exact ZIP transport
  with bounded 64 MiB parts. The installed copy recovers the complete original
  bundle and prepares a separate local-path request for actual installed Lean
  verification. Original construction request/argv bytes remain provenance.
- `documentation.py bundle-current --repository ROOT --selection FILE
  --selection-sha256 SHA --destination ABSENT` joins the complete frozen source,
  exact model, source manifest, owner-reproduced unified viewer and current
  proof reader. All readers use the same selected model. Its guide links the
  external five-Product manifest; that manifest is not embedded in native A.
- `tooling.py build --repository ROOT --selection FILE --selection-sha256 SHA
  --destination ABSENT` selects regular members from the four peer owner
  inventories. It packages portable source, the materializer and `setup.py`.
  Setup creates a separate runtime-installation anchor and a manager launcher
  with explicit store and executable/native pins, then delegates host binding
  to the selected Skills installer. Nominated construction Products retain
  their own basis. Graphify/Lean setup and actual installed qualification are
  separate operations with their own receipts.

Schema-1 historical checks retain their exact source/materializer fixtures in
`fixtures/`. Do not omit that directory when moving the registered tools.
`test_current_assets.py` exercises current selection, archive, source/model/view
bindings, and actual manager-launcher refusal controls. Set
`STDO_PROOF_CONTROL` to an explicitly retained toy reader for owner-evidence and
offline DOM integration tests; it is never current STDO-model proof. DOM tests
require `jsdom` through `NODE_PATH`; the anchor-schema test uses `jsonschema`.

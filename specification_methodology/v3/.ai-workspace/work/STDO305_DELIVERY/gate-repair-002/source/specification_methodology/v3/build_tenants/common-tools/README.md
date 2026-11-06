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
- `native_release.py --cohort-manifest /absolute/path/stack_release.json
  --cohort-manifest-sha256 EXACT_SHA256 COMMAND ...` prepares the selected
  current stable candidate. The digest-bound manifest controls version,
  predecessor, output territory and mandatory component selection. Configured
  native preparation cannot publish alone; the complete five-Product cohort
  checker governs publication. Omitting both options selects the retained
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

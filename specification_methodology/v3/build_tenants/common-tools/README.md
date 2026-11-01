# Common build tools

This directory is the common tenant's registered implementation territory.
The tools require Python 3.11+ and the standard library. They are construction
tools; the ordinary native method payload installs the generated documentation,
plus an exact source-only a_c/Skills bundle; this construction directory itself
is not a runtime dependency.

- `documentation.py` bundles and checks the selected offline documentation. It uses
  sibling `package_tools.py` and `proof_reader.py`; no working record
  supplies executable code. Run `python3 -I -B documentation.py check PACKAGE`.
- `package_tools.py` is the single standalone package checker and materializer.
  Use its `--help` for explicit input/output operations. Existing trusted
  single-file launchers may select this file's digest before execution.
- `native_release.py` prepares and checks exact STDO 3.0.3 native release
  records. It consumes sibling `documentation.py` and keeps output confined to
  this source project's `STDO303_DELIVERY/native-release/` territory. It performs
  no Git mutations, installations or publication. The required public assets
  are the native manifest and manager wheel; extra explicitly selected assets
  are optional.
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

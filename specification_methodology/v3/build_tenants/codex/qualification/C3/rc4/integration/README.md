# RC4 integration

This directory binds the existing render, account and package operations to the
RC4 repair. `INPUTS.json` names the frozen inputs and unchanged helpers;
`COORDINATES.json` records completed source, account and package freezes.
Historical RC1 and iteration records remain unchanged.

`integrate.py` uses the prior operations with this directory as the output
owner. It adds current authored conservation comparisons, preservation of the
previous repair records, and agreement of the two plugin manifests with
`3.0.0-rc.4`. It introduces no runtime or method law.

Run from this tenant with the selected toolchain Python. Use exact coordinates
from `COORDINATES.json`; each phase consumes the preceding frozen result:

```sh
/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python -B \
  qualification/C3/rc4/integration/integrate.py source \
  --source-commit "$RC4_AUTHORED_INPUT" --theory-root "$RC4_THEORY_ROOT"
/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python -B \
  qualification/C3/rc4/integration/integrate.py account \
  --source-commit "$RC4_SOURCE"
/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python -B \
  qualification/C3/rc4/integration/integrate.py generate \
  --source-commit "$RC4_SOURCE" --account-commit "$RC4_ACCOUNT" \
  --theory-root "$RC4_THEORY_ROOT"
/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python -B \
  qualification/C3/rc4/integration/integrate.py verify \
  --source-commit "$RC4_SOURCE" --account-commit "$RC4_ACCOUNT" \
  --package-commit "$RC4_PACKAGE" --theory-root "$RC4_THEORY_ROOT"
```

`RC4_AUTHORED_INPUT`, `RC4_SOURCE`, `RC4_ACCOUNT` and `RC4_PACKAGE` are
respectively the authored-input, documentary-source, account and package
commit fields in `COORDINATES.json`.

`RC4_THEORY_ROOT` identifies the exact installed `v2.5.1-rc.2` encoding theory,
verified at the manifest digest in `INPUTS.json`. Its location is an environment
binding. This is not an installed-v3 test or an adoption instruction.

For reproduction, use a disposable copy at the authored-input commit and
compare generated output with the named freezes. Running `source` over its
already-replaced compression preimages is deliberately refused. Native
projection cases in `PROJECTION_CASES.json` check route availability; they do
not prove source fidelity, useful context size or complete assessment. The
independent semantic readback has a separate subject and return in common
commentary.

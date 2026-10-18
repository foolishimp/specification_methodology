# Final repair integration

This directory binds the existing source, account and package operations to the
final reciprocal-review repair. [Dispositions](DISPOSITIONS.md) explain the
selected source corrections, representation repair and rejected source gaps.
Historical helpers and qualification records remain unchanged.

The wrapper imports the RC4 operations with new immutable input and output
coordinates. It groups the illustrative Worked Binding replacement under the
existing RF-005 question and uses the selected candidate label. It introduces
no method or runtime mechanism.

Run from the Codex tenant using the toolchain Python. The authored-input,
source, account and package commits are separate freezes; use their exact
values from `COORDINATES.json` after the return is complete:

```sh
/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python -B \
  qualification/C3/rc5/integration/integrate.py source \
  --source-commit "$FINAL_AUTHORED_INPUT" --theory-root "$FINAL_THEORY_ROOT"
/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python -B \
  qualification/C3/rc5/integration/integrate.py account \
  --source-commit "$FINAL_SOURCE"
/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python -B \
  qualification/C3/rc5/integration/integrate.py generate \
  --source-commit "$FINAL_SOURCE" --account-commit "$FINAL_ACCOUNT" \
  --theory-root "$FINAL_THEORY_ROOT"
/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python -B \
  qualification/C3/rc5/integration/integrate.py verify \
  --source-commit "$FINAL_SOURCE" --account-commit "$FINAL_ACCOUNT" \
  --package-commit "$FINAL_PACKAGE" --theory-root "$FINAL_THEORY_ROOT"
```

`FINAL_THEORY_ROOT` is the exact installed v2.5.1-rc.2 theory root at the
manifest digest in `INPUTS.json`. Reproduce in a disposable copy beginning at
the authored-input commit; `source` refuses already-replaced compression
preimages. Native projection cases establish route availability only. Semantic
readback, complete qualification and owner acceptance have separate subjects.

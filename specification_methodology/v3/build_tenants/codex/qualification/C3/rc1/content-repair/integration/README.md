# Current content-repair integration

[COORDINATES.json](COORDINATES.json) and [RETURN.md](RETURN.md) identify this
repair's frozen phases and remaining work. Earlier I5, RC1 integration and
end-repair records retain their historical subjects.

`integrate.py` binds existing account, rendering, interpretation and package
helpers to this directory. The parent supplies each exact checkpoint before
the next phase runs: authored input, documentary source, authored account,
complete package, then verification. Its operations are `source`, `account`,
`generate` and `verify`, with the applicable `--source-commit`,
`--account-commit`, `--package-commit` and `--theory-root` arguments.

Run from the own checkout root with
`/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python -B`. The exact encoding
theory is `/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2`.
An available script supplies no new execution, acceptance or release grant.

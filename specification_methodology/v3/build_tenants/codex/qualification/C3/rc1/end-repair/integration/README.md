# Current end-review repair entry

`COORDINATES.json` identifies this successor's exact source, authored account and package. `CANDIDATE.json` is the complete package inventory. `DETERMINATIONS.json`, `CONSERVATION.json`, `REPLACEMENT_QUESTIONS.json` and `FRONTIER.json` are the current author accounts for this repair. Earlier I5 and `rc1/integration` records retain their historical subjects. `QUALIFICATION.md` records current scope and pending decisions.

From the own checkout root, use the installed STDO Python environment:

```sh
/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python -B specification_methodology/v3/build_tenants/codex/qualification/C3/rc1/end-repair/integration/repair.py generate --coordinates specification_methodology/v3/build_tenants/codex/qualification/C3/rc1/end-repair/integration/COORDINATES.json --theory-root '/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2'
/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python -B specification_methodology/v3/build_tenants/codex/qualification/C3/rc1/end-repair/integration/repair.py verify --coordinates specification_methodology/v3/build_tenants/codex/qualification/C3/rc1/end-repair/integration/COORDINATES.json --theory-root '/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2'
```

Generation authenticates the selected source inventory, frozen account and existing compiler/native dependencies. Verification binds those receipts to the package and runs only the changed-scope checks and two selected native projections. Output elapsed fields can vary on replay; the exact frozen package remains the subject. The `account` operation is the one-time authored-patch integration before the account freeze, not an implicit replay against a later source.

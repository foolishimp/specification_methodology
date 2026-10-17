# RC1 integrated construction

`COORDINATES.json` identifies the exact documentary source, authored account and complete package. `CANDIDATE.json` lists every package member, its byte length and SHA256. `CHANGED_SCOPE.json` records the consolidated Writer check. `RETURN.md` states the outcome and remaining qualification.

From the own checkout root, reproduce current generation with the installed STDO Python environment, which supplies the native checker's `jsonschema` dependency:

```sh
'/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python' -B specification_methodology/v3/build_tenants/codex/qualification/C3/rc1/integration/rc1.py generate --coordinates specification_methodology/v3/build_tenants/codex/qualification/C3/rc1/integration/COORDINATES.json --theory-root '/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2'
```

The standalone current verification invocation is:

```sh
'/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python' -B specification_methodology/v3/build_tenants/codex/qualification/C3/rc1/integration/rc1.py verify --coordinates specification_methodology/v3/build_tenants/codex/qualification/C3/rc1/integration/COORDINATES.json
```

Generation authenticates the documentary member set and bytes at the source commit, the authored account bytes at the account commit, the exact account documentary inventory, immutable encoding theory and installed native checker. It invokes the selected I5 compiler and native validation, writing only current interpretation and RC1 evidence. Verification authenticates the package and generation receipts at the package commit, reproduces the views, checks the affected rule and consumers, checks complete package integrity and performs the existing cold identity fixture once. Evidence reports can contain a new elapsed time on replay; the frozen package bytes remain their subject.

`rc1.py` imports byte-pinned existing helpers. It adds current coordinates, explicitly authored source-account changes, exact repeated-block relocation, closed consumer-patch ingestion and current applicability accounting. It changes no compiler, native checker or historical entrypoint. It does not run the eighteen historical projections or full historical suites.

The `source` operation is a one-time construction step from the complete `5fd3b789ef6e0039f722676cdd0126113c745a11` documentary preimage. The `account` operation authenticates the source freeze and integrates the one generic repair over the exact prior account. Admitted consumer groups are then applied by `consumers --consumer-commit <exact-return-commit> --consumer-patch <selected-file>`, with both field presence and value checked against each preimage. These construction stages precede the frozen current invocation above; they are not silently repeated against a later subject.

`REUSE.md`, `CONSERVATION_APPLICABILITY.json` and `FRONTIER.json` preserve the limits of prior evidence and current dependencies. `ACQUISITION.json` records incomplete source/context instrumentation. This is a reviewable construction package; qualification, acceptance and release decisions remain separate.

The final candidate includes the Executive-selected plugin manifest version metadata. Use the same `rc1.py generate --coordinates ... --theory-root ...` command for generation. The final verification entrypoint is:

```sh
/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python -B specification_methodology/v3/build_tenants/codex/qualification/C3/rc1/integration/version_metadata.py verify --coordinates specification_methodology/v3/build_tenants/codex/qualification/C3/rc1/integration/COORDINATES.json
```

`version_metadata.py` authenticates final documentary/account/package coordinates, proves that the four package differences from the first freeze are exactly two version fields and two generated source-coordinate carriers, and binds the successful first-package checks at `ba547177d7c9f2977fd48fa025618264f913a00a` to their unchanged subjects. It preserves every account row and earlier semantic/reuse limitation. The original `rc1.py verify` command remains the historical first-package invocation; its check receipts are not relabeled current.

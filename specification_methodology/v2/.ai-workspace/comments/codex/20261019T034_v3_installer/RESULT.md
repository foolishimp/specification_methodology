# Standalone V3 installer delivered

`stdo-toolchain 0.1.5` is integrated on main and installed as
`/Users/jim/.local/bin/stdo`. It reads a standalone package at the published
`specification_methodology/v3/` root from an exact annotated immutable cut.
Basic installation requires no a_c implementation or STDO Representation.

Source checkpoints `8c547f46` and `4d5de9aa` were integrated as `1a37ee9f`
and `79fa6edb`. All eleven installed Python modules match the reviewed source
and built wheel. Only the toolchain distribution changed in its Python
environment: `0.1.4` to `0.1.5`; all dependency versions are unchanged.

## Verification

| Claim | Observation |
|---|---|
| Regression conservation | [179 tests passed](tests-full.txt), including known immutable V2 manifest hashes and exact RC4 builder verification |
| Independent review | [Satisfied, no material findings](REVIEW.md); fresh V3 and historical/refusal runs, plus independent member-hash comparison and CLI replay |
| Real Git acquisition | Both [source](source-cli/cli-replay.json) and [installed executable](installed-cli/cli-replay.json) installed all 81 frozen common payload files byte-for-byte from an actual annotated fixture tag |
| Package contents | 62 standards, 17 plugin files, LICENSE and release note; canonical standards digest `c60b469b34e80c61e8e8ce5d4f48eb4f12777dfda37ce88f561cf9c12609a1fb` |
| Consumer mechanics | Exact-basis sync, schema/integrity status, resolution of all four V3 entrypoints, idempotent bootstrap, and explicit same-line adoption pass in isolated consumers |
| Refusal behavior | Ambiguous/missing layout, tenant-only input, wrong-major package, missing package note, wrong manifest and changed member refuse; restoring fixture bytes restores verification |
| Packaging | [Wheel identity](wheel-identity.json), SHA-256 `0959b17057aaa46c82a70afbcffca877540b6d1304edc2a8aeaa5cfbbf7b0cc9`, with every packaged module compared to source |
| Existing installed releases | [All 807 files unchanged](after-local-update.json), including registry; inventory digest remains `9b8881b49ee716661bf30a6922b5db1dd21932bec254e0c9a6ae74f0c01fe75c` |

The full suite initially found one historical diagnostic-label regression;
`4d5de9aa` restored that wording, and the complete rerun passed. The initial
log is retained as `tests-initial.txt`. Lint and Git whitespace checks pass.
Testing ran under the existing Python 3.13.7 environment; declared support
remains Python 3.11 or newer.

## Exact package and replay boundary

The source package is commit
`494451522072ec34381c644f1ccfa2331f2b1e27`, path
`specification_methodology/v3/build_tenants/common`, tree
`082df4ea2b7b3658aab528bbfbcfe81234ccc810`. Re-rooting those exact bytes into
an isolated Git repository preserves that project tree. Its real fixture
commit is `2f70c08eaf45949901f9c1d839ca3466ec83d236`, annotated tag object
`8bc886b16260b05d210997ef07ecdcc2808c299f`. The fixture manifest is
`d63e0aa15eb44dd3e7f004d00404453459573f0524fbbe95f981a2c383429f65`.

`v3.0.0-rc.9999` exists only as the replay's temporary fixture identity. It was
not created in the source repository or installed in the real shared store.
The fixture manifest is not the digest of any future published V3 release.
No common candidate, original tenant, a_c or Representation source was edited.
No release refs, selectors, real consumer definitions or remotes were changed.

To repeat the installed-executable observation from the toolchain directory:

```sh
/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python \
  .ai-workspace/comments/codex/20261019T034_v3_installer/replay_v3_package.py \
  --source-repository /Users/jim/src/apps/specification_methodology \
  --cli /Users/jim/.local/bin/stdo \
  --output /tmp/stdo-v3-installer-replay
```

The script creates and removes its own Git repository, stores and consumer.
Omit `--cli` to exercise the checkout's source with that Python interpreter.

## Consumer migration boundary

Installation support is complete at this scope. Publishing V3 and accepting
its method remain separate. V2 consumers also need explicit review of their
entrypoints and local authority before migration: `adopt` preserves those
routes, and structural status alone cannot establish their resolution. The
[installation guide](../../../../V3_INSTALLATION.md) provides the exact scope
and three changed built-in routes. The selected-cohort updater remains
unchanged and has not acquired a bypass for missing companions.

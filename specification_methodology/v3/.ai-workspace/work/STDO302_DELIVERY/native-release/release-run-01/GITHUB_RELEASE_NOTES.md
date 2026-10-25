# STDO 3.0.2

STDO 3.0.2 is a published immutable release with no RC suffix. It adds recursive
Product composition, explicit edge authority and context conditions, composition
contracts and examples, and source-matched reference frames. The stable-v1 release
profile gives this exact version an immutable tag while preserving historical
RC release and selector semantics.

The accompanying manager 0.1.6 wheel supports stable acquisition and explicit
composition-edge verification. The updated a_c and Codex/Claude Skills sources are
checkpointed on main; those independently owned tools and their consumer bases
retain their own lifecycle. Installing the native method does not adopt a project
or change an existing method installation.

## Exact release

| Coordinate | Identity |
|---|---|
| Immutable tag | `specification_methodology/v3.0.2` |
| Native commit C | `23ca9c0929d7be8570edafaf30542e3daeb8dc1f` |
| Annotated tag object T | `d03b00a7fdf8972dc236b52eb09f3eccba7f62cb` |
| Native manifest SHA256 | `f7f3f824ee1ac3e048d1b1ea86ce3aae84866e2e9d5010fe5eda2e38e12f4477` |
| Manager wheel SHA256 | `ef726f780220a4be93c8ce014e2838d140851ec0e3d47902ea2ddd36a26c3242` |
| Reviewed source A | `44448b14ecc9c5636d0e7972c7a4f1a80a07c623` |

The native distribution contains 86 payload files plus its installed manifest:
standards, generated frames, the supplied spec plugin, licence and release note.
The native predecessor is the published 3.0.1 RC1 commit; its tags and bytes remain
unchanged. No legacy 2.* coordinated cohort is republished.

## Install the exact method

Use Python 3.11 or later. Download the manager wheel, native manifest and their
checksum sidecars from the assets below. In that download directory, verify and create a separate environment:

```sh
shasum -a 256 -c stdo_toolchain-0.1.6-py3-none-any.whl.sha256
shasum -a 256 -c stdo-v3.0.2-manifest.json.sha256
python3 -m venv .stdo302
.stdo302/bin/python -I -m pip install ./stdo_toolchain-0.1.6-py3-none-any.whl
.stdo302/bin/python -I -m stdo_toolchain.cli --store ./stdo-store install v3.0.2 \
  --repository https://github.com/foolishimp/specification_methodology.git \
  --manifest-sha256 f7f3f824ee1ac3e048d1b1ea86ce3aae84866e2e9d5010fe5eda2e38e12f4477
.stdo302/bin/python -I -m stdo_toolchain.cli --store ./stdo-store verify v3.0.2 \
  --manifest-sha256 f7f3f824ee1ac3e048d1b1ea86ce3aae84866e2e9d5010fe5eda2e38e12f4477
```

The manager wheel is a separate distribution asset, not executable content added
to the native standards package. Existing installed 3.0.1/2.5.1 and pinned project
bases remain unchanged by this separate-store installation.

## Representation and evidence

The separate `stdo-v3.0.2-composition-release-supplement.tar.gz` and its sidecar bind
the same native commit and manifest. The archive supplies 32 authored composition
and release records, exact source custody, both graph carriers, and a portable
verifier. Check the sidecar, extract the archive, then run:

```sh
python3 -I -S -B stdo-v3.0.2-supplement/supplement.py verify \
  --bundle stdo-v3.0.2-supplement
```

Independent source and local-native readbacks passed. The exact manager wheel
passed 121 affected tests; a_c support passed 240 tests. Fresh isolated local
installation and both carrier recoveries passed on these exact assets. The
supplement is bounded to the selected 32 records; it does not complete the earlier
whole-method representation. Whole-method practical qualification, host behavior
and cost/efficiency claims remain outside this release's established evidence.

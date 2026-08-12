# specification_methodology

Authoring source repository for the shared specification methodology.

Mutable future-method source lives under `specification/standards/`. Publication
authority is one immutable released STDO cut identified by version, immutable
reference, and exact member inventory. A consumer is governed by the complete
released cut it selects, whether referenced directly or installed into a local
location such as `.genesis/docs/standards/`.

Initial provenance:

- `SPEC_METHOD.md` first appeared in `genesis_sdlc` at commit `e27e895e7e6e1f80aaa337da52c23a6ea4669980` on 2026-03-27.
- `GRAPH_METHOD.md` first appeared in `genesis_sdlc` at commit `bfa5d7710e6ac4cab52f8d9bdc08e0f8740e6345` on 2026-04-03.
- `abiogenesis` installed the standards library from `genesis_sdlc/specification/standards/` through `gen-install.py` as of commit `f7820d4cfdff3e1b1cf270223f62b758a43a2214` on 2026-04-06.

Going forward, edit methodology here first. Downstream repos select and pin one
complete released STDO version. Mutable repository head is authoring input, not
consumer constitutional authority.

Release notes for tapped cuts live under `releases/`.

## License

Copyright 2026 Dimitar Popov.

Unless a file states otherwise, this repository and its STDO distributions are
licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE).

An installed or otherwise redistributed STDO cut must carry an exact copy of
that license with the standards payload. The license grants legal permissions;
it does not become normative methodology authority or alter the selected
release's standards-member identity.

Pre-constitutional work under development lives under `strategy/`. Those
artifacts are explicitly not-yet-ratified and graduate to `specification/`
only when re-authored as constitutional material. See `strategy/README.md`
for the authority boundary and graduation path.

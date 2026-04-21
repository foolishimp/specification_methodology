# specification_methodology

Definitive source repository for the shared specification methodology.

The authoritative shared methodology surfaces live under
`specification/standards/`.
Installers may vend copies of that tree into workspace-local locations such as
`.genesis/docs/standards/`, but those installed copies are distributions, not
the source of truth.

Initial provenance:

- `SPEC_METHOD.md` first appeared in `genesis_sdlc` at commit `e27e895e7e6e1f80aaa337da52c23a6ea4669980` on 2026-03-27.
- `GRAPH_METHOD.md` first appeared in `genesis_sdlc` at commit `bfa5d7710e6ac4cab52f8d9bdc08e0f8740e6345` on 2026-04-03.
- `abiogenesis` installed the standards library from `genesis_sdlc/specification/standards/` through `gen-install.py` as of commit `f7820d4cfdff3e1b1cf270223f62b758a43a2214` on 2026-04-06.

Going forward, edit methodology here first. Downstream repos should either
reference this repository directly as source authority or install copies from
this tree.

Release notes for tapped cuts live under `releases/`.

Pre-constitutional work under development lives under `strategy/`. Those
artifacts are explicitly not-yet-ratified and graduate to `specification/`
only when re-authored as constitutional material. See `strategy/README.md`
for the authority boundary and graduation path.

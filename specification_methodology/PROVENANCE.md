# Provenance

This repository was created to end ambiguity around the authoritative source of
the specification methodology.

## Origin

The currently adopted methodology was authored in
`/Users/jim/src/apps/genesis_sdlc/specification/standards/`.

The key authored origin points are:

- `SPEC_METHOD.md`
  - first added in commit `e27e895e7e6e1f80aaa337da52c23a6ea4669980`
  - date: 2026-03-27
  - subject: `Checkpoint gsdlcV2 spec and standards refactor`
- `GRAPH_METHOD.md`
  - first added in commit `bfa5d7710e6ac4cab52f8d9bdc08e0f8740e6345`
  - date: 2026-04-03
  - subject: `checkpoint: add graph method and usecase surfaces`

## Distribution Path

`abiogenesis` currently distributes the shared standards into installed
workspaces through:

- `/Users/jim/src/apps/abiogenesis/build_tenants/abiogenesis/python/code/gen-install.py`

That installer previously sourced its standards tree from:

- `/Users/jim/src/apps/genesis_sdlc/specification/standards/`

and installed it into:

- `workspace://.genesis/docs/standards/`

For example, the installed copies in
`/Users/jim/src/apps/odd_method/.genesis/docs/standards/` were byte-identical
to the `genesis_sdlc` source surfaces at the time this repository was created.

## Going Forward

This repository is now the authoring home for the shared methodology.

- Author methodology updates here.
- Publish accepted methodology as complete immutable versioned cuts.
- Bind installers, tests, and canonical references to one released version,
  immutable reference, and exact member inventory.
- Treat mutable repository head as future-cut authoring input, never as
  operative consumer law.
- Treat copies inside product repos or installed workspaces as selected
  distributions whose authority derives from their pinned release identity.

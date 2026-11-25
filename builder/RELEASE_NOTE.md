# STDO Builder 3.2.1

This is release 3.2.1 of STDO Builder: the command `stdo-builder` and the library it is a thin program over.
It runs on Node.js 24 or later.

- To install it, read `INSTALL.md`. The install checks every file against `manifest.json` before it writes anything.
- To use it, read `INSTRUCTIONS.md`.

## Licences

STDO Builder's own files, all but those under `lib/node_modules/` and `licenses/`, are under the Apache License 2.0, in `LICENSE`.
Each library the release ships keeps its own licence, which the release holds beside it in `licenses/<package>/`:

- @effect/platform-node 4.1.4, licence MIT
- @effect/platform-node-shared 4.1.4, licence MIT
- effect 4.1.4, licence MIT
- undici 8.12.4, licence MIT
- ws 8.23.0, licence MIT

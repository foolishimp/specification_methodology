# STDO 3.2.0

One release of two parts:

- `standards/`: the STDO standards, release v3.1.0-rc.2, with their plugin and licence.
- `builder/`: STDO Builder 3.2.0, the framework that builds a product to its specification under those standards.

To install: `sh install.sh <folder>`, then put `<folder>/bin` on your PATH.
It needs Node.js 24 or later, git, and an LLM agent command (Claude Code by default).
Then start with `builder/GETTING_STARTED.md`.

Builder still resolves the standards through the method's release manager, `stdo`,
as `builder/INSTALL.md` says. The copy installed from this bundle is for reading.

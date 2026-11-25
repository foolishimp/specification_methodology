# STDO Builder

STDO Builder builds a product to its specification. You write what you want in
the product's specification, or ask for a change in a ticket. Builder runs LLM
agent sessions step by step over one workspace, checks and judges each step,
asks you where the decision is yours, and merges the work when it is done. It
keeps one event log of what it did. Each ticket is built in the product's own
folder, on a branch of its own.

It is released as part of STDO 3.2.1, together with the STDO standards. Release
3.2.0 was reviewed in full and the verdict was no: do not use it on real work.
The [release note](../releases/3.2.1/RELEASE.md) says what 3.2.1 repairs and
what it does not.

## Get it

1. Download `stdo-3.2.1.tar.gz` from the
   [3.2.1 release](https://github.com/foolishimp/specification_methodology/releases/tag/stdo%2Fv3.2.1)
   and unpack it.
2. Run `sh stdo-3.2.1/install.sh <folder>` and put `<folder>/bin` on your PATH.
3. Follow [the getting-started guide](build_tenants/typescript/packaging/GETTING_STARTED.md).

It needs Node.js 24 or later, git 2.38 or later, the program `ps`, the method's
release manager `stdo`, and an LLM agent command (Claude Code by default). The
[install page](build_tenants/typescript/packaging/INSTALL.md) and
the [instructions for users](build_tenants/typescript/packaging/INSTRUCTIONS.md)
have the detail.

## Read it

- [The intent](specification/INTENT.md): what is built and why.
- [The product definition](specification/PRODUCT.md): what the product is.
- [The requirements](specification/requirements/): what it must do.
- [The design](build_tenants/typescript/design/), the tests and the code are
  under [build_tenants/typescript/](build_tenants/typescript/).

The product is defined by [stdo_builder.json](stdo_builder.json), which selects
the method release it is built under.

## Build it from source

In `build_tenants/typescript/`: `pnpm install`, then `pnpm check` runs the type
check, the tests and the compliance check. `pnpm release <version>` cuts a
release folder.

## Not in this release

The MCP tools interface, the service with an API, a workspace reached through a
service, and several tickets at once are not built. Builder finds the standards
through the method's release manager, `stdo`.

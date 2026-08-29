# specification_methodology

Authoring source repository for the shared specification methodology.

New to the toolchain or adding STDO to an existing project? Start with the
[STDO Quickstart](QUICKSTART.md).

Mutable future-method source lives under `specification/standards/`. Publication
authority is one immutable released STDO RC cut identified by its annotated tag,
commit, tree, and exact member inventory. A consumer is governed by the complete
cut pinned in its Product Definition. The `v<version>` tag is only the mutable
alias to the highest-ordinal published RC on that line.

The standards library includes the domain-specific
[`a_c` STDO Axiomatic Calculus for Governed Symbolic Systems](specification/standards/AXIOMATIC_CALCULUS.md).
`a_c` is the carrier-neutral constitutional calculus. Interpreted subjects and
carrier encodings are separately governed downstream layers; they become
Products only through their own acceptance and release authority.

STDO also provides the application-neutral [`a_c` Traversal Occurrence
Profile](specification/standards/TRAVERSAL_OCCURRENCE_PROFILE.md) for reasoning
about immutable application histories over externally mutable subjects. The
profile remains optional to adopt; availability does not activate it for a
consumer.

The `stdo` toolchain manager installs immutable cuts once in a shared versioned
store, resolves logical `stdo:` URIs, verifies installed bytes, synchronizes
already pinned Product Definitions, and performs explicit adoption and fleet
updates. Projects do not need a copied standards tree or prescribed layout.

During development, install the manager itself with an isolated Python
application installer:

```sh
pipx install .
```

For a released manager, install from an immutable RC tag rather than the moving
version-line alias:

```sh
pipx install "git+https://github.com/foolishimp/specification_methodology.git@v<version>-rc.<n>"
```

Then install or inspect a cut:

```sh
STDO_CUT='<immutable-cut>'
stdo install "$STDO_CUT"
stdo list
stdo resolve "stdo://releases/${STDO_CUT}/standards/SPEC_METHOD.md"
```

For a governed project, use `stdo sync --definition stdo_default.json` to
materialize the exact basis already pinned by that definition. Use the following
to inspect the latest published RC. Resolution fails closed if the alias lags
the highest published ordinal or would move the Product Definition backward.
The dry-run emits `plan_sha256`; pass that exact digest in a separate invocation
only when the project accepts the presented target:

```sh
stdo adopt --definition stdo_default.json --dry-run
stdo adopt --definition stdo_default.json \
  --accept-plan-sha256 <plan_sha256>
```

For a monorepo or a directory of independently governed projects, fleet reads
discover every `stdo_<label>.json` recursively. Writes require explicit
whole-selection authorization:

```sh
stdo fleet status --root /path/to/workspace
stdo fleet sync --root /path/to/workspace --all
stdo fleet adopt --root /path/to/workspace --all --dry-run
stdo fleet adopt --root /path/to/workspace --all \
  --accept-plan-sha256 <plan_sha256>
stdo fleet bootstrap --root /path/to/workspace --all
```

Bootstrap targets are portable paths relative to each definition's resolved
`product.source_project`. Fleet bootstrap first confirms that every source
project and target remains inside the authorized fleet root.

Initial provenance:

- `SPEC_METHOD.md` first appeared in `genesis_sdlc` at commit `e27e895e7e6e1f80aaa337da52c23a6ea4669980` on 2026-03-27.
- `GRAPH_METHOD.md` first appeared in `genesis_sdlc` at commit `bfa5d7710e6ac4cab52f8d9bdc08e0f8740e6345` on 2026-04-03.
- `abiogenesis` installed the standards library from `genesis_sdlc/specification/standards/` through `gen-install.py` as of commit `f7820d4cfdff3e1b1cf270223f62b758a43a2214` on 2026-04-06.

Going forward, edit methodology here first. Downstream repos select and pin one
complete immutable STDO RC cut. Mutable repository head and the moving version-
line alias are discovery or authoring inputs, not consumer constitutional
authority.

Release notes for immutable RC cuts live under `releases/`.

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

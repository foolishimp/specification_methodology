# specification_methodology

Authoring source repository for the shared specification methodology.

New to STDO? Read [Using STDO](plugins/spec/references/GETTING_STARTED.md) for
the daily human and LLM workflow. Use the [Project Quickstart](QUICKSTART.md)
when adding the toolchain and Product Definition to a project.

The [2.5.1 RC1 release](.ai-workspace/comments/codex/20260920T070629Z_stdo_251_rc1/RELEASED.md)
records the published matched cohort and its qualification limits. The exact
[release declaration](releases/v2.5.1.md) and installation examples identify
the available cut.
The [RC7 release work](.ai-workspace/comments/codex/20260915T093130Z_rc7_release/README.md)
and [2.5.0 declaration](releases/v2.5.0.md) preserve the published predecessor.
The source project's separately selected operative RC4 basis remains unchanged.

Mutable future-method source lives under `specification/standards/`. Publication
authority is one immutable released STDO RC cut identified by its annotated tag,
commit, tree, and exact member inventory. A consumer is governed by the complete
cut pinned in its Product Definition. The shared-source
`specification_methodology/v<version>` tag is only the mutable alias to the
highest-ordinal published RC on that line. Historical unqualified selectors
remain frozen history.

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

During development from a Specification Stack checkout, install the manager
itself with an isolated Python application installer:

```sh
pipx install --force ./specification_methodology/v2
```

When already inside the `specification_methodology/v2/` toolchain directory, use
`pipx install --force .`. The explicit replacement avoids leaving an older
manager in place when a qualified cut requires newer ref-resolution behavior.

To install a released manager, select its qualified immutable ref from the
[release records](releases/). The [cohort record](../../stack_release.json) locates
the selected release and its matching assets. Use that exact ref:

```sh
STDO_REF='<qualified-immutable-ref>'
pipx install --force \
  "git+https://github.com/foolishimp/specification_methodology.git@${STDO_REF}#subdirectory=specification_methodology"
```

Then install or inspect a cut:

```sh
STDO_CUT='<immutable-cut>'
stdo install "$STDO_CUT"
stdo list
stdo resolve "stdo://releases/${STDO_CUT}/standards/SPEC_METHOD.md"
```

The current toolchain, `0.1.5`, also supports a standalone V3 package at the
published `specification_methodology/v3/` root. See
[V3 installation](V3_INSTALLATION.md) for the package contract, exact-cut
commands, and consumer migration boundary. V3 candidate review and publication
remain separate from this installer capability.

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
stdo fleet verify --root /path/to/workspace
stdo fleet sync --root /path/to/workspace --all
stdo fleet adopt --root /path/to/workspace --all --dry-run
stdo fleet adopt --root /path/to/workspace --all \
  --accept-plan-sha256 <plan_sha256>
stdo fleet bootstrap --root /path/to/workspace --all
```

Bootstrap targets are portable paths relative to each definition's resolved
`product.source_project`. Fleet bootstrap first confirms that every source
project and target remains inside the authorized fleet root.

### Composition verification in the current source candidate

The composition-verification increment is available in this source checkout.
An already installed `stdo` may still be the earlier 0.1.5 implementation. Until
that manager is explicitly updated, run the candidate from the repository root
with a Python interpreter containing the manager's declared dependencies:

```sh
PYTHONPATH=specification_methodology/v2/src python3 -B -m stdo_toolchain.cli \
  fleet verify --root stdo_skills/stdo_skills.json --resolver-root .
```

The new result identifies `kind: stdo.composition-verification`,
`schema_version: 1`. Require this capability marker and `valid: true` when the
task needs composition resolution; an old manager's successful per-definition
report does not establish that result. This source instruction does not replace
or install the user's global manager.

`--root` selects either a definition or recursively discovered definitions.
Their declared composition closure is then checked, including each target's
own schema and installed method basis, exact target identity, relation fragment
and every contract reference. `--resolver-root` explicitly sets the local
filesystem acquisition boundary. Its default is the selected directory or the
selected definition's parent. For a single Product with sibling dependencies,
choose the containing boundary deliberately; this does not select unrelated
Products or grant operation authority. Boundaries and referenced paths must be
physical, with no symlink components; canonicalize an intentional system path
alias before selecting it.

Local relative/absolute and local `file:` paths must remain inside that
boundary. Exact `stdo://releases/` resources are a separate resolver capability
through the selected installed Store, whose release bytes are verified. No
missing release is installed and no network/custom-scheme URI is fetched.
Queries and unsupported fragment forms return explicit unsupported results.
Supported fragments are Markdown ATX headings using the shared Axiom Indexer
slug convention and explicit HTML anchors, JSON Pointers, and HTML IDs/anchor
names. Fenced examples are not headings or anchors. Directory contracts check
directory existence only. Markdown escaped markup and matching inline-code
spans, including multiline spans, do not supply explicit HTML anchors. Actual
HTML tags keep their attributes intact; the shared heading slug convention is
unchanged. This bounded fragment scanner is not a general Markdown renderer.
Each file observation includes its actual byte hash;
a commit label cannot substitute for changed working bytes.

Each edge retains its source/index, expected target identity, reference
observations and diagnostics. Shared targets are checked once; cycles terminate
without implying an executable work schedule. The bounded API permits at most
1,000 definitions, 10,000 edges and 8 MiB per acquired reference by default;
exceeding a limit fails verification. The result covers mechanical resolution.
Authority congruence, context sufficiency, compatibility and work admission
still require their owning contracts and evidence. `status --verify` and
`fleet status` retain their basis-status scope.

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

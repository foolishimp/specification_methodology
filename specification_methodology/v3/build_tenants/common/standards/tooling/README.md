# STDO 3.0.4 tools

This installation includes a pinned source snapshot of a_c's representation,
code-overlay and Lean tenants, plus the Codex and Claude Skills packages. The
[tool inventory](TOOLING.json) identifies every source file from repository cut
`9c9626ffd20ea88a75ac8143802c13f4f828ec1c`. These are separately owned Products
distributed with STDO; their existing contracts and methodology bases remain
in force. Distribution does not accept their semantic or actual-host claims.

Read the [offline documentation home](../documentation/index.html) immediately.
The constraints, ABI code example and Lean proof reader need no tool setup.

## Create a writable tool workspace

First resolve the immutable installed directory using the ordinary manager:

```sh
stdo resolve stdo://releases/v3.0.4/standards/tooling/materialize.py
```

Use the returned absolute `path`. Python 3.11 or later is required. Replace the
example paths below with that path and an absent directory under an existing
writable parent. Use canonical paths, without symbolic-link ancestors.

```sh
python3 -I -B /absolute/installed/standards/tooling/materialize.py check
python3 -I -B /absolute/installed/standards/tooling/materialize.py materialize --destination /absolute/work/stdo-tools
python3 -I -B /absolute/installed/standards/tooling/materialize.py verify-tree --destination /absolute/work/stdo-tools
```

The last command checks the pristine source copy. Later toolchains, caches or
local edits intentionally make that exact-tree check fail. Keep the installed
copy immutable and select a new workspace to reproduce it. Materialization
does not install Python dependencies, tools, Skills or methodology globally.

## Build a project's representation

The ordinary direct path uses the Python standard library and an explicitly
selected installed `stdo` manager. The current coding session authors the
representation through `task` and `submit`; a model is not inferred just by
running `prepare`. From any current directory:

```sh
python3 -B /absolute/work/stdo-tools/a_c/build_tenants/graphify/code/ac_project.py --help
python3 -B /absolute/work/stdo-tools/a_c/build_tenants/graphify/code/ac_project.py prepare --help
python3 -B /absolute/work/stdo-tools/a_c/build_tenants/graphify/code/ac_code.py --help
python3 -I -S -B /absolute/work/stdo-tools/a_c/build_tenants/lean/scripts/formal_gate.py --help
```

In the extracted tree read `a_c/build_tenants/graphify/design/project-build.md`
for the complete `prepare → task → submit → build → status` contract. The
Graphify tenant README covers exact source manifests, native model/carrier,
closure, projection, grounded views and the optional code overlay. Select the
project's existing Product Definition, installed methodology and source paths;
this package supplies neither a work grant nor cross-Product source authority.

## Optional Graphify and code extraction

Use a separately selected clean Git checkout of
`https://github.com/Graphify-Labs/graphify.git` at
`fe085cedddde3a18554f8749b230bfe47f3dcce7`. The tools verify that checkout;
a source ZIP is not a substitute for its Git custody. No dependency is acquired
implicitly. In a workspace-local Python virtual environment:

```sh
python3 -m venv /absolute/work/stdo-python
/absolute/work/stdo-python/bin/python -m pip install networkx==3.4.2
/absolute/work/stdo-python/bin/python -m pip install -r /absolute/work/stdo-tools/a_c/build_tenants/graphify/code/code-requirements.txt
/absolute/work/stdo-python/bin/python -m pip install -r /absolute/work/stdo-tools/a_c/build_tenants/graphify/code/generation/requirements.txt
```

The code parser pins are tree-sitter 0.25.2, Python/JavaScript grammars 0.25.0
and TypeScript grammar 0.23.2. The generation requirements supply the additional
Graphify build dependencies. Select `--upstream` explicitly. Code extraction
reads only selected source/test bytes; imports and configuration outside that
selection remain unavailable. Caller-authored trace links are proposals, not
proof that code satisfies a requirement or that a test executed.

## Lean checking and proof evidence

The offline proof reader shows exact retained proof sources and a historical
report. Fresh checks use the extracted `a_c/build_tenants/lean` tree. Its
`README.md`, `design/FORMAL_GATE.md`, `toolchain-lock.json` and
`profiles/proof-support-v1.json` define the execution contract. Lean is pinned
to 4.35.0 and Mathlib to `56a005855ea17e0b0958f73ec801ae140b0a1679`.
`scripts/bootstrap.py --help` describes explicit dependency acquisition into
that writable tree. Do not run bootstrap or checks beneath the installed
release. Exact compiled proof support is not included: the prior 3.25 GB
Darwin-arm64 support qualification does not establish fresh-machine execution
on another host. A missing or unfinished support check supplies no proof verdict.

Structural closure/projection results preserve their declared model and
signature scope. They do not establish fidelity to source prose, code-overlay
semantics, authority, admission or whole-method correctness.

## Skills and source scope

The extracted `stdo_skills/build_tenants/codex/README.md` and
`stdo_skills/build_tenants/claude/INSTALL.md` describe explicit workspace-local
installation. Both packages and their provider contract pins are included;
the running coding host and nominated project's selected methodology remain
external. Their original static construction basis is STDO 3.0.1 RC1, not an
automatic adoption of the distributing 3.0.4 release. The provider was built
under 2.5.1 RC2. This distribution does not migrate either basis.

The archive preserves source tests and design records as reference material.
Some historical links and tests require unshipped work evidence or host/tool
installations; no complete source test-suite claim is made. The Codex
`tests/verify_package.py` and Claude `tests/check_package.py` package checks
are runnable from this preserved layout. The sole `.ai-workspace` member is the public current
`stdo_skills/.ai-workspace/tickets/active/T-003-project-representation.md`,
required by the Codex package's selected source-route pin. It is a documentary
dependency, not an executable or authority grant. All other work records,
private support origins, caches, virtual environments and runtime binaries
are excluded. Source contracts do not gain authority from their filenames.

The archive retains the STDO distribution's Apache-2.0 license at
`specification_methodology/v3/build_tenants/common/LICENSE`, and the bundled
renderer license/notices under the Graphify tenant's `code/viewer/vendor/`.
Separately acquired Graphify, Python packages, Lean and Mathlib retain their
own licenses. This inventory does not relicense separately owned material.

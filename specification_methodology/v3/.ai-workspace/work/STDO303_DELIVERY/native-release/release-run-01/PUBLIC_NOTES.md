# STDO 3.0.3

STDO 3.0.3 is a normal, immutable `stable-v1` release. It bundles the project
representation tools and offline documentation with the methodology.

The installed documentation home now provides:

- **Constraints:** the historical STDO representation, with unified 3D, 2D and
  layered views and file-to-logical navigation.
- **Code example:** the reviewed ABIogenesis example, connecting selected
  requirements, code observations, proposed traces and test sources.
- **Lean proofs:** searchable declarations, exact proof source, readable
  explanations and the retained check report, with source-reference navigation.
- **Tools:** the pinned a_c and Codex/Claude Skills source bundle, with an
  integrity checker and explicit extraction into a separate writable workspace.

These readers are self-contained HTML pages; opening the installed pages needs
no web service or toolchain setup.

## Install and open the documentation

With STDO manager 0.1.6 already available:

```sh
stdo install v3.0.3 --repository https://github.com/foolishimp/specification_methodology.git --manifest-sha256 f07e6681355023e30ad8cc4c2ebecaa520ee4e75da6e140ef5a160b31082178d
stdo verify v3.0.3 --manifest-sha256 f07e6681355023e30ad8cc4c2ebecaa520ee4e75da6e140ef5a160b31082178d
stdo resolve stdo://releases/v3.0.3/standards/documentation/index.html
```

Open the absolute `path` returned by the last command in your browser. To
prepare a workspace-local manager with Python 3.11 or later, download the
[manager wheel](https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology/v3.0.3/stdo_toolchain-0.1.6-py3-none-any.whl)
and its checksum from this release, then run:

```sh
python3 -m venv .stdo-manager
.stdo-manager/bin/python -m pip install ./stdo_toolchain-0.1.6-py3-none-any.whl
.stdo-manager/bin/stdo --store ./.stdo-store install v3.0.3 --repository https://github.com/foolishimp/specification_methodology.git --manifest-sha256 f07e6681355023e30ad8cc4c2ebecaa520ee4e75da6e140ef5a160b31082178d
.stdo-manager/bin/stdo --store ./.stdo-store resolve stdo://releases/v3.0.3/standards/documentation/index.html
```

The [installed-tooling guide at the immutable native commit](https://github.com/foolishimp/specification_methodology/blob/07bdb34a2d472a3b5e678f60584fd02b24a388f4/specification_methodology/v3/standards/tooling/README.md)
explains checked extraction, representation/code commands, optional Graphify
dependencies, Lean support and Skills installation. Extraction preserves the
installed release; it does not install dependencies or adopt a methodology
for an existing project.

## Exact release and scope

- Native commit: `07bdb34a2d472a3b5e678f60584fd02b24a388f4`.
- Annotated tag: `specification_methodology/v3.0.3`.
- Manifest SHA-256: `f07e6681355023e30ad8cc4c2ebecaa520ee4e75da6e140ef5a160b31082178d`.
- Native payload: 106 files; installation adds the manifest as its 107th file.
- Tool source bundle: 191 exact files from `9c9626ffd20ea88a75ac8143802c13f4f828ec1c`.

The four downloadable assets are the canonical manifest, manager wheel and
their checksum sidecars. Documentation and tool sources are inside the native
installation; no separate representation supplement is required.

The tools are distributed as source. Optional Python/parser/Graphify support,
Lean/Mathlib and compiled proof support require explicit setup in a writable
workspace. The proof reader retains an exact historical check—46 projection
outputs, 46 budget refusals and 204 audited declaration contracts—not a fresh
proof run or proof of application-code correctness. The code example's trace
links are proposals; test sources do not imply executed test results.

Independent review and installed-path checks cover the bounded distribution
and tooling behavior. Browser/WebGL visual qualification, fresh-machine Lean
execution, new coding-host Skills trials, semantic completeness and practical
efficiency retain their recorded limits. Existing a_c/Skills construction
bases and consumer installations are unchanged by this release.

# STDO 3.0.4 builder and tools

This versioned binding implements the owner's [adoption instruction](../.ai-workspace/work/STDO304_BUILDER_ADOPTION/INTAKE.json)
for `urn:stdo:product-definition:stdo-3`. [stdo_3.json](../stdo_3.json) remains
the sole current method selection. This guide binds launch paths and source
provenance; it adds no method law or work grant.

See [Products and components in an STDO release](../../../RELEASE_PRODUCTS.md)
for the single release-composition table, ownership and currentness gaps.
The historical representation and older source bundles are not automatically
current 3.0.4 implementations.

## Exact binding

- Basis: `stdo://releases/v3.0.4/`.
- Manifest: `stdo://releases/v3.0.4/manifest.json`, SHA-256
  `102817a3f4bea4dca1d6fa0fc634b94404dd2ba82ba6d8c38b273402dda9f95b`.
- Native commit: `16bc30d215915a4b7b3ed2f13e52e14510ae1c9d`;
  tag: `specification_methodology/v3.0.4`.
- Native plugin: `stdo://releases/v3.0.4/plugins/spec/`, exactly the
  **21 members** inventoried by that manifest's `auxiliary.plugin` object.
- Tool archive: **191 sources** from original snapshot
  `9c9626ffd20ea88a75ac8143802c13f4f828ec1c`, as inventoried by `TOOLING.json`.
- Writable source destination, relative to this Product root:
  `.stdo/tools/3.0.4/`; ignored by the repository's existing `.stdo/` rule.

Every path in this table is relative to the immutable basis URI above; its
logical URI is that basis followed by the path. The manifest pins the complete
native package, including references and scripts; these are direct entry pins.

| Released member path | SHA-256 |
|---|---|
| `plugins/spec/.codex-plugin/plugin.json` | `fad5097996c8d0f3835c75966348e3c05b0b9bdbb484252f1b364089f1376f4d` |
| `plugins/spec/skills/stdo-work/SKILL.md` | `9dc06e03fd6f64483fa485ed55f35e414fefae472bb69aa930ecef9335585b35` |
| `plugins/spec/skills/stdo-review/SKILL.md` | `b90b3a2014d7891e25b40c11e5f3638accb9f3408cb3f0cf3922d26f17bc57df` |
| `plugins/spec/skills/stdo-ticket/SKILL.md` | `c37e615dbf280ef5a134f604932f5e709c5012968d73ae9362eb47dbab65719b` |
| `plugins/spec/skills/stdo-status/SKILL.md` | `23122f6bf8e78d6167fc0e45d24f17421459172ddc41e8ccb6b35a4873b29407` |
| `plugins/spec/skills/stdo-help/SKILL.md` | `8a488add6bbba99dae6173adfcef4f949df264624620f52adb15e20b5144f931` |
| `plugins/spec/scripts/read_basis.py` | `df7730a1f661a8be7a3144feff474f83197987ebfd1cce4063aa9c5504e75c41` |
| `standards/tooling/TOOLING.json` | `53a2453422c5c385755d5f230d495c836120dbbf0fc07ba8969bf84d450c1352` |
| `standards/tooling/sources.zip` | `172eeb57040004365671372294e5c2a42833a0f574224fb66c57cf5a30c5d4e0` |
| `standards/tooling/materialize.py` | `1a4068b5ff9568f1a7a964534e18bbff06398db2184bb59b9ede3f77f3ff4d8d` |

## Enter future work

From `specification_methodology/v3/`, use the existing installed manager. Continue
only when the definition and helper report the exact basis and manifest above,
with `installed: true`, `valid: true` and no failures:

```sh
set -eu
STDO_MANAGER="$(command -v stdo)"
"$STDO_MANAGER" status --definition stdo_3.json --verify
STDO_RELEASE="$("$STDO_MANAGER" resolve stdo://releases/v3.0.4/manifest.json |
  python3 -c 'import json,pathlib,sys; print(pathlib.Path(json.load(sys.stdin)["path"]).parent)')"
python3 -I -B "$STDO_RELEASE/plugins/spec/scripts/read_basis.py" check \
  --stdo "$STDO_MANAGER" --definition stdo_3.json
python3 -I -B "$STDO_RELEASE/plugins/spec/scripts/read_basis.py" read \
  --stdo "$STDO_MANAGER" --definition stdo_3.json \
  --member standards/PRODUCT_DEFINITION.md \
  --heading '4. Shared installed release basis and toolchain manager'
```

The definition's declared bootstrap is
`stdo://releases/v3.0.4/standards/frames/bootstrap.md`. Verify it and its deciding
source digests through the release's `FRAME_INPUTS.json` before relying on its
projection; enter exact owning sections when a question needs them. The compact
reader verifies the selected definition and named source member and emits only
the requested section. It owns no admission or dispatch.

For an admitted work task, explicitly read
`$STDO_RELEASE/plugins/spec/skills/stdo-work/SKILL.md` and follow it.
For assessment, tickets, status or help, select the corresponding pinned
`stdo-review`, `stdo-ticket`, `stdo-status` or `stdo-help` skill. Read shared
references relative to that installed package, including `PRODUCT_BASIS.md`,
`COORDINATED_HANDOFF.md` and `HOST_BINDING.md` where applicable. This direct
file-loading route is documented by the installed
`plugins/spec/references/GETTING_STARTED.md`; it needs no host-global plugin
registration. An actor's skill name alone does not identify its loaded bytes.
The installed skill and its relative package are the workflow authority route.

## Materialize and use the released sources

Python 3.11 or later is required by the materializer. Resolve and verify the
release as above, then run this block from the Product root. It sets the
destination before choosing the fresh or existing-tree path:

```sh
set -eu
STDO_TOOLS="$(pwd -P)/.stdo/tools/3.0.4"
python3 -I -B "$STDO_RELEASE/standards/tooling/materialize.py" check
if [ -e "$STDO_TOOLS" ] || [ -L "$STDO_TOOLS" ]; then
  python3 -I -B "$STDO_RELEASE/standards/tooling/materialize.py" verify-tree \
    --destination "$STDO_TOOLS"
else
  mkdir -p .stdo/tools
  python3 -I -B "$STDO_RELEASE/standards/tooling/materialize.py" materialize \
    --destination "$STDO_TOOLS"
  python3 -I -B "$STDO_RELEASE/standards/tooling/materialize.py" verify-tree \
    --destination "$STDO_TOOLS"
fi
```

An existing destination, including a dangling symlink, is sent to verification.
The released tool refuses a malformed or modified tree; this block never
repairs, replaces or overwrites one.

Use source entrypoints from this materialized archive:

```sh
python3 -B "$STDO_TOOLS/a_c/build_tenants/graphify/code/ac_project.py" --help
python3 -B "$STDO_TOOLS/a_c/build_tenants/graphify/code/ac_graph.py" --help
python3 -B "$STDO_TOOLS/a_c/build_tenants/graphify/code/ac_code.py" --help
python3 -I -S -B "$STDO_TOOLS/a_c/build_tenants/lean/scripts/formal_gate.py" --help
```

Read the installed `standards/tooling/README.md` and the materialized
`a_c/build_tenants/graphify/design/project-build.md` or Lean
`design/FORMAL_GATE.md` for the selected operation. Pass the target Product's
exact definition and basis. Source availability and CLI help are not a build,
semantic assessment, proof verdict or actual-host qualification. Optional
Graphify, Python and Lean/Mathlib dependencies require their documented,
explicit setup when a selected task needs them. This adoption installs none.

The archive's independent `stdo_skills` packages retain their original static
3.0.1 construction provenance; a_c retains its own contracts and basis. They
are source material, not the adopted native 3.0.4 workflow. Existing C3
concrete-operation evidence remains on 2.5.1-rc.2; reuse needs the relevant
successor classification and applicability. No blanket FD compatibility is
claimed. Keep generated work and toolchain caches outside the pristine source
tree when exact `verify-tree` reproducibility is needed; later additions or
edits deliberately fail that check.

The [adoption record](../.ai-workspace/work/STDO304_BUILDER_ADOPTION/README.md)
retains the exact manager plan, checks, local paths and review boundary.

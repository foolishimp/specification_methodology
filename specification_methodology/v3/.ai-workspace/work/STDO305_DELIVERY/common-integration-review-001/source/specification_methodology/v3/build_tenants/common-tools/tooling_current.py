"""Package explicitly selected current Product members, with portable setup."""
from __future__ import annotations

import io
import json
import ast
from pathlib import Path
import tomllib
import zipfile

import current_assets as a
import tooling_materialize as materializer

HERE = Path(__file__).resolve().parent
REQUIRED = {
    "a_c": {"VERSION", "scripts/ac.py", "scripts/bootstrap.py", "build_tenants/graphify/code/ac_upstream.py",
            "build_tenants/graphify/code/ac_fs_boundary.py", "build_tenants/graphify/code/ac_support.py",
            "build_tenants/lean/scripts/formal_gate.py", "build_tenants/lean/lakefile.toml"},
    "stdo_skills": {"VERSION", "scripts/manage_skills.py", "release/3.0.5/manifest.json"},
    "axiom_indexer": {"VERSION", "build_tenants/core/code/ac.py", "build_tenants/core/code/ac_model.py"},
    "stdo_representation": {"VERSION", "build_tenants/a_c/representation/stdo-v3.0.5/model.json",
                            "build_tenants/a_c/representation/stdo-v3.0.5/source-freeze.json"},
}


def guide(version):
    return f"""# STDO {version} installed tools

The native release contains the current a_c implementation, Representation,
Axiom Indexer and Codex/Claude Skills packages with exact file inventories.
Read [the current model and proof](../documentation/index.html) offline.

Create a writable copy outside the immutable installed release:

```sh
python3 materialize.py check
python3 materialize.py materialize --destination /absolute/new/tools
```

The destination must be absent. Run these commands from this tooling directory,
or give the scripts' absolute paths. The copy preserves root-relative Product
paths. Its archive and [selection](SELECTION.json) identify every member.

From the copy, `python3 a_c/scripts/ac.py --help` lists public operations.
Use `python3 a_c/scripts/bootstrap.py --help` for the controlled Graphify and
Lean setup commands. They create private runtimes, retain exact dependencies
and actual setup receipts. Lean support establishment is an executed operation;
its new runtime identity needs its own current-model verification. The installed
proof reader retains the construction result and does not execute Lean.

To install a host binding, run this installed `setup.py host --help`. Supply the
verified method root, explicit store, manager and Python, materialized tools,
host workspace and an absent anchor directory. The helper checks the selected
native manifest, creates a separately scoped runtime-installation anchor, and
invokes the selected Skills installer. Choose `codex` or `claude`; install each
host explicitly. The host core workflows load the same native owner. The
`stdo-project` extension provides model, code and formal operation routes.
Nominated project Product Definitions keep their construction basis.

For Lean support setup, first use `setup.py derive-runtime --help` to copy the
selected a_c source into an explicit writable runtime, retaining the exact
initial mapping. Then use `setup.py bootstrap-lean --help` with that receipt
and its SHA256. It invokes the existing public Lean bootstrap and records the
only allowed source change: the freshly established proof-support profile.
Pass this runtime and its resulting derivation receipt to host setup. The
original materialized Product source remains unchanged. Any other source
delta or unsupported profile provenance refuses setup; the current model
still requires actual verification against the new runtime identity.

Follow the [portable verification recipe](../documentation/README.md) after
setup: materialize the retained proof, generate a current request using its
extracted model and views, then invoke the selected runtime's formal `verify`
command. Original construction paths remain provenance only.

The [five-Product release manifest](https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology%2Fv{version}/stack-release-v{version}.json)
is the external binding of these components and the native installation.
Materialization establishes source custody. Actual installed qualification,
semantic review, and publication have separately recorded evidence.
""".encode()


def check_files(files):
    meta, sources = materializer.source_bytes(files)
    a.require(meta["kind"] == "stdo.installed-tooling/2", "current tooling profile required")
    selected = json.loads(files["SELECTION.json"])
    freeze = a.source_freeze(a.encoded(selected["source_freeze"]), meta["distribution_version"])
    a.require(freeze["source_identity_sha256"] == meta["source_identity_sha256"], "tooling semantic source differs")
    for owner, required in REQUIRED.items():
        a.require({owner + "/" + name for name in required} <= sources.keys(), "required Product entrypoint missing: " + owner)
        a.require(sources[owner + "/VERSION"].decode().strip() == meta["distribution_version"], "Product VERSION differs")
    lean = tomllib.loads(sources['a_c/build_tenants/lean/lakefile.toml'].decode())
    a.require(lean.get('name') == 'ac_lean' and lean.get('version') == meta['distribution_version'], 'owned Lean package version differs')
    source = ast.parse(sources['a_c/build_tenants/graphify/code/ac_support.py'].decode())
    declared = [ast.literal_eval(node.value) for node in source.body if isinstance(node, ast.Assign)
                and any(isinstance(t, ast.Name) and t.id == 'SERVER_VERSION' for t in node.targets)]
    a.require(declared == [meta['distribution_version']], 'owned MCP server version differs')
    a.require(files["materialize.py"] == (HERE / "tooling_materialize.py").read_bytes(), "current materializer differs")
    a.require(files["setup.py"] == (HERE / "tooling_setup.py").read_bytes(), "current setup differs")
    a.require(files["runtime.py"] == (HERE / "tooling_runtime.py").read_bytes(), "current runtime derivation implementation differs")
    a.require(files["README.md"] == guide(meta["distribution_version"]), "current tooling guide differs")
    return {"kind": meta["kind"], "status": "checked", "version": meta["distribution_version"],
            "source_identity_sha256": meta["source_identity_sha256"], "source_files": len(sources),
            "source_inventory_sha256": meta["source_inventory_sha256"], "archive_sha256": a.sha(files["sources.zip"])}


def build(repository, destination, selection_path, selection_sha):
    repository, destination = a.ordinary(repository), a.ordinary(destination)
    selected = a.selection(repository, selection_path, selection_sha, "stdo.current-tooling-selection/1")
    for owner in selected["owners"]:
        a.disjoint(destination, repository / a.name(owner))
    archive = io.BytesIO(); rows = []
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipped:
        for owner, unit in sorted(selected["owners"].items()):
            for row in unit["members"]:
                raw = a.pinned(repository, row)
                path = a.name(row["path"])
                a.require(path.startswith(owner + "/"), "member crosses selected Product boundary")
                a.require(row["git_mode"] in ("100644", "100755"), "regular source mode required")
                entry = zipfile.ZipInfo(path, (1980, 1, 1, 0, 0, 0))
                entry.create_system = 3; entry.external_attr = int(row["git_mode"], 8) << 16
                zipped.writestr(entry, raw, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
                rows.append({"archive_path": path, "bytes": len(raw), "sha256": a.sha(raw), "git_mode": row["git_mode"]})
    rows.sort(key=lambda row: row["archive_path"])
    files = {"sources.zip": archive.getvalue(), "materialize.py": (HERE / "tooling_materialize.py").read_bytes(),
             "setup.py": (HERE / "tooling_setup.py").read_bytes(), "README.md": guide(selected["version"]),
             "runtime.py": (HERE / "tooling_runtime.py").read_bytes(),
             "SELECTION.json": a.regular(selection_path)}
    meta = {"kind": "stdo.installed-tooling/2", "distribution_version": selected["version"],
            "source_identity_sha256": selected["source_identity_sha256"], "selection_sha256": selection_sha,
            "sources": rows, "source_inventory_sha256": a.sha(materializer.encoded(rows)),
            "distribution_members": {p: {"bytes": len(raw), "sha256": a.sha(raw)} for p, raw in sorted(files.items())}}
    files["TOOLING.json"] = a.encoded(meta)
    result = check_files(files)
    a.write_tree(destination, files)
    return dict(result, status="bundled", destination=str(destination))

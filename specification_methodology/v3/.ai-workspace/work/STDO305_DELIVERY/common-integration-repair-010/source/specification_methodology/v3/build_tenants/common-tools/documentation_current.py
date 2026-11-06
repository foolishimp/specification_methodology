"""Assemble current source/model/view/proof documentation without a self-hash cycle."""
from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

import current_assets as a
import proof_reader_current as proofs


def guide(version):
    return f"""# STDO {version} documentation

Open the [documentation home](index.html), the
[current constraint explorer](constraint-explorer/index.html), or the
[current Lean proof reader](proofs/index.html). These readers work offline.

```sh
stdo resolve stdo://releases/v{version}/standards/documentation/index.html
```

Open the returned path in a browser. Choose **3D**, **2D** or **Layered** to
view the same model, selection and reading trail. Search by statement, select
a record to read its full content and caveats, then follow labelled relations.
Use **Files**, **Show in files** and **Back to file** to follow embedded source
passages. Layered and text work without WebGL. No service or tool installation
is needed to read these files.

The explorer embeds the complete selected semantic source: standards plus
native workflow contracts. Its model and source inventory are exact inputs,
bound in [DOCUMENTATION.json](DOCUMENTATION.json). Generated frames and these
documentation files are derived routes rather than additional semantic owners.
Use the [owning installed standards](../README.md) and
[Getting Started](../../plugins/spec/references/GETTING_STARTED.md) for method
decisions. A graph edge does not by itself prove an implication.

The proof reader exposes actual verification of this exact finite model and
its selected views, generated proof source, compiled artifacts, theorem axiom
audit, runtime identities, logs and explicit limits. Its reusable library
retains its original provenance. The source-prose-to-model assessment is
separate from Lean's structural model/projection result. Checking the reader
verifies retained bytes and bindings; it does not execute a new Lean proof.

[Use the installed tools](../tooling/README.md) to materialize the four peer
Product packages and set up Graphify, Lean and host bindings in writable
locations. The native workflow stays intact inside its installed package.

After the declared Lean setup, run the following with new writable output
locations. Use the selected runtime's Python and formal owner executable:

```sh
python3 proofs/materialize.py materialize --destination /absolute/new/evidence
python3 proofs/materialize.py request --evidence /absolute/new/evidence --output /absolute/current-request.json
/absolute/runtime-python -I -S -B /absolute/runtime-a_c/build_tenants/lean/scripts/formal_gate.py verify --request /absolute/current-request.json --output /absolute/new/verification
```

The request command verifies the extracted bytes and substitutes only local
model/view paths. The original request, including construction paths, remains
unchanged in the evidence. A new verification produces its own result and
runtime identity; the retained construction verdict does not become an
installed verdict. Output directories and the request must not already exist.

The [five-Product release manifest](https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology%2Fv{version}/stack-release-v{version}.json)
is the separately published binding of semantic source, current model, native
installation, component inventories and qualification evidence. It is external
to this payload so the release does not contain its own unknown digest.
""".encode()


def landing(version):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" href="data:,"><title>STDO {version} documentation</title><style>
body{{background:#101820;color:#e8eef0;font:17px/1.7 system-ui;margin:0}}main{{max-width:1000px;margin:5vh auto;padding:30px}}a{{color:#acdbbd}}h1{{font-size:38px;line-height:1.2}}.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px}}article{{border:1px solid #455862;padding:22px;border-radius:9px}}.scope{{color:#b5c8d0;font-size:14px}}footer{{margin-top:28px}}</style></head><body><main>
<p>STDO {version} · INSTALLED DOCUMENTATION</p><h1>Follow the current method into source and proof.</h1><p>Explore one source-matched model through 3D, 2D, Layered and Files views. Read its exact structural proof and retained results.</p><div class="cards">
<article><h2><a href="constraint-explorer/index.html">Current constraints →</a></h2><p>Search complete statements, follow labelled relationships and open their embedded source passages.</p><p class="scope">The selected semantic standards and native workflow contracts share one exact source inventory.</p></article>
<article><h2><a href="proofs/index.html">Current model proofs →</a></h2><p>Inspect selected views, generated Lean source, theorem axioms, kernel and runtime results.</p><p class="scope">Finite model and projection results retain their premises. Prose fidelity and semantic acceptance are assessed separately.</p></article>
<article><h2><a href="../tooling/README.md">Use the tools →</a></h2><p>Set up the exact a_c, Representation, Axiom Indexer and Codex/Claude Skills packages.</p><p class="scope">Materialize writable tools and select their controlled Graphify and Lean dependencies.</p></article></div>
<footer><a href="README.md">Reading guide</a> · <a href="../README.md">Owning standards</a> · <a href="../../plugins/spec/references/GETTING_STARTED.md">Getting Started</a> · <a href="DOCUMENTATION.json">Exact inventory</a><p class="scope">Readers work offline. Layered and text remain available without WebGL. Use browser Back or open readers in separate tabs.</p></footer></main></body></html>""".encode()


def viewer_data(raw):
    match = re.search(rb'<script id="explorer-data" type="application/json">(.*?)</script>', raw, re.S)
    a.require(match is not None, "current viewer data missing")
    value = json.loads(match[1])
    a.require(value.get("profile") == "a_c.constraint-explorer/1", "current unified viewer profile differs")
    return value


def validate_inputs(files):
    selected = json.loads(files["SELECTION.json"])
    a.require(selected.get("kind") == "stdo.current-documentation-selection/1", "current documentation selection required")
    version = a.version(selected["version"])
    for key, name in (("source_freeze", "source-freeze.json"), ("model", "model.json"),
                      ("source_manifest", "source-manifest.json"), ("viewer", "constraint-explorer/index.html")):
        a.require(a.sha(files[name]) == selected[key]["sha256"], "selected documentation input differs: " + key)
    freeze = a.source_freeze(files["source-freeze.json"], version)
    model = json.loads(files["model.json"]); identity = a.model_identity(files["model.json"])
    rows = a.source_model(freeze, model, json.loads(files["source-manifest.json"]), selected["source_copy_prefix"])
    data = viewer_data(files["constraint-explorer/index.html"])
    a.require(data["model"] == identity and data["basis"] == model["basis"] and data["interpretation"] == model["interpretation"], "viewer/model identity differs")
    a.require(set(data["sources"]) == {r["path"] for r in rows}, "viewer semantic source population differs")
    for row in rows:
        source = data["sources"][row["path"]]; raw = source["text"].encode()
        a.require(a.sha(raw) == row["sha256"] == source["sha256"] and len(raw) == row["bytes"], "viewer source bytes differ")
    result = proofs.check_files({p[len("proofs/"):]: raw for p, raw in files.items() if p.startswith("proofs/")})
    a.require(result["version"] == version and result["source_identity_sha256"] == freeze["source_identity_sha256"] and result["model"] == identity,
              "proof reader does not qualify the selected current model")
    a.require(a.sha(files["proofs/PROOFS.json"]) == selected["proof_catalog"]["sha256"], "selected current proof catalog differs")
    return selected, freeze, identity


def metadata(files):
    selected, freeze, identity = validate_inputs(files)
    return {"kind": "stdo.installed-documentation/2", "distribution_version": selected["version"],
            "role": "non-normative-documentation", "entrypoint": "index.html",
            "selection_sha256": a.sha(files["SELECTION.json"]),
            "source": {"source_identity_sha256": freeze["source_identity_sha256"], "source_freeze_sha256": a.sha(files["source-freeze.json"])},
            "model": identity, "viewer_sha256": a.sha(files["constraint-explorer/index.html"]),
            "proof_catalog_sha256": a.sha(files["proofs/PROOFS.json"]),
            "members": a.inventory({p: raw for p, raw in files.items() if p != "DOCUMENTATION.json"})}


def check_files(files):
    expected = metadata(files)
    version = expected["distribution_version"]
    a.require(files["DOCUMENTATION.json"] == a.encoded(expected), "current documentation metadata differs")
    a.require(files["README.md"] == guide(version) and files["index.html"] == landing(version), "current documentation navigation differs")
    fixed = {"DOCUMENTATION.json", "SELECTION.json", "source-freeze.json", "model.json", "source-manifest.json", "constraint-explorer/index.html", "README.md", "index.html"}
    a.require({p for p in files if not p.startswith("proofs/")} == fixed, "current documentation member closure differs")
    return {"kind": expected["kind"], "status": "checked", "version": version,
            "source_identity_sha256": expected["source"]["source_identity_sha256"], "model": expected["model"], "members": len(files)}


def build(repository, selection_path, selection_sha, output):
    root = a.ordinary(repository)
    selected = a.selection(root, selection_path, selection_sha, "stdo.current-documentation-selection/1")
    files = {"SELECTION.json": a.regular(selection_path), "source-freeze.json": a.pinned(root, selected["source_freeze"]),
             "model.json": a.pinned(root, selected["model"]), "source-manifest.json": a.pinned(root, selected["source_manifest"]),
             "constraint-explorer/index.html": a.pinned(root, selected["viewer"]),
             "README.md": guide(selected["version"]), "index.html": landing(selected["version"])}
    proof_catalog = root / a.name(selected["proof_catalog"]["path"])
    a.pinned(root, selected["proof_catalog"])
    a.disjoint(output, proof_catalog.parent)
    a.disjoint(output, root / a.name(selected["source_project"]))
    a.disjoint(output, root / "a_c")
    files.update({"proofs/" + p: raw for p, raw in a.read_tree(proof_catalog.parent).items()})
    # Reproduce the imported view through its current owner and exact renderer inputs.
    producer = root / a.name(selected["viewer_producer"]["path"])
    a.pinned(root, selected["viewer_producer"])
    a.require(producer == root / "a_c/build_tenants/graphify/code/ac_explore.py", "current viewer owner differs")
    for ref in selected["viewer_machinery"]:
        a.pinned(root, ref)
    data = viewer_data(files["constraint-explorer/index.html"])
    with tempfile.TemporaryDirectory(prefix="stdo-current-view-") as temporary:
        generated = Path(temporary).resolve() / "view.html"
        command = [sys.executable, "-B", str(producer), str(root / selected["model"]["path"]),
                   "--source-root", str(root / a.name(selected["source_project"])), "--out", str(generated),
                   "--layout", "unified", "--title", data["title"], "--focus", data["focus"]]
        run = subprocess.run(command, capture_output=True, timeout=180)
        a.require(run.returncode == 0 and a.regular(generated) == files["constraint-explorer/index.html"], "current viewer reproduction differs")
    value = metadata(files); files["DOCUMENTATION.json"] = a.encoded(value)
    result = check_files(files)
    a.write_tree(output, files)
    return dict(result, status="bundled", destination=str(output))

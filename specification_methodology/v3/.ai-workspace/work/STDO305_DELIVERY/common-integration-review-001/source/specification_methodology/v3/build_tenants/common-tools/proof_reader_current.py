"""Current exact-model proof documentation; retained evidence is not a new proof run."""
from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import tempfile

import current_assets as a
import proof_reader as lexical
import proof_evidence as transport

CLAIMS = ["imported-model-well-formedness", "whole-model-source-correspondence", "declared-closure-and-projection",
          "record-budget-result", "supplied-graphify-view-correspondence"]
CHECKS = {"complete-member-integrity", "current-runtime-and-support", "exact-current-request-inputs",
          "known-required-obligations", "regenerated-proof-sources", "complete-theorem-axiom-audit",
          "cold-stage-consistency", "current-runtime-output-correspondence", "supplied-view-correspondence"}
MODULES = ["GateData", "GateLocalNames", "GateExternalNames", "GateIdentities", "GateBounds", "GateModel", "GateViews", "GateRun"]
LIBRARY = {"AC/Closure.lean", "AC/GateProof.lean", "AC/GateRuntime.lean", "AC/Model.lean", "AC/Projection.lean", "AC/Structure.lean"}
TITLES = {"imported-model-well-formedness": "Is the supplied finite model well formed?",
          "whole-model-source-correspondence": "Does the imported model preserve this exact model JSON?",
          "declared-closure-and-projection": "Do these selections retain their declared closure?",
          "record-budget-result": "Does each declared budget return the prescribed result?",
          "supplied-graphify-view-correspondence": "Do the supplied views match these projections?"}


def validate_evidence(files):
    archive_raw, archive, recovered = transport.join(files["transport/TRANSPORT.json"], lambda name: files["transport/" + name], visible=True)
    a.require({p[len("transport/"):] for p in files if p.startswith("transport/")} == {'TRANSPORT.json'} | {r['path'] for r in archive['parts']},
              "proof transport part closure differs")
    visible = {n: raw for n, raw in recovered.items() if n.endswith((".lean", ".log")) or n in
               ("manifest.json", "result.json", "request.json", "replay-request.json", "supplied-views.json", "view-comparison.json")}
    a.require({p[len("evidence/"):] for p in files if p.startswith("evidence/")} == set(visible), "visible proof member closure differs")
    for name, raw in visible.items():
        a.require(files["evidence/" + name] == raw, "visible evidence differs from exact archive: " + name)
    recovered = {"evidence/" + n: raw for n, raw in recovered.items()}
    result = json.loads(recovered["evidence/result.json"])
    manifest = json.loads(recovered["evidence/manifest.json"])
    request = json.loads(files["selected-request.json"])
    inspection = json.loads(files["inspection.json"])
    a.require(manifest.get("schema") == "a_c.formal-gate.bundle/1" and
              result.get("schema") == "a_c.formal-gate.result/1" and result.get("status") == "verified", "successful current formal result required")
    members = manifest["members"]
    a.require(result["evidence"] == {"manifest_sha256": a.sha(files["evidence/manifest.json"]), "members": members}, "formal result/manifest differs")
    a.require(result["checked_claims"] == result["requested_claims"] == CLAIMS, "current required proof obligations differ")
    a.require(inspection.get("schema") == "a_c.formal-gate.inspection/1" and inspection.get("status") == "consistent" and
              set(inspection["checks"]) == CHECKS and inspection["required_claims"] == CLAIMS, "complete owner inspection required")
    for key in ("model", "inputs", "selections", "context_binding"):
        a.require(inspection[key] == result[key], "owner inspection differs from retained result: " + key)
    a.require(inspection["selected_request_sha256"] == a.canonical_sha(request) and
              inspection["evidence"] == {"result_sha256": a.sha(files["evidence/result.json"]), **result["evidence"]}, "owner inspection binding differs")
    a.require(request["selections"] == result["selections"] and request["context_binding"] == result["context_binding"], "selected proof request differs")
    observations = result["observations"]
    a.require(observations["proof_modules"] == MODULES, "required current proof module set differs")
    for key, count in (("current_dynamic_proof_invocations", 7), ("current_kernel_replay_invocations", 1), ("current_runtime_invocations", 1)):
        a.require(observations[key] == count and inspection["observations"][key] == count, "retained proof execution stage missing")
    for module in MODULES[:-1]:
        a.require(all(module + suffix in members for suffix in (".lean", ".olean", ".log")), "required compiled current proof missing")
    a.require({"GateRun.lean", "actual-runtime.log", "dynamic-kernel-replay.log"} <= members.keys(), "current kernel/runtime evidence missing")
    pins = result["runtime_identity"]["pins"]
    a.require(result["runtime_identity"]["sha256"] == a.canonical_sha(pins), "proof runtime identity differs")
    a.require({p[len("machinery/"):] for p in files if p.startswith("machinery/")} == set(pins), "proof machinery closure differs")
    fixed = {"SELECTION.json", "source-freeze.json", "selected-request.json", "correspondence.md", "library-provenance.md", "materialize.py",
             "inspection.json", "inspection-execution.json", "inspection-stderr.txt"}
    a.require({p for p in files if not p.startswith(("machinery/", "evidence/", "transport/"))} - {"PROOFS.json", "index.html"} == fixed,
              "current proof documentation closure differs")
    for path, digest in pins.items():
        a.require(a.sha(files["machinery/" + a.name(path)]) == digest, "retained proof machinery differs")
    a.require({p for p in pins if p.endswith(".lean")} == LIBRARY, "selected formal library source profile differs")
    inspected = {k: v for k, v in inspection["runtime_identity"]["pins"].items() if k != ".cache/formal-origin-v1/selection.json"}
    a.require(inspected == {k: v for k, v in pins.items() if k != ".cache/formal-origin-v1/selection.json"}, "inspected proof machinery differs")
    audit = observations["theorem_audit"]
    a.require(audit and all(set(v) <= {"Classical.choice", "Quot.sound", "propext"} for v in audit.values()), "unsupported proof axiom")
    model_raw = recovered["evidence/" + result["inputs"]["model"]["retained_path"]]
    # The selected path supplies a model, not a carrier; the formal owner checks reconstruction.
    a.require(request["input"]["format"] == "model" and a.sha(model_raw) == result["inputs"]["model"]["raw_sha256"] == request["input"]["raw_sha256"], "selected model input differs")
    identity = a.model_identity(model_raw)
    a.require({k: identity[k] for k in ("id", "sha256")} == result["model"], "proof result describes another model")
    views = recovered["evidence/" + result["inputs"]["supplied_views"]["retained_path"]]
    a.require(a.sha(views) == result["inputs"]["supplied_views"]["raw_sha256"] == request["supplied_views"]["raw_sha256"], "supplied current views differ")
    return result, identity, archive


def catalog(files):
    selected = json.loads(files["SELECTION.json"])
    version = a.version(selected["version"])
    freeze = a.source_freeze(files["source-freeze.json"], version)
    result, identity, archive = validate_evidence(files)
    a.require(a.sha(files["transport/TRANSPORT.json"]) == selected["bundle_archive"]["sha256"], "selected proof transport differs")
    a.require(files["materialize.py"] == Path(transport.__file__).read_bytes(), "installed proof materializer differs")
    a.require(a.sha(files["source-freeze.json"]) == selected["source_freeze"]["sha256"] and
              result["inputs"]["model"]["raw_sha256"] == selected["model"]["sha256"], "selected source/model bytes differ")
    for key, path in (("result", "evidence/result.json"), ("request", "selected-request.json"),
                      ("library_provenance", "library-provenance.md")):
        a.require(a.sha(files[path]) == selected[key]["sha256"], "selected current proof input differs: " + key)
    a.require(a.sha(files["correspondence.md"]) == selected["correspondence"]["sha256"], "method correspondence differs")
    a.require(a.sha(files["machinery/scripts/formal_gate.py"]) == selected["inspector"]["sha256"], "selected formal inspector differs")
    execution = json.loads(files["inspection-execution.json"])
    a.require(execution["returncode"] == 0 and execution["stdout_sha256"] == a.sha(files["inspection.json"]) and
              execution["stderr_sha256"] == a.sha(files["inspection-stderr.txt"]), "retained inspection output differs")
    source_files = {"library/" + p: files["machinery/" + p].decode() for p in sorted(LIBRARY)}
    source_files.update({"current/" + m + ".lean": files["evidence/" + m + ".lean"].decode() for m in MODULES})
    declarations, imports = lexical.source_catalog(source_files)
    value = {"kind": "stdo.current-proof-reader/1", "version": version,
             "source_identity_sha256": freeze["source_identity_sha256"], "model": identity,
             "selection_sha256": a.sha(files["SELECTION.json"]), "result_sha256": a.sha(files["evidence/result.json"]),
             "runtime_identity": result["runtime_identity"], "selections": result["selections"],
             "transport": archive,
             "transport_sha256": a.sha(files["transport/TRANSPORT.json"]),
             "claims": [{"id": claim, "title": TITLES[claim]} for claim in CLAIMS],
             "checked_claims": result["checked_claims"], "observations": result["observations"], "limits": result["limits"],
             "source_scope": "Current generated Gate sources and their exact selected reusable library; library provenance retains its own original basis.",
             "reference_scope": "Lexical source links, not kernel proof dependencies. Source-to-model prose fidelity is independently assessed.",
             "standing": "Retained successful exact model/view verification and owner consistency inspection. Reading/checking this page executes no Lean proof.",
             "sources": [{"file": p, "sha256": a.sha(text.encode()), "lines": len(text.splitlines()), "imports": imports[p]} for p, text in source_files.items()],
             "declarations": declarations,
             "members": a.inventory({p: raw for p, raw in files.items() if p not in ("PROOFS.json", "index.html")})}
    return value, source_files


APP = r"""'use strict';(()=>{
const d=JSON.parse(document.getElementById('proof-data').textContent),c=d.catalog,$=id=>document.getElementById(id);
const el=(tag,text)=>{let n=document.createElement(tag);if(text!==undefined)n.textContent=text;return n};
const byId=new Map(c.declarations.map(x=>[x.id,x]));let trail=[];
$('model').textContent=c.model.id+' · SHA256 '+c.model.sha256;
$('counts').textContent=c.observations.current_dynamic_proof_invocations+' current elaborations · '+c.observations.current_kernel_replay_invocations+' kernel replay · '+c.observations.current_runtime_invocations+' runtime invocation';
for(const claim of c.claims){let n=el('article');n.append(el('h3',claim.title),el('p',claim.id));$('claims').append(n)}
for(const limit of c.limits)$('limits').append(el('li',limit));
$('evidence').textContent=JSON.stringify({selections:c.selections,runtime_identity:c.runtime_identity,observations:c.observations},null,2);
function file(path,line=1){let pre=el('pre');pre.className='source-box';d.sources[path].split('\n').forEach((text,i)=>{let row=el('span');row.className='source-row'+(i+1===line?' selected':'');row.id='line-'+(i+1);row.append(el('span',String(i+1).padStart(5)+'  '),el('span',text));pre.append(row)});$('reader').replaceChildren(el('h2',path),pre);pre.querySelector('.selected')?.scrollIntoView({block:'nearest'})}
function declaration(id){let x=byId.get(id);if(!x)return;trail.push(id);let button=el('button','Open complete source at line '+x.start_line);button.onclick=()=>file(x.file,x.start_line);$('reader').replaceChildren(el('h2',x.id),el('p',x.kind+' · '+x.file+':'+x.start_line+'–'+x.end_line),el('pre',x.statement),button);let nav=el('nav');for(const ref of x.references){let b=el('button',ref.target+' (line '+ref.line+')');b.onclick=()=>declaration(ref.target);nav.append(b)}$('reader').append(nav);$('back').disabled=trail.length<2}
$('back').onclick=()=>{if(trail.length>1){trail.pop();let id=trail.pop();declaration(id)}};
for(const source of c.sources){let b=el('button',source.file);b.onclick=()=>file(source.file);$('modules').append(b)}
function search(){let query=$('query').value.toLowerCase(),matches=c.declarations.filter(x=>(x.id+' '+x.statement).toLowerCase().includes(query));$('results').replaceChildren();$('matches').textContent=matches.length+' declarations';for(const x of matches.slice(0,100)){let b=el('button',x.id);b.onclick=()=>declaration(x.id);$('results').append(b)}}
$('query').oninput=search;search();
})();"""


def render(value, sources):
    data = json.dumps({"catalog": value, "sources": sources}, ensure_ascii=True, separators=(",", ":")).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    html = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" href="data:,"><title>Current STDO model proofs</title><style>@@CSS@@</style></head><body>
<header><nav class="topnav"><a href="../index.html">Documentation home</a><a href="../constraint-explorer/index.html">Current constraints</a><a href="../../AXIOMATIC_CALCULUS.md">Owning calculus</a><a href="correspondence.md">Current method correspondence</a><a href="library-provenance.md">Library provenance</a></nav>
<p class="eyebrow">STDO @@VERSION@@ / EXACT MODEL AND VIEWS</p><h1>Read the current model proofs</h1><p id="model" class="identity"></p><p id="counts"></p><p class="boundary">These retained executions check the finite declared model and selected views. Original prose-to-model fidelity and semantic acceptance remain separate. This reader and its inventory checker do not execute Lean.</p></header>
<div class="layout"><aside><label for="query">Find a declaration</label><input id="query" type="search"><p id="matches"></p><nav id="results"></nav><h3>Complete source files</h3><nav id="modules"></nav></aside><main><div id="claims" class="claims"></div><div class="reader-nav"><button id="back" disabled>Back</button></div><article id="reader"></article>
<details><summary>Selected inputs, runtime, stages and theorem axiom audit</summary><pre id="evidence"></pre></details><h2>Exact bounds</h2><ul id="limits"></ul></main></div>
<footer><a href="PROOFS.json">Exact catalog</a> · <a href="evidence/result.json">Executed result</a> · <a href="inspection.json">Owner consistency inspection</a> · <a href="evidence/view-comparison.json">Current view comparison</a> · <a href="selected-request.json">Selected request</a> · <a href="transport/TRANSPORT.json">Complete exact evidence transport</a><p>To recover every compiled artifact from its ordered archive parts, run this directory's <code>python3 materialize.py materialize --destination /absolute/new/evidence</code>. The destination must be outside the immutable release. Extraction verifies all original bytes; it does not run Lean. Then run <code>python3 materialize.py request --evidence /absolute/new/evidence --output /absolute/current-request.json</code> to select extracted model/view paths. Follow the <a href="../README.md">portable verification recipe</a> with the selected installed runtime. The original request and verdict remain unchanged.</p></footer>
<script id="proof-data" type="application/json">@@DATA@@</script><script>@@APP@@</script></body></html>"""
    values = {"CSS": lexical.CSS, "VERSION": value["version"], "DATA": data, "APP": APP}
    return re.sub(r"@@(CSS|VERSION|DATA|APP)@@", lambda match: values[match[1]], html).encode()


def check_files(files):
    value, sources = catalog(files)
    a.require(files["PROOFS.json"] == a.encoded(value) and files["index.html"] == render(value, sources), "current proof reader/catalog differs")
    a.require({r["path"] for r in value["members"]} | {"PROOFS.json", "index.html"} == set(files), "current proof reader population differs")
    return {"kind": value["kind"], "status": "checked", "version": value["version"],
            "source_identity_sha256": value["source_identity_sha256"], "model": value["model"], "members": len(files),
            "standing": "documentation custody/reproduction; no fresh Lean execution"}


def build(repository, selection_path, selection_sha, output):
    root = a.ordinary(repository)
    selected = a.selection(root, selection_path, selection_sha, "stdo.current-proof-selection/1")
    archive_path = root / a.name(selected["bundle_archive"]["path"])
    lean_root = root / a.name(selected["lean_root"])
    a.disjoint(output, archive_path); a.disjoint(output, lean_root)
    result_raw = a.pinned(root, selected["result"])
    result = json.loads(result_raw)
    descriptor_raw = a.pinned(root, selected["bundle_archive"])
    archive_raw, archive, recovered = transport.read_transport(archive_path, selected["bundle_archive"]["sha256"], visible=True)
    a.require(recovered["result.json"] == result_raw, "proof archive/result differs")
    files = {"SELECTION.json": a.regular(selection_path), "source-freeze.json": a.pinned(root, selected["source_freeze"]),
             "selected-request.json": a.pinned(root, selected["request"]), "correspondence.md": a.pinned(root, selected["correspondence"]),
             "library-provenance.md": a.pinned(root, selected["library_provenance"]),
             "transport/TRANSPORT.json": descriptor_raw, "materialize.py": Path(transport.__file__).read_bytes()}
    files.update({"transport/" + row["path"]: a.regular(archive_path.parent / row["path"]) for row in archive['parts']})
    files.update({"evidence/" + n: raw for n, raw in recovered.items() if n.endswith((".lean", ".log")) or n in
                 ("manifest.json", "result.json", "request.json", "replay-request.json", "supplied-views.json", "view-comparison.json")})
    a.pinned(root, selected["model"])
    for path, digest in result["runtime_identity"]["pins"].items():
        raw = a.regular(lean_root / a.name(path)); a.require(a.sha(raw) == digest, "current proof machinery differs: " + path)
        files["machinery/" + path] = raw
    inspector = root / a.name(selected["inspector"]["path"])
    a.pinned(root, selected["inspector"])
    a.require(inspector == lean_root / "scripts/formal_gate.py", "formal owner inspector path differs")
    python = Path(selected["python"]["invocation"])
    a.require(python.is_absolute() and a.sha(a.regular(python.resolve(strict=True))) == selected["python"]["sha256"], "selected inspector Python differs")
    with tempfile.TemporaryDirectory(prefix="stdo-proof-inspection-") as temporary:
        bundle = Path(temporary).resolve() / "evidence"
        transport.materialize_transport(archive_path, bundle, selected["bundle_archive"]["sha256"])
        command = [str(python), "-I", "-S", "-B", str(inspector), "inspect-evidence", "--bundle", str(bundle), "--request", str(root / selected["request"]["path"])]
        process = subprocess.run(command, capture_output=True, timeout=180)
    a.require(process.returncode == 0, "formal owner inspection refused: " + process.stdout.decode(errors="replace"))
    files["inspection.json"] = process.stdout
    files["inspection-execution.json"] = a.encoded({"argv": command, "returncode": process.returncode,
                                                  "stdout_sha256": a.sha(process.stdout), "stderr_sha256": a.sha(process.stderr)})
    files["inspection-stderr.txt"] = process.stderr
    value, sources = catalog(files)
    files.update({"PROOFS.json": a.encoded(value), "index.html": render(value, sources)})
    checked = check_files(files)
    a.write_tree(output, files)
    return dict(checked, status="built", destination=str(output))

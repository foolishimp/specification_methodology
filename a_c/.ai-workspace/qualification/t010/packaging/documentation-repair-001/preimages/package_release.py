#!/usr/bin/env python3
"""Prepare the fixed common proposal as a local, inspectable release bundle.

This application-specific packager copies supplied F_P meanings unchanged.
It does not author meaning, issue acceptance, select a Product version or publish.
The build command is for an explicitly closed model selected by the Executive.
"""
from __future__ import annotations

import argparse
from collections import defaultdict, deque
from contextlib import chdir
import gzip
import hashlib
import html
import importlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tarfile

ROOT = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / "release_tools"))
import bundle_check as checks
import public_receipts as receipts

ARTIFACT = "a_c-stdo-v3-common-35fb4824"
UPSTREAM = "fe085cedddde3a18554f8749b230bfe47f3dcce7"
BUILDER_MANIFEST = "3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782"


def save(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def copy(source: Path, target: Path) -> None:
    checks.require(source.is_file() and not source.is_symlink(), f"missing or redirected input: {source}")
    target.parent.mkdir(parents=True, exist_ok=True)
    checks.require(not target.exists(), f"preserve existing output: {target}")
    target.write_bytes(source.read_bytes())


def custody(root: Path) -> None:
    info = checks.load(root / "custody.json")
    for row in info["files"]:
        if "path" not in row:
            continue
        data = (root / checks.safe_path(row["path"])).read_bytes()
        checks.require(len(data) == row["bytes"] and checks.sha(data) == row["sha256"],
                       f"stale prepared dependency: {row['path']}")


def preparation(upstream: Path) -> dict:
    sources = checks.check_sources(ROOT)
    sections = checks.check_sections(ROOT)
    for directory in ("vendor", "upstream", "builder_basis"):
        custody(ROOT / "release_tools" / directory)
    checks.require(checks.sha((ROOT / "release_tools/builder_basis/manifest.json").read_bytes()) == BUILDER_MANIFEST,
                   "installed builder source changed")
    checks.require(checks.load(ROOT / "release_tools/upstream/custody.json")["commit"] == UPSTREAM,
                   "prepared exporter commit differs")
    codec_input = ROOT / "build/implementation/code/ac_graph.py"
    if not codec_input.exists():
        codec_input = ROOT / "codec/ac_graph.py"
    checks.require(checks.sha(codec_input.read_bytes()) == checks.CODEC_SHA, "exact codec snapshot changed")
    upstream = upstream.resolve(strict=True)
    head = subprocess.check_output(["git", "--no-optional-locks", "-C", str(upstream), "rev-parse", "HEAD"], text=True).strip()
    checks.require(head == UPSTREAM, "Graphify checkout differs from the pinned commit")
    status = subprocess.check_output(["git", "--no-optional-locks", "-C", str(upstream), "status", "--porcelain=v1", "--untracked-files=no"])
    checks.require(not status, "pinned Graphify checkout has tracked modifications")
    for row in checks.load(ROOT / "release_tools/upstream/custody.json")["files"]:
        checks.require(checks.sha((upstream / row["path"]).read_bytes()) == row["sha256"],
                       f"Graphify exporter input changed: {row['path']}")
    import base64
    data = (ROOT / checks.VIS_LOCAL).read_bytes()
    checks.require("sha384-" + base64.b64encode(hashlib.sha384(data).digest()).decode() == checks.VIS_SRI,
                   "offline display runtime differs from the official SRI pin")
    return {"status": "prepared_inputs_checked", "subject": checks.SUBJECT, "sources": sources,
            "source_sections": len(sections),
            "graphify_commit": head, "offline_visualization_sri": checks.VIS_SRI,
            "claim": "Packaging inputs only; no model, final bundle, archive, semantic acceptance or publication created by this check."}


def modules(upstream: Path):
    sys.path.insert(0, str(upstream.resolve()))
    import networkx as nx
    checks.require(nx.__version__ == "3.4.2", "use the pinned existing networkx3.4.2 environment")
    exporter = importlib.import_module("graphify.export")
    checks.require(Path(exporter.__file__).resolve().is_relative_to(upstream.resolve()),
                   "Graphify import did not select the pinned checkout")
    return nx, exporter


def record_label(record) -> str:
    fields = record.fields
    for field in ("value", "predicate", "qualifiers", "uncertainty", "allowed_variation"):
        value = fields.get(field)
        if isinstance(value, dict):
            for key in ("label", "statement", "definition", "meaning", "detail"):
                if isinstance(value.get(key), str) and value[key]:
                    return value[key].replace("\n", " ")[:150]
            statements = value.get("statements")
            if isinstance(statements, list) and statements and isinstance(statements[0], str):
                return statements[0].replace("\n", " ")[:150]
    return record.family + ": " + record.identity.rsplit(":", 1)[-1]


def grounding(value) -> list[dict]:
    result = []
    if isinstance(value, dict):
        if {"path", "quote", "start_line", "end_line"} <= value.keys():
            result.append(value)
        for child in value.values():
            result.extend(grounding(child))
    elif isinstance(value, list):
        for child in value:
            result.extend(grounding(child))
    return result


def select_records(model, limit: int) -> list[str]:
    checks.require(limit > 0, "display budget must be positive")
    groups = defaultdict(deque)
    for identity, record in sorted(model.records.items()):
        gs = grounding(record.fields)
        source = gs[0]["path"] if gs else ""
        groups[(record.family, source)].append(identity)
    selected = []
    keys = sorted(groups)
    while len(selected) < min(limit, len(model.records)):
        for key in keys:
            if groups[key] and len(selected) < limit:
                selected.append(groups[key].popleft())
    return sorted(selected)


def views(bundle: Path, model, upstream: Path, limit: int) -> dict:
    nx, exporter = modules(upstream)
    graph = nx.DiGraph()
    for identity, record in sorted(model.records.items()):
        paths = sorted({g["path"] for g in grounding(record.fields)})
        graph.add_node(identity, label=record_label(record), source_file="; ".join(paths),
                       file_type="document", family=record.family)
    local_occurrences = 0
    external_occurrences = 0
    for ref in model.references:
        if ref.target not in model.records:
            external_occurrences += 1
            continue
        local_occurrences += 1
        if not graph.has_edge(ref.owner, ref.target):
            graph.add_edge(ref.owner, ref.target, occurrences=[], confidence="EXTRACTED",
                           _src=ref.owner, _tgt=ref.target)
        graph[ref.owner][ref.target]["occurrences"].append(
            {"path": list(ref.path), "governing": ref.schema["governing"]})
    for _, _, data in graph.edges(data=True):
        paths = sorted({"/" + "/".join(x["path"]) for x in data["occurrences"]})
        data["relation"] = "; ".join(paths)[:180] + f" ({len(data['occurrences'])} exact reference occurrences)"
    all_data = {"kind": "a_c.common.readable-record-projection/1", "parent": {"id": model.identity, "sha256": model.sha256},
                "directed": True, "multigraph": False,
                "nodes": [{"id": identity, **data} for identity, data in graph.nodes(data=True)],
                "links": [{"source": a, "target": b, **{k: v for k, v in data.items() if k not in ("_src", "_tgt")}}
                          for a, b, data in graph.edges(data=True)],
                "claim": "Full record-discovery graph; local typed references displayed, parallel occurrences counted; external coordinate plumbing omitted. Not a reversible carrier, complete governing model or implication graph."}
    save(bundle / "records-graph.json", all_data)
    selected = select_records(model, limit)
    view = graph.subgraph(selected).copy()
    families = sorted({model.records[key].family for key in selected})
    communities = {i: [key for key in selected if model.records[key].family == family]
                   for i, family in enumerate(families)}
    labels = {i: "Record family: " + family for i, family in enumerate(families)}
    # The official exporter derives its title from cwd/output_path. A fixed
    # relative filename makes the unmodified export reproducible in any location.
    with chdir(bundle):
        written = exporter.to_html(view, communities, "graph.html", community_labels=labels,
                                   node_limit=len(selected), learning_overlay={})
    checks.require(written, "official Graphify HTML exporter did not produce the record view")
    rendered = (bundle / "graph.html").read_text(encoding="utf-8")
    original_sha = checks.sha(rendered.encode("utf-8"))
    checks.require(rendered.count(f'src="{checks.VIS_URL}"') == 1, "official dependency markup changed")
    scope_text = (f"Proposed common35fb4824 · {len(selected)} of {len(model.records)} exact records · "
                  f"{view.number_of_edges()} displayed reference pairs · family colours · no algorithmic communities or semantic acceptance. ")
    banner = ('<div id="record-view-scope" style="position:fixed;top:10px;left:10px;z-index:10;'
              'max-width:calc(100% - 330px);padding:10px;background:#172330;color:white;border-radius:6px;'
              'font:12px/1.5 system-ui">' + html.escape(scope_text)
              + '<a style="color:#87c7ff" href="records.html" target="_blank">All records and grounding</a> · '
              '<a style="color:#87c7ff" href="index.html" target="_blank">Scope and qualification</a></div>')
    checks.require(rendered.count('<div id="graph"></div>') == 1, "official graph anchor changed")
    rendered = rendered.replace(f'src="{checks.VIS_URL}"', f'src="{checks.VIS_LOCAL}"', 1)
    rendered = rendered.replace('<div id="graph"></div>', banner + '<div id="graph"></div>', 1)
    (bundle / "graph.html").write_text(rendered, encoding="utf-8")
    scope = {"kind": "a_c.common.readable-display-scope/1", "parent": {"id": model.identity, "sha256": model.sha256},
             "full_records": len(model.records), "displayed_records": len(selected),
             "included": selected, "omitted": sorted(set(model.records) - set(selected)),
             "selection": "Deterministic round robin by (record family, first recorded grounding path), ordered record IDs within each group; no relevance or truth ranking.",
             "display_limit": limit, "aggregated_nodes": 0, "family_colours": labels,
             "full_reference_pairs": graph.number_of_edges(), "displayed_reference_pairs": view.number_of_edges(),
             "local_reference_occurrences": local_occurrences, "omitted_external_reference_occurrences": external_occurrences,
             "parallel_occurrences": "Collapsed only for display; every occurrence path and governing flag retained in records-graph.json; complete reversible carrier preserved separately.",
             "official_exporter_commit": UPSTREAM, "official_html_sha256": original_sha,
             "modifications": ["Exact runtime script URL rewritten to local byte-identical SRI-pinned asset", "Explicit scope/navigation banner inserted before graph div"],
             "banner_html": banner, "claim": "Display projection only; connectivity and arrow direction do not establish implication, normative force, complete acquisition or acceptance."}
    save(bundle / "view-scope.json", scope)
    return scope


def source_views(bundle: Path) -> None:
    for row in checks.load(bundle / "package-custody.json")["members"]:
        name = row["path"]
        text = (bundle / "source" / name).read_text(encoding="utf-8")
        lines = "\n".join(f'<span id="L{i}" data-line="{i}">{html.escape(line)}</span>'
                          for i, line in enumerate(text.splitlines(), 1))
        page = ('<!doctype html><html lang="en"><meta charset="utf-8"><title>' + html.escape(name)
                + '</title><style>body{font:14px system-ui;margin:24px;background:#101720;color:#dfeaf4}a{color:#87c7ff}'
                  'pre{white-space:pre-wrap;overflow-wrap:anywhere;line-height:1.5;counter-reset:line}span{display:block}'
                  'span:before{content:attr(data-line);display:inline-block;width:4em;color:#7392aa;user-select:none}'
                  'span:target{background:#36481d}</style><h1>' + html.escape(name) + '</h1><p>Exact frozen source · SHA256 '
                + row["sha256"] + '</p><pre>' + lines + '</pre></html>\n')
        target = bundle / "source-view" / (name + ".html")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page, encoding="utf-8")


def guide(bundle: Path, model, scope: dict) -> None:
    seed = next(iter(model.records))
    readme = f'''# Common STDO proposal representation

Prepared artifact `{ARTIFACT}` represents source commit
`35fb4824a064a84df5af214a0d0e2da597c18ac6`, package tree
`7f2070b61c848b42b4dfb3af1e0ce53869de1aa1`. It is a local release-preparation
bundle, with no Product version, release tag, publication or acceptance.

Open `index.html` or `records.html` locally. Serve the Graphify view through the
loopback preview command below to retain its official integrity/CORS settings.
The Graphify view
displays {scope['displayed_records']} of {len(model.records)} records. Its colours
identify authored record families. Every record remains searchable in
`records.html`; source links open line-addressed exact frozen source views.
The browser needs no CDN, model provider or installed Python package.
Interactive behavior has not been verified. The available browser surface
blocked an older local I5 view; no server or alternate browser route was used
to bypass that restriction. Static generation and exact-dependency checks do
not establish search, selection, filtering or neighbor-navigation behavior.

From this extracted directory, Python3 standard library is sufficient:

```sh
python3 -B release_tools/bundle_check.py .
python3 -B codec/ac_graph.py validate model.json
python3 -B codec/ac_graph.py decode carrier.json --out /tmp/common-model-recovered.json
python3 -B codec/ac_graph.py decode graph.json --out /tmp/common-upstream-recovered.json
python3 -B codec/ac_graph.py find carrier.json admission
python3 -B codec/ac_graph.py inspect carrier.json {seed}
python3 -B codec/ac_graph.py project carrier.json --seed {seed} --out /tmp/common-projection.json
python3 -B release_tools/source_reentry.py standards/ACTIVATION.md --start 1 --end 30
python3 -B release_tools/serve_preview.py .
```

Decode/project output paths must be fresh; choose new filenames for another run.
The last command prints a loopback-only HTTP URL; stop it with Ctrl-C.
`model.json`, `carrier.json` and actual upstream `graph.json` retain separate raw
file identities and exact model recovery. `records-graph.json` and the HTML are
display projections, with exact displayed/omitted/parallel-reference scope in
`view-scope.json`. They do not replace the complete reversible carrier or prove
governing closure. `coverage.json` retains the F_P processing dispositions and
unqualified semantic/cross-chunk boundaries. Search, inspection and acquisition
report only the declared codec fragment.

`source/` preserves all81 package members. `source-manifest.json` identifies the
58 semantic inputs, while `source-classification.json` separately accounts for
13 derived frame members and10 host/legal/release metadata members. Inclusion
does not turn templates or optional profiles into a consumer constitution.
`SOURCE-READINESS.md` retains the method's current unaccepted/unpublished
`not_ready` standing and open owner, independent-review and actual-use gates.
The source candidate is the represented subject, not a newly adopted builder.
The codec's selected builder remains exact STDO v2.5.1-rc.2; selected raw basis
sources under `release_tools/builder_basis/` are a documented subset, not an
Install or a complete STDO distribution.

`evidence/` contains explicitly supplied public authoring/review receipts only.
Both receipt types bind the exact source commitments, canonical model and raw
model/carrier/export/coverage/result bytes. A readable Markdown/text review is
copied only through its typed JSON receipt's explicit path/hash binding. See
`release_tools/PUBLIC-RECEIPTS.md`. Receipt matching does not prove its issuer,
its reported independence or the truth/sufficiency of its bounded assessment.
Private native invocation bodies, event streams, settings files and any hidden
reasoning are excluded. Opaque hashes and curated reported usage do not give a
recipient complete private acquisition custody. They are retained locally by
the construction record and remain a stated verification boundary.

`inventory.json` accounts for every bundle file except itself and `SHA256SUMS`.
`SHA256SUMS` also binds the inventory and omits only its own bytes. The archive's
external `.sha256` file binds the complete deterministic tar.gz. Repackaging
identical bytes uses sorted members, fixed modes/owners/timestamps and gzip
mtime0. `package_release.py` and `release_tools/` preserve the packaging recipe,
exact exporter source, offline asset and third-party licensing custody. Building
requires the existing pinned Graphify checkout and networkx3.4.2 environment;
viewing, codec use and bundle verification require no Graphify installation.

Third-party licenses retain their own scope: frozen common source licenses,
Graphify Apache2.0/MIT and notices, vis-network Apache2.0/MIT, and the selected
builder source license are preserved unchanged. No applicable license for the
a_c-owned codec, authored interpretation and new packaging has been selected
here. Distribution terms and license metadata remain an owner choice; absence
of a root license is not asserted as an automatic publication gate. This
bundle does not apply a third-party license to those materials. Owner release
disposition and any required semantic acceptance remain separate decisions.
'''
    (bundle / "README.md").write_text(readme, encoding="utf-8")
    body = ('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>Common STDO · proposal representation</title><style>body{max-width:920px;margin:40px auto;padding:0 20px;'
            'background:#101720;color:#e5edf5;font:16px/1.6 system-ui}a{color:#87c7ff}code{overflow-wrap:anywhere}'
            'nav{display:flex;flex-wrap:wrap;gap:18px;padding:20px;background:#172330}pre{white-space:pre-wrap;font:13px/1.6 ui-monospace,monospace}</style>'
            '<h1>Common STDO · proposal representation</h1><p>Source35fb4824 · a_c/Graphify · prepared locally, unaccepted and unpublished.</p>'
            '<nav><a href="graph.html">Explore Graphify graph</a><a href="records.html">Search all exact records and grounding</a>'
            '<a href="RELEASE.json">Release standing</a><a href="coverage.json">Coverage and unresolved scope</a>'
            '<a href="evidence/">Public evidence</a></nav><h2>Use and qualification</h2><pre>' + html.escape(readme) + '</pre></html>\n')
    (bundle / "index.html").write_text(body, encoding="utf-8")


def archive(bundle: Path, output: Path) -> dict:
    checks.require(not output.exists(), "archive exists; preserve the previous result")
    sidecar = output.with_name(output.name + ".sha256")
    checks.require(not sidecar.exists(), "archive checksum already exists")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("xb") as stream:
        with gzip.GzipFile(filename="", mode="wb", fileobj=stream, mtime=0, compresslevel=9) as compressed:
            with tarfile.open(fileobj=compressed, mode="w", format=tarfile.PAX_FORMAT) as tar:
                for name in checks.files(bundle):
                    data = (bundle / name).read_bytes()
                    member = tarfile.TarInfo(ARTIFACT + "/" + name)
                    member.size = len(data)
                    member.mode = 0o644
                    member.uid = member.gid = member.mtime = 0
                    member.uname = member.gname = ""
                    tar.addfile(member, io.BytesIO(data))
    digest = checks.sha(output.read_bytes())
    sidecar.write_text(f"{digest}  {output.name}\n", encoding="ascii")
    return {"file": output.name, "bytes": output.stat().st_size, "sha256": digest,
            "format": "deterministic tar.gz; sorted files, fixed0644 uid/gid/mtime0, blank owner names, gzip mtime0"}


def build(args) -> dict:
    preparation(args.upstream)
    proposal = args.proposal.resolve(strict=True)
    graph = args.graph.resolve(strict=True) if args.graph else proposal / "graph.json"
    codec_input = ROOT / "build/implementation/code/ac_graph.py"
    if not codec_input.exists():
        codec_input = ROOT / "codec/ac_graph.py"
    ac = checks.codec(codec_input)
    model = ac.validate(ac.read_json(proposal / "model.json"))
    checks.check_model_source(ac, model, ROOT)
    checks.require(model.records, "record display requires a nonempty supplied model")
    result = checks.load(proposal / "result.json")
    coverage = checks.load(proposal / "coverage.json")
    checks.require(result["model_id"] == model.identity and result["model_sha256"] == model.sha256,
                   "supplied result does not bind this exact model")
    checks.require(result["processing_complete"] is True and coverage["processing_complete"] is True,
                   "preserve incomplete processing; do not package it as the complete final proposal")
    for path in (proposal / "carrier.json", graph):
        checks.require(ac.decode(ac.GraphCarrier(ac.read_json(path))).document == model.document,
                       f"supplied carrier does not recover the unchanged model: {path.name}")
    paths = {name: proposal / name for name in receipts.ARTIFACTS}
    paths["graph.json"] = graph
    expected = receipts.expected_bindings(ROOT, model, paths)
    construction, _ = receipts.receipt(args.public_evidence, expected, receipts.CONSTRUCTION)
    checks.require(bool(args.review), "at least one typed bounded-review receipt is required")
    reviewed = []
    receipt_ids = {construction["receipt_id"]}
    for path in args.review:
        review, reports = receipts.receipt(path, expected, receipts.REVIEW)
        checks.require(review["receipt_id"] not in receipt_ids, "public receipt identity collision")
        receipt_ids.add(review["receipt_id"])
        reviewed.append((path, review, reports))
    bundle = args.bundle or ROOT / "bundle" / ARTIFACT
    dist = args.dist or ROOT / "dist"
    checks.require(not bundle.exists(), "bundle output exists; preserve its identity")
    bundle.mkdir(parents=True)
    for name in ("model.json", "carrier.json", "coverage.json", "result.json"):
        copy(proposal / name, bundle / name)
    copy(graph, bundle / "graph.json")
    for name in checks.SOURCE_PINS:
        copy(ROOT / name, bundle / name)
    copy(ROOT / "SOURCE-READINESS.md", bundle / "SOURCE-READINESS.md")
    for row in checks.load(ROOT / "package-custody.json")["members"]:
        copy(ROOT / "source" / row["path"], bundle / "source" / row["path"])
    copy(codec_input, bundle / "codec/ac_graph.py")
    copy(Path(__file__).resolve(), bundle / "package_release.py")
    for name in checks.files(ROOT / "release_tools"):
        copy(ROOT / "release_tools" / name, bundle / "release_tools" / name)
    copy(args.public_evidence, bundle / "evidence/authoring-public.json")
    review_rows = []
    for i, (path, review, reports) in enumerate(reviewed, 1):
        directory = f"evidence/reviews/review-{i:03d}"
        name = directory + "/receipt.json"
        copy(path, bundle / name)
        report_rows = []
        for binding, report in reports:
            destination = directory + "/" + binding["path"]
            copy(report, bundle / destination)
            report_rows.append({"path": destination, "bytes": binding["bytes"], "sha256": binding["sha256"]})
        review_rows.append({"path": name, "sha256": checks.sha(path.read_bytes()),
                            "receipt_id": review["receipt_id"], "reports": report_rows})
    scope = views(bundle, model, args.upstream, args.display_limit)
    data = {"kind": "a_c.common.exact-record-browser/1", "parent": {"id": model.identity, "sha256": model.sha256},
            "source_paths": [row["path"] for row in checks.load(bundle / "package-custody.json")["members"]],
            "records": [{"family": record.family, "record": record.fields} for record in model.records.values()]}
    save(bundle / "records.json", data)
    template = (ROOT / "release_tools/records-template.html").read_text(encoding="utf-8")
    checks.require(template.count("__RECORD_DATA__") == 1, "record-browser template differs")
    embedded = json.dumps(data, ensure_ascii=True, separators=(",", ":")).replace("<", "\\u003c")
    (bundle / "records.html").write_text(template.replace("__RECORD_DATA__", embedded), encoding="utf-8")
    source_views(bundle)
    save(bundle / "RELEASE.json", {"kind": "a_c.common.representation-release-preparation/1", "artifact": ARTIFACT,
         "subject": checks.SUBJECT, "source_commit": "35fb4824a064a84df5af214a0d0e2da597c18ac6",
         "package_tree": "7f2070b61c848b42b4dfb3af1e0ce53869de1aa1", "model": {"id": model.identity, "sha256": model.sha256},
         "standing": "local_reviewable_preparation", "semantic_acceptance": "not_issued", "publication": "not_performed",
         "interactive_verification": "not_performed; prior local I5 browser action was policy-blocked and not bypassed; this new artifact remains interactively unverified",
         "source_method_release": "unaccepted_unpublished_not_ready", "product_version": None,
         "builder_basis": "stdo://releases/v2.5.1-rc.2/", "builder_manifest_sha256": BUILDER_MANIFEST,
         "graphify_commit": UPSTREAM, "codec_sha256": checks.CODEC_SHA,
         "review_receipts": review_rows, "public_authoring_receipt_sha256": checks.sha(args.public_evidence.read_bytes()),
         "public_receipt_contract": [receipts.CONSTRUCTION, receipts.REVIEW],
         "private_custody_boundary": "Native invocation bodies/events/config and hidden reasoning excluded. Public opaque hashes/curated receipts are not complete independently replayable private acquisition evidence.",
         "reserved_owner_decisions": ["Distribution terms/license metadata for a_c-owned codec, authored interpretation and new packaging; no inferred automatic licence gate", "Representation semantic acceptance where required by selected publication contract", "Exact artifact release/publication disposition"],
         "claim": "Prepared proposal artifact only; no STDO/a_c Product release, adoption, complete semantic fidelity, whole-calculus conformance or measured efficiency claim."})
    guide(bundle, model, scope)
    rows = [{"path": name, "bytes": (bundle / name).stat().st_size,
             "sha256": checks.sha((bundle / name).read_bytes())} for name in checks.files(bundle)]
    save(bundle / "inventory.json", {"kind": "a_c.common.complete-bundle-inventory/1", "artifact": ARTIFACT,
         "excluded_self_descriptors": ["inventory.json", "SHA256SUMS"], "files": rows})
    sums = "".join(f"{checks.sha((bundle / name).read_bytes())}  {name}\n"
                   for name in sorted([row["path"] for row in rows] + ["inventory.json"]))
    (bundle / "SHA256SUMS").write_text(sums, encoding="utf-8")
    replay = checks.check(bundle)
    packed = archive(bundle, dist / (ARTIFACT + ".tar.gz"))
    return {"status": "local_bundle_prepared", "bundle": str(bundle), "archive": packed,
            "checks": replay, "claim": "Local release preparation; owner licensing/acceptance/publication decisions reserved."}


def receipt_bindings(args) -> dict:
    """Print identities only; an author/reviewer supplies its own account."""
    checks.check_sources(ROOT)
    codec_input = ROOT / "build/implementation/code/ac_graph.py"
    if not codec_input.exists():
        codec_input = ROOT / "codec/ac_graph.py"
    ac = checks.codec(codec_input)
    proposal = args.proposal.resolve(strict=True)
    model = ac.validate(ac.read_json(proposal / "model.json"))
    checks.check_model_source(ac, model, ROOT)
    paths = {name: proposal / name for name in receipts.ARTIFACTS}
    if args.graph:
        paths["graph.json"] = args.graph.resolve(strict=True)
    return {"kind": "a_c.common.public-receipt-bindings/1",
            "bindings": receipts.expected_bindings(ROOT, model, paths),
            "claim": "Exact input coordinates only; not a construction/review receipt, semantic judgment or issuer-legitimacy proof."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    prepare = sub.add_parser("check-preparation", help="check exact sources, offline assets and pinned exporter without constructing final artifacts")
    prepare.add_argument("--upstream", type=Path, required=True)
    binding = sub.add_parser("receipt-bindings", help="read-only exact coordinates for receipt authors; never generates a review")
    binding.add_argument("--proposal", type=Path, required=True)
    binding.add_argument("--graph", type=Path)
    final = sub.add_parser("build", help="package an explicitly closed unchanged model; never publishes or accepts")
    final.add_argument("--proposal", type=Path, required=True)
    final.add_argument("--graph", type=Path, help="exact actual upstream export, if stored outside the proposal folder")
    final.add_argument("--public-evidence", type=Path, required=True)
    final.add_argument("--review", type=Path, action="append", required=True,
                       help="typed bounded-review JSON receipt; any Markdown/text reports must be bound by that receipt")
    final.add_argument("--upstream", type=Path, required=True)
    final.add_argument("--bundle", type=Path)
    final.add_argument("--dist", type=Path)
    final.add_argument("--display-limit", type=int, default=5000)
    args = parser.parse_args()
    try:
        if args.command == "check-preparation":
            result = preparation(args.upstream)
        elif args.command == "receipt-bindings":
            result = receipt_bindings(args)
        else:
            result = build(args)
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    except (ValueError, KeyError, TypeError, OSError, subprocess.CalledProcessError) as exc:
        print(json.dumps({"status": "refusal", "reason": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

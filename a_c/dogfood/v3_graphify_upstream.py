#!/usr/bin/env python3
"""Exercise pinned upstream Graphify on either frozen V3 I5 representation.

This helper performs no model/backend calls and makes no semantic acceptance,
governing-acquisition or efficiency claim. The exported JSON is the complete
carrier; the optional official HTML exporter receives a separately declared
discovery view. Upstream packages are qualification-only dependencies.
"""

from __future__ import annotations

import argparse
from collections import deque
from collections.abc import Iterator, Sequence
import copy
import gzip
import hashlib
import html
import json
from pathlib import Path
import sys
import tempfile
import time
from typing import Protocol, cast


AC_ROOT = Path(__file__).resolve().parents[1]
TENANT_ROOT = AC_ROOT / "build_tenants" / "graphify"
sys.path.insert(0, str(TENANT_ROOT / "code"))
sys.path.insert(0, str(TENANT_ROOT / "test_env"))

import ac_graph as ac
import check_upstream as boundary


class ViewGraph(boundary.Graph, Protocol):
    def neighbors(self, identity: str) -> Iterator[str]: ...

    def subgraph(self, identities: Sequence[str]) -> ViewGraph: ...

    def copy(self) -> ViewGraph: ...


class HtmlAPI(Protocol):
    def to_html(
        self,
        graph: ViewGraph,
        communities: dict[int, list[str]],
        output_path: str,
        *,
        community_labels: dict[int, str],
        node_limit: int,
        learning_overlay: dict[str, object],
    ) -> bool: ...


def read_object(path: Path) -> ac.Object:
    raw = path.read_bytes()
    if path.suffix == ".gz":
        raw = gzip.decompress(raw)
    parsed: ac.JSON = json.loads(raw)
    return ac.obj(parsed, str(path))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(value: bool, message: str) -> None:
    if not value:
        raise boundary.QualificationError(message)


def aliases(left: Path, right: Path) -> bool:
    """Include hard links when protecting unchanged subjects from output."""
    return left.resolve() == right.resolve() or (
        left.exists() and right.exists() and left.samefile(right)
    )


def write_report(path: Path, result: dict[str, object]) -> None:
    """Replace an old report without writing through any existing hard link."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent,
            prefix=".native-graphify-", suffix=".tmp", delete=False,
        ) as handle:
            temporary = Path(handle.name)
            handle.write(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n")
        temporary.replace(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def source_paths(consumer: Path) -> dict[str, Path]:
    paths = {
        "model": consumer / "artifacts" / "model.json.gz",
        "carrier": consumer / "artifacts" / "graph.json.gz",
        "selectors": consumer / "artifacts" / "selectors.json",
        "artifact_manifest": consumer / "artifacts" / "manifest.json",
        "input_archive": consumer / "input" / "candidate.tar.gz",
        "input_manifest": consumer / "input" / "manifest.json",
        "subject": consumer / "subject.json",
        "input_builder": consumer / "prepare.py",
        "consumer_builder": AC_ROOT / "dogfood" / "v3_graphify.py",
        "codec": TENANT_ROOT / "code" / "ac_graph.py",
        "boundary_helper": TENANT_ROOT / "test_env" / "check_upstream.py",
        "trial_helper": Path(__file__).resolve(),
    }
    return paths


def tamper_trials(persisted: ac.Object) -> list[dict[str, str]]:
    checks: list[dict[str, str]] = []
    for trial in ("missing-occurrence", "reversed-occurrence", "search-identity", "directed-profile"):
        changed = copy.deepcopy(persisted)
        nodes = [ac.obj(value, "node") for value in ac.seq(changed["nodes"], "nodes")]
        if trial == "missing-occurrence":
            victim = next(node for node in nodes if node["ac_role"] == "reference-occurrence")["id"]
            changed["nodes"] = [node for node in ac.seq(changed["nodes"], "nodes") if ac.obj(node, "node")["id"] != victim]
            changed["links"] = [
                edge for edge in ac.seq(changed["links"], "links")
                if ac.obj(edge, "edge")["source"] != victim
                and ac.obj(edge, "edge")["target"] != victim
            ]
        elif trial == "reversed-occurrence":
            occurrence = next(
                ac.obj(node["ac_payload"], "occurrence") for node in nodes
                if node["ac_role"] == "reference-occurrence"
                and ac.obj(node["ac_payload"], "occurrence")["owner"]
                != ac.obj(node["ac_payload"], "occurrence")["target"]
            )
            occurrence["owner"], occurrence["target"] = occurrence["target"], occurrence["owner"]
        elif trial == "search-identity":
            record = next(node for node in nodes if node["ac_role"] == "record")
            ac.obj(record["attributes"], "attributes")["semantic_identity"] = "urn:a-c:trial:misleading-identity"
        else:
            changed["directed"] = True
        try:
            ac.decode(ac.GraphCarrier(changed))
        except ac.Refusal as exc:
            checks.append({"trial": trial, "status": "refused", "reason": str(exc)})
        else:
            raise boundary.QualificationError(f"decoder accepted {trial} after actual upstream export")
    return checks


def visual_export(
    exporter: HtmlAPI,
    loaded: ViewGraph,
    persisted: ac.Object,
    seed: str,
    output: Path,
    *,
    mode: str,
    depth: int,
    budget: int,
) -> dict[str, object]:
    """Build a discovery view; a display budget is never an acquisition result."""
    if mode == "none":
        return {"status": "not-requested"}
    require(depth >= 0 and budget > 0, "HTML view requires nonnegative depth and positive node budget")
    if mode == "full":
        selected = sorted(loaded.nodes)
        candidates = len(selected)
    else:
        distances = {seed: 0}
        pending = deque([seed])
        while pending:
            current = pending.popleft()
            if distances[current] >= depth:
                continue
            for neighbor in sorted(loaded.neighbors(current)):
                if neighbor not in distances:
                    distances[neighbor] = distances[current] + 1
                    pending.append(neighbor)
        ordered = sorted(distances, key=lambda identity: (distances[identity], identity))
        candidates = len(ordered)
        selected = ordered[:budget]
    graph = loaded.subgraph(selected).copy()
    selected_set = set(selected)
    roles: dict[str, list[str]] = {}
    for raw in ac.seq(persisted["nodes"], "nodes"):
        node = ac.obj(raw, "node")
        identity = ac.string(node["id"], "node id")
        if identity in selected_set:
            role = ac.string(node["ac_role"], "carrier role")
            roles.setdefault(role, []).append(identity)
    communities = {index: sorted(roles[role]) for index, role in enumerate(sorted(roles))}
    labels = {index: "Carrier role: " + role for index, role in enumerate(sorted(roles))}
    require(
        exporter.to_html(
            graph, communities, str(output), community_labels=labels,
            node_limit=max(1, len(selected)), learning_overlay={},
        ),
        "official upstream HTML exporter declined the selected view",
    )
    scope = (
        f"Full structural carrier: {len(selected)} nodes. " if mode == "full" else
        f"Bounded structural discovery view: {len(selected)} of {candidates} nodes within {depth} hops. "
    )
    scope += (
        f"Complete carrier has {loaded.number_of_nodes()} nodes. "
        "Colors are carrier roles. This view is not governing acquisition or semantic acceptance."
    )
    banner = (
        '<div id="ac-view-scope" style="position:fixed;top:10px;left:10px;z-index:10;'
        'max-width:calc(100% - 330px);padding:10px;border-radius:6px;'
        'background:#1f2937;color:#fff;font:12px/1.5 system-ui">'
        + html.escape(scope) + "</div>\n"
    )
    rendered = output.read_text(encoding="utf-8")
    require('<div id="graph"></div>' in rendered, "unexpected official HTML output structure")
    output.write_text(rendered.replace('<div id="graph"></div>', banner + '<div id="graph"></div>', 1), encoding="utf-8")
    return {
        "status": "written",
        "path": str(output), "sha256": sha(output), "bytes": output.stat().st_size,
        "exporter": "graphify.export.to_html; scope banner added by this helper",
        "mode": mode, "seed": seed,
        "radius_hops": None if mode == "full" else depth,
        "node_budget": None if mode == "full" else budget,
        "candidate_nodes": candidates, "displayed_nodes": len(selected),
        "omitted_candidate_nodes": candidates - len(selected),
        "complete_carrier_nodes": loaded.number_of_nodes(),
        "displayed_edges": graph.number_of_edges(),
        "browser_dependency": "https://unpkg.com/vis-network@9.1.6/standalone/umd/vis-network.min.js (upstream integrity-pinned CDN)",
        "build_network_calls": False,
        "claim": "official structural visualization of a declared view; no governing acquisition or semantic acceptance",
    }


def qualification(args: argparse.Namespace) -> dict[str, object]:
    started = time.perf_counter()
    consumer = AC_ROOT / "dogfood" / f"stdo-v3-i5-{args.tenant}"
    paths = source_paths(consumer)
    for name, path in paths.items():
        require(path.is_file(), f"missing {name}: {path}")
    source_hashes = {name: sha(path) for name, path in paths.items()}
    subject = read_object(paths["subject"])
    require(subject["tenant"] == args.tenant, "subject tenant does not match selected consumer")
    query_text = ac.string(subject["discovery_query"], "discovery query")
    expected_identity = ac.string(subject["discovery_record"], "discovery record")
    require(bool(query_text.strip()), "discovery query must not be empty")
    manifest = read_object(paths["artifact_manifest"])
    require(manifest["profile"] == "a_c.v3-graphify-representation/1" and manifest["tenant"] == args.tenant, "wrong artifact manifest profile or tenant")
    require(manifest["subject_sha256"] == source_hashes["subject"], "artifact subject binding differs")
    require(manifest["input_manifest_sha256"] == source_hashes["input_manifest"], "artifact input binding differs")
    require(manifest["builder_sha256"] == source_hashes["consumer_builder"], "artifact builder changed; rebuild before trial")
    require(manifest["codec_sha256"] == source_hashes["codec"], "artifact codec changed; rebuild before trial")
    artifact_pins = ac.obj(manifest["artifacts"], "artifact manifest")
    for name in ("model", "carrier", "selectors"):
        pin = ac.obj(artifact_pins[paths[name].name], "artifact pin")
        require(pin["sha256"] == source_hashes[name], f"{name} differs from artifact manifest")
        require(pin["bytes"] == paths[name].stat().st_size, f"{name} size differs from artifact manifest")
    upstream = args.upstream.resolve()
    upstream_evidence = boundary.verify_upstream(upstream)
    sys.path.insert(0, str(upstream))
    builder = cast(boundary.BuildAPI, boundary.upstream_module(upstream, "graphify.build"))
    exporter_module = boundary.upstream_module(upstream, "graphify.export")
    exporter = cast(boundary.ExportAPI, exporter_module)
    loader = cast(boundary.PathsAPI, boundary.upstream_module(upstream, "graphify.paths"))
    query = cast(boundary.QueryAPI, boundary.upstream_module(upstream, "graphify.serve"))
    validator = cast(boundary.ValidateAPI, boundary.upstream_module(upstream, "graphify.validate"))
    upstream_evidence["entrypoint_sha256"] = {
        relative: sha(upstream / relative)
        for relative in (
            "graphify/build.py", "graphify/export.py", "graphify/paths.py",
            "graphify/serve.py", "graphify/validate.py", "graphify/exporters/html.py",
        )
    }
    model = ac.validate(read_object(paths["model"]))
    carrier = ac.GraphCarrier(read_object(paths["carrier"]))
    require(ac.model_identity(model) == manifest["model"], "artifact model identity differs")
    require(ac.digest(carrier.document) == manifest["carrier_sha256"], "artifact semantic carrier digest differs")
    require(ac.decode(carrier).document == model.document, "source carrier does not recover complete exact model")
    proposal = ac.extraction(carrier)
    errors = validator.validate_extraction(cast(dict[str, object], copy.deepcopy(proposal)))
    require(not errors, f"actual upstream schema errors: {errors[:4]}")
    expected_nodes = {
        ac.string(ac.obj(node, "node")["id"], "node id")
        for node in ac.seq(proposal["nodes"], "nodes")
    }
    expected_edges = len(ac.seq(proposal["edges"], "edges"))
    before_build = time.perf_counter()
    built = builder.build_from_json(cast(dict[str, object], copy.deepcopy(proposal)), dedup=False)
    require(set(built.nodes) == expected_nodes, "upstream builder changed node identities")
    require(built.number_of_edges() == expected_edges, "upstream builder changed occurrence edge count")
    build_seconds = time.perf_counter() - before_build
    graph_out = (args.graph_out or AC_ROOT / "graphify-out" / "v3-i5" / args.tenant / "graph.json").resolve()
    html_out = graph_out.with_suffix(".html")
    input_paths = {path.resolve() for path in paths.values()}
    require(graph_out not in input_paths and html_out not in input_paths, "output aliases an unchanged source")
    require(not graph_out.exists(), "choose a fresh --graph-out; output already exists")
    require(args.html == "none" or not html_out.exists(), "HTML output already exists")
    graph_out.parent.mkdir(parents=True, exist_ok=True)
    require(
        exporter.to_json(built, {}, str(graph_out), built_at_commit=boundary.UPSTREAM_COMMIT),
        "actual exporter declined fresh output",
    )
    del built
    persisted = read_object(graph_out)
    require(ac.decode(ac.GraphCarrier(persisted)).document == model.document, "actual build/export/decode changed complete model")
    loaded = cast(ViewGraph, loader.load_node_link_graph(graph_out))
    require(set(loaded.nodes) == expected_nodes, "actual loader changed node identities")
    require(loaded.number_of_edges() == expected_edges, "actual loader changed occurrence edge count")
    record_node = next(
        ac.obj(raw, "record node") for raw in ac.seq(carrier.document["nodes"], "nodes")
        if ac.obj(raw, "node")["ac_role"] == "record"
        and ac.obj(ac.obj(ac.obj(raw, "node")["ac_payload"], "payload")["record"], "record")["id"] == expected_identity
    )
    record_id = ac.string(record_node["id"], "record node id")
    require(query_text.lower() in json.dumps(model.records[expected_identity].fields, ensure_ascii=False).lower(), "query does not occur in authored record")
    discovery_text = query._query_graph_text(loaded, query_text, depth=0, token_budget=2000, graph_path=str(graph_out))
    require(
        any(line.startswith("NODE ") and expected_identity in line for line in discovery_text.splitlines()),
        "unseeded actual Graphify search did not retrieve expected authored record",
    )
    seeded_text = query._query_graph_text(loaded, query_text, depth=2, token_budget=2000, graph_path=str(graph_out), seeds=[record_id])
    require("Traversal: BFS" in seeded_text and "NODE " in seeded_text and expected_identity in seeded_text, "seeded actual query failed")
    view = visual_export(cast(HtmlAPI, exporter_module), loaded, persisted, record_id, html_out, mode=args.html, depth=args.view_depth, budget=args.view_nodes)
    del loaded
    tamper_checks = tamper_trials(persisted)
    require(all(sha(path) == source_hashes[name] for name, path in paths.items()), "source changed during actual-upstream trial")
    boundary.verify_upstream(upstream)
    return {
        "status": "passed", "tenant": args.tenant,
        "claim": "bounded actual-upstream representation compatibility; no v3 semantic acceptance, calculus admission or efficiency claim",
        "upstream": upstream_evidence,
        "sources": {name: {"path": str(path), "sha256": source_hashes[name], "bytes": path.stat().st_size} for name, path in paths.items()},
        "model_identity": ac.model_identity(model), "carrier_identity": ac.carrier_identity(carrier),
        "family_counts": {family: sum(record.family == family for record in model.records.values()) for family in ac.CORE_FIELDS},
        "nodes": len(expected_nodes), "edges": expected_edges,
        "checks": [
            "actual upstream validates extraction",
            "dedup=False actual builder preserves every node identity and occurrence edge",
            "actual exporter/loader preserve every node identity and edge count",
            "decoder recovers complete exact model after actual upstream processing",
            "unseeded depth-zero native search retrieves expected authored wording",
            "exact seed resolves and renders bounded native graph context",
        ],
        "tamper_checks": tamper_checks,
        "exported_graph": {"path": str(graph_out), "sha256": sha(graph_out), "bytes": graph_out.stat().st_size},
        "visualization": view,
        "observations": {"build_seconds": round(build_seconds, 3), "total_seconds": round(time.perf_counter() - started, 3), "python": sys.version.split()[0]},
        "native_discovery": {"query": query_text, "expected_record": expected_identity, "depth": 0, "explicit_seeds": False, "token_budget": 2000, "text": discovery_text, "claim": "bounded keyword retrieval only; not governing acquisition"},
        "seeded_query": {"seed": record_id, "depth": 2, "token_budget": 2000, "text": seeded_text, "claim": "bounded structural context; not governing acquisition"},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tenant", required=True, choices=("codex", "claude"))
    parser.add_argument("--upstream", required=True, type=Path)
    parser.add_argument("--graph-out", type=Path, help="fresh actual-export output; defaults to ignored graphify-out/v3-i5/TENANT/graph.json")
    parser.add_argument("--out", type=Path, help="report; defaults to consumer evidence/native-graphify.json")
    parser.add_argument("--html", choices=("bounded", "full", "none"), default="bounded")
    parser.add_argument("--view-depth", type=int, default=3, help="bounded visual discovery radius, unrelated to governing acquisition")
    parser.add_argument("--view-nodes", type=int, default=500, help="bounded visual discovery display budget")
    args = parser.parse_args()
    report_out = args.out or AC_ROOT / "dogfood" / f"stdo-v3-i5-{args.tenant}" / "evidence" / "native-graphify.json"
    protected = list(source_paths(AC_ROOT / "dogfood" / f"stdo-v3-i5-{args.tenant}").values())
    graph_out = (args.graph_out or AC_ROOT / "graphify-out" / "v3-i5" / args.tenant / "graph.json").resolve()
    if any(aliases(report_out, path) for path in [*protected, graph_out, graph_out.with_suffix(".html")]):
        print(json.dumps({"status": "refusal", "error": "report output aliases an unchanged source or graph output"}), file=sys.stderr)
        return 2
    try:
        result = qualification(args)
        code = 0
    except Exception as exc:
        result = {"status": "failed", "tenant": args.tenant, "error": f"{type(exc).__name__}: {exc}"}
        code = 1
    write_report(report_out, result)
    print(json.dumps({"status": result["status"], "report": str(report_out), **({"error": result["error"]} if "error" in result else {})}))
    return code


if __name__ == "__main__":
    raise SystemExit(main())

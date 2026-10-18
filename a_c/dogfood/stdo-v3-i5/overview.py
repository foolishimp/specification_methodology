#!/usr/bin/env python3
"""Render readable, explicitly derived record-discovery views with Graphify.

The complete reversible carriers remain in the separate consumer artifacts.
This display collapses occurrence plumbing and omits selector/envelope nodes.
It preserves the direction and kinds of the displayed authored references;
parallel occurrences are counted, not presented as separate display edges.
"""
from __future__ import annotations

import argparse
from collections import deque
import html
import importlib
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
AC_ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(AC_ROOT / "build_tenants/graphify/test_env"))
import v3_graphify as transport  # noqa: E402
import check_upstream as boundary  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--upstream", required=True, type=Path)
    parser.add_argument("--nodes", type=int, default=100)
    args = parser.parse_args()
    transport.ac.require(args.nodes > 0, "display budget must be positive")
    upstream = args.upstream.resolve()
    upstream_pin = boundary.verify_upstream(upstream)
    sys.path.insert(0, str(upstream))
    import networkx as nx
    export = importlib.import_module("graphify.export")
    paths = importlib.import_module("graphify.paths")
    reports = []
    for tenant in ("claude", "codex"):
        subject, model, manifest = transport.load_representation(tenant)
        graph = nx.DiGraph()
        for identity, record in model.records.items():
            value = record.fields["value"]
            family = value["native_family"]
            if family in ("envelope", "frame_indexes"):
                continue
            native = transport.parse(value["native_json"])
            if family == "source_members":
                label = "Source: " + Path(native["path"]).name
                source = native["path"]
            elif family == "symbols":
                label = native["label"]
                source = "\n".join(native["source_refs"])
            elif family == "residuals":
                label = "Residual: " + native["detail"][:85]
                source = "\n".join(native["source_refs"])
            else:
                label = identity.split(":clause:")[-1].replace("_", " ").replace(".", ": ", 1).replace("-", " ")
                source = "\n".join(native["source_refs"])
            graph.add_node(identity, label=label, file_type="document", source_file=source,
                           attributes=dict(native_family=family, exact_identity=identity,
                                           authored_excerpt=value["a_text"][:2000],
                                           scope="derived discovery record; full payload in reversible carrier"))
        def connect(source, target, kind, origin):
            if source not in graph or target not in graph:
                return
            if not graph.has_edge(source, target):
                graph.add_edge(source, target, relation=kind, confidence="EXTRACTED",
                               source_file="a_c://authored-reference-occurrences", occurrences=[])
            edge = graph[source][target]
            edge["occurrences"].append(dict(kind=kind, coordinate=origin))
            edge["relation"] = ", ".join(sorted({row["kind"] for row in edge["occurrences"]}))
        for identity, record in model.records.items():
            value = record.fields["value"]
            for field, prefix in (("required_refs", "required:"), ("non_governing_refs", "discovery:")):
                for occurrence in value[field]:
                    connect(identity, occurrence["target"], prefix + occurrence["kind"],
                            occurrence["origin"] + "#" + occurrence["pointer"])
            for route in value["routes"]:
                authored = transport.parse(route["payload"])
                for target in route["targets"]:
                    connect(identity, target, "route:" + authored["acquisition"],
                            identity + "#/arguments/" + str(route["ordinal"]))
        full_json = HERE / (tenant + "-records.json")
        transport.ac.require(not full_json.exists(), "overview output must be fresh")
        transport.ac.require(export.to_json(graph, {}, str(full_json), built_at_commit=upstream_pin["commit"]), "record export failed")
        loaded = paths.load_node_link_graph(full_json)
        transport.ac.require(set(loaded.nodes) == set(graph.nodes) and loaded.number_of_edges() == graph.number_of_edges(), "record overview export lost identities/edges")
        seed = subject.config["discovery_record"]
        distances = {seed: 0}
        pending = deque([seed])
        while pending:
            current = pending.popleft()
            if distances[current] == 2:
                continue
            for target in sorted(set(graph.predecessors(current)) | set(graph.successors(current))):
                if target not in distances:
                    distances[target] = distances[current] + 1
                    pending.append(target)
        selected = sorted(distances, key=lambda key: (distances[key], key))[:args.nodes]
        view = graph.subgraph(selected).copy()
        kinds = sorted({graph.nodes[key]["attributes"]["native_family"] for key in selected})
        communities = {i: [key for key in selected if graph.nodes[key]["attributes"]["native_family"] == kind] for i, kind in enumerate(kinds)}
        labels = {i: kind.replace("_", " ").title() for i, kind in enumerate(kinds)}
        output = HERE / (tenant + ".html")
        transport.ac.require(not output.exists(), "overview HTML output must be fresh")
        transport.ac.require(export.to_html(view, communities, str(output), community_labels=labels,
                                          node_limit=len(selected), learning_overlay={}), "record HTML export failed")
        scope = (f"{tenant.title()} · {len(selected)} of {len(distances)} records within two hops · "
                 f"{graph.number_of_nodes()} records in complete discovery graph · package {manifest['package_commit'][:8]}. "
                 "Search or click records. Use the CLI for required acquisition.")
        banner = '<div id="record-view-scope" style="position:fixed;top:10px;left:10px;z-index:10;max-width:calc(100% - 340px);padding:10px;background:#1f2937;color:#fff;border-radius:6px;font:13px/1.5 system-ui">' + html.escape(scope) + '</div>'
        rendered = output.read_text()
        transport.ac.require('<div id="graph"></div>' in rendered, "unexpected official HTML structure")
        output.write_text(rendered.replace('<div id="graph"></div>', banner + '<div id="graph"></div>', 1))
        reports.append(dict(tenant=tenant, input_model=manifest["model"], input_manifest_sha256=subject.config["input_manifest_sha256"],
                            records=graph.number_of_nodes(), edges=graph.number_of_edges(),
                            candidate_records=len(distances), displayed_records=len(selected), omitted_records_within_radius=len(distances)-len(selected),
                            seed=seed, radius=2, claim="derived record discovery only; parallel occurrences counted; selectors/envelope excluded; no added semantic coverage",
                            outputs={p.name: dict(sha256=transport.sha(p.read_bytes()), bytes=p.stat().st_size) for p in (full_json, output)}))
        print(tenant, "record view", len(selected), "of", graph.number_of_nodes(), flush=True)
    boundary.verify_upstream(upstream)
    (HERE / "evidence/overview.json").write_bytes(transport.pretty(dict(status="passed", upstream=upstream_pin,
         builder_sha256=transport.sha(Path(__file__).read_bytes()), views=reports)))


if __name__ == "__main__":
    main()

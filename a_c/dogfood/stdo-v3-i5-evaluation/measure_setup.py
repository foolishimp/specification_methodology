#!/usr/bin/env python3
"""Measure a fresh, fully preserved transport build, not semantic authoring.

Use the existing a_c qualification environment. Outputs are study evidence;
the original consumer artifacts and the upstream checkout remain unchanged.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))
import v3_graphify as v3
sys.path.insert(0, str(ROOT.parents[1] / "build_tenants/graphify/test_env"))
import check_upstream as boundary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--upstream", type=Path, required=True)
    parser.add_argument("--out", type=Path, default=ROOT / "evidence/graph-setup.json")
    args = parser.parse_args()
    upstream = args.upstream.resolve()
    verified = boundary.verify_upstream(upstream)
    sys.path.insert(0, str(upstream))
    started = time.perf_counter()
    build = boundary.upstream_module(upstream, "graphify.build")
    export = boundary.upstream_module(upstream, "graphify.export")
    loader = boundary.upstream_module(upstream, "graphify.paths")
    import_seconds = time.perf_counter() - started
    results = []
    for tenant in ("codex", "claude"):
        stages = {}
        def stage(name, operation):
            started = time.perf_counter()
            value = operation()
            stages[name] = round(time.perf_counter() - started, 6)
            return value
        subject = stage("verify_frozen_source_seconds", lambda: v3.load_subject(tenant))
        model = stage("construct_and_validate_model_seconds", lambda: v3.build_model(subject))
        carrier = stage("materialize_codec_seconds", lambda: v3.ac.materialize(model))
        graph = stage("upstream_build_seconds", lambda: build.build_from_json(carrier.document, dedup=False, directed=False))
        with tempfile.TemporaryDirectory(prefix="ac-eval-setup-") as temporary:
            target = Path(temporary) / "graph.json"
            stage("upstream_export_seconds", lambda: export.to_json(graph, {}, str(target), built_at_commit=boundary.UPSTREAM_COMMIT))
            loaded = stage("upstream_reload_seconds", lambda: loader.load_node_link_graph(target))
            raw = target.read_bytes()
            compressed = stage("compress_export_seconds", lambda: gzip.compress(raw, mtime=0))
            counts = dict(nodes=loaded.number_of_nodes(), edges=loaded.number_of_edges())
            expected = json.loads((subject.root / "artifacts/manifest.json").read_bytes())["counts"]
            if counts != dict(nodes=expected["graph_nodes"], edges=expected["graph_edges"]):
                raise ValueError("upstream graph counts differ")
            results.append(dict(tenant=tenant, stages=stages, counts=counts,
                                full_export_bytes=len(raw), gzip_export_bytes=len(compressed),
                                source_manifest_sha256=subject.config["input_manifest_sha256"],
                                native_program_bytes=len(subject.members[subject.config["program_path"]]),
                                graph_scope="Full already-qualified T003 transport, including historical source files excluded from actor discovery. Actor filtering/loading is separately metered per run.",
                                preserved_node_and_edge_counts=True))
        print(json.dumps(dict(tenant=tenant, completed=True, stages=stages)), flush=True)
    evidence = dict(profile="ac.eval.graph-setup/1", upstream=verified,
                    import_seconds=round(import_seconds,6), results=results,
                    script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                    limits=["One local build measurement; not a throughput estimate.",
                            "Common historical LLM/F_P authoring and validation costs are not measured or attributed to either arm.",
                            "Full original transport preparation cost is separate from the actor's filtered discovery-view startup."])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    if args.out.exists():
        raise ValueError("setup evidence already exists; choose a new output")
    args.out.write_text(json.dumps(evidence, sort_keys=True, indent=2)+"\n")


if __name__ == "__main__":
    main()

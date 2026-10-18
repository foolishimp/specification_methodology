#!/usr/bin/env python3
"""Reproduce the actual Graphify boundary trial on the frozen v3 transport.

This qualification helper uses the tenant's pinned-upstream checks, but does
not impose the toy conformance fixture's nonempty-family requirements on an
authored corpus. Upstream packages are qualification-only dependencies.
"""

from __future__ import annotations

import argparse
import copy
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time
from typing import cast


AC_ROOT = Path(__file__).resolve().parents[3]
TENANT = AC_ROOT / "build_tenants" / "graphify"
sys.path.insert(0, str(TENANT / "code"))
sys.path.insert(0, str(TENANT / "test_env"))

import ac_graph as ac
import check_upstream as boundary


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


def tamper_trials(persisted: ac.Object) -> list[str]:
    checks: list[str] = []
    for trial in ("missing-occurrence", "reversed-occurrence", "search-identity", "directed-profile"):
        changed = copy.deepcopy(persisted)
        nodes = [ac.obj(v, "node") for v in ac.seq(changed["nodes"], "nodes")]
        if trial == "missing-occurrence":
            victim = next(n for n in nodes if n["ac_role"] == "reference-occurrence")["id"]
            changed["nodes"] = [n for n in ac.seq(changed["nodes"], "nodes") if ac.obj(n, "node")["id"] != victim]
            changed["links"] = [
                e for e in ac.seq(changed["links"], "links")
                if ac.obj(e, "edge")["source"] != victim and ac.obj(e, "edge")["target"] != victim
            ]
        elif trial == "reversed-occurrence":
            occurrence = next(
                ac.obj(n["ac_payload"], "occurrence") for n in nodes
                if n["ac_role"] == "reference-occurrence"
                and ac.obj(n["ac_payload"], "occurrence")["owner"] != ac.obj(n["ac_payload"], "occurrence")["target"]
            )
            occurrence["owner"], occurrence["target"] = occurrence["target"], occurrence["owner"]
        elif trial == "search-identity":
            record = next(n for n in nodes if n["ac_role"] == "record")
            ac.obj(record["attributes"], "attributes")["semantic_identity"] = "urn:trial:misleading-identity"
        else:
            changed["directed"] = True
        try:
            ac.decode(ac.GraphCarrier(changed))
        except ac.Refusal:
            checks.append(trial + " refused after actual upstream export")
        else:
            raise boundary.QualificationError(f"decoder accepted {trial}")
    return checks


def qualification(args: argparse.Namespace) -> dict[str, object]:
    started = time.perf_counter()
    source_paths = {
        "model": args.model.resolve(),
        "carrier": args.carrier.resolve(),
        "artifact_manifest": args.model.resolve().parent / "manifest.json",
        "consumer_builder": Path(__file__).resolve().parents[1] / "representation.py",
        "codec": TENANT / "code" / "ac_graph.py",
        "boundary_helper": TENANT / "test_env" / "check_upstream.py",
        "trial_helper": Path(__file__).resolve(),
    }
    source_hashes = {k: sha(v) for k, v in source_paths.items()}
    upstream = args.upstream.resolve()
    upstream_evidence = boundary.verify_upstream(upstream)
    sys.path.insert(0, str(upstream))
    builder = cast(boundary.BuildAPI, boundary.upstream_module(upstream, "graphify.build"))
    exporter = cast(boundary.ExportAPI, boundary.upstream_module(upstream, "graphify.export"))
    loader = cast(boundary.PathsAPI, boundary.upstream_module(upstream, "graphify.paths"))
    query = cast(boundary.QueryAPI, boundary.upstream_module(upstream, "graphify.serve"))
    validator = cast(boundary.ValidateAPI, boundary.upstream_module(upstream, "graphify.validate"))
    upstream_evidence["entrypoint_sha256"] = {
        f"graphify/{name}.py": sha(upstream / "graphify" / f"{name}.py")
        for name in ("build", "export", "paths", "serve", "validate")
    }
    model = ac.validate(read_object(args.model))
    carrier = ac.GraphCarrier(read_object(args.carrier))
    require(ac.decode(carrier).document == model.document, "source graph does not recover exact model")
    proposal = ac.extraction(carrier)
    errors = validator.validate_extraction(cast(dict[str, object], copy.deepcopy(proposal)))
    require(not errors, f"actual upstream schema errors: {errors[:4]}")
    expected_nodes = {
        ac.string(ac.obj(n, "node")["id"], "node id")
        for n in ac.seq(proposal["nodes"], "nodes")
    }
    expected_edges = len(ac.seq(proposal["edges"], "edges"))
    before_build = time.perf_counter()
    built = builder.build_from_json(cast(dict[str, object], copy.deepcopy(proposal)), dedup=False)
    require(set(built.nodes) == expected_nodes, "upstream builder changed node identities")
    require(built.number_of_edges() == expected_edges, "upstream builder changed occurrence edges")
    build_seconds = time.perf_counter() - before_build
    graph_out = args.graph_out.resolve()
    require(not graph_out.exists(), "choose a fresh --graph-out; output already exists")
    graph_out.parent.mkdir(parents=True, exist_ok=True)
    require(
        exporter.to_json(built, {}, str(graph_out), built_at_commit=boundary.UPSTREAM_COMMIT),
        "actual exporter refused fresh output",
    )
    del built
    persisted = read_object(graph_out)
    recovered = ac.decode(ac.GraphCarrier(persisted))
    require(recovered.document == model.document, "actual build/export/decode changed the complete model")
    loaded = loader.load_node_link_graph(graph_out)
    require(set(loaded.nodes) == expected_nodes, "actual loader changed node identities")
    require(loaded.number_of_edges() == expected_edges, "actual loader changed edge count")
    record_node = next(
        ac.obj(n, "node") for n in ac.seq(carrier.document["nodes"], "nodes")
        if ac.obj(n, "node")["ac_role"] == "record"
        and ac.obj(ac.obj(ac.obj(n, "node")["ac_payload"], "payload")["record"], "record")["id"] == args.expect_record
    )
    record_id = ac.string(record_node["id"], "record node id")
    expected_record = model.records[args.expect_record].fields
    require(args.query.lower() in json.dumps(expected_record, ensure_ascii=False).lower(), "query not in authored record")
    discovery_text = query._query_graph_text(
        loaded, args.query, depth=0, token_budget=2000, graph_path=str(graph_out)
    )
    require(
        any(line.startswith("NODE ") and args.expect_record in line for line in discovery_text.splitlines()),
        "unseeded actual Graphify search did not retrieve expected authored record",
    )
    seeded_text = query._query_graph_text(
        loaded, args.query, depth=2, token_budget=2000,
        graph_path=str(graph_out), seeds=[record_id],
    )
    require("Traversal: BFS" in seeded_text and "NODE " in seeded_text and args.expect_record in seeded_text, "seeded query failed")
    del loaded
    checks = [
        "actual upstream validates extraction",
        "dedup=False builder preserves every node identity and occurrence edge",
        "actual exporter/loader preserve every node identity and edge count",
        "decoder recovers complete exact model after actual upstream processing",
        "unseeded depth-zero native search retrieves expected authored wording",
        "exact seed resolves and renders bounded native graph context",
        *tamper_trials(persisted),
    ]
    require(all(sha(v) == source_hashes[k] for k, v in source_paths.items()), "source changed during trial")
    boundary.verify_upstream(upstream)
    return {
        "status": "passed",
        "claim": "bounded actual-upstream corpus compatibility; no v3 acceptance, calculus admission or efficiency claim",
        "upstream": upstream_evidence,
        "sources": {k: {"path": str(v), "sha256": source_hashes[k], "bytes": v.stat().st_size} for k, v in source_paths.items()},
        "model_identity": ac.model_identity(model),
        "carrier_identity": ac.carrier_identity(carrier),
        "family_counts": {family: sum(r.family == family for r in model.records.values()) for family in ac.CORE_FIELDS},
        "nodes": len(expected_nodes), "edges": expected_edges,
        "checks": checks,
        "exported_graph": {"path": str(graph_out), "sha256": sha(graph_out), "bytes": graph_out.stat().st_size},
        "observations": {"build_seconds": round(build_seconds, 3), "total_seconds": round(time.perf_counter() - started, 3), "python": sys.version.split()[0]},
        "native_discovery": {
            "query": args.query, "expected_record": args.expect_record,
            "depth": 0, "explicit_seeds": False, "token_budget": 2000,
            "text": discovery_text,
            "claim": "bounded keyword retrieval only; this is not governing acquisition",
        },
        "seeded_query": {"depth": 2, "token_budget": 2000, "text": seeded_text},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--upstream", required=True, type=Path)
    parser.add_argument("--model", required=True, type=Path)
    parser.add_argument("--carrier", required=True, type=Path)
    parser.add_argument("--graph-out", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--query", default="Every admitted fundamental record")
    parser.add_argument("--expect-record", default="urn:codex-stdo3:iteration-3-r2:clause:AXIOMATIC_CALCULUS.ac-001-closed-signature")
    args = parser.parse_args()
    try:
        result = qualification(args)
        code = 0
    except Exception as exc:
        result = {"status": "failed", "error": f"{type(exc).__name__}: {exc}"}
        code = 1
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "report": str(args.out), **({"error": result["error"]} if "error" in result else {})}))
    return code


if __name__ == "__main__":
    raise SystemExit(main())

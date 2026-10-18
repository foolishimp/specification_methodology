#!/usr/bin/env python3
"""Index and verify the eight frozen inputs for later performance tests."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[2]
OLDER = ROOT.with_name("stdo-v3-generation")
sys.path.insert(0, str(ROOT.parents[1] / "build_tenants/graphify/code"))
import ac_graph


def load(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def relative(path):
    return str(path.relative_to(REPO))


def verify_sources(manifest, directory):
    members = manifest["files"]
    require(len(members) == manifest["file_count"], "source file count differs")
    require(sum(m["bytes"] for m in members) == manifest["total_bytes"], "source byte count differs")
    paths = [m["path"] for m in members]
    require(len(set(paths)) == len(paths), "duplicate source member")
    actual = {str(p.relative_to(directory)) for p in directory.rglob("*") if p.is_file()}
    require(actual == set(paths), "indexed source member set differs")
    for member in members:
        path = directory / member["path"]
        require(path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(directory.resolve()), "unsafe source member")
        require(path.stat().st_size == member["bytes"] and sha(path) == member["sha256"], "source bytes changed: " + str(path))
    raw = json.dumps(members, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    require(hashlib.sha256(raw).hexdigest() == manifest["input_corpus_sha256"], "source inventory digest differs")
    return [{k: member[k] for k in ("path", "sha256", "bytes")} for member in members]


def build():
    delta = load(ROOT / "evidence/source-delta.json")
    cells = []
    implementation = None
    actor_settings = None
    for period, study in (("older", OLDER), ("newer", ROOT)):
        results = load(study / "results.json")
        rows = {(r["candidate"], r["mode"]): r for r in results["runs"]}
        require(len(rows) == len(results["runs"]) == 4, "four unique runs required")
        for candidate in ("codex", "claude"):
            manifest_path = study / "corpora" / candidate / "manifest.json"
            manifest = load(manifest_path)
            selected_files = verify_sources(manifest, manifest_path.parent / "source")
            for mode in ("graphify-ac", "direct"):
                run = rows[(candidate, mode)]
                require(run["state"] == "proposed", "unfinished run")
                proposal = run["proposal"]
                require(proposal["status"] == "proposed" and proposal["processing_complete"], "complete proposal required")
                require(all(a["status"] != "in_progress_or_interrupted" for a in run["attempts"]), "unfinished actor")
                out = study / run["proposal_path"]
                require(load(out / "result.json") == proposal, "proposal result differs from summary")
                plan_path = out.parent / "plan.json"
                plan = load(plan_path)
                settings = load(out.parent / "actor-settings.json")
                actor_settings = settings if actor_settings is None else actor_settings
                require(settings == actor_settings, "old/new actor settings or CLI differ")
                require(sha(plan_path) == run["plan_sha256"], "plan identity changed")
                require(plan["subject_id"] == run["subject"] == manifest["subject_id"], "subject mismatch")
                retained_manifest = out.parent / "source-manifest.json"
                require(plan["source_manifest_sha256"] == sha(retained_manifest), "retained source manifest changed")
                require(load(retained_manifest) == manifest, "retained and corpus manifests differ")
                require(plan["files"] == selected_files, "plan source inventory differs")
                verify_sources(manifest, out.parent / "corpus")
                pins = {key: plan[key] for key in ("runner_sha256", "codec_sha256", "assets", "calculus", "chunk_chars", "graph_chars")}
                implementation = pins if implementation is None else implementation
                require(pins == implementation, "old/new implementation or settings differ")
                artifacts = {}
                for name, expected in proposal["files"].items():
                    path = out / name
                    require(sha(path) == expected, "proposal file changed: " + str(path))
                    artifacts[name] = {"path": relative(path), "file_sha256": expected, "bytes": path.stat().st_size}
                model = load(out / "model.json")
                require(ac_graph.digest(model) == proposal["model_sha256"], "model canonical digest changed")
                require({k: len(v) for k, v in model["populations"].items()} == proposal["family_counts"], "family counts changed")
                basis = model["basis"]
                require(basis["calculus"] == plan["calculus"], "model calculus basis differs")
                require(basis["subject"]["id"] == plan["subject_id"], "model source subject differs")
                require(basis["subject"]["sha256"] == ac_graph.digest(plan["files"]), "model source inventory digest differs")
                chunks_path = out.parent / "chunks.json"
                require(sha(chunks_path) == plan["chunks_sha256"], "source chunks changed")
                inventory = [{"id": s["id"], "sha256": s["sha256"]} for c in load(chunks_path) for s in c["segments"]]
                require(basis["subject"]["inventory"] == inventory, "model source section inventory differs")
                stages = dict(Counter(a["stage"] for a in run["attempts"]))
                cells.append({
                    "cell": "-".join((period, candidate, mode)), "period": period,
                    "candidate": candidate, "mode": mode,
                    "semantic_extraction_profile": plan["semantic_extraction_profile"],
                    "candidate_version": manifest["candidate_version"],
                    "revision": manifest["revision"], "custody_checkpoint": manifest["checkpoint"],
                    "subject_id": manifest["subject_id"],
                    "source_manifest": {"path": relative(manifest_path), "file_sha256": sha(manifest_path)},
                    "source_directory": relative(manifest_path.parent / "source"),
                    "source_files": manifest["file_count"], "source_bytes": manifest["total_bytes"],
                    "input_corpus_sha256": manifest["input_corpus_sha256"],
                    "content_inventory_sha256": manifest["content_inventory_sha256"],
                    "planned_chunks": run["planned_chunks"],
                    "plan": {"path": relative(plan_path), "file_sha256": sha(plan_path)},
                    "model_canonical_sha256": proposal["model_sha256"],
                    "artifacts": artifacts, "family_counts": proposal["family_counts"],
                    "build_resources": {
                        "attempt_count": run["attempt_count"], "calls_by_stage": stages,
                        "attempts_without_usage": run["attempts_without_usage"],
                        "reported_usage_totals": run["reported_usage_totals"],
                        "sum_recorded_actor_seconds": run["sum_recorded_actor_seconds"],
                        "fd_discovery_seconds": run["discovery"]["elapsed_seconds"] if run["discovery"] else None,
                        "fd_assembly_seconds": proposal["fd_assembly_elapsed_seconds"],
                    },
                    "results": {"path": relative(study / "results.json"), "file_sha256": sha(study / "results.json")},
                    "semantic_assessment": "Older bounded source-fidelity assessment only; see its retained scope." if period == "older" else "Not performed for this rebuild; no inherited old grades.",
                    "comparison_tests": "not run",
                })
    for candidate in ("codex", "claude"):
        candidate_cells = [c for c in cells if c["candidate"] == candidate]
        for period in ("older", "newer"):
            paired = [c for c in candidate_cells if c["period"] == period]
            require(paired[0]["input_corpus_sha256"] == paired[1]["input_corpus_sha256"], "paired source input differs")
        older, newer = candidate_cells[0], candidate_cells[2]
        same = older["content_inventory_sha256"] == newer["content_inventory_sha256"]
        require(same == delta["subjects"][candidate]["source_content_identical"], "source delta mismatch")
    return {
        "profile": "ac.generation.comparison-inputs/1",
        "older_checkpoint": "efae9c749275838029a871863f0b3ce7d7aba8b6",
        "operating_basis": "STDO v2.5.1-rc.2; V3 candidates are subject data.",
        "implementation": implementation,
        "actor_settings": actor_settings,
        "cells": cells,
        "source_delta": {"path": relative(ROOT / "evidence/source-delta.json"), "file_sha256": sha(ROOT / "evidence/source-delta.json")},
        "comparison_tests": "not run",
        "limits": [
            "Codex newer source bytes equal older source bytes; subject coordinates and fresh generation differ.",
            "Claude changes two selected owner files and some chunk boundaries; no single causal effect is isolated.",
            "All source actors use the same model and settings; Codex/Claude label source corpora, not model families.",
            "Build resources include retained failures and repairs; missing usage is unknown, not zero.",
            "Summed actor seconds are not concurrent wall time or total accepted-result cost; cache counters do not establish billing.",
            "Documentary grounding and carrier recovery do not establish semantic fidelity, operational conformance or acceptance.",
            "The descriptive profile has no authored traversals, transformations or judgments.",
            "One generation per cell and unequal cache histories support no general performance conclusion.",
        ],
    }


def markdown(data):
    lines = ["# Inputs for older/newer performance tests", "",
             "Eight complete representations are indexed in [`comparison.json`](comparison.json). "
             "The planned comparison tests have not been run.", "",
             "| Period | Source | Path | Model | Calls | Reported input tokens | Reported output tokens | Actor seconds |",
             "|---|---|---|---|---:|---:|---:|---:|"]
    for c in data["cells"]:
        b = c["build_resources"]
        usage = b["reported_usage_totals"]
        marker = "*" if b["attempts_without_usage"] else ""
        link = os.path.relpath(REPO / c["artifacts"]["model.json"]["path"], ROOT)
        value = lambda field: f"{usage[field]:,}{marker}" if usage[field] is not None else "unknown"
        lines.append(f"| {c['period']} | {c['candidate']} {c['candidate_version']} | {c['mode']} | [model]({link}) | {b['attempt_count']} | {value('input_tokens')} | {value('output_tokens')} | {b['sum_recorded_actor_seconds']:,.1f} |")
    missing = [f"{c['cell']} ({c['build_resources']['attempts_without_usage']} calls)" for c in data['cells'] if c['build_resources']['attempts_without_usage']]
    note = "*Unknown backend usage: " + ", ".join(missing) + ". Recorded elapsed time is included. Tokens shown are reported totals only." if missing else "All calls report backend usage; counters are not a billing formula."
    lines += ["", note, "",
              "Codex RC9 has the same selected source bytes as older RC5. Claude RC9 changes "
              "`ASSURANCE.md` and `FOUNDATIONS.md` (+761 bytes); its source partition also changes. "
              "The [source delta](evidence/source-delta.json) retains every selected member's identity.", "",
              "Use each cell's exact model and matching frozen source for tests. "
              "The index distinguishes the file digest from the model's canonical digest and retains "
              "the Graphify carrier/graph, source cut, build evidence and resource counters. "
              "The implementation and model settings are held constant across old/new builds.", "",
              "Old fidelity grades apply to old models only. New models have passed the build's "
              "mechanical checks and require their own semantic evaluation. "
              "The descriptive profile does not author traversals, transformations or judgments.", "",
              "These are build observations. Summed actor time, unknown usage, cache differences "
              "and one generation per cell prevent a general cost or quality conclusion. "
              "Later tests should use common tasks, version-appropriate source truth, identical "
              "execution limits and separately recorded correctness and resource results.", "",
              "Recheck all indexed artifact identities without model calls:", "",
              "```sh", "a_c/.venv/bin/python a_c/dogfood/stdo-v3-generation-rc9/build_comparison.py --check", "```", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = build()
    outputs = {"comparison.json": json.dumps(data, ensure_ascii=False, indent=2) + "\n", "COMPARISON.md": markdown(data)}
    for name, content in outputs.items():
        path = ROOT / name
        if args.check:
            require(path.read_text() == content, "index differs: " + name)
        else:
            path.open("x").write(content)
    print(json.dumps({"status": "verified" if args.check else "created", "cells": len(data["cells"]), "comparison_tests": "not run"}))


if __name__ == "__main__":
    main()

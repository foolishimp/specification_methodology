#!/usr/bin/env python3
"""Schedule selected exact chunks through the unchanged frozen author functions.

This is study orchestration, not a semantic compiler or recovery operation.
The explicit selection is retained before any call. Retries use the identical
frozen source/treatment prompt and never replace earlier attempts.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parent
CODE = ROOT.parents[1] / "build_tenants/graphify/code"
sys.path.insert(0, str(CODE))
import ac_generate as g

EXPECTED_SETTINGS = {
    "model": "gpt-6-astra", "model_reasoning_effort": "high",
    "service_tier": "default",
}
EXPECTED_RUNNER = "7002a7942f612f5a11e2a69dc865849ffef51c29c7b0cab9feb5170fb32d0479"
EXPECTED_CLI = "codex-cli 0.162.1"


def utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def context(item: dict) -> tuple[Path, dict, dict, list[Path], str]:
    g.require(set(item) == {"candidate", "mode", "chunk", "attempt"}, "selection shape")
    g.require(item["candidate"] in ("codex", "claude"), "unknown candidate")
    g.require(item["mode"] in ("direct", "graphify-ac"), "unknown treatment")
    output = ROOT / "runs-v2" / item["candidate"] / item["mode"]
    plan, chunks = g.checkpoint(output)
    g.require(plan["runner_sha256"] == EXPECTED_RUNNER, "different frozen runner")
    chunk = next((c for c in chunks if c["id"] == item["chunk"]), None)
    g.require(chunk is not None, "selection names unknown chunk")
    g.require(plan["mode"] == item["mode"], "treatment mismatch")
    if plan["mode"] in g.GRAPH_MODES:
        g.verify_discovery(output)
    fixed = g.load(output / "actor-settings.json")
    g.require(fixed == {"settings": EXPECTED_SETTINGS, "cli_version": EXPECTED_CLI}, "settings changed")
    root = output / "actors/author" / chunk["id"]
    attempts = sorted(root.glob("attempt-*")) if root.exists() else []
    g.require(isinstance(item["attempt"], int) and 1 <= item["attempt"] <= 3, "three-attempt ceiling")
    g.require([p.name for p in attempts] == [f"attempt-{i:03d}" for i in range(1, item["attempt"])], "attempt selection is stale or noncontiguous")
    g.require(all((p / "result.json").is_file() for p in attempts), "prior actor is still running or interrupted")
    g.require(g.successful_attempt(output, "author", chunk) is None, "strictly complete chunk must be reused")
    for p in attempts:
        g.require(g.load(p / "result.json")["status"] == "failed", "retry requires a retained failed attempt")
    return output, plan, chunk, attempts, g.author_prompt(plan, chunk, output)


def run_one(item: dict, journal: Path) -> dict:
    output, plan, chunk, attempts, prompt = context(item)
    attempt = output / "actors/author" / chunk["id"] / f"attempt-{item['attempt']:03d}"
    provenance = {
        "profile": "ac.generation.coordinated-author/1", "selection": item,
        "coordinator_sha256": g.sha(Path(__file__).read_bytes()),
        "coordinator_journal": str(journal.relative_to(ROOT)),
        "plan_sha256": g.sha((output / "plan.json").read_bytes()),
        "chunk_sha256": g.digest(chunk), "prompt_sha256": g.sha(prompt.encode()),
        "prompt_policy": "exact frozen author_prompt, including on a fresh retry",
        "prior_attempts": [{"path": str(p.relative_to(output)),
                            "result_sha256": g.sha((p / "result.json").read_bytes())}
                           for p in attempts],
    }
    print(json.dumps({"event": "started", "time": utc(), **item}), flush=True)
    result = g.run_actor(prompt, g.ASSETS / "author.schema.json", attempt,
                         "/Users/jim/bin/codex", 1200, EXPECTED_SETTINGS)
    g.require(result["cli_version"] == EXPECTED_CLI, "actor CLI changed")
    # Exactly the frozen stage's declared validation and failure semantics.
    if result["status"] == "completed":
        try:
            g.author_check(g.load(attempt / "answer.json"), chunk)
            g.save(attempt / "validation.json", {
                "status": "structurally_valid_proposal",
                "answer_sha256": g.sha((attempt / "answer.json").read_bytes()),
                "chunk_sha256": g.digest(chunk),
                "claim": "Source coordinates and declared shape checked; semantic fitness unassessed.",
            }, exclusive=True)
        except g.GenerationError as exc:
            result["status"] = "failed"
            result["failures"].append("source_or_semantic_fragment_validation")
            result["validation_error"] = str(exc)
            g.save(attempt / "result.json", result)
    g.save(attempt / "coordinator.json", provenance, exclusive=True)
    record = {"time": utc(), **item, "status": result["status"],
              "failures": result["failures"],
              "elapsed_seconds": result["elapsed_seconds"],
              "attempt_path": str(attempt.relative_to(ROOT)),
              "result_sha256": g.sha((attempt / "result.json").read_bytes())}
    g.save(journal / ("-".join(str(item[k]) for k in ("candidate", "mode", "chunk", "attempt")) + ".json"), record, exclusive=True)
    print(json.dumps({"event": "finished", **record}), flush=True)
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selection", type=Path, required=True)
    parser.add_argument("--journal", type=Path, required=True)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--jobs", type=int, default=4, choices=range(1, 5))
    args = parser.parse_args()
    args.selection = args.selection.resolve(strict=True)
    args.journal = args.journal.resolve()
    g.require(args.journal.is_relative_to(ROOT), "journal escapes study root")
    items = g.load(args.selection)
    g.require(isinstance(items, list) and items, "empty or invalid selection")
    g.require(len({(i["candidate"], i["mode"], i["chunk"]) for i in items}) == len(items), "duplicate chunk selection")
    # Whole selection preflight before effects or model calls.
    summaries = []
    for item in items:
        _, _, chunk, _, prompt = context(item)
        summaries.append({**item, "chunk_sha256": g.digest(chunk),
                          "prompt_sha256": g.sha(prompt.encode()),
                          "prompt_chars": len(prompt)})
    plan = {"profile": "ac.generation.coordinator-plan/1", "created_at": utc(),
            "coordinator_sha256": g.sha(Path(__file__).read_bytes()),
            "selection_sha256": g.sha(args.selection.read_bytes()),
            "runner_sha256": EXPECTED_RUNNER, "settings": EXPECTED_SETTINGS,
            "cli_version": EXPECTED_CLI, "timeout_seconds": 1200,
            "jobs": args.jobs, "selected": summaries,
            "claim": "Same frozen authoring algorithm; no grounding recovery or semantic assessment."}
    if not args.execute:
        print(json.dumps(plan, indent=2))
        return
    active = [str(p.parent.relative_to(ROOT))
              for p in (ROOT / "runs-v2").glob("*/*/actors/author/*/attempt-*/invocation.json")
              if not (p.parent / "result.json").exists()]
    g.require(not active, "prior actors are active or interrupted; do not exceed global call limit: " + repr(active))
    _, _, metadata = g.actor_settings("/Users/jim/bin/codex", EXPECTED_SETTINGS)
    g.require(metadata["settings"] == EXPECTED_SETTINGS and metadata["cli_version"] == EXPECTED_CLI, "live actor environment differs")
    g.require(not args.journal.exists(), "preserve existing coordinator journal")
    lock = ROOT / "evidence/generation-coordinator.lock"
    lock.mkdir()  # One coordinator; a stale lock requires explicit inspection.
    args.journal.mkdir(parents=True)
    g.save(args.journal / "plan.json", plan, exclusive=True)
    started = time.perf_counter()
    records, errors = [], []
    try:
        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            futures = {pool.submit(run_one, item, args.journal): item for item in items}
            for future in as_completed(futures):
                try:
                    records.append(future.result())
                except Exception as exc:
                    error = {"selection": futures[future], "error": str(exc), "time": utc()}
                    errors.append(error)
                    print(json.dumps({"event": "coordinator_error", **error}), flush=True)
    finally:
        lock.rmdir()
    g.save(args.journal / "result.json", {
        "profile": "ac.generation.coordinator-result/1", "finished_at": utc(),
        "elapsed_wall_seconds": time.perf_counter() - started,
        "attempts": records, "errors": errors,
        "claim": "Measured scheduling and strict checks only; draft interpretation fidelity unassessed.",
    }, exclusive=True)
    raise SystemExit(1 if errors or any(r["status"] == "failed" for r in records) else 0)


if __name__ == "__main__":
    main()

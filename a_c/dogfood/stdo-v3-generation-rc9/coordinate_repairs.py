#!/usr/bin/env python3
"""Schedule explicit conditional F_P repairs after original authoring closes."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[2]
sys.path.insert(0, str(ROOT.parents[1] / "build_tenants/graphify/code"))
import ac_generate as g
import ac_grounding as h
import ac_repair as r


def utc():
    return datetime.now(timezone.utc).isoformat()


def check_item(item):
    required = {"candidate", "mode", "chunk"}
    g.require(required <= set(item) <= required | {"parent_repair", "prepared_attempt"}, "repair selection shape")
    g.require(item["candidate"] in ("codex", "claude") and item["mode"] in ("graphify-ac", "direct"), "unknown repair subject/treatment")
    g.require(not (item.get("parent_repair") and item.get("prepared_attempt")), "choose a parent or an existing reservation")
    output = ROOT / "runs-v2" / item["candidate"] / item["mode"]
    plan, chunk = r.choose_chunk(output, item["chunk"])
    inventory = r.call_inventory(output, item["chunk"])
    if item.get("prepared_attempt"):
        attempt = r.safe_attempt(output, Path(item["prepared_attempt"]))
        request, _, selected, _ = r.verify_request(output, attempt)
        g.require(selected["id"] == item["chunk"] and request["mode"] == item["mode"], "reservation differs from selected chunk/treatment")
        g.require(not (attempt / "actor").exists() and not (attempt / "journal.json").exists(), "reservation already started")
        return output, {"selection": item, "reserved_attempt": str(attempt.relative_to(output)), "inventory": inventory}
    g.require(len(inventory) < r.LIMIT, "shared three-call limit exhausted")
    if item.get("parent_repair"):
        parent_path = r.safe_attempt(output, Path(item["parent_repair"]))
        g.require(parent_path.parent.name == item["chunk"], "repair parent belongs to another chunk")
        parent = {"kind": "repair", "path": str(parent_path.relative_to(output))}
    else:
        parent_path = h.latest_attempt(output, chunk)
        g.require(parent_path is not None, "original parent is missing")
        parent = {"kind": "author", "path": str(parent_path.relative_to(output))}
    answer, proof = r.parent_draft(output, plan, chunk, parent)
    invalid = r.preflight(answer, chunk)
    return output, {"selection": item, "parent": parent, "parent_proof_sha256": g.digest(proof),
                    "invalid_groundings": len(invalid), "inventory": inventory,
                    "source_plan_sha256": g.sha((output / "plan.json").read_bytes()),
                    "prompt_sha256": g.sha(r.prompt_text(output, plan, chunk, answer, invalid, parent).encode())}


def one(output, item, attempt, journal):
    print(json.dumps({"event": "repair_started", "time": utc(), **item,
                      "attempt": str(attempt.relative_to(output))}), flush=True)
    result = r.execute(output, attempt, codex="/Users/jim/bin/codex", timeout=1200)
    r.verify(output, attempt, require_complete=result["status"] == "complete_patch")
    record = {"selection": item, "attempt": str(attempt.relative_to(output)),
              "status": result["status"], "time": utc(),
              "journal_sha256": g.sha((attempt / "journal.json").read_bytes()),
              "elapsed_seconds": result["elapsed_seconds"]}
    g.save(journal / f"{item['candidate']}-{item['mode']}-{item['chunk']}.json", record, exclusive=True)
    print(json.dumps({"event": "repair_finished", **record}), flush=True)
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selection", type=Path, required=True)
    parser.add_argument("--journal", type=Path, required=True)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--jobs", type=int, default=4, choices=range(1, 5))
    args = parser.parse_args()
    args.selection, args.journal = args.selection.resolve(strict=True), args.journal.resolve()
    g.require(args.journal.is_relative_to(ROOT), "repair journal escapes study")
    items = g.load(args.selection)
    g.require(isinstance(items, list) and items, "repair selection must be nonempty")
    g.require(len({(x["candidate"], x["mode"], x["chunk"]) for x in items}) == len(items), "duplicate repair chunk")
    checked = [(item, *check_item(item)) for item in items]
    plan = {"profile": "ac.generation.repair-coordinator-plan/1", "created_at": utc(),
            "coordinator_sha256": g.sha(Path(__file__).read_bytes()),
            "selection_sha256": g.sha(args.selection.read_bytes()), "code_pins": r.code_pins(),
            "jobs": args.jobs, "timeout_seconds": 1200, "selected": [entry[2] for entry in checked],
            "claim": "Conditional F_P evidence-selection repairs; original failures remain measured; no semantic equivalence or acceptance."}
    if not args.execute:
        print(json.dumps(plan, indent=2))
        return
    freeze = g.load(ROOT / "repair-freeze.json")
    for relative, pin in freeze["files"].items():
        path = REPO / relative
        g.require(g.sha(path.read_bytes()) == pin["sha256"], "repair preflight binding changed: " + relative)
    g.require((ROOT / "evidence/initial-coordinator/result.json").is_file(), "initial author coordinator has not closed")
    invocations = list((ROOT / "runs-v2").glob("*/*/actors/author/*/attempt-*/invocation.json"))
    invocations += list((ROOT / "runs-v2").glob("*/*/grounding-repairs/*/attempt-*/actor/invocation.json"))
    g.require(not any(not (p.parent / "result.json").exists() for p in invocations), "a prior generation/repair actor is unfinished")
    g.require(not args.journal.exists(), "preserve previous repair coordinator journal")
    lock = ROOT / "evidence/generation-coordinator.lock"
    lock.mkdir()
    args.journal.mkdir(parents=True)
    g.save(args.journal / "plan.json", plan, exclusive=True)
    prepared, records, errors = [], [], []
    started = time.perf_counter()
    try:
        # Retain every reservation, so a preparation failure can be resumed
        # explicitly with prepared_attempt rather than wasting another call.
        for item, output, _ in checked:
            try:
                attempt = r.safe_attempt(output, Path(item["prepared_attempt"])) if item.get("prepared_attempt") else r.prepare(
                    output, item["chunk"], parent_repair=Path(item["parent_repair"]) if item.get("parent_repair") else None)
                prepared.append((output, item, attempt))
                g.save(args.journal / f"reservation-{item['candidate']}-{item['mode']}-{item['chunk']}.json",
                       {"selection": item, "attempt": str(attempt.relative_to(output)),
                        "request_sha256": g.sha((attempt / "request.json").read_bytes())}, exclusive=True)
            except Exception as exc:
                errors.append({"selection": item, "phase": "prepare", "error": str(exc)})
                break
        if not errors:
            with ThreadPoolExecutor(max_workers=args.jobs) as pool:
                futures = {pool.submit(one, output, item, attempt, args.journal): item for output, item, attempt in prepared}
                for future in as_completed(futures):
                    try:
                        records.append(future.result())
                    except Exception as exc:
                        errors.append({"selection": futures[future], "phase": "execute_or_verify", "error": str(exc)})
    finally:
        lock.rmdir()
    g.save(args.journal / "result.json", {"profile": "ac.generation.repair-coordinator-result/1",
           "finished_at": utc(), "elapsed_wall_seconds": time.perf_counter() - started,
           "repairs": records, "errors": errors}, exclusive=True)
    raise SystemExit(1 if errors or any(row["status"] != "complete_patch" for row in records) else 0)


if __name__ == "__main__":
    main()

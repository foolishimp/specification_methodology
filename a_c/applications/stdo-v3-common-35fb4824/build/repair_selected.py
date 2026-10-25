#!/usr/bin/env python3
"""Exactly one existing grounding-repair profile call per two granted chunks."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import subprocess
import sys
import threading
import time

APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))
import build_common as b

b.environment()
g = b.generator()
import ac_grounding as h
import ac_repair as r

IDS = ["chunk-cf22b253a1db7d64a8f8", "chunk-e1247fa9e1eb5dbd49cd"]
SETTINGS = {"model": "gpt-6-astra", "model_reasoning_effort": "high", "service_tier": "default"}
CLI = "codex-cli 0.162.1"
PLAN = APP / "build/grounding-repair-plan.json"
EXECUTION = b.PROOF / "grounding-repair-execution.json"
STATUS = APP / "build/grounding-repair-status.json"
PINS = {
    b.PROOF / "grounding-repair-activation.json": "a856cf0b7e5a0fc706a257a2d9fb1d5bb87579f03825523c0f253f28f0bf53cb",
    APP / "build/repair-dependencies.json": "ea19c7c4e1bcc2fa95259fa2ba4f8dfe39ef5f3dc70268a60986392be2aab40d",
    b.PROOF / "grounding-diagnostic-closure.json": "4262726dc5ecc3e815d399f2010b66d2526f34c827ebf1f77cc40ded395ac9c1",
    APP / "build/initial-author-results.json": "5f361fbb57426975f0f692eb1320db363174c58fdb3acdaa709d15d71c09defe",
    b.RUN / "plan.json": "31a88bb55aa025cb95ba4f7710bd8559b5e0e5f4976b55388cdac1e1cf8337cf",
    b.RUN / "chunks.json": "2ce228fa4f647bcb275ff6653aff1a20eca792c93037f9d7959080668129d073",
    b.RUN / "actor-settings.json": "f3b748facc38547ccdceeb05350b9e75b9afb8e30b009a63f916ea374f7e40ed",
}


def frozen():
    subject = b.guard()
    for path, pin in PINS.items():
        assert b.sha(path) == pin, str(path)
    grant = b.load(b.PROOF / "grounding-repair-activation.json")
    assert grant["native_grant"]["exact_chunk_ids"] == IDS
    assert grant["native_grant"]["repair_calls"] == 2 and grant["native_grant"]["timeout_seconds"] == 1800
    dependencies = b.load(APP / "build/repair-dependencies.json")
    assert dependencies["supplemented_manifest_sha256"] == b.sha(APP / "build/implementation-manifest.json")
    assert {path.name for path in r.ASSETS.iterdir()} == {"repair.txt", "patch.schema.json"}
    for member in dependencies["files"]:
        for path in (APP / member["snapshot"], b.AC / member["source"]):
            assert b.sha(path) == member["sha256"] and path.stat().st_size == member["bytes"]
    diagnostic = b.load(b.PROOF / "grounding-diagnostic-closure.json")
    for name, pin in diagnostic["files"].items():
        path = b.AC / name
        if name == "applications/stdo-v3-common-35fb4824/BUILD.md" and b.sha(path) != pin["sha256"]:
            path = APP / "build/history/BUILD.grounding-diagnostics-closed.md"
        assert b.sha(path) == pin["sha256"] and path.stat().st_size == pin["bytes"], name
    originals = b.load(APP / "build/initial-author-results.json")
    original_attempts = list((b.RUN / "actors/author").glob("*/attempt-*"))
    assert len(original_attempts) == 18 and all(path.name == "attempt-001" for path in original_attempts)
    for record in originals["attempts"]:
        attempt = b.RUN / record["attempt"]
        assert {path.name for path in attempt.iterdir() if path.is_file()} == set(record["files"])
        for name, pin in record["files"].items():
            path = attempt / name
            assert b.sha(path) == pin["sha256"] and path.stat().st_size == pin["bytes"]
    root = b.RUN / r.REPAIRS
    if root.exists():
        assert {path.name for path in root.iterdir()} <= set(IDS)
        for folder in root.iterdir():
            assert folder.is_dir() and {path.name for path in folder.iterdir()} == {"attempt-001"}
    for record in originals["attempts"]:
        inventory = r.call_inventory(b.RUN, record["chunk"])
        assert len([value for value in inventory if value["family"] == "author"]) == 1
        assert len(inventory) <= (2 if record["chunk"] in IDS else 1)
    for member in b.load(APP / "build/implementation-manifest.json")["files"]:
        assert b.sha(b.AC / member["source"]) == member["sha256"]
    existing = b.load(b.PROOF / "unrelated-source-guard.json")
    for name, pin in existing["files"].items():
        path = b.AC / name
        assert path.is_file() and b.sha(path) == pin["sha256"] and path.stat().st_size == pin["bytes"], name
    assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=b.AC, text=True).strip() == "bfe228511415d346459523cec44e7e8157e2991a"
    assert not any((b.RUN / name).exists() for name in ("proposal", "partial-proposal", "grounded-proposal", "grounded-partial-proposal", "repaired-proposal", "repaired-partial-proposal", "model.json"))
    plan, chunks = g.checkpoint(b.RUN)
    g.verify_discovery(b.RUN)
    assert g.load(b.RUN / "actor-settings.json") == {"settings": SETTINGS, "cli_version": CLI}
    return subject, plan, chunks, len(existing["files"])


def live_settings():
    _, _, metadata = g.actor_settings("/Users/jim/bin/codex", SETTINGS)
    initial = b.load(b.PROOF / "environment-preflight.json")["native_actor"]
    assert metadata["settings"] == SETTINGS and metadata["cli_version"] == CLI
    assert metadata["config_path"] == initial["config_path"] and metadata["config_sha256"] == initial["config_sha256"]
    return metadata


def prepare():
    subject, plan, chunks, _ = frozen()
    assert not PLAN.exists() and not EXECUTION.exists() and not (b.RUN / r.REPAIRS).exists()
    live_settings()
    selected = []
    for identity in IDS:
        attempt = r.prepare(b.RUN, identity)
        request, _, chunk, parent = r.verify_request(b.RUN, attempt)
        assert request["parent"] == {"kind": "author", "path": "actors/author/" + identity + "/attempt-001"}
        parent_pin = b.load(b.PROOF / "grounding-repair-activation.json")["exact_original_parents"][identity]
        original_path = b.RUN / request["parent"]["path"] / "answer.json"
        assert b.sha(original_path) == parent_pin["sha256"] and original_path.stat().st_size == parent_pin["bytes"]
        selected.append({"chunk": identity, "attempt": str(attempt.relative_to(b.RUN)),
                         "request_sha256": b.sha(attempt / "request.json"), "prompt_sha256": request["prompt_sha256"],
                         "prompt_chars": len((attempt / "prompt.txt").read_text()), "schema_sha256": request["schema_sha256"],
                         "chunk_sha256": g.digest(chunk), "parent_original_answer_sha256": parent_pin["sha256"],
                         "prepared_parent_answer_sha256": request["parent_answer_sha256"],
                         "invalid_anchor_count": len(request["invalid_grounding_entries"]),
                         "budget_after_reservation": r.call_inventory(b.RUN, identity)})
    frozen()
    record = {"profile": "ac.common.grounding-repair-plan/1", "created_at": b.now(), "script_sha256": b.sha(Path(__file__)),
              "activation_sha256": b.sha(b.PROOF / "grounding-repair-activation.json"),
              "supplemental_dependencies_sha256": b.sha(APP / "build/repair-dependencies.json"),
              "source_guard": subject, "source_plan_sha256": b.sha(b.RUN / "plan.json"), "chunks_sha256": b.sha(b.RUN / "chunks.json"),
              "repair_code_pins": r.code_pins(), "settings": SETTINGS, "cli_version": CLI,
              "repair_calls": 2, "reservations": 2, "jobs": 2, "timeout_seconds": 1800, "selected": selected,
              "new_native_calls": 0, "claims": "Exactly two separately granted initial grounding repairs reserved, with original parents. No retry, fallback, second patch, assembly or final public receipt."}
    b.save(PLAN, record)
    print(json.dumps({"status": "prepared", "plan_sha256": b.sha(PLAN), "script_sha256": record["script_sha256"],
                      "dependency_manifest_sha256": record["supplemental_dependencies_sha256"], "reservations": 2,
                      "new_native_calls": 0, "settings": SETTINGS, "cli_version": CLI, "selected": selected}, indent=2))


def execute():
    subject, _, _, _ = frozen()
    selected = b.load(PLAN)
    assert selected["script_sha256"] == b.sha(Path(__file__))
    assert selected["activation_sha256"] == PINS[b.PROOF / "grounding-repair-activation.json"]
    assert [value["chunk"] for value in selected["selected"]] == IDS
    assert not EXECUTION.exists()
    for value in selected["selected"]:
        attempt = b.RUN / value["attempt"]
        assert b.sha(attempt / "request.json") == value["request_sha256"]
        assert not (attempt / "actor").exists() and not (attempt / "journal.json").exists()
        r.verify_request(b.RUN, attempt)
    live_settings()
    b.save(EXECUTION, {"profile": "ac.common.grounding-repair-execution/1", "started_at": b.now(),
                      "plan_sha256": b.sha(PLAN), "script_sha256": b.sha(Path(__file__)),
                      "source_guard": subject, "repair_calls_authorized": 2, "jobs": 2, "timeout_seconds": 1800})
    lock = threading.Lock()
    active, closed = set(), {}
    errors = []
    started = time.perf_counter()

    def status():
        body = {"profile": "ac.common.grounding-repair-status/1", "observed_at": b.now(), "active": sorted(active),
                "closed": [closed[identity] for identity in IDS if identity in closed], "closed_count": len(closed),
                "claim": "Selection only; retained actual invocation and result files decide actual native execution."}
        temporary = STATUS.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
        temporary.replace(STATUS)

    def one(value):
        identity = value["chunk"]
        attempt = b.RUN / value["attempt"]
        try:
            with lock:
                frozen()
                live_settings()
                assert b.sha(Path(__file__)) == selected["script_sha256"]
                assert b.sha(attempt / "request.json") == value["request_sha256"]
                r.verify_request(b.RUN, attempt)
                assert not (attempt / "actor").exists() and not (attempt / "journal.json").exists()
                b.save(b.PROOF / "grounding-repair-launches" / (identity + ".json"),
                       {"selected_at": b.now(), "chunk": identity, "attempt": value["attempt"],
                        "request_sha256": value["request_sha256"], "plan_sha256": b.sha(PLAN),
                        "timeout_seconds": 1800, "claim": "Preflight selection only; actual native invocation is retained by unchanged run_actor."})
                active.add(identity)
                status()
                print(json.dumps({"event": "repair_selected", "time": b.now(), "chunk": identity}), flush=True)
            journal = r.execute(b.RUN, attempt, codex="/Users/jim/bin/codex", timeout=1800)
            _, verified = r.verify(b.RUN, attempt, require_complete=journal["status"] == "complete_patch")
            assert verified == journal
            raw = b.load(attempt / "actor/result.json")
            record = {"chunk": identity, "attempt": value["attempt"], "status": journal["status"],
                      "journal_sha256": b.sha(attempt / "journal.json"), "request_sha256": b.sha(attempt / "request.json"),
                      "derived_answer_sha256": journal.get("derived_answer_sha256"),
                      "verification": "reverified_complete" if journal["status"] == "complete_patch" else "reverified_retained_outcome",
                      "remaining_invalid_anchor_count": len(journal.get("remaining_invalid_grounding_entries", [])),
                      "usage_events": raw.get("usage_events", []), "raw_actor_result": raw,
                      "files": {str(path.relative_to(attempt)): {"bytes": path.stat().st_size, "sha256": b.sha(path)}
                                for path in sorted(attempt.rglob("*")) if path.is_file()}}
            b.save(b.PROOF / "grounding-repair-closed" / (identity + ".json"), record)
            with lock:
                active.remove(identity)
                closed[identity] = {"chunk": identity, "status": journal["status"], "journal_sha256": record["journal_sha256"]}
                status()
                print(json.dumps({"event": "repair_closed", "time": b.now(), "chunk": identity,
                                  "status": journal["status"], "actor_elapsed_seconds": raw["elapsed_seconds"]}), flush=True)
            return record
        except Exception as exc:
            with lock:
                active.discard(identity)
                errors.append({"chunk": identity, "error": type(exc).__name__ + ": " + str(exc)})
                status()
                print(json.dumps({"event": "repair_error", "chunk": identity, "error": errors[-1]["error"]}), flush=True)
            return None

    with ThreadPoolExecutor(max_workers=2) as pool:
        records = [value for value in (future.result() for future in as_completed([pool.submit(one, value) for value in selected["selected"]])) if value]
    records.sort(key=lambda value: IDS.index(value["chunk"]))
    after, _, _, count = frozen()
    aggregate = {}
    for record in records:
        for event in record["usage_events"]:
            for key, value in event.items():
                assert type(value) is int
                aggregate[key] = aggregate.get(key, 0) + value
    invocations = sum((b.RUN / value["attempt"] / "actor/invocation.json").is_file() for value in selected["selected"])
    result = {"profile": "ac.common.grounding-repair-result/1", "closed_at": b.now(), "phase_calls_authorized": 2,
              "actual_native_invocations": invocations, "actual_invocations_including_initials": 18 + invocations,
              "reservations": 2, "closed_records": len(records), "records": records, "errors": errors,
              "aggregate_reported_usage": aggregate,
              "calls_with_reported_usage": sum(bool(value["usage_events"]) for value in records),
              "calls_with_unknown_usage": sum(not value["usage_events"] for value in records),
              "phase_elapsed_wall_seconds": time.perf_counter() - started,
              "summed_actor_elapsed_seconds": sum(value["raw_actor_result"]["elapsed_seconds"] for value in records),
              "source_guard_after": after, "guarded_existing_files_unchanged": count,
              "plan_sha256": b.sha(PLAN), "script_sha256": b.sha(Path(__file__)),
              "claims": "Only the two granted first grounding repair calls. All original failures and raw repair results retained. No second patch, author retry, normalization overwrite, assembly, final public receipt, semantic acceptance or release. Usage counters kept separately without a billing formula."}
    b.save(APP / "build/grounding-repair-result.json", result)
    print(json.dumps({"event": "phase_closed", "actual_native_invocations": invocations,
                      "closed_records": len(records), "statuses": [value["status"] for value in records],
                      "errors": errors, "result_sha256": b.sha(APP / "build/grounding-repair-result.json"),
                      "aggregate_reported_usage": aggregate}), flush=True)
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=("prepare", "execute"))
    if parser.parse_args().phase == "prepare":
        prepare()
    else:
        execute()

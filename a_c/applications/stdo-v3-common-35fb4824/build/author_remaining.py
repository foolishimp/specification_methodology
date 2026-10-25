#!/usr/bin/env python3
"""Exact sixteen fresh common author attempts; no retry or recovery operation."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import sys
import threading
import time

APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))
import build_common as b

IDS = [
    "chunk-48d20c632dceaba4c74c", "chunk-6a6fe643ed4a56a2207f", "chunk-9ad55c758435da840238",
    "chunk-5de9b50d9be9a9a975ec", "chunk-681e3bcdbe30d3f19555", "chunk-840f31f0a41659bed31f",
    "chunk-a9bfe9fddc1bbf8bf726", "chunk-fb45aab9fdaa869d1b60", "chunk-dd5da8dbb2163820ad7c",
    "chunk-2f24e576ad073131be2b", "chunk-e6c17b5f309623af04f5", "chunk-e1247fa9e1eb5dbd49cd",
    "chunk-f4383ca77391f9eb91c7", "chunk-aee29b86d3101ee98ba1", "chunk-dac75ca2eb8f2a17b8e5",
    "chunk-1e8571ebafdc9e3b6403",
]
EXPECTED_SETTINGS = {"model": "gpt-6-astra", "model_reasoning_effort": "high", "service_tier": "default"}
EXPECTED_CLI = "codex-cli 0.162.1"
PLAN = APP / "build/remaining-author-plan.json"
STATUS = APP / "build/remaining-author-status.json"
EXECUTION = b.PROOF / "remaining-author-execution.json"


def first_batch_guard() -> None:
    assert b.sha(APP / "build/first-batch-result.json") == "ebf9da663379f37ec723a558e83045276785602c95510df93fe6d8948e721890"
    first = b.load(APP / "build/first-batch-result.json")
    for item in first["attempts"]:
        attempt = b.RUN / item["attempt"]
        assert not any((attempt / "empty-workspace").iterdir())
        for name, expected in item["files"].items():
            assert b.sha(attempt / name) == expected["sha256"], "first-batch evidence drift"


def frozen():
    b.environment()
    guard = b.guard()
    first_batch_guard()
    grant = b.load(b.PROOF / "remaining-author-activation.json")
    assert grant["native_grant"]["exact_chunk_ids"] == IDS
    assert grant["native_grant"]["calls"] == 16 and grant["native_grant"]["timeout_seconds"] == 1800
    g = b.generator()
    plan, chunks = g.checkpoint(b.RUN)
    assert [chunk["id"] for chunk in chunks[2:]] == IDS
    assert g.load(b.RUN / "actor-settings.json") == {"settings": EXPECTED_SETTINGS, "cli_version": EXPECTED_CLI}
    g.verify_discovery(b.RUN)
    assert not (b.RUN / "grounding-repairs").exists(), "no repair reservation authorized"
    assert not any((b.RUN / name).exists() for name in
                   ("proposal", "partial-proposal", "grounded-proposal", "repaired-proposal")), "no assembly authorized"
    return g, plan, chunks, guard


def live_settings(g):
    _, _, metadata = g.actor_settings("/Users/jim/bin/codex", {"model": "gpt-6-astra", "model_reasoning_effort": "high"})
    initial = b.load(b.PROOF / "environment-preflight.json")["native_actor"]
    assert metadata["settings"] == EXPECTED_SETTINGS and metadata["cli_version"] == EXPECTED_CLI
    assert metadata["config_path"] == initial["config_path"] and metadata["config_sha256"] == initial["config_sha256"], "configuration drift"
    return metadata


def preflight() -> None:
    g, plan, chunks, guard = frozen()
    assert not EXECUTION.exists(), "execution already selected"
    assert all(not (b.RUN / "actors/author" / identity).exists() for identity in IDS), "fresh-only selection is not fresh"
    metadata = live_settings(g)
    selected = []
    for chunk in chunks[2:]:
        prompt = g.author_prompt(plan, chunk, b.RUN)
        selected.append({"chunk": chunk["id"], "chunk_sha256": g.digest(chunk), "source_chars": chunk["source_chars"],
                         "source_sections": len(chunk["segments"]), "prompt_sha256": g.sha(prompt.encode()),
                         "prompt_chars": len(prompt), "attempt": "actors/author/" + chunk["id"] + "/attempt-001"})
    record = {"profile": "ac.common.remaining-author-plan/1", "created_at": b.now(),
              "scheduler_sha256": b.sha(Path(__file__)), "grant_sha256": b.sha(b.PROOF / "remaining-author-activation.json"),
              "source_guard": guard, "plan_sha256": b.sha(b.RUN / "plan.json"), "chunks_sha256": b.sha(b.RUN / "chunks.json"),
              "discovery_result_sha256": b.sha(b.RUN / "discovery/result.json"),
              "settings": metadata["settings"], "cli_version": metadata["cli_version"],
              "timeout_seconds": 1800, "jobs": 4, "calls": 16, "selected": selected,
              "intentional_timeout_change": "Remaining calls use1800seconds after first strict1200-second call took1118.518seconds.",
              "claims": "Exactly sixteen listed never-attempted original chunks, once each; no retry, normalization, repair or assembly."}
    b.save(PLAN, record)
    print(json.dumps({"plan_sha256": b.sha(PLAN), "scheduler_sha256": record["scheduler_sha256"],
                      "calls": 16, "jobs": 4, "timeout_seconds": 1800, "settings": EXPECTED_SETTINGS,
                      "selected": selected, "new_model_calls": 0}, indent=2))


def execute() -> None:
    g, plan, chunks, guard = frozen()
    selected = b.load(PLAN)
    assert selected["scheduler_sha256"] == b.sha(Path(__file__))
    assert selected["grant_sha256"] == b.sha(b.PROOF / "remaining-author-activation.json")
    assert selected["plan_sha256"] == b.sha(b.RUN / "plan.json") and selected["chunks_sha256"] == b.sha(b.RUN / "chunks.json")
    assert [item["chunk"] for item in selected["selected"]] == IDS
    assert all(not (b.RUN / "actors/author" / identity).exists() for identity in IDS)
    live_settings(g)
    b.save(EXECUTION, {"profile": "ac.common.remaining-author-execution/1", "started_at": b.now(),
                      "plan_sha256": b.sha(PLAN), "scheduler_sha256": b.sha(Path(__file__)),
                      "calls_authorized": 16, "jobs": 4, "timeout_seconds": 1800, "source_guard": guard})
    lock = threading.Lock()
    hold = threading.Event()
    active, closed = {}, {}
    started = time.perf_counter()

    def status() -> None:
        body = {"profile": "ac.common.remaining-author-status/1", "observed_at": b.now(),
                "selected_active_ids": sorted(active), "closed_count": len(closed),
                "closed": [closed[identity] for identity in IDS if identity in closed],
                "hold": hold.is_set(), "claim": "Active selection is not proof that backend execution or billing occurred; actual invocation/result files decide."}
        temporary = STATUS.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        temporary.replace(STATUS)

    def one(item):
        identity = item["chunk"]
        try:
            with lock:
                assert not hold.is_set(), "scheduler held after a material custody error"
                frozen()
                live_settings(g)
                assert b.sha(Path(__file__)) == selected["scheduler_sha256"]
                assert not (b.RUN / "actors/author" / identity).exists()
                chunk = next(chunk for chunk in chunks if chunk["id"] == identity)
                prompt = g.author_prompt(plan, chunk, b.RUN)
                assert g.digest(chunk) == item["chunk_sha256"] and g.sha(prompt.encode()) == item["prompt_sha256"]
                b.guard()
                b.save(b.PROOF / "remaining-author-launches" / (identity + ".json"),
                       {"selected_at": b.now(), "chunk": identity, "attempt": item["attempt"],
                        "prompt_sha256": item["prompt_sha256"], "chunk_sha256": item["chunk_sha256"],
                        "plan_sha256": b.sha(PLAN), "timeout_seconds": 1800,
                        "claim": "Selection/preflight receipt; actual native invocation is retained by unchanged run_actor."})
                active[identity] = True
                status()
                print(json.dumps({"event": "author_selected", "time": b.now(), "chunk": identity}), flush=True)
            attempt = b.RUN / item["attempt"]
            result = g.run_actor(prompt, g.ASSETS / "author.schema.json", attempt, "/Users/jim/bin/codex", 1800, EXPECTED_SETTINGS)
            if result["status"] == "completed":
                try:
                    g.author_check(g.load(attempt / "answer.json"), chunk)
                    g.save(attempt / "validation.json", {"status": "structurally_valid_proposal",
                           "answer_sha256": g.sha((attempt / "answer.json").read_bytes()), "chunk_sha256": g.digest(chunk),
                           "claim": "Source coordinates and declared shape checked; semantic fitness unassessed."}, exclusive=True)
                except g.GenerationError as error:
                    result["status"] = "failed"
                    result["failures"].append("source_or_semantic_fragment_validation")
                    result["validation_error"] = str(error)
                    g.save(attempt / "result.json", result)
            custody, custody_error = None, None
            if result["status"] == "completed" or result["failures"] == ["source_or_semantic_fragment_validation"]:
                try:
                    g.actor_evidence(b.RUN, plan, chunk, attempt, allow_source_failure=result["status"] != "completed")
                    custody = "strict_original" if result["status"] == "completed" else "source_only_failure_custody_verified"
                except (ValueError, OSError) as error:
                    custody_error = str(error)
                    hold.set()
            after = b.guard()
            first_batch_guard()
            live_settings(g)
            record = {"closed_at": b.now(), "chunk": identity, "attempt": item["attempt"], "result": result,
                      "custody": custody, "custody_error": custody_error, "after": after,
                      "files": {path.name: {"bytes": path.stat().st_size, "sha256": b.sha(path)}
                                for path in sorted(attempt.iterdir()) if path.is_file()}}
            b.save(b.PROOF / "remaining-author-closed" / (identity + ".json"), record)
            with lock:
                active.pop(identity)
                closed[identity] = {"chunk": identity, "status": result["status"], "failures": result["failures"],
                                    "validation_error": result.get("validation_error"), "custody": custody,
                                    "elapsed_seconds": result["elapsed_seconds"], "usage_events": result["usage_events"]}
                status()
            print(json.dumps({"event": "author_closed", "time": b.now(), **closed[identity]}), flush=True)
            return record
        except Exception:
            hold.set()
            raise

    records, errors = [], []
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(one, item): item["chunk"] for item in selected["selected"]}
        for future in as_completed(futures):
            try:
                records.append(future.result())
            except Exception as error:
                record = {"time": b.now(), "chunk": futures[future], "error": str(error)}
                errors.append(record)
                print(json.dumps({"event": "scheduler_error", **record}), flush=True)
    records.sort(key=lambda item: IDS.index(item["chunk"]))
    usage = {}
    for record in records:
        for event in record["result"].get("usage_events", []):
            for key, value in event.items():
                assert type(value) is int
                usage[key] = usage.get(key, 0) + value
    result = {"profile": "ac.common.remaining-author-result/1", "closed_at": b.now(),
              "selected_calls": 16, "closed_records": len(records), "records": records, "errors": errors,
              "aggregate_reported_usage": usage,
              "calls_with_reported_usage": sum(bool(record["result"].get("usage_events")) for record in records),
              "calls_with_unknown_usage": sum(not record["result"].get("usage_events") for record in records),
              "phase_elapsed_wall_seconds": time.perf_counter() - started,
              "summed_actor_elapsed_seconds": sum(record["result"]["elapsed_seconds"] for record in records),
              "scheduler_sha256": b.sha(Path(__file__)), "plan_sha256": b.sha(PLAN), "after": b.guard(),
              "claims": "Fresh listed originals only. Every original failure and reported usage retained. No retry, normalization, repair or assembly. Separate usage counters are not summed into a billing formula."}
    b.save(APP / "build/remaining-author-result.json", result)
    print(json.dumps({"event": "phase_closed", "closed_records": len(records), "errors": errors,
                      "result_sha256": b.sha(APP / "build/remaining-author-result.json"),
                      "aggregate_reported_usage": usage}), flush=True)
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=("preflight", "execute"))
    if parser.parse_args().phase == "preflight":
        preflight()
    else:
        execute()

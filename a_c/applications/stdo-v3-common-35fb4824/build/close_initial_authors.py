#!/usr/bin/env python3
"""Join closed initial-attempt custody; no calls, recovery, model or receipt."""
from __future__ import annotations

from datetime import datetime
import json
from pathlib import Path
import sys

APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))
import build_common as b


def main() -> None:
    b.environment()
    guard = b.guard()
    assert b.sha(APP / "build/first-batch-result.json") == "ebf9da663379f37ec723a558e83045276785602c95510df93fe6d8948e721890"
    first = b.load(APP / "build/first-batch-result.json")
    rest = b.load(APP / "build/remaining-author-result.json")
    assert rest["selected_calls"] == rest["closed_records"] == 16 and rest["errors"] == []
    g = b.generator()
    plan, chunks = g.checkpoint(b.RUN)
    g.verify_discovery(b.RUN)
    source = first["attempts"] + rest["records"]
    assert len(source) == 18 and {item["chunk"] for item in source} == {chunk["id"] for chunk in chunks}
    attempts = sorted((b.RUN / "actors/author").glob("*/attempt-*"))
    assert len(attempts) == 18 and all(path.name == "attempt-001" and (path / "result.json").is_file() for path in attempts)
    assert not (b.RUN / "grounding-repairs").exists()
    assert not any((b.RUN / name).exists() for name in ("normalization", "proposal", "partial-proposal", "grounded-proposal", "repaired-proposal"))
    rows = []
    usage = {}
    for chunk in chunks:
        item = next(item for item in source if item["chunk"] == chunk["id"])
        attempt = b.RUN / item["attempt"]
        assert not any((attempt / "empty-workspace").iterdir())
        for name, expected in item["files"].items():
            assert b.sha(attempt / name) == expected["sha256"] and (attempt / name).stat().st_size == expected["bytes"], "closed attempt drift"
        result = b.load(attempt / "result.json")
        assert result == item["result"]
        invocation = b.load(attempt / "invocation.json")
        assert result["settings"] == {"model": "gpt-6-astra", "model_reasoning_effort": "high", "service_tier": "default"}
        assert result["cli_version"] == "codex-cli 0.162.1"
        for event in result.get("usage_events", []):
            for key, value in event.items():
                assert type(value) is int
                usage[key] = usage.get(key, 0) + value
        answer = None
        if (attempt / "answer.json").is_file():
            try:
                candidate = b.load(attempt / "answer.json")
                if isinstance(candidate, dict) and all(isinstance(candidate.get(key), list) for key in
                                                       ("concepts", "constraints", "relations", "latitude", "residuals", "dispositions")):
                    answer = candidate
            except (ValueError, OSError):
                pass  # Retain malformed native output and its failure, without invented draft counts.
        rows.append({"chunk": chunk["id"], "attempt": item["attempt"], "status": result["status"],
                     "failures": result["failures"], "validation_error": result.get("validation_error"),
                     "custody": item["custody"], "custody_error": item["custody_error"],
                     "timeout_seconds": invocation["timeout_seconds"], "elapsed_seconds": result["elapsed_seconds"],
                     "usage_events": result["usage_events"], "settings": result["settings"], "cli_version": result["cli_version"],
                     "draft_family_counts": {key: len(answer[key]) for key in ("concepts", "constraints", "relations", "latitude", "residuals")} if answer else None,
                     "draft_dispositions": len(answer["dispositions"]) if answer else None,
                     "files": item["files"]})
    first_start = datetime.fromisoformat(b.load(b.PROOF / "commands/first-batch-author.invocation.json")["created_at"])
    last_close = max(datetime.fromisoformat(item["closed_at"]) for item in rest["records"])
    joined = {"profile": "ac.common.initial-authors-closed/1", "created_at": b.now(),
              "source_guard": guard, "plan_sha256": b.sha(b.RUN / "plan.json"), "chunks_sha256": b.sha(b.RUN / "chunks.json"),
              "first_batch_result_sha256": b.sha(APP / "build/first-batch-result.json"),
              "remaining_author_result_sha256": b.sha(APP / "build/remaining-author-result.json"),
              "calls": 18, "closed_calls": 18, "calls_each_chunk": 1, "retry_calls": 0, "repair_reservations_or_calls": 0,
              "strict_originals": sum(item["custody"] == "strict_original" for item in rows),
              "source_only_failed_originals": sum(item["custody"] == "source_only_failure_custody_verified" for item in rows),
              "other_failed_or_unverified_originals": sum(item["custody"] not in ("strict_original", "source_only_failure_custody_verified") for item in rows),
              "calls_with_reported_usage": sum(bool(item["usage_events"]) for item in rows),
              "calls_with_unknown_usage": sum(not item["usage_events"] for item in rows),
              "aggregate_reported_usage": usage, "summed_actor_elapsed_seconds": sum(item["elapsed_seconds"] for item in rows),
              "sum_native_phase_wall_seconds": first["phase_elapsed_wall_seconds"] + rest["phase_elapsed_wall_seconds"],
              "observed_first_launch_to_last_close_seconds": (last_close - first_start).total_seconds(),
              "observed_span_includes": "Native execution, between-phase coordination and preflights; not an isolated latency benchmark.",
              "attempts": rows, "interpretation_state": "not_assembled",
              "claims": "All18 initial author attempts are closed; original failures remain failures. Documentary custody and reported counters only. No F_D normalization, F_P repair, model assembly, final public receipt, semantic acceptance or release performed. Reasoning-output counter is retained separately and not added to output again."}
    b.save(APP / "build/initial-author-results.json", joined)
    print(json.dumps({"calls": 18, "strict_originals": joined["strict_originals"],
                      "source_only_failed_originals": joined["source_only_failed_originals"],
                      "other_failed_or_unverified_originals": joined["other_failed_or_unverified_originals"],
                      "aggregate_reported_usage": usage,
                      "joined_sha256": b.sha(APP / "build/initial-author-results.json")}, indent=2))


if __name__ == "__main__":
    main()

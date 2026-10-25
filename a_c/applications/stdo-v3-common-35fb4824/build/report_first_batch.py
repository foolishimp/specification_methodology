#!/usr/bin/env python3
"""Close retained two-call evidence without issuing calls or changing outcomes."""
from __future__ import annotations

import json
from pathlib import Path
import sys

APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))
import build_common as b


def main() -> None:
    b.environment()
    before = b.guard()
    command = b.load(b.PROOF / "commands/first-batch-author.result.json")
    assert command["exit_code"] in (0, 1), "Protocol/refusal exit needs explicit diagnosis"
    g = b.generator()
    plan, chunks = g.checkpoint(b.RUN)
    g.verify_discovery(b.RUN)
    selection = b.load(APP / "build/first-batch-plan.json")["selection"]
    assert [item["chunk"] for item in selection] == [chunk["id"] for chunk in chunks[:2]]
    attempts = sorted((b.RUN / "actors/author").glob("*/attempt-*"))
    assert len(attempts) == 2 and {path.parent.name for path in attempts} == {item["chunk"] for item in selection}
    assert all(path.name == "attempt-001" and (path / "result.json").is_file() for path in attempts)
    assert not (b.RUN / "grounding-repairs").exists()
    records = []
    for attempt in attempts:
        result = b.load(attempt / "result.json")
        chunk = next(value for value in chunks if value["id"] == attempt.parent.name)
        custody, custody_error = None, None
        if result["status"] == "completed" or result["failures"] == ["source_or_semantic_fragment_validation"]:
            try:
                g.actor_evidence(b.RUN, plan, chunk, attempt, allow_source_failure=result["status"] != "completed")
                custody = "strict_original" if result["status"] == "completed" else "source_only_failure_custody_verified"
            except (ValueError, OSError) as error:
                custody_error = str(error)
        answer = b.load(attempt / "answer.json") if (attempt / "answer.json").is_file() else None
        records.append({"chunk": chunk["id"], "attempt": str(attempt.relative_to(b.RUN)), "result": result,
                        "custody": custody, "custody_error": custody_error,
                        "draft_family_counts": {key: len(answer[key]) for key in
                                                ("concepts", "constraints", "relations", "latitude", "residuals")} if answer else None,
                        "draft_dispositions": len(answer["dispositions"]) if answer else None,
                        "files": {path.name: {"bytes": path.stat().st_size, "sha256": b.sha(path)}
                                  for path in sorted(attempt.iterdir()) if path.is_file()}})
    usage = {}
    for record in records:
        for event in record["result"].get("usage_events", []):
            for key, value in event.items():
                assert type(value) is int
                usage[key] = usage.get(key, 0) + value
    result = {"profile": "ac.common.first-batch-closure/1", "created_at": b.now(), "calls": 2, "closed_calls": 2,
              "attempts": records, "aggregate_reported_usage": usage,
              "calls_with_reported_usage": sum(bool(item["result"].get("usage_events")) for item in records),
              "calls_with_unknown_usage": sum(not item["result"].get("usage_events") for item in records),
              "summed_actor_elapsed_seconds": sum(item["result"]["elapsed_seconds"] for item in records),
              "phase_elapsed_wall_seconds": command["elapsed_wall_seconds"],
              "remaining_unattempted_chunks": len(chunks) - 2,
              "unattempted_chunk_ids": [chunk["id"] for chunk in chunks[2:]],
              "phase_command_exit_code": command["exit_code"],
              "reporting_helper_sha256": b.sha(Path(__file__)), "before": before, "after": b.guard(),
              "claims": "Two initial calls closed. Original failures are unchanged. No retry, F_D normalization, F_P repair, assembly, semantic acceptance or release performed. Usage fields are summed separately without adding reasoning_output_tokens to output_tokens."}
    b.save(APP / "build/first-batch-result.json", result)
    b.save(b.PROOF / "first-batch-reporting-correction.json", {
        "profile": "ac.common.harness-correction/1", "created_at": b.now(),
        "original_orchestrator_sha256": b.sha(APP / "build_common.py"),
        "cause": "Application wrapper required CLI exit0, but the unchanged public CLI correctly exits1 when any retained actor fails source validation.",
        "correction": "Separate reporter consumes both closed attempts and ordinary CLI evidence; no actor, original result, validator, source or implementation changed or rerun.",
        "reporting_helper_sha256": b.sha(Path(__file__)),
        "joined_result_sha256": b.sha(APP / "build/first-batch-result.json")})
    print(json.dumps({"calls": 2, "closed_calls": 2, "aggregate_reported_usage": usage,
                      "attempts": [{"chunk": item["chunk"], "status": item["result"]["status"],
                                    "failures": item["result"]["failures"], "validation_error": item["result"].get("validation_error"),
                                    "custody": item["custody"], "custody_error": item["custody_error"]} for item in records],
                      "remaining_unattempted_chunks": len(chunks) - 2,
                      "result_sha256": b.sha(APP / "build/first-batch-result.json")}, indent=2))


if __name__ == "__main__":
    main()

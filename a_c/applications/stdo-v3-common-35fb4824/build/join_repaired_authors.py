#!/usr/bin/env python3
"""Join closed native usage and available strict draft evidence, no assembly."""
from __future__ import annotations

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import repair_selected as worker

b, g, h, r = worker.b, worker.g, worker.h, worker.r
APP = worker.APP


def main():
    subject, plan, chunks, guarded = worker.frozen()
    initial = b.load(APP / "build/initial-author-results.json")
    repair_path = APP / "build/grounding-repair-result.json"
    assert b.sha(repair_path) == "a888079892fae76d4720463c4bfe5a2885cd213ccf35f0c010fae8f6a2214671"
    repair_result = b.load(repair_path)
    assert repair_result["actual_native_invocations"] == repair_result["closed_records"] == 2
    assert repair_result["errors"] == []
    originals = {row["chunk"]: row for row in initial["attempts"]}
    diagnostic = {row["chunk"]: row for row in b.load(APP / "build/grounding-diagnostics.json")["chunks"]}
    repairs = {row["chunk"]: row for row in repair_result["records"]}
    rows = []
    for chunk in chunks:
        identity = chunk["id"]
        original = originals[identity]
        row = {"chunk": identity, "chunk_sha256": g.digest(chunk), "original_attempt": original["attempt"],
               "original_status_unchanged": original["status"],
               "original_answer_sha256": b.sha(b.RUN / original["attempt"] / "answer.json"),
               "original_result_sha256": b.sha(b.RUN / original["attempt"] / "result.json")}
        if identity in repairs:
            evidence = repairs[identity]
            attempt = b.RUN / evidence["attempt"]
            assert {str(path.relative_to(attempt)) for path in attempt.rglob("*") if path.is_file()} == set(evidence["files"])
            for name, pin in evidence["files"].items():
                path = attempt / name
                assert b.sha(path) == pin["sha256"] and path.stat().st_size == pin["bytes"]
            answer, journal = r.verify(b.RUN, attempt)
            assert answer is not None and journal["status"] == "complete_patch"
            raw = b.load(attempt / "actor/result.json")
            assert raw == evidence["raw_actor_result"] and raw["status"] == "completed" and not raw["failures"]
            assert journal["parent_meaning_sha256"] == journal["derived_meaning_sha256"]
            path = attempt / "derived-answer.json"
            row.update(available_draft="F_P_complete_patch", repair_attempt=evidence["attempt"],
                       request_sha256=b.sha(attempt / "request.json"), journal_sha256=b.sha(attempt / "journal.json"),
                       parent_and_derived_meaning_sha256=journal["parent_meaning_sha256"],
                       patch_target_count=len(b.load(attempt / "actor/answer.json")["patches"]))
        else:
            normalized, journal = h.verify_normalization(b.RUN, plan, chunk, b.RUN / "normalization" / identity)
            if original["status"] == "completed":
                answer, _ = h.evidence(b.RUN, plan, chunk, b.RUN / original["attempt"])
                assert g.canonical(answer) == g.canonical(normalized)
                path = b.RUN / original["attempt"] / "answer.json"
                row.update(available_draft="strict_original")
            else:
                assert diagnostic[identity]["selection"] == "F_D_valid"
                answer = normalized
                path = b.RUN / "normalization" / identity / "derived-answer.json"
                row.update(available_draft="F_D_valid", recovered_anchor_count=len(journal["changes"]))
            row["normalization_journal_sha256"] = b.sha(b.RUN / "normalization" / identity / "journal.json")
        g.author_check(answer, chunk)
        assert not r.invalid_anchors(answer, chunk)
        inventory = r.call_inventory(b.RUN, identity)
        assert len(inventory) == (2 if identity in repairs else 1)
        assert all(value["invocation_recorded"] for value in inventory)
        row.update(available_answer=str(path.relative_to(b.RUN)), available_answer_sha256=b.sha(path),
                   exact_source_fragment_validation="passed", remaining_invalid_anchors=0,
                   actual_call_count=len(inventory))
        rows.append(row)
    aggregate = dict(initial["aggregate_reported_usage"])
    for key, value in repair_result["aggregate_reported_usage"].items():
        assert type(value) is int
        aggregate[key] = aggregate.get(key, 0) + value
    summary = {kind: sum(row["available_draft"] == kind for row in rows)
               for kind in ("strict_original", "F_D_valid", "F_P_complete_patch")}
    result = {"profile": "ac.common.author-and-repair-closed/1", "closed_at": b.now(),
              "script_sha256": b.sha(Path(__file__)), "source_guard": subject,
              "guarded_existing_files_unchanged": guarded,
              "initial_author_results_sha256": b.sha(APP / "build/initial-author-results.json"),
              "grounding_repair_result_sha256": b.sha(repair_path),
              "supplemental_dependency_manifest_sha256": b.sha(APP / "build/repair-dependencies.json"),
              "original_implementation_manifest_sha256": b.sha(APP / "build/implementation-manifest.json"),
              "source_plan_sha256": b.sha(b.RUN / "plan.json"), "chunks_sha256": b.sha(b.RUN / "chunks.json"),
              "initial_author_calls": 18, "initial_author_strict_results": 11,
              "initial_author_source_only_failures_preserved": 7, "grounding_repair_calls": 2,
              "grounding_repair_complete_patches": 2, "actual_native_invocations": 20,
              "closed_native_invocations": 20, "unfinished_reservations": 0,
              "author_retry_calls": 0, "second_repair_calls": 0,
              "available_strict_drafts": 18, "draft_origin_summary": summary, "draft_inventory": rows,
              "aggregate_reported_usage": aggregate, "calls_with_reported_usage": 20, "calls_with_unknown_usage": 0,
              "summed_actor_elapsed_seconds": initial["summed_actor_elapsed_seconds"] + repair_result["summed_actor_elapsed_seconds"],
              "sum_native_phase_wall_seconds": initial["sum_native_phase_wall_seconds"] + repair_result["phase_elapsed_wall_seconds"],
              "interpretation_state": "not_assembled", "final_public_receipt_emitted": False,
              "claims": "Closed initial author and grounding repair custody, reported usage and available strict source drafts only. Draft inventory is a preassembly frontier, not final assembled-model provenance. Original failures remain failures. No assembly, canonical model, final public receipt, semantic acceptance, installed qualification or release. Reasoning-output counter remains separate and is not added again to output; no efficiency or billing claim."}
    path = APP / "build/author-and-repair-results.json"
    b.save(path, result)
    print(json.dumps({"status": "CLOSED_native_inventory", "joined_result_sha256": b.sha(path),
                      "available_draft_summary": summary, "actual_native_invocations": 20,
                      "closed_native_invocations": 20, "aggregate_reported_usage": aggregate,
                      "unfinished_reservations": 0, "model_assembled": False}, indent=2))


if __name__ == "__main__":
    main()

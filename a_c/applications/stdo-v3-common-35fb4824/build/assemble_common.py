#!/usr/bin/env python3
"""Complete unchanged mechanical assembly and direct checks; no packaging."""
from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import subprocess
import sys
import time

APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP / "build"))
import repair_selected as worker

b, g, h, r = worker.b, worker.g, worker.h, worker.r
import ac_graph as ac

PROPOSAL = b.RUN / "repaired-proposal"
ARTIFACTS = ("model.json", "carrier.json", "graph.json", "coverage.json", "result.json")


def guard():
    subject = b.guard()
    expected = {
        b.PROOF / "construction-activation.json": "0c7bdbacb0ae3f44415296aba0f941a4d41d4ef898db2af6a766b671bc97104f",
        b.PROOF / "grounding-repair-closure.json": "b7f11a781a513521969c86043b8ee06de767a0b8a747bfaf24d7c4f464abd408",
        APP / "build/author-and-repair-results.json": "e2e1e51cbd95c10cedb1ab5312d37f8a2777877a9ee6ea9523824619c617f07a",
        APP / "build/repair-dependencies.json": "ea19c7c4e1bcc2fa95259fa2ba4f8dfe39ef5f3dc70268a60986392be2aab40d",
        APP / "release_tools/PUBLIC-RECEIPTS.md": "8dddf06b1b193cb3968556ef22bdfd77c65e087041026e8150d1106d2effab93",
        APP / "release_tools/public_receipts.py": "c400d1eb1ffac70d62bd257e1451d6b45542b5065c7c4f693d7a9e09fe70c0e5",
    }
    for path, pin in expected.items():
        assert b.sha(path) == pin, str(path)
    for closure_name in ("grounding-repair-closure.json", "grounding-diagnostic-closure.json"):
        for name, pin in b.load(b.PROOF / closure_name)["files"].items():
            path = b.AC / name
            if name == "applications/stdo-v3-common-35fb4824/BUILD.md" and b.sha(path) != pin["sha256"]:
                history = {"0e1abf169cf7773345697835b6650e3f47980e412ba1d0b3daaa47053698b4da": "BUILD.grounding-repairs-closed.md",
                           "cb6e8889c228bdb8b19411bbe2bc174b17ec1dff3e63715fb48e4ca31acd888f": "BUILD.grounding-diagnostics-closed.md"}
                path = APP / "build/history" / history[pin["sha256"]]
            assert b.sha(path) == pin["sha256"] and path.stat().st_size == pin["bytes"], name
    initial = b.load(APP / "build/initial-author-results.json")
    attempts = list((b.RUN / "actors/author").glob("*/attempt-*"))
    assert len(attempts) == 18 and all(path.name == "attempt-001" for path in attempts)
    for record in initial["attempts"]:
        attempt = b.RUN / record["attempt"]
        assert {path.name for path in attempt.iterdir() if path.is_file()} == set(record["files"])
        for name, pin in record["files"].items():
            path = attempt / name
            assert b.sha(path) == pin["sha256"] and path.stat().st_size == pin["bytes"]
    assert {path.parent.name for path in (b.RUN / r.REPAIRS).glob("*/attempt-*")} == set(worker.IDS)
    assert len(list((b.RUN / r.REPAIRS).glob("*/attempt-*"))) == 2
    for dependency in b.load(APP / "build/repair-dependencies.json")["files"]:
        for path in (APP / dependency["snapshot"], b.AC / dependency["source"]):
            assert b.sha(path) == dependency["sha256"] and path.stat().st_size == dependency["bytes"]
    existing = b.load(b.PROOF / "unrelated-source-guard.json")
    for name, pin in existing["files"].items():
        path = b.AC / name
        assert path.is_file() and b.sha(path) == pin["sha256"] and path.stat().st_size == pin["bytes"], name
    settings = b.load(b.PROOF / "environment-preflight.json")["native_actor"]
    assert b.sha(Path(settings["config_path"])) == settings["config_sha256"]
    assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=b.AC, text=True).strip() == "bfe228511415d346459523cec44e7e8157e2991a"
    assert subprocess.check_output(["git", "-C", str(b.UPSTREAM), "rev-parse", "HEAD"], text=True).strip() == g.UPSTREAM_COMMIT == "fe085cedddde3a18554f8749b230bfe47f3dcce7"
    assert not subprocess.check_output(["git", "-C", str(b.UPSTREAM), "status", "--porcelain=v1"], text=True).strip()
    assert not any((b.RUN / name).exists() for name in ("proposal", "partial-proposal", "grounded-proposal", "grounded-partial-proposal", "repaired-partial-proposal"))
    plan, chunks = g.checkpoint(b.RUN)
    g.verify_discovery(b.RUN)
    inventories = {chunk["id"]: r.call_inventory(b.RUN, chunk["id"]) for chunk in chunks}
    assert sum(map(len, inventories.values())) == 20
    for chunk in chunks:
        inventory = inventories[chunk["id"]]
        assert len(inventory) == (2 if chunk["id"] in worker.IDS else 1)
        assert len(inventory) <= r.LIMIT and all(item["invocation_recorded"] for item in inventory)
    return subject, plan, chunks, len(existing["files"])


def selected_evidence(plan, chunks):
    answers, rows = {}, []
    initial = {row["chunk"]: row for row in b.load(APP / "build/initial-author-results.json")["attempts"]}
    for chunk in chunks:
        identity = chunk["id"]
        original = initial[identity]
        original_path = b.RUN / original["attempt"]
        h.evidence(b.RUN, plan, chunk, original_path)
        row = {"chunk": identity, "original_attempt": original["attempt"],
               "original_status": original["status"], "original_answer_sha256": b.sha(original_path / "answer.json"),
               "original_result_sha256": b.sha(original_path / "result.json")}
        if identity in worker.IDS:
            attempt = b.RUN / r.REPAIRS / identity / "attempt-001"
            answer, journal = r.verify(b.RUN, attempt)
            assert journal["status"] == "complete_patch" and answer is not None
            path = attempt / "derived-answer.json"
            row.update(origin="F_P_complete_patch", assembly_derivation="verified_f-p-grounding-patch",
                       repair_attempt=str(attempt.relative_to(b.RUN)), request_sha256=b.sha(attempt / "request.json"),
                       repair_journal_sha256=b.sha(attempt / "journal.json"),
                       invariant_non_grounding_sha256=journal["parent_meaning_sha256"])
        else:
            folder = b.RUN / "normalization" / identity
            answer, journal = h.verify_normalization(b.RUN, plan, chunk, folder)
            path = folder / "derived-answer.json"
            row.update(origin="strict_original" if original["status"] == "completed" else "F_D_valid",
                       assembly_derivation="verified_f-d-grounding", normalization_status=journal["status"],
                       normalization_changes=len(journal["changes"]),
                       normalization_journal_sha256=b.sha(folder / "journal.json"),
                       invariant_non_grounding_sha256=journal["non_grounding_sha256"])
        g.author_check(answer, chunk)
        assert not r.invalid_anchors(answer, chunk)
        row.update(selected_answer=str(path.relative_to(b.RUN)), selected_answer_sha256=b.sha(path),
                   author_grounding_entries=sum(1 for _ in h.anchors(answer)),
                   actual_call_count=len(r.call_inventory(b.RUN, identity)))
        answers[identity] = answer
        rows.append(row)
    return answers, rows


def main():
    started = time.perf_counter()
    subject, plan, chunks, guarded = guard()
    assert not PROPOSAL.exists(), "New immutable complete proposal only; no overwrite or fallback."
    answers, selections = selected_evidence(plan, chunks)
    b.save(APP / "build/construction-preflight.json", {"profile": "ac.common.construction-preflight/1",
           "created_at": b.now(), "script_sha256": b.sha(Path(__file__)), "source_guard": subject,
           "selected_evidence": selections, "actual_calls_closed": 20, "new_native_calls": 0,
           "allow_partial": False, "upstream_commit": g.UPSTREAM_COMMIT,
           "claim": "Selected source/FD/FP evidence and shared budgets verified before unchanged complete assembly."})
    assembly_started = time.perf_counter()
    result = r.assemble(b.RUN, normalization_name="normalization", allow_partial=False, upstream=b.UPSTREAM)
    assembly_seconds = time.perf_counter() - assembly_started
    assert {path.name for path in PROPOSAL.iterdir()} == set(ARTIFACTS)
    document = b.load(PROPOSAL / "model.json")
    model = ac.validate(document)
    assert result == b.load(PROPOSAL / "result.json")
    assert result["status"] == "proposed" and result["processing_complete"] is True
    assert result["model_id"] == model.identity and result["model_sha256"] == model.sha256
    recoveries = {}
    for name in ("carrier.json", "graph.json"):
        recovered = ac.decode(ac.GraphCarrier(b.load(PROPOSAL / name)))
        assert recovered.document == document and recovered.identity == model.identity and recovered.sha256 == model.sha256
        recoveries[name] = {"exact_document_equality": True, "canonical_model_sha256": recovered.sha256}
    source_files = [{key: value[key] for key in ("path", "sha256", "bytes")}
                    for value in b.load(APP / "source-manifest.json")["files"]]
    assert source_files == plan["files"] and len(source_files) == 58
    sources = {}
    for file in source_files:
        path = APP / "source" / file["path"]
        assert b.sha(path) == file["sha256"] and path.stat().st_size == file["bytes"]
        sources[file["path"]] = path.read_bytes().decode("utf-8").splitlines(keepends=True)
    sections = [section for chunk in chunks for section in chunk["segments"]]
    assert len(sections) == len({section["id"] for section in sections}) == 845
    by_section = {section["id"]: section for section in sections}
    for section in sections:
        text = "".join(sources[section["path"]][section["start_line"] - 1:section["end_line"]])
        assert text == section["text"] and g.sha(text.encode()) == section["sha256"]
    inventory = [{"id": section["id"], "sha256": section["sha256"]} for section in sections]
    assert document["basis"]["subject"] == {"id": plan["subject_id"], "sha256": g.digest(source_files), "inventory": inventory}
    assert document["interpretation"]["source_reentry"]["sha256"] == g.digest({"files": source_files, "sections": inventory})
    dispositions = document["interpretation"]["dispositions"]
    assert len(dispositions) == len({row["source"] for row in dispositions}) == 845
    assert {row["source"] for row in dispositions} == set(by_section)
    counts = {family: len(values) for family, values in document["populations"].items()}
    for family in ("traversals", "transformations", "judgments"):
        assert counts[family] == 0
    assert document["functor_bindings"] == {}
    coverage = b.load(PROPOSAL / "coverage.json")
    assert coverage["processing_complete"] is True and coverage["chunks_total"] == coverage["chunks_authored"] == 18
    assert coverage["chunks_missing"] == [] and coverage["source_sections"] == 845
    assert counts == coverage["family_counts"] == result["family_counts"]
    actual_selections = coverage["grounding_repair"]["selections"]
    assert len(actual_selections) == 18
    for expected, actual in zip(selections, actual_selections):
        assert actual["chunk"] == expected["chunk"] and actual["derivation"] == expected["assembly_derivation"]
        assert actual["answer_sha256"] == expected["selected_answer_sha256"]
    emitted = Counter()
    def walk(value, family):
        if isinstance(value, list):
            for child in value:
                walk(child, family)
        elif isinstance(value, dict):
            if {"section", "path", "start_line", "end_line", "quote"} <= set(value):
                section = by_section[value["section"]]
                assert value["path"] == section["path"]
                assert section["start_line"] <= value["start_line"] <= value["end_line"] <= section["end_line"]
                text = "".join(sources[value["path"]][value["start_line"] - 1:value["end_line"]])
                assert bool(value["quote"].strip()) and value["quote"] in text
                emitted[family] += 1
            for child in value.values():
                walk(child, family)
    for family, records in document["populations"].items():
        for record in records:
            walk(record, family)
    assert result["upstream_trial"]["commit"] == g.UPSTREAM_COMMIT
    assert result["upstream_trial"]["model_sha256"] == model.sha256
    for name, pin in result["files"].items():
        assert name in ARTIFACTS and name != "result.json" and b.sha(PROPOSAL / name) == pin
    guard()
    files = {name: {"id": "urn:sha256:" + b.sha(PROPOSAL / name), "bytes": (PROPOSAL / name).stat().st_size,
                    "sha256": b.sha(PROPOSAL / name)} for name in ARTIFACTS}
    checks = {"profile": "ac.common.complete-construction-checks/1", "created_at": b.now(),
              "script_sha256": b.sha(Path(__file__)), "source_guard": subject,
              "guarded_existing_files_unchanged": guarded, "model": {"id": model.identity, "sha256": model.sha256},
              "artifacts": files, "recoveries": recoveries, "source_files": 58, "source_bytes": sum(row["bytes"] for row in source_files),
              "source_sections": 845, "section_dispositions": dict(Counter(row["decision"] for row in dispositions)),
              "chunks": 18, "selected_evidence": selections, "family_counts": counts, "records": sum(counts.values()),
              "author_grounding_entries": sum(row["author_grounding_entries"] for row in selections),
              "physical_grounding_occurrences": sum(emitted.values()), "grounding_by_family": dict(emitted),
              "physical_grounding_note": "Latitude grounding appears once in authored answers and twice in emitted allowed/forbidden variation fields; all physical occurrences checked.",
              "shared_call_limit_per_chunk": 3, "actual_native_calls_closed": 20, "new_native_or_model_calls": 0,
              "fresh_upstream_trial": result["upstream_trial"], "assembly_observed_wall_seconds": assembly_seconds,
              "total_observed_wall_seconds": time.perf_counter() - started,
              "receipt_bindings_state": "Not emitted: waiting for Root fresh CLOSED package_release.py pin after independent documentation repair.",
              "claims": "Complete mechanical proposal assembly only; exact declared finite model/carrier preservation and source reentry. Five active families, three explicitly empty/inert. No cross-chunk/governing sufficiency, semantic correctness, complete calculus conformance, acceptance, qualification, efficiency or release claim."}
    b.save(APP / "build/construction-checks.json", checks)
    b.save(b.PROOF / "construction-artifacts-sealed.json", {"profile": "ac.common.construction-artifacts-sealed/1",
           "sealed_at": b.now(), "model": checks["model"], "artifacts": files,
           "construction_checks_sha256": b.sha(APP / "build/construction-checks.json"),
           "claim": "Five construction artifacts frozen for independent review; this is not Root MODEL-CLOSED-for-packaging or acceptance."})
    print(json.dumps({"status": "construction_artifacts_sealed", "model": checks["model"], "artifacts": files,
                      "family_counts": counts, "records": checks["records"], "author_grounding_entries": checks["author_grounding_entries"],
                      "physical_grounding_occurrences": checks["physical_grounding_occurrences"],
                      "section_dispositions": checks["section_dispositions"],
                      "checks_sha256": b.sha(APP / "build/construction-checks.json"),
                      "seal_sha256": b.sha(b.PROOF / "construction-artifacts-sealed.json"),
                      "public_receipt_state": "Waiting for Root fresh CLOSED receipt-bindings dependency pin."}, indent=2))


if __name__ == "__main__":
    main()

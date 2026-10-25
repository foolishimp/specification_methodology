#!/usr/bin/env python3
"""Bounded F_D normalization and read-only grounding-repair diagnostics.

This application script never invokes or reserves an actor, patches a draft,
assembles a model, or changes frozen Product implementation or source.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
import subprocess
import time

APP = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("common_build", APP / "build_common.py")
b = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(b)
b.environment()
g = b.generator()
import ac_grounding as h
import ac_repair as r

PINS = {
    b.PROOF / "grounding-diagnostic-activation.json": "18b7b71f7aa7ad26e7d8bfe91a04aa05a089b86dbe76bb48694025895eb458ac",
    b.PROOF / "remaining-author-closure.json": "0fa04134752e181d06f490422a606d8dfe8b2ada7c2678f7b2124d4e8a009b1c",
    APP / "build/initial-author-results.json": "5f361fbb57426975f0f692eb1320db363174c58fdb3acdaa709d15d71c09defe",
    APP / "run/plan.json": "31a88bb55aa025cb95ba4f7710bd8559b5e0e5f4976b55388cdac1e1cf8337cf",
    APP / "run/chunks.json": "2ce228fa4f647bcb275ff6653aff1a20eca792c93037f9d7959080668129d073",
    APP / "run/actor-settings.json": "f3b748facc38547ccdceeb05350b9e75b9afb8e30b009a63f916ea374f7e40ed",
}


def guard():
    subject = b.guard()
    for path, pin in PINS.items():
        assert b.sha(path) == pin, str(path)
    plan, chunks = g.checkpoint(b.RUN)
    g.verify_discovery(b.RUN)
    joined = b.load(APP / "build/initial-author-results.json")
    assert joined["calls"] == joined["closed_calls"] == 18
    attempts = list((b.RUN / "actors/author").glob("*/attempt-*"))
    assert len(attempts) == 18 and {p.parent.name for p in attempts} == {c["id"] for c in chunks}
    assert all(p.name == "attempt-001" for p in attempts)
    assert {p.name for p in (b.RUN / "actors").iterdir()} == {"author"}
    assert not (b.RUN / r.REPAIRS).exists(), "repair reservation is outside this activation"
    for record in joined["attempts"]:
        attempt = b.RUN / record["attempt"]
        assert {p.name for p in attempt.iterdir() if p.is_file()} == set(record["files"])
        for name, pin in record["files"].items():
            path = attempt / name
            assert b.sha(path) == pin["sha256"] and path.stat().st_size == pin["bytes"], str(path)
        inventory = r.call_inventory(b.RUN, record["chunk"])
        assert len(inventory) == 1 and inventory[0]["family"] == "author" and inventory[0]["invocation_recorded"]
    existing = b.load(b.PROOF / "unrelated-source-guard.json")
    for name, pin in existing["files"].items():
        path = b.AC / name
        assert path.is_file() and b.sha(path) == pin["sha256"] and path.stat().st_size == pin["bytes"], name
    for item in b.load(APP / "build/implementation-manifest.json")["files"]:
        path = b.AC / item["source"]
        assert b.sha(path) == item["sha256"] and path.stat().st_size == item["bytes"], item["source"]
    assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=b.AC, text=True).strip() == "bfe228511415d346459523cec44e7e8157e2991a"
    assert not any((b.RUN / name).exists() for name in ("proposal", "partial-proposal", "grounded-proposal", "grounded-partial-proposal", "repaired-proposal", "model.json"))
    return subject, plan, chunks, joined, len(existing["files"])


def anchor_diagnostic(invalid, chunk, structurally_eligible):
    section_map = {value["id"]: value for value in chunk["segments"]}
    ground = invalid["grounding"]
    fd_possible, fd_refusal = False, None
    if ground["section_id"] not in section_map:
        fd_refusal = "SectionId is outside exact chunk; F_D policy cannot change SectionId."
    else:
        try:
            _, witness = h.recover_anchor(ground, section_map[ground["section_id"]])
            fd_possible = witness is not None
        except h.GroundingError as exc:
            fd_refusal = str(exc)
    return {**invalid, "fd_individual_anchor_recoverable": fd_possible,
            "fd_individual_refusal": fd_refusal,
            "unchanged_f_p_profile_supports_coordinate_replacement": structurally_eligible,
            "f_p_ground_fields": list(r.GROUND_FIELDS),
            "semantic_sufficiency_of_replacement": "unassessed; requires F_P evidence selection within this exact original chunk, and the actor may refuse"}


def main():
    started = time.perf_counter()
    before, plan, chunks, joined, guarded_count = guard()
    assert not (b.RUN / "normalization").exists(), "one new normalization namespace only; no implicit reuse"
    assert not (APP / "build/grounding-diagnostics.json").exists()
    normalization = h.normalize(b.RUN, name="normalization")
    assert normalization["new_fp_calls"] == 0 and len(normalization["chunks"]) == 18
    b.save(APP / "build/normalization-result.json", normalization)
    normalization_rows = {row["chunk"]: row for row in normalization["chunks"]}
    originals = {record["chunk"]: record for record in joined["attempts"]}
    rows = []
    for chunk in chunks:
        original = originals[chunk["id"]]
        attempt = b.RUN / original["attempt"]
        answer, proof = h.evidence(b.RUN, plan, chunk, attempt)
        original_invalid = r.invalid_anchors(answer, chunk)
        folder = b.RUN / "normalization" / chunk["id"]
        journal = b.load(folder / "journal.json")
        assert journal["status"] == normalization_rows[chunk["id"]]["status"]
        assert journal["selected_original_attempt"] == original["attempt"]
        assert journal["original_evidence"] == proof
        assert journal["unverified_original_pins"] == h.unverified_pins(b.RUN, attempt)
        original_failed = original["status"] != "completed"
        preflight_status, preflight_error, eligible = "not_needed_strict_original", None, False
        if original_failed:
            try:
                invalid = r.preflight(answer, chunk)
                assert invalid == original_invalid
                preflight_status, eligible = "non_grounding_structural_preflight_passed", True
            except r.RepairError as exc:
                preflight_status, preflight_error = "refused", str(exc)
        selected = answer
        invariant = None
        if journal["status"] != "refused":
            selected, verified = h.verify_normalization(b.RUN, plan, chunk, folder)
            assert verified == journal
            original_sections = [(path, key, ground["section_id"]) for path, key, ground in h.anchors(answer)]
            selected_sections = [(path, key, ground["section_id"]) for path, key, ground in h.anchors(selected)]
            assert original_sections == selected_sections
            assert g.canonical(h.nongrounding(answer)) == g.canonical(h.nongrounding(selected))
            assert g.canonical(r.meaning_payload(answer)) == g.canonical(r.meaning_payload(selected))
            invariant = {"non_grounding_payload_sha256": g.digest(h.nongrounding(answer)),
                         "derived_non_grounding_payload_sha256": g.digest(h.nongrounding(selected)),
                         "section_id_and_anchor_order_unchanged": True,
                         "non_grounding_meaning_fields_unchanged": True,
                         "all_other_fields_unchanged": True,
                         "claim": "Declared field equality only; no proof of semantic correctness or sufficient evidence."}
            if original_failed:
                assert journal["status"] == "derived_validated" and journal["changes"]
                selection = "F_D_valid"
                selected_path = folder / "derived-answer.json"
            else:
                assert journal["status"] == "validated_original" and not journal["changes"]
                assert g.canonical(answer) == g.canonical(selected)
                selection = "strict_original"
                selected_path = attempt / "answer.json"
            assert not r.invalid_anchors(selected, chunk)
        else:
            assert original_failed and not (folder / "derived-answer.json").exists()
            assert journal["policy"] == h.POLICY and journal["policy_sha256"] == g.digest(h.POLICY)
            assert journal["normalizer_sha256"] == b.sha(Path(h.__file__))
            try:
                h.normalize_answer(answer, chunk)
            except (h.GroundingError, g.GenerationError, OSError, ValueError) as exc:
                assert str(exc) == journal["refusal"]
            else:
                raise AssertionError("refused normalization now succeeds")
            selection, selected_path = "refused", None
        remaining_invalid = r.invalid_anchors(selected, chunk) if selection == "refused" else []
        rows.append({"chunk": chunk["id"], "chunk_sha256": g.digest(chunk),
                     "original_attempt": original["attempt"], "original_status": original["status"],
                     "original_answer_sha256": b.sha(attempt / "answer.json"),
                     "original_result_sha256": b.sha(attempt / "result.json"),
                     "selection": selection, "selected_answer": str(selected_path.relative_to(b.RUN)) if selected_path else None,
                     "selected_answer_sha256": b.sha(selected_path) if selected_path else None,
                     "normalization_status": journal["status"], "normalization_changes": len(journal["changes"]),
                     "normalization_refusal": journal.get("refusal"),
                     "journal_sha256": b.sha(folder / "journal.json"), "fd_invariants": invariant,
                     "original_invalid_anchor_count": len(original_invalid),
                     "original_invalid_anchors": [anchor_diagnostic(value, chunk, eligible) for value in original_invalid],
                     "repair_preflight": preflight_status, "repair_preflight_error": preflight_error,
                     "remaining_invalid_anchor_count": len(remaining_invalid),
                     "remaining_invalid_anchors": [anchor_diagnostic(value, chunk, eligible) for value in remaining_invalid],
                     "f_p_grounding_repair_needed_for_selection": selection == "refused" and eligible and bool(remaining_invalid),
                     "existing_call_or_reservation_count": len(r.call_inventory(b.RUN, chunk["id"]))})
    after, _, _, _, final_guarded = guard()
    assert final_guarded == guarded_count
    summary = {value: sum(row["selection"] == value for row in rows) for value in ("strict_original", "F_D_valid", "refused")}
    repairs = [row["chunk"] for row in rows if row["f_p_grounding_repair_needed_for_selection"]]
    structural_refusals = [row["chunk"] for row in rows if row["selection"] == "refused" and row["repair_preflight"] == "refused"]
    original_assets = b.AC / "build_tenants/graphify/code/grounding_repair"
    result = {"profile": "ac.common.grounding-diagnostics/1", "closed_at": b.now(),
              "script_sha256": b.sha(Path(__file__)), "source_guard_before": before, "source_guard_after": after,
              "guarded_existing_files_unchanged": guarded_count, "summary": summary, "chunks": rows,
              "total_fd_changed_anchors": sum(row["normalization_changes"] for row in rows),
              "remaining_invalid_anchor_count": sum(row["remaining_invalid_anchor_count"] for row in rows),
              "mechanically_eligible_grounding_repair_chunks": repairs,
              "non_grounding_structural_refusal_chunks": structural_refusals,
              "all_initial_calls_closed": 18, "existing_calls_and_reservations": 18,
              "new_native_or_model_calls": 0, "retry_calls": 0, "repair_calls_or_reservations": 0,
              "assembly_performed": False, "final_public_receipt_emitted": False,
              "normalization_result_sha256": b.sha(APP / "build/normalization-result.json"),
              "normalization_policy_sha256": g.digest(h.POLICY),
              "repair_profile": r.PROFILE,
              "later_repair_asset_dependency": {"snapshot_assets_present": r.ASSETS.is_dir(),
                  "original_assets_observed_only": {path.name: {"bytes": path.stat().st_size, "sha256": b.sha(path)} for path in sorted(original_assets.iterdir()) if path.is_file()},
                  "disposition": "No asset copied or snapshot changed. Any later F_P repair requires a separate grant binding exact repair assets and calls; this receipt reserves nothing."},
              "elapsed_wall_seconds": time.perf_counter() - started,
              "claims": "Mechanical source-grounding normalization and repair eligibility only. Original outcomes remain unchanged. Grounding profile eligibility does not prove adequate replacement evidence, semantic correctness, complete calculus conformance, acceptance or release."}
    b.save(APP / "build/grounding-diagnostics.json", result)
    table = ["# Grounding diagnostic selection", "", "All 18 original attempts remain immutable. No native call, retry, repair reservation, model assembly or public receipt was performed.", "", "| Chunk | Selection | F_D changes | Remaining invalid anchors | Repair preflight |", "|---|---|---:|---:|---|"]
    table += [f"| `{row['chunk']}` | `{row['selection']}` | {row['normalization_changes']} | {row['remaining_invalid_anchor_count']} | {row['repair_preflight']} |" for row in rows]
    table += ["", "The full JSON report retains each invalid anchor and exact diagnostic. F_D preserves SectionId, all non-anchor fields and non-whitespace quote characters; F_P eligibility permits only the unchanged grounding profile and makes no semantic acceptance claim.", "", "Later frontier: " + (", ".join(f"`{chunk}`" for chunk in repairs) if repairs else "no grounding repair needed") + ". Any later calls require a separate Root grant and pinned repair assets; no reservation exists.", ""]
    (APP / "build/grounding-selection.md").open("x").write("\n".join(table))
    print(__import__("json").dumps({"status": "diagnostics_closed", "summary": summary,
          "total_fd_changed_anchors": result["total_fd_changed_anchors"], "remaining_invalid_anchor_count": result["remaining_invalid_anchor_count"],
          "repair_chunks": repairs, "structural_refusal_chunks": structural_refusals,
          "new_native_or_model_calls": 0, "repair_calls_or_reservations": 0,
          "diagnostics_sha256": b.sha(APP / "build/grounding-diagnostics.json"),
          "selection_table_sha256": b.sha(APP / "build/grounding-selection.md"),
          "normalization_result_sha256": result["normalization_result_sha256"]}, indent=2))


if __name__ == "__main__":
    main()

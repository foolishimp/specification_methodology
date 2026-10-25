#!/usr/bin/env python3
"""Report this Worker's checked construction account; never author a review."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parent))
import assemble_common as construction

b, g, h, r, ac = construction.b, construction.g, construction.h, construction.r, construction.ac
APP = construction.APP
PREFIX = "urn:a-c:common:35fb4824:"


def usage(events):
    total = {}
    for event in events:
        for key, value in event.items():
            assert type(value) is int
            total[key] = total.get(key, 0) + value
    return total


def sealed():
    checks_path = APP / "build/construction-checks.json"
    assert b.sha(checks_path) == "e7bc50642a87670173068a635c4f6944ccbe0ae9fe08af89e92e3b13b82eac77"
    assert b.sha(b.PROOF / "construction-artifacts-sealed.json") == "9690964649fa2d6a0deb7a4278cf698a874995940d6b094d18968d07094b86e9"
    checks = b.load(checks_path)
    for name, pin in checks["artifacts"].items():
        path = construction.PROPOSAL / name
        assert b.sha(path) == pin["sha256"] and path.stat().st_size == pin["bytes"]
    return checks


def main():
    started = time.perf_counter()
    construction.guard()
    checks = sealed()
    dependency = b.load(b.PROOF / "receipt-bindings-dependency-closed.json")
    assert dependency["root_consumed_independent_delta"] is True
    assert dependency["package_release_sha256"] == b.sha(APP / "package_release.py")
    activation = b.load(b.PROOF / "construction-activation.json")
    assert b.sha(APP / "release_tools/public_receipts.py") == activation["public_helper_sha256"]
    assert b.sha(APP / "release_tools/PUBLIC-RECEIPTS.md") == activation["public_contract_sha256"]
    assert b.sha(APP / "release_tools/bundle_check.py") == activation["public_bundle_checker_sha256"]
    assert b.sha(APP / "release_tools/source-sections.json") == activation["source_section_inventory_sha256"]
    invocation = {"created_at": b.now(), "argv": [str(b.PYTHON), "-B", str(APP / "package_release.py"),
                  "receipt-bindings", "--proposal", str(construction.PROPOSAL)],
                  "dependency_sha256": b.sha(b.PROOF / "receipt-bindings-dependency-closed.json"),
                  "claim": "Read-only source/model/raw-artifact coordinates only; helper does not generate this Worker's account."}
    b.save(b.PROOF / "commands/construction-receipt-bindings.invocation.json", invocation)
    completed = subprocess.run(invocation["argv"], cwd=b.AC, env=b.environment(), capture_output=True, check=False)
    for name, data in (("stdout.json", completed.stdout), ("stderr.txt", completed.stderr)):
        with (b.PROOF / "commands" / ("construction-receipt-bindings." + name)).open("xb") as stream:
            stream.write(data)
    b.save(b.PROOF / "commands/construction-receipt-bindings.result.json",
           {"closed_at": b.now(), "exit_code": completed.returncode,
            "stdout_sha256": g.sha(completed.stdout), "stderr_sha256": g.sha(completed.stderr)})
    assert completed.returncode == 0, "receipt-bindings failed; retain exact output, no alternative derivation"
    assert dependency["package_release_sha256"] == b.sha(APP / "package_release.py")
    coordinates = json.loads(completed.stdout)
    assert coordinates["kind"] == "a_c.common.public-receipt-bindings/1"
    bindings = coordinates["bindings"]
    assert bindings["model"] == checks["model"]
    assert bindings["artifacts"] == {name: {key: pin[key] for key in ("bytes", "sha256")}
                                      for name, pin in checks["artifacts"].items()}
    b.save(APP / "build/public-bindings.json", coordinates)
    initial = b.load(APP / "build/initial-author-results.json")
    repairs = b.load(APP / "build/grounding-repair-result.json")
    joined = b.load(APP / "build/author-and-repair-results.json")
    source_manifest = b.load(APP / "source-manifest.json")
    custody = b.load(APP / "package-custody.json")
    basis = b.load(b.PROOF / "activation.json")["basis"]
    preflight = b.load(b.PROOF / "environment-preflight.json")
    implementation = b.load(APP / "build/implementation-manifest.json")
    supplements = b.load(APP / "build/repair-dependencies.json")
    original_calls = {row["chunk"]: row for row in initial["attempts"]}
    repair_calls = {row["chunk"]: row for row in repairs["records"]}
    native_calls = []
    for row in initial["attempts"]:
        raw = b.load(b.RUN / row["attempt"] / "result.json")
        native_calls.append({"call_id": PREFIX + "author:" + row["chunk"] + ":attempt-001",
             "profile": "source-author", "chunk": row["chunk"], "attempt": 1,
             "retained_result_status": row["status"], "failure_categories": row["failures"],
             "source_validation_error": row["validation_error"], "cli_exit_code": raw["cli_exit_code"],
             "cli_version": row["cli_version"], "settings": row["settings"], "timeout_seconds": row["timeout_seconds"],
             "elapsed_seconds": row["elapsed_seconds"], "reported_usage": usage(row["usage_events"]),
             "reported_usage_entries": len(row["usage_events"]),
             "prompt_sha256": row["files"]["prompt.txt"]["sha256"],
             "schema_sha256": g.sha((g.ASSETS / "author.schema.json").read_bytes()),
             "answer_raw_sha256": row["files"]["answer.json"]["sha256"],
             "result_raw_sha256": row["files"]["result.json"]["sha256"]})
    for row in repairs["records"]:
        attempt = b.RUN / row["attempt"]
        request, journal, raw = b.load(attempt / "request.json"), b.load(attempt / "journal.json"), row["raw_actor_result"]
        native_calls.append({"call_id": PREFIX + "grounding-repair:" + row["chunk"] + ":attempt-001",
             "profile": r.PROFILE, "chunk": row["chunk"], "attempt": 1,
             "parent_call_id": PREFIX + "author:" + row["chunk"] + ":attempt-001",
             "parent_original_answer_raw_sha256": original_calls[row["chunk"]]["files"]["answer.json"]["sha256"],
             "retained_result_status": raw["status"], "failure_categories": raw["failures"],
             "derived_status": journal["status"], "cli_exit_code": raw["cli_exit_code"],
             "cli_version": raw["cli_version"], "settings": raw["settings"], "timeout_seconds": 1800,
             "elapsed_seconds": raw["elapsed_seconds"], "reported_usage": usage(raw["usage_events"]),
             "reported_usage_entries": len(raw["usage_events"]), "prompt_sha256": request["prompt_sha256"],
             "schema_sha256": request["schema_sha256"], "request_raw_sha256": b.sha(attempt / "request.json"),
             "patch_answer_raw_sha256": row["files"]["actor/answer.json"]["sha256"],
             "result_raw_sha256": row["files"]["actor/result.json"]["sha256"],
             "journal_raw_sha256": b.sha(attempt / "journal.json"), "derived_answer_raw_sha256": journal["derived_answer_sha256"],
             "patched_anchor_entries": len(b.load(attempt / "actor/answer.json")["patches"]),
             "non_grounding_payload_sha256": journal["parent_meaning_sha256"]})
    assert len(native_calls) == 20 and all(row["reported_usage_entries"] > 0 for row in native_calls)
    aggregate = {}
    for row in native_calls:
        for key, value in row["reported_usage"].items():
            aggregate[key] = aggregate.get(key, 0) + value
    assert aggregate == joined["aggregate_reported_usage"]
    selections = []
    for row in checks["selected_evidence"]:
        value = {key: row[key] for key in ("chunk", "origin", "assembly_derivation", "original_status",
                  "original_answer_sha256", "original_result_sha256", "selected_answer_sha256",
                  "author_grounding_entries", "actual_call_count", "invariant_non_grounding_sha256")}
        value["parent_author_call_id"] = PREFIX + "author:" + row["chunk"] + ":attempt-001"
        if row["origin"] == "F_P_complete_patch":
            value.update(selected_repair_call_id=PREFIX + "grounding-repair:" + row["chunk"] + ":attempt-001",
                         request_raw_sha256=row["request_sha256"], journal_raw_sha256=row["repair_journal_sha256"],
                         meaning_and_order_fields_unchanged=True, evidence_selection_semantics="unassessed")
        else:
            value.update(normalization_status=row["normalization_status"], normalization_changes=row["normalization_changes"],
                         journal_raw_sha256=row["normalization_journal_sha256"], section_ids_and_other_fields_unchanged=True,
                         selected_serialization="derived-answer serialization; eleven validated-original no-op cases preserve the entire original JSON value")
        selections.append(value)
    discovery = b.load(APP / "build/discovery.json")
    coverage = b.load(construction.PROPOSAL / "coverage.json")
    first = b.load(APP / "build/first-batch-result.json")
    remaining = b.load(APP / "build/remaining-author-result.json")
    limitations = ["Proposal only: source common remains an unaccepted/unpublished not_ready candidate; this representation does not adopt it as the a_c builder.",
        "Complete processing, section dispositions and exact quotes do not prove semantic completeness or sufficient evidence.",
        "Five active families only; traversals, transformations and judgments are explicitly empty. Conditions, exceptions and uncertainty are inert source-linked statements, not executed predicates.",
        "References are chunk-local. Cross-chunk identity, governing-relation sufficiency and normative interpretation fidelity remain independently unqualified.",
        "F_P grounding repair preserves non-grounding fields but selects new evidence; semantic adequacy and equivalence remain unassessed.",
        "Declared finite schema, reference, dependency and carrier checks do not establish complete axiomatic-calculus conformance or semantic truth.",
        "No semantic acceptance, installed qualification, RC designation, owner release/publication decision or public-distribution authorization is issued by this account.",
        "No accepted-result cost, billing formula, compression benefit or efficiency gain has been qualified.",
        "This issuer performed construction and reports its own work; this is not an independent review. Private event, invocation and native custody is held locally outside the public account; opaque hashes do not make it replayable by recipients."]
    receipt = {"kind": "a_c.common.public-construction-receipt/1",
        "receipt_id": PREFIX + "public-construction-account:1",
        "issuer": "urn:codex:worker:common-representation-construction",
        "bindings": bindings,
        "scope": "Own account of complete mechanical construction of the frozen common source as an a_c.graphify proposal under the unchanged installed STDO v2.5.1-rc.2 builder. Exact source custody, author/repair lineage, separately reported usage and declared finite carrier/source checks only; no independent review, semantic acceptance or release.",
        "details": {"account_recorded_at": b.now(),
            "represented_source": {"commit": custody["source"]["commit"], "package_tree": custody["source"]["package_tree"],
                "semantic_files": 58, "semantic_bytes": 2000888, "semantic_file_coordinates": [{key: row[key] for key in ("path", "sha256", "bytes")} for row in source_manifest["files"]],
                "complete_package_members": 81, "derived_acquisition_frames": 13, "host_legal_release_metadata_members": 10,
                "source_manifest_raw_sha256": b.sha(APP / "source-manifest.json"), "package_custody_raw_sha256": b.sha(APP / "package-custody.json"),
                "classification_raw_sha256": b.sha(APP / "source-classification.json"), "standing": source_manifest["standing"]},
            "builder_basis": {"installed_stdo_version": "v2.5.1-rc.2", "release_manifest_raw_sha256": basis["manifest"],
                "bootstrap_raw_sha256": basis["bootstrap"], "calculus_raw_sha256": basis["calculus"],
                "calculus_uri": "stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md",
                "a_c_product_definition_raw_sha256": basis["product_definition"], "builder_and_product_unchanged": True},
            "implementation": {"original_nine_file_manifest_raw_sha256": b.sha(APP / "build/implementation-manifest.json"),
                "original_snapshot_files": [{key: row[key] for key in ("source", "snapshot", "bytes", "sha256")} for row in implementation["files"]],
                "supplemental_repair_manifest_raw_sha256": b.sha(APP / "build/repair-dependencies.json"),
                "supplemental_two_assets": supplements["files"], "original_manifest_plan_chunks_and_code_unchanged": True,
                "source_plan_raw_sha256": b.sha(b.RUN / "plan.json"), "chunks_raw_sha256": b.sha(b.RUN / "chunks.json"),
                "python_version": preflight["python"]["version"], "dependency_versions": preflight["dependencies"]},
            "generation": {"mode": "graphify-ac", "source_chunk_character_ceiling": 120000, "graph_cue_character_ceiling": 40000,
                "source_characters": 1996064, "chunks": 18, "sections": 845,
                "native_input_scope": "Each original author received only its source chunk and actual Graphify discovery cues under the unchanged profile. Repair actors additionally received the complete same original parent and mechanical invalid-anchor diagnostics. No prior representation, private semantic oracle or independent review answer was an authoring input.",
                "actual_upstream_commit": g.UPSTREAM_COMMIT, "actual_upstream_version": "0.9.90",
                "structural_discovery_counts": discovery["result"]["counts"],
                "structural_discovery_sources_dispatched": 58, "structural_discovery_source_failures": 0,
                "data_json_files_without_structural_nodes": discovery["structural_source_files_without_nodes"],
                "discovery_authority": "Fallible discovery cues only; graph structure did not author or accept normative meaning."},
            "selected_chunk_ancestry": selections,
            "native_execution": {"client": "Codex CLI", "cli_version": "codex-cli 0.162.1",
                "settings": worker_settings(), "actual_executions": 20, "all_executions_closed": 20,
                "original_author_calls": 18, "original_strict_successes": 11, "original_source_only_failures_preserved": 7,
                "author_retry_calls": 0, "grounding_repair_calls": 2, "complete_grounding_patches": 2,
                "second_repair_calls": 0, "unfinished_reservations": 0, "shared_call_limit_per_chunk": 3,
                "overall_call_ceiling": 54, "per_call": native_calls,
                "isolation_checks": "Original and repair custody verified exact prompts/schemas/settings, empty workspaces, read-only sandbox, disabled tools/docs/MCP, clean protocol/schema and unchanged user settings. Event evidence was checked locally and is excluded here."},
            "failure_and_recovery_account": {"original_failures_are_not_relabelled": True,
                "fd_recovered_chunks": 5, "fd_recovered_anchor_entries": 8,
                "fd_policy": h.POLICY, "fd_policy_sha256": g.digest(h.POLICY),
                "fd_section_ids_and_non_anchor_fields_preserved": True,
                "fd_atomic_refusals_preserved": ["chunk-cf22b253a1db7d64a8f8", "chunk-e1247fa9e1eb5dbd49cd"],
                "fp_repaired_chunks": 2, "fp_patched_anchor_entries": 3, "fp_profile": r.PROFILE,
                "fp_non_grounding_statement_and_order_fields_preserved": True,
                "non_model_harness_corrections": ["System Python lacked NetworkX; selected the existing pinned virtual environment before any model call, without installation.",
                    "Initial orchestration expected exit zero; ordinary author CLI correctly returned one for a source-failed draft. A separate reporter closed retained evidence without rerunning an actor."],
                "partial_or_excluded_chunks": 0, "source_files_dropped_after_authoring": 0},
            "reported_usage": {"aggregate_counters": aggregate, "calls_with_known_usage": 20, "calls_with_unknown_usage": 0,
                "usage_scope": "Only these twenty native CLI actor executions, including all seven source-failed originals and both repairs. Executive, construction Worker and reviewer sessions, local F_D processing, source intake and packaging are not included in these counters; total workflow cost is unqualified.",
                "counter_interpretation": "Actual backend-reported integer counters retained as separate fields. Reasoning-output counter is not added again to output. Cached-input and cache-write counters remain separate; no billing inference.",
                "native_phases": [{"name": "first_two_original_authors", "calls": 2, "jobs": 2, "timeout_seconds_each": 1200,
                    "observed_phase_wall_seconds": first["phase_elapsed_wall_seconds"], "reported_counters": first["aggregate_reported_usage"]},
                    {"name": "remaining_sixteen_original_authors", "calls": 16, "jobs": 4, "timeout_seconds_each": 1800,
                    "observed_phase_wall_seconds": remaining["phase_elapsed_wall_seconds"], "reported_counters": remaining["aggregate_reported_usage"]},
                    {"name": "two_grounding_repairs", "calls": 2, "jobs": 2, "timeout_seconds_each": 1800,
                    "observed_phase_wall_seconds": repairs["phase_elapsed_wall_seconds"], "reported_counters": repairs["aggregate_reported_usage"]}],
                "timeout_change_reason": "Remaining original calls used 1800 seconds after the first strict 1200-second original took 1118.518 seconds. No model, effort, tier or profile change.",
                "summed_actor_elapsed_seconds": joined["summed_actor_elapsed_seconds"],
                "sum_native_phase_wall_seconds": joined["sum_native_phase_wall_seconds"],
                "timing_scope": "Actor intervals overlap under concurrency; phase walls include local scheduling and custody checks and omit between-phase coordination. Neither is an isolated performance benchmark."},
            "checked_properties": {"processing_complete": True, "source_file_coordinates_checked": 58,
                "ordered_section_inventory_checked": 845, "section_dispositions_checked": checks["section_dispositions"],
                "disposition_scope": "All 845 sections have explicit dispositions; 24 omitted is an authored disposition, not an excluded source file or unprocessed chunk. Semantic sufficiency remains unassessed.",
                "records": checks["records"], "family_counts": checks["family_counts"],
                "author_grounding_entries_checked": checks["author_grounding_entries"],
                "physical_grounding_occurrences_checked": checks["physical_grounding_occurrences"],
                "grounding_by_family": checks["grounding_by_family"], "grounding_count_scope": checks["physical_grounding_note"],
                "exact_full_model_recoveries": checks["recoveries"], "fresh_actual_upstream_export": checks["fresh_upstream_trial"],
                "declared_finite_carrier_preservation": "Passed exact document and canonical digest equality for both native carrier and actual upstream graph export under the declared signature; no semantic-preservation proof claimed.",
                "assembly_observed_wall_seconds": checks["assembly_observed_wall_seconds"],
                "assembly_time_scope": "One new unchanged complete assemble call including validation/materialization, fresh upstream build/cluster/export and its internal round trips; no model/provider call.",
                "active_families": ["objects", "relations", "constraints", "latitude", "residuals"],
                "explicitly_empty_families": ["traversals", "transformations", "judgments"],
                "functor_bindings": "empty; no prescribed operation or acceptance was executed",
                "cross_chunk_semantic_completeness": coverage["semantic_completeness"]},
            "privacy_and_custody": "Only public source/code/model coordinates, selected-answer/proof hashes, settings, numeric usage and bounded accounts are included. Raw event streams, hidden reasoning, native invocation bodies, user configuration, credentials and private absolute paths remain outside this account. No independent review or acceptance account was generated.",
            "qualification_limits": limitations},
        "construction_state": "complete", "private_material_included": False}
    def privacy(value):
        if isinstance(value, str):
            assert not any(marker in value for marker in ("/Users/", "/private/", "/var/folders/", "config.toml", "events.jsonl", "invocation.json")), value
        elif isinstance(value, list):
            for child in value:
                privacy(child)
        elif isinstance(value, dict):
            for child in value.values():
                privacy(child)
    privacy(receipt)
    path = APP / "build/authoring-public.json"
    b.save(path, receipt)
    sys.path.insert(0, str(APP / "release_tools"))
    import public_receipts
    validated, _ = public_receipts.receipt(path, bindings, public_receipts.CONSTRUCTION)
    assert validated == receipt
    construction.guard()
    sealed()
    assert dependency["package_release_sha256"] == b.sha(APP / "package_release.py")
    proof = {"profile": "ac.common.public-construction-account-checked/1", "created_at": b.now(),
             "script_sha256": b.sha(Path(__file__)), "public_receipt_sha256": b.sha(path),
             "public_receipt_bytes": path.stat().st_size, "bindings_sha256": g.digest(bindings),
             "receipt_bindings_dependency_sha256": b.sha(b.PROOF / "receipt-bindings-dependency-closed.json"),
             "typed_contract_validation": "passed", "public_private_path_scan": "passed",
             "all_five_artifacts_unchanged": True, "new_native_or_model_calls": 0,
             "account_observed_wall_seconds": time.perf_counter() - started,
             "claim": "This Worker authored its own account from retained checked evidence; coordinate helper supplied identities only. This is not independent review, acceptance or packaging authorization."}
    b.save(APP / "build/public-construction-checks.json", proof)
    print(json.dumps({"status": "public_construction_account_checked", "public_receipt_sha256": b.sha(path),
                      "public_receipt_bytes": path.stat().st_size, "checks_sha256": b.sha(APP / "build/public-construction-checks.json"),
                      "bindings": bindings, "new_native_or_model_calls": 0}, indent=2))


def worker_settings():
    return {"model": "gpt-6-astra", "model_reasoning_effort": "high", "service_tier": "default"}


if __name__ == "__main__":
    main()

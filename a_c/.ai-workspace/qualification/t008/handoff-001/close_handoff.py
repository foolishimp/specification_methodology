"""Retain structural custody, permitted-diff and local-link proof only."""
from pathlib import Path
import difflib
import hashlib
import json
import os
import re
import shutil
import time
from urllib.parse import unquote

D = Path(__file__).resolve().parent
P = D.parents[3]
R = P.parent
I = P / ".ai-workspace/qualification/t008/interfaces/integration-004"
REVIEW = P / ".ai-workspace/comments/codex/t008-platform-code-review-003"


def h(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def save(name, value):
    with (D / name).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, sort_keys=True, ensure_ascii=False)
        stream.write("\n")


def loc(path):
    return {"path": str(path.relative_to(P)), "sha256": h(path), "bytes": path.stat().st_size}


plan = json.loads((D / "EDIT_PLAN.json").read_bytes())["sources"]
before = {row["path"]: (D / "before" / row["path"]).read_bytes() for row in plan}
after = {row["path"]: (P / row["path"]).read_bytes() for row in plan}
assert len(plan) == len(before) == 11
diffs = []
source_after = []
checks = []
for row in plan:
    relative = row["path"]
    assert digest(before[relative]) == row["before_sha256"]
    result = b""
    offset = 0
    for edit in row["edits"]:
        assert offset <= edit["start"] <= edit["end"] <= len(before[relative])
        result += before[relative][offset:edit["start"]] + edit["replacement"].encode()
        offset = edit["end"]
    result += before[relative][offset:]
    assert result == after[relative] and digest(result) == row["after_sha256"]
    target = D / "after" / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(result)
    target.chmod(0o444)
    source_after.append({"path": relative, "before_sha256": row["before_sha256"], "sha256": digest(result),
        "bytes": len(result), "before_snapshot": "before/" + relative, "after_snapshot": "after/" + relative})
    diffs.extend(difflib.unified_diff(before[relative].decode().splitlines(keepends=True), result.decode().splitlines(keepends=True),
        fromfile="before/" + relative, tofile=relative))
    checks.append({"path": relative, "exact_plan_reconstruction": True, "unchanged_outside_permitted_ranges": True,
        "ranges": [{k: edit[k] for k in ["start", "end", "scope"]} for edit in row["edits"]]})
with (D / "PATCH.diff").open("x", encoding="utf-8") as stream:
    stream.writelines(diffs)
save("SOURCE_AFTER.json", {"sources": source_after, "changed_existing_paths": 11,
    "classification": "Factual status/navigation/header metadata only; no normative body, runtime code or test edits"})


def suffix_proof(path, marker):
    old = before[path][before[path].index(marker.encode()):]
    new = after[path][after[path].index(marker.encode()):]
    assert old == new, path
    return {"path": path, "boundary": marker, "before_sha256": digest(old), "after_sha256": digest(new), "byte_equal": True}


body_proofs = [suffix_proof("specification/requirements/fd-support-tools.md", "### REQ-AC-FD-001"),
    suffix_proof("specification/requirements/fd-support-verification.md", "### REQ-AC-FDV-001"),
    suffix_proof("build_tenants/graphify/design/fd-support.md", "## Boundary and method binding"),
    suffix_proof("build_tenants/graphify/examples/fd-support/LIFECYCLE_QUICKSTART.md", "Status:")]
assert body_proofs[2]["after_sha256"] == "42d4e8ae0869d9a81e39d3bb2fea5a97c1fd1d0b883dcb24b47503a4a77eb9d8"
for path, marker in [("specification/requirements/fd-support-tools.md", "### REQ-AC-FD-001"),
        ("specification/requirements/fd-support-verification.md", "### REQ-AC-FDV-001"),
        ("build_tenants/graphify/design/fd-support.md", "## Boundary and method binding")]:
    boundary = before[path].index(marker.encode())
    assert all(edit["end"] <= boundary for row in plan if row["path"] == path for edit in row["edits"])
    if "requirements" in path:
        assert b"**Status**: Active" in after[path][:after[path].index(marker.encode())]
assert b"FDV-003 accepted-result benefit remains Deferred/unqualified" in after["specification/requirements/fd-support-verification.md"]
ticket = ".ai-workspace/tickets/active/T-008-fd-tenant-implementation.md"
old_nav = b"Current design state and exact repair routing are owned by\n[Current candidate after reconciliation-008](#current-candidate-after-reconciliation-008) below."
new_nav = b"Current implementation standing and remaining qualification are owned by\n[Current provisional implementation](#current-provisional-implementation) below."
replaced_ticket = before[ticket].replace(old_nav, new_nav, 1)
assert after[ticket].startswith(replaced_ticket)
assert after[ticket][len(replaced_ticket):].startswith(b"\n## Current provisional implementation\n")
assert len([row for row in plan if row["path"] == ticket][0]["edits"]) == 2
binding_before = b"".join(before[ticket].splitlines(keepends=True)[784:860])
binding_after = b"".join(after[ticket].splitlines(keepends=True)[784:860])
assert binding_before == binding_after
assert b"- status: active\n" in after[ticket]
assert after[ticket][:52350] != before[ticket][:52350]
ticket_proof = {"exact_two_navigation_lines_and_append_only": True, "all_other_existing_ticket_bytes_equal": True,
    "binding002_original_lines": [785, 860], "binding002_bytes_equal": True, "binding002_sha256": digest(binding_before),
    "full_before_snapshot": "before/" + ticket, "original_52350_prefix_retained_in_snapshot": True,
    "current_52350_prefix_byte_exact_claim": False, "ticket_active": True, "binding002_standing": "HISTORICAL/stale; no repin"}
goals_marker = b"The completed comparison-preparation increment is"
assert before["specification/GOALS.md"].split(goals_marker, 1)[1] == after["specification/GOALS.md"].split(goals_marker, 1)[1]
req_marker = b"## Deterministic support tools"
assert before["specification/requirements/README.md"].split(req_marker, 1)[0] == after["specification/requirements/README.md"].split(req_marker, 1)[0]
product = "specification/PRODUCT.md"
assert before[product].split(b"## Delivery and qualification boundary", 1)[0] == after[product].split(b"## Delivery and qualification boundary", 1)[0]
assert before[product].split(b"## Independence", 1)[1].split(b"## Product disposition authority", 1)[0] == after[product].split(b"## Independence", 1)[1].split(b"## Product disposition authority", 1)[0]
owner = b"Jim, the Product owner, retains scope, meaning, acceptance and release decisions."
assert owner in before[product] and owner in after[product]
assert b"Construction and independent assessment do not accept their own subjects." in after[product]
save("PERMITTED_DIFF.json", {"exact_11_paths": True, "edit_plan": loc(D / "EDIT_PLAN.json"),
    "per_file": checks, "normative_and_historical_body_proofs": body_proofs, "ticket": ticket_proof,
    "older_study_sections_and_existing_core_requirements_unchanged": True,
    "Product_meaning_prefix_Independence_and_owner_authority_preserved": True,
    "guide_note_standing": "Writer header metadata only; original Status and remainder byte-exact; no new native authorship claim"})

integration = json.loads((I / "CLOSED_RETURN.json").read_bytes())
old_sources = json.loads((I / "SOURCE_MANIFEST.json").read_bytes())["sources"]
raw_pin_applicability = [{"path": row["path"], "historical_sha256": row["sha256"], "current_sha256": h(R / row["path"]),
    "whole_raw_document_unchanged": h(R / row["path"]) == row["sha256"]} for row in old_sources]
implementation = []
for name in ["code/ac_support.py", "code/ac_support_core.py", "code/ac_support_effects.py", "test_env/test_ac_support_core.py", "test_env/test_ac_support_effects.py", "test_env/test_ac_support_interfaces.py"]:
    path = P / "build_tenants/graphify" / name
    row = next(row for row in old_sources if row["path"] == str(path.relative_to(R)))
    assert h(path) == row["sha256"]
    implementation.append(loc(path))
profile = P / "build_tenants/graphify/design/fd-method-claude-rc9.json"
assert h(profile) == "bdb937545c13d2cea8eaa93507102cff7c2ea41ca0fc169a8ec84c81003dc7d1"
review_result = json.loads((REVIEW / "CLOSED_RETURN.json").read_bytes())["reported_result"]
q = P / ".ai-workspace/qualification/t008"
coordinates = {name: loc(path) for name, path in {
    "Root_external_Work_disposition_and_Writer_grant": D / "WRITER.contract.txt",
    "Root_reported_Writer_admission": D / "WRITER.admission.json",
    "implementation_repair001": q / "code-review-repair-001/implementation-001/CLOSED_RETURN.json",
    "implementation_repair002": q / "code-review-repair-002/implementation-001/CLOSED_RETURN.json",
    "initial_wrong_subject_fixture_failure_correction": q / "code-review-repair-002/implementation-001/FIXTURE_ASSERTION_CORRECTION.json",
    "current_code_review_report": REVIEW / "REVIEW.md", "current_code_review_publication": REVIEW / "CLOSED_RETURN.json",
    "ontology_design_dispositions": q / "design-review-repair-001/publication-001/ROOT-DISPOSITION.json",
    "reviewed_HOW_body_preservation": q / "design-review-repair-001/publication-001/HEADER-PRESERVATION.json",
    "technical_integration004": I / "CLOSED_RETURN.json", "integration_results": I / "RESULTS.json",
    "operation_scenario_map": I / "OPERATION_SCENARIO_MAP.json", "repair_controls": I / "REPAIR_CONTROL_EVIDENCE_MAP.json",
    "actual_public_retry_proof": I / "PUBLIC_RETRY_PROOF_INDEX.json", "actual_public_repair_calls": I / "PUBLIC_REPAIR_CALLS_INDEX.json",
    "carried_actual_upstream": q / "interfaces/integration-003/upstream-001/upstream-report.json",
    "upstream_applicability": I / "UPSTREAM_APPLICABILITY.after.json",
    "worker_run_reconciliation": q / "live-reconciliation-001/CLOSED_RETURN.json",
    "guide_provenance_repair": q / "guide-provenance-repair-001/CLOSED_RETURN.json",
    "initial_reviewer_helper_prerequisite_repair": q / "live-review-runtime-001/prereq-repair-001/CLOSED_RETURN.json",
    "phase1_actual_return_acquisition_bridge": q / "live-review-runtime-002/assessment-001/PHASE1_BRIDGE.json",
    "phase1_actual_acquisition_index": q / "live-review-runtime-002/assessment-001/PHASE1_ACQUISITION_INDEX.json",
    "phase2_actual_factual_reconciliation": q / "live-review-runtime-002/phase2-reconciliation-001/CLOSED_RETURN.json",
    "phase2_actual_readable_scope": q / "live-review-runtime-002/phase2-reconciliation-001/READABLE_SCOPE_INDEX.json",
}.items()}
save("PROJECTION.json", {"kind": "Factual read model/index, not authority or another work-state ledger",
    "Root_selected_standing": "Provisional current realization for further dogfood; bounded implementation/review/technical integration complete",
    "ticket_status": "active", "family_status": {"FD": "Active operative work", "FDV": "Active begun/partial qualification", "FDV003": "Deferred/unqualified"},
    "implementation_sources_unchanged": implementation, "profile": loc(profile), "Product_Definition": loc(P / "stdo_a_c.json"),
    "selected_method": {"source": "c2cfa9b908d1722ae3f26c32fa4ece691083bdc3", "tree": "98de394b352179c25dfa63b0b59a9b6bdd43632d",
        "builder": "installed STDO2.5.1-rc.2", "installed_manifest": "3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782", "unchanged": True},
    "current_metadata_sources": loc(D / "SOURCE_AFTER.json"), "coordinates": coordinates,
    "reviewed_design_network_sha256": "d08fe97e4920b10030eb0406325503772e678d9ed0391394558cfc358b59ff7b",
    "body_conservation": body_proofs, "code_review_reported_scope": review_result,
    "review_of_integration004_by_code_reviewer_claimed": False,
    "fresh_checks": {"unique_full_suite_tests": 281, "skipped": 0, "full_suite_runs": 1, "seconds": "58.068", "strict_normal_import_files": 9, "ordinary_CLI_MCP_demo_checks": 10},
    "carried_checks": {"actual_upstream_checks": 9, "from": "integration003", "fresh_standalone_upstream_runs": 0,
        "complete_source_tree": "6e11ed7cda0437ff12a29a328ca785e8915ddbc0", "upstream_source_members": 1064,
        "upstream_commit": "fe085cedddde3a18554f8749b230bfe47f3dcce7", "exact_dependency_boundary_unchanged": True},
    "catalog_scope": {"declared_operations": 23, "all_operations_qualified": False,
        "current_canonical_operation_witnesses": 251, "actual_indexed_public_repair_calls": 188,
        "operations_without_current_owning_witness": integration["operations_without_current_owning_witness"],
        "new8_plus_prior19_control_rows": "Current mechanical execution only; author35 not added to unique full count"},
    "preserved_failures": ["Original design/code F/I/S subjects retain their exact cuts; old review002 F is not relabelled",
        "Initial wrong-subject fixture assertion failed; exact correction and initial raw run retained",
        "Original three code deviations and later E10/E11 reproductions/repairs remain in their own proof",
        "Initial Reviewer helper failed before native launch; parent prerequisite repair did not retry or grant authority"],
    "actual_public_actor_trials": {
        "Worker": "Wrote guide then timed out; no final closed return; captured/check unconsumable; no retry",
        "Reviewer_phase1": "Actual original source-derived-expectations indeterminate/performed_partial; expectation artifact emitted but native wrapper hid ref; final check unconsumable",
        "Reviewer_phase2": "Configured1200000ms timeout; no final vendor result/F_P assessment/return; empty final capture/check unconsumable",
        "original_expectation_source_limits": ["18 protected source_inputs were selected, not full Product/WHAT/12-member method coverage",
            "Phase1 original unread governing scope remains recorded in acquisition index/bridge; later supplemental expectation does not raise or rewrite original I",
            "Large base64/host-saved previews are not readable whole-proof acquisition; actual UTF8 ranges decide observed scope"],
        "independence_limits": ["Same-family review takes no cross-family credit; recorded nonauthorship/source-first/producer/exposure conditions are bounded",
            "Historical native implementation family/model/provider are unobserved; declared unknown group is not attestation",
            "Prior/external/automatic host exposure and mental continuity remain unknown; new process/policy does not prove absolute independence"],
        "process_host_usage_limits": ["Parent end is not process-tree/external effect completion", "Actual delivered/acquired bytes differ from mental receipt", "Unknown usage/billing/whole-host context are not zero or a fit claim"]},
    "qualification_limits": ["F1/R1 isolated _qualified_operator gate is not public qualified-operator or semantic conjunction proof",
        "Direct/callback/fixture process controls are not actual F_P usability or complete FDV001/002 qualification",
        "Unexercised operation/variant/caller/source/host boundaries remain gaps, including SC-AC-FD-001 incomplete actor task",
        "No complete-calculus, matched accepted-result quality/cost/benefit, Product acceptance or installed/RC/release qualification"],
    "runtime_authority": {"binding002": "HISTORICAL/stale, original lines785–860 byte-exact", "renewal_or_repin": False,
        "binding003_selected": False, "new_policy_or_native_call_budget": False, "future_effect_condition": "Separately selected exact current authority/basis and material preconditions required"},
    "raw_document_pin_applicability": {"old_source_count": len(old_sources), "whole_raw_unchanged": sum(row["whole_raw_document_unchanged"] for row in raw_pin_applicability),
        "all_old_raw_source_hashes_current": False, "rows": raw_pin_applicability,
        "interpretation": "Original complete review/integration raw-document pins remain historical after factual metadata edits. Identical code/tests and unchanged normative requirement/design bodies support only explicit bounded applicability, not a reissued review or runtime authority."},
    "metadata_writer": {"actor": "/root/ac_fd_interfaces_worker", "role": "Writer factual metadata only", "guide_body_or_native_authorship_changed": False},
    "new_runtime_or_native_calls": 0, "new_tests_or_substantive_assessments": 0})

# Check only newly authored local Markdown links, including the concise read model.
link_rows = []
texts = [(P / row["path"], "\n".join(edit["replacement"] for edit in row["edits"])) for row in plan]
texts.append((D / "README.md", (D / "README.md").read_text()))
for source, text in texts:
    for match in re.finditer(r"\[[^\]\n]*\]\(([^)\s]+)\)", text):
        target = unquote(match.group(1))
        if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
            continue
        path_part, _, fragment = target.partition("#")
        path = (source.parent / path_part).resolve() if path_part else source
        assert path.exists(), (str(source), target)
        fragment_found = True
        if fragment and path.suffix == ".md":
            headings = []
            for heading in re.findall(r"^#{1,6}\s+(.+?)\s*$", path.read_text(), re.M):
                slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
                headings.append(slug)
            fragment_found = fragment in headings
            assert fragment_found, (str(source), target)
        link_rows.append({"source": str(source.relative_to(P)), "target": target, "exists": True, "fragment_found": fragment_found})
save("LINK_CHECKS.json", {"new_local_links": link_rows, "checked_links": len(link_rows), "all_resolved": True,
    "scope": "New Markdown links/fragments only; no browser, network, runtime or semantic assessment"})

guards = json.loads((D / "GUARDS_BEFORE.json").read_bytes())["files"]
actual = []
for row in guards:
    path = R / row["path"]
    if row["kind"] == "symlink":
        value = {"path": row["path"], "kind": "symlink", "target": os.readlink(path) if path.is_symlink() else None, "target_not_followed": True}
    else:
        value = {"path": row["path"], "kind": "regular", "sha256": h(path) if path.is_file() and not path.is_symlink() else None,
            "bytes": path.stat().st_size if path.is_file() and not path.is_symlink() else None}
    assert row == value, row["path"]
    actual.append(value)
save("GUARD_CHECK.json", {"before": loc(D / "GUARDS_BEFORE.json"), "members": len(guards),
    "regular_files": sum(row["kind"] == "regular" for row in guards), "symlink_target_texts_only": sum(row["kind"] == "symlink" for row in guards),
    "before_values_sha256": digest(json.dumps(guards, sort_keys=True, separators=(",", ":")).encode()),
    "after_values_sha256": digest(json.dumps(actual, sort_keys=True, separators=(",", ":")).encode()),
    "unchanged": True, "mismatches": [], "includes": "Code/tests/helpers/profile/PD/INTENT/basis/owner-map/original Graphify/studies/old proof/comments/live histories"})
json_files = [path for path in D.rglob("*.json") if path.is_file() and not path.is_symlink()]
for path in json_files:
    json.loads(path.read_bytes())
save("STRUCTURAL_CHECKS.json", {"JSON_files_parsed_before_closure": len(json_files), "local_links_checked": len(link_rows),
    "permitted_source_paths": 11, "requirement_design_and_guide_status_suffixes_exact": True, "ticket_navigation_append_only": True,
    "binding002_lines785_860_exact": True, "immutable_guard_members": len(guards), "all_structural_checks_passed": True,
    "tests_run": 0, "runtime_native_provider_Git_network_install_calls": 0, "new_semantic_or_Product_acceptance_assessment": False})
files = [loc(path) for path in sorted(D.rglob("*")) if path.is_file() and not path.is_symlink()
    and path.name not in {"MANIFEST.json", "CLOSED_RETURN.json"}]
save("MANIFEST.json", {"files": files, "role": "Custody of factual metadata proof only", "source_changes": 11})
save("CLOSED_RETURN.json", {"kind": "Closed factual Writer handoff", "activation": "T008-handoff-001", "actor": "/root/ac_fd_interfaces_worker", "consumer": "/root",
    "source_before": loc(D / "SOURCE_BEFORE.json"), "source_after": loc(D / "SOURCE_AFTER.json"), "projection": loc(D / "PROJECTION.json"),
    "permitted_diff": loc(D / "PERMITTED_DIFF.json"), "patch": loc(D / "PATCH.diff"), "structural_checks": loc(D / "STRUCTURAL_CHECKS.json"),
    "link_checks": loc(D / "LINK_CHECKS.json"), "guard_check": loc(D / "GUARD_CHECK.json"), "manifest": loc(D / "MANIFEST.json"),
    "contract": loc(D / "WRITER.contract.txt"), "Root_reported_admission": loc(D / "WRITER.admission.json"),
    "existing_source_changes": 11, "unchanged_guard_members": len(guards), "normative_bodies_preserved": True,
    "ticket_active": True, "binding002_historical_stale_and_byte_exact": True, "new_runtime_authority_or_budget": False,
    "tests_runtime_native_provider_Git_network_install_actions": 0, "new_acceptance_or_semantic_assessment": False,
    "remaining": ["Partial actual actor/operation/variant/host qualification; original Worker/Reviewer failures and source/independence limits retained",
        "Ten operations without current owning witnesses; isolated gate is not public qualified-operator proof",
        "FDV003 benefit Deferred/unqualified; no full-calculus/Product acceptance/install/RC/release",
        "Future real effects require separately selected current authority/basis; no binding003 or call budget"], "next_action": "STOP for Root consumption"})
print(json.dumps({"closed_return": h(D / "CLOSED_RETURN.json"), "source_before": h(D / "SOURCE_BEFORE.json"), "source_after": h(D / "SOURCE_AFTER.json"),
    "manifest": h(D / "MANIFEST.json"), "projection": h(D / "PROJECTION.json"), "permitted_diff": h(D / "PERMITTED_DIFF.json"),
    "changed_sources": source_after, "guard_members": len(guards), "local_links": len(link_rows), "proof_files": len(files)}, indent=2))

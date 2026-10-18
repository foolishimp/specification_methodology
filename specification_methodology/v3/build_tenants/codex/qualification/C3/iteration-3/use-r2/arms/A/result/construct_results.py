"""Construct arm A's initial bounded-use return from the authorized reader.

All task acquisition goes through acquire.py. Writes stay beside this script.
This is a deterministic artifact constructor, not a disposition authority.
"""

from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

from total_cents import candidate_q, partition_total, total_cents


RESULT = Path(__file__).resolve().parent
READER = "/Users/jim/src/apps/specification_methodology-codex/specification_methodology/v3/build_tenants/codex/qualification/C3/iteration-3/use-r2/harness/acquire.py"
METHOD_BASIS = "stdo://releases/v2.5.1-rc.2/"
METHOD_DIGEST = "3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782"
TASK_DIGEST = "d6f7bcba133228ae74c3b54f0055696da191fb697b5151070049566c3baaa559"
STARTED = "2026-10-14T12:54:11Z"
ACTOR = "arm-A fresh bounded-use actor"


def write_json(name, value):
    (RESULT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def file_digest(name):
    return hashlib.sha256((RESULT / name).read_bytes()).hexdigest()


def method(path, start, end, clause, digest):
    return {
        "basis": METHOD_BASIS, "path": path, "start_line": start, "end_line": end,
        "owning_clause": clause, "source_sha256": digest,
    }


SPEC_SHA = "7f12d32ef4e5720d5d59ee5ace50de6c1a12cc56afa53dd67a8ee4c54f8fb8a4"
FRAME_SHA = "6e9148d7c8eff847abf172315b0e282e4477f3d40866b28f7fef21c41cb067e7"
TICKET_SHA = "f031ce7fb3b5b366ffaee5996ae76e861697ad86897cc04c06b67da249fe0eca"
METHOD_SOURCES = {
    "M.work": method("plugins/spec/skills/stdo-work/SKILL.md", 1, 175, "STDO Work: select basis, establish work basis, construct, prove, return", "39d9f88af4b574c4e30f45adc3b19ed324c25ae453d7359112af71aa9d4d4d8f"),
    "M.basis": method("plugins/spec/references/PRODUCT_BASIS.md", 1, 41, "Product Basis Selection", "4dcf0bb305732dcb280187804889426bd5abcd7188d9bb8df8b16af265a0b23f"),
    "M.chain": method("standards/SPEC_METHOD.md", 943, 992, "Constitutional Chain", SPEC_SHA),
    "M.triage": method("standards/SPEC_METHOD.md", 1180, 1327, "Universal Intake Triage; Computed Classification And Treatment", SPEC_SHA),
    "M.proportional": method("standards/SPEC_METHOD.md", 1429, 1502, "Proportional Method And Delivery (STDO-UP-014)", SPEC_SHA),
    "M.construction": method("standards/SPEC_METHOD.md", 1503, 1665, "Agentic Construction Execution (STDO-UP-020)", SPEC_SHA),
    "M.domain": method("standards/SPEC_METHOD.md", 586, 674, "Bounded-Context Semantic Resolution", SPEC_SHA),
    "M.results": method("standards/REFERENCE_FRAME_METHOD.md", 324, 442, "RF-005 exact basis, RF-006 authority, RF-007 separation, RF-008 meaning, RF-012 closed results, RF-015 uncertainty", FRAME_SHA),
    "M.applicability": method("standards/REFERENCE_FRAME_METHOD.md", 577, 643, "Establish The Evaluation Basis; Applicability And Required Results; Return A Closed Result", FRAME_SHA),
    "M.conjunction": method("standards/REFERENCE_FRAME_METHOD.md", 662, 708, "Using Frames In Conjunction; Result Conjunction; Evidence Or Coordinate Translation", FRAME_SHA),
    "M.result_record": method("standards/REFERENCE_FRAME_METHOD.md", 1312, 1331, "Minimal Evaluation Result", FRAME_SHA),
    "M.release": method("standards/RELEASE_METHOD.md", 208, 280, "Exact-Cut Qualification; Selector And Consumer Adoption", "582bc15451855670495e559db3ae6a89ba37edaa3656f33499d02220cbdb141c"),
    "M.carrier": method("standards/TICKET_METHOD.md", 637, 726, "Work-Carrier-To-Execution Rule; Execution Contract Admission", TICKET_SHA),
    "M.continuity": method("standards/TICKET_METHOD.md", 777, 891, "Recorded Judgment And Owner-Ruling Continuity; Condition-Based Closure And Reuse", TICKET_SHA),
    "M.functor_limit": method("standards/AXIOMATIC_CALCULUS.md", 666, 727, "Traversals And Functor Kinds; categorical identity and composition proof requirement", "cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d"),
}


def base_case(task_id, case_id, sources, methods, dependencies, unresolved=None):
    return {
        "case_id": case_id,
        "fixture_sources": sources,
        "case_source": f"task {task_id} / initial_fixture_state.cases[{case_id}]",
        "method_sources": methods,
        "dependencies": dependencies,
        "unresolved": unresolved or [],
        "invalidation": "A change to this independent case, its named owner declarations, exact subject, basis, applicable evidence or grant invalidates only affected claims and their dependants.",
    }


def acquire_packet():
    command = [sys.executable, "-B", READER, "--arm", "A", "task", "all"]
    before = time.monotonic()
    completed = subprocess.run(command, check=True, capture_output=True)
    elapsed = time.monotonic() - before
    packet = json.loads(completed.stdout)
    write_json("fixture-acquisition.json", {
        "kind": "ordinary task acquisition used directly by artifact constructor",
        "command": command,
        "stdout_bytes": len(completed.stdout),
        "stderr_bytes": len(completed.stderr),
        "stdout_sha256": hashlib.sha256(completed.stdout).hexdigest(),
        "elapsed_wall_seconds": elapsed,
        "exit_code": completed.returncode,
        "parsed_task_ids": [task["task_id"] for task in packet["tasks"]],
        "actor_receipt_limit": "This programmatic acquisition is not evidence that the model received or retained every emitted byte. The actor had acquired task all and separately reacquired truncated T3 before construction.",
    })
    return packet


def task_t1(task):
    sources = {s["source_id"]: s["content"] for s in task["initial_fixture_state"]["sources"]}
    contract = sources["E.contract"]
    catalogue = sources["E.evidence"]["observations"]
    cases = []
    for case in task["initial_fixture_state"]["cases"]:
        record = base_case("T1", case["case_id"], ["E.contract", "E.evidence"], ["M.results", "M.applicability", "M.conjunction"], {
            check: ["E.contract", f"{case['case_id']}.returned_assessments", f"{case['case_id']}.other_assessments"] for check in contract["required_checks"]
        })
        assessments = case["returned_assessments"] + case["other_assessments"]
        components = []
        for check in contract["required_checks"]:
            entries = [deepcopy(a) for a in assessments if a["check"] == check]
            for entry in entries:
                entry["observation"] = catalogue[entry["evidence"]]
                entry["authenticated"] = True
                entry["producer_authorized_for_check"] = entry["producer"] == contract["review_authority"][check]
                entry["subject_matches"] = entry["subject"] == contract["subject"]
                entry["basis_matches"] = entry["basis"] == contract["basis"]
            applicable = [a for a in entries if a["producer_authorized_for_check"] and a["subject_matches"] and a["basis_matches"]]
            if not entries:
                result, standing, explanation = "indeterminate", "required result missing", "No assessment for this required check is supplied in this case; being unplanned does not remove the obligation."
            elif not applicable:
                result, standing, explanation = "invalid_basis", "supplied result inapplicable", "The authentic access result is for bundle 16, while the contract requires bundle 17. Current bundle-17 access is unresolved."
            elif any(a["judgement"] == "failed" for a in applicable):
                result, standing, explanation = "falsified", "applicable authenticated failure", "The current checksum observation is a material counterexample; it remains constraining regardless of the other checks."
            else:
                result, standing, explanation = "satisfied", "applicable authenticated success", "The authorized producer assessed this exact subject on this exact basis successfully."
            components.append({
                "check": check, "required": True, "planned": check in contract["planned_assessments"],
                "predicate": f"{check} has an applicable authenticated successful assessment for bundle 17 on requirements 4",
                "required_producer": contract["review_authority"][check],
                "result": result, "standing": standing, "supporting_records": entries, "explanation": explanation,
            })
        supported = all(row["result"] == "satisfied" for row in components)
        residuals = []
        for row in components:
            if row["result"] != "satisfied":
                residuals.append({"check": row["check"], "standing": row["standing"], "required_input": f"Applicable successful {row['check']} assessment from {row['required_producer']} for {contract['subject']} on {contract['basis']}. No repair is authorized."})
        record.update({
            "subject": contract["subject"], "basis": contract["basis"], "components": components,
            "recommendation": {
                "predicate": contract["recommendation_condition"],
                "result": "satisfied" if supported else "falsified",
                "supports_approval_recommendation": supported,
                "decision": "recommend approval to owner" if supported else "withhold approval recommendation",
                "owner_approval_performed": False,
                "permitted_action": "Construct this recommendation only; owner approval and repairs remain outside the grant.",
                "inference": "All mandatory components must be satisfied on the exact coordinates. E1/E2 each have a decisive checksum failure; E1 also retains missing and wrong-subject results.",
            },
            "unresolved": residuals,
        })
        record["change_explanation"] = {
            "E1": "Initial independent case: checksum fails, retention is absent, and access success belongs to bundle 16.",
            "E2": "Compared for explanation with E1: access now matches bundle 17 and retention is supplied outside the planned set; checksum still fails. No observation is carried between cases.",
            "E3": "Compared for explanation with E2: this case cites obs-45, a matching checksum success. All three checks now succeed. obs-41 is not an observation of E3.",
        }[case["case_id"]]
        cases.append(record)
    artifact = {
        "task_id": "T1", "actor": ACTOR, "method_basis": METHOD_BASIS,
        "required_set": contract["required_checks"], "planned_set": contract["planned_assessments"],
        "decision_authority": "Fixture Product owner; actor evaluates and recommends only",
        "case_independence": "Catalogue entries exist as observations only when cited by the current independent case.",
        "cases": cases,
    }
    write_json("assessment-ledger.json", artifact)
    return {"task_id": "T1", "artifacts": ["assessment-ledger.json"], "cases": cases}


def task_t2(task):
    rows, cases = [], []
    for case in task["initial_fixture_state"]["cases"]:
        records, partitions = case["input"], case["partition_record_ids"]
        outputs = {"p": partition_total(records, partitions), "q": candidate_q(records, partitions), "r": total_cents(records)}
        expected = {"K1": 5, "K2": 0, "K3": 5}[case["case_id"]]
        row = {"case_id": case["case_id"], "input": records, "partition_record_ids": partitions, "required_total_cents": expected, "outputs": outputs, "matches_this_case": {plan: value == expected for plan, value in outputs.items()}}
        rows.append(row)
        record = base_case("T2", case["case_id"], ["K.intent", "K.product", "K.spec", "K.plans"], ["M.chain", "M.construction", "M.results", "M.functor_limit"], {"total": ["every record occurrence", "signed integer cents", "K.spec"], "p_and_q_partition": ["complete and disjoint record-ID coverage"]})
        record.update({
            "observation": row,
            "evaluation": {"p": "satisfied", "q": "falsified" if outputs["q"] != expected else "satisfied for this input only", "r": "satisfied"},
            "decision": "Use r as the delivered realization. p is valid under the partition precondition. Reject q as a general realization even when this case happens to match.",
            "permitted_action": "Local construction and deterministic computation only.",
            "artifact": "total_cents.py",
        })
        cases.append(record)
    counterexample = {"input": [{"record_id": "a", "cents": 4}, {"record_id": "b", "cents": 4}], "partition_record_ids": [["a", "b"]], "required_total_cents": 8, "p": 8, "q": 4, "r": 8, "violated_clause": "K.intent: repeated equal amounts are separate records; K.spec: every occurrence contributes exactly once"}
    derivation = {
        "task_id": "T2", "selected_realization": "total_cents.py:total_cents (plan r)",
        "trace": [
            {"layer": "Intent", "source": "K.intent", "meaning": "Exact total of all submitted records, preserving multiplicity."},
            {"layer": "Product", "source": "K.product", "meaning": "Finite record list to one exact signed integer; record_id is identity; no external effect."},
            {"layer": "Specification", "source": "K.spec", "meaning": "Exactly-once contribution, zero for empty, subtraction for negatives, mathematical integers, complete disjoint partitions."},
            {"layer": "Design choice", "source": "Actor choice permitted by K.product and M.proportional", "meaning": "Single sequential accumulator initialized to zero, adding cents for each original occurrence; standard Python integer operations. No parallelism, deduplication or optional graph profile is needed."},
            {"layer": "Realisation", "source": "total_cents.py", "meaning": "total_cents implements r; partition_total validates and implements p; candidate_q is diagnostic rejected code only."},
        ],
        "partition_precondition": "The original list has unique record IDs. Each partition member denotes exactly one original record. Across the finite partitions every original record ID occurs exactly once, with no foreign ID. Empty partitions are permitted. Values may repeat and partitions need not preserve original order.",
        "preservation_argument": {
            "r_invariant": "After k iterations, accumulator equals the sum of cents for exactly the first k original records. Initially k=0 and accumulator=0. Each iteration adds exactly the next signed integer once, preserving the invariant. At k=n the accumulator is the required total. A negative integer subtracts by integer addition.",
            "p_argument": "Complete disjoint ID coverage makes the flattened partitions a permutation of the original records with multiplicity one. Associativity groups additions into partial totals; commutativity permits their order; identity 0 handles empty partitions and the empty input. Therefore p equals r under the declared precondition.",
            "q_failure": "Deduplication by cents changes multiplicity whenever two distinct record IDs in one partition have the same nonzero cents. K1 yields 1 rather than 5; the smaller counterexample yields 4 rather than 8. Coincidental equal totals, zeros or distinct-valued inputs do not repair the universal contract.",
            "number_model": "Python integer arithmetic preserves exact signed integer values without fixed-width overflow or approximation. Resource or input failure is not reported as a successful approximate total. Physical resource sufficiency for every finite mathematical input is not claimed.",
        },
        "identity_binding": "record_id equality is the input identity relation; the fixture uses string IDs. The algorithm does not equate records by cents. Python checks uniqueness with ID equality, and partition resolution uses that same relation.",
        "plan_dispositions": {"p": "accept as a bounded realization under the explicit partition precondition", "q": "reject", "r": "accept as the selected bounded realization"},
        "counterexample": counterexample,
        "categorical_claim": "None. This is an integer algebra and loop-invariant preservation argument, not a category-theoretic proof. Source/target categories and identity/composition laws have not been supplied, so no categorical functor claim is made.",
        "method_sources": ["M.chain", "M.proportional", "M.construction", "M.functor_limit"],
        "fixture_sources": ["K.intent", "K.product", "K.spec", "K.plans"],
        "cases": cases,
    }
    write_json("total-cents-output.json", rows)
    write_json("construction-derivation.json", derivation)
    return {"task_id": "T2", "artifacts": ["total_cents.py", "total-cents-output.json", "construction-derivation.json"], "cases": cases, "plan_dispositions": derivation["plan_dispositions"], "counterexample": counterexample, "unresolved": [], "limits": [derivation["categorical_claim"], derivation["preservation_argument"]["number_model"]]}


def task_t3(task):
    sources = {s["source_id"]: s["content"] for s in task["initial_fixture_state"]["sources"]}
    cases = []
    for case in task["initial_fixture_state"]["cases"]:
        domain_source = {"Archive": "D.archive", "Admission": "D.admission", "Dispatch": "D.dispatch"}[case["domain"]]
        record = base_case("T3", case["case_id"], [domain_source, "D.consumer"], ["M.domain", "M.results", "M.conjunction", "M.result_record"], {
            "domain_meaning": [domain_source], "consumer_admissibility": ["D.consumer", "successful conformance", "exact digest acceptance certificate"]
        })
        record.update({
            "frame_identity": "A:T3:domain-predicate-evaluation:v1", "activation_identity": f"A:T3:{case['case_id']}",
            "actor": ACTOR, "basis": [domain_source, "D.consumer"],
            "semantic_owner": next(s["owner"] for s in task["initial_fixture_state"]["sources"] if s["source_id"] == domain_source),
            "decision_owner": "Deployment owner for consumer input; domain owner for domain semantics and effects",
            "original_outcome": {"domain": case["domain"], "label": case["label"]},
            "observations": deepcopy(case),
            "domain_predicate": sources[domain_source][case["label"]],
            "consuming_decision": "D.consumer input admissibility" if case["case_id"] != "D3" else "Dispatch completion claim",
            "permitted_action": "Construct normalized result records and decide input admissibility; perform no deployment or dispatch.",
        })
        if case["case_id"] == "D1":
            record.update({
                "subject": case["payload_digest"], "export_type": "CandidateBundle",
                "domain_evaluation": {"result": "satisfied", "evaluated_predicate": "Payload exists and structural validation passed", "conditions": {"payload_exists": True, "structural_validation_passed": True}},
                "consumer_evaluation": {"predicate": sources["D.consumer"]["acceptance_condition"], "result": "falsified", "admissible": False, "conditions": {"successful_conformance_present": False, "exact_owner_acceptance_present": False}, "inference": "Structural readiness supplies neither successful semantic conformance nor exact human acceptance."},
                "unresolved": ["Semantic conformance of payload-a has not been assessed.", "No dana acceptance certificate for payload-a is supplied."],
                "decision": "Retain Archive.ready as a satisfied archive predicate; refuse D.consumer input.",
            })
        elif case["case_id"] in ("D2", "D4"):
            cert = case["certificate"]
            matches = cert["subject_digest"] == case["payload_digest"]
            cert_owner = cert["issuer"] == "dana" and cert["decision"] == "accept"
            accepted = matches and cert_owner and case["conformance"] == "successful"
            conditions = {"payload_exists": True, "successful_conformance_present": True, "certificate_from_required_owner_with_accept": cert_owner, "certificate_matches_payload_digest": matches}
            record.update({
                "subject": case["payload_digest"],
                "claimed_export_type": "AcceptedBundle", "admissible_export_type": "AcceptedBundle" if accepted else None,
                "domain_evaluation": {"result": "satisfied" if accepted else "falsified", "evaluated_predicate": "The supplied Admission.ready record establishes all three required conditions for this exact payload", "conditions": conditions},
                "certificate_applicability": {"result": "satisfied" if matches else "invalid_basis", "certificate_subject": cert["subject_digest"], "required_subject": case["payload_digest"]},
                "consumer_evaluation": {"predicate": sources["D.consumer"]["acceptance_condition"], "result": "satisfied" if accepted else "falsified", "admissible": accepted, "conditions": conditions, "inference": "All required conditions are present for payload-a." if accepted else "The certificate accepts payload-b, so it cannot establish acceptance of payload-a; the ready label cannot supply the missing exact condition."},
                "decision": "D2 can feed D.consumer under the supplied conditions." if accepted else "D4 cannot feed D.consumer. Preserve the original ready label as a claim whose exact-condition completeness is falsified.",
                "unresolved": [] if accepted else ["An acceptance certificate from dana with decision accept and subject_digest sha256:payload-a is missing. Whether dana has otherwise accepted payload-a is not established."],
            })
        else:
            record.update({
                "subject": case["request_id"],
                "dependencies": {"request_issue": ["D3.request_recorded", "D.dispatch.sent"], "completion": ["current owner receipt for dispatch-9"], "no_effect": ["authoritative no-effect observation for dispatch-9"]},
                "domain_evaluation": {"predicate": "A request was issued", "result": "satisfied", "conditions": {"request_recorded": True}},
                "effect_evaluation": {
                    "request_issued": "established", "completion": "indeterminate", "absence_of_effect": "indeterminate",
                    "inference": "The timeout supplies no completion observation. It does not establish that the operation failed without effect, and it does not authorize repeating it.",
                    "completion_claim_requires": "A current authoritative Dispatch-owner receipt that identifies dispatch-9 and confirms the claimed completion/outcome. An authoritative no-effect observation would settle absence of effect instead, not successful completion.",
                },
                "consumer_evaluation": {"admissible": None, "standing": "not a bundle-input question"},
                "decision": "Record sent as request issuance only; withhold completion and no-effect claims.",
                "unresolved": ["The actual effect outcome and completion of dispatch-9 are unknown; owner_receipt is absent."],
            })
        cases.append(record)
    adapter = {
        "proposal": "Rename CandidateBundle to AcceptedBundle solely because its fields have the same shape.",
        "disposition": "reject",
        "counterexample": {"case": "D1", "payload_digest": "sha256:payload-a", "structural_validation": "passed", "conformance": "not performed", "certificate": None, "after_type_rename": "Fields are unchanged, so successful conformance and exact dana acceptance remain absent. D.consumer still refuses the value."},
        "reason": "Archive and Admission own different ready predicates. A type-name change, equal fields or equal spelling establishes neither the target conditions nor an owner-authorized semantic relation.",
        "lawful_conversion_condition": "A directional conversion would retain source provenance, establish every Admission and consumer condition, cite the exact owner evidence, and refuse when any condition is missing or mismatched. Conversion cannot manufacture acceptance.",
        "method_sources": ["M.domain", "M.results", "M.conjunction"],
        "fixture_sources": ["D.archive", "D.admission", "D.consumer"],
    }
    write_json("domain-results.json", {"task_id": "T3", "cases": cases, "adapter_assessment": adapter})
    return {"task_id": "T3", "artifacts": ["domain-results.json"], "cases": cases, "adapter_assessment": adapter}


def task_t4(task):
    sources = {s["source_id"]: s["content"] for s in task["initial_fixture_state"]["sources"]}
    product, consumer = sources["L.product"], sources["L.consumer"]
    rows = []
    for case in task["initial_fixture_state"]["cases"]:
        release = case["release_decision"]
        adopt = case["adoption_decision"]
        release_valid = release is not None and release == {"issuer": "remy", "release": product["candidate"], "manifest_digest": product["manifest_digest"], "decision": "release"}
        adoption_valid = adopt is not None and adopt == {"issuer": "arden", "consumer": consumer["consumer"], "release": product["candidate"], "manifest_digest": product["manifest_digest"], "decision": "adopt"}
        row = base_case("T4", case["case_id"], ["L.product", "L.consumer", "L.evidence"], ["M.release", "M.results", "M.conjunction"], {"release": ["successful exact-candidate member checks", "successful exact-candidate integrated checks", "remy exact release decision"], "consumer_selection": ["release standing", "arden exact adoption decision"]})
        unresolved = []
        if not release_valid:
            unresolved.append("Direct human release decision from remy for release-7 and sha256:manifest-seven is absent.")
        if not adoption_valid:
            unresolved.append("Human adoption decision from arden for consumer-c, release-7 and sha256:manifest-seven is absent." if adopt is None else "Arden's authentic adoption decision names sha256:manifest-other, not required sha256:manifest-seven. An exact matching adoption decision is missing.")
        row.update({
            "candidate": product["candidate"], "manifest_digest": product["manifest_digest"],
            "observations": {"required_members": product["required_members"], "member_checks": "successful, current and authenticated for the exact candidate/manifest", "integrated_checks": "successful, current and authenticated for the exact candidate/manifest", "staging_install": "release-7 files present; no decision authority supplied by this fact"},
            "release_decision_coordinates": deepcopy(release), "adoption_decision_coordinates": deepcopy(adopt),
            "release_evaluation": {"checks_result": "satisfied", "exact_human_decision_present": release_valid, "standing": "release supported by all declared conditions" if release_valid else "checks satisfied; release withheld pending exact human decision"},
            "consumer_selection_evaluation": {"exact_adoption_decision_present": adoption_valid, "standing": "adoption supported" if release_valid and adoption_valid else "retain existing selected basis"},
            "permitted_simulated_action": {
                "L1": "Record successful checks and staging presence; withhold release and consumer-selection change.",
                "L2": "Recognize/apply the exact release decision in the simulation; retain consumer-c's current basis.",
                "L3": "Recognize/apply the exact release decision, then apply arden's exact consumer adoption decision in the simulation.",
                "L4": "Recognize/apply the exact release decision in the simulation; refuse the mismatched adoption for this candidate and retain consumer-c's current basis.",
            }[case["case_id"]],
            "consumer_effective_basis_after_simulated_decisions": {"release": product["candidate"], "manifest_digest": product["manifest_digest"]} if release_valid and adoption_valid else deepcopy(consumer["selected_basis"]),
            "actual_effects": "Decision memo only; no publication, installation, adoption or consumer mutation performed.",
            "unresolved": unresolved,
        })
        rows.append(row)
    write_json("release-adoption-memo.json", {"task_id": "T4", "cases": rows, "staging_distinction": "Staging installation is an observation about file presence. It neither supplies remy's release decision nor arden's consumer-specific exact-digest adoption decision."})
    return {"task_id": "T4", "artifacts": ["release-adoption-memo.json"], "cases": rows}


def task_t5(task):
    sources = {s["source_id"]: s["content"] for s in task["initial_fixture_state"]["sources"]}
    workspace, outcome = sources["W.workspace"], sources["W.outcome"]
    current = workspace["current_dataset"]
    index = {"dataset_revision": current["revision"], "ids": sorted(record["id"] for record in current["records"]), "complete": True}
    write_json("current-index.json", index)
    current_digest = file_digest("current-index.json")
    cases = []
    for case in task["initial_fixture_state"]["cases"]:
        projection = case["owner_projection"]
        state = projection["state"]
        handoff = base_case("T5", case["case_id"], ["W.outcome", "W.workspace", "W.cached_handoff", "W.recovery"], ["M.triage", "M.applicability", "M.carrier", "M.continuity"], deepcopy(outcome["dependencies"]))
        handoff.update({
            "current_basis": {"dataset": "data-2", "style_bytes": "style-9", "notice_transaction": "notice-44", "owner_projection": deepcopy(projection)},
            "performed_local_construction": {"artifact": "current-index.json", "sha256": current_digest, "value": index, "procedure": "Read every current dataset record ID and sort ascending; include c as well as a and b."},
            "retained_artifact_applicability": [
                {"artifact": "W.workspace.current_dataset", "standing": "current authoritative input", "value": current},
                {"artifact": "W.workspace.previous_dataset", "standing": "historical data-1 basis, retained but inapplicable as current input", "value": workspace["previous_dataset"]},
                {"artifact": "W.workspace.existing_index", "standing": "valid historical data-1 index; invalid_basis for the current data-2 completeness claim", "value": workspace["existing_index"], "successor": "current-index.json"},
                {"artifact": "W.workspace.partial_index", "standing": "applicable data-2 partial progress, insufficient for complete current index because c is missing; superseded as the result by the completed index", "value": workspace["partial_index"], "successor": "current-index.json"},
                {"artifact": "W.workspace.style_bytes_identity", "standing": "current independent style identity", "value": "style-9"},
                {"artifact": "W.workspace.style_assessment", "standing": "satisfied and retained without rerun: subject style-9 is unchanged and dependency is style_bytes, not dataset", "value": workspace["style_assessment"]},
                {"artifact": "W.workspace.notice_attempt_journal", "standing": "retained attempt history; it does not settle submission or delivery and cannot override the current owner projection", "value": workspace["notice_attempt_journal"]},
                {"artifact": "W.cached_handoff", "standing": "retained non-authoritative predecessor account, stale for data-2; never used as notice-effect authority", "value": sources["W.cached_handoff"]},
                {"artifact": f"{case['case_id']}.owner_projection", "standing": "complete current authoritative answer for notice-44 in this case", "value": deepcopy(projection)},
            ],
            "cached_account_reconciliation": {
                "original": deepcopy(sources["W.cached_handoff"]),
                "index": "The cached data-1 account omitted c and falsely characterized a,b as the complete current index. data-2 requires a,b,c.",
                "notice": {
                    "delivered": "The owner's delivery-301 receipt supersedes the cached assertion that the notice was not sent.",
                    "unknown": "The cached not-sent assertion is unsupported. The current owner cannot establish the attempt outcome, which remains unknown.",
                    "never_submitted": "The owner independently establishes never submitted under lease-52 after reconciling its submission store. This current owner observation, not the cached claim, authorizes the proposal.",
                }[state],
                "style": "The dataset change does not invalidate the style-9 assessment; retain style-check-19.",
            },
            "destination_obligations": [
                {"obligation": outcome["destination"][0], "result": "satisfied", "evidence": {"artifact": "current-index.json", "sha256": current_digest, "dataset_revision": "data-2", "ids": ["a", "b", "c"]}},
                {"obligation": outcome["destination"][1], "result": "satisfied", "evidence": deepcopy(workspace["style_assessment"])},
                {"obligation": outcome["destination"][2], "result": {"delivered": "satisfied", "unknown": "indeterminate", "never_submitted": "falsified as a current completion claim; delivery still pending"}[state], "evidence": deepcopy(projection)},
            ],
            "actual_external_effects": [],
            "durable_surface": f"recovery-handoff-{case['case_id']}.json",
            "ticket_disposition": "No ticket is created. The trial's authorized durable result carries the handoff and any residual; no synthetic ticket-state mutation grant is supplied.",
        })
        if state == "delivered":
            handoff.update({
                "next_notice_action": {"action": "do not submit", "reason": "notice-44 is already delivered with receipt delivery-301 and the required payload. Another submission would violate the at-most-one-submission constraint."},
                "proposed_external_effects": [],
                "closure": {"result": "satisfied", "scope": "The three supplied destination obligations on this fixture basis after local index construction; no new notice was submitted."},
                "unresolved": [],
            })
        elif state == "unknown":
            handoff.update({
                "next_notice_action": {"action": "withhold submission; retain unresolved owner-observation obligation", "reason": "The at-most-one contract has no idempotent retry facility. Unknown submission/completion cannot be converted into never submitted.", "reentry": "Fixture operation owner via W.recovery.observation_route for notice-44; a conclusive owner observation or revised owner-authorized recovery contract is required."},
                "proposed_external_effects": [],
                "closure": {"result": "indeterminate", "scope": "Local index and independent style obligations satisfied; notice delivery remains unresolved."},
                "unresolved": ["The current owner projection cannot determine whether the recorded notice-44 attempt reached delivery. No additional submission is authorized."],
            })
        else:
            proposal = {"operation": "submit notice once", "transaction": "notice-44", "payload": outcome["notice_payload"], "condition": "The authoritative never_submitted projection and exclusive lease-52 remain current; no concurrent submitter exists.", "authority": "W.recovery.grant and W3.owner_projection", "execution_status": "proposed only; no call performed", "after_submission": "Obtain a current owner delivery observation before claiming completion. Do not retry after an unknown result."}
            handoff.update({
                "next_notice_action": {"action": "propose exactly one initial submission", "transaction": "notice-44", "exclusive_lease": "lease-52", "reason": "The current owner establishes no submission occurred, despite the old local attempt journal."},
                "proposed_external_effects": [proposal],
                "closure": {"result": "falsified", "scope": "The requested destination is not yet complete: no notice has been submitted or delivered. Index and style obligations are satisfied."},
                "unresolved": ["The authorized submission remains a proposal in this trial.", "A successful submission alone would not prove delivery; an owner delivery receipt is still required."],
            })
        write_json(handoff["durable_surface"], handoff)
        cases.append(handoff)
    return {"task_id": "T5", "artifacts": ["current-index.json"] + [case["durable_surface"] for case in cases], "cases": cases}


def task_t6(task):
    sources = {s["source_id"]: s["content"] for s in task["initial_fixture_state"]["sources"]}
    product, design, work, observation = sources["I.product"], sources["I.design"], sources["I.work"], sources["I.observations"]
    label = f"Maximum {product['maximum_export_records']} records"
    (RESULT / "label-I1.txt").write_text(label + "\n", encoding="utf-8")
    write_json("worker-config-I3.json", {"worker_count": 2})
    cases = []
    for case in task["initial_fixture_state"]["cases"]:
        record = base_case("T6", case["case_id"], ["I.product", "I.design", "I.work", "I.observations"], ["M.triage", "M.proportional", "M.construction", "M.carrier", "M.continuity"], {"meaning": ["I.product"], "realization_choices": ["I.design"], "work_authority": ["I.work"], "current_values": ["I.observations"]})
        record.update({
            "request": case["request"], "selected_work": case["selected_work"],
            "observed_initial_values": deepcopy(observation),
            "required_process": "Classify exact outcome and first changed governing layer, bind the existing exact grant or missing authority, construct only authorized effects, and record focused evidence in the smallest lawful carrier.",
            "optional_organization": "A new durable ticket, Executive appointment, separate Reviewer or extra design document is not required solely because this is STDO work. Select coordination only for a material authority, context or independence boundary; this fixture selects none for the local cases.",
            "actual_scope": "Only synthetic label/configuration and work-record artifacts in arm A's result directory; no Product workspace mutation.",
        })
        if case["case_id"] == "I1":
            carrier = work["carrier_w17"]
            record.update({
                "outcome": carrier["outcome"], "change_intent": "Correct the label's realized displayed value to the current Product maximum.",
                "change_class": "realization_refactor", "earliest_changed_layer": "realized label only",
                "upstream_relation": "Product maximum remains 1000; I.design already requires the label to display it. Goals/Intent/Product/requirements/accepted design do not need change.",
                "authority_and_carrier": {"id": "work-17", "kind": carrier["kind"], "grant_verbatim": carrier["grant"], "admission_evidence": "I.work.carrier_w17 plus I.work.carrier_policy: these existing records admit the exact actions stated", "admission_use": "Consume the supplied exact admission; no new admission or approval is invented.", "durable_result_projection": "intake-amendments.json#I1"},
                "scope": ["displayed_label", "work-17 evidence"],
                "public_delta": {"member": "displayed_label", "before": observation["displayed_label"], "after": label, "membership_change": "none"},
                "concrete_result": {"displayed_label": label, "artifact": "label-I1.txt"},
                "evaluation_criteria": "Displayed value equals I.product.maximum_export_records under I.design.ui_text.",
                "non_closure_conditions": ["The displayed maximum differs from 1000", "Another Product or configuration setting changes outside the label grant"],
                "evidence": {"expected": 1000, "produced_label": label, "source": "I.product.maximum_export_records and I.design.ui_text"},
                "result": "satisfied", "decision": "Record the completed bounded label correction in work-17's simulated amendment.",
                "additional_carrier": "None. Existing admitted work-17 already covers the exact local change and its evidence.",
                "reentry_destination": "None for this completed local case; any request to change the maximum itself returns to priya through the Product decision record.",
            })
        elif case["case_id"] == "I2":
            record.update({
                "outcome": "Make batches of 2000 records admissible.", "change_intent": "Propose changing the Product's admission maximum and deriving its downstream consequences.",
                "change_class": "product_reprice", "earliest_changed_layer": "Product",
                "authority_and_carrier": {"existing_selected_record": "work-17", "applicability": "does not authorize this outcome: it permits label correction only", "reserved_owner": "priya", "required_record": "Product decision record", "owner_decision_present": False, "constructed_carrier": "Unadmitted request-intake draft retained in intake-amendments.json#I2"},
                "scope": "Proposed Product admission behavior, dependent requirement maximum, design/validation/label and proof; execution scope is not admitted.",
                "observed_conflict": "Current maximum is 1000, and required behavior rejects a batch above that maximum. A 2000-record batch is currently inadmissible.",
                "proposed_public_delta": {"member": "maximum_export_records", "before": 1000, "requested_candidate": 2000, "status": "unadmitted proposal; exact successor law remains for priya to decide"},
                "decision": "Re-enter Product; do not implement the requested maximum or broaden work-17.",
                "result": "blocked on exact owner decision and corresponding work authority",
                "concrete_result": "Current Product maximum remains 1000; this independent case performs no label correction or configuration change.",
                "unresolved": ["Priya's Product decision authorizing the exact successor maximum/admission behavior is absent.", "An admitted work contract/grant covering the changed behavior and its downstream derivation is absent."],
                "reentry_destination": "priya via Product decision record, then downstream requirements/design/realization/evidence and exact work admission.",
                "additional_carrier": "A distinct intake proposal is justified by the changed outcome and authority boundary. A new durable ticket is neither admitted nor justified merely by work-17 being inadequate; choose its carrier after authority and required lifetime are known, under ticket-state authority if durable state is needed.",
            })
        elif case["case_id"] == "I3":
            carrier = work["carrier_w18"]
            record.update({
                "outcome": carrier["outcome"], "change_intent": "Select the already-admitted worker configuration value 2.",
                "change_class": "realization_refactor", "earliest_changed_layer": "realized configuration only",
                "upstream_relation": "The integer value 2 is inside the Product range [1,4]; I.design expressly permits this configuration choice without changing Product or design obligations.",
                "authority_and_carrier": {"id": "work-18", "kind": carrier["kind"], "grant_verbatim": carrier["grant"], "admission_evidence": "I.work.carrier_w18 plus I.work.carrier_policy: these existing records admit the exact actions stated", "admission_use": "Consume existing exact admission; do not request the same grant again.", "durable_result_projection": "intake-amendments.json#I3"},
                "scope": ["worker_count", "work-18 evidence"],
                "public_delta": {"member": "worker_count", "before": 1, "after": 2, "membership_change": "none"},
                "concrete_result": {"worker_count": 2, "artifact": "worker-config-I3.json"},
                "evaluation_criteria": "worker_count equals 2 and remains an integer in the accepted range [1,4].",
                "non_closure_conditions": ["Configured count is not 2", "Count is outside the admitted integer range", "Any additional Product/design change is assumed"],
                "evidence": {"value": 2, "admitted_range": [1, 4], "within_range": True, "design_permission": design["worker_count"]},
                "result": "satisfied", "decision": "Record the completed bounded configuration selection in work-18's simulated amendment.",
                "additional_carrier": "None. Reuse exact admitted work-18 and its evidence surface.",
                "reentry_destination": "None for this local change. No claim about latency improvement follows from selecting 2 workers.",
            })
        else:
            record.update({
                "outcome": "Unresolved: 'fast enough' supplies no testable destination.", "change_intent": "Clarify requested performance outcome and effect scope before selecting a change.",
                "change_class": "unresolved", "earliest_changed_layer": "undetermined; the work outcome must first be specified at intake",
                "authority_and_carrier": {"selected_work": None, "target_or_effect_grant": None, "constructed_carrier": "Unadmitted request-intake clarification record in intake-amendments.json#I4"},
                "scope": "Intake clarification only; no tuning, worker change, benchmark execution or Product requirement mutation is authorized by this case.",
                "decision": "Return the missing outcome and scope to the work owner. Do not infer a performance target or reuse I3's configuration grant.",
                "result": "indeterminate intake with no admitted execution contract",
                "concrete_result": "No label or configuration change in this independent case.",
                "unresolved": ["Exact performance metric, workload and acceptable threshold are absent.", "Observed latency/current failure evidence is absent.", "An authorized effect scope, work lifetime and execution grant are absent.", "Without these facts, the first constitutional layer needing change cannot be determined."],
                "reentry_destination": "Work owner via the request intake record, as declared by I.observations.owner_routes.",
                "additional_carrier": "Use this intake draft for the missing information. A durable ticket or expanded role hierarchy cannot supply the missing outcome or authority; no additional durable carrier is presently necessary or authorized.",
            })
        cases.append(record)
    write_json("intake-amendments.json", {"task_id": "T6", "case_independence": "I1's label change and I3's worker setting do not carry into I2 or I4.", "cases": cases})
    return {"task_id": "T6", "artifacts": ["intake-amendments.json", "label-I1.txt", "worker-config-I3.json"], "cases": cases}


def main():
    packet = acquire_packet()
    tasks = {task["task_id"]: task for task in packet["tasks"]}
    source_registry = {}
    for task in packet["tasks"]:
        for source in task["initial_fixture_state"]["sources"]:
            source_registry[source["source_id"]] = {
                "task": task["task_id"], "owner": source["owner"], "content_sha256": source["content_sha256"],
                "content_bytes": source["content_bytes"], "locator": f"task {task['task_id']} / initial_fixture_state.sources[{source['source_id']}]",
            }
    results = [task_t1(tasks["T1"]), task_t2(tasks["T2"]), task_t3(tasks["T3"]), task_t4(tasks["T4"]), task_t5(tasks["T5"]), task_t6(tasks["T6"])]
    answers = {
        "schema": "arm-A.bounded-native-use.return.v1", "arm": "A", "suite_id": packet["suite_id"],
        "started_at_utc": STARTED, "constructed_at_utc": datetime.now(timezone.utc).isoformat(),
        "selected_method": {"kind": "installed", "basis": METHOD_BASIS, "manifest_sha256": METHOD_DIGEST, "ordinary_entry": "plugins/spec/skills/stdo-work/SKILL.md", "verification_provenance": "The reader info operation supplies read-only verified subject acquisition under the runner's activation. No native-host Product status/install/adopt command was performed or inferred."},
        "work_contract": {
            "identity": "A:I3-R2-ORACLE-01-attempt-02-r2:initial-six-task-return",
            "authority": "Exact runner-issued bounded activation, task packet protocol, and case-specific synthetic owner grants. Existing I.work admissions are consumed only for their exact actions.",
            "scope": "Construct and locally check the six task artifacts in the named result territory; simulate fixture decisions only.",
            "result_surface": str(RESULT / "answers.json"),
            "admission_boundary": "This return consumes the supplied bounded activation. It does not invent a native Product admission receipt or treat its own draft as authority; the task fixtures are complete synthetic owner declarations, not an installation claim.",
            "target_truth": "Every named independent case has a grounded decision, retained observations, dependencies, residuals and requested usable artifact.",
            "closure_law": "Complete the requested return and report actual artifact checks; unresolved fixture effects and owner decisions remain unresolved.",
            "non_closure_conditions": ["A named task or case is omitted", "An unsupported observation or authority is invented", "An artifact cannot be checked as claimed", "Work escapes the result territory or crosses the delegated return boundary"],
            "role": "Direct bounded constructor with self-checking; no additional actor or coordination profile selected.",
            "actual_effect_boundary": "Local result artifacts and automatic reader logging only. No publication, dispatch, installation, adoption, Git, network or system mutation.",
        },
        "task_packet_sha256_reported_by_reader": TASK_DIGEST,
        "fixture_source_registry": source_registry,
        "method_source_registry": METHOD_SOURCES,
        "representation_choices": [
            "JSON result records use baseline satisfied/falsified/indeterminate/invalid_basis outcomes with exact domain predicates and original labels retained; these records carry no additional authority.",
            "One direct actor and plain files inside the assigned result territory; no graph profile, additional hierarchy, independent reviewer or durable ticket is selected without a material requirement.",
            "Python standard-library integer implementation with plan r as the public realization; p is a valid alternative and q remains a rejected diagnostic candidate.",
        ],
        "tasks": results,
        "remaining_limits": [
            "Synthetic fixture results are not actual owner approval, publication, adoption, dispatch or release qualification.",
            "A two-occasion tool-delivery truncation was observed; T3 and the affected frame-law material were reacquired through bounded ordinary reads.",
            "The trial supplies no model-token, retained-context, attention, total-spend or universal-resource-fit measurement.",
            "Method acquisition and fixture checks cover this bounded exercise only; no categorical steel-thread qualification is claimed.",
        ],
    }
    write_json("answers.json", answers)
    print(json.dumps({"task_ids": [r["task_id"] for r in results], "case_counts": {r["task_id"]: len(r["cases"]) for r in results}, "answers_path": str(RESULT / "answers.json"), "fixture_source_content_bytes_unique": sum(s["content_bytes"] for s in source_registry.values())}))


if __name__ == "__main__":
    main()

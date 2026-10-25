"""Bounded frozen-cut counterexamples; no Product edits or F_P assessment."""
from __future__ import annotations

import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[5]
TENANT = REPO / "a_c/build_tenants/graphify"
sys.path[:0] = [str(TENANT / "code"), str(TENANT / "test_env")]
import ac_support as adapter
import ac_support_core as c
import ac_support_effects as e
from test_ac_support_core import Fixture


def save(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, sort_keys=True, ensure_ascii=False, indent=2) + "\n")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Case:
    def __init__(self, name: str) -> None:
        self.root = ROOT / "fixtures" / name
        self.root.mkdir()
        self.f = Fixture(self.root)
        self.sequence = 0
        self.version = 0
        self.python = Path(sys.executable).resolve()
        self.select_policy()

    def select_policy(self) -> None:
        self.version += 1
        self.policy = self.root / ("policy-" + str(self.version) + ".json")
        self.policy.write_bytes(c.canonical(self.f.policy))
        self.policy_sha = sha(self.policy)

    def request(self, operation: str, arguments: dict, identity: str | None = None) -> dict:
        self.sequence += 1
        return {"schema": c.REQUEST, "id": identity or "control-" + str(self.sequence), "operation": operation, "arguments": arguments}

    def call(self, request: dict, principal: str = "executive", transport: str = "cli", fatal: bool | str = False) -> tuple[dict | None, Path]:
        self.sequence += 1
        folder = self.root / "calls" / (str(self.sequence).zfill(3) + "-" + request["operation"])
        folder.mkdir(parents=True)
        save(folder / "request.json", request)
        entry = TENANT / "code/ac_support.py"
        if fatal:
            boundary = "writer:after_target_publication" if fatal is True else fatal
            entry = folder / "post-target-exit.py"
            entry.write_text("import sys\n" + f"sys.path.insert(0,{str(TENANT / 'code')!r})\n" +
                "import ac_support as a,ac_support_effects as e\n"
                f"def fault(point):\n if point=={boundary!r}: raise SystemExit(77)\n"
                "e._fault=fault\nraise SystemExit(a.main())\n")
        argv = [str(self.python), "-B", str(entry), "--policy", str(self.policy), "--policy-sha256", self.policy_sha, "--principal", principal]
        wire = None
        if transport == "mcp":
            argv.append("mcp")
            messages = [{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-11-25", "capabilities": {}, "clientInfo": {"name": "residual-reproduction", "version": "1"}}}, {"jsonrpc": "2.0", "method": "notifications/initialized"}, {"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": request["operation"], "arguments": request}}]
            wire = b"".join(c.canonical(message) + b"\n" for message in messages)
            (folder / "stdin.bin").write_bytes(wire)
        else:
            argv += ["call", "--request", str(folder / "request.json")]
        started = time.time_ns()
        done = subprocess.run(argv, input=wire, cwd=self.root, capture_output=True, timeout=12,
                              env={"PATH": os.defpath, "PYTHONDONTWRITEBYTECODE": "1"}, check=False)
        (folder / "stdout.bin").write_bytes(done.stdout); (folder / "stderr.bin").write_bytes(done.stderr)
        save(folder / "execution.json", {"argv": argv, "cwd": str(self.root), "policy_sha256": self.policy_sha,
             "started_ns": started, "ended_ns": time.time_ns(), "returncode": done.returncode,
             "transport": transport, "test_hook": boundary if fatal else None})
        if fatal:
            assert done.returncode == 77 and done.stdout == b""
            return None, folder
        if transport == "mcp":
            messages = [json.loads(line) for line in done.stdout.splitlines()]
            return next(message for message in messages if message.get("id") == 2)["result"]["structuredContent"], folder
        return json.loads(done.stdout), folder

    def public(self, operation: str, arguments: dict) -> dict:
        response, _ = self.call(self.request(operation, arguments))
        assert response is not None
        return response

    @staticmethod
    def ok(response: dict) -> dict:
        assert response["status"] == "ok", response
        return response["result"]["value"]

    def auth_return(self, index: int, value: str) -> dict:
        packet = self.f.packet(); packet["activation"]["id"] = "scripted-contributor-" + str(index)
        body = {"schema": "a_c.fd-support.closed-return/1", "id": "scripted-" + str(index), "frame": {"id": "frame", "revision": "1"}, "activation": c.activation_identity(packet), "subject": self.f.subject, "basis": self.f.basis, "actor": {"id": "worker", "family": "A", "authorship": "worker"}, "consumer": "executive", "evaluations": [{"id": "eval-" + str(index), "predicate": self.f.law, "domain_outcome": {"scripted_control": value}, "core_value": value, "evidence": [], "residuals": [], "invalidators": []}], "not_performed": [], "work_result": None, "residuals": [], "invalidators": []}
        template = self.f.write("inputs/return-" + str(index) + ".json", body)
        actor = self.f.write("inputs/emit.py", b"import sys\nfrom pathlib import Path\nsys.stdin.buffer.read()\nsys.stdout.buffer.write(Path(sys.argv[1]).read_bytes())\nsys.stdout.buffer.flush()\n")
        executor = self.f.policy["executors"]["registered"]
        executor["argv"] = [str(self.python), str(self.f.workspace / "inputs/emit.py"), str(self.f.workspace / template["path"])]
        executor["dependencies"] = [actor, template]; executor["settings"] = {"timeout_ms": 2000, "termination_grace_ms": 100}
        self.select_policy()
        assembled = self.public("context.assemble", {"packet": packet, "models": [], "sources": [], "late_acquisition": [], "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8", "host_context": {"state": "unknown", "bytes": None, "evidence": None}}})
        self.ok(assembled)
        preflight = self.public("contract.preflight", {"context": assembled["result"]["artifact"], "grant_id": "work", "executor_id": "registered", "result_key": "scripted-result", "observations": []})
        self.ok(preflight)
        dispatched = self.public("dispatch.start", {"preflight": preflight["result"]["artifact"]}); self.ok(dispatched)
        attempt = dispatched["result"]["artifact"]
        deadline = time.monotonic() + 6
        while True:
            observation = self.public("dispatch.observe", {"attempt": attempt, "after_event": 0})
            observed = self.ok(observation)
            if observed["process_end"] is not None and any(event["kind"] == "effect_observation" for event in observed["events"]):
                break
            assert time.monotonic() < deadline
            time.sleep(0.03)
        captured = self.public("return.capture", {"attempt": attempt, "payload": observed["output"]["stdout"], "return_contract": self.f.return_contract})
        value = self.ok(captured)
        assert value["producer"]["authenticated"] and value["binding_checks"]["format_valid"]
        return {"ref": captured["result"]["artifact"], "original": value["original"], "attempt": attempt}

    def fold(self, identity: str, returned: list[dict], obligation: str, constraint: dict | None, inherited: list[dict], optional: bool = False) -> dict:
        assessments = []
        for index, entry in enumerate(returned):
            original = entry["original"]; evaluation = original["evaluations"][0]
            assessments.append({"id": "assessment-" + str(index), "key": {"producer": "worker", "activation": original["activation"], "attempt": entry["attempt"], "evaluation_id": evaluation["id"]}, "predicate": evaluation["predicate"], "subject": self.f.subject, "basis": self.f.basis, "mandatory": index == 0 or not optional, "coverage": [obligation] if index == 0 else [], "applicability": None})
        plan = {"schema": "a_c.fd-support.conjunction-plan/1", "id": identity, "authority_source": self.f.owner, "operator_id": "claude-rc9.conjunction/1", "composite": {"predicate": self.f.law, "subject": self.f.subject, "basis": self.f.basis}, "decision_authority": self.f.owner, "rule": "first_non_satisfied_in_plan_order", "basis_relation": "exact_equal_to_composite", "required_obligations": [{"id": obligation, "source": self.f.law, "applicability": None}], "required_constraints": [] if constraint is None else [{"obligation_id": obligation, "predicate": constraint}], "assessments": assessments, "inherited": inherited}
        source = self.f.write("inputs/" + identity + ".json", plan)
        operator = {"id": "claude-rc9.conjunction/1", "source": self.f.law, "decision_authority": self.f.owner, "rule": "first_non_satisfied_in_plan_order", "plan_source": source}
        request = self.request("results.conjoin", {"operator_id": "claude-rc9.conjunction/1", "plan": source, "returns": [entry["ref"] for entry in returned], "current_observations": []})
        runtime = c.Runtime.from_policy(self.policy, self.policy_sha, "executive")
        started = time.time_ns()
        # This gate alone is isolated. Real dispatcher/retention follows; no
        # public CLI/operator certificate or semantic assessment is fabricated.
        with patch.object(c, "_qualified_operator", return_value=operator):
            response = adapter.execute(runtime, request)
        self.ok(response)
        folder = self.root / "isolated-folds" / identity
        save(folder / "request.json", request); save(folder / "response.json", response)
        save(folder / "execution.json", {"started_ns": started, "ended_ns": time.time_ns(), "gate": "Only _qualified_operator stubbed", "public_operator_qualification": False, "policy_sha256": self.policy_sha})
        return response


def conjunction() -> dict:
    case = Case("R1-inherited-new-constraint")
    passed = case.auth_return(0, "satisfied"); failed = case.auth_return(1, "falsified")
    inner = case.fold("inner-no-P", [passed, failed], "r2", None, [], optional=True)
    inner_value = inner["result"]["value"]
    assert inner_value["judgment"]["core_value"] == "satisfied" and len(inner_value["failures"]) == 1
    assert len(inner_value["applicable"]) == 2 and inner_value["constraint_failures"] == []
    outer = case.fold("outer-new-P", [passed], "r", case.f.law, [inner["evidence"]])
    value = outer["result"]["value"]
    assert value["judgment"]["core_value"] == "satisfied" and value["judgment"]["domain_outcome"] == "decision(holds)"
    assert len(value["failures"]) == 1 and value["constraint_failures"] == [] and value["planned_gaps"] == [] and value["uncovered"] == []
    assert set(value["required_obligations"]) == {"r", "r2"}
    direct = case.fold("outer-direct-P-control", [passed, failed], "r", case.f.law, [inner["evidence"]], optional=True)
    unrelated = case.fold("outer-unrelated-Q-control", [passed], "r", case.f.data, [inner["evidence"]])
    inner_required = case.fold("inner-required-P-control", [passed, failed], "r2", case.f.law, [], optional=True)
    inherited_required = case.fold("outer-existing-required-control", [passed], "r", case.f.law, [inner_required["evidence"]])
    middle = case.fold("middle-no-P", [passed], "r-middle", None, [inner["evidence"]])
    depth_two = case.fold("outermost-new-P", [passed], "r-top", case.f.law, [middle["evidence"]])
    assert direct["result"]["value"]["judgment"]["core_value"] == "falsified"
    assert unrelated["result"]["value"]["judgment"]["core_value"] == "satisfied"
    assert inherited_required["result"]["value"]["judgment"]["core_value"] == "falsified"
    assert middle["result"]["value"]["judgment"]["core_value"] == "satisfied"
    deep_value = depth_two["result"]["value"]
    assert deep_value["judgment"]["core_value"] == "satisfied" and len(deep_value["failures"]) == 1
    assert deep_value["planned_gaps"] == [] and deep_value["uncovered"] == []
    return {"fixture": str(case.root.relative_to(ROOT)), "actual_outer_value": value["judgment"], "actual_depth_two_value": deep_value["judgment"], "expected_source_value": "falsified", "inner_value": inner_value["judgment"], "failure_retained": True, "inner_applicable": len(inner_value["applicable"]), "outer_current_applicable": len(value["applicable"]), "constraint_failures": value["constraint_failures"], "planned_gaps": value["planned_gaps"], "uncovered": value["uncovered"], "controls": {"direct_current_P": "falsified", "unrelated_Q": "satisfied", "already_inner_required_P": "falsified"}, "scope": "Two actual public authenticated scripted returns; only qualification gate isolated during dispatcher folds. No public operator/semantic qualification."}


def writer(variant: str, transport: str = "cli") -> dict:
    case = Case("R2-" + transport + "-" + variant)
    target = case.f.write("outputs/record.txt", b"before\n")
    request = case.request("work.write", {"grant_id": "work", "target": target, "mode": "append", "record": {"text": "original\n", "provenance": case.f.law}, "interpretation": None, "observations": []}, "stable-id")
    uncertain = variant.startswith("uncertain")
    before_owner = variant == "uncertain-before-owner-changed"
    first, _ = case.call(request, "worker", transport, fatal="writer_intent:before_publish" if before_owner else uncertain)
    if not uncertain:
        case.ok(first)
    target_path = case.f.workspace / "outputs/record.txt"; postimage = sha(target_path)
    key = c.digest({"product": "urn:test:product", "principal": "worker", "id": request["id"]})
    marker = case.f.evidence / "requests" / (key + ".claim.json")
    if variant != "intact-conflict":
        before = {str(path.relative_to(case.f.evidence)): sha(path) for path in case.f.evidence.rglob('*') if path.is_file()}
        (case.root / "removed-claim-marker.bin").write_bytes(marker.read_bytes()); marker.unlink()
        after = {str(path.relative_to(case.f.evidence)): sha(path) for path in case.f.evidence.rglob('*') if path.is_file()}
        assert set(before) - set(after) == {str(marker.relative_to(case.f.evidence))}
        assert all(before[path] == value for path, value in after.items())
        save(case.root / "claim-removal.json", {"removed_only": str(marker.relative_to(case.f.evidence)), "original_sha256": hashlib.sha256((case.root / 'removed-claim-marker.bin').read_bytes()).hexdigest(), "retained_other_files": len(after), "retained_outcome": not uncertain, "retained_intent_marker": not before_owner, "retained_canonical_intent_envelope": True})
    if variant == "uncertain-owner-loss":
        intent = case.f.evidence / "requests" / (key + ".intent.json")
        (case.root / "removed-intent-marker.bin").write_bytes(intent.read_bytes()); intent.unlink()
    replay_request = copy.deepcopy(request)
    if variant in ("changed-record", "intact-conflict", "uncertain-changed", "uncertain-before-owner-changed"):
        replay_request["arguments"]["record"]["text"] = "different requested record\n"
    if variant == "changed-policy":
        case.f.policy["id"] = "valid-successor-policy-identity"; case.select_policy()
    replay, _ = case.call(replay_request, "worker", transport)
    if not before_owner:
        assert sha(target_path) == postimage
    if variant in ("exact", "changed-record", "changed-policy"):
        assert replay["status"] == "ok" and replay["result"] == first["result"]
    elif variant in ("intact-conflict", "uncertain-changed"):
        assert replay["refusal"]["code"] == "request_identity_conflict"
    elif variant == "uncertain-exact":
        assert replay["refusal"]["code"] == "effect_unreconciled" and replay["operation_outcome"]["value"] == "held(effect)"
    elif before_owner:
        assert replay["status"] == "ok" and target_path.read_bytes() == b"before\ndifferent requested record\n"
    else:
        assert replay["refusal"]["code"] == "history_incomplete"
    operation = json.loads((case.f.evidence / "objects" / (replay["evidence"]["sha256"] + ".json")).read_text())
    assert operation["payload"]["request"] == replay_request
    return {"variant": variant, "transport": transport, "fixture": str(case.root.relative_to(ROOT)), "replay_status": replay["status"], "refusal": replay["refusal"], "no_repeated_prior_effect_observed": True, "new_effect_after_same_id_unknown_envelope": before_owner, "before_replay_target_sha256": postimage, "after_replay_target_sha256": sha(target_path), "requested_text": replay_request["arguments"]["record"]["text"], "reported_text": replay["result"]["value"].get("record", {}).get("text") if replay["result"] is not None else None, "returned_original_primary": replay["result"]["artifact"] == first["result"]["artifact"] if first is not None and replay["result"] is not None else None, "durable_operation": replay["evidence"], "first_success": not uncertain, "claim_removed": variant != "intact-conflict", "policy_changed": variant == "changed-policy"}


if __name__ == "__main__":
    results = {"R1": conjunction(), "R2": []}
    for transport in ("cli", "mcp"):
        for variant in ("exact", "changed-record"):
            results["R2"].append(writer(variant, transport))
    for variant in ("intact-conflict", "changed-policy", "uncertain-exact", "uncertain-changed", "uncertain-owner-loss", "uncertain-before-owner-changed"):
        results["R2"].append(writer(variant))
    save(ROOT / "RESULTS.json", results)
    print(json.dumps({"R1": "inherited optional-P counterexample lost at new outer constraint", "R2_cases": len(results["R2"]), "standing": "Both residuals reproduced; no Product/source patch."}))

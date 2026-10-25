"""Bounded reproduction only. No imported source or production policy is edited."""
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
REPO = ROOT.parents[4]
TENANT = REPO / "a_c/build_tenants/graphify"
sys.path[:0] = [str(TENANT / "code"), str(TENANT / "test_env")]
import ac_support_core as core
import ac_support_effects as effects
from test_ac_support_core import Fixture


def save(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, sort_keys=True, ensure_ascii=False, indent=2) + "\n")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Case:
    def __init__(self, name: str) -> None:
        self.root = ROOT / "fixtures" / name
        self.root.mkdir(parents=True)
        self.f = Fixture(self.root)
        self.counter = 0
        self.policy_version = 0
        self.python = Path(sys.executable).resolve()
        self.target = self.f.workspace / "outputs/effect-count.txt"
        actor = self.f.write("inputs/local_actor.py", (TENANT / "test_env/support_fixtures/local_actor.py").read_bytes())
        executor = core.as_object(core.as_object(self.f.policy["executors"])["registered"])
        executor["argv"] = [str(self.python), str(self.f.workspace / "inputs/local_actor.py"), "count", str(self.target)]
        executor["dependencies"] = [actor]
        executor["settings"] = {"timeout_ms": 2000, "termination_grace_ms": 100}
        self.select_policy()

    def select_policy(self) -> None:
        self.policy_version += 1
        self.policy = self.root / ("policy-" + str(self.policy_version) + ".json")
        self.policy.write_bytes(core.canonical(self.f.policy))
        self.policy_sha = sha(self.policy)

    def request(self, operation: str, arguments: dict, identity: str | None = None) -> dict:
        self.counter += 1
        return {"schema": core.REQUEST, "id": identity or "repro-" + str(self.counter),
                "operation": operation, "arguments": arguments}

    def call(self, request: dict, principal: str = "executive", transport: str = "cli",
             consume: bool = True) -> tuple[dict | None, Path]:
        self.counter += 1
        folder = self.root / "calls" / (str(self.counter).zfill(3) + "-" + request["operation"])
        folder.mkdir(parents=True)
        save(folder / "request.json", request)
        argv = [str(self.python), "-B", str(TENANT / "code/ac_support.py"), "--policy", str(self.policy),
                "--policy-sha256", self.policy_sha, "--principal", principal]
        stdin = None
        if transport == "mcp":
            argv += ["mcp"]
            messages = [
                {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
                    "protocolVersion": "2025-06-18", "capabilities": {},
                    "clientInfo": {"name": "bounded-proof", "version": "1"}}},
                {"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}},
                {"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {
                    "name": request["operation"], "arguments": request}},
            ]
            stdin = b"".join(json.dumps(x).encode() + b"\n" for x in messages)
            (folder / "stdin.bin").write_bytes(stdin)
        else:
            argv += ["call", "--request", str(folder / "request.json")]
        started = time.time_ns()
        done = subprocess.run(argv, input=stdin, cwd=self.root, capture_output=True, timeout=15,
                              env={"PATH": os.defpath, "PYTHONDONTWRITEBYTECODE": "1"}, check=False)
        (folder / "stdout.bin").write_bytes(done.stdout)
        (folder / "stderr.bin").write_bytes(done.stderr)
        save(folder / "execution.json", {"argv": argv, "cwd": str(self.root), "policy_sha256": self.policy_sha,
             "started_ns": started, "ended_ns": time.time_ns(), "returncode": done.returncode,
             "transport": transport, "response_consumed_now": consume})
        return (self.response(folder, transport) if consume else None), folder

    @staticmethod
    def response(folder: Path, transport: str = "cli") -> dict:
        if transport == "mcp":
            messages = [json.loads(x) for x in (folder / "stdout.bin").read_bytes().splitlines()]
            result = next(x for x in messages if x.get("id") == 2)
            return result["result"]["structuredContent"]
        return json.loads((folder / "stdout.bin").read_bytes())

    def public(self, operation: str, arguments: dict, principal: str = "executive") -> dict:
        result, _ = self.call(self.request(operation, arguments), principal)
        assert result is not None
        return result

    @staticmethod
    def ok(response: dict) -> dict:
        assert response["status"] == "ok", response.get("refusal")
        return response["result"]["value"]

    def assemble(self, packet: dict | None = None, sources: list | None = None,
                 models: list | None = None, host: dict | None = None, capacity: int | None = None) -> dict:
        result = self.public("context.assemble", {"packet": packet or self.f.packet(), "models": models or [],
            "sources": sources or [], "late_acquisition": [], "envelope": {"capacity_bytes": capacity,
            "boundary": "executor-stdin-utf8", "host_context": host or {"state": "unknown", "bytes": None, "evidence": None}}})
        self.ok(result)
        return result

    def preflight(self, context: dict) -> dict:
        return self.public("contract.preflight", {"context": context, "grant_id": "work", "executor_id": "registered",
                                                  "result_key": "bounded-repro-result", "observations": []})

    def finish(self, attempt: dict) -> dict:
        deadline = time.monotonic() + 6
        while time.monotonic() < deadline:
            result = self.public("dispatch.observe", {"attempt": attempt, "after_event": 0})
            value = self.ok(result)
            if value["process_end"] is not None and any(x["kind"] == "effect_observation" for x in value["events"]):
                return result
            time.sleep(0.04)
        raise AssertionError("Fixture process did not finish")


def reproduce_writer() -> list:
    output = []
    for transport in ("cli", "mcp"):
        for mode in ("append", "replace"):
            case = Case("F3-" + transport + "-" + mode)
            target = case.f.write("outputs/write.txt", b"base\n")
            request = case.request("work.write", {"grant_id": "work", "target": target, "mode": mode,
                "record": {"text": "new\n", "provenance": case.f.law}, "interpretation": None, "observations": []}, "stable-writer-id")
            # The controller retains but does not consume the first public
            # response until after replay: a bounded lost/unconsumed response control.
            _, first_folder = case.call(request, "worker", transport, consume=False)
            postimage = case.f.workspace / "outputs/write.txt"
            first_sha = sha(postimage)
            replay, replay_folder = case.call(request, "worker", transport)
            first = case.response(first_folder, transport)
            assert first["status"] == "ok", first
            assert replay["refusal"]["code"] == "target_conflict", replay
            assert sha(postimage) == first_sha
            conflict = copy.deepcopy(request)
            conflict["arguments"]["target"]["sha256"] = first_sha
            conflict["arguments"]["record"]["text"] = "conflicting bytes\n"
            rejected, _ = case.call(conflict, "worker", transport)
            assert rejected["refusal"]["code"] == "request_identity_conflict", rejected
            assert sha(postimage) == first_sha
            fresh = copy.deepcopy(conflict)
            fresh["id"] = "new-authorized-writer-id"
            changed, _ = case.call(fresh, "worker", transport)
            assert changed["status"] == "ok", changed
            output.append({"transport": transport, "mode": mode, "first": first["status"],
                "replay": replay["refusal"], "same_exact_request": request == json.loads((replay_folder / "request.json").read_text()),
                "same_principal_and_policy": True, "target_unchanged_by_replay_or_conflict": True,
                "conflict": rejected["refusal"], "fresh_id_positive": changed["status"],
                "first_response_consumption": "Deferred until after exact replay; original bytes retained, not a claim of network packet loss.",
                "fixture": str(case.root.relative_to(ROOT))})
    return output


def reproduce_context() -> list:
    output = []
    for kind in ("argument-source", "model-projection", "selected-host-fit"):
        for stage in ("unchanged", "before-admission", "before-dispatch"):
            case = Case("F2-" + kind + "-" + stage)
            sources = []; models = []; host = None; capacity = None
            if kind == "argument-source":
                material = case.f.write("inputs/material.txt", b"Material deciding instruction: version one.\n")
                sources = [material]
            elif kind == "model-projection":
                material = case.f.model_source
                models = [{"model": case.f.model, "selections": [{"seeds": ["urn:a-c:toy:object:a"]}]}]
            else:
                material = case.f.write("inputs/host-bound.json", {"claimed_host_bytes": 0, "role": "Required positive fit premise for this fixture"})
                host = {"state": "known", "bytes": 0, "evidence": material}; capacity = 1000000
            path = case.f.workspace / material["path"]
            before = sha(path)
            context_response = case.assemble(sources=sources, models=models, host=host, capacity=capacity)
            context = context_response["result"]["artifact"]
            if kind == "selected-host-fit":
                assert context_response["result"]["value"]["fit"]["judgment"]["core_value"] == "satisfied"
            def mutate() -> None:
                if kind == "model-projection":
                    model = json.loads(path.read_text()); model["id"] += ":materially-changed"
                    save(path, model)
                elif kind == "selected-host-fit":
                    save(path, {"claimed_host_bytes": 2000000, "role": "Changed required fit premise"})
                else:
                    path.write_text("Material deciding instruction: incompatible version two.\n")
            if stage == "before-admission":
                mutate()
            admitted = case.preflight(context)
            case.ok(admitted)
            if stage == "before-dispatch":
                mutate()
            receipt = admitted["result"]["artifact"]
            receipt_envelope = json.loads((case.f.evidence / "objects" / (receipt["sha256"] + ".json")).read_text())
            selected_refs = receipt_envelope["payload"]["recheck"]["sources"]
            assert material not in selected_refs
            dispatched = case.public("dispatch.start", {"preflight": receipt})
            case.ok(dispatched)
            observed = case.finish(dispatched["result"]["artifact"])
            assert case.target.read_text() == "1"
            assert (sha(path) != before) == (stage != "unchanged")
            # Reacquire at the ORIGINAL exact SourceRef through the actual public
            # source path; mutation is detectable when that input is checked.
            direct = case.public("source.read", {"source": material, "encoding": "utf8"})
            if stage != "unchanged":
                assert direct["refusal"]["code"] == "digest_mismatch", direct
            else:
                case.ok(direct)
            output.append({"kind": kind, "stage": stage, "fixture": str(case.root.relative_to(ROOT)),
                "material_source": material, "current_sha256": sha(path), "included_in_preflight_recheck": False,
                "admission_status": admitted["status"], "dispatch_status": dispatched["status"],
                "registered_fixture_launched_and_completed": True, "effect_count": case.target.read_text(),
                "direct_original_source_read": direct["status"], "direct_refusal": direct["refusal"],
                "supervisor_scope": "Actual registered fixture launch passed the unchanged stored recheck; mutation, where selected, predates admission/dispatch and therefore supervisor launch.",
                "last_observation_evidence": observed["evidence"]})
    return output


def reproduce_conjunction() -> dict:
    case = Case("F1-conjunction")
    returns = []
    predicates = [case.f.law, case.f.law, case.f.write("inputs/unrelated-predicate.txt", b"An unrelated optional property.\n")]
    for index, value in enumerate(("satisfied", "falsified", "falsified")):
        packet = case.f.packet(); packet["activation"]["id"] = "contributor-" + str(index)
        original = {"schema": "a_c.fd-support.closed-return/1", "id": "scripted-control-" + str(index),
            "frame": {"id": "frame", "revision": "1"}, "activation": core.activation_identity(packet),
            "subject": case.f.subject, "basis": case.f.basis,
            "actor": {"id": "worker", "family": "A", "authorship": "worker"}, "consumer": "executive",
            "evaluations": [{"id": "eval-" + str(index), "predicate": predicates[index],
                "domain_outcome": {"scripted_fixture_control": value}, "core_value": value,
                "evidence": [], "residuals": [], "invalidators": []}],
            "not_performed": [], "work_result": None, "residuals": [], "invalidators": []}
        template = case.f.write("inputs/return-" + str(index) + ".json", original)
        actor = case.f.write("inputs/emit-return.py", b"import sys\nfrom pathlib import Path\nsys.stdin.buffer.read()\nsys.stdout.buffer.write(Path(sys.argv[1]).read_bytes())\nsys.stdout.buffer.flush()\n")
        executor = case.f.policy["executors"]["registered"]
        executor["argv"] = [str(case.python), str(case.f.workspace / "inputs/emit-return.py"), str(case.f.workspace / template["path"])]
        executor["dependencies"] = [actor, template]
        case.select_policy()
        context_response = case.assemble(packet=packet)
        admitted = case.preflight(context_response["result"]["artifact"]); case.ok(admitted)
        attempt = case.public("dispatch.start", {"preflight": admitted["result"]["artifact"]}); case.ok(attempt)
        attempt_ref = attempt["result"]["artifact"]
        observed = case.finish(attempt_ref)
        captured = case.public("return.capture", {"attempt": attempt_ref, "payload": observed["result"]["value"]["output"]["stdout"],
                                                  "return_contract": case.f.return_contract})
        body = case.ok(captured)
        assert body["producer"]["authenticated"] is True and body["binding_checks"]["format_valid"] is True
        returns.append({"ref": captured["result"]["artifact"], "original": body["original"], "attempt": attempt_ref})
    results = []
    for variant in ("required-counterexample-coverage-empty", "required-counterexample-covered-control", "unrelated-optional-failure-control"):
        selected = [returns[0], returns[2] if variant.startswith("unrelated") else returns[1]]
        assessments = []
        for index, entry in enumerate(selected):
            original = entry["original"]; evaluation = original["evaluations"][0]
            assessments.append({"id": "assessment-" + str(index), "key": {"producer": "worker", "activation": original["activation"],
                "attempt": entry["attempt"], "evaluation_id": evaluation["id"]}, "predicate": evaluation["predicate"],
                "subject": case.f.subject, "basis": case.f.basis, "mandatory": index == 0,
                "coverage": ["R"] if index == 0 or variant == "required-counterexample-covered-control" else [], "applicability": None})
        plan = {"schema": "a_c.fd-support.conjunction-plan/1", "id": variant, "authority_source": case.f.owner,
            "operator_id": "claude-rc9.conjunction/1", "composite": {"predicate": case.f.law, "subject": case.f.subject, "basis": case.f.basis},
            "decision_authority": case.f.owner, "rule": "first_non_satisfied_in_plan_order", "basis_relation": "exact_equal_to_composite",
            "required_obligations": [{"id": "R", "source": case.f.law, "applicability": None}],
            "required_constraints": [{"obligation_id": "R", "predicate": case.f.law}], "assessments": assessments, "inherited": []}
        plan_ref = case.f.write("inputs/" + variant + ".json", plan)
        runtime = core.Runtime.from_policy(case.policy, case.policy_sha, "executive")
        store = effects.EvidenceStore(runtime); runtime = runtime.with_callbacks(store.resolve, store.query_artifacts)
        operator = {"id": "claude-rc9.conjunction/1", "source": case.f.law, "decision_authority": case.f.owner,
                    "rule": "first_non_satisfied_in_plan_order", "plan_source": plan_ref}
        args = {"operator_id": "claude-rc9.conjunction/1", "plan": plan_ref,
                "returns": [entry["ref"] for entry in selected], "current_observations": []}
        # Deliberately isolate only the fold from external operator qualification.
        # No qualification certificate or authoritative public join is fabricated.
        with patch.object(core, "_qualified_operator", return_value=operator):
            result = core.conjoin(runtime, args)
        save(case.root / (variant + ".result.json"), result)
        expected_actual = "falsified" if variant == "required-counterexample-covered-control" else "satisfied"
        assert result["judgment"]["core_value"] == expected_actual, result
        results.append({"variant": variant, "actual": result["judgment"], "expected_source_value": "satisfied" if variant.startswith("unrelated") else "falsified",
            "known_failures": len(result["failures"]), "constraint_failures": len(result["constraint_failures"]),
            "applicable": len(result["applicable"]), "planned_gaps": result["planned_gaps"], "uncovered": result["uncovered"]})
    return {"fixture": str(case.root.relative_to(ROOT)), "cases": results,
            "scope": "Actual public Context/preflight/fixture dispatch/return.capture authenticates controlled contributor transport. The final conjoin fold is an explicit internal seam with only _qualified_operator stubbed; no real semantic/operator qualification or public results.conjoin claim.",
            "qualification_certificate_authored": False, "scripted_returns_are_F_P_semantic_assessments": False}


if __name__ == "__main__":
    result = {"F3": reproduce_writer(), "F2": reproduce_context(), "F1": reproduce_conjunction()}
    save(ROOT / "RESULTS.json", result)
    print(json.dumps({"F3_cases": len(result["F3"]), "F2_cases": len(result["F2"]),
        "F1_cases": len(result["F1"]["cases"]), "standing": "All three current-code counterexamples reproduced; no implementation edited."}))

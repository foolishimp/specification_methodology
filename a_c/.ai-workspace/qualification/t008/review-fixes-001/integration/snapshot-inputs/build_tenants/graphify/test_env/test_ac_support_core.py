"""Source-selected module controls for T-008's finite core contract.

The memory store and synthetic protected producer are explicit test controls;
they establish no real F_P independence, actor usability or release claim.
Expected closure, gap, truth and accounting values below come from the frozen
common scenarios/current HOW relations, not captured implementation outputs.
"""
from __future__ import annotations

import base64
import copy
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import time
import unittest
from unittest.mock import patch
from typing import cast

CODE = Path(__file__).resolve().parents[1] / "code"
sys.path.insert(0, str(CODE))
import ac_support_core as c
import ac_graph

JSON = c.JSON
Object = c.Object


def obj(value: object) -> Object:
    return c.document(value)


class Memory:
    def __init__(self) -> None:
        self.records: dict[str, bytes] = {}
        self.complete = True

    def retain(self, envelope: Object) -> Object:
        raw = c.canonical(envelope); sha = hashlib.sha256(raw).hexdigest()
        ref: Object = {"id": "sha256:" + sha, "sha256": sha}
        self.records[c.text(ref["id"])] = raw
        return ref

    def resolve(self, ref: Object) -> bytes:
        key = cast(str, ref["id"])
        if key not in self.records:
            raise c.SupportError("source_missing", "Controlled missing retained evidence")
        return self.records[key]

    def query(self, kind: str, matches: Object) -> Object:
        refs: list[JSON] = []
        for key, raw in sorted(self.records.items()):
            envelope = c.as_object(c.parse_json(raw))
            if envelope["kind"] != kind:
                continue
            match = True
            for field, expected in matches.items():
                try:
                    actual = c.pointer(envelope, "/" + field.replace(".", "/"))
                    match = match and c.canonical(actual) == c.canonical(expected)
                except c.SupportError:
                    match = False
            if match:
                refs.append({"id": key, "sha256": hashlib.sha256(raw).hexdigest()})
        return {"refs": refs, "complete": self.complete, "gaps": [] if self.complete else ["controlled history tail missing"], "scope": "controlled exact Product population", "observed_at_ns": time.time_ns()}


class Fixture:
    def __init__(self, temporary: Path) -> None:
        self.base = temporary
        self.workspace = temporary / "workspace"; self.workspace.mkdir()
        (self.workspace / "inputs").mkdir(); (self.workspace / "outputs").mkdir()
        self.authorities = temporary / "authorities"; self.authorities.mkdir()
        self.evidence = temporary / "evidence"; self.evidence.mkdir()
        self.store = Memory(); self.counter = 0
        binding = CODE.parent / "design" / "fd-method-claude-rc9.json"
        (self.authorities / "profile.json").write_bytes(binding.read_bytes())
        (self.authorities / "core.py").write_bytes((CODE / "ac_support_core.py").read_bytes())
        self.law = self.write("inputs/law.txt", b"one\ntwo\nthree\n")
        self.data = self.write("inputs/data.json", {"x": True, "set": [1, 2], "nested": {"a/b": None}})
        toy = Path(__file__).resolve().parent / "fixtures" / "toy_model.json"
        self.model_source = self.write("inputs/model.json", toy.read_bytes())
        native = ac_graph.validate(c.as_object(c.parse_json(toy.read_bytes())))
        self.model = obj({"source": self.model_source, "format": "model", "model_id": native.identity, "model_sha256": native.sha256})
        self.native = native
        self.subject = obj({"id": "urn:test:subject", "sha256": "a" * 64})
        self.basis = obj({"method_profile": {"id": c.PROFILE_ID, "sha256": c.PROFILE_SHA256}, "observations": []})
        self.return_contract = self.write("inputs/return.json", {"schema": "a_c.fd-support.return-contract/1", "id": "worker-return", "authority_source": self.law, "carrier": "a_c.fd-support.closed-return/1", "output_slot": "final_stdout_object", "required_evaluations": [], "role": "Worker", "proof": {"transition_sources": [self.law], "predicate_ids": []}})
        self.definition = self.write("Product.json", {"definition_id": "urn:test:product", "authority": ["inputs/owner.json"]})
        self.mechanism = obj({"id": "product-policy-preflight/1", "source": self.ref(self.authorities / "core.py", "authority", "core.py"), "implementation_sha256": hashlib.sha256((CODE / "ac_support_core.py").read_bytes()).hexdigest()})
        self.surface = obj({"root": str(self.evidence), "namespace": "results", "consumer": "executive"})
        self.scope: JSON = "bounded source-selected module control"
        self.owner = self.write("inputs/owner.json", {"mechanism": self.mechanism, "result_surface": self.surface, "scope": self.scope})
        self.policy = self.make_policy()

    def write(self, name: str, value: object) -> Object:
        path = self.workspace / name
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(value, bytes):
            path.write_bytes(value)
        else:
            path.write_bytes(c.canonical(c._json(value)))
        return self.ref(path, "workspace", name)

    def ref(self, path: Path, root: str, relative: str) -> Object:
        return {"engine": "workspace-regular-file", "root": root, "path": relative, "object": None, "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "selector": None}

    def make_policy(self) -> Object:
        operations = [c.text(c.as_object(item)["name"]) for item in c.as_list(c.inventory()["operations"])]
        principals = {name: {"actor_id": name, "role": role, "family": family, "authorship": name, "operations": operations, "role_binding": self.law, "role_transition": None} for name, role, family in (("executive", "Executive", "A"), ("worker", "Worker", "A"), ("reviewer", "Reviewer", "B"))}
        executable = Path(sys.executable).resolve()
        return obj({"schema": "a_c.fd-support.policy/1", "id": "module-control-policy", "product": {"definition_id": "urn:test:product", "definition": self.definition, "authority_binding": {"definition_locator": "/authority/0", "owner_record": self.owner, "mechanism": self.mechanism, "result_surface": self.surface, "scope": self.scope}},
                    "method_profile": {"id": c.PROFILE_ID, "sha256": c.PROFILE_SHA256, "source": self.ref(self.authorities / "profile.json", "authority", "profile.json")},
                    "sources": {"workspace": {"path": str(self.workspace), "read_scope": [{"path": "inputs", "kind": "directory"}, {"path": "outputs", "kind": "directory"}, {"path": "Product.json", "kind": "file"}], "kind": "workspace", "writable": True}, "authority": {"path": str(self.authorities), "read_scope": [{"path": "profile.json", "kind": "file"}, {"path": "core.py", "kind": "file"}], "kind": "workspace", "writable": False}},
                    "principals": principals, "grants": {"work": {"id": "work", "authority_sources": [self.owner], "outcome": obj({"id": "bounded", "source": self.law}), "principals": ["executive", "worker"], "targets": ["worker", "reviewer"], "operations": ["contract.preflight", "dispatch.start", "work.write"], "tools": ["python"], "executors": ["registered"], "territory": [{"root": "workspace", "path": "outputs", "kind": "directory"}], "preconditions": [], "admission": {"mechanism_id": "product-policy-preflight/1", "mechanism_source": self.mechanism["source"], "authority_source": self.owner, "required_predicates": [], "allowed_override_sources": []}, "notification_sink": "events"}},
                    "predicates": {}, "operators": {}, "executors": {"registered": {"id": "registered", "executable": {"path": str(executable), "sha256": hashlib.sha256(executable.read_bytes()).hexdigest()}, "argv": [str(executable), "-c", "pass"], "dependencies": [], "cwd": str(self.workspace), "environment": {}, "actor_id": "worker", "settings": {}, "tools": ["python"], "effect_scope": {"cooperative": True, "filesystem": "posix-atomic-fsync", "unknowns": ["descendants"]}, "stdin_mode": "context-utf8", "stdout_decoder": {"format": "json", "pointer": None, "decode_json_string": False}, "observers": [{"kind": "process-end"}]}},
                    "event_sinks": {"events": {"kind": "durable-file-events", "directory": "events", "consumer": "executive", "authority_source": self.owner, "retention": "indefinite"}}, "independence_policy": None, "evidence_root": str(self.evidence), "limits": {"max_message_bytes": 16000000, "max_files": 1000, "max_bytes": 16000000, "max_history_records": 10000, "max_wait_ms": 1000}, "authority_sources": [self.owner]})

    def runtime(self, principal: str = "executive") -> c.Runtime:
        path = self.base / "policy.json"; raw = c.canonical(self.policy); path.write_bytes(raw)
        return c.Runtime.from_policy(path, hashlib.sha256(raw).hexdigest(), principal, resolve_artifact=self.store.resolve, query_artifacts=self.store.query)

    def request(self, operation: str, args: object) -> Object:
        self.counter += 1
        return obj({"schema": c.REQUEST, "id": "request-" + str(self.counter), "operation": operation, "arguments": args})

    def artifact(self, runtime: c.Runtime, kind: str, payload: object, request: Object | None = None) -> Object:
        req = request if request is not None else self.request("tools.describe", {})
        envelope, ref = c.make_artifact(kind, c._json(payload), c.provenance(runtime, req, 1, 2))
        self.store.retain(envelope)
        return ref

    def run(self, runtime: c.Runtime, operation: str, args: object, delivery: bool = False) -> tuple[Object, Object]:
        request = self.request(operation, args); outcome = c.execute_read(runtime, request)
        for artifact in c.as_list(outcome["artifacts"]):
            self.store.retain(c.as_object(artifact))
        boundary = outcome["operation_outcome"]
        state = c.as_object(boundary)["value"] if boundary is not None else None
        status = "ok" if state == "returned" else "error" if state in ("held(effect)", "held(observation)") else "refused"
        response = obj({"schema": "a_c.fd-support.response/1", "id": request["id"], "operation": operation, "status": status, "result": outcome["result"], "refusal": outcome["refusal"], "operation_outcome": boundary, "evidence": None})
        operation_payload = obj({"schema": "a_c.fd-support.operation/1", "request": request, "response_without_evidence": copy.deepcopy(response), "artifacts": outcome["artifacts"], "acquisitions": outcome["acquisitions"], "interval": {"clock": "unix_ns", "started_ns": 1, "ended_ns": 2}, "resources": [], "gaps": []})
        ref = self.artifact(runtime, "operation", operation_payload, request); response["evidence"] = ref
        if delivery:
            envelope = c.transport_observation(runtime, request, response, {"clock": "unix_ns", "started_ns": 3, "ended_ns": 4}, hashlib.sha256(c.canonical(response)).hexdigest(), len(c.canonical(response)))
            self.store.retain(envelope)
        return response, outcome

    def packet(self, role: str = "Worker") -> Object:
        actor = role.lower(); refs: list[JSON] = [self.law]
        territory: list[JSON] = [{"root": "workspace", "path": "outputs", "kind": "directory"}] if role == "Worker" else []
        if role == "Worker":
            extra = obj({"worker": {"operation_grant_id": "work", "mutation_subject": self.subject, "territory": territory}})
        elif role == "Reviewer":
            extra = obj({"reviewer": {**{key: self.law for key in ("claim", "composition", "population", "oracle", "ordinary_module_path", "falsification_condition", "independence", "assurance")}, "severity_scale": None}})
        else:
            extra = obj({"executive": {**{key: self.law for key in ("product_role_map", "mandate", "frontier", "result_triage_ledger", "priority_policy")}, "conjunction": None, "disposition_grant": None}})
        return obj({"activation": {"id": "activation", "revision": "1", "configuration": self.law}, "frame": {"id": "frame", "revision": "1", "declaration": self.law, "evaluation": self.law, "result_algebra": self.law}, "subject_basis": {"subject": self.subject, "method_profile": self.basis["method_profile"], "product": obj({"id": "urn:test:product", "definition": self.definition}), "observations": [], "dependencies": refs, "time_basis": "explicit test observation"}, "attention": {"material_relations": refs, "invariants": refs, "semantic_sources": refs, "exclusions": [], "prohibited_assumptions": []}, "actor_authority": {"actor_id": actor, "role": role, "capability": self.law, "semantic": None, "evaluation": self.law, "operation": self.owner if role == "Worker" else None, "decision": None, "acceptance": None, "publication": None, "territory": territory, "tools": ["python"]}, "evidence_relations": {"admissible_evidence": refs, "acquisition": refs, "dependencies": refs, "conjunction": None, "translation": None, "consumer": "executive", "return_contract": self.return_contract}, "stop_change": {key: [] for key in ("invalidators", "stop_conditions", "residuals", "re_entry", "reconfiguration")}, "profile_additions": extra})

    def context(self, runtime: c.Runtime, capacity: int | None = None, host_known: bool = False) -> tuple[Object, Object]:
        args = obj({"packet": self.packet(), "models": [], "sources": [self.law], "late_acquisition": [], "envelope": {"capacity_bytes": capacity, "boundary": "executor-stdin-utf8", "host_context": {"state": "known" if host_known else "unknown", "bytes": 0 if host_known else None, "evidence": self.law if host_known else None}}})
        return self.run(runtime, "context.assemble", args)

    def predicate(self, identity: str, expression: object, subject: Object | None = None, basis: Object | None = None) -> None:
        c.as_object(self.policy["predicates"])[identity] = obj({"id": identity, "source": self.law, "subject": self.subject if subject is None else subject, "basis": self.basis if basis is None else basis, "input_names": ["x", "y", "original", "context", "proof", "history", "totals", "unknowns", "elapsed", "actor_duration"], "expression": expression, "limits": ["supplied finite property only"]})

    def relations(self) -> Object:
        native_basis = c.as_object(self.native.document["basis"]); native_subject = c.as_object(native_basis["subject"])
        a, b, d = ("urn:a-c:toy:object:" + value for value in ("a", "b", "c"))
        return obj({"schema": "a_c.fd-support.relation-declarations/1", "id": "relations", "model": self.model, "model_basis": {"id": native_basis["id"], "sha256": c.digest(native_basis)}, "subject": {"id": native_subject["id"], "sha256": native_subject["sha256"]}, "basis": self.basis, "relations": [{"id": "e1", "source": a, "target": b, "kind": "governs"}, {"id": "e2", "source": b, "target": a, "kind": "governs"}, {"id": "annotation", "source": a, "target": d, "kind": "annotation"}], "governing_kinds": ["governs"], "coverage": {"obligations": [a, b, d], "mapped_support": [{"obligation_id": a, "support_ids": [b]}, {"obligation_id": b, "support_ids": []}], "explicit_unknowns": [{"obligation_id": b, "reason": "source-owned unresolved coverage"}]}, "applicability": [{"target": {"kind": "relation", "id": "e1"}, "condition": None}, {"target": {"kind": "relation", "id": "e2"}, "condition": None}, {"target": {"kind": "relation", "id": "annotation"}, "condition": None}, {"target": {"kind": "obligation", "id": a}, "condition": None}, {"target": {"kind": "obligation", "id": b}, "condition": None}, {"target": {"kind": "obligation", "id": d}, "condition": None}]})


class CoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="ac-support-core-")
        self.addCleanup(self.temp.cleanup)
        self.f = Fixture(Path(self.temp.name))

    def value(self, response: Object) -> Object:
        self.assertEqual(response["status"], "ok", response.get("refusal"))
        return c.as_object(c.as_object(response["result"])["value"])

    def test_reconciliation_selection_is_optional_and_closed(self) -> None:
        admission = c.as_object(c.as_object(c.as_object(self.f.policy["grants"])["work"])["admission"])
        self.f.runtime()  # Existing policy/1 without the new optional field.
        for selected in ([], ["predecessor-settled"]):
            admission["required_reconciliation_predicates"] = c._json(selected)
            self.f.runtime()
        for invalid_selected in (None, "predecessor-settled", [1], [""], [True]):
            with self.subTest(selected=invalid_selected):
                admission["required_reconciliation_predicates"] = c._json(invalid_selected)
                with self.assertRaises(c.SupportError):
                    self.f.runtime()
        admission["required_reconciliation_predicates"] = []
        admission["reconciliation_predicate_ids"] = []
        with self.assertRaises(c.SupportError):
            self.f.runtime()

    def test_preflight_does_not_apply_predecessor_predicate_to_task_subject(self) -> None:
        predecessor = obj({"id": "sha256:" + "b" * 64, "sha256": "b" * 64})
        self.f.predicate("predecessor-settled", {"literal": False}, subject=predecessor)
        admission = c.as_object(c.as_object(c.as_object(self.f.policy["grants"])["work"])["admission"])
        admission["required_reconciliation_predicates"] = ["predecessor-settled"]
        runtime = self.f.runtime()
        response, _ = self.f.context(runtime)
        context = c.as_object(c.as_object(response["result"])["artifact"])
        plan = c.build_preflight(runtime, self.f.request("contract.preflight", {
            "context": context, "grant_id": "work", "executor_id": "registered",
            "result_key": "task-result", "observations": [],
        }))
        self.assertEqual(c.as_object(plan["payload"])["gaps"], [])
        self.assertNotEqual(self.f.subject, predecessor)

    def test_strict_json_lexical_and_duplicate_controls(self) -> None:
        for raw in (b'{"x":1,"x":2}', b'{"x":1.0}', b'{"x":1e0}', b'{"x":NaN}', b'\xff'):
            with self.subTest(raw=raw), self.assertRaises(c.SupportError):
                c.parse_json(raw)
        self.assertEqual(c.parse_json(b'{"x":1,"b":true}'), {"x": 1, "b": True})
        self.assertNotEqual(c.canonical(1), c.canonical(True))

    def test_inventory_has_one_closed_schema_and_33_codes(self) -> None:
        inventory = c.inventory(); self.assertEqual(len(c.CODES), 33)
        self.assertEqual(len(c.as_object(c.CONTENT_SCHEMAS["$defs"])), 58)
        names = [c.as_object(item)["name"] for item in c.as_list(inventory["operations"])]
        self.assertIn("return.capture", names); self.assertIn("work.write", names)
        for operation in names:
            description = c.inventory(c.text(operation))
            output = c.as_object(c.as_list(description["operations"])[0])["output_schema"]
            self.assertEqual(c.as_object(output)["type"], "object")
        with self.assertRaises(c.SupportError):
            c.request_schema("caller.register_authority")

    def test_request_unknown_fields_and_profile_refuse(self) -> None:
        request = self.f.request("source.read", {"source": self.f.law, "encoding": "utf8", "unexpected": True})
        with self.assertRaises(c.SupportError): c.validate_request(request)
        runtime = self.f.runtime()
        response, _ = self.f.run(runtime, "tools.describe", {"method_profile": {"id": "same label", "sha256": c.PROFILE_SHA256}})
        self.assertEqual(response["status"], "refused")
        self.assertEqual(c.as_object(response["operation_outcome"])["value"], "refused(capability)")

    def test_source_raw_slices_pointer_and_missing_are_distinct(self) -> None:
        runtime = self.f.runtime(); source = copy.deepcopy(self.f.law); source["selector"] = {"lines": [2, 3]}
        response, _ = self.f.run(runtime, "source.read", {"source": source, "encoding": "utf8"})
        value = self.value(response); self.assertEqual(value["content"], "two\nthree\n")
        self.assertEqual(value["parent_sha256"], self.f.law["sha256"]); self.assertNotEqual(value["selected_sha256"], value["parent_sha256"])
        source = copy.deepcopy(self.f.data); source["selector"] = {"json_pointer": "/nested/a~1b"}
        value = self.value(self.f.run(runtime, "source.read", {"source": source, "encoding": "utf8"})[0]); self.assertEqual(value["content"], "null")
        source["selector"] = {"json_pointer": "/missing"}
        response, _ = self.f.run(runtime, "source.read", {"source": source, "encoding": "utf8"}); self.assertEqual(c.as_object(response["refusal"])["code"], "basis_missing")

    def test_source_binary_stale_denied_escape_and_symlink(self) -> None:
        binary = self.f.write("inputs/binary.bin", b'\xff\x00'); runtime = self.f.runtime()
        response, _ = self.f.run(runtime, "source.read", {"source": binary, "encoding": "base64"}); self.assertEqual(self.value(response)["content"], "/wA=")
        response, _ = self.f.run(runtime, "source.read", {"source": binary, "encoding": "utf8"}); self.assertEqual(c.as_object(response["refusal"])["code"], "domain_invalid")
        for field, replacement, code in (("sha256", "0" * 64, "digest_mismatch"), ("path", "../policy.json", "path_refused"), ("root", "unregistered", "acquisition_denied")):
            bad = copy.deepcopy(self.f.law); bad[field] = replacement
            response, _ = self.f.run(runtime, "source.read", {"source": bad, "encoding": "utf8"}); self.assertEqual(c.as_object(response["refusal"])["code"], code)
        alias = self.f.workspace / "inputs/alias"; alias.symlink_to(self.f.workspace / "inputs/law.txt")
        bad = copy.deepcopy(self.f.law); bad["path"] = "inputs/alias"
        response, _ = self.f.run(runtime, "source.read", {"source": bad, "encoding": "utf8"}); self.assertEqual(c.as_object(response["refusal"])["code"], "path_refused")

    def test_dirty_and_new_population_recheck_without_head_proxy(self) -> None:
        runtime = self.f.runtime(); response, _ = self.f.run(runtime, "workspace.observe", {"scope": [{"root": "workspace", "path": "inputs", "kind": "directory"}]})
        reference = c.as_object(c.as_object(response["result"])["artifact"])
        (self.f.workspace / "inputs/law.txt").write_text("new dirty bytes")
        self.f.write("inputs/untracked.txt", b'new untracked')
        recheck = c._recheck(runtime, [], [reference]); result = c.check_preconditions(runtime, recheck)
        paths = {c.as_object(change)["path"] for change in c.as_list(result["changes"])}
        self.assertIn("inputs/law.txt", paths); self.assertIn("inputs/untracked.txt", paths)
        self.assertIsNone(self.value(response)["git"])

    def test_observation_caps_never_return_complete_looking_partial(self) -> None:
        c.as_object(self.f.policy["limits"])["max_files"] = 1
        runtime = self.f.runtime(); response, _ = self.f.run(runtime, "workspace.observe", {"scope": [{"root": "workspace", "path": "inputs", "kind": "directory"}]})
        self.assertEqual(c.as_object(response["refusal"])["code"], "budget_exceeded"); self.assertIsNone(response["result"])

    def test_context_null_capacity_has_no_invented_fit(self) -> None:
        runtime = self.f.runtime(); response, _ = self.f.context(runtime)
        value = self.value(response); fit = c.as_object(value["fit"])
        self.assertFalse(fit["selected"]); self.assertIsNone(fit["judgment"])
        self.assertEqual(value["activation_identity"], c.activation_identity(self.f.packet()))
        ref = c.as_object(c.as_object(response["result"])["artifact"])
        body = c.as_object(c.load_artifact(runtime, ref, "context")["payload"])
        rendered = c.text(body["rendered_utf8"])
        self.assertEqual(hashlib.sha256(rendered.encode()).hexdigest(), body["rendered_sha256"])
        self.assertEqual(fit["stdin_bytes"], len(rendered.encode()))
        self.assertNotIn("content_base64", c.canonical(value).decode())
        self.assertIn("activation_identity", c.as_object(body["boundaries"]))

    def test_context_required_fit_known_unknown_exceeded_without_trim(self) -> None:
        runtime = self.f.runtime()
        unknown = self.value(self.f.context(runtime, 1000000)[0]); self.assertEqual(c.as_object(c.as_object(unknown["fit"])["judgment"])["core_value"], "indeterminate")
        known = self.value(self.f.context(runtime, 1000000, True)[0]); self.assertEqual(c.as_object(c.as_object(known["fit"])["judgment"])["core_value"], "satisfied")
        excess_response, _ = self.f.context(runtime, 1, True); excess = self.value(excess_response)
        self.assertEqual(c.as_object(c.as_object(excess["fit"])["judgment"])["core_value"], "falsified")
        self.assertGreater(c.integer(c.as_object(excess["fit"])["stdin_bytes"]), 1)
        self.assertEqual(c.as_object(excess_response["operation_outcome"])["core_value"], "satisfied")

    def test_context_role_packet_unknown_fields_refused(self) -> None:
        runtime = self.f.runtime(); packet = self.f.packet(); c.as_object(packet["actor_authority"])["pretend_owner"] = True
        args = obj({"packet": packet, "models": [], "sources": [], "late_acquisition": [], "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8", "host_context": {"state": "unknown", "bytes": None, "evidence": None}}})
        with self.assertRaises(c.SupportError): c.validate_request(self.f.request("context.assemble", args))

    def test_predicate_true_false_missing_domain_and_typed_equality(self) -> None:
        self.f.predicate("truth", {"op": "equals", "args": [{"input": "x", "pointer": "/x"}, {"literal": True}]})
        self.f.predicate("typed", {"op": "equals", "args": [{"literal": 1}, {"literal": True}]})
        self.f.predicate("domain", {"op": "member", "args": [{"literal": 1}, {"literal": "not array"}]})
        runtime = self.f.runtime()
        for identity, inputs, expected in (("truth", {"x": {"x": True}}, "satisfied"), ("truth", {"x": {"x": False}}, "falsified"), ("truth", {}, "indeterminate"), ("typed", {}, "falsified"), ("domain", {}, "invalid_basis")):
            with self.subTest(identity=identity, expected=expected): self.assertEqual(c.evaluate_predicate(runtime, identity, obj(inputs), self.f.subject, self.f.basis)["core_value"], expected)

    def test_predicate_decisive_branch_retains_gaps_and_unsupported_unperformed(self) -> None:
        self.f.predicate("decisive", {"op": "all", "args": [{"literal": False}, {"input": "x", "pointer": "/absent"}]})
        self.f.predicate("unsupported", {"op": "eval_python", "args": []})
        runtime = self.f.runtime(); result = c.evaluate_predicate(runtime, "decisive", {}, self.f.subject, self.f.basis)
        self.assertEqual(result["core_value"], "falsified"); self.assertTrue(result["gaps"])
        response, _ = self.f.run(runtime, "checks.evaluate", {"predicate_id": "unsupported", "inputs": {}, "subject": self.f.subject, "basis": self.f.basis})
        self.assertEqual(c.as_object(response["refusal"])["code"], "unsupported_check"); self.assertIsNone(response["result"])

    def test_bound_source_predicate_executes_actual_json(self) -> None:
        self.f.predicate("truth", {"op": "equals", "args": [{"input": "x", "pointer": "/x"}, {"literal": True}]})
        runtime = self.f.runtime(); response, _ = self.f.run(runtime, "checks.evaluate", {"predicate_id": "truth", "inputs": {"x": self.f.data}, "subject": self.f.subject, "basis": self.f.basis})
        self.assertEqual(c.as_object(self.value(response)["judgment"])["core_value"], "satisfied")
        ref = c.as_object(response["evidence"]); judgment = c.judgment(runtime, {"record": ref, "pointer": "/payload/response_without_evidence/result/value/judgment"})
        self.assertEqual(judgment["predicate"], self.f.law)
        forged = self.f.artifact(runtime, "raw", {"core_value": "satisfied", "predicate": self.f.law})
        with self.assertRaises(c.SupportError): c.judgment(runtime, {"record": forged, "pointer": "/payload"})

    def test_relations_seed_scoped_support_and_annotation_limits(self) -> None:
        runtime = self.f.runtime(); source = self.f.write("inputs/relations.json", self.f.relations())
        a, b, d = ("urn:a-c:toy:object:" + value for value in ("a", "b", "c"))
        value = c.relation_query(runtime, {"model": self.f.model, "declarations": source, "query": "coverage", "seeds": [a]})
        self.assertEqual(value["records"], [a, b]); coverage = c.as_object(value["coverage"])
        self.assertEqual(coverage["scoped_population"], [a, b]); self.assertEqual(coverage["empty_declared_support"], [b]); self.assertEqual(coverage["required_missing"], [b]); self.assertEqual(c.as_object(value["boundary"])["out_of_scope_obligations"], [d]); self.assertIsNone(value["path"])
        self.assertNotIn("judgment", value)

    def test_relations_missing_mapping_vs_empty_unknown_and_empty_scope(self) -> None:
        runtime = self.f.runtime(); declarations = self.f.relations(); c.as_object(declarations["coverage"])["mapped_support"] = []
        source = self.f.write("inputs/relations.json", declarations); a = "urn:a-c:toy:object:a"
        value = c.relation_query(runtime, {"model": self.f.model, "declarations": source, "query": "coverage", "seeds": [a]})
        coverage = c.as_object(value["coverage"]); self.assertEqual(coverage["mapping_absent"], ["urn:a-c:toy:object:a", "urn:a-c:toy:object:b"]); self.assertEqual(coverage["empty_declared_support"], []); self.assertTrue(coverage["explicit_unknowns"])
        empty = c.relation_query(runtime, {"model": self.f.model, "declarations": source, "query": "coverage", "seeds": []}); self.assertEqual(c.as_object(empty["coverage"])["scoped_population"], [])

    def test_relations_unknown_conditions_conservatively_include_and_nonrecursive_binding(self) -> None:
        declarations = self.f.relations(); declarations["applicability"] = []
        runtime = self.f.runtime(); source = self.f.write("inputs/relations.json", declarations)
        a = "urn:a-c:toy:object:a"
        result = c.relation_query(runtime, {"model": self.f.model, "declarations": source, "query": "dependencies", "seeds": [a]})
        self.assertTrue(c.as_object(result["boundary"])["candidate_closure"])
        facts = [c.as_object(raw) for raw in c.as_list(result["applicability"])]; edge = next(fact for fact in facts if c.as_object(fact["target"])["id"] == "e1")
        expected = c.as_object(edge["expected_subject"])
        self.f.predicate("exclude", {"literal": False}, expected)
        runtime = self.f.runtime(); response, _ = self.f.run(runtime, "checks.evaluate", {"predicate_id": "exclude", "inputs": {}, "subject": expected, "basis": self.f.basis})
        proof = obj({"predicate": self.f.law, "evaluation": {"record": response["evidence"], "pointer": "/payload/response_without_evidence/result/value/judgment"}})
        declarations["applicability"] = [{"target": {"kind": "relation", "id": "e1"}, "condition": proof}]
        source = self.f.write("inputs/relations.json", declarations)
        after = c.relation_query(runtime, {"model": self.f.model, "declarations": source, "query": "dependencies", "seeds": [a]})
        new_edge = next(c.as_object(raw) for raw in c.as_list(after["applicability"]) if c.as_object(c.as_object(raw)["target"])["id"] == "e1")
        self.assertEqual(new_edge["expected_subject"], expected); self.assertTrue(new_edge["excluded"]); self.assertEqual(after["records"], [a])

    def test_relations_wrong_native_basis_dangling_and_duplicate_controls(self) -> None:
        runtime = self.f.runtime()
        for mutation, code in (("basis", "basis_stale"), ("dangling", "domain_invalid"), ("duplicate", "contract_violation")):
            declarations = self.f.relations()
            if mutation == "basis": c.as_object(declarations["model_basis"])["sha256"] = "0" * 64
            elif mutation == "dangling": c.as_object(c.as_list(declarations["relations"])[0])["target"] = "missing"
            else: c.as_list(declarations["relations"]).append(copy.deepcopy(c.as_list(declarations["relations"])[0]))
            source = self.f.write("inputs/relations.json", declarations)
            with self.subTest(mutation=mutation), self.assertRaises(c.SupportError) as caught: c.relation_query(runtime, {"model": self.f.model, "declarations": source, "query": "dependencies", "seeds": []})
            self.assertEqual(caught.exception.code, code)

    def test_relations_shortest_path_parallel_tie_and_equal_endpoint(self) -> None:
        runtime = self.f.runtime(); declarations = self.f.relations(); relations = c.as_list(declarations["relations"])
        parallel = copy.deepcopy(c.as_object(relations[0])); parallel["id"] = "e0"; relations.append(parallel)
        c.as_list(declarations["applicability"]).append({"target": {"kind": "relation", "id": "e0"}, "condition": None})
        source = self.f.write("inputs/relations.json", declarations); a = "urn:a-c:toy:object:a"; b = "urn:a-c:toy:object:b"
        result = c.relation_query(runtime, {"model": self.f.model, "declarations": source, "query": "path", "seeds": [a, b]}); self.assertEqual(c.as_object(result["path"])["relations"], ["e0"])
        result = c.relation_query(runtime, {"model": self.f.model, "declarations": source, "query": "path", "seeds": [a, a]}); self.assertEqual(result["path"], {"records": [a], "relations": []})

    def test_preflight_actual_owner_binding_and_requester_target(self) -> None:
        runtime = self.f.runtime(); response, _ = self.f.context(runtime); context_ref = c.as_object(c.as_object(response["result"])["artifact"])
        plan = c.build_preflight(runtime, self.f.request("contract.preflight", {"context": context_ref, "grant_id": "work", "executor_id": "registered", "result_key": "return", "observations": []}))
        payload = c.as_object(plan["payload"]); self.assertEqual(payload["contract_state"], "drafted"); self.assertIsNone(payload["decision"]); self.assertEqual(payload["requester"], "executive"); self.assertEqual(payload["target"], "worker"); self.assertEqual(payload["gaps"], [])
        self.assertNotEqual(payload["contract_sha256"], context_ref["sha256"])

    def test_preflight_forged_receipt_and_bad_target_sink_refuse(self) -> None:
        runtime = self.f.runtime(); response, _ = self.f.context(runtime); ref = c.as_object(c.as_object(response["result"])["artifact"])
        args = obj({"context": ref, "grant_id": "work", "executor_id": "registered", "result_key": "return", "observations": [], "admission_record": self.f.data})
        with self.assertRaises(c.SupportError) as caught: c.build_preflight(runtime, self.f.request("contract.preflight", args))
        self.assertEqual(caught.exception.code, "authority_missing")
        c.as_object(c.as_object(self.f.policy["event_sinks"])["events"])["consumer"] = "wrong"
        runtime = self.f.runtime(); args.pop("admission_record")
        with self.assertRaises(c.SupportError) as caught: c.build_preflight(runtime, self.f.request("contract.preflight", args))
        self.assertEqual(caught.exception.code, "contract_violation")

    def test_preflight_product_pointer_cannot_be_minted_by_policy(self) -> None:
        c.as_object(c.as_object(self.f.policy["product"])["authority_binding"])["definition_locator"] = "/definition_id"
        runtime = self.f.runtime(); response, _ = self.f.context(runtime); ref = c.as_object(c.as_object(response["result"])["artifact"])
        with self.assertRaises(c.SupportError) as caught: c.build_preflight(runtime, self.f.request("contract.preflight", {"context": ref, "grant_id": "work", "executor_id": "registered", "result_key": "return", "observations": []}))
        self.assertEqual(caught.exception.code, "authority_missing")

    def test_writer_pure_plan_exact_preimage_and_role_membrane(self) -> None:
        target = self.f.write("outputs/work.md", b'original\n'); runtime = self.f.runtime("worker")
        args = obj({"grant_id": "work", "target": target, "mode": "append", "record": obj({"text": "literal", "provenance": self.f.law}), "interpretation": {"text": "separate", "author": self.f.law}, "observations": []})
        plan = c.prepare_write(runtime, self.f.request("work.write", args)); payload = c.as_object(plan["payload"])
        self.assertEqual(base64.b64decode(c.text(payload["intended_base64"])), b'original\nliteral')
        self.assertEqual((self.f.workspace / "outputs/work.md").read_bytes(), b'original\n')
        for role in ("executive", "reviewer"):
            with self.subTest(role=role), self.assertRaises(c.SupportError) as caught: c.prepare_write(self.f.runtime(role), self.f.request("work.write", args))
            self.assertEqual(caught.exception.code, "role_effect_denied")
        (self.f.workspace / "outputs/work.md").write_text("unexpected")
        with self.assertRaises(c.SupportError) as caught: c.prepare_write(self.f.runtime("worker"), self.f.request("work.write", args))
        self.assertEqual(caught.exception.code, "target_conflict")

    def test_writer_authority_is_current_without_obsolete_target_preimage(self) -> None:
        target = self.f.write("outputs/authority-only.md", b"original")
        runtime = self.f.runtime("worker")
        request = self.f.request("work.write", {"grant_id": "work", "target": target, "mode": "append", "record": {"text": "new", "provenance": self.f.law}, "interpretation": None, "observations": []})
        c.check_writer_authority(runtime, request)
        (self.f.workspace / "outputs/authority-only.md").write_bytes(b"already published")
        c.check_writer_authority(runtime, request)
        with self.assertRaises(c.SupportError) as caught:
            c.prepare_write(runtime, request)
        self.assertEqual(caught.exception.code, "target_conflict")
        (self.f.workspace / "inputs/law.txt").write_bytes(b"changed authority")
        with self.assertRaises(c.SupportError) as caught:
            c.check_writer_authority(runtime, request)
        self.assertEqual(caught.exception.code, "digest_mismatch")

    def test_context_typed_recheck_does_not_mine_opaque_source_content(self) -> None:
        quoted = obj({"engine": "workspace-regular-file", "root": "workspace", "path": "inputs/unavailable.txt", "object": None, "sha256": "0" * 64, "selector": None})
        source = self.f.write("inputs/opaque.json", {"supplied_literal": quoted})
        runtime = self.f.runtime()
        response, _ = self.f.run(runtime, "context.assemble", {"packet": self.f.packet(), "models": [], "sources": [source], "late_acquisition": [], "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8", "host_context": {"state": "unknown", "bytes": None, "evidence": None}}})
        context = c.as_object(c.as_object(response["result"])["artifact"])
        plan = c.build_preflight(runtime, self.f.request("contract.preflight", {"context": context, "grant_id": "work", "executor_id": "registered", "result_key": "opaque", "observations": []}))
        sources = c.as_list(c.as_object(plan["recheck"])["sources"])
        self.assertIn(source, sources); self.assertNotIn(quoted, sources)
        self.assertEqual(c.check_preconditions(runtime, c.as_object(plan["recheck"]))["gaps"], [])

    def test_unselected_fit_and_late_source_keep_their_declared_boundary(self) -> None:
        source = self.f.write("inputs/host-only.json", {"bound": 0})
        late = self.f.write("inputs/late.txt", b"late route, not supplied actor bytes")
        runtime = self.f.runtime()
        response, _ = self.f.run(runtime, "context.assemble", {"packet": self.f.packet(), "models": [], "sources": [late], "late_acquisition": [late], "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8", "host_context": {"state": "known", "bytes": 0, "evidence": source}}})
        context = c.as_object(c.as_object(response["result"])["artifact"])
        plan = c.build_preflight(runtime, self.f.request("contract.preflight", {"context": context, "grant_id": "work", "executor_id": "registered", "result_key": "boundaries", "observations": []}))
        sources = c.as_list(c.as_object(plan["recheck"])["sources"])
        self.assertNotIn(source, sources); self.assertNotIn(late, sources)
        payload = c.as_object(c.load_artifact(runtime, context, "context")["payload"])
        self.assertEqual(payload["late_acquisition"], [late])
        self.assertFalse(c.as_object(payload["fit"])["selected"])

    def test_projection_keeps_original_ruling_without_task_state(self) -> None:
        carrier = self.f.write("inputs/work.md", b'# Decision\nOwner said pending.\n## Notes\nReview recommends accept.\n# Other\nNo closure.\n')
        runtime = self.f.runtime(); value = self.value(self.f.run(runtime, "work.project", {"carrier": carrier, "selection": ["Decision"]})[0])
        self.assertIn("Owner said pending.", c.canonical(value).decode()); self.assertNotIn("task_state", value)
        self.assertNotIn("No closure.", c.canonical(value).decode())

    def test_source_first_expectation_requires_real_delivery_and_producer(self) -> None:
        runtime = self.f.runtime("reviewer"); response, outcome = self.f.run(runtime, "source.read", {"source": self.f.law, "encoding": "utf8"}, delivery=True)
        source_inputs = c.as_list(outcome["acquisitions"])
        candidate = self.f.write("inputs/candidate.txt", b'candidate'); claim = self.f.write("inputs/claim.json", {"id": "bounded-exact-source-question", "candidate_sources": [candidate]})
        args = obj({"phase": "expectation", "claim": claim, "sources": [], "candidate": candidate, "proof": [], "comparison": None, "expectations": None, "expectation_body": {"text": "Source requires exact preserved wording.", "source_inputs": source_inputs}})
        result, _ = self.f.run(runtime, "review.prepare", args); value = self.value(result); ref = c.as_object(value["expectations"])
        expectation = c.as_object(c.load_artifact(runtime, ref, "expectation")["payload"])
        self.assertTrue(c.as_object(expectation["exposure_check"])["source_first_observed"])
        self.assertEqual(expectation["external_exposure"], "unknown")
        # Existing prepared source bytes without a transport observation do not
        # establish this additional source delivery.
        _, pending = self.f.run(runtime, "source.read", {"source": self.f.data, "encoding": "utf8"})
        c.as_object(args["expectation_body"])["source_inputs"] = pending["acquisitions"]
        result, _ = self.f.run(runtime, "review.prepare", args); value = self.value(result)
        expectation = c.as_object(c.load_artifact(runtime, c.as_object(value["expectations"]), "expectation")["payload"])
        self.assertFalse(c.as_object(expectation["exposure_check"])["source_first_observed"])

    def test_prior_candidate_exposure_survives_fresh_runtime_and_history_gap(self) -> None:
        candidate = self.f.write("inputs/candidate.txt", b'candidate'); claim = self.f.write("inputs/claim.json", {"claim": "bounded"})
        runtime = self.f.runtime("reviewer"); self.f.run(runtime, "source.read", {"source": candidate, "encoding": "utf8"}, delivery=True)
        fresh = self.f.runtime("reviewer"); self.f.store.complete = False
        result, _ = self.f.run(fresh, "review.prepare", {"phase": "expectation", "claim": claim, "sources": [], "candidate": candidate, "proof": [], "comparison": None, "expectations": None, "expectation_body": {"text": "Expectation after exposure", "source_inputs": []}})
        value = self.value(result); self.assertTrue(value["exposure"]); self.assertTrue(value["gaps"])

    def test_nonreviewer_cannot_impersonate_expectation_producer(self) -> None:
        runtime = self.f.runtime(); claim = self.f.write("inputs/claim.json", {})
        response, _ = self.f.run(runtime, "review.prepare", {"phase": "expectation", "claim": claim, "sources": [], "candidate": None, "proof": [], "comparison": None, "expectations": None, "expectation_body": {"text": "Pretend Reviewer", "source_inputs": []}})
        self.assertEqual(c.as_object(response["refusal"])["code"], "role_effect_denied")

    def test_artifact_identity_covers_producer_and_preserves_raw_import(self) -> None:
        executive = self.f.runtime(); reviewer = self.f.runtime("reviewer")
        request = self.f.request("tools.describe", {})
        first, first_ref = c.make_artifact("raw", {"same": "answer"}, c.provenance(executive, request, 1, 2))
        second, second_ref = c.make_artifact("raw", {"same": "answer"}, c.provenance(reviewer, request, 1, 2))
        self.assertNotEqual(first_ref, second_ref); self.assertEqual(first["payload"], second["payload"])
        self.f.store.retain(first)
        self.assertEqual(c.load_artifact(executive, first_ref)["payload"], {"same": "answer"})

    def test_resource_unknown_and_no_double_counted_cumulative_subset(self) -> None:
        runtime = self.f.runtime(); operation, _ = self.f.run(runtime, "tools.describe", {})
        owner_ref = c.as_object(operation["evidence"]); owner = obj({"kind": "operation", "record": owner_ref})
        samples = [{"owner": owner, "provider": "provider", "counter_id": counter, "unit": "tokens", "scope": "call", "sample_id": identity, "sequence": sequence, "value": value, "raw_source": self.f.data, "interval": None} for counter, identity, sequence, value in (("input", "s1", 1, 10), ("input", "s2", 2, 15), ("cached", "c1", 1, 5), ("unknown", "u1", 1, None))]
        self.f.artifact(runtime, "resource", {"schema": "a_c.fd-support.resource/1", "owner": owner, "samples": samples, "interval": {"clock": "unix_ns", "started_ns": 10, "ended_ns": 30}, "gaps": []})
        accounting = self.f.write("inputs/accounting.json", {"schema": "a_c.fd-support.accounting/1", "id": "accounting", "authority_source": self.f.law, "records": [owner_ref], "counter_rules": [{"provider": "provider", "counter_id": counter, "unit": "tokens", "scope": "call", "source": self.f.law, "mode": "cumulative" if counter == "input" else "delta", "subset_of": "input" if counter == "cached" else None} for counter in ("input", "cached", "unknown")], "elapsed": {"mode": "interval_union", "window": None}, "pricing": None, "limit_predicates": []})
        value = c.aggregate_resources(runtime, {"attempts": [owner_ref, owner_ref], "accounting": accounting})
        totals = {c.as_object(raw)["counter_id"]: c.as_object(raw)["known_subtotal"] for raw in c.as_list(value["totals"])}
        self.assertEqual(totals["input"], 15); self.assertNotIn("cached", totals); self.assertTrue(value["unknowns"])
        self.assertEqual(c.as_object(value["elapsed"])["nanoseconds"], 20); self.assertEqual(c.as_object(value["actor_duration"])["nanoseconds"], 0)

    def test_content_wrong_role_unknown_keys_invalidators_and_zero_rate_refuse(self) -> None:
        contract = c._source_json(self.f.runtime(), self.f.return_contract)
        contract["role"] = "Reviewer"
        with self.assertRaises(c.SupportError): c.validate_content(contract, "ReturnContract")
        with self.assertRaises(c.SupportError): c.validate_content({"kind": "new_lifecycle_invalidator"}, "Invalidator")
        with self.assertRaises(c.SupportError): c.validate_content({"provider": "p", "counter_id": "x", "unit": "u", "scope": "s", "numerator": 1, "denominator": 0}, "Rate")
        bad = copy.deepcopy(self.f.basis); bad["new_private_field"] = True
        with self.assertRaises(c.SupportError): c.validate_content(bad, "Basis")


    def protected_return(self, runtime: c.Runtime, core_value: str, evaluation_id: str = "evaluation", wrong_subject: bool = False, raw_override: bytes | None = None, predicate: Object | None = None) -> tuple[Object, Object, Object]:
        response, _ = self.f.context(runtime); context_ref = c.as_object(c.as_object(response["result"])["artifact"])
        context = c.as_object(c.load_artifact(runtime, context_ref, "context")["payload"]); packet = c.as_object(context["packet"])
        request = self.f.request("dispatch.start", {"preflight": context_ref})
        executor = c.as_object(c.as_object(self.f.policy["executors"])["registered"])
        anchor = obj({"schema": "a_c.fd-support.attempt/1", "preflight": context_ref, "context": context_ref, "request": request, "requester": "executive", "target": "worker", "executor": executor, "invocation": {}, "notification": {"sink_id": "events", "binding": c.as_object(self.f.policy["event_sinks"])["events"]}, "result_key": "return", "retry_of": None, "reconciliation": None})
        attempt_ref = self.f.artifact(runtime, "attempt", anchor, request)
        original = obj({"schema": "a_c.fd-support.closed-return/1", "id": "return", "frame": {"id": "frame", "revision": "1"}, "activation": c.activation_identity(packet), "subject": {"id": "wrong", "sha256": "0" * 64} if wrong_subject else self.f.subject, "basis": self.f.basis, "actor": {"id": "worker", "family": "A", "authorship": "worker"}, "consumer": "executive", "evaluations": [{"id": evaluation_id, "predicate": self.f.law, "domain_outcome": {"retained_original": core_value}, "core_value": core_value, "evidence": [self.f.data], "residuals": [], "invalidators": []}], "not_performed": [], "work_result": None, "residuals": [], "invalidators": []})
        if predicate is not None:
            c.as_object(c.as_list(original["evaluations"])[0])["predicate"] = predicate
        output = obj({"schema": "a_c.fd-support.process-output/1", "attempt": attempt_ref, "stream": "stdout", "slot": "final_stdout_object", "bytes_base64": base64.b64encode(c.canonical(original) if raw_override is None else raw_override).decode(), "complete": True, "decoder": executor["stdout_decoder"], "producer": {"principal_id": "worker", "actor": c.as_object(self.f.policy["principals"])["worker"], "executor_id": "registered", "executable": executor["executable"]}, "interval": {"clock": "unix_ns", "started_ns": 10, "ended_ns": 20}})
        output_ref = self.f.artifact(runtime, "raw", output)
        event = {"schema": "a_c.fd-support.attempt-event/1", "attempt": attempt_ref, "cursor": 1, "kind": "output_finalized", "data": {"stdout": output_ref, "stderr": None, "process_end": {"observed": True, "returncode": 0}}, "previous": None, "observed_at_ns": 20}
        self.f.artifact(runtime, "raw", event)
        captured, _ = self.f.run(runtime, "return.capture", {"attempt": attempt_ref, "payload": output_ref, "return_contract": self.f.return_contract})
        returned = c.as_object(c.as_object(captured["result"])["artifact"])
        self.assertTrue(c.as_object(c.as_object(self.value(captured)["producer"]))["authenticated"])
        return returned, original, context_ref

    def required_counterexample(self, variant: str) -> Object:
        """Isolated fold; controlled protected producer, no operator qualification."""
        runtime = self.f.runtime()
        mandatory_value = "indeterminate" if variant == "mandatory-precedence" else "satisfied"
        passed, first, _ = self.protected_return(runtime, mandatory_value, "mandatory")
        predicate = self.f.data if variant == "unrelated" else self.f.law
        failed, second, _ = self.protected_return(runtime, "falsified", "counterexample", variant == "stale", predicate=predicate)
        assessments: list[JSON] = []
        for index, (reference, original) in enumerate(((passed, first), (failed, second))):
            payload = c.as_object(c.load_artifact(runtime, reference, "return")["payload"])
            evaluation = c.as_object(c.as_list(original["evaluations"])[0])
            assessments.append(obj({"id": "assessment-" + str(index), "key": {"producer": "worker", "activation": original["activation"], "attempt": payload["attempt"], "evaluation_id": evaluation["id"]}, "predicate": self.f.data if variant == "wrong-predicate" and index else evaluation["predicate"], "subject": self.f.subject, "basis": self.f.basis, "mandatory": index == 0, "coverage": ["R"] if index == 0 or variant == "covered" else [], "applicability": None}))
        plan = obj({"schema": "a_c.fd-support.conjunction-plan/1", "id": "counterexample-" + variant, "authority_source": self.f.owner, "operator_id": "claude-rc9.conjunction/1", "composite": {"predicate": self.f.law, "subject": self.f.subject, "basis": self.f.basis}, "decision_authority": self.f.owner, "rule": "first_non_satisfied_in_plan_order", "basis_relation": "exact_equal_to_composite", "required_obligations": [{"id": "R", "source": self.f.law, "applicability": None}], "required_constraints": [{"obligation_id": "R", "predicate": self.f.law}], "assessments": assessments, "inherited": []})
        source = self.f.write("inputs/counterexample-" + variant + ".json", plan)
        operator = obj({"id": "claude-rc9.conjunction/1", "source": self.f.law, "decision_authority": self.f.owner, "rule": "first_non_satisfied_in_plan_order", "plan_source": source})
        returns: list[JSON] = [passed, failed]
        if variant in ("wrong-basis", "cardinality"):
            payload = copy.deepcopy(c.as_object(c.load_artifact(runtime, failed, "return")["payload"]))
            original = c.as_object(payload["original"])
            if variant == "wrong-basis":
                c.as_object(original["basis"])["observations"] = [{"id": "sha256:" + "0" * 64, "sha256": "0" * 64}]
                returns = [passed]
            else:
                c.as_object(c.as_list(original["evaluations"])[0])["core_value"] = "satisfied"
            returns.append(self.f.artifact(runtime, "return", payload))
        with patch.object(c, "_qualified_operator", return_value=operator):
            return c.conjoin(runtime, {"operator_id": "claude-rc9.conjunction/1", "plan": source, "returns": returns, "current_observations": []})

    def test_required_counterexample_does_not_require_contributor_coverage(self) -> None:
        for variant in ("empty", "covered"):
            with self.subTest(variant=variant):
                value = self.required_counterexample(variant)
                self.assertEqual(c.as_object(value["judgment"])["core_value"], "falsified")
                self.assertEqual(len(c.as_list(value["constraint_failures"])), 1)
                self.assertEqual(value["uncovered"], [])

    def test_required_counterexample_exclusions_and_mandatory_precedence(self) -> None:
        for variant, expected in (("unrelated", "satisfied"), ("stale", "indeterminate"), ("wrong-basis", "indeterminate"), ("wrong-predicate", "indeterminate"), ("cardinality", "indeterminate"), ("mandatory-precedence", "indeterminate")):
            with self.subTest(variant=variant):
                value = self.required_counterexample(variant)
                self.assertEqual(c.as_object(value["judgment"])["core_value"], expected)
                if variant != "mandatory-precedence":
                    self.assertEqual(value["constraint_failures"], [])

    def nested_counterexample(self, variant: str, depth: int = 1) -> Object:
        """Controlled protected producer and isolated operator gate, not qualification."""
        runtime = self.f.runtime()
        passed, first, _ = self.protected_return(runtime, "satisfied", "nested-S")
        predicate = self.f.data if variant == "unrelated" else self.f.law
        failed, second, _ = self.protected_return(runtime, "falsified", "nested-F", variant == "wrong-subject", predicate=predicate)
        rows = [(passed, first), (failed, second)]
        extra_returns: list[JSON] = []
        if variant in ("wrong-basis", "cardinality"):
            payload = copy.deepcopy(c.as_object(c.load_artifact(runtime, failed, "return")["payload"]))
            original = c.as_object(payload["original"])
            if variant == "wrong-basis":
                c.as_object(original["basis"])["observations"] = [{"id": "sha256:" + "0" * 64, "sha256": "0" * 64}]
                changed = self.f.artifact(runtime, "return", payload)
                rows[1] = (changed, original)
            else:
                c.as_object(c.as_list(original["evaluations"])[0])["core_value"] = "satisfied"
                extra_returns.append(self.f.artifact(runtime, "return", payload))
        condition: JSON = None
        if variant == "excluded":
            self.f.predicate("exclude-nested", {"literal": False})
            runtime = self.f.runtime()
            response, _ = self.f.run(runtime, "checks.evaluate", {"predicate_id": "exclude-nested", "inputs": {}, "subject": self.f.subject, "basis": self.f.basis})
            condition = obj({"predicate": self.f.law, "evaluation": {"record": response["evidence"], "pointer": "/payload/response_without_evidence/result/value/judgment"}})

        def join(identity: str, entries: list[tuple[Object, Object]], inherited: list[JSON], required: bool, inner: bool = False) -> tuple[Object, Object]:
            assessments: list[JSON] = []
            for index, (reference, original) in enumerate(entries):
                payload = c.as_object(c.load_artifact(runtime, reference, "return")["payload"])
                evaluation = c.as_object(c.as_list(original["evaluations"])[0])
                assessments.append(obj({"id": "assessment-" + str(index), "key": {"producer": "worker", "activation": original["activation"], "attempt": payload["attempt"], "evaluation_id": evaluation["id"]}, "predicate": self.f.data if inner and index and variant == "wrong-predicate" else evaluation["predicate"], "subject": self.f.subject, "basis": self.f.basis, "mandatory": index == 0, "coverage": [identity] if index == 0 else [], "applicability": condition if inner and index else None}))
            if not inner and required and variant == "gap":
                missing = copy.deepcopy(c.as_object(assessments[0])); missing["id"] = "not-performed"
                c.as_object(missing["key"])["evaluation_id"] = "not-performed"
                assessments.append(missing)
            plan = obj({"schema": "a_c.fd-support.conjunction-plan/1", "id": identity, "authority_source": self.f.owner, "operator_id": "claude-rc9.conjunction/1", "composite": {"predicate": self.f.law, "subject": self.f.subject, "basis": self.f.basis}, "decision_authority": self.f.owner, "rule": "first_non_satisfied_in_plan_order", "basis_relation": "exact_equal_to_composite", "required_obligations": [{"id": identity, "source": self.f.law, "applicability": None}], "required_constraints": [{"obligation_id": identity, "predicate": self.f.law}] if required else [], "assessments": assessments, "inherited": inherited})
            self.f.counter += 1
            source = self.f.write("inputs/nested-plan-" + str(self.f.counter) + ".json", plan)
            operator = obj({"id": "claude-rc9.conjunction/1", "source": self.f.law, "decision_authority": self.f.owner, "rule": "first_non_satisfied_in_plan_order", "plan_source": source})
            returns: list[JSON] = [reference for reference, _ in entries]
            if inner:
                returns.extend(extra_returns)
            with patch.object(c, "_qualified_operator", return_value=operator):
                response, _ = self.f.run(runtime, "results.conjoin", {"operator_id": "claude-rc9.conjunction/1", "plan": source, "returns": returns, "current_observations": []})
            return self.value(response), c.as_object(response["evidence"])

        inner_value, inherited = join("r2", rows, [], variant == "already-required", True)
        if variant in ("new-P", "excluded", "unrelated"):
            self.assertEqual(c.as_object(inner_value["judgment"])["core_value"], "satisfied")
        for level in range(depth - 1):
            _, inherited = join("middle-" + str(level), [(passed, first)], [inherited], False)
        outer = [(passed, first)]
        if variant == "mandatory-precedence":
            held, held_original, _ = self.protected_return(runtime, "indeterminate", "outer-held")
            outer = [(held, held_original)]
        value, _ = join("r", outer, [inherited], True)
        self.assertEqual(len(c.as_list(value["applicable"])), 1)
        if variant == "wrong-subject":
            # Binding rejects this carrier for the current subject. Its raw
            # original survives; it is not an authenticated applicable F.
            retained = c.as_object(c.load_artifact(runtime, failed, "return")["payload"])
            self.assertEqual(retained["original"], second)
        else:
            self.assertTrue(value["failures"])
        return value

    def test_new_outer_required_constraint_revalidates_nested_counterexample(self) -> None:
        for depth in (1, 2):
            with self.subTest(depth=depth):
                value = self.nested_counterexample("new-P", depth)
                self.assertEqual(c.as_object(value["judgment"])["core_value"], "falsified")
                self.assertTrue(value["constraint_failures"])
                self.assertEqual(value["planned_gaps"], []); self.assertEqual(value["uncovered"], [])

    def test_inherited_counterexample_cannot_grant_excluded_or_invalid_results(self) -> None:
        for variant, expected in (("unrelated", "satisfied"), ("excluded", "satisfied"), ("wrong-subject", "indeterminate"), ("wrong-basis", "indeterminate"), ("wrong-predicate", "indeterminate"), ("cardinality", "indeterminate")):
            with self.subTest(variant=variant):
                value = self.nested_counterexample(variant, 2)
                self.assertEqual(c.as_object(value["judgment"])["core_value"], expected)
                self.assertEqual(value["constraint_failures"], [])

    def test_inherited_counterexample_preserves_gaps_and_current_mandatory_order(self) -> None:
        for variant, expected in (("gap", "indeterminate"), ("mandatory-precedence", "indeterminate"), ("already-required", "falsified")):
            with self.subTest(variant=variant):
                value = self.nested_counterexample(variant, 2)
                self.assertEqual(c.as_object(value["judgment"])["core_value"], expected)
                self.assertTrue(value["constraint_failures"])

    def qualified_plan(self, runtime: c.Runtime, returned: list[tuple[Object, Object]], missing: bool = False) -> tuple[Object, c.Runtime]:
        assessments = []
        for index, (ref, original) in enumerate(returned):
            payload = c.as_object(c.load_artifact(runtime, ref, "return")["payload"])
            assessment = {"id": "assessment-" + str(index), "key": {"producer": "worker", "activation": original["activation"], "attempt": payload["attempt"], "evaluation_id": c.as_object(c.as_list(original["evaluations"])[0])["id"]}, "predicate": self.f.law, "subject": self.f.subject, "basis": self.f.basis, "mandatory": True, "coverage": ["obligation"], "applicability": None}
            assessments.append(assessment)
        if missing:
            fake = {"id": "sha256:" + "0" * 64, "sha256": "0" * 64}
            assessments.append({"id": "unperformed", "key": {"producer": "worker", "activation": {"id": "unperformed", "sha256": "0" * 64}, "attempt": fake, "evaluation_id": "not-run"}, "predicate": self.f.law, "subject": self.f.subject, "basis": self.f.basis, "mandatory": True, "coverage": ["obligation"], "applicability": None})
        plan = obj({"schema": "a_c.fd-support.conjunction-plan/1", "id": "plan", "authority_source": self.f.owner, "operator_id": "claude-rc9.conjunction/1", "composite": {"predicate": self.f.law, "subject": self.f.subject, "basis": self.f.basis}, "decision_authority": self.f.owner, "rule": "first_non_satisfied_in_plan_order", "basis_relation": "exact_equal_to_composite", "required_obligations": [{"id": "obligation", "source": self.f.law, "applicability": None}], "required_constraints": [{"obligation_id": "obligation", "predicate": self.f.law}], "assessments": assessments, "inherited": []})
        return self.register_plan(plan)

    def register_plan(self, plan: Object) -> tuple[Object, c.Runtime]:
        self.f.counter += 1
        source = self.f.write("inputs/plan-" + str(self.f.counter) + ".json", plan)
        operator = obj({"id": "claude-rc9.conjunction/1", "source": self.f.law, "decision_authority": self.f.owner, "rule": "first_non_satisfied_in_plan_order", "plan_source": source})
        qualification = self.f.write("inputs/qualification-" + str(self.f.counter) + ".json", {"schema": "a_c.fd-support.operator-qualification/1", "operator_id": "claude-rc9.conjunction/1", "definition_sha256": c.digest(operator), "rule": "first_non_satisfied_in_plan_order", "method_profile": self.f.basis["method_profile"], "implementation_sha256": hashlib.sha256((CODE / "ac_support_core.py").read_bytes()).hexdigest(), "dependencies": [], "fragment": ["controlled exact source-selected module cases"], "proof_sources": [self.f.data]})
        operator["qualification"] = qualification; c.as_object(self.f.policy["operators"])["claude-rc9.conjunction/1"] = operator
        return source, self.f.runtime()

    def test_authentic_final_return_retained_and_historical_subject_not_rewritten(self) -> None:
        runtime = self.f.runtime(); returned, original, context = self.protected_return(runtime, "satisfied", wrong_subject=True)
        response, _ = self.f.run(runtime, "return.check", {"return": returned, "context": context, "consumer": "executive", "observations": [], "predicates": []})
        value = self.value(response); self.assertFalse(value["consumable"])
        historical = c.as_object(value["original"]); self.assertEqual(c.as_object(c.as_list(historical["evaluations"])[0])["core_value"], "satisfied")
        self.assertEqual(historical["subject"], original["subject"])
        self.assertTrue(value["gaps"])

    def test_original_judgment_rejects_material_capture_binding_gaps(self) -> None:
        runtime = self.f.runtime()
        _, original, _ = self.protected_return(runtime, "falsified")
        wrong_coordinates = obj({
            "frame": {"id": "other-frame", "revision": "1"},
            "activation": {"id": "other-activation", "sha256": "0" * 64},
            "subject": {"id": "other-subject", "sha256": "0" * 64},
            "basis": {"method_profile": self.f.basis["method_profile"],
                      "observations": [{"id": "sha256:" + "0" * 64, "sha256": "0" * 64}]},
            "actor": {"id": "other-worker", "family": "A", "authorship": "other-worker"},
            "consumer": "other-consumer",
        })
        for coordinate, replacement in wrong_coordinates.items():
            with self.subTest(coordinate=coordinate):
                historical = copy.deepcopy(original); historical[coordinate] = replacement
                returned, _, _ = self.protected_return(runtime, "falsified", raw_override=c.canonical(historical))
                payload = c.as_object(c.load_artifact(runtime, returned, "return")["payload"])
                binding_gaps = c.as_list(c.as_object(payload["binding_checks"])["gaps"])
                self.assertTrue(any(isinstance(gap, dict) and gap.get("binding") == coordinate for gap in binding_gaps))
                reference = obj({"record": returned, "pointer": "/payload/original/evaluations/0"})
                with self.assertRaises(c.SupportError) as caught:
                    c.judgment(runtime, reference)
                self.assertEqual(caught.exception.code, "basis_missing")
                self.assertEqual(caught.exception.gaps, binding_gaps)
                value, gaps = c._condition(runtime, {"predicate": self.f.law, "evaluation": reference}, self.f.subject, self.f.basis)
                self.assertIsNone(value); self.assertTrue(gaps)
                candidates, originals, failures = c._conjunction_returns(runtime, [returned])
                self.assertEqual(candidates, {}); self.assertEqual(failures, [])
                self.assertEqual(c.as_object(originals[0])["original"], historical)
                self.assertEqual(payload["original"], historical)

    def test_original_judgment_requires_exact_performed_evaluation_membership(self) -> None:
        runtime = self.f.runtime()
        _, original, _ = self.protected_return(runtime, "satisfied", "actual-satisfied")
        first = c.as_object(c.as_list(original["evaluations"])[0])
        nested = copy.deepcopy(first)
        nested.update({"id": "nested-not-performed", "domain_outcome": False, "core_value": "falsified"})
        domain = obj({"nested": nested, "arbitrary": [None, True, 4, {"a/b~": "unchanged"}]})
        first["domain_outcome"] = domain
        second = copy.deepcopy(first)
        second.update({"id": "actual-falsified", "domain_outcome": [False, {"original": "domain value"}], "core_value": "falsified"})
        c.as_list(original["evaluations"]).append(second)
        original["not_performed"] = ["nested-not-performed"]
        returned, _, _ = self.protected_return(runtime, "satisfied", raw_override=c.canonical(original))
        for index, expected in enumerate((first, second)):
            reference = obj({"record": returned, "pointer": "/payload/original/evaluations/" + str(index)})
            actual = c.judgment(runtime, reference)
            self.assertEqual(actual["core_value"], expected["core_value"])
            self.assertEqual(actual["domain_outcome"], expected["domain_outcome"])
        for suffix in ("0/domain_outcome/nested", "0/domain_outcome", "00", "-1", "2", "0/"):
            with self.subTest(suffix=suffix):
                reference = obj({"record": returned, "pointer": "/payload/original/evaluations/" + suffix})
                with self.assertRaises(c.SupportError) as caught:
                    c.judgment(runtime, reference)
                self.assertEqual(caught.exception.code, "basis_missing")
                value, gaps = c._condition(runtime, {"predicate": self.f.law, "evaluation": reference}, self.f.subject, self.f.basis)
                self.assertIsNone(value); self.assertTrue(gaps)
        retained = c.as_object(c.load_artifact(runtime, returned, "return")["payload"])
        self.assertEqual(retained["original"], original)

    def test_original_judgment_retains_known_provenance_with_unrelated_history_gap(self) -> None:
        runtime = self.f.runtime(); self.f.store.complete = False
        returned, original, _ = self.protected_return(runtime, "falsified")
        payload = c.as_object(c.load_artifact(runtime, returned, "return")["payload"])
        self.assertTrue(c.as_list(c.as_object(payload["binding_checks"])["gaps"]))
        reference = obj({"record": returned, "pointer": "/payload/original/evaluations/0"})
        actual = c.judgment(runtime, reference)
        self.assertEqual(actual["core_value"], "falsified")
        self.assertEqual(actual["domain_outcome"], c.as_object(c.as_list(original["evaluations"])[0])["domain_outcome"])
        value, gaps = c._condition(runtime, {"predicate": self.f.law, "evaluation": reference}, self.f.subject, self.f.basis)
        self.assertEqual(value, "falsified"); self.assertEqual(gaps, [])
        candidates, _, failures = c._conjunction_returns(runtime, [returned])
        self.assertEqual(len(candidates), 1); self.assertEqual(len(failures), 1)
        missing, missing_gaps = c._condition(runtime, {"predicate": self.f.law, "evaluation": None}, self.f.subject, self.f.basis)
        self.assertIsNone(missing); self.assertEqual(missing_gaps, ["Missing actual condition judgment"])

    def test_pasted_raw_payload_cannot_borrow_attempt_authentication(self) -> None:
        runtime = self.f.runtime(); returned, original, _ = self.protected_return(runtime, "satisfied")
        attempt = c.as_object(c.as_object(c.load_artifact(runtime, returned, "return")["payload"])["attempt"])
        pasted = self.f.artifact(runtime, "raw", original)
        response, _ = self.f.run(runtime, "return.capture", {"attempt": attempt, "payload": pasted, "return_contract": self.f.return_contract})
        value = self.value(response); self.assertFalse(c.as_object(value["producer"])["authenticated"])
        self.assertEqual(c.as_object(value["original"])["evaluations"], original["evaluations"])

    def test_conjunction_declared_two_orders_preserve_failures_and_rf_output(self) -> None:
        runtime = self.f.runtime(); invalid, i, _ = self.protected_return(runtime, "invalid_basis", "first")
        failed, f, _ = self.protected_return(runtime, "falsified", "second")
        passed, p, _ = self.protected_return(runtime, "satisfied", "third")
        source, runtime = self.qualified_plan(runtime, [(invalid, i), (failed, f), (passed, p)])
        args = obj({"operator_id": "claude-rc9.conjunction/1", "plan": source, "returns": [passed, failed, invalid], "current_observations": []})
        value = c.conjoin(runtime, args); self.assertEqual(c.as_object(value["judgment"])["core_value"], "invalid_basis"); self.assertEqual(c.as_object(value["judgment"])["domain_outcome"], "invalid_basis"); self.assertTrue(value["failures"])
        plan = c._source_json(runtime, source, "ConjunctionPlan"); c.as_list(plan["assessments"]).reverse(); source, runtime = self.register_plan(plan); args["plan"] = source
        value = c.conjoin(runtime, args); self.assertEqual(c.as_object(value["judgment"])["core_value"], "falsified"); self.assertEqual(c.as_object(value["judgment"])["domain_outcome"], "conflict"); self.assertTrue(value["failures"])

    def test_conjunction_stale_is_planned_gap_and_uncovered_is_separate(self) -> None:
        runtime = self.f.runtime(); stale, original, _ = self.protected_return(runtime, "satisfied", wrong_subject=True)
        source, runtime = self.qualified_plan(runtime, [(stale, original)], missing=True)
        plan = c._source_json(runtime, source, "ConjunctionPlan"); c.as_list(plan["required_obligations"]).append({"id": "uncovered", "source": self.f.data, "applicability": None}); source, runtime = self.register_plan(plan)
        value = c.conjoin(runtime, {"operator_id": "claude-rc9.conjunction/1", "plan": source, "returns": [stale], "current_observations": []})
        self.assertEqual(c.as_object(value["judgment"])["core_value"], "indeterminate"); self.assertEqual(value["uncovered"], ["uncovered"])
        self.assertEqual(len(c.as_list(value["planned_gaps"])), 2)
        historical = c.as_object(c.as_list(value["originals"])[0]); self.assertEqual(c.as_object(c.as_list(c.as_object(historical["original"])["evaluations"])[0])["core_value"], "satisfied")

    def test_conjunction_unqualified_operator_refuses_actual_join(self) -> None:
        runtime = self.f.runtime(); returned, original, _ = self.protected_return(runtime, "satisfied")
        source, runtime = self.qualified_plan(runtime, [(returned, original)])
        operator = c.as_object(c.as_object(self.f.policy["operators"])["claude-rc9.conjunction/1"]); operator["qualification"] = self.f.data
        runtime = self.f.runtime()
        with self.assertRaises(c.SupportError) as caught: c.conjoin(runtime, {"operator_id": "claude-rc9.conjunction/1", "plan": source, "returns": [returned], "current_observations": []})
        self.assertEqual(caught.exception.code, "unqualified_operator")

    def test_conjunction_cardinality_conflict_is_gap_not_input_order_winner(self) -> None:
        runtime = self.f.runtime(); returned, original, _ = self.protected_return(runtime, "satisfied")
        payload = copy.deepcopy(c.as_object(c.load_artifact(runtime, returned, "return")["payload"]))
        c.as_object(c.as_list(c.as_object(payload["original"])["evaluations"])[0])["core_value"] = "falsified"
        conflicting = self.f.artifact(runtime, "return", payload)
        source, runtime = self.qualified_plan(runtime, [(returned, original)])
        value = c.conjoin(runtime, {"operator_id": "claude-rc9.conjunction/1", "plan": source, "returns": [conflicting, returned, returned], "current_observations": []})
        self.assertEqual(c.as_object(value["judgment"])["core_value"], "indeterminate"); self.assertTrue(value["conflicts"]); self.assertTrue(value["planned_gaps"])

    def test_refresh_conservative_unknown_and_original_handoff(self) -> None:
        runtime = self.f.runtime(); before, _ = self.f.run(runtime, "workspace.observe", {"scope": [{"root": "workspace", "path": "outputs", "kind": "directory"}]}); before_ref = c.as_object(c.as_object(before["result"])["artifact"])
        self.f.write("outputs/new.txt", b'changed')
        after, _ = self.f.run(runtime, "workspace.observe", {"scope": [{"root": "workspace", "path": "outputs", "kind": "directory"}]}); after_ref = c.as_object(c.as_object(after["result"])["artifact"])
        old_basis = obj({"method_profile": self.f.basis["method_profile"], "observations": [before_ref]}); new_basis = obj({"method_profile": self.f.basis["method_profile"], "observations": [after_ref]})
        declarations = obj({"schema": "a_c.fd-support.refresh-declarations/1", "id": "refresh", "authority_source": self.f.owner, "old_subject": self.f.subject, "new_subject": self.f.subject, "old_basis": old_basis, "new_basis": new_basis, "nodes": [{"id": "check", "source": self.f.law}, {"id": "dependency", "source": self.f.data}], "dependencies": [{"dependent": "check", "dependency": "dependency", "source": self.f.law}], "checks": [{"id": "existing-check", "node": "check", "result": None, "obligations": []}], "coverage": {"population_source": self.f.law, "dependency_complete": None, "impact_complete": None}, "impact_cover": ["dependency"], "new_obligations": [{"id": "new", "source": self.f.law, "applicability": None}], "mandatory_gates": ["existing-check", "new"], "retention": []})
        source = self.f.write("inputs/refresh.json", declarations); invalidators = self.f.write("inputs/invalidators.json", {"schema": "a_c.fd-support.invalidators/1", "id": "invalidators", "declarations_sha256": source["sha256"], "events": []})
        value = c.refresh(runtime, {"previous": before_ref, "current": after_ref, "declarations": source, "invalidators": invalidators, "results": []})
        self.assertTrue(value["differences"]); self.assertEqual(len(c.as_list(value["affected_candidates"])), 1); self.assertEqual(value["unchanged_candidates"], []); self.assertTrue(value["gaps"]); self.assertEqual(value["mandatory_gates"], ["existing-check", "new"]); self.assertEqual(c.as_object(value["handoff"])["previous"], before_ref)

    def preservation_case(self, claim_scope_preserved: bool = True) -> tuple[c.Runtime, Object, Object]:
        """Supply a finite preservation contract; execute every condition as a real check.

        The source-owned universe is exactly one check and its one data dependency.
        These controls do not infer semantic completeness for any larger population.
        """
        dependency = self.f.write("outputs/stable.json", {"measured_value": 4})
        old_body = obj({"id": "urn:test:preservation:old", "revision": "1", "claim_scope": ["stable-value"], "assertion_basis": {"expected_value": 5}, "dependencies": [dependency], "measured_value": 4})
        new_body = copy.deepcopy(old_body); new_body["id"] = "urn:test:preservation:new"; new_body["revision"] = "2"
        if not claim_scope_preserved:
            new_body["claim_scope"] = ["different-selected-claim"]
        old_source = self.f.write("inputs/preservation-old.json", old_body)
        new_source = self.f.write("inputs/preservation-new.json", new_body)
        old_subject = obj({"id": old_body["id"], "sha256": c.digest(old_body)})
        new_subject = obj({"id": new_body["id"], "sha256": c.digest(new_body)})
        scope = [{"root": "workspace", "path": "outputs", "kind": "directory"}]
        runtime = self.f.runtime()
        previous, _ = self.f.run(runtime, "workspace.observe", {"scope": scope})
        current, _ = self.f.run(runtime, "workspace.observe", {"scope": scope})
        self.value(previous); self.value(current)
        previous_ref = c.as_object(c.as_object(previous["result"])["artifact"])
        current_ref = c.as_object(c.as_object(current["result"])["artifact"])
        old_basis = obj({"method_profile": self.f.basis["method_profile"], "observations": [previous_ref]})
        new_basis = obj({"method_profile": self.f.basis["method_profile"], "observations": [current_ref]})
        population_body = obj({"id": "finite-preservation-universe", "nodes": ["check", "dependency"], "dependencies": [{"dependent": "check", "dependency": "dependency"}], "material_sources": [dependency], "impact_cover": []})
        population = self.f.write("inputs/preservation-universe.json", population_body)
        frontier = self.f.write("inputs/preservation-frontier.json", {"nodes": ["check", "dependency"], "dependencies": [{"dependent": "check", "dependency": "dependency"}], "material_sources": [dependency], "impact_cover": []})

        def equal(left: str, left_pointer: str, right: str, right_pointer: str) -> Object:
            return obj({"op": "equals", "args": [{"input": left, "pointer": left_pointer}, {"input": right, "pointer": right_pointer}]})

        def register(identity: str, meaning: str, expression: Object, subject: Object, basis: Object, names: list[str]) -> Object:
            source = self.f.write("inputs/preservation-predicate-" + identity + ".json", {"id": identity, "meaning": meaning, "expression": expression, "subject": subject, "basis": basis, "scope": "only the explicitly declared finite preservation universe"})
            c.as_object(self.f.policy["predicates"])[identity] = obj({"id": identity, "source": source, "subject": subject, "basis": basis, "input_names": names, "expression": expression, "limits": ["supplied finite structural preservation property only"]})
            return source

        original_source = register("original-five", "The old measured value equals five; four is an actual counterexample.", obj({"op": "equals", "args": [{"input": "old", "pointer": "/measured_value"}, {"literal": 5}]}), old_subject, old_basis, ["old"])
        expressions = {
            "claim_scope": equal("old", "/claim_scope", "new", "/claim_scope"),
            "assertion_basis": equal("old", "/assertion_basis", "new", "/assertion_basis"),
            "observation_basis": equal("previous", "/payload/entries", "current", "/payload/entries"),
            "dependencies": equal("old", "/dependencies", "new", "/dependencies"),
            "dependency_complete": obj({"op": "all", "args": [equal("population", "/nodes", "frontier", "/nodes"), equal("population", "/dependencies", "frontier", "/dependencies"), equal("population", "/material_sources", "frontier", "/material_sources")]}),
            "impact_complete": obj({"op": "all", "args": [equal("previous", "/payload/entries", "current", "/payload/entries"), equal("population", "/impact_cover", "frontier", "/impact_cover"), {"op": "equals", "args": [{"input": "frontier", "pointer": "/impact_cover"}, {"literal": []}]}]}),
        }
        meanings = {
            "claim_scope": "Old and current supplied claim scopes are equal.",
            "assertion_basis": "Old and current supplied deciding assertions are equal.",
            "observation_basis": "The actual old and current scoped observed entry populations are equal.",
            "dependencies": "Old and current declared exact material dependency SourceRefs are equal.",
            "dependency_complete": "The selected declaration exactly covers the source-owned finite node, edge and material-source population.",
            "impact_complete": "Actual observed entry populations are equal and the selected finite impact cover is empty.",
        }
        condition_sources = {name: register(name, meanings[name], expression, new_subject, new_basis, ["old", "new", "previous", "current", "population", "frontier"]) for name, expression in expressions.items()}
        runtime = self.f.runtime()
        original_response, _ = self.f.run(runtime, "checks.evaluate", {"predicate_id": "original-five", "inputs": {"old": old_source}, "subject": old_subject, "basis": old_basis})
        self.assertEqual(c.as_object(self.value(original_response)["judgment"])["core_value"], "falsified")
        original_record = c.as_object(original_response["evidence"])
        original = obj({"record": original_record, "pointer": "/payload/response_without_evidence/result/value/judgment"})
        conditions: Object = {}
        condition_records: list[JSON] = []
        for name, source in condition_sources.items():
            response, _ = self.f.run(runtime, "checks.evaluate", {"predicate_id": name, "inputs": {"old": old_source, "new": new_source, "previous": previous_ref, "current": current_ref, "population": population, "frontier": frontier}, "subject": new_subject, "basis": new_basis})
            expected = "falsified" if name == "claim_scope" and not claim_scope_preserved else "satisfied"
            self.assertEqual(c.as_object(self.value(response)["judgment"])["core_value"], expected, name)
            record = c.as_object(response["evidence"]); condition_records.append(record)
            conditions[name] = obj({"predicate": source, "evaluation": {"record": record, "pointer": "/payload/response_without_evidence/result/value/judgment"}})
        edge_source = self.f.write("inputs/preservation-edge.json", {"dependent": "check", "dependency": "dependency", "meaning": "The finite original measured-value check depends on stable.json."})
        declarations = obj({"schema": "a_c.fd-support.refresh-declarations/1", "id": "preservation-refresh", "authority_source": self.f.owner, "old_subject": old_subject, "new_subject": new_subject, "old_basis": old_basis, "new_basis": new_basis, "nodes": [{"id": "check", "source": original_source}, {"id": "dependency", "source": dependency}], "dependencies": [{"dependent": "check", "dependency": "dependency", "source": edge_source}], "checks": [{"id": "stable-check", "node": "check", "result": original, "obligations": []}], "coverage": {"population_source": population, "dependency_complete": conditions["dependency_complete"], "impact_complete": conditions["impact_complete"]}, "impact_cover": [], "new_obligations": [], "mandatory_gates": ["stable-check"], "retention": [{"result": original, **{name: conditions[name] for name in ("claim_scope", "assertion_basis", "observation_basis", "dependencies")}}]})
        args = self.refresh_arguments(declarations, previous_ref, current_ref, original_record)
        case = obj({"old_subject": old_subject, "new_subject": new_subject, "old_basis": old_basis, "new_basis": new_basis, "original": original, "original_record": original_record, "condition_records": condition_records, "conditions": conditions, "declarations": declarations, "population_source": population, "frontier_source": frontier, "original_source": original_source, "claim_scope_preserved": claim_scope_preserved})
        return runtime, args, case

    def refresh_arguments(self, declarations: Object, previous: Object, current: Object, original_record: Object) -> Object:
        source = self.f.write("inputs/preservation-refresh.json", declarations)
        invalidators = self.f.write("inputs/preservation-invalidators.json", {"schema": "a_c.fd-support.invalidators/1", "id": "preservation-invalidators", "declarations_sha256": source["sha256"], "events": []})
        return obj({"previous": previous, "current": current, "declarations": source, "invalidators": invalidators, "results": [original_record]})

    def retain_preservation_execution(self, args: Object, response: Object, outcome: Object, case: Object, history: dict[str, bytes]) -> None:
        """Optional exact raw custody for the dedicated qualification run, before assertions."""
        selected = os.environ.get("A_C_CORE_QUALIFICATION_CUSTODY")
        if selected is None:
            return
        target = Path(selected) / self._testMethodName
        target.mkdir(parents=True, exist_ok=False)
        for directory in (self.f.workspace, self.f.authorities):
            for source in sorted(directory.rglob("*")):
                if source.is_file():
                    destination = target / directory.name / source.relative_to(directory)
                    destination.parent.mkdir(parents=True, exist_ok=True); destination.write_bytes(source.read_bytes())
        (target / "policy.json").write_bytes((self.f.base / "policy.json").read_bytes())
        (target / "artifacts").mkdir()
        for identity, raw in sorted(self.f.store.records.items()):
            (target / "artifacts" / (identity.removeprefix("sha256:") + ".json")).write_bytes(raw)
        values: dict[str, object] = {"arguments.json": args, "response.json": response, "outcome.json": outcome, "case.json": case, "historical-records.json": {identity: {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)} for identity, raw in sorted(history.items())}}
        for name, value in values.items():
            (target / name).write_bytes(c.canonical(c._json(value)))
        manifest = {str(path.relative_to(target)): {"sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "bytes": path.stat().st_size} for path in sorted(target.rglob("*")) if path.is_file()}
        (target / "RAW_MANIFEST.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")

    def assert_preservation_history(self, runtime: c.Runtime, case: Object, history: dict[str, bytes], value: Object) -> None:
        for identity, raw in history.items():
            self.assertEqual(self.f.store.records.get(identity), raw, identity)
        original = c.judgment(runtime, c.as_object(case["original"]))
        self.assertEqual(original["subject"], case["old_subject"]); self.assertEqual(original["basis"], case["old_basis"])
        self.assertEqual(original["core_value"], "falsified"); self.assertFalse(original["domain_outcome"])
        retention = c.as_object(c.as_list(value["retention"])[0])
        self.assertEqual(retention["original"], case["original"]); self.assertEqual(retention["historical_subject"], case["old_subject"])
        self.assertEqual(retention["historical_core_value"], "falsified"); self.assertEqual(retention["new_subject"], case["new_subject"]); self.assertEqual(retention["new_basis"], case["new_basis"])
        self.assertNotEqual(case["old_subject"], case["new_subject"]); self.assertNotEqual(case["old_basis"], case["new_basis"])
        handoff = c.as_object(value["handoff"])
        self.assertEqual(handoff["original_results"], [case["original_record"]]); self.assertEqual(handoff["retention"], value["retention"])
        for name, condition in c.as_object(case["conditions"]).items():
            judgment_ref = c.as_object(c.as_object(condition)["evaluation"])
            check = c.judgment(runtime, judgment_ref)
            self.assertEqual(check["subject"], case["new_subject"], name); self.assertEqual(check["basis"], case["new_basis"], name)
            self.assertEqual(check["predicate"], c.as_object(condition)["predicate"])
            envelope = c.load_artifact(runtime, c.as_object(judgment_ref["record"]), "operation")
            self.assertEqual(c.as_object(c.as_object(envelope["payload"])["request"])["operation"], "checks.evaluate")
        operation_ids = []
        for identity, raw in self.f.store.records.items():
            envelope = c.as_object(c.parse_json(raw))
            if envelope["kind"] == "operation":
                request = c.as_object(c.as_object(envelope["payload"])["request"])
                if request["operation"] == "checks.evaluate" and c.as_object(request["arguments"])["predicate_id"] == "original-five":
                    operation_ids.append(identity)
        self.assertEqual(operation_ids, [c.as_object(case["original_record"])["id"]])

    def test_refresh_preserves_falsified_original_with_four_conditions_and_certified_frontier(self) -> None:
        runtime, args, case = self.preservation_case(); history = dict(self.f.store.records)
        response, outcome = self.f.run(runtime, "refresh.prepare", args)
        self.retain_preservation_execution(args, response, outcome, case, history)
        value = self.value(response); self.assert_preservation_history(runtime, case, history, value)
        self.assertEqual(value["differences"], []); self.assertEqual(value["affected_candidates"], []); self.assertEqual(value["gaps"], [])
        survivors = c.as_list(value["unchanged_candidates"])
        self.assertEqual(survivors, [{"check": "stable-check", "dependencies": ["check", "dependency"], "impact_intersection": [], "original": case["original"], "candidate": False}])
        retention = c.as_object(c.as_list(value["retention"])[0]); self.assertTrue(retention["supported_applicability"])
        proof = [c.as_object(item) for item in c.as_list(retention["proof"])]
        self.assertEqual([item["condition"] for item in proof], ["claim_scope", "assertion_basis", "observation_basis", "dependencies"])
        self.assertTrue(all(item["core_value"] == "satisfied" and item["gaps"] == [] for item in proof))
        self.assertEqual(value["mandatory_gates"], ["stable-check"]); self.assertEqual(value["new_obligations"], [])
        operation = c.as_object(c.load_artifact(runtime, c.as_object(response["evidence"]), "operation")["payload"])
        self.assertEqual(c.as_object(c.as_object(c.as_object(operation["response_without_evidence"])["result"])["value"])["retention"], value["retention"])

    def test_refresh_missing_preservation_condition_withholds_reuse_without_rewriting_history(self) -> None:
        runtime, args, case = self.preservation_case()
        declarations = copy.deepcopy(c.as_object(case["declarations"]))
        c.as_object(c.as_object(c.as_list(declarations["retention"])[0])["claim_scope"])["evaluation"] = None
        args = self.refresh_arguments(declarations, c.as_object(args["previous"]), c.as_object(args["current"]), c.as_object(case["original_record"]))
        history = dict(self.f.store.records); response, outcome = self.f.run(runtime, "refresh.prepare", args)
        self.retain_preservation_execution(args, response, outcome, case, history)
        value = self.value(response); self.assert_preservation_history(runtime, case, history, value)
        retention = c.as_object(c.as_list(value["retention"])[0]); self.assertFalse(retention["supported_applicability"])
        missing = next(c.as_object(item) for item in c.as_list(retention["proof"]) if c.as_object(item)["condition"] == "claim_scope")
        self.assertIsNone(missing["core_value"]); self.assertTrue(missing["gaps"])

    def test_refresh_falsified_preservation_condition_withholds_reuse_without_rewriting_history(self) -> None:
        runtime, args, case = self.preservation_case(claim_scope_preserved=False)
        history = dict(self.f.store.records); response, outcome = self.f.run(runtime, "refresh.prepare", args)
        self.retain_preservation_execution(args, response, outcome, case, history)
        value = self.value(response); self.assert_preservation_history(runtime, case, history, value)
        retention = c.as_object(c.as_list(value["retention"])[0]); self.assertFalse(retention["supported_applicability"])
        failure = next(c.as_object(item) for item in c.as_list(retention["proof"]) if c.as_object(item)["condition"] == "claim_scope")
        self.assertEqual(failure["core_value"], "falsified")

    def test_policy_revocation_does_not_hot_reload_for_read_access(self) -> None:
        runtime = self.f.runtime(); (self.f.base / "policy.json").write_text("changed after binding")
        response = c.execute_read(runtime, self.f.request("source.read", {"source": self.f.law, "encoding": "utf8"}))
        self.assertEqual(c.as_object(response["refusal"])["code"], "basis_stale"); self.assertIsNone(response["result"])


    def test_nested_conjunction_cannot_hide_inherited_counterexample(self) -> None:
        runtime = self.f.runtime(); failed, f, _ = self.protected_return(runtime, "falsified", "failed")
        passed, p, _ = self.protected_return(runtime, "satisfied", "passed")
        source, runtime = self.qualified_plan(runtime, [(failed, f)])
        response, _ = self.f.run(runtime, "results.conjoin", {"operator_id": "claude-rc9.conjunction/1", "plan": source, "returns": [failed], "current_observations": []})
        original_value = self.value(response); self.assertEqual(c.as_object(original_value["judgment"])["core_value"], "falsified")
        next_source, runtime = self.qualified_plan(runtime, [(passed, p)])
        plan = c._source_json(runtime, next_source, "ConjunctionPlan"); plan["inherited"] = [response["evidence"]]
        next_source, runtime = self.register_plan(plan)
        value = c.conjoin(runtime, {"operator_id": "claude-rc9.conjunction/1", "plan": next_source, "returns": [passed], "current_observations": []})
        self.assertEqual(c.as_object(value["judgment"])["core_value"], "falsified"); self.assertTrue(value["failures"]); self.assertTrue(value["constraint_failures"])

    def test_relations_excluded_obligation_keeps_raw_missing_mapping_fact(self) -> None:
        runtime = self.f.runtime(); declarations = self.f.relations(); a = "urn:a-c:toy:object:a"; b = "urn:a-c:toy:object:b"
        source = self.f.write("inputs/relations.json", declarations)
        first = c.relation_query(runtime, {"model": self.f.model, "declarations": source, "query": "coverage", "seeds": [a]})
        fact = next(c.as_object(raw) for raw in c.as_list(first["applicability"]) if c.as_object(c.as_object(raw)["target"]) == {"kind": "obligation", "id": b})
        expected = c.as_object(fact["expected_subject"]); self.f.predicate("not_applicable", {"literal": False}, expected); runtime = self.f.runtime()
        response, _ = self.f.run(runtime, "checks.evaluate", {"predicate_id": "not_applicable", "inputs": {}, "subject": expected, "basis": self.f.basis})
        for raw in c.as_list(declarations["applicability"]):
            row = c.as_object(raw)
            if row["target"] == {"kind": "obligation", "id": b}: row["condition"] = {"predicate": self.f.law, "evaluation": {"record": response["evidence"], "pointer": "/payload/response_without_evidence/result/value/judgment"}}
        source = self.f.write("inputs/relations.json", declarations)
        after = c.relation_query(runtime, {"model": self.f.model, "declarations": source, "query": "coverage", "seeds": [a]}); coverage = c.as_object(after["coverage"])
        self.assertEqual(coverage["missing_declared_support"], [b]); self.assertEqual(coverage["required_missing"], [])
        self.assertEqual(coverage["empty_declared_support"], [b]); self.assertTrue(coverage["explicit_unknowns"])

    def test_required_fit_predicate_stays_required_when_no_capacity_selected(self) -> None:
        self.f.predicate("required_fit", {"op": "equals", "args": [{"input": "context", "pointer": "/fit/judgment/core_value"}, {"literal": "satisfied"}]})
        c.as_object(c.as_object(c.as_object(self.f.policy["grants"])["work"])["admission"])["required_predicates"] = ["required_fit"]
        runtime = self.f.runtime(); response, _ = self.f.context(runtime)
        context_ref = c.as_object(c.as_object(response["result"])["artifact"])
        plan = c.build_preflight(runtime, self.f.request("contract.preflight", {"context": context_ref, "grant_id": "work", "executor_id": "registered", "result_key": "return", "observations": []}))
        self.assertTrue(c.as_object(plan["payload"])["gaps"])
        fit = c.as_object(self.value(response)["fit"]); self.assertIsNone(fit["judgment"])

    def test_same_actor_role_change_needs_existing_transition_before_writer(self) -> None:
        principal = c.as_object(c.as_object(self.f.policy["principals"])["worker"]); principal["actor_id"] = "executive"
        target = self.f.write("outputs/work.txt", b'old'); runtime = self.f.runtime("worker")
        args = obj({"grant_id": "work", "target": target, "mode": "replace", "record": {"text": "new", "provenance": self.f.law}, "interpretation": None, "observations": []})
        with self.assertRaises(c.SupportError) as caught: c.prepare_write(runtime, self.f.request("work.write", args))
        self.assertEqual(caught.exception.code, "transition_record_missing")
        transition = self.f.write("inputs/transition.json", {"actor_id": "executive", "old_activation": "old", "new_activation": "new", "old_frame": "executive-frame", "new_frame": "writer-frame", "operation": "work.write", "grant_id": "work", "subject": {"id": str((self.f.workspace / "outputs/work.txt").resolve()), "sha256": target["sha256"]}, "territory": c.as_object(c.as_object(self.f.policy["grants"])["work"])["territory"], "authority_source": self.f.owner})
        principal["role_transition"] = transition; runtime = self.f.runtime("worker")
        plan = c.prepare_write(runtime, self.f.request("work.write", args)); self.assertEqual(c.as_object(plan["payload"])["intended_sha256"], hashlib.sha256(b'new').hexdigest())

    def test_all_closed_codes_map_without_overwriting_inner_values(self) -> None:
        mapping = {"refused(capability)": "out_of_frame", "refused(authority)": "out_of_frame", "refused(basis)": "invalid_basis", "refused(constraint)": "falsified", "held(effect)": "indeterminate", "held(observation)": "indeterminate"}
        for code, value in c.CODES.items():
            if value is None: continue
            with self.subTest(code=code): self.assertEqual(c.operation_outcome("source.read", code=code)["core_value"], mapping[value])
        self.assertEqual(c.operation_outcome("checks.evaluate")["core_value"], "satisfied")

    def test_request_schema_transitive_closure_is_self_contained_and_smaller(self) -> None:
        source = c.request_schema("source.read"); definitions = c.as_object(source["$defs"])
        self.assertIn("SourceRef", definitions); self.assertNotIn("ConjunctionPlan", definitions)
        self.assertLess(len(definitions), len(c.as_object(c.CONTENT_SCHEMAS["$defs"])))
        request = self.f.request("source.read", {"source": self.f.law, "encoding": "utf8"})
        c.validate_schema(request, source, definitions)


    def test_new_model_wrappers_acquire_payload_and_refuse_unknown_seed(self) -> None:
        runtime = self.f.runtime(); identity = "urn:a-c:toy:object:a"
        response, _ = self.f.run(runtime, "records.read", {"model": self.f.model, "ids": [identity]})
        value = self.value(response); record = c.as_object(c.as_list(value["records"])[0])
        self.assertEqual(record["family"], "objects"); self.assertEqual(c.as_object(record["record"])["id"], identity)
        search = self.value(self.f.run(runtime, "records.find", {"model": self.f.model, "text": "object:a"})[0]); self.assertTrue(search["matches"])
        projected = self.value(self.f.run(runtime, "graph.project", {"model": self.f.model, "selections": [{"seeds": [identity]}]})[0]); self.assertTrue(projected["views"])
        bad, _ = self.f.run(runtime, "graph.project", {"model": self.f.model, "selections": [{"seeds": ["missing"]}]}); self.assertEqual(c.as_object(bad["refusal"])["code"], "domain_invalid")

    def test_exact_immutable_git_source_acquisition_uses_pinned_blob(self) -> None:
        member = "specification_methodology/v3/build_tenants/claude/standards/FOUNDATIONS.md"
        c.as_object(self.f.policy["sources"])["method-git"] = obj({"path": str(CODE.parents[3]), "read_scope": [{"path": member, "kind": "file"}], "kind": "git", "writable": False})
        runtime = self.f.runtime()
        source = {"engine": "immutable-git-blob", "root": "method-git", "path": member, "object": "c2cfa9b908d1722ae3f26c32fa4ece691083bdc3", "sha256": "fd2d895f90eb39bda0950c1c7ff02057ef5d8ae73fcbc5b3203f7e99081d6e3f", "selector": {"lines": [1, 3]}}
        value = self.value(self.f.run(runtime, "source.read", {"source": source, "encoding": "utf8"})[0])
        self.assertEqual(value["parent_sha256"], source["sha256"]); self.assertTrue(c.text(value["content"]).startswith("#"))
        self.assertEqual(c.as_object(value["acquisition"])["object"], source["object"])
        bad = copy.deepcopy(source); bad["object"] = "main"
        with self.assertRaises(c.SupportError): c.validate_request(self.f.request("source.read", {"source": bad, "encoding": "utf8"}))

    def test_explicit_file_scope_preserves_unlisted_addition_boundary(self) -> None:
        runtime = self.f.runtime(); scope = [{"root": "workspace", "path": "inputs/law.txt", "kind": "file"}]
        original = c.observe(runtime, c.as_list(c._json(scope)))
        self.f.write("inputs/not-in-scope.txt", b'unrelated')
        current = c.observe(runtime, c.as_list(c._json(scope)))
        self.assertEqual(c.observation_diff(original, current), []); self.assertEqual(len(c.as_list(current["entries"])), 1)

    def test_malformed_actual_final_stdout_is_retained_without_worker_verdict(self) -> None:
        runtime = self.f.runtime(); returned, _, _ = self.protected_return(runtime, "satisfied", raw_override=b'{')
        payload = c.as_object(c.load_artifact(runtime, returned, "return")["payload"])
        self.assertIsNone(payload["original"]); self.assertTrue(c.as_object(payload["producer"])["authenticated"])
        self.assertTrue(c.as_object(payload["binding_checks"])["gaps"])
        raw = c.as_object(c.load_artifact(runtime, c.as_object(payload["raw_payload"]), "raw")["payload"])
        self.assertEqual(base64.b64decode(c.text(raw["bytes_base64"])), b'{')

    def test_genuine_equal_answers_from_two_attempts_are_distinct_assessments(self) -> None:
        runtime = self.f.runtime(); first, a, _ = self.protected_return(runtime, "satisfied")
        second, b, _ = self.protected_return(runtime, "satisfied")
        self.assertEqual(a, b); self.assertNotEqual(first, second)
        source, runtime = self.qualified_plan(runtime, [(first, a), (second, b)])
        value = c.conjoin(runtime, {"operator_id": "claude-rc9.conjunction/1", "plan": source, "returns": [first, first, second], "current_observations": []})
        self.assertEqual(c.as_object(value["judgment"])["core_value"], "satisfied"); self.assertEqual(len(c.as_list(value["originals"])), 2); self.assertEqual(len(c.as_list(value["applicable"])), 2)

    def test_executive_prepared_context_delivery_binds_actual_target_source(self) -> None:
        executive = self.f.runtime(); response, outcome = self.f.context(executive)
        context_ref = c.as_object(c.as_object(response["result"])["artifact"]); context = c.as_object(c.load_artifact(executive, context_ref, "context")["payload"])
        request = self.f.request("dispatch.start", {"preflight": context_ref})
        attempt = self.f.artifact(executive, "attempt", {"target": "worker", "context": context_ref}, request)
        rendered = c.text(context["rendered_utf8"]).encode()
        self.f.artifact(executive, "raw", {"schema": "a_c.fd-support.attempt-event/1", "attempt": attempt, "cursor": 1, "kind": "context_delivery", "data": {"context": context_ref, "recipient": "worker", "rendered_sha256": hashlib.sha256(rendered).hexdigest(), "bytes": len(rendered), "complete": True, "scope": "actual controlled pipe write", "interval": {"clock": "unix_ns", "started_ns": 10, "ended_ns": 20}}, "previous": None, "observed_at_ns": 20})
        worker = self.f.runtime("worker"); source_ref = c.as_object(c.as_list(outcome["acquisitions"])[0])
        delivered, gaps = c._delivery_records(worker, source_ref, "worker", time.time_ns())
        self.assertTrue(delivered, gaps); self.assertEqual(gaps, [])


    def test_review_claim_population_detects_prior_fixture_member_exposure(self) -> None:
        runtime = self.f.runtime("reviewer"); candidate = self.f.write("inputs/candidate.txt", b'candidate'); fixture = self.f.write("inputs/candidate-test.txt", b'candidate fixture')
        claim = self.f.write("inputs/claim.json", {"id": "whole-candidate", "candidate_sources": [candidate, fixture]})
        self.f.run(runtime, "source.read", {"source": fixture, "encoding": "utf8"}, delivery=True)
        response, _ = self.f.run(runtime, "review.prepare", {"phase": "expectation", "claim": claim, "sources": [], "candidate": candidate, "proof": [], "comparison": None, "expectations": None, "expectation_body": None})
        value = self.value(response); self.assertTrue(value["population_complete"]); self.assertEqual(len(c.as_list(value["candidate_population"])), 2); self.assertTrue(value["exposure"])
        scopes = c.as_list(c.as_object(c.as_list(value["exposure"])[0])["scope"])
        self.assertIn(fixture, scopes)

    def test_opaque_claim_keeps_population_unknown_without_inferred_mapping(self) -> None:
        runtime = self.f.runtime("reviewer"); claim = self.f.write("inputs/claim.md", b'Review whatever the linked page means: https://example.invalid/candidate')
        response, _ = self.f.run(runtime, "review.prepare", {"phase": "expectation", "claim": claim, "sources": [], "candidate": None, "proof": [], "comparison": None, "expectations": None, "expectation_body": {"text": "Supplied words", "source_inputs": []}})
        value = self.value(response); self.assertFalse(value["population_complete"]); self.assertEqual(value["candidate_population"], []); self.assertTrue(value["gaps"])
        expectation = c.as_object(c.load_artifact(runtime, c.as_object(value["expectations"]), "expectation")["payload"])
        self.assertFalse(c.as_object(expectation["exposure_check"])["source_first_observed"])

    def test_review_claim_duplicate_ambiguous_and_dangling_refs_refuse(self) -> None:
        runtime = self.f.runtime("reviewer"); candidate = self.f.write("inputs/candidate.txt", b'candidate')
        competing = copy.deepcopy(candidate); competing["sha256"] = "0" * 64
        missing = copy.deepcopy(candidate); missing["path"] = "inputs/not-present"
        for refs in ([candidate, candidate], [candidate, competing], [missing]):
            claim = self.f.write("inputs/claim.json", {"id": "claim", "candidate_sources": refs})
            response, _ = self.f.run(runtime, "review.prepare", {"phase": "expectation", "claim": claim, "sources": [], "candidate": candidate, "proof": [], "comparison": None, "expectations": None, "expectation_body": None})
            self.assertEqual(response["status"], "refused"); self.assertIsNone(response["result"])

    def test_candidate_phase_acquires_entire_declared_population_and_wrong_parent_refuses(self) -> None:
        runtime = self.f.runtime("reviewer"); candidate = self.f.write("inputs/candidate.txt", b'candidate'); proof = self.f.write("inputs/proof.txt", b'actual proof')
        member = self.f.write("inputs/test.txt", b'actual tests'); claim = self.f.write("inputs/claim.json", {"id": "claim", "candidate_sources": [candidate, member]})
        response, _ = self.f.run(runtime, "review.prepare", {"phase": "candidate", "claim": claim, "sources": [], "candidate": candidate, "proof": [proof], "comparison": None, "expectations": None, "expectation_body": None})
        value = self.value(response); acquired = [c.as_object(raw)["source"] for raw in c.as_list(value["acquired"])]
        self.assertIn(member, acquired); self.assertIn(proof, acquired)
        wrong = copy.deepcopy(member); wrong["sha256"] = "0" * 64
        claim = self.f.write("inputs/claim.json", {"id": "claim", "candidate_sources": [candidate, wrong]})
        response, _ = self.f.run(runtime, "review.prepare", {"phase": "candidate", "claim": claim, "sources": [], "candidate": candidate, "proof": [], "comparison": None, "expectations": None, "expectation_body": None})
        self.assertEqual(c.as_object(response["refusal"])["code"], "digest_mismatch")

    def test_context_model_projection_retains_prepared_target_acquisition(self) -> None:
        runtime = self.f.runtime(); args = obj({"packet": self.f.packet(), "models": [{"model": self.f.model, "selections": [{"seeds": ["urn:a-c:toy:object:a"]}]}], "sources": [], "late_acquisition": [], "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8", "host_context": {"state": "unknown", "bytes": None, "evidence": None}}})
        response, outcome = self.f.run(runtime, "context.assemble", args); self.value(response)
        acquisitions = [c.as_object(c.load_artifact(runtime, c.as_object(ref), "acquisition")["payload"]) for ref in c.as_list(outcome["acquisitions"])]
        models = [item for item in acquisitions if item["model"] is not None]
        self.assertEqual(len(models), 1); self.assertEqual(models[0]["source"], self.f.model_source); self.assertEqual(models[0]["channel"], "actor-context"); self.assertEqual(models[0]["recipient"], "worker")


    def test_evidence_read_inline_context_content_preserves_candidate_exposure(self) -> None:
        candidate = self.f.write("inputs/candidate.txt", b'candidate content'); claim = self.f.write("inputs/claim.json", {"id": "claim", "candidate_sources": [candidate]})
        executive = self.f.runtime(); args = obj({"packet": self.f.packet(), "models": [], "sources": [candidate], "late_acquisition": [], "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8", "host_context": {"state": "unknown", "bytes": None, "evidence": None}}})
        response, _ = self.f.run(executive, "context.assemble", args); context_ref = c.as_object(c.as_object(response["result"])["artifact"])
        reviewer = self.f.runtime("reviewer"); self.f.run(reviewer, "evidence.read", {"artifact": context_ref}, delivery=True)
        prepared, _ = self.f.run(reviewer, "review.prepare", {"phase": "expectation", "claim": claim, "sources": [], "candidate": candidate, "proof": [], "comparison": None, "expectations": None, "expectation_body": None})
        self.assertTrue(self.value(prepared)["exposure"])


if __name__ == "__main__":
    unittest.main()

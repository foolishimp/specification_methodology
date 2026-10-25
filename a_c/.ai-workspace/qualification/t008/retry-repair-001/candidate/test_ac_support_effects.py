"""Source-selected local membrane controls; not semantic/ordinary-use acceptance.

These tests inspect actual filesystem/process effects. Synthetic lower-layer
Context/receipt carriers make no claim to Product/method admission qualification;
that full ordinary path is separately exercised by integration/actor assurance.
PublicRetryTests below uses the actual CLI and public Context/preflight receipts
for a bounded local-process retry regression; it is not actual F_P usability.
"""
from __future__ import annotations

import base64
import copy
import hashlib
import json
import os
import shutil
import stat
import subprocess
from pathlib import Path
import sys
import tempfile
import threading
import time
import unittest
from unittest.mock import patch
from typing import cast

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code"))
import ac_support_core as c
import ac_support_effects as e
from test_ac_support_core import Fixture


class MembraneCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="ac-effects-")
        self.root = Path(self.temp.name).resolve()
        self.source = self.root / "source"
        (self.source / "work").mkdir(parents=True)
        (self.source / "method").mkdir()
        (self.source / "definition.json").write_text('{"id":"fixture-product"}')
        (self.source / "authority.txt").write_text("Fixture operator's bounded existing grant.")
        self.profile = Path(__file__).resolve().parents[1] / "design" / "fd-method-claude-rc9.json"
        (self.source / "method" / "profile.json").write_bytes(self.profile.read_bytes())
        self.fixture = Path(__file__).resolve().parent / "support_fixtures" / "local_actor.py"
        self.python = Path(sys.executable).resolve()
        self.operations: list[c.JSON] = ["tools.describe", "workspace.observe", "source.read", "contract.preflight", "dispatch.start", "dispatch.observe", "dispatch.cancel", "events.wait", "work.write", "evidence.read", "checks.evaluate"]
        self.policy: c.Object = {
            "schema": "a_c.fd-support.policy/1", "id": "fixture-policy",
            "product": {"definition_id": "urn:fixture:product", "definition": self.source_ref("definition.json"), "authority_binding": {"definition_locator": "/authority", "owner_record": self.source_ref("authority.txt"), "mechanism": {"id": "product-policy-preflight/1", "source": self.source_ref("authority.txt"), "implementation_sha256": hashlib.sha256((Path(__file__).resolve().parents[1] / "code" / "ac_support_core.py").read_bytes()).hexdigest()}, "result_surface": {"root": str(self.root / "evidence"), "namespace": "fixture", "consumer": "fixture-consumer"}, "scope": "fixture-lower-layer-controls"}},
            "method_profile": {"id": c.PROFILE_ID, "sha256": c.PROFILE_SHA256, "source": self.source_ref("method/profile.json")},
            "sources": {"fixture": {"path": str(self.source), "read_scope": [{"path": "work", "kind": "directory"}, {"path": "definition.json", "kind": "file"}, {"path": "authority.txt", "kind": "file"}, {"path": "method", "kind": "directory"}], "kind": "workspace", "writable": True}},
            "principals": {"executive": {"actor_id": "fixture-executive", "role": "Executive", "family": "fixture", "authorship": "fixture-executive", "operations": self.operations, "role_binding": self.source_ref("authority.txt"), "role_transition": None}, "worker": {"actor_id": "fixture-worker", "role": "Worker", "family": "fixture", "authorship": "fixture-worker", "operations": self.operations, "role_binding": self.source_ref("authority.txt"), "role_transition": None}, "reviewer": {"actor_id": "fixture-reviewer", "role": "Reviewer", "family": "fixture-other", "authorship": "fixture-reviewer", "operations": self.operations, "role_binding": self.source_ref("authority.txt"), "role_transition": None}},
            "grants": {"fixture-grant": {"id": "fixture-grant", "authority_sources": [self.source_ref("authority.txt")], "outcome": {"id": "fixture-outcome", "source": self.source_ref("authority.txt")}, "principals": ["executive", "worker"], "targets": ["worker"], "operations": self.operations, "tools": [], "executors": ["fixture-actor"], "territory": [{"root": "fixture", "path": "work", "kind": "directory"}], "preconditions": [], "admission": {"mechanism_id": "product-policy-preflight/1", "mechanism_source": self.source_ref("authority.txt"), "authority_source": self.source_ref("authority.txt"), "required_predicates": [], "allowed_override_sources": []}, "notification_sink": "fixture-sink"}},
            "predicates": {}, "operators": {}, "executors": {},
            "event_sinks": {"fixture-sink": {"kind": "durable-file-events", "directory": "notifications", "consumer": "fixture-consumer", "authority_source": self.source_ref("authority.txt"), "retention": "indefinite"}},
            "independence_policy": None, "evidence_root": str(self.root / "evidence"),
            "limits": {"max_message_bytes": 1000000, "max_files": 1000, "max_bytes": 1000000, "max_history_records": 10000, "max_wait_ms": 5000, "max_output_bytes": 100000, "max_attempt_ms": 3000, "min_poll_ms": 20},
            "authority_sources": [self.source_ref("authority.txt")]
        }
        self.policy_path = self.root / "policy.json"
        self.runtime = self.runtime_for("worker")
        self.store = e.EvidenceStore(self.runtime)
        self.runtime = self.runtime.with_callbacks(self.store.resolve, self.store.query_artifacts)
        self.request = self.req("store-1", "tools.describe", {})

    def tearDown(self) -> None:
        custody = os.environ.get("AC_SUPPORT_EFFECTS_PROOF_ROOT")
        if custody is not None:
            destination = Path(custody).resolve() / self.id().replace(".", "_")
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(self.root, destination, symlinks=True)
            (destination / "CUSTODY.json").write_bytes(c.canonical({"schema": "a_c.effects-test-custody/1", "test": self.id(), "original_root": str(self.root), "meaning": "Historical raw local fixture/store bytes copied before disposable root removal; absolute original bindings are not silently rebased or represented as a new runnable policy.", "source_candidates": {name: hashlib.sha256((Path(__file__).resolve().parents[1] / "code" / name).read_bytes()).hexdigest() for name in ("ac_support.py", "ac_support_core.py", "ac_support_effects.py")}}))
        self.temp.cleanup()

    def source_ref(self, relative: str, *, absent: bool = False) -> c.Object:
        sha: c.JSON = None if absent else hashlib.sha256((self.source / relative).read_bytes()).hexdigest()
        return {"engine": "workspace-regular-file", "root": "fixture", "path": relative, "object": None, "sha256": sha, "selector": None}

    def runtime_for(self, principal: str) -> c.Runtime:
        raw = c.canonical(self.policy)
        self.policy_path.write_bytes(raw)
        return c.Runtime(self.policy_path, hashlib.sha256(raw).hexdigest(), principal, copy.deepcopy(self.policy), copy.deepcopy(c.as_object(c.as_object(self.policy["principals"])[principal])), self.root / "evidence")

    def req(self, identity: str, operation: str, arguments: c.Object) -> c.Object:
        return {"schema": c.REQUEST, "id": identity, "operation": operation, "arguments": arguments}

    def artifact(self, kind: str, payload: c.JSON, request: c.Object | None = None) -> tuple[c.Object, c.Object]:
        now = time.time_ns()
        return c.make_artifact(kind, payload, c.provenance(self.runtime, self.request if request is None else request, now, now))

    def recheck(self) -> c.Object:
        return {"schema": "a_c.fd-support.recheck/1", "policy_sha256": self.runtime.policy_sha256, "product_definition": self.source_ref("definition.json"), "method_profile": self.source_ref("method/profile.json"), "sources": [self.source_ref("authority.txt")], "observations": [], "executor_dependencies": []}

    def writer_plan(self, request: c.Object, raw: bytes, *, absent: bool = False) -> c.Object:
        target = self.source_ref("work/record.txt", absent=absent)
        args = c.as_object(request["arguments"])
        return {"schema": "a_c.fd-support.effect-plan/1", "operation": "work.write", "request_id": request["id"], "request_sha256": c.digest(request), "requester_principal": self.runtime.principal_id, "target_principal": None, "policy_sha256": self.runtime.policy_sha256, "recheck": self.recheck(), "payload": {"target": target, "path": str(self.source / "work" / "record.txt"), "mode": args["mode"], "record": args["record"], "interpretation": args["interpretation"], "intended_base64": base64.b64encode(raw).decode("ascii"), "intended_sha256": hashlib.sha256(raw).hexdigest(), "grant_id": "fixture-grant", "requester": "worker", "target_preimage": target["sha256"]}}

    def write_request(self, identity: str, text: str, *, absent: bool = False) -> c.Object:
        return self.req(identity, "work.write", {"grant_id": "fixture-grant", "target": self.source_ref("work/record.txt", absent=absent), "mode": "append", "record": {"text": text, "provenance": self.source_ref("authority.txt")}, "interpretation": None, "observations": []})

    def actor_setup(self, mode: str, *, timeout: int = 1500, file_observer: bool = False) -> tuple[c.Runtime, c.Object, Path]:
        target = self.source / "work" / "actor-effect.txt"
        executable: c.Object = {"path": str(self.python), "sha256": hashlib.sha256(self.python.read_bytes()).hexdigest()}
        executor: c.Object = {"id": "fixture-actor", "executable": executable, "argv": [str(self.python), str(self.fixture), mode, str(target)], "dependencies": [], "cwd": str(self.source), "environment": {"PATH": os.defpath}, "actor_id": "fixture-worker", "settings": {"timeout_ms": timeout, "termination_grace_ms": 100}, "tools": [], "effect_scope": {"kind": "cooperative-local-fixture", "external_descendants": "unknown"}, "stdin_mode": "context-utf8", "stdout_decoder": {"format": "json", "pointer": None, "decode_json_string": False}, "observers": [{"kind": "process-end"}]}
        if mode == "public-writer":
            c.as_list(executor["argv"]).extend([str(self.policy_path), str(Path(__file__).resolve().parents[1] / "code" / "ac_support.py")])
            executor["tools"] = ["work.write"]
            c.as_object(c.as_object(self.policy["grants"])["fixture-grant"])["tools"] = ["work.write"]
        if file_observer:
            expected: c.Object = {"engine": "workspace-regular-file", "root": "fixture", "path": "work/actor-effect.txt", "object": None, "sha256": hashlib.sha256(b"1").hexdigest(), "selector": None}
            c.as_list(executor["observers"]).append({"kind": "file-postimages", "scope": [{"root": "fixture", "path": "work", "kind": "directory"}], "expected": [expected]})
        c.as_object(self.policy["executors"])["fixture-actor"] = executor
        runtime = self.runtime_for("executive")
        # The separate supervisor reconstructs through the real trusted startup
        # parser; the synthetic receipt only scopes this lower-layer test.
        runtime = c.Runtime.from_policy(self.policy_path, runtime.policy_sha256, "executive")
        store = e.EvidenceStore(runtime)
        runtime = runtime.with_callbacks(store.resolve, store.query_artifacts)
        self.runtime, self.store = runtime, store
        context_payload: c.Object = {"schema": "a_c.fd-support.context/1", "packet": {"activation": {"id": "fixture-activation-" + mode, "revision": "1"}, "evidence_relations": {"consumer": "fixture-consumer"}, "subject_basis": {"method_profile": {"id": c.PROFILE_ID, "sha256": c.PROFILE_SHA256}, "observations": []}}, "projections": [], "sources": [], "late_acquisition": [], "boundaries": [], "rendered_utf8": "fixture exact input\n", "rendered_sha256": hashlib.sha256(b"fixture exact input\n").hexdigest(), "fit": {"judgment": None}, "observations": []}
        if mode == "public-writer":
            target_ref: c.Object = {"engine": "workspace-regular-file", "root": "fixture", "path": "work/actor-effect.txt", "object": None, "sha256": None, "selector": None}
            writer = self.req("actor-side-public-write", "work.write", {"grant_id": "fixture-grant", "target": target_ref, "mode": "append", "record": {"text": "actor-side tool progress", "provenance": self.source_ref("authority.txt")}, "interpretation": None, "observations": []})
            rendered = c.canonical({"policy_sha256": runtime.policy_sha256, "request": writer})
            context_payload["rendered_utf8"] = rendered.decode("utf-8")
            context_payload["rendered_sha256"] = hashlib.sha256(rendered).hexdigest()
        context, context_ref = self.artifact("context", context_payload)
        store.retain(context)
        receipt: c.Object = {"schema": "a_c.fd-support.preflight/1", "context": context_ref, "contract_sha256": "0" * 64, "grant_id": "fixture-grant", "executor_id": "fixture-actor", "result_key": "fixture-result", "requester": "executive", "target": "worker", "contract_state": "admitted", "decision": "admitted", "state_evidence": [], "mechanism": {"id": "fixture-lower-layer-only"}, "authority": self.source_ref("authority.txt"), "evaluations": [], "recheck": self.recheck(), "gaps": []}
        envelope, receipt_ref = self.artifact("preflight", receipt)
        store.retain(envelope)
        return runtime, self.req("dispatch-" + mode, "dispatch.start", {"preflight": receipt_ref}), target

    def finished(self, runtime: c.Runtime, attempt: c.Object, *, seconds: float = 5) -> c.Object:
        deadline = time.monotonic() + seconds
        sequence = 0
        while time.monotonic() < deadline:
            sequence += 1
            request = self.req("observe-" + c.text(attempt["sha256"])[:10] + "-" + str(sequence), "dispatch.observe", {"attempt": attempt, "after_event": 0})
            value = c.as_object(c.as_object(e.execute_effect(runtime, request, None)["result"])["value"])
            if value["process_end"] is not None and any(c.as_object(event)["kind"] == "effect_observation" for event in c.as_list(value["events"])):
                return value
            time.sleep(0.05)
        diagnostics = self.store.root / "diagnostics" / (c.text(attempt["sha256"]) + ".stderr")
        reason = diagnostics.read_text()[:2000] if diagnostics.exists() else "no supervisor stderr observed"
        self.fail("Registered fixture process did not produce an observed end within the bounded test deadline; " + reason)


class StoreTests(MembraneCase):
    def test_participating_publication_and_history_share_complete_prefix_lock(self) -> None:
        staged = threading.Event()
        release = threading.Event()
        reader_started = threading.Event()
        reader_done = threading.Event()
        failures: list[Exception] = []
        queries: list[c.Object] = []
        envelope, _ = self.artifact("raw", {"concurrent": True})
        def pause(point: str) -> None:
            if point == "artifact:raw:after_stage_fsync":
                staged.set()
                if not release.wait(2):
                    raise OSError("test release deadline")
        def publish() -> None:
            try:
                self.store.retain(envelope)
            except Exception as error:
                failures.append(error)
        def acquire_history() -> None:
            reader_started.set()
            queries.append(self.store.query_artifacts("raw", {}))
            reader_done.set()
        with patch.object(e, "_fault", pause):
            writer = threading.Thread(target=publish)
            writer.start()
            self.assertTrue(staged.wait(1))
            reader = threading.Thread(target=acquire_history)
            reader.start()
            self.assertTrue(reader_started.wait(1))
            self.assertFalse(reader_done.wait(0.05))
            release.set()
            writer.join(2)
            reader.join(2)
        self.assertFalse(failures)
        self.assertTrue(reader_done.is_set())
        self.assertTrue(queries[0]["complete"])
        self.assertEqual(len(c.as_list(queries[0]["refs"])), 1)

    def test_complete_envelope_roundtrip_and_distinct_execution_identity(self) -> None:
        first, first_ref = self.artifact("raw", {"answer": "equal"})
        self.store.retain(first)
        second, second_ref = self.artifact("raw", {"answer": "equal"}, self.req("store-2", "tools.describe", {}))
        self.store.retain(second)
        self.assertEqual(self.store.resolve(first_ref), c.canonical(first))
        self.assertNotEqual(first_ref, second_ref)
        self.assertEqual(self.store.retain(first), first_ref)
        self.assertEqual(len(c.as_list(self.store.query_artifacts("raw", {})["refs"])), 2)

    def test_missing_reference_tamper_symlink_and_corrupt_history(self) -> None:
        missing: c.Object = {"id": "sha256:" + "0" * 64, "sha256": "0" * 64}
        envelope, _ = self.artifact("resource", {"schema": "a_c.fd-support.resource/1", "owner": {"kind": "operation", "record": missing}})
        with self.assertRaises(c.SupportError):
            self.store.retain(envelope)
        valid, ref = self.artifact("raw", {"answer": 1})
        self.store.retain(valid)
        path = self.store.root / "objects" / (c.text(ref["sha256"]) + ".json")
        path.write_bytes(b"changed")
        with self.assertRaises(c.SupportError):
            self.store.resolve(ref)
        self.assertFalse(self.store.query_artifacts("raw", {})["complete"])
        path.unlink()
        path.symlink_to(self.source / "authority.txt")
        with self.assertRaises(c.SupportError):
            self.store.resolve(ref)

    def test_atomic_failure_surface_fresh_reconstruction(self) -> None:
        boundaries = ("before_stage", "before_stage_fsync", "after_stage_fsync", "before_publish", "after_publish", "before_directory_fsync", "after_directory_fsync")
        for index, boundary in enumerate(boundaries):
            with self.subTest(boundary=boundary):
                envelope, ref = self.artifact("raw", {"case": index})
                def fail(point: str) -> None:
                    if point == "artifact:raw:" + boundary:
                        raise OSError("injected " + point)
                with patch.object(e, "_fault", fail):
                    with self.assertRaises(c.SupportError):
                        self.store.retain(envelope)
                path = self.store.root / "objects" / (c.text(ref["sha256"]) + ".json")
                if boundary in ("after_publish", "before_directory_fsync", "after_directory_fsync"):
                    self.assertEqual(e.EvidenceStore(self.runtime).resolve(ref), c.canonical(envelope))
                else:
                    self.assertFalse(path.exists())

    def test_dependency_order_and_nonrecursive_operation_evidence(self) -> None:
        child, child_ref = self.artifact("observation", {"schema": "a_c.fd-support.observation/1", "scope": []})
        parent, parent_ref = self.artifact("context", {"schema": "a_c.fd-support.context/1", "observations": [child_ref]})
        outcome: c.CoreOutcome = {"result": {"artifact": parent_ref, "value": "available"}, "artifacts": [parent, child], "operation_outcome": c.operation_outcome("tools.describe"), "refusal": None, "acquisitions": []}
        response = e.persist_outcome(self.runtime, self.request, outcome)
        self.assertEqual(response["status"], "ok")
        evidence = c.load_artifact(self.runtime, c.as_object(response["evidence"]), "operation")
        self.assertIsNone(c.as_object(c.as_object(evidence["payload"])["response_without_evidence"])["evidence"])
        self.assertEqual(self.store.resolve(parent_ref), c.canonical(parent))

    def test_publication_failure_has_no_computed_durable_reference(self) -> None:
        child, child_ref = self.artifact("raw", {"child": True})
        outcome: c.CoreOutcome = {"result": {"artifact": child_ref, "value": "available"}, "artifacts": [child], "operation_outcome": c.operation_outcome("tools.describe"), "refusal": None, "acquisitions": []}
        def fail(point: str) -> None:
            if point == "artifact:raw:before_publish":
                raise OSError("publication unavailable")
        with patch.object(e, "_fault", fail):
            response = e.persist_outcome(self.runtime, self.request, outcome)
        self.assertEqual(response["status"], "error")
        self.assertIsNone(response["evidence"])
        self.assertIsNone(response["result"])
        self.assertEqual(c.as_object(response["refusal"])["code"], "evidence_publication_failed")

    def test_prepared_acquisition_refs_survive_without_rewrapping(self) -> None:
        acquisition, ref = self.artifact("acquisition", {"source": self.source_ref("authority.txt"), "delivery": "prepared"})
        outcome: c.CoreOutcome = {"result": {"artifact": None, "value": "content"}, "artifacts": [acquisition], "operation_outcome": c.operation_outcome("tools.describe"), "refusal": None, "acquisitions": [ref]}
        response = e.persist_outcome(self.runtime, self.request, outcome)
        operation = c.as_object(c.load_artifact(self.runtime, c.as_object(response["evidence"]), "operation")["payload"])
        self.assertEqual(operation["acquisitions"], [ref])
        self.assertEqual(self.store.resolve(ref), c.canonical(acquisition))

    def test_negative_inner_result_is_returned_and_refusals_keep_mapping(self) -> None:
        outcome: c.CoreOutcome = {"result": {"artifact": None, "value": {"judgment": {"core_value": "falsified"}}}, "artifacts": [], "operation_outcome": c.operation_outcome("tools.describe"), "refusal": None, "acquisitions": []}
        response = e.persist_outcome(self.runtime, self.request, outcome)
        self.assertEqual(response["status"], "ok")
        self.assertEqual(c.as_object(c.as_object(c.as_object(response["result"])["value"])["judgment"])["core_value"], "falsified")
        refusal = c.refusal_outcome(self.runtime, self.request, c.SupportError("authority_missing", "no grant"))
        response = e.persist_outcome(self.runtime, self.request, refusal)
        self.assertEqual(response["status"], "refused")
        self.assertEqual(c.as_object(response["operation_outcome"])["core_value"], "out_of_frame")


class DependencyTests(MembraneCase):
    def missing(self) -> c.Object:
        return {"id": "sha256:" + "0" * 64, "sha256": "0" * 64}

    def public_call(self, request: c.Object) -> c.Object:
        entry = Path(__file__).resolve().parents[1] / "code" / "ac_support.py"
        argv = [str(self.python), str(entry), "--policy", str(self.policy_path), "--policy-sha256", self.runtime.policy_sha256, "--principal", self.runtime.principal_id, "call", "--request", "-"]
        run = subprocess.run(argv, input=c.canonical(request), capture_output=True, timeout=5, check=False)
        stem = self.root / c.text(request["id"])
        stem.with_suffix(".stdout").write_bytes(run.stdout)
        stem.with_suffix(".stderr").write_bytes(run.stderr)
        stem.with_suffix(".invocation.json").write_bytes(c.canonical({"argv": cast(c.JSON, argv), "request": request, "returncode": run.returncode}))
        return c.as_object(c.parse_json(run.stdout))

    def test_public_missing_input_preserves_original_refusal_and_readable_operation(self) -> None:
        request = self.req("missing-public-input", "evidence.read", {"artifact": self.missing()})
        response = self.public_call(request)
        self.assertEqual(c.as_object(response["refusal"])["code"], "source_missing")
        self.assertEqual(response["status"], "refused")
        self.assertEqual(c.as_object(response["operation_outcome"])["value"], "refused(basis)")
        self.assertEqual(c.as_object(response["operation_outcome"])["core_value"], "invalid_basis")
        ref = c.as_object(response["evidence"])
        retained = c.load_artifact(self.runtime, ref, "operation")
        self.assertEqual(c.as_object(retained["payload"])["request"], request)
        read = self.public_call(self.req("read-refused-operation", "evidence.read", {"artifact": ref}))
        self.assertEqual(read["status"], "ok")
        self.assertEqual(c.as_object(c.as_object(read["result"])["value"])["envelope"], retained)

    def test_identity_shaped_raw_json_and_literal_result_are_data(self) -> None:
        literal = self.missing()
        raw, ref = self.artifact("raw", {"literal": literal, "nested": [{"subject": literal}]})
        self.store.retain(raw)
        self.assertEqual(self.store.resolve(ref), c.canonical(raw))
        outcome: c.CoreOutcome = {"result": {"artifact": None, "value": {"literal": literal}}, "artifacts": [], "operation_outcome": c.operation_outcome("tools.describe"), "refusal": None, "acquisitions": []}
        response = e.persist_outcome(self.runtime, self.request, outcome)
        self.assertEqual(response["status"], "ok")
        self.assertEqual(c.as_object(c.as_object(response["result"])["value"])["literal"], literal)
        refusal = c.refusal_outcome(self.runtime, self.request, c.SupportError("authority_missing", "No supplied authority", [literal], []))
        refused = e.persist_outcome(self.runtime, self.request, refusal)
        self.assertEqual(refused["status"], "refused")
        self.assertEqual(c.as_object(refused["refusal"])["gaps"], [literal])
        self.assertIsNotNone(refused["evidence"])

    def test_public_projected_source_identity_is_preserved_without_dereference(self) -> None:
        (self.source / "work" / "literal.json").write_bytes(c.canonical({"record": self.missing()}))
        self.operations.append("work.project")
        self.runtime = self.runtime_for("worker").with_callbacks(self.store.resolve, self.store.query_artifacts)
        request = self.req("literal-public-projection", "work.project", {"carrier": self.source_ref("work/literal.json"), "selection": ["/record"]})
        response = self.public_call(request)
        self.assertEqual(response["status"], "ok")
        value = c.as_object(c.as_object(response["result"])["value"])
        self.assertEqual(c.as_object(c.as_list(value["selected"])[0])["original"], self.missing())
        self.assertIsNotNone(response["evidence"])

    def test_true_primary_provenance_and_carrier_support_must_exist(self) -> None:
        missing = self.missing()
        outcome: c.CoreOutcome = {"result": {"artifact": missing, "value": "declared required support"}, "artifacts": [], "operation_outcome": c.operation_outcome("tools.describe"), "refusal": None, "acquisitions": []}
        response = e.persist_outcome(self.runtime, self.request, outcome)
        self.assertEqual(c.as_object(response["refusal"])["code"], "evidence_publication_failed")
        now = time.time_ns()
        provenance = c.provenance(self.runtime, self.request, now, now, attempt=missing)
        envelope, _ = c.make_artifact("raw", {"literal": "not the dependency"}, provenance)
        with self.assertRaises(c.SupportError):
            self.store.retain(envelope)
        resource, _ = self.artifact("resource", {"schema": "a_c.fd-support.resource/1", "owner": {"kind": "operation", "record": missing}})
        with self.assertRaises(c.SupportError):
            self.store.retain(resource)

    def test_declared_carrier_support_rejects_missing_and_tampered_parents(self) -> None:
        missing = self.missing()
        retained: c.Object = {"engine": "retained-evidence", "root": "evidence", "path": missing["id"], "object": None, "sha256": missing["sha256"], "selector": None}
        carriers: list[tuple[str, c.Object]] = [
            ("context", {"observations": [missing]}),
            ("preflight", {"context": missing}),
            ("preflight", {"state_evidence": [missing]}),
            ("preflight", {"recheck": {"observations": [missing]}}),
            ("attempt", {"preflight": missing}),
            ("attempt", {"retry_of": missing}),
            ("return", {"raw_payload": missing}),
            ("expectation", {"source_inputs": [missing]}),
            ("acquisition", {"schema": "a_c.fd-support.acquisition/1", "source": retained}),
            ("acquisition", {"schema": "a_c.fd-support.transport-observation/1", "operation": missing}),
            ("operation", {"artifacts": [missing]}),
            ("resource", {"owner": {"record": missing}}),
            ("raw", {"schema": "a_c.fd-support.request-claim/1", "selected_policy": missing}),
            ("raw", {"schema": "a_c.fd-support.writer-intent/1", "recheck": {"observations": [missing]}}),
            ("raw", {"schema": "a_c.fd-support.writer-result/1", "intent": missing}),
            ("raw", {"schema": "a_c.fd-support.writer-recovery/1", "intent": missing}),
            ("raw", {"schema": "a_c.fd-support.process-output/1", "attempt": missing}),
            ("raw", {"schema": "a_c.fd-support.attempt-event/1", "previous": missing, "kind": "actor_started"}),
            ("raw", {"schema": "a_c.fd-support.attempt-event/1", "kind": "output_finalized", "data": {"stdout": missing}}),
            ("qualification", {"schema": "a_c.fd-support.operator-qualification/1", "proof_sources": [missing]}),
            ("raw", {"schema": "a_c.fd-support.operator-qualification/1", "dependencies": [retained]}),
        ]
        for kind, payload in carriers:
            with self.subTest(kind=kind, payload=payload):
                envelope, reference = self.artifact(kind, payload)
                with self.assertRaises(c.SupportError) as raised:
                    self.store.retain(envelope)
                self.assertEqual(raised.exception.code, "source_missing")
                self.assertFalse((self.store.root / "objects" / (c.text(reference["sha256"]) + ".json")).exists())
        child, child_ref = self.artifact("observation", {"scope": []})
        self.store.retain(child)
        (self.store.root / "objects" / (c.text(child_ref["sha256"]) + ".json")).write_bytes(b"tampered")
        parent, _ = self.artifact("context", {"observations": [child_ref]})
        with self.assertRaises(c.SupportError) as corrupt:
            self.store.retain(parent)
        self.assertEqual(corrupt.exception.code, "digest_mismatch")

    def test_return_ownership_graph_preserves_quoted_actor_and_qualification_data(self) -> None:
        # This is a support-retention graph, not semantic Return admission.
        observation, observation_ref = self.artifact("observation", {"scope": []})
        context, context_ref = self.artifact("context", {"observations": [observation_ref]})
        preflight, preflight_ref = self.artifact("preflight", {"context": context_ref})
        attempt, attempt_ref = self.artifact("attempt", {"preflight": preflight_ref, "context": context_ref})
        output, output_ref = self.artifact("raw", {"schema": "a_c.fd-support.process-output/1", "attempt": attempt_ref, "bytes_base64": ""})
        original: c.Object = {"subject": self.missing(), "actor_supplied": {"evidence": [self.missing()]}}
        returned, returned_ref = self.artifact("return", {"attempt": attempt_ref, "raw_payload": output_ref, "return_contract": self.source_ref("authority.txt"), "original": original, "producer": {"attempt": attempt_ref}})
        artifacts: list[c.JSON] = [returned, output, attempt, preflight, context, observation]
        outcome: c.CoreOutcome = {"result": {"artifact": returned_ref, "value": {"quoted": original}}, "artifacts": artifacts, "operation_outcome": c.operation_outcome("tools.describe"), "refusal": None, "acquisitions": []}
        response = e.persist_outcome(self.runtime, self.request, outcome)
        self.assertEqual(response["status"], "ok")
        self.assertEqual(self.store.resolve(returned_ref), c.canonical(returned))
        read = self.public_call(self.req("read-original-return", "evidence.read", {"artifact": returned_ref}))
        self.assertEqual(read["status"], "ok")
        generic, generic_ref = self.artifact("qualification", {"subject": self.missing(), "evidence": [self.missing()]})
        self.store.retain(generic)
        known, known_ref = self.artifact("qualification", {"schema": "a_c.fd-support.operator-qualification/1", "method_profile": self.missing(), "fragment": [self.missing()], "dependencies": [], "proof_sources": [generic_ref]})
        self.store.retain(known)
        self.assertEqual(self.store.resolve(known_ref), c.canonical(known))

    def test_unresolved_candidates_and_unknown_host_do_not_claim_support(self) -> None:
        retained: c.Object = {"engine": "retained-evidence", "root": "evidence", "path": self.missing()["id"], "object": None, "sha256": self.missing()["sha256"], "selector": None}
        context, ref = self.artifact("context", {"fit": {"host_context": {"state": "unknown", "bytes": None, "evidence": retained}}, "late_acquisition": [retained]})
        self.store.retain(context)
        self.assertEqual(self.store.resolve(ref), c.canonical(context))
        candidate: c.Object = {"core_value": None, "judgment": {"record": self.missing(), "pointer": "/unavailable"}, "condition": {"predicate": retained}, "gaps": [{"missing": self.missing()}]}
        request = self.req("unresolved-relation", "relations.query", {})
        outcome: c.CoreOutcome = {"result": {"artifact": None, "value": {"subject": self.missing(), "basis": {"observations": []}, "applicability": [candidate]}}, "artifacts": [], "operation_outcome": c.operation_outcome("relations.query"), "refusal": None, "acquisitions": []}
        self.assertEqual(e.persist_outcome(self.runtime, request, outcome)["status"], "ok")

    def test_public_predicate_identity_subject_and_json_domain_are_data(self) -> None:
        basis: c.Object = {"method_profile": {"id": c.PROFILE_ID, "sha256": c.PROFILE_SHA256}, "observations": []}
        definition: c.Object = {"id": "literal-identity", "source": self.source_ref("authority.txt"), "subject": self.missing(), "basis": basis, "input_names": [], "expression": {"literal": self.missing()}, "limits": ["Literal identity data, not a protected support coordinate."]}
        c.as_object(self.policy["predicates"])["literal-identity"] = definition
        self.runtime = self.runtime_for("worker").with_callbacks(self.store.resolve, self.store.query_artifacts)
        request = self.req("literal-public-predicate", "checks.evaluate", {"predicate_id": "literal-identity", "inputs": {}, "subject": self.missing(), "basis": basis})
        response = self.public_call(request)
        self.assertEqual(response["status"], "ok")
        judgment = c.as_object(c.as_object(c.as_object(response["result"])["value"])["judgment"])
        self.assertEqual(judgment["subject"], self.missing())
        self.assertEqual(judgment["domain_outcome"], self.missing())
        self.assertEqual(judgment["core_value"], "invalid_basis")
        self.assertIsNotNone(response["evidence"])


class ReceiptTests(MembraneCase):
    def draft(self, accepted: bool = True) -> tuple[c.Object, c.Object]:
        context, context_ref = self.artifact("context", {"schema": "a_c.fd-support.context/1"})
        self.store.retain(context)
        request = self.req("receipt-1", "contract.preflight", {"context": context_ref, "grant_id": "fixture-grant", "executor_id": "fixture-actor", "result_key": "fixture-result", "observations": []})
        payload: c.Object = {"schema": "a_c.fd-support.preflight/1", "context": context_ref, "contract_sha256": "0" * 64, "grant_id": "fixture-grant", "executor_id": "fixture-actor", "result_key": "fixture-result", "requester": "worker", "target": "worker", "contract_state": "drafted", "decision": None, "state_evidence": [], "mechanism": {"id": "fixture-lower-layer-only"}, "authority": self.source_ref("authority.txt"), "evaluations": [{"core_value": "satisfied" if accepted else "out_of_frame"}], "recheck": self.recheck(), "gaps": [] if accepted else ["fixture denied guard"]}
        return request, {"schema": "a_c.fd-support.effect-plan/1", "operation": "contract.preflight", "request_id": request["id"], "request_sha256": c.digest(request), "requester_principal": "worker", "target_principal": "worker", "policy_sha256": self.runtime.policy_sha256, "recheck": self.recheck(), "payload": payload}

    def test_receipt_commits_once_and_rejected_decision_is_available_output(self) -> None:
        request, plan = self.draft(False)
        first = e.execute_effect(self.runtime, request, plan)
        value = c.as_object(c.as_object(first["result"])["value"])
        self.assertEqual(value["contract_state"], "rejected")
        self.assertEqual(value["decision"], "rejected")
        self.assertEqual(c.as_object(first["operation_outcome"])["value"], "returned")
        self.assertEqual(e.execute_effect(self.runtime, request, plan), first)
        self.assertEqual(len(c.as_list(self.store.query_artifacts("preflight", {})["refs"])), 1)

    def test_failure_before_receipt_marker_does_not_commit_admission(self) -> None:
        request, plan = self.draft()
        def fail(point: str) -> None:
            if point == "artifact:preflight:before_publish":
                raise OSError("before complete receipt")
        with patch.object(e, "_fault", fail):
            outcome = e.execute_effect(self.runtime, request, plan)
        self.assertEqual(c.as_object(outcome["operation_outcome"])["value"], "held(observation)")
        self.assertEqual(c.as_list(self.store.query_artifacts("preflight", {})["refs"]), [])

    def test_failure_after_receipt_marker_reconstructs_original_decision(self) -> None:
        request, plan = self.draft()
        def fail(point: str) -> None:
            if point == "artifact:preflight:after_publish":
                raise OSError("after complete receipt")
        with patch.object(e, "_fault", fail):
            outcome = e.execute_effect(self.runtime, request, plan)
        self.assertEqual(c.as_object(outcome["operation_outcome"])["value"], "held(observation)")
        replay = e.execute_effect(self.runtime, request, plan)
        self.assertEqual(c.as_object(c.as_object(replay["result"])["value"])["decision"], "admitted")
        self.assertEqual(len(c.as_list(e.EvidenceStore(self.runtime).query_artifacts("preflight", {})["refs"])), 1)


class WriterTests(MembraneCase):
    def test_append_exact_replay_and_conflicting_identity(self) -> None:
        path = self.source / "work" / "record.txt"
        path.write_bytes(b"original")
        path.chmod(0o640)
        request = self.write_request("write-1", "\nrecord")
        plan = self.writer_plan(request, b"original\nrecord")
        first = e.execute_effect(self.runtime, request, plan)
        self.assertEqual(path.read_bytes(), b"original\nrecord")
        self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o640)
        self.assertEqual(e.execute_effect(self.runtime, request, plan), first)
        self.assertEqual(path.read_bytes(), b"original\nrecord")
        conflict = copy.deepcopy(request)
        c.as_object(c.as_object(conflict["arguments"])["record"])["text"] = "different"
        with self.assertRaises(c.SupportError) as caught:
            e.execute_effect(self.runtime, conflict, self.writer_plan(conflict, b"different"))
        self.assertEqual(caught.exception.code, "request_identity_conflict")

    def test_exclusive_creation_and_wrong_direct_role(self) -> None:
        request = self.write_request("new", "exact", absent=True)
        result = e.execute_effect(self.runtime, request, self.writer_plan(request, b"exact", absent=True))
        self.assertEqual(c.as_object(result["operation_outcome"])["value"], "returned")
        self.assertEqual((self.source / "work" / "record.txt").read_bytes(), b"exact")
        for role in ("executive", "reviewer"):
            self.runtime = self.runtime_for(role)
            self.runtime = self.runtime.with_callbacks(self.store.resolve, self.store.query_artifacts)
            denied = self.write_request("denied-" + role, "evil")
            outcome = e.execute_effect(self.runtime, denied, self.writer_plan(denied, b"evil"))
            self.assertEqual(c.as_object(outcome["refusal"])["code"], "role_effect_denied")
            self.assertEqual((self.source / "work" / "record.txt").read_bytes(), b"exact")

    def test_stale_preimage_and_material_drift_are_distinct(self) -> None:
        path = self.source / "work" / "record.txt"
        path.write_bytes(b"old")
        request = self.write_request("stale-target", "new")
        plan = self.writer_plan(request, b"oldnew")
        path.write_bytes(b"changed")
        outcome = e.execute_effect(self.runtime, request, plan)
        self.assertEqual(c.as_object(outcome["refusal"])["code"], "target_conflict")
        self.assertEqual(path.read_bytes(), b"changed")
        request = self.write_request("stale-basis", "new")
        plan = self.writer_plan(request, b"changednew")
        (self.source / "authority.txt").write_text("advanced")
        outcome = e.execute_effect(self.runtime, request, plan)
        self.assertEqual(c.as_object(outcome["refusal"])["code"], "basis_missing")
        self.assertEqual(path.read_bytes(), b"changed")

    def test_post_target_evidence_failure_never_repeats_or_rolls_back(self) -> None:
        path = self.source / "work" / "record.txt"
        path.write_bytes(b"old")
        request = self.write_request("lost-result", "new")
        plan = self.writer_plan(request, b"oldnew")
        def fail(point: str) -> None:
            if point == "writer:after_target_publication":
                raise OSError("lost after replace")
        with patch.object(e, "_fault", fail):
            outcome = e.execute_effect(self.runtime, request, plan)
        self.assertEqual(path.read_bytes(), b"oldnew")
        self.assertEqual(c.as_object(outcome["operation_outcome"])["value"], "held(effect)")
        again = e.execute_effect(self.runtime, request, plan)
        self.assertEqual(path.read_bytes(), b"oldnew")
        self.assertEqual(again, outcome)

    def test_fatal_post_target_interruption_reconstructs_intent_without_retry(self) -> None:
        path = self.source / "work" / "record.txt"
        path.write_bytes(b"old")
        request = self.write_request("fatal-post-target", "new")
        plan = self.writer_plan(request, b"oldnew")
        def interrupt(point: str) -> None:
            if point == "writer:after_target_publication":
                raise SystemExit(77)
        with patch.object(e, "_fault", interrupt), self.assertRaises(SystemExit):
            e.execute_effect(self.runtime, request, plan)
        self.assertEqual(path.read_bytes(), b"oldnew")
        self.runtime = self.runtime.with_callbacks(e.EvidenceStore(self.runtime).resolve, e.EvidenceStore(self.runtime).query_artifacts)
        reconstructed = e.execute_effect(self.runtime, request, plan)
        self.assertEqual(c.as_object(reconstructed["refusal"])["code"], "effect_unreconciled")
        self.assertEqual(path.read_bytes(), b"oldnew")
        value = c.as_object(c.as_object(reconstructed["result"])["value"])
        self.assertTrue(value["matches_intended_postimage"])
        self.assertFalse(value["repeated"])

    def test_every_writer_publication_boundary_preserves_whole_target(self) -> None:
        boundaries = ("before_stage", "before_stage_fsync", "after_stage_fsync", "before_publish", "after_publish", "before_directory_fsync", "after_directory_fsync")
        path = self.source / "work" / "record.txt"
        for index, boundary in enumerate(boundaries):
            with self.subTest(boundary=boundary):
                path.write_bytes(b"before")
                request = self.write_request("writer-boundary-" + str(index), "+after")
                plan = self.writer_plan(request, b"before+after")
                def fail(point: str) -> None:
                    if point == "writer_target:" + boundary:
                        raise OSError("post-validation " + point)
                with patch.object(e, "_fault", fail):
                    result = e.execute_effect(self.runtime, request, plan)
                self.assertEqual(c.as_object(result["operation_outcome"])["value"], "held(effect)")
                expected = b"before+after" if boundary in ("after_publish", "before_directory_fsync", "after_directory_fsync") else b"before"
                self.assertEqual(path.read_bytes(), expected)
                self.assertTrue(list((self.store.root / "requests").glob("*.intent.json")))
                self.assertEqual(e.execute_effect(self.runtime, request, plan), result)
                self.assertEqual(path.read_bytes(), expected)

    def test_exclusive_creation_failure_has_absent_or_complete_target(self) -> None:
        path = self.source / "work" / "record.txt"
        for index, boundary in enumerate(("before_publish", "after_publish")):
            with self.subTest(boundary=boundary):
                if path.exists():
                    path.unlink()
                request = self.write_request("create-boundary-" + str(index), "whole", absent=True)
                plan = self.writer_plan(request, b"whole", absent=True)
                def fail(point: str) -> None:
                    if point == "writer_target:" + boundary:
                        raise OSError(point)
                with patch.object(e, "_fault", fail):
                    result = e.execute_effect(self.runtime, request, plan)
                self.assertEqual(c.as_object(result["operation_outcome"])["value"], "held(effect)")
                self.assertEqual(path.read_bytes() if path.exists() else None, b"whole" if boundary == "after_publish" else None)

    def test_symlink_and_competing_target_writer_refuse(self) -> None:
        path = self.source / "work" / "record.txt"
        path.write_bytes(b"old")
        request = self.write_request("locked-target", "new")
        plan = self.writer_plan(request, b"oldnew")
        with self.store._lock("target:" + str(path)):
            result = e.execute_effect(self.runtime, request, plan)
        self.assertEqual(c.as_object(result["refusal"])["code"], "target_conflict")
        self.assertEqual(path.read_bytes(), b"old")
        path.unlink()
        path.symlink_to(self.source / "authority.txt")
        request["id"] = "symlink-target"
        plan["request_id"] = request["id"]
        plan["request_sha256"] = c.digest(request)
        result = e.execute_effect(self.runtime, request, plan)
        self.assertEqual(c.as_object(result["refusal"])["code"], "path_refused")
        self.assertEqual((self.source / "authority.txt").read_text(), "Fixture operator's bounded existing grant.")


class ProcessTests(MembraneCase):
    def test_actor_side_public_mcp_writer_completes_before_actor_exit(self) -> None:
        runtime, request, target = self.actor_setup("public-writer", timeout=1800)
        first = e.execute_effect(runtime, request, None)
        ref = c.as_object(c.as_object(first["result"])["artifact"])
        value = self.finished(runtime, ref)
        self.assertEqual(c.as_object(value["process_end"])["returncode"], 0)
        output = c.as_object(c.load_artifact(runtime, c.as_object(c.as_object(value["output"])["stdout"]), "raw")["payload"])
        actor = json.loads(base64.b64decode(c.text(output["bytes_base64"])))
        self.assertTrue(actor["writer_progress_before_actor_exit"])
        self.assertEqual(actor["tool_result"]["status"], "ok")
        self.assertEqual(target.read_bytes(), b"actor-side tool progress")
        self.assertEqual(len(actor["mcp_raw_responses"]), 2)

    def test_real_registered_invocation_exact_replay_and_final_output(self) -> None:
        runtime, request, target = self.actor_setup("count")
        first = e.execute_effect(runtime, request, None)
        ref = c.as_object(c.as_object(first["result"])["artifact"])
        value = self.finished(runtime, ref)
        self.assertEqual(target.read_text(), "1")
        self.assertEqual(e.execute_effect(runtime, request, None), first)
        self.assertEqual(target.read_text(), "1")
        self.assertEqual(c.as_object(value["process_end"])["returncode"], 0)
        output = c.as_object(value["output"])
        raw = c.as_object(c.load_artifact(runtime, c.as_object(output["stdout"]), "raw")["payload"])
        body = json.loads(base64.b64decode(c.text(raw["bytes_base64"])))
        self.assertEqual(body["stdin_sha256"], hashlib.sha256(b"fixture exact input\n").hexdigest())
        self.assertEqual(c.as_object(value["effect"])["value"], "completion_unknown")
        self.assertEqual(e.supervise(runtime, ref), 0)
        self.assertEqual(target.read_text(), "1")

    def test_timeout_preserves_partial_effect_and_separate_end(self) -> None:
        runtime, request, target = self.actor_setup("partial", timeout=150)
        first = e.execute_effect(runtime, request, None)
        ref = c.as_object(c.as_object(first["result"])["artifact"])
        value = self.finished(runtime, ref)
        self.assertEqual(target.read_text(), "partial-effect")
        kinds = [c.as_object(event)["kind"] for event in c.as_list(value["events"])]
        self.assertIn("deadline", kinds)
        self.assertIn("signal_delivery", kinds)
        self.assertEqual(c.as_object(value["effect"])["value"], "completion_unknown")
        self.assertIsNotNone(value["process_end"])

    def test_forged_anchor_and_new_unreconciled_attempt_refuse(self) -> None:
        missing: c.Object = {"id": "sha256:" + "0" * 64, "sha256": "0" * 64}
        with self.assertRaises(c.SupportError):
            e.supervise(self.runtime, missing)
        runtime, request, target = self.actor_setup("count")
        first = e.execute_effect(runtime, request, None)
        self.finished(runtime, c.as_object(c.as_object(first["result"])["artifact"]))
        new_request = copy.deepcopy(request)
        new_request["id"] = "new-unreconciled-attempt"
        refused = e.execute_effect(runtime, new_request, None)
        self.assertEqual(c.as_object(refused["refusal"])["code"], "effect_unreconciled")
        self.assertEqual(target.read_text(), "1")

    def test_cancel_records_request_and_signal_with_partial_effect(self) -> None:
        runtime, request, target = self.actor_setup("partial", timeout=1800)
        first = e.execute_effect(runtime, request, None)
        ref = c.as_object(c.as_object(first["result"])["artifact"])
        deadline = time.monotonic() + 2
        while not target.exists() and time.monotonic() < deadline:
            time.sleep(0.01)
        cancel_request = self.req("cancel-1", "dispatch.cancel", {"attempt": ref, "reason": "bounded fixture cancellation"})
        cancelled = e.execute_effect(runtime, cancel_request, None)
        self.assertEqual(e.execute_effect(runtime, cancel_request, None), cancelled)
        value = self.finished(runtime, ref)
        kinds = [c.as_object(event)["kind"] for event in c.as_list(value["events"])]
        self.assertEqual(kinds.count("cancel_requested"), 1)
        self.assertIn("signal_delivery", kinds)
        self.assertEqual(target.read_text(), "partial-effect")
        self.assertEqual(value["consumer_receipt"], "unknown")

    def test_lost_supervisor_spawn_ack_never_relaunches(self) -> None:
        runtime, request, target = self.actor_setup("count")
        def fail(point: str) -> None:
            if point == "supervisor:after_spawn":
                raise OSError("lost supervisor acknowledgment")
        with patch.object(e, "_fault", fail):
            first = e.execute_effect(runtime, request, None)
        ref = c.as_object(c.as_object(first["result"])["artifact"])
        value = self.finished(runtime, ref)
        self.assertIn("supervisor_launch_uncertain", [c.as_object(event)["kind"] for event in c.as_list(value["events"])])
        self.assertEqual(e.execute_effect(runtime, request, None), first)
        self.assertEqual(target.read_text(), "1")

    def test_lost_actor_spawn_ack_preserves_effect_and_reentry_does_not_repeat(self) -> None:
        runtime, request, target = self.actor_setup("count")
        def stop_supervisor(point: str) -> None:
            if point == "supervisor:before_spawn":
                raise OSError("retain reservation without launching supervisor")
        with patch.object(e, "_fault", stop_supervisor):
            first = e.execute_effect(runtime, request, None)
        ref = c.as_object(c.as_object(first["result"])["artifact"])
        def lose_actor_ack(point: str) -> None:
            if point == "actor:after_spawn":
                raise OSError("lost actor spawn acknowledgment")
        with patch.object(e, "_fault", lose_actor_ack):
            self.assertEqual(e.supervise(runtime, ref), 1)
        deadline = time.monotonic() + 2
        while not target.exists() and time.monotonic() < deadline:
            time.sleep(0.01)
        self.assertEqual(target.read_text(), "1")
        self.assertEqual(e.supervise(runtime, ref), 0)
        self.assertEqual(target.read_text(), "1")
        observed = e.execute_effect(runtime, self.req("observe-lost-actor", "dispatch.observe", {"attempt": ref, "after_event": 0}), None)
        value = c.as_object(c.as_object(observed["result"])["value"])
        self.assertIsNone(value["process_end"])
        self.assertEqual(c.as_object(value["effect"])["value"], "completion_unknown")

    def test_reservation_alias_publication_failure_never_launches(self) -> None:
        runtime, request, target = self.actor_setup("count")
        def fail(point: str) -> None:
            if point == "attempt_reservation:after_publish":
                raise OSError("lost reservation publication acknowledgment")
        with patch.object(e, "_fault", fail):
            first = e.execute_effect(runtime, request, None)
        self.assertEqual(c.as_object(first["operation_outcome"])["value"], "held(observation)")
        self.assertFalse(target.exists())
        replay = e.execute_effect(runtime, request, None)
        self.assertIsNotNone(replay["result"])
        self.assertFalse(target.exists())

    def test_sink_failure_and_bounded_fallback_remain_visible(self) -> None:
        runtime, request, target = self.actor_setup("count")
        def fail(point: str) -> None:
            if point == "sink:before_publish":
                raise OSError("sink unavailable")
        # The reservation delivery fails locally before supervisor spawn. Later
        # process events may deliver normally; neither implies consumer receipt.
        with patch.object(e, "_fault", fail):
            first = e.execute_effect(runtime, request, None)
        ref = c.as_object(c.as_object(first["result"])["artifact"])
        value = self.finished(runtime, ref)
        self.assertIn("notification_failure", [c.as_object(event)["kind"] for event in c.as_list(value["events"])])
        waiting = self.req("bounded-fallback", "events.wait", {"attempt": ref, "after_event": value["cursor"], "timeout_ms": 30, "cadence_ms": 20, "purpose": "selected notification fallback", "stop_condition": "return at deadline"})
        waited = e.execute_effect(runtime, waiting, None)
        observed = c.as_object(c.as_object(waited["result"])["value"])
        self.assertIn("fallback", observed)
        self.assertEqual(observed["consumer_receipt"], "unknown")
        self.assertEqual(target.read_text(), "1")

    def test_mismatched_registered_sink_consumer_refuses_before_reservation(self) -> None:
        c.as_object(c.as_object(self.policy["event_sinks"])["fixture-sink"])["consumer"] = "wrong-consumer"
        runtime, request, target = self.actor_setup("count")
        result = e.execute_effect(runtime, request, None)
        self.assertEqual(c.as_object(result["refusal"])["code"], "contract_violation")
        self.assertFalse(target.exists())
        self.assertEqual(c.as_list(self.store.query_artifacts("attempt", {})["refs"]), [])

    def test_descendant_pipe_tail_does_not_establish_external_end(self) -> None:
        runtime, request, _ = self.actor_setup("descendant")
        first = e.execute_effect(runtime, request, None)
        ref = c.as_object(c.as_object(first["result"])["artifact"])
        value = self.finished(runtime, ref)
        self.assertEqual(c.as_object(value["process_end"])["descendants"], "unknown")
        self.assertFalse(c.as_object(value["effect"])["end_established"])

    def test_declared_file_postimage_is_observed_without_semantic_completion(self) -> None:
        runtime, request, target = self.actor_setup("count", file_observer=True)
        first = e.execute_effect(runtime, request, None)
        ref = c.as_object(c.as_object(first["result"])["artifact"])
        value = self.finished(runtime, ref)
        observed = next(c.as_object(c.as_object(event)["data"]) for event in c.as_list(value["events"]) if c.as_object(event)["kind"] == "file_postimages_observed")
        self.assertEqual(c.as_object(c.as_list(observed["checks"])[0])["core_value"], "satisfied")
        self.assertEqual(target.read_text(), "1")
        self.assertEqual(c.as_object(value["effect"])["value"], "completion_unknown")

    def test_lower_layer_selected_reconciliation_allows_one_explicit_retry(self) -> None:
        # Synthetic receipt control only. PublicRetryTests exercises the actual
        # context/preflight/check/dispatch composition without this shortcut.
        runtime, request, target = self.actor_setup("count")
        first = e.execute_effect(runtime, request, None)
        predecessor = c.as_object(c.as_object(first["result"])["artifact"])
        first_observation = self.finished(runtime, predecessor)
        self.assertEqual(target.read_text(), "1")
        basis: c.Object = {"method_profile": {"id": c.PROFILE_ID, "sha256": c.PROFILE_SHA256}, "observations": []}
        (self.source / "work" / "reconcile.json").write_text('{"safe":true}')
        definition: c.Object = {"id": "fixture-reconciliation", "source": self.source_ref("authority.txt"), "subject": predecessor, "basis": basis, "input_names": ["state"], "expression": {"op": "equals", "args": [{"input": "state", "pointer": "/safe"}, {"literal": True}]}, "limits": ["Fixture's supplied safe-repetition predicate; original effect end is unchanged."]}
        c.as_object(self.policy["predicates"])["fixture-reconciliation"] = definition
        c.as_object(c.as_object(c.as_object(self.policy["grants"])["fixture-grant"])["admission"])["required_reconciliation_predicates"] = ["fixture-reconciliation"]
        self.runtime = self.runtime_for("executive")
        self.store = e.EvidenceStore(self.runtime)
        runtime = self.runtime.with_callbacks(self.store.resolve, self.store.query_artifacts)
        self.runtime = runtime
        check_request = self.req("actual-reconciliation-check", "checks.evaluate", {"predicate_id": "fixture-reconciliation", "inputs": {"state": self.source_ref("work/reconcile.json")}, "subject": predecessor, "basis": basis})
        proof = e.persist_outcome(runtime, check_request, c.execute_read(runtime, check_request))
        self.assertEqual(proof["status"], "ok")
        old_receipt = c.as_object(c.load_artifact(runtime, c.as_object(c.as_object(request["arguments"])["preflight"]), "preflight")["payload"])
        receipt = copy.deepcopy(old_receipt)
        receipt["recheck"] = self.recheck()
        envelope, ref = self.artifact("preflight", receipt, self.req("new-fixture-receipt", "contract.preflight", {}))
        self.store.retain(envelope)
        retry = self.req("explicit-retry", "dispatch.start", {"preflight": ref, "retry_of": predecessor, "reconciliation": proof["evidence"]})
        retried = e.execute_effect(runtime, retry, None)
        self.assertIsNone(retried["refusal"])
        second = c.as_object(c.as_object(retried["result"])["artifact"])
        self.finished(runtime, second)
        self.assertEqual(target.read_text(), "2")
        self.assertEqual(e.execute_effect(runtime, retry, None), retried)
        self.assertEqual(target.read_text(), "2")
        self.assertEqual(c.as_object(first_observation["effect"])["value"], "completion_unknown")


class PublicRetryTests(unittest.TestCase):
    """CLI composition controls, using real receipts and a local process only."""

    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="ac-public-retry-")
        self.root = Path(self.temp.name).resolve()
        self.f = Fixture(self.root)
        self.sequence = 0
        self.policy_version = 0
        self.policy_path = self.root / "not-selected.json"
        self.policy_sha = ""
        self.code = Path(__file__).resolve().parents[1] / "code"
        self.python = Path(sys.executable).resolve()
        fixture = Path(__file__).resolve().parent / "support_fixtures" / "local_actor.py"
        dependency = self.f.write("inputs/actor.py", fixture.read_bytes())
        self.target = self.f.workspace / "outputs" / "counter.txt"
        executor = c.as_object(c.as_object(self.f.policy["executors"])["registered"])
        executor["argv"] = [str(self.python), str(self.f.workspace / "inputs" / "actor.py"), "count", str(self.target)]
        executor["dependencies"] = [dependency]
        executor["settings"] = {"timeout_ms": 1500, "termination_grace_ms": 100}
        self._select_policy()

    def tearDown(self) -> None:
        custody = os.environ.get("AC_SUPPORT_EFFECTS_PROOF_ROOT")
        if custody is not None:
            destination = Path(custody).resolve() / self.id().replace(".", "_")
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(self.root, destination)
            (destination / "CUSTODY.json").write_bytes(c.canonical({
                "test": self.id(), "original_root": str(self.root),
                "standing": "Actual public CLI/local process fixture evidence; no F_P usability or production retry.",
                "source_sha256": hashlib.sha256((self.code / "ac_support_core.py").read_bytes()).hexdigest(),
            }))
        self.temp.cleanup()

    def _select_policy(self) -> None:
        self.policy_version += 1
        self.policy_path = self.root / ("policy-" + str(self.policy_version) + ".json")
        raw = c.canonical(self.f.policy)
        self.policy_path.write_bytes(raw)
        self.policy_sha = hashlib.sha256(raw).hexdigest()

    def _public(self, operation: str, arguments: c.Object) -> c.Object:
        self.sequence += 1
        folder = self.root / "calls" / (str(self.sequence).zfill(3) + "-" + operation)
        folder.mkdir(parents=True)
        request: c.Object = {"schema": c.REQUEST, "id": "public-" + str(self.sequence),
                             "operation": operation, "arguments": arguments}
        request_path = folder / "request.json"
        request_path.write_bytes(c.canonical(request))
        argv = [str(self.python), "-B", str(self.code / "ac_support.py"),
                "--policy", str(self.policy_path), "--policy-sha256", self.policy_sha,
                "--principal", "executive", "call", "--request", str(request_path)]
        started = time.time_ns()
        process = subprocess.run(argv, cwd=self.root, capture_output=True, timeout=10,
                                 env={"PATH": os.defpath, "PYTHONDONTWRITEBYTECODE": "1"}, check=False)
        (folder / "stdout.bin").write_bytes(process.stdout)
        (folder / "stderr.bin").write_bytes(process.stderr)
        (folder / "execution.json").write_bytes(c.canonical(c.document({
            "argv": argv, "started_ns": started, "ended_ns": time.time_ns(),
            "returncode": process.returncode, "policy_sha256": self.policy_sha,
        })))
        response = c.as_object(c.parse_json(process.stdout))
        self.assertIsNotNone(response["evidence"], response)
        return response

    def _ok(self, response: c.Object) -> c.Object:
        self.assertEqual(response["status"], "ok", response.get("refusal"))
        return c.as_object(c.as_object(response["result"])["value"])

    def _admit(self, context: c.Object) -> c.Object:
        response = self._public("contract.preflight", {
            "context": context, "grant_id": "work", "executor_id": "registered",
            "result_key": "public-counter", "observations": [],
        })
        self._ok(response)
        ref = c.as_object(c.as_object(response["result"])["artifact"])
        return ref

    def _finished(self, attempt: c.Object) -> c.Object:
        deadline = time.monotonic() + 5
        while time.monotonic() < deadline:
            response = self._public("dispatch.observe", {"attempt": attempt, "after_event": 0})
            value = self._ok(response)
            if value["process_end"] is not None and any(c.as_object(event)["kind"] == "effect_observation" for event in c.as_list(value["events"])):
                return response
            time.sleep(0.05)
        self.fail("Public registered fixture did not finish within its bounded deadline")

    def _retry_case(self, variant: str) -> None:
        core_sha = hashlib.sha256((self.code / "ac_support_core.py").read_bytes()).hexdigest()
        assembled = self._public("context.assemble", {
            "packet": self.f.packet(), "models": [], "sources": [self.f.law],
            "late_acquisition": [], "envelope": {"capacity_bytes": None,
                "boundary": "executor-stdin-utf8", "host_context": {
                    "state": "unknown", "bytes": None, "evidence": None}},
        })
        self._ok(assembled)
        context = c.as_object(c.as_object(assembled["result"])["artifact"])
        first = self._public("dispatch.start", {"preflight": self._admit(context)})
        self._ok(first)
        predecessor = c.as_object(c.as_object(first["result"])["artifact"])
        observed = self._finished(predecessor)
        self.assertEqual(self.target.read_text(), "1")
        self.assertEqual(c.as_object(self._ok(observed)["effect"])["value"], "completion_unknown")
        source = self.f.write("inputs/reconciliation-contract.json", {
            "meaning": "The exact registered local counter fixture process has an observed successful end; owner-selected explicit repetition may increment it once. No all-effects/descendant end or semantic acceptance is claimed.",
            "proof": "Actual protected dispatch.observe OperationEvidence on the predecessor; no asserted safe Boolean substitutes.",
        })
        prefix = "/payload/response_without_evidence/result/value/"
        expression: c.Object = {"op": "all", "args": [
            {"op": "equals", "args": [{"input": "observed", "pointer": prefix + "attempt"}, {"literal": predecessor}]},
            {"op": "equals", "args": [{"input": "observed", "pointer": prefix + "process_end/observed"}, {"literal": True}]},
            {"op": "equals", "args": [{"input": "observed", "pointer": prefix + "process_end/returncode"}, {"literal": 17 if variant == "false" else 0}]},
        ]}
        definition: c.Object = {"id": "predecessor-observed", "source": source,
            "subject": predecessor, "basis": self.f.basis, "input_names": ["observed"],
            "expression": expression, "limits": ["Actual fixture-process end only; prior generic effect remains unknown."]}
        definitions = c.as_object(self.f.policy["predicates"])
        definitions["predecessor-observed"] = definition
        admission = c.as_object(c.as_object(c.as_object(self.f.policy["grants"])["work"])["admission"])
        if variant == "admission-only":
            admission_definition = copy.deepcopy(definition)
            admission_definition["id"] = "task-admission"
            admission_definition["subject"] = self.f.subject
            admission_definition["input_names"] = ["context"]
            admission_definition["expression"] = {"op": "equals", "args": [
                {"input": "context", "pointer": "/packet/subject_basis/subject"}, {"literal": self.f.subject}]}
            definitions["task-admission"] = admission_definition
            admission["required_predicates"] = ["task-admission"]
        else:
            admission["required_reconciliation_predicates"] = [] if variant == "empty" else ["predecessor-observed"]
        if variant.startswith("mixed-"):
            wrong = copy.deepcopy(definition)
            wrong["id"] = "wrong-selected"
            if variant == "mixed-subject":
                wrong["subject"] = self.f.subject
            elif variant == "mixed-basis":
                wrong["basis"] = {"method_profile": self.f.basis["method_profile"], "observations": [observed["evidence"]]}
            if variant != "mixed-unknown":
                definitions["wrong-selected"] = wrong
            admission["required_reconciliation_predicates"] = ["predecessor-observed", "wrong-selected"]
        self._select_policy()
        check_basis = self.f.basis
        if variant == "invalid-basis":
            extra = self._public("workspace.observe", {"scope": [{"root": "workspace", "path": "Product.json", "kind": "file"}]})
            self._ok(extra)
            check_basis = {"method_profile": self.f.basis["method_profile"],
                           "observations": [c.as_object(extra["result"])["artifact"]]}
        proof = observed
        if variant != "missing":
            proof = self._public("checks.evaluate", {
                "predicate_id": "predecessor-observed", "inputs": {"observed": observed["evidence"]},
                "subject": predecessor, "basis": check_basis,
            })
            judgment = c.as_object(self._ok(proof)["judgment"])
            expected = "falsified" if variant == "false" else "invalid_basis" if variant == "invalid-basis" else "satisfied"
            self.assertEqual(judgment["core_value"], expected)
        receipt = self._admit(context)
        retried = self._public("dispatch.start", {"preflight": receipt,
            "retry_of": context if variant == "wrong-predecessor" else predecessor,
            "reconciliation": proof["evidence"]})
        if variant == "positive":
            self._ok(retried)
            self._finished(c.as_object(c.as_object(retried["result"])["artifact"]))
            self.assertEqual(self.target.read_text(), "2")
        else:
            self.assertEqual(c.as_object(retried["refusal"])["code"], "effect_unreconciled", retried)
            self.assertEqual(self.target.read_text(), "1")
        self.assertEqual(hashlib.sha256((self.code / "ac_support_core.py").read_bytes()).hexdigest(), core_sha)

    def test_public_selected_retry(self) -> None:
        self._retry_case("positive")

    def test_public_retry_requires_actual_check(self) -> None:
        self._retry_case("missing")

    def test_public_retry_refuses_false_check(self) -> None:
        self._retry_case("false")

    def test_public_retry_refuses_invalid_check_basis(self) -> None:
        self._retry_case("invalid-basis")

    def test_public_retry_refuses_wrong_predecessor(self) -> None:
        self._retry_case("wrong-predecessor")

    def test_public_retry_absent_selection_stays_held(self) -> None:
        self._retry_case("admission-only")

    def test_public_retry_empty_selection_stays_held(self) -> None:
        self._retry_case("empty")

    def test_public_retry_checks_every_selected_subject(self) -> None:
        self._retry_case("mixed-subject")

    def test_public_retry_checks_every_selected_basis(self) -> None:
        self._retry_case("mixed-basis")

    def test_public_retry_checks_every_selected_registered_id(self) -> None:
        self._retry_case("mixed-unknown")


if __name__ == "__main__":
    unittest.main()

"""Public mediated-composition paths; controlled actors, not LLM qualification."""
from __future__ import annotations

import copy
import base64
import contextlib
import io
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time
import unittest
from unittest.mock import patch

import test_ac_support_native301 as native
import test_ac_support_effects as legacy
import ac_support_core as c
import ac_support_composition as composition
import ac_support


class CompositionPublicTests(unittest.TestCase):
    _select_policy = legacy.PublicRetryTests._select_policy
    _ok = legacy.PublicRetryTests._ok
    _assemble = legacy.PublicRetryTests._assemble
    _admit = legacy.PublicRetryTests._admit
    tearDown = legacy.PublicRetryTests.tearDown

    def setUp(self):
        native.Native301PublicTests.setUp(self)
        self.hidden = self.f.write("inputs/hidden.txt", b"DONOR-PRIVATE-ALGORITHM")
        self.summary = self.f.write("inputs/summary.txt", b"A restatement of the donor algorithm")
        self.resource_refs = {
            "law": self.f.law, "definition": self.f.definition, "owner": self.f.owner,
            "return": self.f.return_contract, "profile": self.f.policy["method_profile"]["source"],
            "mechanism": self.f.mechanism["source"], "data": self.f.data,
            "model": self.f.model_source, "hidden": self.hidden, "summary": self.summary,
        }
        self.declaration = {
            "schema": composition.SCHEMA, "id": "test-composition",
            "authority_sources": [self.f.owner], "edges": {},
            "resources": {name: {"source": ref, "owner": "urn:test:product", "complete": True,
                                  "parents": ["hidden"] if name == "summary" else []}
                          for name, ref in self.resource_refs.items()},
            "bindings": {},
        }
        for name in ("executive", "worker", "reviewer"):
            self.declaration["bindings"][name] = {
                "engagement": "composition-case", "purpose": name + "-task", "route": [],
                "operations": sorted(composition.SUPPORTED), "allow": list(self.resource_refs),
                "exclude": ["hidden"] if name == "worker" else [], "exports": [],
                "require_complete": True, "clean_room": name == "worker", "host_isolation": False,
                "output": {"complete": True, "sources": []},
            }
        self.select()

    def select(self):
        ref = self.f.write("inputs/composition.json", self.declaration)
        self.f.policy["composition"] = ref
        self._select_policy()

    def _public(self, operation, arguments, *, principal="executive", **unused):
        self.sequence += 1
        folder = self.root / "calls" / (str(self.sequence).zfill(3) + "-" + operation)
        folder.mkdir(parents=True)
        request = {"schema": c.REQUEST, "id": "composition-" + str(self.sequence), "operation": operation, "arguments": arguments}
        (folder / "request.json").write_bytes(c.canonical(request))
        argv = [str(self.python), "-B", str(self.code / "ac_support.py"), "--policy", str(self.policy_path),
                "--policy-sha256", self.policy_sha, "--principal", principal, "call", "--request", str(folder / "request.json")]
        run = subprocess.run(argv, cwd=self.root, capture_output=True, timeout=15,
                             env={"PATH": os.defpath, "PYTHONDONTWRITEBYTECODE": "1"})
        (folder / "stdout.bin").write_bytes(run.stdout); (folder / "stderr.bin").write_bytes(run.stderr)
        (folder / "execution.json").write_text(json.dumps({"argv": argv, "exit": run.returncode}))
        self.assertTrue(run.stdout, run.stderr)
        return json.loads(run.stdout)

    def read(self, ref, principal="worker"):
        return self._public("source.read", {"source": ref, "encoding": "utf8"}, principal=principal)

    def assertRefused(self, response, code=None):
        self.assertNotEqual(response["status"], "ok", response)
        if code:
            self.assertEqual(response["refusal"]["code"], code, response)

    def test_direct_read_inspection_and_native_boundary(self):
        result = self._ok(self._public("composition.inspect", {}, principal="worker"))
        self.assertTrue(result["selected"])
        self.assertNotIn("resources", result)
        self.assertEqual(self._ok(self.read(self.f.law))["content"], "one\ntwo\nthree\n")
        self.assertRefused(self.read(self.hidden), "acquisition_denied")
        self.assertRefused(self._public("results.conjoin", {"operator_id": "x", "plan": self.f.law, "returns": [], "current_observations": []}), "unsupported_check")

    def test_prohibited_derivation_and_explicit_eligible_export(self):
        self.assertRefused(self.read(self.summary), "acquisition_denied")
        binding = self.declaration["bindings"]["worker"]
        binding["exports"] = [{"resource": "summary", "authority": self.f.owner, "eligible": False}]
        self.select(); self.assertRefused(self.read(self.summary), "acquisition_denied")
        binding["exports"][0]["eligible"] = True
        self.select(); self.assertIn("restatement", self._ok(self.read(self.summary))["content"])
        self.assertRefused(self.read(self.hidden), "acquisition_denied")

    def test_unknown_and_cyclic_provenance_fail_closed(self):
        self.declaration["resources"]["data"]["complete"] = False
        self.select(); self.assertRefused(self.read(self.f.data), "basis_missing")
        self.declaration["resources"]["hidden"]["parents"] = ["summary"]
        self.select(); self.assertRefused(self._public("composition.inspect", {}), "basis_ambiguous")

    def test_missing_provenance_and_population_bound_refuse(self):
        self.declaration["resources"]["data"]["parents"] = ["missing-origin"]
        self.select(); self.assertRefused(self.read(self.f.data), "basis_missing")
        self.declaration["resources"]["data"]["parents"] = []
        self.f.policy["limits"]["max_files"] = 5
        self.select(); self.assertRefused(self._public("composition.inspect", {}), "budget_exceeded")

    def test_target_and_requester_authored_text_are_both_checked(self):
        packet = self.f.packet(); packet["attention"]["semantic_sources"].append(self.hidden)
        response = self._public("context.assemble", {"packet": packet, "models": [], "sources": [], "late_acquisition": [], "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8", "host_context": {"state": "unknown", "bytes": None, "evidence": None}}})
        self.assertRefused(response, "acquisition_denied")
        self._ok(self.read(self.hidden, "executive"))
        # The caller could paraphrase H into a string without a SourceRef. Its
        # retained exposure still taints the authored Context for this Worker.
        packet = self.f.packet(); packet["attention"]["prohibited_assumptions"] = ["a donor-derived restatement"]
        response = self._public("context.assemble", {"packet": packet, "models": [], "sources": [], "late_acquisition": [], "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8", "host_context": {"state": "unknown", "bytes": None, "evidence": None}}})
        self.assertRefused(response, "acquisition_denied")
        self.assertIn("DONOR-PRIVATE", self._ok(self.read(self.hidden, "reviewer"))["content"])

    def test_ordinary_context_retains_unknown_provenance_and_strict_scope_holds(self):
        for binding in self.declaration["bindings"].values():
            binding.update({"require_complete": False, "clean_room": False, "exclude": []})
            binding["output"]["complete"] = False
        self.select()
        context = self._assemble()
        retained = json.loads((self.f.evidence / "objects" / (context["sha256"] + ".json")).read_text())["payload"]
        self.assertFalse(retained["boundaries"]["declared_input_provenance_complete"])
        self.assertIn('"declared_input_provenance_complete":false', retained["rendered_utf8"])
        self.assertTrue(any(item.get("unknown") is True for item in retained["composition"]["input_sources"]))
        for strict in ({"require_complete": True}, {"clean_room": True}, {"exclude": ["hidden"]}):
            with self.subTest(strict=strict):
                target = self.declaration["bindings"]["worker"]
                target.update({"require_complete": False, "clean_room": False, "exclude": []})
                target.update(strict); self.select()
                response = self._public("context.assemble", {"packet": self.f.packet(), "models": [], "sources": [], "late_acquisition": [], "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8", "host_context": {"state": "unknown", "bytes": None, "evidence": None}}})
                self.assertRefused(response, "basis_missing")
        target.update({"require_complete": False, "clean_room": False, "exclude": []})
        target["allow"].remove("law"); self.select()
        self.assertRefused(self.read(self.f.law), "acquisition_denied")

    def test_revocation_survives_principal_and_engagement_relabel(self):
        self.declaration["bindings"]["worker"]["exclude"] = []
        self.select(); self._ok(self.read(self.hidden))
        old = self.declaration["bindings"].pop("worker")
        old["exclude"] = ["hidden"]; old["engagement"] = "renamed-not-fresh"
        self.declaration["bindings"]["renamed"] = old
        actor = self.f.policy["principals"].pop("worker")
        self.f.policy["principals"]["renamed"] = actor  # stable actor_id=worker
        self.select()
        self.assertRefused(self.read(self.f.law, "renamed"), "basis_stale")
        self.f.policy["principals"]["renamed"]["actor_id"] = "actually-fresh-fixture-actor"
        self._select_policy()
        self._ok(self.read(self.f.law, "renamed"))

    def test_unknown_prior_provenance_is_not_retroactively_complete(self):
        selected = self.f.policy.pop("composition")
        self._select_policy(); self._ok(self.read(self.f.law))
        self.f.policy["composition"] = selected; self._select_policy()
        self.assertRefused(self.read(self.f.law), "basis_stale")

    def test_missing_transport_receipt_does_not_erase_possible_exposure(self):
        self.declaration["bindings"]["worker"]["exclude"] = []
        self.select()
        runtime = ac_support._load_runtime(self.policy_path, self.policy_sha, "worker")
        response = ac_support.execute(runtime, {"schema": c.REQUEST, "id": "receipt-not-observed",
            "operation": "source.read", "arguments": {"source": self.hidden, "encoding": "utf8"}})
        self._ok(response)  # prepared response, deliberately no transport publication
        self.declaration["bindings"]["worker"]["exclude"] = ["hidden"]
        self.select(); self.assertRefused(self.read(self.f.law), "basis_stale")

    def test_dirty_source_and_selector_widening(self):
        selected = copy.deepcopy(self.f.law); selected["selector"] = {"lines": [1, 1]}
        self.declaration["resources"]["law"]["source"] = selected
        self.select(); self._ok(self.read(selected))
        self.assertRefused(self.read(self.f.law), "acquisition_denied")
        (self.f.workspace / "inputs/law.txt").write_text("different uncommitted bytes\n")
        self.assertRefused(self.read(selected), "digest_mismatch")

    def test_unrelated_unacquired_change_does_not_reset_scope(self):
        (self.f.workspace / "inputs/data.json").write_text('{"unrelated":true}')
        self._ok(self.read(self.f.law))

    def test_isolation_and_unknown_retained_carriers_refuse(self):
        self.declaration["bindings"]["worker"]["host_isolation"] = True
        self.select(); self.assertRefused(self.read(self.f.law), "unsupported_contract")
        self.declaration["bindings"]["worker"]["host_isolation"] = False
        self.select()
        source = self.read(self.f.law)
        self.assertRefused(self._public("evidence.read", {"artifact": source["evidence"]}, principal="worker"), "unsupported_contract")

    def _route(self):
        relation = self.f.write("inputs/relation.md", b"# Support\nA selected finite relation.\n")
        provider = self.f.write("inputs/Provider.json", {"product": {"definition_id": "urn:test:provider"}, "composition": []})
        definition = json.loads((self.f.workspace / "Product.json").read_text())
        definition["product"] = {"definition_id": "urn:test:product"}
        definition["composition"] = [{"product_definition": "inputs/Provider.json", "target_definition_id": "urn:test:provider", "relation": "inputs/relation.md#support", "contracts": ["inputs/data.json"]}]
        self.f.definition = self.f.write("Product.json", definition)
        self.f.policy["product"]["definition"] = self.f.definition
        self.declaration["resources"]["definition"]["source"] = self.f.definition
        edge = {"source_definition": self.f.definition, "source_id": "urn:test:product", "index": 0,
                "target_definition": provider, "target_id": "urn:test:provider", "relation": relation,
                "contracts": [self.f.data]}
        self.declaration["edges"]["A-D"] = edge
        self.declaration["resources"]["data"]["owner"] = "urn:test:provider"

    def test_selected_route_is_not_transitive_permission(self):
        self._route()
        self.declaration["bindings"]["reviewer"]["route"] = ["A-D"]
        self.select()
        self.assertRefused(self.read(self.f.data), "authority_missing")
        self._ok(self.read(self.f.data, "reviewer"))
        self.declaration["bindings"]["worker"]["route"] = ["A-D"]
        self.declaration["bindings"]["worker"]["allow"].remove("data")
        self.select(); self.assertRefused(self.read(self.f.data), "acquisition_denied")

    def test_route_target_identity_and_fragment_are_rechecked(self):
        self._route(); self.declaration["bindings"]["worker"]["route"] = ["A-D"]
        self.select(); self._ok(self.read(self.f.data))
        (self.f.workspace / "inputs/relation.md").write_text("# No longer the selected relation\n")
        self.assertRefused(self.read(self.f.data), "digest_mismatch")

    def test_shared_leaf_edges_keep_separate_permissions(self):
        self._route()
        definition = json.loads((self.f.workspace / "Product.json").read_text())
        definition["composition"].append(copy.deepcopy(definition["composition"][0]))
        self.f.definition = self.f.write("Product.json", definition)
        self.f.policy["product"]["definition"] = self.f.definition
        self.declaration["resources"]["definition"]["source"] = self.f.definition
        self.declaration["edges"]["A-D"]["source_definition"] = self.f.definition
        second = copy.deepcopy(self.declaration["edges"]["A-D"]); second["index"] = 1
        self.declaration["edges"]["A-D-other"] = second
        self.declaration["bindings"]["reviewer"]["route"] = ["A-D"]
        self.declaration["bindings"]["worker"]["route"] = ["A-D-other"]
        self.declaration["bindings"]["worker"]["allow"].remove("data")
        self.select()
        self._ok(self.read(self.f.data, "reviewer"))
        self.assertRefused(self.read(self.f.data), "acquisition_denied")

    def test_route_cannot_substitute_another_version_of_same_product(self):
        self._route(); self.declaration["bindings"]["worker"]["route"] = ["A-D"]
        other = self.f.write("inputs/other-definition.json", json.loads((self.f.workspace / "Product.json").read_text()))
        self.declaration["edges"]["A-D"]["source_definition"] = other
        self.select(); self.assertRefused(self.read(self.f.data), "basis_stale")

    def test_markdown_examples_and_escapes_do_not_supply_edge_anchors(self):
        self._route(); self.declaration["bindings"]["worker"]["route"] = ["A-D"]
        for text in ('```markdown\n# Support\n<a id="support"></a>\n```\n',
                     '\\<a id="support"></a>\n',
                     '`example\n<a id="support"></a>\nexample`\n',
                     '    <a id="support"></a>\n',
                     '<!-- <a id="support"></a> -->\n'):
            with self.subTest(text=text):
                self.declaration["edges"]["A-D"]["relation"] = self.f.write("inputs/relation.md", text.encode())
                self.select(); self.assertRefused(self.read(self.f.data), "basis_missing")
        self.declaration["edges"]["A-D"]["relation"] = self.f.write("inputs/relation.md", b'<a id="support"></a>\n')
        self.select(); self._ok(self.read(self.f.data))

    def test_derived_model_cannot_bypass_source_guard(self):
        self.declaration["resources"]["model"]["parents"] = ["hidden"]
        self.select()
        identity = "urn:a-c:toy:object:a"
        args = {"model": self.f.model, "ids": [identity]}
        self.assertRefused(self._public("records.read", args, principal="worker"), "acquisition_denied")
        self._ok(self._public("records.read", args, principal="reviewer"))

    def _review_arguments(self):
        return {"phase": "expectation", "claim": self.f.law, "sources": [],
                "candidate": None, "proof": [], "comparison": None,
                "expectations": None, "expectation_body": None}

    def _independence_policy(self, authority=None):
        policy = self.f.write("inputs/private-independence.json", {
            "id": "private-independence", "authority_source": self.f.owner if authority is None else authority,
            "claim_scope": "REVIEW-DENIED-POLICY-CONTENT-7e37", "require_non_author": True,
            "allowed_family_pairs": [["A", "B"]], "source_first": True,
            "mechanical_sharing": [], "predicates": []})
        self.f.policy["independence_policy"] = policy
        self.declaration["resources"]["private-policy"] = {"source": policy,
            "owner": "urn:test:product", "complete": True, "parents": []}
        self.declaration["bindings"]["reviewer"]["allow"].append("private-policy")
        return policy

    def test_automatic_review_policy_is_guarded_and_actual_exposure_is_retained(self):
        policy = self._independence_policy()
        binding = self.declaration["bindings"]["reviewer"]
        binding["exclude"] = ["private-policy"]
        self.select()
        self.assertRefused(self.read(policy, "reviewer"), "acquisition_denied")
        response = self._public("review.prepare", self._review_arguments(), principal="reviewer")
        self.assertRefused(response, "acquisition_denied")
        self.assertNotIn("REVIEW-DENIED-POLICY-CONTENT", json.dumps(response))
        binding["exclude"] = []; self.select()
        permitted = self._ok(self._public("review.prepare", self._review_arguments(), principal="reviewer"))
        self.assertEqual(permitted["independence"]["governing_conditions"]["claim_scope"], "REVIEW-DENIED-POLICY-CONTENT-7e37")
        binding["exclude"] = ["private-policy"]; binding["clean_room"] = True
        self.select(); self.assertRefused(self.read(self.f.law, "reviewer"), "basis_stale")

    def test_automatic_review_policy_authority_does_not_expand_read_permission(self):
        self._independence_policy(self.hidden)
        self.declaration["bindings"]["reviewer"]["exclude"] = ["hidden"]
        self.select()
        response = self._public("review.prepare", self._review_arguments(), principal="reviewer")
        self.assertRefused(response, "acquisition_denied")
        self.assertNotIn("DONOR-PRIVATE", json.dumps(response))

    def test_review_history_diagnostics_stay_private_on_success(self):
        marker = "PRIVATE-REVIEW-HISTORY-DETAIL"
        (self.f.evidence / "objects").mkdir(exist_ok=True)
        (self.f.evidence / "objects" / (".stage-" + marker)).write_text("isolated incomplete-history fixture")
        response = self._public("review.prepare", self._review_arguments(), principal="reviewer")
        value = self._ok(response)
        self.assertTrue(value["gaps"])
        self.assertNotIn(marker, json.dumps(response))
        operation = json.loads((self.f.evidence / "objects" / (response["evidence"]["sha256"] + ".json")).read_text())["payload"]
        private = [json.loads((self.f.evidence / "objects" / (ref["sha256"] + ".json")).read_text()) for ref in operation["artifacts"]]
        self.assertTrue(any(item["payload"].get("schema") == "a_c.fd-support.composition-diagnostic/1" and marker in json.dumps(item) for item in private))

    def test_unretained_failure_and_transport_stderr_have_safe_projections(self):
        marker = "PRIVATE-FAILURE-DETAIL"
        encoded = base64.b64encode(marker.encode()).decode()
        runtime = ac_support._load_runtime(self.policy_path, self.policy_sha, "executive")
        request = {"schema": c.REQUEST, "id": "fault-boundary-probe", "operation": "source.read",
                   "arguments": {"source": self.f.law, "encoding": "utf8"}}
        error = c.SupportError("evidence_publication_failed", marker, [{"nested": {"bytes_base64": encoded}}], [self.hidden])
        with patch.object(ac_support.effects, "persist_outcome", side_effect=error):
            response = ac_support.execute(runtime, request)
        self.assertIsNone(response["evidence"])
        self.assertNotIn(marker, json.dumps(response)); self.assertNotIn(encoded, json.dumps(response))
        self.assertEqual(response["refusal"]["gaps"][0]["private_retention"], "not established")
        response = ac_support.execute(runtime, request)
        self._ok(response)
        target = io.BytesIO(); diagnostics = io.StringIO()
        with patch.object(ac_support.effects.EvidenceStore, "retain", side_effect=RuntimeError(encoded)), contextlib.redirect_stderr(diagnostics):
            ac_support._deliver(runtime, request, response, target)
        self.assertIn("delivery evidence remains unknown", diagnostics.getvalue())
        self.assertNotIn(encoded, diagnostics.getvalue())
        # The optional composition projection does not silently change the
        # pre-existing operator diagnostic contract when no binding is selected.
        self.f.policy.pop("composition"); self._select_policy()
        unbound = ac_support._load_runtime(self.policy_path, self.policy_sha, "executive")
        with patch.object(ac_support.effects, "persist_outcome", side_effect=error):
            legacy_response = ac_support.execute(unbound, request)
        self.assertIn(encoded, json.dumps(legacy_response))

    def _finished(self, attempt, timeout=8):
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            response = self._public("dispatch.observe", {"attempt": attempt, "after_event": 0})
            value = self._ok(response)
            if value["process_end"] is not None:
                return response
            time.sleep(0.03)
        self.fail("controlled actor did not finish")

    def test_public_context_dispatch_output_and_redacted_control(self):
        # Run the existing full authenticated native return fixture through the
        # composition guard and actual subprocess/parent completion path.
        native.Native301PublicTests.test_actual_process_completion_capture_and_return_check(self)

    def test_unknown_provenance_survives_dispatch_return_and_stricter_reentry(self):
        for binding in self.declaration["bindings"].values():
            binding.update({"require_complete": False, "clean_room": False, "exclude": []})
            binding["output"]["complete"] = False
        self.select()
        native.Native301PublicTests.test_actual_process_completion_capture_and_return_check(self)
        # Both actor-delivered Context and parent-acquired return retain the
        # unresolved ancestry when the owner later selects clean-room standing.
        self.declaration["bindings"]["worker"]["clean_room"] = True
        self.declaration["bindings"]["executive"]["clean_room"] = True
        self.select()
        self.assertRefused(self.read(self.f.law), "basis_stale")
        self.assertRefused(self.read(self.f.law, "executive"), "basis_stale")

    def test_revoked_output_still_allows_redacted_observation_and_cancel(self):
        actor = self.f.write("inputs/revocable_actor.py", b'import sys,time\nfrom pathlib import Path\nsys.stdin.buffer.read()\nPath(sys.argv[1]).write_text("launched")\nprint("DONOR-PRIVATE-ALGORITHM",flush=True)\ntime.sleep(30)\n')
        executor = self.f.policy["executors"]["registered"]
        executor["argv"] = [str(self.python), "-B", str(self.f.workspace / "inputs/revocable_actor.py"), str(self.target)]
        executor["dependencies"] = [actor]
        self.f.policy["grants"]["work"]["operations"].append("dispatch.cancel")
        self.declaration["bindings"]["worker"]["exclude"] = []
        self.declaration["bindings"]["worker"]["output"]["sources"] = ["hidden"]
        self.select()
        context = self._assemble()
        started = self._ok(self._public("dispatch.start", {"preflight": self._admit(context)}))
        attempt = started["attempt"]
        deadline = time.monotonic() + 3
        while not self.target.exists() and time.monotonic() < deadline:
            time.sleep(.02)
        self.assertTrue(self.target.exists())
        self.declaration["bindings"]["executive"]["exclude"] = ["hidden"]
        self.declaration["bindings"]["executive"]["operations"] = []
        self.select()
        observed = self._ok(self._public("dispatch.observe", {"attempt": attempt, "after_event": 0}))
        self.assertNotIn("DONOR-PRIVATE", json.dumps(observed))
        self.assertNotIn("anchor", observed); self.assertNotIn("events", observed)
        self._ok(self._public("dispatch.cancel", {"attempt": attempt, "reason": "bounded test cancellation"}))
        ended = self._ok(self._finished(attempt))
        self.assertIsNotNone(ended["process_end"])
        self.declaration["bindings"]["executive"]["operations"] = sorted(composition.SUPPORTED)
        self.select()
        self.assertRefused(self._public("evidence.read", {"artifact": ended["output"]["stdout"]}), "acquisition_denied")

    def test_stale_material_prevents_dispatch_before_effect(self):
        context = self._assemble(); receipt = self._admit(context)
        (self.f.workspace / "inputs/law.txt").write_text("advanced dirty deciding input\n")
        response = self._public("dispatch.start", {"preflight": receipt})
        self.assertRefused(response)
        self.assertFalse(self.target.exists())

    def test_control_refusal_redacts_private_events_and_retains_private_diagnostic(self):
        marker = "CONTROL-DENIED-OUTPUT-9492"
        actor = self.f.write("inputs/control_actor.py", b'import sys\nsys.stdin.buffer.read()\nprint("CONTROL-DENIED-OUTPUT-9492",flush=True)\n')
        executor = self.f.policy["executors"]["registered"]
        executor["argv"] = [str(self.python), "-B", str(self.f.workspace / "inputs/control_actor.py")]
        executor["dependencies"] = [actor]
        self.f.policy["grants"]["work"]["operations"].append("dispatch.cancel")
        self.declaration["bindings"]["worker"]["exclude"] = []
        self.declaration["bindings"]["worker"]["output"]["sources"] = ["hidden"]
        self.select()
        context = self._assemble()
        attempt = self._ok(self._public("dispatch.start", {"preflight": self._admit(context)}))["attempt"]
        ended = self._ok(self._finished(attempt))
        self.assertEqual(ended["process_end"]["returncode"], 0)
        self.assertTrue(ended["history_complete"])
        allowed = self._ok(self._public("evidence.read", {"artifact": ended["output"]["stdout"]}))
        self.assertIn(marker, base64.b64decode(allowed["envelope"]["payload"]["bytes_base64"]).decode())
        # Revoke readback after completion; the former lawful exposure is not
        # claimed to vanish. Control must not disclose another copy implicitly.
        self.declaration["bindings"]["executive"]["exclude"] = ["hidden"]
        self.select()
        self.assertRefused(self._public("evidence.read", {"artifact": ended["output"]["stdout"]}), "acquisition_denied")
        removed = False
        for path in (self.f.evidence / "objects").glob("*.json"):
            item = json.loads(path.read_text()); payload = item["payload"]
            if isinstance(payload, dict) and payload.get("schema") == "a_c.fd-support.attempt-event/1" and payload.get("attempt") == attempt and payload["cursor"] == 1:
                path.unlink(); removed = True; break
        self.assertTrue(removed)
        refused = self._public("dispatch.cancel", {"attempt": attempt, "reason": "isolated incomplete-history probe"})
        self.assertRefused(refused, "history_incomplete")
        serialized = json.dumps(refused)
        self.assertNotIn(marker, serialized)
        self.assertNotIn(base64.b64encode((marker + "\n").encode()).decode(), serialized)
        self.assertEqual(refused["refusal"]["gaps"][0]["effect_state"], "completion_unknown")
        operation = json.loads((self.f.evidence / "objects" / (refused["evidence"]["sha256"] + ".json")).read_text())["payload"]
        private = []
        for ref in operation["artifacts"]:
            item = json.loads((self.f.evidence / "objects" / (ref["sha256"] + ".json")).read_text())
            if item["payload"].get("schema") == "a_c.fd-support.composition-diagnostic/1":
                private.append((ref, item))
        self.assertEqual(len(private), 1)
        self.assertIn(base64.b64encode((marker + "\n").encode()).decode(), json.dumps(private[0][1]))
        self.assertRefused(self._public("evidence.read", {"artifact": private[0][0]}))
        observed_response = self._public("dispatch.observe", {"attempt": attempt, "after_event": 0})
        self.assertNotIn(base64.b64encode((marker + "\n").encode()).decode(), json.dumps(observed_response))
        if observed_response["status"] == "ok":
            observed = self._ok(observed_response)
            self.assertFalse(observed["history_complete"])
            self.assertFalse(observed["effect"]["end_established"])
        else:
            self.assertIn(observed_response["refusal"]["code"], ("source_missing", "history_incomplete"))
            self.assertEqual(observed_response["refusal"]["gaps"][0]["effect_state"], "completion_unknown")

    def test_delivered_inline_context_retains_author_provenance(self):
        self.declaration["bindings"]["worker"]["exclude"] = []
        self.select(); self._ok(self.read(self.hidden, "executive"))
        packet = self.f.packet()
        packet["attention"]["prohibited_assumptions"] = ["authored text influenced by a donor"]
        context = self._assemble(packet)
        attempt = self._ok(self._public("dispatch.start", {"preflight": self._admit(context)}))["attempt"]
        self._ok(self._finished(attempt))
        self.declaration["bindings"]["worker"]["exclude"] = ["hidden"]
        self.select(); self.assertRefused(self.read(self.f.law), "basis_stale")

    def test_actor_issued_late_tool_read_and_output_readback(self):
        request = self.f.write("inputs/late-request.json", {"schema": c.REQUEST, "id": "actor-late-tool-read",
            "operation": "source.read", "arguments": {"source": self.f.law, "encoding": "utf8"}})
        # The fixed controlled actor computes the selected policy digest to avoid
        # a self-referential digest in its immutable argv. This is a fixture
        # mechanism, not a permission for untrusted actors to select policies.
        actor = self.f.write("inputs/late_actor.py", b'import sys,subprocess,hashlib\nfrom pathlib import Path\nsys.stdin.buffer.read()\na=sys.argv[1:]\ni=a.index("--policy")\na[i:i]=["--policy-sha256",hashlib.sha256(Path(a[i+1]).read_bytes()).hexdigest()]\nr=subprocess.run(a,capture_output=True)\nsys.stdout.buffer.write(r.stdout)\nsys.exit(r.returncode)\n')
        executor = self.f.policy["executors"]["registered"]
        # The selected policy path is known before its immutable file is written.
        policy_path = self.root / ("policy-" + str(self.policy_version + 1) + ".json")
        executor["argv"] = [str(self.python), "-B", str(self.f.workspace / "inputs/late_actor.py"), str(self.python), "-B", str(self.code / "ac_support.py"), "--policy", str(policy_path), "--principal", "worker", "call", "--request", str(self.f.workspace / "inputs/late-request.json")]
        executor["dependencies"] = [actor, request]
        self._select_policy()
        packet = self.f.packet()
        context_response = self._public("context.assemble", {"packet": packet, "models": [], "sources": [], "late_acquisition": [self.f.law], "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8", "host_context": {"state": "unknown", "bytes": None, "evidence": None}}})
        self._ok(context_response); context = context_response["result"]["artifact"]
        attempt = self._ok(self._public("dispatch.start", {"preflight": self._admit(context)}))["attempt"]
        output = self._ok(self._finished(attempt))
        self.assertEqual(output["process_end"]["returncode"], 0)
        readback = self._ok(self._public("evidence.read", {"artifact": output["output"]["stdout"]}))
        raw = readback["envelope"]["payload"]
        actual = json.loads(base64.b64decode(raw["bytes_base64"]))
        self.assertEqual(actual["result"]["value"]["content"], "one\ntwo\nthree\n")

    def test_late_read_remains_guarded_and_context_records_currentness(self):
        packet = self.f.packet()
        packet["stop_change"]["residuals"] = ["join evidence remains unresolved"]
        response = self._public("context.assemble", {"packet": packet, "models": [], "sources": [], "late_acquisition": [self.hidden], "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8", "host_context": {"state": "unknown", "bytes": None, "evidence": None}}})
        self.assertRefused(response, "acquisition_denied")
        self.assertRefused(self.read(self.hidden), "acquisition_denied")
        context = self._assemble(packet)
        retained = json.loads((self.f.evidence / "objects" / (context["sha256"] + ".json")).read_text())
        self.assertIn("join evidence remains unresolved", retained["payload"]["rendered_utf8"])
        self.assertNotIn("output_sources", retained["payload"]["rendered_utf8"])


if __name__ == "__main__":
    unittest.main()

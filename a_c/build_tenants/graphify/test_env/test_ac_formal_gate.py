"""Integration boundary controls. Fake checker cases are explicitly unit controls.

Real Lean and real public Worker delivery are exercised by qualify_formal_gate.py.
"""
from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from typing import Any
from unittest.mock import patch

from test_ac_support_core import Fixture, obj
import test_ac_generate as generation_fixtures
import ac_generate as generation
import ac_grounding as grounding
import ac_repair as repair
import ac_support_core as core
import ac_support_effects as effects

formal = core.ac_formal_gate


class FormalGateControls(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="a-c-formal-control-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.addCleanup(self.retain_control)
        self.checker = self.root / "checker"
        (self.checker / "scripts").mkdir(parents=True)
        (self.checker / "profiles").mkdir()
        self.entry = self.checker / "scripts/formal_gate.py"
        self.entry.write_text("raise RuntimeError('unit control must not execute this checker')\n")
        (self.checker / "scripts/helper.py").write_text("BOUNDARY = 'controlled'\n")
        (self.checker / "profiles/proof-support-v1.json").write_text('{"unit_control":true}')
        python = Path(sys.executable).resolve()
        self.config = {"schema": formal.CONFIG, "root": str(self.checker),
                       "python": {"path": str(python), "sha256": formal.sha(python.read_bytes())},
                       "adapter_sha256": formal.sha(Path(formal.__file__).read_bytes()),
                       "entry_sha256": formal.sha(self.entry.read_bytes()), "runtime_identity": self.identity(), "timeout_seconds": 1}

    def retain_control(self) -> None:
        selected = os.environ.get("AC_FORMAL_CONTROL_EVIDENCE")
        if selected:
            target = Path(selected) / self.id().rsplit(".", 1)[-1]
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(self.root, target)

    def identity(self) -> dict[str, Any]:
        pins = {str(p.relative_to(self.checker)): formal.sha(p.read_bytes())
                for base in ("scripts", "profiles") for p in sorted((self.checker / base).iterdir())}
        return {"pins": pins, "sha256": formal.sha(formal.canonical(pins))}

    def fixture(self, required: bool = True) -> Fixture:
        path = self.root / "fixture"; path.mkdir()
        fixture = Fixture(path)
        fixture.policy["formal_gate"] = obj({"checker": self.config, "required_targets": ["worker"] if required else []})
        return fixture

    def context(self, fixture: Fixture) -> tuple[Any, ...]:
        runtime = fixture.runtime()
        args = {"packet": fixture.packet(), "models": [{"model": fixture.model, "selections": [{"seeds": ["urn:a-c:toy:object:a"], "budget_records": 9}]}],
                "sources": [], "late_acquisition": [], "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8",
                    "host_context": {"state": "unknown", "bytes": None, "evidence": None}}}
        response, outcome = fixture.run(runtime, "context.assemble", args)
        self.assertEqual(response["status"], "ok", response)
        ref = response["result"]["artifact"]
        context = core.load_artifact(runtime, ref, "context")["payload"]
        return runtime, ref, context, outcome

    def test_changed_helper_cannot_execute_forged_old_identity(self) -> None:
        old_identity = copy.deepcopy(self.config["runtime_identity"])
        (self.checker / "scripts/helper.py").write_text("print(" + repr(json.dumps(old_identity)) + ")\n")
        with patch.object(formal.subprocess, "Popen", side_effect=AssertionError("changed helper executed")):
            with self.assertRaisesRegex(formal.GateError, "dependency changed"):
                formal.current(self.config)

    def test_selected_graphify_adapter_drift_refuses_generation_and_support_startup(self) -> None:
        stale = copy.deepcopy(self.config); stale["adapter_sha256"] = "0" * 64
        with self.assertRaisesRegex(generation.ac_formal_gate.GateError, "adapter implementation changed"):
            generation._formal_selection(self.root, {"formal_checker": None}, stale)
        fixture = self.fixture()
        fixture.policy["formal_gate"]["checker"] = stale
        with self.assertRaisesRegex(core.SupportError, "adapter implementation differs"):
            fixture.runtime()

    def test_new_shadow_module_and_changed_support_manifest_refused_before_execution(self) -> None:
        shadow = self.checker / "scripts/json.py"; shadow.write_text("raise RuntimeError('shadow')")
        with patch.object(formal.subprocess, "Popen", side_effect=AssertionError("shadow executed")):
            with self.assertRaisesRegex(formal.GateError, "population changed"):
                formal.current(self.config)
            shadow.unlink()
            (self.checker / "profiles/proof-support-v1.json").write_text('{}')
            with self.assertRaisesRegex(formal.GateError, "dependency changed"):
                formal.current(self.config)

    def test_helper_package_shadow_refused_before_currentness_or_selection_execution(self) -> None:
        marker = self.root / "package-executed"
        package = self.checker / "scripts/helper"; package.mkdir()
        (package / "__init__.py").write_text("from pathlib import Path\nPath(" + repr(str(marker)) + ").write_text('executed')\n")
        # Establish that ordinary Python resolution really chooses the added
        # package while the selected flat helper's bytes remain unchanged.
        direct = subprocess.run([str(Path(sys.executable).resolve()), "-S", "-B", "-c", "import helper"],
                                cwd=self.checker / "scripts", capture_output=True, timeout=5, check=False)
        self.assertEqual(direct.returncode, 0, direct.stderr)
        self.assertTrue(marker.exists()); marker.unlink()
        with patch.object(formal.subprocess, "Popen", side_effect=AssertionError("package executed")):
            with self.assertRaisesRegex(formal.GateError, "namespace"):
                formal.current(self.config)
            with self.assertRaisesRegex(formal.GateError, "namespace"):
                formal._invoke(self.config, ["identity"], selecting=True)
        self.assertFalse(marker.exists())

    def test_extension_sourceless_and_cache_package_shadows_refused(self) -> None:
        for name in ("helper.so", "helper.pyc", "__pycache__/__init__.py"):
            with self.subTest(name=name):
                path = self.checker / "scripts" / name; path.parent.mkdir(exist_ok=True)
                path.write_bytes(b"unselected executable placeholder")
                with patch.object(formal.subprocess, "Popen", side_effect=AssertionError("shadow executed")):
                    with self.assertRaisesRegex(formal.GateError, "namespace"):
                        formal.current(self.config)
                path.unlink()

    def test_exact_bridge_bytes_ignore_same_named_package_and_bind_loaded_source(self) -> None:
        directory = self.root / "graphify-code"; directory.mkdir()
        for source in Path(generation.__file__).parent.glob("*.py"):
            shutil.copyfile(source, directory / source.name)
        marker = self.root / "bridge-package-executed"
        package = directory / "ac_formal_gate"; package.mkdir()
        (package / "__init__.py").write_text("from pathlib import Path\nPath(" + repr(str(marker)) + ").write_text('executed')\nraise RuntimeError('unselected bridge package')\n")
        script = '''import hashlib, json
from pathlib import Path
import ac_generate as generation
import ac_support_core as core
import ac_support_effects as effects
expected = Path.cwd() / "ac_formal_gate.py"
assert effects.formal is core.ac_formal_gate
for module in (generation.ac_formal_gate, core.ac_formal_gate):
    assert Path(module.__file__) == expected
    assert module.__a_c_loaded_sha256__ == hashlib.sha256(expected.read_bytes()).hexdigest()
config = json.loads(Path("config.json").read_text())
expected.write_bytes(expected.read_bytes() + b"\\n# changed after loading\\n")
config["adapter_sha256"] = hashlib.sha256(expected.read_bytes()).hexdigest()
for module in (generation.ac_formal_gate, core.ac_formal_gate):
    try:
        module.validate_config(config)
    except module.GateError as error:
        assert error.status == "refused"
    else:
        raise AssertionError("changed bytes substituted for loaded bridge")
print("exact bridge source checked; package never imported")
'''
        (directory / "config.json").write_bytes(formal.canonical(self.config))
        result = subprocess.run([str(Path(sys.executable).resolve()), "-S", "-B", "-c", script],
                                cwd=directory, capture_output=True, timeout=10, check=False)
        (self.root / "bridge-probe-stdout").write_bytes(result.stdout)
        (self.root / "bridge-probe-stderr").write_bytes(result.stderr)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(marker.exists())

    def test_pure_core_records_required_condition_without_compiler(self) -> None:
        fixture = self.fixture()
        with patch.object(formal.subprocess, "Popen", side_effect=AssertionError("pure core launched compiler")):
            runtime, _, context, _ = self.context(fixture)
            self.assertTrue(context["formal_gate"]["required"])
            self.assertEqual(context["formal_gate"]["state"], "pending")
            self.assertEqual(context["projections"][0]["selections"][0]["budget_records"], 9)
            self.assertEqual(context["fit"]["capacity_bytes"], None)
            self.assertEqual(effects._formal_inputs(runtime, context)[1][0][0], (fixture.workspace / "inputs/model.json").read_bytes())

    def test_optional_unselected_policy_preserves_legacy_context(self) -> None:
        fixture = self.fixture(False)
        runtime, _, context, _ = self.context(fixture)
        self.assertNotIn("formal_gate", context)
        self.assertEqual(effects._formal_inputs(runtime, context), (None, []))

    def test_required_condition_cannot_be_removed(self) -> None:
        fixture = self.fixture()
        runtime, _, context, _ = self.context(fixture)
        del context["formal_gate"]
        with self.assertRaisesRegex(core.SupportError, "dropped or changed"):
            effects._formal_inputs(runtime, context)

    def test_actual_rendering_and_actual_view_population_are_bound(self) -> None:
        fixture = self.fixture()
        runtime, _, context, _ = self.context(fixture)
        altered = copy.deepcopy(context)
        altered["rendered_utf8"] += "\nchanged"
        with self.assertRaisesRegex(core.SupportError, "rendering"):
            effects._formal_inputs(runtime, altered)
        altered = copy.deepcopy(context)
        altered["projections"][0]["selections"] = []
        body = {k: altered[k] for k in ("packet", "projections", "sources", "late_acquisition", "boundaries", "formal_gate")}
        body["schema"] = "a_c.fd-support.actor-context/1"
        altered["rendered_utf8"] = core.PREFIX + core.canonical(body).decode()
        altered["rendered_sha256"] = formal.sha(altered["rendered_utf8"].encode())
        with self.assertRaisesRegex(core.SupportError, "view population"):
            effects._formal_inputs(runtime, altered)

    def test_forged_success_receipt_without_effect_evidence_refused(self) -> None:
        fixture = self.fixture()
        runtime, ref, context, _ = self.context(fixture)
        store = effects.EvidenceStore(runtime)
        receipt = obj({"context": ref, "formal_gate": {"status": "verified"}})
        with self.assertRaisesRegex(core.SupportError, "no effect-produced evidence"):
            effects._recheck_formal(runtime, store, fixture.request("dispatch.start", {}), receipt, context)

    def test_source_change_during_formal_effect_cannot_be_admitted(self) -> None:
        fixture = self.fixture()
        runtime, context_ref, _, outcome = self.context(fixture)
        store = effects.EvidenceStore(runtime)
        for envelope in outcome["artifacts"]:
            store.retain(core.document(envelope))
        runtime = runtime.with_callbacks(store.resolve, store.query_artifacts)
        request = fixture.request("contract.preflight", {"context": context_ref, "grant_id": "work", "executor_id": "registered", "result_key": "fresh-material", "observations": []})
        plan = core.build_preflight(runtime, request)
        def controlled_verifier(config: Any, raw: bytes, format: str, selections: Any, views: Any, binding: Any, output: Path) -> dict[str, Any]:
            source = fixture.workspace / "inputs/model.json"
            source.write_bytes(source.read_bytes() + b" ")
            return {"result": {"status": "verified", "model": {"id": fixture.model["model_id"], "sha256": fixture.model["model_sha256"]},
                    "selections": selections, "context_binding": binding, "runtime_identity": config["runtime_identity"]},
                    "bundle": str(output), "result_sha256": "0" * 64, "input_sha256": formal.sha(raw), "views_sha256": formal.sha(formal.canonical(views))}
        with patch.object(formal, "verify", side_effect=controlled_verifier) as invoked:
            with self.assertRaises(core.SupportError) as stopped:
                effects._preflight(runtime, store, request, plan)
        invoked.assert_called_once()
        self.assertEqual(stopped.exception.code, "basis_missing")
        self.assertEqual(store.query_artifacts("preflight", {})["refs"], [])

    def test_model_acquisition_cannot_escape_authorized_source_scope(self) -> None:
        fixture = self.fixture()
        runtime, _, context, _ = self.context(fixture)
        projection = context["projections"][0]
        projection["model"]["source"]["path"] = "../checker/scripts/formal_gate.py"
        # Bind the forged content itself, so source authority is the failing check.
        body = {k: context[k] for k in ("packet", "projections", "sources", "late_acquisition", "boundaries", "formal_gate")}
        body["schema"] = "a_c.fd-support.actor-context/1"
        context["rendered_utf8"] = core.PREFIX + core.canonical(body).decode()
        context["rendered_sha256"] = formal.sha(context["rendered_utf8"].encode())
        with self.assertRaises(core.SupportError):
            effects._formal_inputs(runtime, context)

    def test_all_three_producers_retain_unverified_proposal_and_distinct_gate_status(self) -> None:
        for status in ("refused", "unsupported", "incomplete"):
            corpus = self.root / ("source-" + status); corpus.mkdir()
            raw = generation_fixtures.SOURCE.encode(); (corpus / "rules.md").write_bytes(raw)
            manifest = self.root / ("manifest-" + status + ".json")
            generation.save(manifest, {"profile": "ac.generation.corpus/1", "subject_id": "repo://unit-control/" + status,
                "files": [{"path": "rules.md", "sha256": formal.sha(raw), "bytes": len(raw)}]})
            output = self.root / ("generation-" + status)
            plan = generation.prepare(corpus, manifest, output, "direct", None, 1000, formal_checker=self.config)
            chunks = generation.load(output / "chunks.json")
            authored = generation_fixtures.GenerationTests("test_snapshot_and_chunks_cover_exact_original_source")
            authored.output = output; authored.plan = plan; authored.chunks = chunks
            authored.fake_attempt("author", generation_fixtures.fixture_answer(chunks[0]))
            with patch.object(generation.ac_formal_gate, "verify", side_effect=generation.ac_formal_gate.GateError(status, "explicit unit control")):
                for module, folder in ((generation, "proposal"), (grounding, "grounded-proposal"), (repair, "repaired-proposal")):
                    result = module.assemble(output)
                    self.assertEqual(result["formal_gate"]["status"], status)
                    self.assertEqual(result["status"], "unverified_proposal")
                    self.assertEqual(generation.formal_exit(result), formal.EXITS[status])
                    self.assertTrue((output / folder / "model.json").is_file())
                    self.assertTrue((output / folder / "carrier.json").is_file())
                    self.assertEqual(generation.load(output / folder / "result.json"), result)

    def test_outer_timeout_stops_nested_group_with_stalled_parent_and_bounds_pipe_drain(self) -> None:
        marker = self.root / "descendant-completed"
        pidfile = self.root / "descendant.pid"
        trigger = self.root / "spawn-after-first-census"
        spawned = self.root / "spawn.json"
        child = "import pathlib,time,signal; signal.signal(signal.SIGTERM,signal.SIG_IGN); time.sleep(8); pathlib.Path(" + repr(str(marker)) + ").write_text('escaped')"
        self.entry.write_text("import subprocess,sys,pathlib,time,signal,json,os\nsignal.signal(signal.SIGTERM,signal.SIG_IGN)\n"
                              + "while not pathlib.Path(" + repr(str(trigger)) + ").exists(): time.sleep(0.01)\n"
                              + "p=subprocess.Popen([sys.executable,'-c'," + repr(child)
                              + "],start_new_session=True)\npathlib.Path(" + repr(str(pidfile)) + ").write_text(str(p.pid))\n"
                              + "pathlib.Path(" + repr(str(spawned)) + ").write_text(json.dumps({'parent_pid':os.getpid(),'child_pid':p.pid,'child_pgid':os.getpgid(p.pid),'spawned_monotonic_ns':time.monotonic_ns()}))\ntime.sleep(30)\n")
        self.config["entry_sha256"] = formal.sha(self.entry.read_bytes())
        self.config["runtime_identity"] = self.identity()
        censuses = []
        actual_census = formal._owned_groups
        def observed_census(pid: int) -> tuple[set[int], list[str]]:
            groups, observations = actual_census(pid)
            censuses.append({"at_monotonic_ns": time.monotonic_ns(), "checker_pid": pid, "groups": sorted(groups), "observations": list(observations)})
            if len(censuses) == 1:
                trigger.write_text("controlled nested spawn after first actual OS census")
            return groups, observations
        def fixture_cleanup() -> None:
            if pidfile.exists():
                try:
                    os.killpg(int(pidfile.read_text()), signal.SIGKILL)
                except ProcessLookupError:
                    pass
        self.addCleanup(fixture_cleanup)
        started = time.monotonic()
        with patch.object(formal, "_owned_groups", side_effect=observed_census):
            with self.assertRaisesRegex(formal.GateError, "outer timeout") as caught:
                formal._invoke(self.config, ["identity"])
        trace = {"source_sha256": formal.sha(Path(formal.__file__).read_bytes()), "started_monotonic_ns": round(started * 1e9),
                 "returned_monotonic_ns": time.monotonic_ns(), "censuses": censuses, "cleanup_observation": str(caught.exception),
                 "spawn": json.loads(spawned.read_bytes()) if spawned.exists() else None,
                 "scope": "Actual private nested process group; test author deliberately triggers spawn after first census and stalls both parents on TERM."}
        (self.root / "timeout_trace.json").write_bytes(formal.canonical(trace))
        self.assertEqual(caught.exception.status, "incomplete")
        self.assertLess(time.monotonic() - started, 6)
        self.assertTrue(pidfile.exists())
        # Process-group cleanup is actual OS evidence, not a mocked return code.
        pid = int(pidfile.read_text())
        self.assertNotIn(pid, censuses[0]["groups"])
        self.assertTrue(any(pid in census["groups"] for census in censuses[1:]), trace)
        for _ in range(30):
            try:
                os.kill(pid, 0)
            except ProcessLookupError:
                break
            time.sleep(0.05)
        else:
            self.fail("controlled checker descendant remains observable after cleanup")
        self.assertFalse(marker.exists(), str(caught.exception))


if __name__ == "__main__":
    unittest.main()

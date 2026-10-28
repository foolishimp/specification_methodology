"""Retained actual CLI qualification with explicitly test-authored source answers.

No paid model call, semantic acceptance, Product authority or release is claimed.
The fixture policy grants only its disposable local Worker/process territory.
"""
from __future__ import annotations

import argparse
import base64
import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from typing import Any

from test_ac_generate import GenerationTests, SOURCE, fixture_answer
from test_ac_support_core import Fixture, obj
import ac_generate as gen
import ac_graph
import ac_support_core as core
import ac_support_effects as effects

formal = gen.ac_formal_gate

TENANT = Path(__file__).resolve().parents[1]


def save(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(formal.canonical(value))


def call(argv: list[str], folder: Path, request: Any = None) -> tuple[int, Any]:
    folder.mkdir(parents=True, exist_ok=False)
    raw = b"" if request is None else formal.canonical(request)
    (folder / "stdin").write_bytes(raw)
    started = time.monotonic()
    process = subprocess.run(argv, input=raw, capture_output=True, timeout=600,
                             env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}, check=False)
    (folder / "stdout").write_bytes(process.stdout)
    (folder / "stderr").write_bytes(process.stderr)
    save(folder / "invocation.json", {"argv": argv, "returncode": process.returncode,
        "elapsed_ms": round((time.monotonic() - started) * 1000), "stdin_sha256": formal.sha(raw),
        "provenance": "actual local CLI execution; explicit controlled semantic/process fixture"})
    value = json.loads(process.stdout)
    return process.returncode, value


def generate(output: Path, config: dict[str, Any], config_path: Path) -> list[Path]:
    models = []
    for label, command in (("fresh-alpha", "assemble"), ("fresh-beta", "run")):
        root = output / label; root.mkdir()
        corpus = root / "source"; corpus.mkdir()
        raw = SOURCE.replace("# Rules", "# " + label).encode()
        (corpus / "rules.md").write_bytes(raw)
        manifest = root / "manifest.json"
        gen.save(manifest, {"profile": "ac.generation.corpus/1", "subject_id": "repo://formal-gate-qualification/" + label + "/",
                           "revision": "explicit-test-authored-1", "files": [{"path": "rules.md", "sha256": gen.sha(raw), "bytes": len(raw)}]})
        run = root / "run"
        plan = gen.prepare(corpus, manifest, run, "direct", None, 1000, formal_checker=config)
        chunks = gen.load(run / "chunks.json")
        # Reuse the existing author-capture fixture, explicitly marked synthetic.
        author = GenerationTests("test_snapshot_and_chunks_cover_exact_original_source")
        author.output = run; author.plan = plan; author.chunks = chunks
        author.fake_attempt("author", fixture_answer(chunks[0]))
        save(root / "SEMANTIC_PROVENANCE.json", {"producer": "test-author", "mode": "explicit replay of test-authored answers",
            "paid_model_calls": 0, "claim": "Exercises ordinary generation mechanics; no LLM quality or semantic fidelity acceptance."})
        args = [sys.executable, str(TENANT / "code/ac_generate.py"), command, "--output", str(run),
                "--formal-checker", str(config_path), "--formal-checker-sha256", formal.sha(config_path.read_bytes())]
        if command == "run":
            args.extend(["--execute", "--codex", "/never-called-completed-authored-replay"])
        code, response = call(args, root / "actual-cli")
        assert code == 0, response
        result = gen.load(run / "proposal/result.json")
        assert result["formal_gate"]["status"] == "verified", result
        assert len(result["formal_gate"]["runs"]) == 2
        assert result["status"] == "proposed" and "semantic acceptance unassessed" in result["claim"]
        models.append(run / "proposal/model.json")
        print(label + " ordinary " + command + " model/carrier gate verified", flush=True)
        if label == "fresh-alpha":
            for module, destination in (("ac_grounding.py", "grounded-proposal"), ("ac_repair.py", "repaired-proposal")):
                code, response = call([sys.executable, str(TENANT / "code" / module), "assemble", "--output", str(run)], root / module.removesuffix(".py"))
                assert code == 0 and response["formal_gate"]["status"] == "verified", response
                assert len(response["formal_gate"]["runs"]) == 2
                assert (run / destination / "model.json").exists()
                save(root / (module + ".provenance.json"), {"path": "ordinary " + module + " assemble",
                     "answer_selection": "strict_original explicitly test-authored replay",
                     "claim": "Required gate exercised at the actual variant producer; no repair/normalization semantic success inferred."})
                print(destination + " required model/carrier gate verified", flush=True)
    return models


class PublicCase:
    def __init__(self, root: Path, model_path: Path, config: dict[str, Any] | None,
                 *, selected: bool = True, missing_authority: bool = False):
        root.mkdir()
        self.root = root; self.f = Fixture(root)
        raw = model_path.read_bytes()
        self.f.model_source = self.f.write("inputs/model.json", raw)
        native = ac_graph.validate(json.loads(raw))
        self.f.model = obj({"source": self.f.model_source, "format": "model", "model_id": native.identity, "model_sha256": native.sha256})
        self.seed = native.document["populations"]["objects"][0]["id"]
        actor = self.f.write("inputs/actor.py", (TENANT / "test_env/support_fixtures/local_actor.py").read_bytes())
        executor = self.f.policy["executors"]["registered"]
        executor["argv"] = [str(Path(sys.executable).resolve()), str(self.f.workspace / "inputs/actor.py"), "count", str(self.f.workspace / "outputs/count")]
        executor["dependencies"] = [actor]
        executor["settings"] = {"timeout_ms": 5000, "max_output_bytes": 100000}
        if config is not None:
            self.f.policy["formal_gate"] = obj({"checker": config, "required_targets": ["worker"] if selected else []})
        if missing_authority:
            self.f.policy["grants"]["work"]["targets"] = []
        runtime = self.f.runtime()
        self.policy_sha256 = runtime.policy_sha256
        self.counter = 0

    def invoke(self, operation: str, args: Any) -> Any:
        self.counter += 1
        request = {"schema": core.REQUEST, "id": "formal-public-" + str(self.counter), "operation": operation, "arguments": args}
        argv = [sys.executable, str(TENANT / "code/ac_support.py"), "--policy", str(self.root / "policy.json"),
                "--policy-sha256", self.policy_sha256, "--principal", "executive", "call", "--request", "-"]
        _, result = call(argv, self.root / "calls" / str(self.counter), request)
        return result

    def load(self, ref: dict[str, str]) -> Any:
        raw = (self.f.evidence / "objects" / (ref["sha256"] + ".json")).read_bytes()
        assert formal.sha(raw) == ref["sha256"]
        return json.loads(raw)

    def context(self) -> tuple[Any, Any]:
        result = self.invoke("context.assemble", {"packet": self.f.packet(),
            "models": [{"model": self.f.model, "selections": [{"seeds": [self.seed], "budget_records": None}]}],
            "sources": [], "late_acquisition": [], "envelope": {"capacity_bytes": None, "boundary": "executor-stdin-utf8",
                "host_context": {"state": "unknown", "bytes": None, "evidence": None}}})
        assert result["status"] == "ok", result
        ref = result["result"]["artifact"]
        return ref, self.load(ref)["payload"]

    def preflight(self, context: Any) -> Any:
        return self.invoke("contract.preflight", {"context": context, "grant_id": "work", "executor_id": "registered", "result_key": "formal-test", "observations": []})

    def dispatch(self, preflight: Any) -> Any:
        return self.invoke("dispatch.start", {"preflight": preflight})

    def delivered(self, preflight: Any, context: Any) -> Any:
        result = self.dispatch(preflight)
        assert result["status"] == "ok", result
        attempt = result["result"]["value"]["attempt"]
        deadline = time.monotonic() + 300
        while time.monotonic() < deadline:
            observed = self.invoke("dispatch.observe", {"attempt": attempt, "after_event": 0})
            assert observed["status"] == "ok", observed
            value = observed["result"]["value"]
            if value["process_end"] is not None:
                assert value["process_end"]["returncode"] == 0, value
                stdout = self.load(value["output"]["stdout"])["payload"]
                worker = json.loads(base64.b64decode(stdout["bytes_base64"]))
                assert worker["stdin_sha256"] == context["rendered_sha256"]
                assert (self.f.workspace / "outputs/count").read_text() == "1"
                formal_use = None
                if "formal_gate" in context:
                    dispatch_use = self.load(value["anchor"]["formal_use"])["payload"]
                    assert dispatch_use["stage"] == "dispatch"
                    checked_events = [event for event in value["events"] if event["kind"] == "formal_gate_verified"]
                    assert len(checked_events) == 1
                    formal_use = checked_events[0]["data"]["formal_use"]
                    use = self.load(formal_use)
                    assert use["payload"]["stage"] == "supervisor" and use["provenance"]["attempt"] == attempt
                    assert use["payload"]["binding"]["rendered_sha256"] == worker["stdin_sha256"]
                summary = {"attempt": attempt, "context_sha256": context["rendered_sha256"], "worker_stdin_sha256": worker["stdin_sha256"],
                           "observed_process_exit": 0, "formal_required": "formal_gate" in context,
                           "supervisor_formal_use": formal_use,
                           "claim": "Actual controlled local Worker stdin; no semantic or external-effect acceptance."}
                save(self.root / "DELIVERY.json", summary)
                return summary
            time.sleep(1)
        raise AssertionError("Actual Worker process end not observed within bound")


def support(output: Path, model: Path, config: dict[str, Any]) -> dict[str, Any]:
    case = PublicCase(output / "required", model, config)
    context_ref, context = case.context()
    receipt = case.preflight(context_ref)
    assert receipt["status"] == "ok" and receipt["result"]["value"]["decision"] == "admitted", receipt
    preflight = receipt["result"]["artifact"]
    formal_ref = receipt["result"]["value"]["formal_evidence"]
    gate = case.load(formal_ref)["payload"]
    assert gate["status"] == "verified"
    adverse = []
    # Retain each exact before/after control; the original protected bytes are restored.
    report = Path(gate["runs"][0]["bundle"]) / "result.json"
    before = report.read_bytes()
    save(case.root / "controls/report-original.json", json.loads(before))
    report.write_bytes(formal.canonical({**json.loads(before), "reason": "caller forged success metadata"}))
    response = case.dispatch(preflight)
    assert response["status"] == "refused", response
    adverse.append({"case": "tampered-real-report", "response": response})
    report.write_bytes(before)
    source = case.f.workspace / "inputs/model.json"; before = source.read_bytes(); source.write_bytes(before + b" ")
    response = case.dispatch(preflight)
    assert response["status"] == "refused", response
    adverse.append({"case": "stale-actual-model-source", "response": response})
    source.write_bytes(before)
    # A caller can construct JSON claiming success; the public request rejects it.
    response = case.invoke("contract.preflight", {"context": context_ref, "grant_id": "work", "executor_id": "registered",
        "result_key": "forged", "observations": [], "formal_gate": {"status": "verified"}})
    assert response["status"] == "refused", response
    adverse.append({"case": "caller-forged-success-json", "response": response})
    # Explicit adversarial producer control: a new digest does not authorize removing a policy condition.
    altered = copy.deepcopy(context); del altered["formal_gate"]
    body = {key: altered[key] for key in ("packet", "projections", "sources", "late_acquisition", "boundaries")}
    body["schema"] = "a_c.fd-support.actor-context/1"
    altered["rendered_utf8"] = core.PREFIX + formal.canonical(body).decode()
    altered["rendered_sha256"] = formal.sha(altered["rendered_utf8"].encode())
    original = case.load(context_ref)
    forged, forged_ref = core.make_artifact("context", obj(altered), obj(original["provenance"]))
    runtime = case.f.runtime()
    effects.EvidenceStore(runtime).retain(forged)
    response = case.preflight(forged_ref)
    assert response["status"] == "refused", response
    adverse.append({"case": "policy-condition-removed-from-new-context", "response": response})
    assert not (case.f.workspace / "outputs/count").exists()
    save(case.root / "ADVERSE.json", adverse)
    delivered = case.delivered(preflight, context)
    print("required actual CLI Context/preflight/dispatch/Worker path verified", flush=True)

    denied = PublicCase(output / "missing-authority", model, config, missing_authority=True)
    denied_ref, _ = denied.context()
    denied_receipt = denied.preflight(denied_ref)
    assert denied_receipt["status"] == "ok" and denied_receipt["result"]["value"]["decision"] == "rejected", denied_receipt
    evidence = denied.load(denied_receipt["result"]["value"]["formal_evidence"])["payload"]
    assert evidence["status"] == "verified"
    refused = denied.dispatch(denied_receipt["result"]["artifact"])
    assert refused["status"] == "refused" and not (denied.f.workspace / "outputs/count").exists()
    save(denied.root / "AUTHORITY.json", {"proof": "verified", "admission": "rejected", "dispatch": refused})
    legacy = []
    for label, selected_config in (("no-lean", None), ("optional-unselected", config)):
        old = PublicCase(output / label, model, selected_config, selected=False)
        ref, ctx = old.context(); pre = old.preflight(ref)
        assert pre["status"] == "ok" and pre["result"]["value"]["decision"] == "admitted", pre
        assert "formal_evidence" not in pre["result"]["value"]
        legacy.append(old.delivered(pre["result"]["artifact"], ctx))
    return {"required_delivery": delivered, "adverse_controls": len(adverse), "good_proof_missing_authority": "rejected", "legacy_deliveries": legacy}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--checker", type=Path, required=True)
    parser.add_argument("--checker-sha256", required=True)
    parser.add_argument("--model", type=Path, help="run support phase over an already generated exact model")
    args = parser.parse_args()
    config = formal.load_config(args.checker, args.checker_sha256)
    output = args.output.resolve(); output.mkdir(parents=True, exist_ok=False)
    models = [args.model] if args.model else generate(output, config, args.checker.resolve())
    result = support(output, models[0].resolve(), config)
    save(output / "QUALIFICATION.json", {"status": "passed", "generation_models": [str(p) for p in models], "support": result,
        "limits": ["Controlled authored/replayed answers; no paid LLM campaign.", "Local fixed Worker process; no semantic acceptance.", "Author qualification only; independent review is separate."]})
    print(json.dumps({"status": "passed", "output": str(output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Fixed qualification executor: outer admission stays outside the ordinary prompt.

This executable is selected and pinned by the qualification operator. It does
not select a task, package, model or authority and is never a general skill
runtime. Its closed return is a local transport report, not an LLM assessment.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def read_pin(pin: dict) -> bytes:
    path = Path(pin["path"])
    if not path.is_absolute() or any(p.is_symlink() for p in (path, *path.parents)):
        raise ValueError("Pinned qualification input must be an exact regular path")
    raw = path.read_bytes()
    if sha(raw) != pin["sha256"]:
        raise ValueError("Pinned qualification input changed: " + str(path))
    return raw


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--config-sha256", required=True)
    args = parser.parse_args()
    raw_config = read_pin({"path": str(args.config), "sha256": args.config_sha256})
    config = json.loads(raw_config)
    if config["schema"] != "stdo_skills.qualification-launch/1":
        raise ValueError("Unsupported fixed qualification configuration")
    read_pin(config["transport"])
    spec = importlib.util.spec_from_file_location("qualification_actor_transport", config["transport"]["path"])
    if spec is None or spec.loader is None:
        raise ValueError("Pinned transport module unavailable")
    transport = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = transport
    spec.loader.exec_module(transport)
    core = transport.core
    plan = transport.load_plan(Path(config["actor_plan"]["path"]), config["actor_plan"]["sha256"])
    prompt = read_pin(config["ordinary_prompt"])
    outer = sys.stdin.buffer.read(config["max_outer_bytes"] + 1)
    if len(outer) > config["max_outer_bytes"] or not outer.startswith(core.PREFIX.encode()):
        raise ValueError("Outer Context unavailable or outside its exact bound")
    body = core.parse_json(outer[len(core.PREFIX.encode()):])
    packet = body["packet"]
    if body["schema"] != "a_c.fd-support.actor-context/1" or packet["activation"]["id"] != config["activation_id"]:
        raise ValueError("Outer Context differs from the selected trial activation")
    if packet["actor_authority"]["actor_id"] != config["return_actor"]["id"]:
        raise ValueError("Outer Context targets a different physical executor")
    output = Path(plan.document["evidence_directory"])
    if output.exists() or not output.parent.is_dir():
        raise ValueError("Trial output must be fresh under an existing operator parent")
    output.mkdir(mode=0o700)

    def save(name: str, value) -> None:
        raw = value if isinstance(value, bytes) else core.canonical(value) + b"\n"
        with (output / name).open("xb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())

    save("outer-context.bin", outer)
    save("ordinary-prompt.bin", prompt)
    save("plan.json", plan.raw)
    save("projection.json", {
        "schema": "stdo_skills.qualification-projection/1",
        "configuration_sha256": sha(raw_config),
        "outer_context_sha256": sha(outer), "outer_context_bytes": len(outer),
        "ordinary_prompt_sha256": sha(prompt), "ordinary_prompt_bytes": len(prompt),
        "rule": "Exact operator-selected ordinary input; outer admission and return bookkeeping are retained but not sent to the host",
        "case": config["case"], "package": config["package"],
        "actor_visible": "ordinary prompt, normal installed skill discovery, ordinary workspace files and configured tools; no oracle or outer Context",
    })
    names = core.environment_passthrough(plan.document["settings"], plan.document["environment"])
    # Only this launched, admitted executor acquires its existing selected value.
    # Preparation and evidence never acquire, serialize or hash credentials.
    inherited = {name: os.environ[name] for name in ("HOME", "home", "CODEX_HOME", *names) if name in os.environ}
    save("invocation.json", {
        "argv": plan.document["argv"], "cwd": plan.document["cwd"],
        "environment": plan.document["environment"],
        "environment_passthrough": [{"name": name, "present": name in inherited} for name in names],
        "protected_environment_presence": [{"name": name, "present": name in inherited} for name in ("HOME", "home", "CODEX_HOME")],
        "settings_declared": plan.document["settings"],
        "model_scope": "Actual vendor model, usage, safety events and costs remain unmodified raw vendor observations; no alias normalization or bypass",
    })
    # Exact pinned existing bounded capture mechanics; no closed-return decoder
    # is imposed on the ordinary host answer. This private implementation seam
    # is explicitly part of this test executor's dependency pin, not public API.
    observed = transport._capture(plan, prompt, output, inherited)
    save("process.json", observed)
    summary = {
        "schema": "stdo_skills.qualification-observation/1", "case": config["case"],
        "package": config["package"], "transport": observed,
        "ordinary_prompt_sha256": sha(prompt),
        "retained": [{"path": name, "sha256": sha((output / name).read_bytes())}
                     for name in ("outer-context.bin", "ordinary-prompt.bin", "projection.json", "invocation.json", "vendor.stdout", "vendor.stderr", "process.json")],
        "assessment": "not performed by this executable; actual skill use, task effects and semantic result require source-first assessment",
    }
    save("result.json", summary)
    report_ref = {"engine": "workspace-regular-file", "root": "control", "path": "actor-output/result.json",
                  "object": None, "sha256": sha((output / "result.json").read_bytes()), "selector": None}
    result = {
        "schema": "a_c.fd-support.closed-return/1", "id": config["activation_id"] + ":observations",
        "frame": {key: packet["frame"][key] for key in ("id", "revision")},
        "activation": core.activation_identity(packet), "subject": packet["subject_basis"]["subject"],
        "basis": {"method_profile": packet["subject_basis"]["method_profile"], "observations": packet["subject_basis"]["observations"]},
        "actor": config["return_actor"], "consumer": packet["evidence_relations"]["consumer"],
        "evaluations": [], "not_performed": [],
        "work_result": {"value": "candidate_ready", "cause": "Exact local trial observations retained; no host success or semantic qualification inferred",
                        "candidate": report_ref, "evidence": [report_ref], "residuals": ["Host skill discovery, behavior and qualification remain unassessed"]},
        "residuals": ["This return identifies the fixed local executor, not the vendor model as an authenticated semantic return producer"],
        "invalidators": [],
    }
    sys.stdout.buffer.write(core.canonical(result))
    sys.stdout.buffer.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

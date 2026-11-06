"""Explicit writable a_c runtime derivation from exact installed source custody."""
from __future__ import annotations

import json
import importlib.util
import os
from pathlib import Path
import subprocess
import time

PROFILE = "build_tenants/lean/profiles/proof-support-v1.json"
GENERATED = tuple("build_tenants/lean/" + n + "/" for n in (".lake", ".cache", ".toolchain", ".bootstrap"))


def boundary():
    path = Path(__file__).absolute().with_name('payload_boundary.py')
    spec = importlib.util.spec_from_file_location('stdo_payload_boundary', path)
    module = importlib.util.module_from_spec(spec)
    exec(compile(path.read_bytes(), str(path), 'exec'), module.__dict__)
    return module


def separate(tool, output, protected):
    output, protected = tool.ordinary_path(output), tool.ordinary_path(protected)
    tool.require(not output.is_relative_to(protected) and not protected.is_relative_to(output), "runtime derivation overlaps protected input")
    for one, other in ((output, protected), (protected, output)):
        tool.require(not any(p.exists() and other.exists() and os.path.samefile(p, other) for p in (one, *one.parents)),
                     "runtime derivation aliases protected input")


def selected(tool, bundle, tools_root):
    meta, sources = tool.source_bytes(tool.read_bundle(bundle))
    tool.require(meta["kind"] == "stdo.installed-tooling/2", "current tooling selection required")
    rows = {r["archive_path"].removeprefix("a_c/"): r for r in meta["sources"] if r["archive_path"].startswith("a_c/")}
    for name, row in rows.items():
        raw = tool.ordinary_path(tools_root / "a_c" / name).read_bytes()
        tool.require(tool.sha(raw) == row["sha256"] and len(raw) == row["bytes"], "original selected a_c custody differs: " + name)
    tool.require(PROFILE in rows and "scripts/bootstrap.py" in rows, "runtime source selection is incomplete")
    return meta, rows


def derive(tool, bundle, tools_root, destination, receipt):
    tools_root, destination, receipt = map(tool.ordinary_path, (tools_root, destination, receipt))
    boundary().guard([destination, receipt], [bundle, tools_root], anchors=[Path(__file__).absolute()])
    meta, rows = selected(tool, bundle, tools_root)
    for protected in (bundle, tools_root):
        separate(tool, destination, protected); separate(tool, receipt, protected)
    separate(tool, receipt, destination)
    tool.require(not destination.exists() and not receipt.exists(), "preserve existing runtime derivation/receipt")
    destination.mkdir(parents=True, exist_ok=False)
    for name, row in rows.items():
        target = destination / name; target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((tools_root / "a_c" / name).read_bytes()); target.chmod(int(row["git_mode"], 8) & 0o777)
    record = {"kind": "stdo.ac-runtime-derivation/1", "status": "prepared", "version": meta["distribution_version"],
              "source_identity_sha256": meta["source_identity_sha256"], "tooling_manifest_sha256": tool.sha((bundle / "TOOLING.json").read_bytes()),
              "source_root": str(tools_root / "a_c"), "runtime_root": str(destination), "source_members": rows,
              "allowed_source_delta": PROFILE, "generated_roots": list(GENERATED)}
    validate(tool, record)
    receipt.parent.mkdir(parents=True, exist_ok=True); receipt.write_bytes(tool.encoded(record))
    return {"status": "derived", "runtime_root": str(destination), "receipt": str(receipt), "receipt_sha256": tool.sha(receipt.read_bytes())}


def validate(tool, record, *, require_support=False):
    tool.require(record.get("kind") == "stdo.ac-runtime-derivation/1" and record.get("allowed_source_delta") == PROFILE and
                 record.get("generated_roots") == list(GENERATED), "unsupported runtime derivation contract")
    source, runtime = map(tool.ordinary_path, (record["source_root"], record["runtime_root"]))
    boundary().guard([runtime], [source], anchors=[Path(__file__).absolute()])
    separate(tool, runtime, source)
    rows = record["source_members"]
    tool.require(rows and PROFILE in rows, "runtime source closure missing")
    supported = record.get("status") == "support-established"
    tool.require(supported or (not require_support and record.get("status") == "prepared"), "successful support establishment receipt required")
    for name, row in rows.items():
        tool.safe_path(name)
        original = tool.ordinary_path(source / name).read_bytes()
        tool.require(tool.sha(original) == row["sha256"] and len(original) == row["bytes"], "original source custody changed")
        raw = tool.ordinary_path(runtime / name).read_bytes()
        expected = record["profile_sha256"] if supported and name == PROFILE else row["sha256"]
        tool.require(tool.sha(raw) == expected, "undeclared runtime source delta: " + name)
    for current, dirs, files in os.walk(runtime, followlinks=False):
        relative = Path(current).relative_to(runtime).as_posix()
        for directory in list(dirs):
            path = Path(current) / directory; name = path.relative_to(runtime).as_posix() + "/"
            if name in GENERATED:
                dirs.remove(directory); continue
            tool.require(not path.is_symlink(), "redirected runtime source directory")
            if directory == "__pycache__":
                tool.require(all(p.is_file() and not p.is_symlink() and p.suffix == ".pyc" for p in path.iterdir()), "undeclared runtime cache")
                dirs.remove(directory)
        for filename in files:
            name = (Path(current) / filename).relative_to(runtime).as_posix()
            tool.require(name in rows, "undeclared runtime source member: " + name)
    if supported:
        run = record["bootstrap"]
        python = run["python"]
        tool.require(Path(python["invocation"]).resolve(strict=True) == Path(python["physical"]) and
                     tool.sha(tool.ordinary_path(python["physical"]).read_bytes()) == python["sha256"], "runtime bootstrap Python changed")
        tool.require(run["argv"] == [python["invocation"], "-B", str(runtime / "scripts/bootstrap.py"), "lean", "--establish-support"] and
                     run["returncode"] == 0, "support profile has no prescribed successful bootstrap provenance")
        for label in ("stdout", "stderr", "execution"):
            ref = run[label]; tool.require(tool.sha(tool.ordinary_path(ref["path"]).read_bytes()) == ref["sha256"], "support bootstrap receipt changed")
        observed = run["result"]
        tool.require(observed["version"] == record["version"] and observed["status"] == "installed" and
                     observed["proof_support"] == "freshly_established" and observed["lean_root"] == str(runtime / "build_tenants/lean") and
                     observed["execution"] == run["execution"]["path"], "support establishment result differs")
        execution = json.loads(Path(run["execution"]["path"]).read_bytes())
        expected = [[python["invocation"], "-B", str(runtime / "build_tenants/lean/scripts/bootstrap.py")],
                    [python["invocation"], "-B", str(runtime / "build_tenants/lean/scripts/formal_support.py"), "--output", str(runtime / PROFILE)]]
        tool.require(execution["schema"] == "a_c.bootstrap.execution/1" and [r["argv"] for r in execution["steps"]] == expected and
                     all(r["exit_code"] == 0 for r in execution["steps"]), "support owner execution steps differ")
        for step in execution["steps"]:
            for label in ("stdout", "stderr"):
                ref = step[label]; raw = tool.ordinary_path(Path(run["execution"]["path"]).parent / tool.safe_path(ref["path"])).read_bytes()
                tool.require(tool.sha(raw) == ref["sha256"] and len(raw) == ref["bytes"], "support owner execution output differs")
        profile = json.loads((runtime / PROFILE).read_bytes()); lock = json.loads((runtime / "build_tenants/lean/toolchain-lock.json").read_bytes())
        tool.require(profile.get("schema") == "a_c.lean.proof-support/1" and profile["lean"] == lock["lean"] and profile["mathlib"] == lock["mathlib"] and
                     profile["kernel_replay"] == "leanchecker --fresh AC.GateProof" and "origin" not in profile and "scale_extension" not in profile,
                     "unsupported fresh support profile provenance")
        core = {"AC/" + name + ".lean" for name in ("Model", "Closure", "Projection", "Structure", "GateProof", "GateRuntime")}
        tool.require(core <= profile["members"].keys() and any(p.endswith("/bin/leanchecker") for p in profile["members"]) and
                     any(p.endswith("/bin/lean") for p in profile["members"]), "support profile omits required sources/compiler")
        for name in core:
            tool.require(profile["members"][name] == rows["build_tenants/lean/" + name]["sha256"], "support profile substitutes selected theorem source")
        for name, digest in profile["members"].items():
            raw = tool.ordinary_path(runtime / "build_tenants/lean" / tool.safe_path(name)).read_bytes()
            tool.require(tool.sha(raw) == digest, "actual support profile member changed")
    return record


def load(tool, path, digest):
    raw = tool.ordinary_path(path).read_bytes()
    tool.require(tool.sha(raw) == digest, "runtime derivation receipt digest differs")
    return json.loads(raw)


def bootstrap(tool, prepared, prepared_sha, python, output):
    boundary().guard([output], [prepared], anchors=[Path(__file__).absolute()])
    record = load(tool, prepared, prepared_sha); validate(tool, record)
    tool.require(record["status"] == "prepared", "fresh prepared derivation required")
    output = tool.ordinary_path(output); runtime = Path(record["runtime_root"])
    boundary().guard([output, runtime], [Path(record['source_root'])], anchors=[Path(__file__).absolute()])
    separate(tool, output, runtime); separate(tool, output, Path(record["source_root"]))
    tool.require(not output.exists(), "preserve prior bootstrap evidence")
    output.mkdir(parents=True, exist_ok=False)
    python = Path(python).absolute(); physical = python.resolve(strict=True)
    command = [str(python), "-B", str(runtime / "scripts/bootstrap.py"), "lean", "--establish-support"]
    start = time.time_ns(); process = subprocess.run(command, capture_output=True, timeout=1800)
    run = {"argv": command, "returncode": process.returncode, "started_ns": start, "ended_ns": time.time_ns(),
           "python": {"invocation": str(python), "physical": str(physical), "sha256": tool.sha(tool.ordinary_path(physical).read_bytes())}}
    for label, raw in (("stdout", process.stdout), ("stderr", process.stderr)):
        path = output / (label + ".txt"); path.write_bytes(raw); run[label] = {"path": str(path), "sha256": tool.sha(raw)}
    (output / "execution.json").write_bytes(tool.encoded(run))
    tool.require(process.returncode == 0, "Lean bootstrap incomplete; retain partial runtime and execution before recovery")
    text = process.stdout.decode(); start = text.rfind("\n{") + 1
    result = json.loads(text[start:]); execution_path = tool.ordinary_path(result["execution"])
    run.update(result=result, execution={"path": str(execution_path), "sha256": tool.sha(execution_path.read_bytes())})
    successor = {**record, "status": "support-established", "predecessor": {"path": str(prepared), "sha256": prepared_sha},
                 "profile_sha256": tool.sha((runtime / PROFILE).read_bytes()), "bootstrap": run}
    validate(tool, successor, require_support=True)
    receipt = output / "derivation.json"; receipt.write_bytes(tool.encoded(successor))
    return {"status": "support-established", "runtime_root": str(runtime), "receipt": str(receipt), "receipt_sha256": tool.sha(receipt.read_bytes()),
            "profile_sha256": successor["profile_sha256"]}

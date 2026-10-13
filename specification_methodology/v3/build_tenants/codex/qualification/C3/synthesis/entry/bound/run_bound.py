#!/usr/bin/env python3
"""Use the original native controller with a lawfully bound fixture."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("entry_controller", HERE.parent / "run_entry.py")
controller = importlib.util.module_from_spec(spec)
spec.loader.exec_module(controller)
controller.HERE = HERE


def prepare(cut):
    if (HERE / "FREEZE.json").exists():
        raise RuntimeError("Freeze already exists")
    cut = controller.git("rev-parse", cut).decode().strip()
    validation = json.loads((HERE / "FIXTURE_VALIDATION.json").read_text())
    roots = [Path(validation["fixture_root"]), Path(tempfile.mkdtemp(prefix="stdo-bound-rc2-", dir="/private/tmp"))]
    source_files = controller.git("ls-tree", "-r", "--name-only", cut, "--", controller.PACKAGE).decode().splitlines()
    snapshots = []
    for index, root in enumerate(roots):
        if index:
            for p in (HERE / "fixture").rglob("*"):
                if p.is_file():
                    dst = root / p.relative_to(HERE / "fixture")
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(p, dst)
        for name in source_files:
            dst = root / "source" / name
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(controller.git("show", cut + ":" + name))
        shutil.copytree(controller.INSTALLED, root / "installed")
        command = ["stdo", "status", "--definition", str(root / "stdo_fixture.json"), "--verify"]
        receipt = json.loads(subprocess.check_output(command, text=True))
        assert receipt["valid"] and receipt["installed"] and not receipt["failures"]
        assert receipt["definition_id"] == "urn:stdo:qualification-fixture:entry-d1"
        assert receipt["manifest_sha256"] == controller.EXPECTED_MANIFEST
        manifest = json.loads((root / "installed/manifest.json").read_text())
        assert controller.digest((root / "installed/manifest.json").read_bytes()) == controller.EXPECTED_MANIFEST
        verified_members = 0
        for g in (manifest["standards"], manifest["auxiliary"]["plugin"]):
            for row in g["members"]:
                assert controller.digest((root / "installed" / g["installed_root"] / row["path"]).read_bytes()) == row["sha256"]
                verified_members += 1
        for row, key in ((manifest["auxiliary"]["license"], "path"), (manifest["auxiliary"]["release_note"], "installed_path")):
            assert controller.digest((root / "installed" / row[key]).read_bytes()) == row["sha256"]
            verified_members += 1
        controller.put(root / "controls/BUILDER_STATUS.json", receipt)
        projected = {k:receipt[k] for k in ("basis", "cut", "definition", "definition_id", "failures", "installed", "manifest_sha256", "path", "valid")}
        projected["projection_of_authentic_receipt"] = "controls/BUILDER_STATUS.json"
        projected["receipt_sha256"] = controller.digest((root / "controls/BUILDER_STATUS.json").read_bytes())
        controller.put(root / "controls/VERIFIED_BASIS.json", projected)
        source_inventory = controller.inventory(root / "source")
        installed_inventory = controller.inventory(root / "installed")
        export = {"frozen_candidate_commit": cut, "candidate_package": "source/" + controller.PACKAGE,
                  "fixture_definition": "stdo_fixture.json", "verified_definition": str(root / "stdo_fixture.json"),
                  "definition_sha256": controller.digest((root / "stdo_fixture.json").read_bytes()),
                  "receipt_command": command, "receipt_is_for_this_actual_fixture_definition": True,
                  "receipt_installed_flag_refers_to_rc2_builder_not_v3_candidate": True,
                  "installed_rc2_verified_members": verified_members,
                  "installed_rc2_manifest_sha256": controller.EXPECTED_MANIFEST,
                  "source_inventory": "controls/SOURCE_INVENTORY.json", "installed_inventory": "controls/INSTALLED_INVENTORY.json"}
        controller.put(root / "controls/EXPORT.json", export)
        controller.put(root / "controls/SOURCE_INVENTORY.json", source_inventory)
        controller.put(root / "controls/INSTALLED_INVENTORY.json", installed_inventory)
        shutil.copyfile(root / "TASK.md", root / "controls/TASK.md")
        controller.put(root / "controls/ACTIVATION.md", """# Experimental method-use activation

The subject is the disposable Product defined by ../stdo_fixture.json. Its WHAT
is the unchanged task at ../TASK.md; its HOW is ../workspace/. Its actual
definition was verified by the real tool in this temporary root. The compact
receipt and full authentic output are supplied here. Its installed flag refers
to the rc.2 builder, never to a v3 release.

The already-authorised run-scoped proposal grant is ../EXECUTION_CONTRACT.md.
The applicable project basis is ../REFERENCE_FRAME_BASIS.md. Read these through
the ordinary entry as required; select your own task-specific acquisitions.
They do not prescribe the task solution or a preselected task frame.

For the candidate call, the frozen successor package is the explicitly selected
experimental method under test. The installed rc.2 builder remains construction
authority. This selection does not claim v3 installation, adoption or release.
For the baseline call, use the complete verified rc.2 package and its ordinary
entry; its authority compressions are available with the owning standards.

Only Read, Glob and Grep are enabled. All granted inputs are beneath this
temporary root. External paths in provenance are not file-access grants. The
actor returns proposals; only the host executes validated workspace changes.
Each call has 120000 selected prompt/tool-material bytes, counting repeated
returns, 15 minutes and USD 2. Unknown or insufficient prerequisites are
reported truthfully. No hidden oracle, selected task frame or expected edits
are supplied to the actor.
""")
        controls = {p.name: controller.digest(p.read_bytes()) for p in (root / "controls").iterdir() if p.is_file()}
        snapshots.append({"root": str(root), "export": export, "control_sha256": controls,
                          "source_inventory": source_inventory, "installed_inventory": installed_inventory,
                          "initial_workspace": controller.inventory(root / "workspace")})
        prefix = "candidate" if index == 0 else "baseline"
        controller.put(HERE / "inputs" / (prefix + "_STATUS.json"), receipt)
        for name in ("ACTIVATION.md", "EXPORT.json", "VERIFIED_BASIS.json", "TASK.md"):
            dest = HERE / "inputs" / prefix / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / "controls" / name, dest)
    freeze = {"cut": cut, "temporary_root": str(roots[0]), "baseline_temporary_root": str(roots[1]),
              "oracle_sha256": controller.digest(controller.ORACLE.read_bytes()),
              "fixture_definition_sha256": validation["files"][next(i for i,p in enumerate(validation["files"]) if p["path"] == "stdo_fixture.json")]["sha256"],
              "snapshots": snapshots, "protocol": "bound-fixture-successor"}
    controller.put(HERE / "FREEZE.json", freeze)
    print(json.dumps({"cut": cut, "roots": [str(p) for p in roots], "verified": True}, indent=2))


def behavior(name, after=False):
    freeze = json.loads((HERE / "FREEZE.json").read_text())
    root = Path(freeze["baseline_temporary_root"] if name == "baseline" else freeze["temporary_root"])
    # Execute only the exact original or exact oracle-approved fixture programs.
    expected = controller.case()["workspace"]
    for rel in ("src/settings.py", "scripts/check_env.sh"):
        original = expected[rel]
        target = controller.re.sub(r"\bAPP_TOKEN\b", "APP_API_TOKEN", original)
        assert (root / "workspace" / rel).read_text() in (original, target)
    env = {"PATH": "/usr/bin:/bin", "APP_API_TOKEN": "fixture-token"}
    commands = [
        [sys.executable, "-B", "-c", "import runpy; runpy.run_path('workspace/src/settings.py')"],
        ["/bin/sh", "workspace/scripts/check_env.sh"]]
    rows = []
    for command in commands:
        p = subprocess.run(command, cwd=root, env=env, capture_output=True, text=True, timeout=10)
        rows.append({"command": command, "exit_code": p.returncode, "stdout": p.stdout, "stderr": p.stderr})
    expected_pass = after
    report = {"subject": name, "phase": "after" if after else "before", "environment": env,
              "commands": rows, "expected_pass": expected_pass,
              "observation_matches_expectation": all((r["exit_code"] == 0) == expected_pass for r in rows),
              "workspace": controller.inventory(root / "workspace")}
    controller.put(HERE / "behavior" / (name + ("-after.json" if after else "-before.json")), report)
    print(json.dumps(report, indent=2))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("action", choices=["prepare", "call", "apply", "behavior"])
    p.add_argument("--cut")
    p.add_argument("--name")
    p.add_argument("--mode", default="candidate", choices=["candidate", "baseline"])
    p.add_argument("--continuation", action="store_true")
    p.add_argument("--partial", action="store_true")
    p.add_argument("--after", action="store_true")
    a = p.parse_args()
    if a.action == "prepare":
        prepare(a.cut)
    elif a.action == "call":
        controller.run_call(a.name, a.mode, a.continuation)
    elif a.action == "apply":
        controller.apply(a.name, a.partial)
    else:
        behavior(a.name, a.after)


if __name__ == "__main__":
    main()

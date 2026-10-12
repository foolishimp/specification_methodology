"""Reacquire an already published exact RC6 cohort using its checked ref vector."""
from pathlib import Path
import argparse
import concurrent.futures
import datetime
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("rc6_public_checker", ROOT / "scripts/check_stack_release.py")
check = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = check
spec.loader.exec_module(check)
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--revision", required=True)
parser.add_argument("--ref-result", type=Path, default=OUT / "cohort-refs-final.json")
parser.add_argument("--manager", type=Path, default=Path("/private/tmp/stdo-rc5-installed-manager-20260906/bin/stdo"))
args = parser.parse_args()


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


revision = check.git(ROOT, "rev-parse", args.revision + "^{commit}").stdout.strip()
candidate = check.View(ROOT, revision)
manifest = candidate.read_json("stack_release.json")
require(manifest["cohort"]["cut"] == "v2.5.0-rc.6", "wrong selected cut")
qualification = json.loads(args.ref_result.read_text())
require(qualification["status"] == "valid" and qualification["phase"] == "refs"
        and not qualification["failures"], "missing passing exact-ref result")
url = manifest["publication"]["repository_url"]
require(qualification["repository_url"] == url, "ref-result endpoint mismatch")
sources = {}
for item in qualification["push_argv"]:
    match = re.fullmatch(r"([0-9a-f]{40}):(refs/.+)", item)
    if match:
        sources[match[2]] = match[1]
require(len(sources) == 13 and sources.get(manifest["cohort"]["carrier_ref"]) == revision,
        "ref result does not bind this exact 13-ref candidate")
scratch = Path(tempfile.mkdtemp(prefix="stdo-rc6-public-", dir="/private/tmp"))
bare = scratch / "public.git"
commands = []


def run(name, argv):
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = subprocess.run([str(a) for a in argv], capture_output=True)
    finished = datetime.datetime.now(datetime.timezone.utc).isoformat()
    (OUT / (name + ".stdout.txt")).write_bytes(result.stdout)
    (OUT / (name + ".stderr.txt")).write_bytes(result.stderr)
    commands.append({"name": name, "argv": [str(a) for a in argv], "returncode": result.returncode,
                     "started_at": started, "finished_at": finished,
                     "stdout_sha256": check.sha256(result.stdout), "stderr_sha256": check.sha256(result.stderr)})
    require(result.returncode == 0, name + " failed; exact output retained")
    return result.stdout


record = {"kind": "stdo.rc6.fresh-public-reacquisition", "status": "incomplete",
          "repository_url": url, "revision": revision, "isolated_root": str(scratch),
          "ref_result_sha256": check.sha256(args.ref_result.read_bytes())}
try:
    run("public-git-init", ["git", "init", "--bare", bare])
    release_refs = [p["release_ref"] for p in manifest["products"].values()]
    fetch = ["git", "--git-dir", bare, "fetch", "--no-tags", "--depth=1", url,
             *[ref + ":" + ref for ref in release_refs]]
    expected_manifest = manifest["products"]["specification_methodology"]["freeze"]["installed_manifest_sha256"]
    install = [args.manager, "--store", scratch / "store", "install", "v2.5.0-rc.6",
               "--repository", url, "--manifest-sha256", expected_manifest]
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        fetched = pool.submit(run, "public-products-fetch", fetch)
        installed = pool.submit(run, "public-stdo-install", install)
        fetched.result()
        installation = json.loads(installed.result())
    verification = json.loads(run("public-stdo-verify", [args.manager, "--store", scratch / "store",
        "verify", "v2.5.0-rc.6", "--manifest-sha256", expected_manifest]))
    require(verification["valid"] and not verification["failures"], "public Install invalid")
    require(installation["manifest_sha256"] == expected_manifest, "public Install identity differs")
    identities = {}
    for name, product in manifest["products"].items():
        ref = product["release_ref"]
        kind = check.git(bare, "cat-file", "-t", ref).stdout.strip()
        oid = check.git(bare, "rev-parse", ref).stdout.strip()
        peel = check.git(bare, "rev-parse", ref + "^{}").stdout.strip()
        expected_commit = product["freeze"]["commit"] if name == "specification_methodology" else revision
        require(kind == "tag" and oid == sources[ref] and peel == expected_commit,
                "reacquired immutable identity mismatch: " + name)
        identities[name] = {"ref": ref, "tag_object": oid, "commit": peel,
            "tree": check.git(bare, "rev-parse", peel + "^{tree}").stdout.strip(),
            "project_subtree_tree": check.git(bare, "rev-parse", peel + ":" + product["subtree"]).stdout.strip()}
    public_view = check.View(bare, revision)
    require(public_view.read_json("stack_release.json") == manifest, "public B cohort bytes differ")
    failures = check.check(bare, "stack_release.json", "content", revision, "origin")
    require(not failures, "public complete content fails: " + "; ".join(failures))
    members = scratch / "members"
    for name in ("axiom_indexer", "stdo_representation"):
        for member in manifest["products"][name]["subject"]["members"]:
            relative = name + "/" + member["path"]
            raw = public_view.read_member_bytes(relative, member["type"])
            require(check.sha256(raw) == member["sha256"], "public member digest differs: " + relative)
            dest = members / relative
            dest.parent.mkdir(parents=True, exist_ok=True)
            if member["type"] == "symlink":
                dest.symlink_to(raw.decode())
            else:
                dest.write_bytes(raw)
    source_commit = manifest["products"]["specification_methodology"]["freeze"]["commit"]
    source_view = check.View(bare, source_commit)
    manager_python = args.manager.with_name("python")
    manager_location = json.loads(run("public-manager-location", [manager_python, "-I", "-c",
        "import importlib.metadata,json,pathlib,stdo_toolchain; print(json.dumps({'version':importlib.metadata.version('stdo-toolchain'),'root':str(pathlib.Path(stdo_toolchain.__file__).parent)}))"]))
    require(manager_location["version"] == "0.1.3", "manager version differs")
    package_root = Path(manager_location["root"])
    package_members = []
    for path in source_view.files("specification_methodology/src/stdo_toolchain"):
        relative = path.removeprefix("specification_methodology/src/stdo_toolchain/")
        expected = check.sha256(source_view.read_bytes(path))
        require(check.sha256((package_root / relative).read_bytes()) == expected,
                "installed manager member differs: " + relative)
        package_members.append({"path": relative, "sha256": expected})
    require(len(package_members) == 11, "manager source membership differs")
    bindings = {"kind": "axiom-indexer.binding-set", "schema_version": 1,
                "bindings": [{"uri_prefix": "stdo://releases/v2.5.0-rc.6/", "path": installation["path"]}]}
    write_json(OUT / "public-bindings.json", bindings)
    binding_path = OUT / "public-bindings.json"
    executable = members / "axiom_indexer/build_tenants/core/code/ac.py"
    artifact_root = members / manifest["assets"]["stdo_semantic_index"]["root"]
    program = artifact_root / "axiomatic-program.json"
    logical_map = artifact_root / "logical-constraint-map.json"
    regenerated = scratch / "regenerated-map.json"
    report = run("public-index-validate", [sys.executable, "-B", executable, "validate", "--program", program,
        "--bindings", binding_path, "--emit-map", regenerated])
    require(regenerated.read_bytes() == logical_map.read_bytes(), "public map does not reproduce")
    report_path = manifest["assets"]["stdo_semantic_index"]["root"] + "/validation-report.json"
    require(report == public_view.read_bytes(report_path), "public validation result does not reproduce")
    recipe_prefix = OUT.relative_to(ROOT).as_posix()
    recipes = public_view.read_json(recipe_prefix + "/representation-index-commands.json")
    projections = []
    for recipe in recipes:
        if recipe["label"] == "validate":
            continue
        original = recipe["argv"]
        selected = [original[i + 1] for i, value in enumerate(original) if value == "--frame-index"]
        mode = original[original.index("--mode") + 1]
        argv = [sys.executable, "-B", executable, "project", "--program", program,
                "--bindings", binding_path, "--map", logical_map]
        for frame in selected:
            argv.extend(("--frame-index", frame))
        raw = run("public-index-" + recipe["label"], [*argv, "--mode", mode])
        expected = public_view.read_bytes(recipe_prefix + "/representation-projections/" + recipe["label"] + ".json")
        require(raw == expected, "public frame view differs: " + recipe["label"])
        projections.append({"label": recipe["label"], "frame_indexes": selected,
                            "mode": mode, "sha256": check.sha256(raw), "byte_equal": True})
    require(len(projections) == 8, "complete selected view population missing")
    record.update(status="valid", observed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        identities=identities, source_install=installation,
        source_verify={"valid": verification["valid"], "manifest_sha256": verification["manifest_sha256"], "failures": verification["failures"]},
        complete_content_failures=failures, child_inventories={name: manifest["products"][name]["subject"] for name in ("axiom_indexer", "stdo_representation")},
        installed_manager={"version": manager_location["version"], "root": str(package_root), "members": package_members},
        reproduced_map_sha256=check.sha256(regenerated.read_bytes()), validation_report_sha256=check.sha256(report),
        projections=projections, native_execution_claimed=False, consumer_adoption_performed=False)
except Exception as error:
    record["failure"] = str(error)
    raise
finally:
    write_json(OUT / "public-reacquisition-commands.json", sorted(commands, key=lambda row: row["started_at"]))
    write_json(OUT / "public-reacquisition.json", record)
print(json.dumps({"status": record["status"], "revision": revision,
                  "source_manifest_sha256": expected_manifest, "reproduced_views": len(projections)}))

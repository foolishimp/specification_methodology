"""Replay the actual historical ABI mismatch in an isolated consumer only."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import unquote, urldefrag

PROJECT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(PROJECT / "src"))
from stdo_toolchain.store import Store


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--abi", required=True, type=Path)
    parser.add_argument("--repository", required=True, type=Path)
    parser.add_argument("--installed-store", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    candidate_paths = ["src/stdo_toolchain/cohort_update.py", "src/stdo_toolchain/cohort_assets.py",
                       "src/stdo_toolchain/cli.py", "tests/test_cohort_update.py",
                       "specification/PRODUCT.md", "specification/standards/SPEC_METHOD.md",
                       "design/TOOLCHAIN_MANAGER.md"]
    candidate_before = {path: digest(PROJECT / path) for path in candidate_paths}
    historical = args.abi / ".ai-workspace/context/axiomatic/history/20260905T025248Z-pre-rc4-adoption"
    context = Path(".ai-workspace/context/axiomatic")
    names = ["axiomatic-program.json", "logical-constraint-map.json", "bindings.json"]
    inputs = [args.abi / "stdo_abiogenesis.json", historical / "operation-record.json",
              historical / "preimages/stdo_abiogenesis.json"]
    inputs += [base / context / name for base in [args.abi, historical / "preimages"] for name in names]
    before = {str(path): digest(path) for path in inputs}
    operation = json.loads((historical / "operation-record.json").read_text())
    native_routes = [Path(f".{host}/skills/{skill}") for host in ["agents", "claude"]
                     for skill in ["axiomatize-corpus", "stdo-representation"]]
    development_routes = [Path(".genesis/development-products") / name for name in ["axiom-indexer", "stdo-representation"]]
    live_links = {str(path): os.readlink(args.abi / path) for path in native_routes + development_routes}
    env = {**os.environ, "PYTHONPATH": str(PROJECT / "src")}
    commands = []
    def command(label, argv, expected):
        completed = subprocess.run([sys.executable, "-m", "stdo_toolchain.cli", *argv],
                                   env=env, capture_output=True, text=True)
        commands.append({"label": label, "argv": completed.args, "exit_code": completed.returncode})
        (args.output / (label + ".stdout.json")).write_text(completed.stdout)
        (args.output / (label + ".stderr.txt")).write_text(completed.stderr)
        if completed.returncode != expected:
            raise RuntimeError(f"{label}: expected {expected}, got {completed.returncode}; retained stdout/stderr in {args.output}")
        return json.loads(completed.stdout)
    with tempfile.TemporaryDirectory(prefix="t029-actual-rc4-") as temporary:
        root = Path(temporary).resolve()
        consumer = root / "consumer"
        consumer.mkdir()
        definition = consumer / "stdo_abiogenesis.json"
        shutil.copyfile(historical / "preimages/stdo_abiogenesis.json", definition)
        for path in development_routes:
            target = operation["preimages"][path.as_posix()]["target"]
            local = consumer / path
            local.parent.mkdir(parents=True, exist_ok=True)
            local.symlink_to(target)
        for path in native_routes:
            local = consumer / path
            local.parent.mkdir(parents=True, exist_ok=True)
            local.symlink_to(live_links[str(path)])
        for name in names:
            target = consumer / context / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(historical / "preimages" / context / name, target)
        status = command("historical-basis-status", ["--store", str(args.installed_store), "status", "--definition", str(definition), "--verify"], 0)
        if not status["valid"]:
            raise RuntimeError("Historical RC4 basis did not reproduce valid status")
        current = json.loads((args.abi / "stdo_abiogenesis.json").read_text())
        composition = {row["target_definition_id"]: row for row in current["composition"]}
        tag = "refs/tags/stdo_representation/v2.5.0-rc.4"
        tag_object = subprocess.run(["git", "rev-parse", tag], cwd=args.repository, capture_output=True, text=True, check=True).stdout.strip()
        selection = {"kind": "stdo.cohort-update-selection", "schema_version": 1,
                     "definition_id": current["product"]["definition_id"],
                     "cohort": {"repository": str(args.repository), "ref": tag,
                                "tag_object": tag_object, "path": "stack_release.json"},
                     "companions": [], "derived_context": [{"program": str(context / names[0]), "map": str(context / names[1]), "bindings": str(context / names[2])}]}
        for product, definition_member, label, skill in [
                ("axiom_indexer", "stdo_default.json", "axiom-indexer", "axiomatize-corpus"),
                ("stdo_representation", "stdo_representation.json", "stdo-representation", "stdo-representation")]:
            selected = composition["urn:stdo:product-definition:" + label]
            selection["companions"].append({"product": product, "definition_member": definition_member,
                "target_definition_id": selected["target_definition_id"], "product_definition": selected["product_definition"],
                "contracts": selected["contracts"], "install_root": str(root / "companions" / product / "v2.5.0-rc.4"),
                "links": [{"path": ".genesis/development-products/" + label, "member": "."}] +
                         [{"path": f".{host}/skills/{skill}", "member": "skills/" + skill} for host in ["agents", "claude"]]})
        selection_path = root / "selection.json"
        write(selection_path, selection)
        write(args.output / "selection.json", selection)
        common = ["--store", str(args.installed_store), "cohort-update", "--definition", str(definition), "--selection", str(selection_path)]
        old_definition = definition.read_bytes()
        old_links = {str(p): os.readlink(consumer / p) for p in native_routes + development_routes}
        held = command("historical-complete-held", [*common, "--dry-run"], 1)
        command("historical-complete-refused", [*common, "--accept-plan-sha256", held["plan_sha256"]], 2)
        if definition.read_bytes() != old_definition or old_links != {str(p): os.readlink(consumer / p) for p in native_routes + development_routes} or (root / "companions").exists():
            raise RuntimeError("Held update changed isolated consumer state")
        # The source owner already supplied this newer program/map. The updater
        # consumes the recorded bytes; it does not produce or reclassify them.
        for name in names:
            shutil.copyfile(args.abi / context / name, consumer / context / name)
        current_held = command("current-owner-context-plan", [*common, "--dry-run"], 1)
        command("current-owner-context-refused", [*common, "--accept-plan-sha256", current_held["plan_sha256"]], 2)
        # A separate positive fixture binds the unchanged authored program/map
        # to the exact recorded source bytes. This is not current ABI readiness.
        snapshot = root / "accepted-source-snapshot"
        source_preimages = []
        mapping = json.loads((consumer / context / names[1]).read_text())
        for item in mapping["resolved_sources"]:
            uri, _ = urldefrag(item["uri"])
            if not uri.startswith("repo://abiogenesis/"):
                continue
            relative = Path(unquote(uri[len("repo://abiogenesis/"):]))
            candidates = [historical / "preimages" / relative, args.abi / relative]
            source = next((path for path in candidates if path.is_file() and "sha256:" + digest(path) == item["sha256"]), None)
            if source is None:
                raise RuntimeError(f"No retained exact source preimage for isolated positive fixture: {uri}")
            before[str(source)] = digest(source)
            destination = snapshot / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
            source_preimages.append({"uri": item["uri"], "input": str(source), "sha256": digest(source)})
        bindings_path = consumer / context / names[2]
        bindings = json.loads(bindings_path.read_text())
        for row in bindings["bindings"]:
            if row["uri_prefix"] == "repo://abiogenesis/":
                row["path"] = str(snapshot)
        write(bindings_path, bindings)
        temporary_store = Store(root / "stdo-store")
        temporary_store.install(str(args.repository), "v2.5.0-rc.4", expected_manifest_sha256="4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e")
        common[1] = str(temporary_store.root)
        ready = command("archived-source-snapshot-plan", [*common, "--dry-run"], 0)
        applied = command("isolated-exact-rc4-complete", [*common, "--accept-plan-sha256", ready["plan_sha256"]], 0)
        if not applied["complete"] or applied["target"]["manifest_sha256"] != "4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e":
            raise RuntimeError("Exact isolated complete update failed")
        source_bytes_preserved = all((consumer / context / name).read_bytes() == (args.abi / context / name).read_bytes() for name in names[:2])
        route_members = {str(path): digest(consumer / path / "SKILL.md") for path in native_routes}
    after = {path: digest(Path(path)) for path in before}
    if before != after or live_links != {str(p): os.readlink(args.abi / p) for p in native_routes + development_routes}:
        raise RuntimeError("Read-only ABI subject drifted during replay")
    candidate_after = {path: digest(PROJECT / path) for path in candidate_paths}
    if candidate_before != candidate_after:
        raise RuntimeError("Candidate changed during replay")
    write(args.output / "result.json", {"kind": "stdo.t029.isolated-actual-release-replay", "commands": commands,
        "candidate_files_before": candidate_before, "candidate_files_after": candidate_after,
        "source_files_before": before, "source_files_after": after, "live_links_unchanged": live_links,
        "historical_stdo_status_valid": status["valid"], "historical_complete_held": held["holds"],
        "current_abi_context_held": current_held["holds"], "positive_fixture_source_preimages": source_preimages,
        "positive_fixture_scope": "Exact retained source snapshot with unchanged authored program/map and an isolated physical source binding; not current ABI readiness",
        "isolated_rc4_complete": applied["complete"], "native_skill_members": route_members,
        "semantic_carriers_preserved": source_bytes_preserved, "actual_consumer_effects": []})
    print(json.dumps({"result": str(args.output / "result.json"), "isolated_complete": True, "actual_consumer_effects": []}))


if __name__ == "__main__":
    main()

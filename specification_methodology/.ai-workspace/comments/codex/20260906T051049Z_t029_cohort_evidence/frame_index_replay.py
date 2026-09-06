"""Join the exact T009 source candidate to the shared updater evidence adapter.

This is isolated source-candidate qualification, not release or consumer adoption.
The complete operation and consumer effects are covered by the retained cohort
replay and the adapter regression test; this replay exercises the actual new
authored program/map against their complete retained source bytes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
from urllib.parse import unquote, urldefrag

PROJECT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(PROJECT / "src"))
from stdo_toolchain.cohort_update import _axiom_digest, _derived
from stdo_toolchain.git_source import GitSnapshot


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--construction-subject", type=Path,
                        help="Explicit successor construction manifest; defaults to the original run-002 subject")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    repository = PROJECT.parent
    proof = repository / "stdo_representation/dogfood/t009-frame-projection"
    subject = (args.construction_subject or proof / "run-002/construction-subject.json").resolve()
    run2 = subject.parent
    manifest = json.loads(subject.read_text())
    program_input = (run2 / manifest["program_file"]).resolve()
    map_input = (run2 / manifest["map_file"]).resolve()
    bindings_input = (run2 / manifest["bindings_file"]).resolve()
    source_directory = (run2 / manifest["source_manifest_file"]).resolve().parent
    inputs = [subject, program_input, map_input, bindings_input]
    inputs += sorted(path for path in source_directory.rglob("*") if path.is_file())
    inputs += [PROJECT / "src/stdo_toolchain/cohort_update.py"]
    before = {str(path.relative_to(repository)): digest(path) for path in inputs}
    for relative, expected in manifest["files"].items():
        if digest(run2 / relative) != expected:
            raise RuntimeError("Frozen construction subject drift: " + relative)
    observations = []
    with tempfile.TemporaryDirectory(prefix="t029-frame-index-join-") as temporary:
        root = Path(temporary).resolve()
        consumer = root / "isolated-consumer"
        consumer.mkdir()
        shutil.copytree(source_directory, root / "source")
        shutil.copyfile(program_input, consumer / "program.json")
        shutil.copyfile(map_input, consumer / "map.json")
        bindings = json.loads(bindings_input.read_text())
        bindings["bindings"][0]["path"] = str(root / "source")
        write(consumer / "bindings.json", bindings)
        program = json.loads((consumer / "program.json").read_text())
        mapping = json.loads((consumer / "map.json").read_text())
        selected = [{"program": "program.json", "map": "map.json", "bindings": "bindings.json"}]
        with GitSnapshot(str(repository), "v2.5.0-rc.4") as source:
            def evaluate(label, expected_hold=None):
                observed, holds = _derived(consumer, selected, source, (consumer / "definition.json", b"{}\n"))
                if expected_hold is None and (holds or len(observed) != 1):
                    raise RuntimeError(f"{label}: unexpected join refusal {holds}")
                if expected_hold is not None and (observed or not any(expected_hold in value for value in holds)):
                    raise RuntimeError(f"{label}: missing expected refusal {holds}")
                observations.append({"case": label, "observations": observed, "holds": holds})

            evaluate("exact-97-clause-two-frame-source-candidate")
            frame_uri = program["frame_indexes"][0]["source_refs"][0]
            base = urldefrag(frame_uri)[0]
            prefix = bindings["bindings"][0]["uri_prefix"]
            target = root / "source" / unquote(base.removeprefix(prefix))
            original = target.read_bytes()
            target.write_bytes(original + b"\nChanged isolated source observation.\n")
            evaluate("changed-frame-source", "Stale derived source digest")
            mapping["resolved_sources"] = [row for row in mapping["resolved_sources"] if urldefrag(row["uri"])[0] != base]
            mapping["source_routes"] = {uri: [ref for ref in refs if urldefrag(ref)[0] != base]
                                        for uri, refs in mapping["source_routes"].items()}
            mapping["map_sha256"] = _axiom_digest({key: value for key, value in mapping.items() if key != "map_sha256"})
            write(consumer / "map.json", mapping)
            evaluate("omitted-frame-source-routes-and-evidence", "Missing declared derived source coverage")
            target.write_bytes(original)
            shutil.copyfile(map_input, consumer / "map.json")
            evaluate("restored-exact-candidate")
            immutable_basis = {"ref": source.ref, "tag_object": source.tag_object, "commit": source.commit}
    after = {str(path.relative_to(repository)): digest(path) for path in inputs}
    if before != after:
        raise RuntimeError("Source or implementation changed during replay")
    result = {"kind": "stdo.t029.frame-index-source-adapter-qualification", "inputs_before": before,
              "inputs_after": after, "immutable_basis": immutable_basis, "cases": observations,
              "source_release": None, "consumer_effects": [],
              "scope": "Actual T009 source candidate and shared updater evidence adapter; complete update effects remain bounded by the separate retained operation evidence."}
    write(args.output / "result.json", result)
    print(json.dumps({"result": str(args.output / "result.json"), "cases_passed": len(observations), "consumer_effects": []}))


if __name__ == "__main__":
    main()

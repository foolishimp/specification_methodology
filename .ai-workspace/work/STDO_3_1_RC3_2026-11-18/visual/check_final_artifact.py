#!/usr/bin/env python3
"""Finite Writer checks on the real final-native-bound visual artifact."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ARTIFACT = ROOT / "stdo_representation/build_tenants/a_c/representation/stdo-v3.1.0-rc.3"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as h:
        h.write(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact", type=Path, default=ARTIFACT)
    parser.add_argument("--evidence-name", default="final-checks-001")
    args = parser.parse_args()
    artifact = args.artifact.resolve()
    evidence = HERE / args.evidence_name
    evidence.mkdir(exist_ok=False)
    providers = {}
    for name in ("a_c", "axiom_indexer"):
        manifest_path = ROOT / name / "PUBLIC_MANIFEST.json"
        doc = json.loads(manifest_path.read_text())
        assert doc["version"] == "3.1.0-rc.3"
        for member in doc["files"]:
            raw = (ROOT / name / member["path"]).read_bytes()
            assert sha(raw) == member["sha256"] and len(raw) == member["bytes"]
        providers[name] = {"public_manifest_sha256": sha(manifest_path.read_bytes()), "version": doc["version"], "members": doc["files"]}
    save(evidence / "PROVIDERS.json", providers)
    n = 0

    def command(label, argv, expected=0):
        nonlocal n
        n += 1
        p = subprocess.run(argv, capture_output=True, text=True)
        result = {"argv": [str(x) for x in argv], "exit_code": p.returncode,
                  "stdout": p.stdout, "stderr": p.stderr, "expected_exit_code": expected}
        save(evidence / (str(n).zfill(2) + "-" + label + ".json"), result)
        if p.returncode != expected:
            raise ValueError(label + " unexpected result; original evidence retained")
        return result

    ac = [sys.executable, "-B", str(ROOT / "a_c/scripts/ac.py")]
    proposal = artifact / "run/generation/proposal"
    model_path = proposal / "model.json"
    carrier_path = proposal / "carrier.json"
    model = json.loads(model_path.read_text())
    binding = json.loads((artifact / "SOURCE_BINDING.json").read_text())
    generated = json.loads((artifact / "GENERATION.json").read_text())
    native_raw = (artifact / "source/manifest.json").read_bytes()
    assert sha(native_raw) == binding["represented_source"]["manifest_sha256"]
    assert generated["source_binding_sha256"] == sha((artifact / "SOURCE_BINDING.json").read_bytes())
    assert generated["represented_source"] == binding["represented_source"]
    assert generated["model"]["id"] == model["id"]
    command("validate-model", ac + ["graph", "validate", str(model_path)])
    command("decode-carrier", ac + ["graph", "decode", str(carrier_path), "--out", str(evidence / "decoded-model.json")])
    constraints = model["populations"]["constraints"]
    chosen = next(row for row in constraints if row["predicate"]["statement"].startswith("Where the selected envelope declares context capacity"))
    inspected = command("inspect-condition-exception", ac + ["graph", "inspect", str(carrier_path), chosen["id"]])
    assert "Where no capacity is declared" in inspected["stdout"]
    assert "selected envelope declares context capacity" in inspected["stdout"]

    sys.path.insert(0, str(ROOT / "a_c/build_tenants/graphify/code"))
    import ac_graph
    import ac_explore
    assert ac_graph.decode(ac_graph.GraphCarrier(json.loads(carrier_path.read_text()))).document == model
    view = ac_explore.view_data(model, artifact / "run/generation/corpus")
    for row in generated["native_member_mapping"]:
        assert view["sources"][row["project_source_path"]]["sha256"] == row["sha256"]
        assert sha((artifact / "source" / row["native_member_path"]).read_bytes()) == row["sha256"]
    grounds = list(ac_explore.groundings(model))
    for ground in grounds:
        source = view["sources"][ground["path"]]["text"]
        span = "\n".join(source.splitlines()[ground["start_line"] - 1:ground["end_line"]])
        assert ground["quote"] in span, ground
    recipe = json.loads((ROOT / "stdo_representation/scripts/visual_31_rc3_annotations.json").read_text())
    answer = json.loads((artifact / "authoring/ANSWER.json").read_text())
    assert all(row["decision"] == "residual" and row["keys"] for row in answer["dispositions"])
    assert len(recipe["annotations"]) == 24
    assert len(view["sources"]) == 3
    html = (proposal / "explorer.html").read_text()
    assert '<script src=' not in html and '<iframe' not in html

    # Refuse stale reuse against a disposable copied selected source. The native
    # installation and retained generated corpus are never changed.
    source = artifact / "source/standards/SDLC_DEFAULTS.md"
    before = source.read_bytes()
    try:
        source.write_bytes(before + b"\n<!-- Controlled stale-input check. -->\n")
        failure = command("stale-source-refusal", ac + ["project", "status", "--run", str(artifact / "run")], 2)
        assert "selected source changed" in failure["stderr"]
    finally:
        source.write_bytes(before)
    assert sha(source.read_bytes()) == sha(before)
    command("restored-source-status", ac + ["project", "status", "--run", str(artifact / "run")])

    # Axiom conversion uses the exact native URI for the copied source members.
    axiom = ROOT / "axiom_indexer/build_tenants/core/code"
    out = artifact / "axiom"
    save(out / "PROVIDER.json", providers["axiom_indexer"])
    uri = "stdo://releases/v3.1.0-rc.3/"
    source_prefix = str((artifact / "source").relative_to(ROOT / "stdo_representation")) + "/"
    config = {"program_uri": "urn:stdo-representation:visual:3.1.0-rc.3:program",
        "source_basis": uri, "calculus_ref": uri + "standards/AXIOMATIC_CALCULUS.md",
        "metadata_source_ref": uri + "manifest.json",
        "source_mappings": [{"path_prefix": source_prefix, "uri_prefix": uri}],
        "frame_indexes": [{"uri": "urn:stdo-representation:visual:3.1.0-rc.3:selected-context-condition",
            "frame_ref": uri + "standards/SDLC_DEFAULTS.md",
            "scope": "Inspect the declared conditional context-fit annotation and its source-linked closure; no semantic acceptance.",
            "clause_refs": [chosen["id"]], "residual_refs": [],
            "source_refs": [uri + "standards/SDLC_DEFAULTS.md"]}]}
    save(out / "conversion-config.json", config)
    save(out / "bindings.json", {"kind": "axiom-indexer.binding-set", "schema_version": 1,
        "bindings": [{"uri_prefix": uri, "path": "../source"}]})
    command("axiom-convert", [sys.executable, "-B", str(axiom / "ac_model.py"), "convert",
        "--model", str(model_path), "--config", str(out / "conversion-config.json"),
        "--output", str(out / "program.json"), "--receipt", str(out / "conversion-receipt.json")])
    command("axiom-restore", [sys.executable, "-B", str(axiom / "ac_model.py"), "restore",
        "--program", str(out / "program.json"), "--output", str(out / "restored-model.json")])
    assert json.loads((out / "restored-model.json").read_text()) == model
    command("axiom-validate", [sys.executable, "-B", str(axiom / "ac.py"), "validate",
        "--program", str(out / "program.json"), "--bindings", str(out / "bindings.json"),
        "--output", str(out / "validation.json"), "--emit-map", str(out / "map.json")])
    command("axiom-project", [sys.executable, "-B", str(axiom / "ac.py"), "project",
        "--program", str(out / "program.json"), "--bindings", str(out / "bindings.json"),
        "--map", str(out / "map.json"), "--frame-index", config["frame_indexes"][0]["uri"],
        "--mode", "materialized", "--output", str(out / "selected-projection.json")])
    save(evidence / "RESULT.json", {"profile": "stdo.visual-finite-writer-checks/1",
        "model_file_sha256": sha(model_path.read_bytes()),
        "model_identity": model["id"], "source_files": len(view["sources"]),
        "grounding_occurrences_checked": len(grounds), "section_dispositions": len(answer["dispositions"]),
        "records": sum(len(x) for x in model["populations"].values()),
        "checks": ["public model/carrier validation", "exact carrier/model value equality",
            "public full-record condition and exception inspection", "every declared source quote resolves",
            "every selected section has an explicit residual disposition", "offline HTML embeds its sources and scripts",
            "stale copied-source refusal and exact restored status", "Axiom convert/restore exact value preservation",
            "Axiom public source validation and selected materialized projection"],
        "source_restored_sha256": sha(source.read_bytes()),
        "limits": ["Writer evidence, not independent source fidelity or acceptance",
                   "No whole-method semantic coverage, external Graphify execution, Lean or subject-code execution"]})
    print(json.dumps({"status": "passed", "evidence": str(evidence)}))


if __name__ == "__main__":
    main()

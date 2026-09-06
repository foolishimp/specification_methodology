"""Construct the bounded RC6 index only after exact commit-A Install handoff.

Run with --install-record, --install-root and --manifest-sha256 from that
handoff. This reproducer authors one declared Executive constraint/index;
it neither selects a caller's frame nor accepts or publishes any Product.
"""
from pathlib import Path
import argparse
import difflib
import hashlib
import json
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[5]
PROOF = Path(__file__).resolve().parent
REP = ROOT / "stdo_representation"
PREVIOUS = REP / "build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.5"
TARGET = REP / "build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.6"
OLD_PREFIX = "stdo://releases/v2.5.0-rc.5/"
NEW_PREFIX = "stdo://releases/v2.5.0-rc.6/"
CLAUSE = "urn:stdo-representation:a-c-text:clause:"
VOCAB = "urn:stdo-representation:vocabulary:"
NEW_CLAUSE = CLAUSE + "executive-steel-thread-delivery"
NEW_INDEX = "urn:stdo-representation:frame-index:executive-steel-thread-delivery"
BASELINE = NEW_PREFIX + "standards/STDO_REFERENCE_FRAME_BASELINE.md"
MECHANIC = ROOT / "axiom_indexer/build_tenants/core/code/ac.py"
EXPECTED_SOURCES = {
    "STDO_REFERENCE_FRAME_BASELINE.md": "3cfb24f507e6746d5263c7b866d2cd4dc4de2d9caf52bb7e90b9f66642208bf0",
    "authority_compressions/stdo_compressed.md": "c67213649da7ab2b2a7c7a785b071e76c804d974de20a4247c18a1233fcb47c5",
    "authority_compressions/stdo_bootstrap.md": "060b18aaaa81f7fe4670e5c0b8dedf21a71d130dc9edbe7933635ab665adfe13",
}
EXPECTED_MECHANICS = {
    "build_tenants/core/code/ac.py": "87c43389c619d9ca0e2d930a10e471a17545be9a0394d1c0f47db7e8e2c6d931",
    "skills/axiomatize-corpus/references/program.schema.json": "43326dbab520bd2d56fbdf605211f66499de1969b13e2e0226868bd6af9777a7",
    "skills/axiomatize-corpus/references/output-contract.md": "c124264d1fc564a8a054bba46b5c188c4e770da51862b4c2122e3c616efb1b6b",
}
PREVIOUS_NATIVE = {
    "SKILL.md": "79d9c2e0ce9d02435c755b9a598da66ef8f0c0937a72ac4bb481b4729ca8f86f",
    "references/frame-index-use.md": "236c728b9ee1749f1b758f6ea5bb82de037737d0281c6979bd19eea7bcc203c6",
    "references/codex.md": "4ddbe37bda55a3c8f9e8545f391a906754067ffc49d2d6f0299eae2d41559497",
    "references/claude.md": "584189012cb0c414392e381969a9b02eda2c3cae826cd310218d92a1a3212c20",
}


def require(condition, detail):
    if not condition:
        raise ValueError(detail)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def sha(path):
    return digest(path.read_bytes())


def load(path):
    return json.loads(path.read_text())


def put(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def rewrite(value, old, new):
    if isinstance(value, str):
        return value.replace(old, new)
    if isinstance(value, list):
        return [rewrite(v, old, new) for v in value]
    if isinstance(value, dict):
        return {k: rewrite(v, old, new) for k, v in value.items()}
    return value


def semantic_addition():
    statement = (
        "When Executive coordination is selected for delivery, establish early or extend the smallest real runnable supported-entry-to-outcome thread through the selected composition. "
        "Choose bounded increments by consequential uncertainty, dependency/interface reach and failure impact. Early end-to-end and integration evidence prunes incompatible construction choices, settles only exercised interfaces and preserves working composition. "
        "A passing thread supports only exercised relations and conditions; material untested branches, combinations, refusals and recovery retain their proof obligations. Revisit settled construction decisions when material counterevidence invalidates their basis. "
        "During construction use focused deterministic regression and targeted judgment probes. Keep module-derived unit evidence for module-owned laws and its smallest congruent population. Schedule substantial resource-intensive UAT near release or when a bounded capability is complete enough to qualify; use an early focused user probe when it decides material outcome uncertainty. "
        "The testing frames retain distinct user-outcome, authoritative runnable-path, composition and module-law claims and govern necessary scenarios, independence and repetitions. Reuse qualified exact-subject/basis results while valid and rerun affected assurance after material invalidation. Existing mandates and operation grants govern all activation and effects."
    )
    arguments = [
        {"role": VOCAB + "role:subject", "ref": "urn:stdo-representation:a-c-text:symbol:executive"},
        {"role": VOCAB + "role:requirement", "literal": statement},
        {"role": VOCAB + "role:condition", "ref": CLAUSE + "engagement-return-topology"},
        {"role": VOCAB + "role:support", "ref": CLAUSE + "executive-mutation-needs-prior-writer-transition"},
        {"role": VOCAB + "role:support", "ref": CLAUSE + "closed-result-reuse-preserves-required-independence"},
        {"role": VOCAB + "role:support", "ref": CLAUSE + "closure-reuse-retains-independent-progress"},
        {"role": VOCAB + "role:qualification", "literal": "This delivery sequence does not appoint Executive for sufficient direct Writer work, waive a module-derived unit lane, infer task applicability, supply a universal repeat count or cost gate, or expand the existing operation grant."},
    ]
    sources = sorted(BASELINE + fragment for fragment in (
        "#steel-thread-delivery", "#engagement-applicability",
        "#derived-product-testing-frame-set", "#derived-unit-test-frame",
    ))
    clause = {"uri": NEW_CLAUSE, "clause_type": "constraint",
              "operator": VOCAB + "operator:requires", "arguments": arguments,
              "statement": statement, "source_refs": sources}
    index = {
        "uri": NEW_INDEX, "frame_ref": BASELINE + "#derived-executive-frame",
        "scope": "Sequence an explicitly selected coordinated Product-delivery outcome under its existing Executive mandate, using an early real steel thread and claim-bound assurance. This index does not select Executive for direct Writer work, provide task facts or acceptance, or grant construction effects.",
        "clause_refs": [NEW_CLAUSE],
        "residual_refs": [
            "urn:stdo-representation:a-c-text:residual:frame-adoption-not-claimed",
            "urn:stdo-representation:a-c-text:residual:task-frame-obligations-require-owned-applicability",
        ],
        "source_refs": sorted(set(sources + [BASELINE + "#derived-executive-frame"])),
    }
    return clause, index


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--install-record", required=True, type=Path)
    parser.add_argument("--install-root", required=True, type=Path)
    parser.add_argument("--manifest-sha256", required=True)
    args = parser.parse_args()
    require(args.install_record.is_file(), "Actual commit-A stdo-install.json is required")
    receipt = load(args.install_record)
    install = args.install_root.resolve(strict=True)
    manifest_path = install / "manifest.json"
    require(sha(manifest_path) == args.manifest_sha256, "Installed manifest differs from the exact handoff")
    manifest = load(manifest_path)
    require(receipt["status"] == "installed" and receipt["uri"] == NEW_PREFIX, "Wrong installed receipt subject")
    require(Path(receipt["path"]).resolve(strict=True) == install, "Receipt names another Install")
    require(receipt["manifest_sha256"] == args.manifest_sha256 and receipt["release"] == manifest["release"], "Receipt/manifest identity mismatch")
    require(all(receipt["standards"][k] == manifest["standards"][k] for k in ["member_count", "member_set_sha256"]), "Receipt source inventory mismatch")
    require(manifest["release"]["cut"] == "v2.5.0-rc.6", "The Install is not RC6")
    require(manifest["release"]["qualified_ref"] == "refs/tags/specification_methodology/v2.5.0-rc.6", "Wrong source-cut owner/ref")
    require(not TARGET.exists(), "RC6 target already exists; preserve the prior candidate")
    require(sha(PREVIOUS / "axiomatic-program.json") == "933f72d9f6c13969b3705d69ea555e713120fa3d7abef6b90629b4a91ca0fb74", "RC5 program drift")
    require(sha(PREVIOUS / "source-corpus.json") == "bd37ab41762017d96121439397d9bff6912eda5b84257873b9915f087f4d3342", "RC5 source-corpus drift")
    for path, expected in EXPECTED_MECHANICS.items():
        require(sha(ROOT / "axiom_indexer" / path) == expected, "Mechanical dependency drift: " + path)
    standards = install / manifest["standards"]["installed_root"]
    members = manifest["standards"]["members"]
    paths = [m["path"] for m in members]
    actual_paths = sorted(p.relative_to(standards).as_posix() for p in standards.rglob("*") if p.is_file() or p.is_symlink())
    require(paths == sorted(set(paths)) == actual_paths, "Source member inventory is not exact")
    require(len(members) == manifest["standards"]["member_count"], "Source member count mismatch")
    for row in members:
        require(sha(standards / row["path"]) == row["sha256"], "Source member drift: " + row["path"])
    old_members = {m["path"]: m["sha256"] for m in load(PREVIOUS / "source-corpus.json")["source_release"]["standards_members"]}
    current_members = {m["path"]: m["sha256"] for m in members}
    require(old_members.keys() == current_members.keys(), "Unexpected source membership change")
    changed = {p: h for p, h in current_members.items() if old_members[p] != h}
    require(changed == EXPECTED_SOURCES, "Source changes exceed the reviewed steel-thread amendment")
    native_delta = {}
    for path, before_sha in PREVIOUS_NATIVE.items():
        current = (REP / "skills/stdo-representation" / path).read_text()
        previous = current.replace("v2.5.0-rc.6", "v2.5.0-rc.5").replace("RC6", "RC5")
        require(digest(previous.encode()) == before_sha, "Native instructions changed beyond exact selection routes: " + path)
        native_delta[path] = {"before_sha256": before_sha, "after_sha256": digest(current.encode()),
                              "inverse_route_transform_equals_predecessor": True,
                              "diff": "".join(difflib.unified_diff(previous.splitlines(True), current.splitlines(True), fromfile=path + "@RC5", tofile=path + "@RC6"))}

    old = load(PREVIOUS / "axiomatic-program.json")
    program = rewrite(old, OLD_PREFIX, NEW_PREFIX)
    program["uri"] = "urn:stdo-representation:program:a-c-text:stdo-v2.5.0-rc.6"
    clause, index = semantic_addition()
    program["clauses"] = sorted(program["clauses"] + [clause], key=lambda x: x["uri"])
    program["frame_indexes"] = sorted(program["frame_indexes"] + [index], key=lambda x: x["uri"])
    restored = rewrite(program, NEW_PREFIX, OLD_PREFIX)
    restored["uri"] = old["uri"]
    restored["clauses"] = [c for c in restored["clauses"] if c["uri"] != NEW_CLAUSE]
    restored["frame_indexes"] = [i for i in restored["frame_indexes"] if i["uri"] != NEW_INDEX]
    require(restored == old, "Unrelated authored content changed")
    require(OLD_PREFIX not in json.dumps(program), "RC5 source routes remain in the RC6 candidate")

    bindings = PROOF / "representation-rc6-bindings.json"
    put(TARGET / "axiomatic-program.json", program)
    put(bindings, {"kind": "axiom-indexer.binding-set", "schema_version": 1,
                   "bindings": [{"uri_prefix": NEW_PREFIX, "path": str(install)}]})
    commands = []

    def run(label, arguments):
        argv = [sys.executable, "-B", str(MECHANIC), *arguments]
        result = subprocess.run(argv, capture_output=True, text=True)
        commands.append({"label": label, "argv": argv, "exit_code": result.returncode})
        (PROOF / f"representation-index-{label}.stdout.txt").write_text(result.stdout)
        (PROOF / f"representation-index-{label}.stderr.txt").write_text(result.stderr)
        put(PROOF / "representation-index-commands.json", commands)
        require(result.returncode == 0, f"{label}: {result.stderr or result.stdout}")

    common = ["--program", str(TARGET / "axiomatic-program.json"), "--bindings", str(bindings)]
    run("validate", ["validate", *common, "--output", str(TARGET / "validation-report.json"), "--emit-map", str(TARGET / "logical-constraint-map.json")])
    selections = {"worker": ["urn:stdo-representation:frame-index:t009:complete-update-worker"],
                  "reviewer": ["urn:stdo-representation:frame-index:t009:complete-update-reviewer"],
                  "executive": [NEW_INDEX]}
    selections["combined"] = selections["worker"] + selections["reviewer"]
    for name, selected in selections.items():
        for mode in ["reference-only", "materialized"]:
            output = PROOF / "representation-projections" / f"{name}-{mode}.json"
            output.parent.mkdir(exist_ok=True)
            flags = [part for uri in selected for part in ["--frame-index", uri]]
            run(f"{name}-{mode}", ["project", *common, "--map", str(TARGET / "logical-constraint-map.json"), *flags, "--mode", mode, "--output", str(output)])
    release = dict(manifest["release"])
    release.update({"uri": NEW_PREFIX, "installed_manifest_sha256": sha(manifest_path),
                    "standards_member_count": len(members), "standards_member_set_sha256": manifest["standards"]["member_set_sha256"], "standards_members": members})
    put(TARGET / "source-corpus.json", {"kind": "stdo-representation.source-corpus", "schema_version": 1,
                                      "representation_version": "2.5.0-rc.6", "source_release": release})
    put(PROOF / "representation-index-conservation.json", {
        "kind": "stdo.rc6-index-conservation", "install_record": str(args.install_record),
        "install_record_sha256": sha(args.install_record), "installed_manifest_sha256": sha(manifest_path),
        "predecessor_program_sha256": sha(PREVIOUS / "axiomatic-program.json"),
        "source_changes": changed, "unchanged_source_members": len(members) - len(changed),
        "source_uri_rebinding": {"from": OLD_PREFIX, "to": NEW_PREFIX},
        "new_clause": clause, "new_frame_index": index,
        "inverse_transform_without_additions_equals_predecessor": restored == old,
        "preserved_prior_clauses": len(old["clauses"]), "preserved_prior_frame_indexes": len(old["frame_indexes"]),
        "mechanical_dependency": EXPECTED_MECHANICS, "native_selection_route_delta": native_delta,
        "generated_files": {str(p.relative_to(ROOT)): sha(p) for p in sorted(TARGET.iterdir()) if p.is_file()},
        "claim": "Bounded construction and mechanical evidence; independent semantic comparison and release disposition remain external.",
    })
    print(json.dumps({"program_sha256": sha(TARGET / "axiomatic-program.json"),
                      "map_sha256": sha(TARGET / "logical-constraint-map.json"),
                      "source_members": len(members), "projections": 8, "candidate_ready": True}))


if __name__ == "__main__":
    main()

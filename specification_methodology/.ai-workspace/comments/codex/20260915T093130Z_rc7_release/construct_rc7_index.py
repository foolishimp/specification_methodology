"""Construct the bounded RC7 index only after exact commit-A Install handoff.

Run with --install-record, --install-root and --manifest-sha256 from that
handoff. This adapter serializes three Writer-authored attention constraints and one index;
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
PREVIOUS = REP / "build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.6"
TARGET = REP / "build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.7"
OLD_PREFIX = "stdo://releases/v2.5.0-rc.6/"
NEW_PREFIX = "stdo://releases/v2.5.0-rc.7/"
CLAUSE = "urn:stdo-representation:a-c-text:clause:"
VOCAB = "urn:stdo-representation:vocabulary:"
NEW_CLAUSE = CLAUSE + "executive-event-driven-attention"
NEW_INDEX = "urn:stdo-representation:frame-index:executive-event-driven-attention"
BASELINE = NEW_PREFIX + "standards/STDO_REFERENCE_FRAME_BASELINE.md"
MECHANIC = ROOT / "axiom_indexer/build_tenants/core/code/ac.py"
EXPECTED_SOURCES = {
    "STDO_REFERENCE_FRAME_BASELINE.md": "234172dd0d403d28a3fdee9dfe740ba35b1c7656e92c249aa6f70af67c408ee1",
    "authority_compressions/stdo_compressed.md": "8d30240a4d1323d838aad19051326ec6126040313f580c5a7ebeb8c146d56fcf",
    "authority_compressions/stdo_bootstrap.md": "9542d4c95dba044a08e2f17b84a3b6ab513fac6d96b7600a32baa45646c8d410",
}
EXPECTED_MECHANICS = {
    "build_tenants/core/code/ac.py": "87c43389c619d9ca0e2d930a10e471a17545be9a0394d1c0f47db7e8e2c6d931",
    "skills/axiomatize-corpus/references/program.schema.json": "43326dbab520bd2d56fbdf605211f66499de1969b13e2e0226868bd6af9777a7",
    "skills/axiomatize-corpus/references/output-contract.md": "c124264d1fc564a8a054bba46b5c188c4e770da51862b4c2122e3c616efb1b6b",
}
PREVIOUS_NATIVE = {
    "SKILL.md": "424785112fb70e9f0c0c484a2a074d6ecfd8f9478f33a6960b7ca86968c3828d",
    "references/frame-index-use.md": "0e5ed60300e4355856df04b46760944827b77329f80d40600a4ebf014dc950c0",
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
    # These are Writer-authored source interpretations, not extracted by code.
    fallback = CLAUSE + "executive-bounded-fallback-observation"
    reassess = CLAUSE + "executive-no-progress-reassessment"
    def authored(uri, statement, links, fragments):
        return {"uri": uri, "clause_type": "constraint",
                "operator": VOCAB + "operator:requires",
                "arguments": [
                    {"role": VOCAB + "role:subject", "ref": "urn:stdo-representation:a-c-text:symbol:executive"},
                    {"role": VOCAB + "role:requirement", "literal": statement},
                    *[{"role": VOCAB + "role:" + role, "ref": ref} for role, ref in links]],
                "statement": statement,
                "source_refs": sorted(BASELINE + fragment for fragment in fragments)}
    attention = authored(NEW_CLAUSE,
        "When Executive coordination is selected, attention is event-driven by default: re-enter for a decision-relevant closed return, material exception or changed basis, owner request, or declared deadline/checkpoint. While Workers perform bounded grants and no other authorized decision is ready, wait rather than repeatedly inspecting unfinished work, replaying unchanged judgments or seeking status without a decision need. Retain the frontier, return conditions and valid evidence; refresh affected support on material invalidation and revalidate all Executive drift locks before activation and disposition. Waiting preserves current-workspace verification, evidence validity, required independent assessment, closed-return consumption and every authority/closure duty.",
        [("condition", CLAUSE + "engagement-return-topology"),
         ("exception", fallback), ("support", reassess),
         ("support", CLAUSE + "computed-result-reuse-invalidates-affected-dependencies"),
         ("support", CLAUSE + "closed-result-reuse-preserves-required-independence"),
         ("support", CLAUSE + "closure-is-satisfied-obligations-not-review-occurrence"),
         ("support", CLAUSE + "executive-mutation-needs-prior-writer-transition")],
        ["#event-driven-executive-attention", "#executive-drift-locks", "#product-chain-basis", "#complete-engagement-transition"])
    observation = authored(fallback,
        "When notification is unavailable or unreliable, or an actual supervision obligation requires observation, use bounded fallback observation with a declared purpose, cadence or checkpoint, evidence target and stop/escalation condition. Silence proves neither progress nor failure; unknown status alone does not establish a stalled Worker. Investigate a genuine blocker or material risk and intervene when required within existing grants. Reliable notification does not waive an actual supervision duty, and observation or intervention cannot widen write territory or other authority.",
        [("support", CLAUSE + "engagement-return-topology"),
         ("support", CLAUSE + "executive-mutation-needs-prior-writer-transition")],
        ["#event-driven-executive-attention", "#executive-drift-locks"])
    no_progress = authored(reassess,
        "Repeated no-progress observations or returns without new decision-relevant evidence require bounded reassessment of the frame, grant, dependency or evidence gap and a decision under existing authority. Do not continue polling or repeat the same repair on an unchanged basis. Reduced reasoning churn neither lowers assurance nor permits reduced required actor capability, and introduces no universal cost, budget or accounting gate.",
        [("support", CLAUSE + "engagement-return-topology"),
         ("support", CLAUSE + "closed-result-reuse-preserves-required-independence"),
         ("support", CLAUSE + "required-frame-conjunction-retains-every-constraint")],
        ["#event-driven-executive-attention", "#executive-drift-locks"])
    index = {
        "uri": NEW_INDEX, "frame_ref": BASELINE + "#derived-executive-frame",
        "scope": "Manage attention and consume results for an explicitly selected Executive outcome under existing authority: wait during ordinary in-grant progress, respond to decision-relevant events, preserve bounded fallback supervision and reassess repeated no-progress. Current evidence, required independent assessment and lawful closure remain required. This index neither appoints Executive, provides task facts nor grants effects.",
        "clause_refs": [NEW_CLAUSE],
        "residual_refs": [
            "urn:stdo-representation:a-c-text:residual:frame-adoption-not-claimed",
            "urn:stdo-representation:a-c-text:residual:task-frame-obligations-require-owned-applicability"],
        "source_refs": sorted([BASELINE + "#derived-executive-frame", BASELINE + "#event-driven-executive-attention", BASELINE + "#executive-drift-locks", BASELINE + "#product-chain-basis"]),
    }
    return [attention, observation, no_progress], index


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
    require(manifest["release"]["cut"] == "v2.5.0-rc.7", "The Install is not RC7")
    require(manifest["release"]["qualified_ref"] == "refs/tags/specification_methodology/v2.5.0-rc.7", "Wrong source-cut owner/ref")
    require(not TARGET.exists(), "RC7 target already exists; preserve the prior candidate")
    require(sha(PREVIOUS / "axiomatic-program.json") == "ea68d04a125e7a7035759b69dba063cd86dd72c0438254c7fabfee8134f0fc9e", "RC6 program drift")
    require(sha(PREVIOUS / "source-corpus.json") == "d79c4d97336c062ad58a677b3c304acfc218b30d5040ee723170243ca9ef2efb", "RC6 source-corpus drift")
    prior_cohort = load(ROOT / "stack_release.json")
    axiom_subject = prior_cohort["products"]["axiom_indexer"]["subject"]
    require(axiom_subject["member_count"] == 7, "Expected complete seven-member mechanics")
    for member in axiom_subject["members"]:
        path = ROOT / "axiom_indexer" / member["path"]
        content = str(path.readlink()).encode() if member["type"] == "symlink" else path.read_bytes()
        require(digest(content) == member["sha256"], "Axiom full member drift: " + member["path"])
    put(PROOF / "axiom-construction-subject.json", axiom_subject)
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
    require(changed == EXPECTED_SOURCES, "Source changes exceed the reviewed event-driven amendment")
    native_delta = {}
    for path, before_sha in PREVIOUS_NATIVE.items():
        current = (REP / "skills/stdo-representation" / path).read_text()
        previous = current.replace("v2.5.0-rc.7", "v2.5.0-rc.6").replace("RC7", "RC6")
        require(digest(previous.encode()) == before_sha, "Native instructions changed beyond exact selection routes: " + path)
        native_delta[path] = {"before_sha256": before_sha, "after_sha256": digest(current.encode()),
                              "inverse_route_transform_equals_predecessor": True,
                              "diff": "".join(difflib.unified_diff(previous.splitlines(True), current.splitlines(True), fromfile=path + "@RC6", tofile=path + "@RC7"))}

    old = load(PREVIOUS / "axiomatic-program.json")
    program = rewrite(old, OLD_PREFIX, NEW_PREFIX)
    program["uri"] = "urn:stdo-representation:program:a-c-text:stdo-v2.5.0-rc.7"
    clauses, index = semantic_addition()
    program["clauses"] = sorted(program["clauses"] + clauses, key=lambda x: x["uri"])
    program["frame_indexes"] = sorted(program["frame_indexes"] + [index], key=lambda x: x["uri"])
    steel = next(c for c in program["clauses"] if c["uri"] == CLAUSE + "executive-steel-thread-delivery")
    steel["arguments"].append({"role": VOCAB + "role:support", "ref": NEW_CLAUSE})
    restored = rewrite(program, NEW_PREFIX, OLD_PREFIX)
    restored["uri"] = old["uri"]
    restored["clauses"] = [c for c in restored["clauses"] if c["uri"] not in {c["uri"] for c in clauses}]
    restored["frame_indexes"] = [i for i in restored["frame_indexes"] if i["uri"] != NEW_INDEX]
    prior_steel = next(c for c in restored["clauses"] if c["uri"] == CLAUSE + "executive-steel-thread-delivery")
    require(prior_steel["arguments"].pop() == {"role": VOCAB + "role:support", "ref": NEW_CLAUSE}, "Steel support bridge drift")
    require(restored == old, "Unrelated authored content changed")
    require(OLD_PREFIX not in json.dumps(program), "RC6 source routes remain in the RC7 candidate")

    bindings = PROOF / "representation-rc7-bindings.json"
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
                  "executive": [NEW_INDEX],
                  "steel": ["urn:stdo-representation:frame-index:executive-steel-thread-delivery"]}
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
                                      "representation_version": "2.5.0-rc.7", "source_release": release})
    put(PROOF / "representation-index-conservation.json", {
        "kind": "stdo.rc7-index-conservation", "install_record": str(args.install_record),
        "install_record_sha256": sha(args.install_record), "installed_manifest_sha256": sha(manifest_path),
        "predecessor_program_sha256": sha(PREVIOUS / "axiomatic-program.json"),
        "source_changes": changed, "unchanged_source_members": len(members) - len(changed),
        "source_uri_rebinding": {"from": OLD_PREFIX, "to": NEW_PREFIX},
        "new_clauses": clauses, "new_frame_index": index,
        "changed_existing_support": {"clause": steel["uri"], "added_support": NEW_CLAUSE, "statement_conserved": True},
        "inverse_transform_without_additions_equals_predecessor": restored == old,
        "preserved_prior_clauses": len(old["clauses"]) - 1, "preserved_prior_frame_indexes": len(old["frame_indexes"]),
        "mechanical_dependency": EXPECTED_MECHANICS, "native_selection_route_delta": native_delta,
        "generated_files": {str(p.relative_to(ROOT)): sha(p) for p in sorted(TARGET.iterdir()) if p.is_file()},
        "claim": "Bounded construction and mechanical evidence; independent semantic comparison and release disposition remain external.",
    })
    print(json.dumps({"program_sha256": sha(TARGET / "axiomatic-program.json"),
                      "map_sha256": sha(TARGET / "logical-constraint-map.json"),
                      "source_members": len(members), "projections": 10, "candidate_ready": True}))


if __name__ == "__main__":
    main()


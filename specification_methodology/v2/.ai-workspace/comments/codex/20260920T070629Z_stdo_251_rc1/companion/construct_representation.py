"""Serialize an explicitly authored semantic delta against a frozen RC1 Install.

No source interpretation, frame selection, Product acceptance, Git or provider
effect is performed by this helper. All changed semantics are supplied in the
Writer-authored delta; unchanged preimage rows are mechanically conserved.
"""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys

OUT = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[6]
OLD = "stdo://releases/v2.5.0-rc.7/"
NEW = "stdo://releases/v2.5.1-rc.1/"
PREVIOUS_REL = "stdo_representation/build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.7"
TARGET = ROOT / "stdo_representation/build_tenants/axiom_indexer/representation/stdo-v2.5.1-rc.1"
MECHANIC = ROOT / "axiom_indexer/build_tenants/core/code/ac.py"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    content = str(path.readlink()).encode() if path.is_symlink() else path.read_bytes()
    return hashlib.sha256(content).hexdigest()


def load(path):
    return json.loads(path.read_text())


def put(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def rebind(value):
    if isinstance(value, str):
        return value.replace(OLD, NEW)
    if isinstance(value, list):
        return [rebind(v) for v in value]
    if isinstance(value, dict):
        return {k: rebind(v) for k, v in value.items()}
    return value


def check_axiom(preimage):
    subject = preimage["axiom_product"]
    require(subject["member_count"] == len(subject["members"]) == 7,
            "The preserved generic Product must contain its seven members")
    for row in subject["members"]:
        path = ROOT / "axiom_indexer" / row["path"]
        require(sha(path) == row["sha256"], "Generic Axiom member changed: " + row["path"])
    return subject


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--install-record", required=True, type=Path)
    parser.add_argument("--install-root", required=True, type=Path)
    parser.add_argument("--manifest-sha256", required=True)
    parser.add_argument("--delta", required=True, type=Path)
    args = parser.parse_args()
    preimage = load(OUT / "preimage.json")
    axiom_subject = check_axiom(preimage)
    receipt = load(args.install_record)
    install = args.install_root.resolve(strict=True)
    manifest_path = install / "manifest.json"
    manifest = load(manifest_path)
    require(sha(manifest_path) == args.manifest_sha256, "Wrong frozen manifest")
    require(receipt["status"] == "installed" and receipt["uri"] == NEW,
            "Wrong install receipt subject")
    require(Path(receipt["path"]).resolve(strict=True) == install,
            "Receipt names another Install")
    require(receipt["manifest_sha256"] == args.manifest_sha256 and
            receipt["release"] == manifest["release"], "Receipt/manifest identity mismatch")
    require(manifest["release"]["cut"] == "v2.5.1-rc.1" and
            manifest["release"]["qualified_ref"] == "refs/tags/specification_methodology/v2.5.1-rc.1",
            "Wrong cut or release owner")
    require(not TARGET.exists(), "Preserve the existing RC1 candidate")
    standards = install / manifest["standards"]["installed_root"]
    members = manifest["standards"]["members"]
    paths = [m["path"] for m in members]
    actual = sorted(p.relative_to(standards).as_posix() for p in standards.rglob("*")
                    if p.is_file() or p.is_symlink())
    require(paths == sorted(set(paths)) == actual, "Source member set is not exact")
    require(len(members) == manifest["standards"]["member_count"], "Wrong source member count")
    for row in members:
        require(sha(standards / row["path"]) == row["sha256"], "Changed source member: " + row["path"])
    previous = ROOT / PREVIOUS_REL
    for row in preimage["files"]:
        if row["path"].startswith(PREVIOUS_REL + "/"):
            require(sha(ROOT / row["path"]) == row["sha256"], "Historical artifact drift")
    old_program = load(previous / "axiomatic-program.json")
    old_members = {m["path"]: m["sha256"] for m in
                   load(previous / "source-corpus.json")["source_release"]["standards_members"]}
    current_members = {m["path"]: m["sha256"] for m in members}
    changed_sources = {p: {"before_sha256": old_members.get(p), "after_sha256": current_members.get(p)}
                       for p in sorted(old_members.keys() | current_members.keys())
                       if old_members.get(p) != current_members.get(p)}
    delta = load(args.delta)
    require(delta["installed_manifest_sha256"] == args.manifest_sha256,
            "Authored delta names another frozen source")
    require(delta["source_changes"] == changed_sources, "Authored source-delta coverage differs")
    require(set(delta["source_assessments"]) == set(changed_sources),
            "Every changed source member needs its authored disposition")
    program = rebind(old_program)
    program["uri"] = "urn:stdo-representation:program:a-c-text:stdo-v2.5.1-rc.1"
    conservation = {}
    for collection in ("symbols", "clauses", "residuals", "frame_indexes"):
        rows = {row["uri"]: row for row in program.get(collection, [])}
        old_rows = dict(rows)
        replacements = delta.get("replace_" + collection, [])
        additions = delta.get("add_" + collection, [])
        require(len({r["uri"] for r in replacements + additions}) == len(replacements + additions),
                "Duplicate authored change in " + collection)
        for row in replacements:
            require(row["uri"] in rows, "Replacement target absent: " + row["uri"])
            require(row != rows[row["uri"]], "Replacement contains no change: " + row["uri"])
            rows[row["uri"]] = row
        for row in additions:
            require(row["uri"] not in rows, "Addition already exists: " + row["uri"])
            rows[row["uri"]] = row
        changed_uris = {r["uri"] for r in replacements}
        unchanged = [uri for uri, row in old_rows.items() if uri not in changed_uris]
        require(all(rows[uri] == old_rows[uri] for uri in unchanged),
                "Unrelated authored row changed")
        program[collection] = sorted(rows.values(), key=lambda row: row["uri"])
        conservation[collection] = {"unchanged_after_source_uri_rebinding": unchanged,
                                    "replaced": sorted(changed_uris),
                                    "added": sorted(r["uri"] for r in additions)}
    for field in ("frame_refs", "vocabulary_refs"):
        additions = delta.get("add_" + field, [])
        require(not set(additions) & set(program[field]), "Added URI already declared")
        program[field] = sorted(set(program[field]) | set(additions))
    require(OLD not in json.dumps(program), "Old source routes remain in the candidate")
    require(all(c["statement"] in [a.get("literal") for a in c["arguments"]]
                for c in delta.get("replace_clauses", []) + delta.get("add_clauses", [])),
            "Changed clause statement and executable operand disagree")
    bindings = OUT / "rc1-bindings.json"
    put(bindings, {"kind": "axiom-indexer.binding-set", "schema_version": 1,
                   "bindings": [{"uri_prefix": NEW, "path": str(install)}]})
    put(TARGET / "axiomatic-program.json", program)
    commands = []

    def run(label, arguments):
        argv = [sys.executable, "-B", str(MECHANIC), *arguments]
        result = subprocess.run(argv, capture_output=True, text=True)
        commands.append({"label": label, "argv": argv, "exit_code": result.returncode})
        (OUT / f"{label}.stdout.txt").write_text(result.stdout)
        (OUT / f"{label}.stderr.txt").write_text(result.stderr)
        put(OUT / "construction-commands.json", commands)
        require(result.returncode == 0, label + ": " + (result.stderr or result.stdout))

    common = ["--program", str(TARGET / "axiomatic-program.json"), "--bindings", str(bindings)]
    run("validate", ["validate", *common, "--output", str(TARGET / "validation-report.json"),
                     "--emit-map", str(TARGET / "logical-constraint-map.json")])
    # Select explicit authored indexes. Both views must carry the same closure.
    selections = {index["uri"].rsplit(":", 1)[-1]: [index["uri"]]
                  for index in program["frame_indexes"]}
    require(len(selections) == len(program["frame_indexes"]), "Projection label collision")
    selections.update(delta.get("combined_projection_selections", {}))
    projections = []
    for label, selected in selections.items():
        views = {}
        for mode in ("reference-only", "materialized"):
            output = OUT / "projections" / f"{label}-{mode}.json"
            output.parent.mkdir(exist_ok=True)
            flags = [v for uri in selected for v in ("--frame-index", uri)]
            run(f"project-{label}-{mode}", ["project", *common, "--map",
                str(TARGET / "logical-constraint-map.json"), *flags, "--mode", mode,
                "--output", str(output)])
            views[mode] = load(output)
            projections.append({"path": str(output.relative_to(ROOT)), "sha256": sha(output)})
        require(views["reference-only"]["closure"] == views["materialized"]["closure"],
                "Projection modes disagree on closure: " + label)
    run("reproduce", ["validate", *common, "--output", str(OUT / "reproduced-report.json"),
                      "--emit-map", str(OUT / "reproduced-map.json")])
    require((OUT / "reproduced-map.json").read_bytes() ==
            (TARGET / "logical-constraint-map.json").read_bytes(), "Map replay differs")
    require((OUT / "reproduced-report.json").read_bytes() ==
            (TARGET / "validation-report.json").read_bytes(), "Report replay differs")
    release = dict(manifest["release"])
    release.update({"uri": NEW, "installed_manifest_sha256": sha(manifest_path),
                    "standards_member_count": len(members),
                    "standards_member_set_sha256": manifest["standards"]["member_set_sha256"],
                    "standards_members": members})
    put(TARGET / "source-corpus.json", {"kind": "stdo-representation.source-corpus", "schema_version": 1,
                                      "representation_version": "2.5.1-rc.1", "source_release": release})
    check_axiom(preimage)
    put(OUT / "construction-conservation.json", {
        "kind": "stdo.rc1-companion-conservation", "schema_version": 1,
        "install_record": str(args.install_record), "install_record_sha256": sha(args.install_record),
        "installed_manifest_sha256": sha(manifest_path), "authored_delta_sha256": sha(args.delta),
        "predecessor_program_sha256": sha(previous / "axiomatic-program.json"),
        "source_changes": changed_sources, "authored_content": conservation,
        "all_seven_axiom_members_preserved": axiom_subject,
        "report_and_map_reproduced_byte_identically": True,
        "projections": projections,
        "generated_files": {str(p.relative_to(ROOT)): sha(p) for p in sorted(TARGET.iterdir()) if p.is_file()},
        "claim": "Exact construction and mechanical reproduction only. Independent source fidelity, native usefulness and configuration disposition remain separate."
    })
    print(json.dumps({"target": str(TARGET.relative_to(ROOT)),
                      "program_sha256": sha(TARGET / "axiomatic-program.json"),
                      "map_sha256": sha(TARGET / "logical-constraint-map.json"),
                      "clauses": len(program["clauses"]), "indexes": len(program["frame_indexes"]),
                      "projections": len(projections)}))


if __name__ == "__main__":
    main()

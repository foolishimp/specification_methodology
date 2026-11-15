"""Bind RC2 visual publication members after actual native-bound generation."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PRODUCT = ROOT / "stdo_representation"
OLD = "3.1.0-rc.1"
NEW = "3.1.0-rc.2"
OLD_REL = f"build_tenants/a_c/representation/stdo-v{OLD}"
NEW_REL = f"build_tenants/a_c/representation/stdo-v{NEW}"
old = PRODUCT / OLD_REL
new = PRODUCT / NEW_REL


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def inventory(root, paths):
    return [{"path": p, "sha256": sha(root / p), "bytes": (root / p).stat().st_size}
            for p in sorted(paths)]


def main():
    checks = HERE / "final-checks-001"
    assert (checks / "RESULT.json").is_file(), "Wait for the completed artifact check before freezing membership"
    check_commands = sorted(checks.glob("[0-9]*.json"))
    assert len(check_commands) == 9
    assert all(read(p)["exit_code"] == read(p)["expected_exit_code"] for p in check_commands)
    binding = read(new / "SOURCE_BINDING.json")
    generation = read(new / "GENERATION.json")
    assert binding["version"] == NEW
    assert binding["represented_source"]["uri"] == f"stdo://releases/v{NEW}/"
    assert generation["source_binding_sha256"] == sha(new / "SOURCE_BINDING.json")
    native = binding["represented_source"]
    recipe_old = read(PRODUCT / "scripts/visual_31_annotations.json")
    recipe_new = read(PRODUCT / "scripts/visual_31_rc2_annotations.json")
    assert {k: v for k, v in recipe_old.items() if k != "source_cut"} == {
        k: v for k, v in recipe_new.items() if k != "source_cut"}
    source_comparison = []
    for row in binding["selected_native_members"]:
        before, after = old / "source" / row["path"], new / "source" / row["path"]
        assert before.read_bytes() == after.read_bytes()
        source_comparison.append({"path": row["path"], "sha256": sha(after),
                                  "byte_equal_to_predecessor": True})

    old_model = read(old / "run/generation/proposal/model.json")
    new_model = read(new / "run/generation/proposal/model.json")
    assert old_model["populations"].keys() == new_model["populations"].keys()
    identity_map = {}
    for family, values in old_model["populations"].items():
        successor = new_model["populations"][family]
        assert len(values) == len(successor)
        for a, b in zip(values, successor):
            identity_map[a["id"]] = b["id"]
    assert len(set(identity_map.values())) == len(identity_map)
    old_namespace = old_model["id"].split(":model:")[0]
    new_namespace = new_model["id"].split(":model:")[0]
    old_subject = old_model["basis"]["subject"]["id"]
    new_subject = new_model["basis"]["subject"]["id"]

    def normalize(value):
        if isinstance(value, str):
            return identity_map.get(value, value).replace(old_namespace, new_namespace).replace(
                old_subject, new_subject).replace(OLD, NEW)
        if isinstance(value, list):
            return [normalize(x) for x in value]
        if isinstance(value, dict):
            return {normalize(k): normalize(v) for k, v in value.items()}
        return value

    comparisons = {
        "populations": normalize(old_model["populations"]) == new_model["populations"],
        "signature_definition": normalize(old_model["signature"]["definition"]) == new_model["signature"]["definition"],
        "source_inventory": normalize(old_model["basis"]["subject"]["inventory"]) == new_model["basis"]["subject"]["inventory"],
        "dispositions": normalize(old_model["interpretation"]["dispositions"]) == new_model["interpretation"]["dispositions"],
        "dependency_contract": normalize(old_model["dependency_contract"]) == new_model["dependency_contract"],
        "empty_functor_bindings": old_model["functor_bindings"] == new_model["functor_bindings"] == {},
    }
    assert all(comparisons.values()), comparisons
    save(HERE / "PREDECESSOR_COMPARISON.json", {
        "kind": "stdo.rc2-visual-predecessor-comparison/1",
        "predecessor": OLD, "successor": NEW,
        "selected_sources": source_comparison,
        "annotations_unchanged_except_declared_source_cut": True,
        "record_identity_bijection": identity_map,
        "normalization": {"generation_namespace": [old_namespace, new_namespace],
                          "source_subject": [old_subject, new_subject],
                          "release_source_path": [OLD, NEW]},
        "comparisons": comparisons,
        "standing": "Mechanical preservation of complete records, source selection, qualifications, directed references and residuals. Independent reuse applicability remains externally assessed; generated identity/provenance changes are explicit."})

    old_native = read(old / "SOURCE_BINDING.json")["represented_source"]
    text = (old / "README.md").read_text().replace(OLD, NEW)
    replacements = {
        old_native["manifest_sha256"]: native["manifest_sha256"],
        old_native["release"]["commit"]: native["release"]["commit"],
        old_native["release"]["tag_object"]: native["release"]["tag_object"],
        read(old / "GENERATION.json")["model"]["sha256"]: generation["model"]["sha256"],
        old_model["id"]: new_model["id"],
    }
    for before, after in replacements.items():
        text = text.replace(before, after)
    text = text.replace("fresh source-authored visual", "freshly regenerated visual")
    text = text.replace("The first independent source-fidelity assessment", "RC1's first independent source-fidelity assessment")
    text = text.replace("changed records require their own bounded independent recheck.",
                        "changed RC1 records received their own bounded independent recheck. RC2 retains those corrected annotation meanings and the same selected native member bytes; its new generated identities and source/provider bindings are checked explicitly.")
    (new / "README.md").write_text(text)
    (new / "COVERAGE.md").write_text((old / "COVERAGE.md").read_text().replace(
        "visual_31_annotations.json", "visual_31_rc2_annotations.json"))
    release = PRODUCT / f"releases/v{NEW}.md"
    release_prefix = release.read_text().split("\nThe current regenerated artifact binds native commit ", 1)[0]
    release.write_text(release_prefix + f"\nThe current regenerated artifact binds native commit `{native['release']['commit']}` and manifest `{native['manifest_sha256']}`. Its 93 section dispositions and 24 annotations retain 306 complete records. See the [current artifact](../{NEW_REL}/README.md) and the corrective release's exact predecessor comparison and independent reuse assessment.\n")

    manifest = read(PRODUCT / "PUBLIC_MANIFEST.json")
    assert manifest["version"] in {OLD, NEW}
    manifest.update(version=NEW, represented_source=native, model=generation["model"],
                    entrypoint=NEW_REL + "/run/generation/proposal/explorer.html",
                    regeneration="scripts/build_31_rc2_visual.py",
                    source_binding=NEW_REL + "/SOURCE_BINDING.json",
                    generation_binding=NEW_REL + "/GENERATION.json")
    manifest["scope"] = binding["scope"]
    manifest["limits"] = binding["limits"]
    for key, product in [("representation_tools", "a_c"), ("optional_axiom_conversion", "axiom_indexer")]:
        manifest["dependencies"][key]["version"] = NEW
        manifest["dependencies"][key]["public_manifest_sha256"] = sha(ROOT / product / "PUBLIC_MANIFEST.json")
    artifact_files = [p.relative_to(PRODUCT).as_posix() for p in new.rglob("*")
                      if p.is_file() and "__pycache__" not in p.parts and p.name != ".DS_Store"]
    public_paths = ["VERSION", "stdo_representation.json", "scripts/build_31_rc2_visual.py",
                    "scripts/visual_31_rc2_annotations.json", *artifact_files]
    manifest["files"] = inventory(PRODUCT, public_paths)
    save(PRODUCT / "PUBLIC_MANIFEST.json", manifest)

    selection = read(ROOT / ".ai-workspace/work/STDO_3_1_RELEASE_2026-11-15/visual/PACKAGE_SELECTION.json")
    selection["version"] = NEW
    selection["native_manifest_sha256"] = native["manifest_sha256"]
    selection["standing"] = "Exact RC2 visual Product members; unchanged selected source and annotation meaning with new native/provider bindings. Independent reuse applicability and release standing are external."
    for product, entry in selection["products"].items():
        paths = [p for p in entry["member_paths"] if not p.startswith(OLD_REL + "/")]
        paths = [p.replace(f"releases/v{OLD}.md", f"releases/v{NEW}.md").replace(
            "scripts/build_31_visual.py", "scripts/build_31_rc2_visual.py").replace(
            "scripts/visual_31_annotations.json", "scripts/visual_31_rc2_annotations.json") for p in paths]
        if product == "stdo_representation":
            paths.extend(artifact_files)
        entry["member_paths"] = sorted(paths)
        entry["members"] = inventory(ROOT / product, entry["member_paths"])
        entry["member_count"] = len(entry["members"])
        entry["inventory_sha256"] = hashlib.sha256(json.dumps(entry["members"], sort_keys=True,
            separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    save(HERE / "PACKAGE_SELECTION.json", selection)
    print(json.dumps({"public_manifests": {p: sha(ROOT / p / "PUBLIC_MANIFEST.json")
        for p in selection["products"]}, "members": {p: e["member_count"]
        for p, e in selection["products"].items()}, "comparisons": comparisons}, indent=2))


if __name__ == "__main__":
    main()

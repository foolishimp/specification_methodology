"""Read exact application/source commitments; no authority or semantic inference."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import re


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def digest(value):
    return sha(canonical(value))


def load(path):
    def pairs(items):
        value = {}
        for key, item in items:
            require(key not in value, "duplicate JSON key")
            value[key] = item
        return value
    def constant(value):
        raise ValueError("nonfinite JSON number: " + value)
    return json.loads(Path(path).read_bytes(), object_pairs_hook=pairs, parse_constant=constant)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)
        stream.write("\n")


def relative(value):
    require(isinstance(value, str), "path must be text")
    path = PurePosixPath(value)
    require(bool(value) and not path.is_absolute() and path.as_posix() == value
            and all(part not in ("", ".", "..") for part in path.parts)
            and "\\" not in value and "\0" not in value, "unsafe relative path")
    return value


def exact_file(root, name):
    path = Path(root)
    require(not path.is_symlink(), "redirected root")
    for part in PurePosixPath(relative(name)).parts:
        path /= part
        require(not path.is_symlink(), "redirected file component")
    require(path.is_file(), "missing file: " + name)
    return path


def files(root):
    root = Path(root)
    require(root.is_dir() and not root.is_symlink(), "missing or redirected directory")
    result = []
    for path in root.rglob("*"):
        require(not path.is_symlink(), "redirected directory member")
        if path.is_file():
            result.append(path.relative_to(root).as_posix())
        else:
            require(path.is_dir(), "unsupported directory member")
    return sorted(result)


def hex_digest(value, length=64):
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{%d}" % length, value) is not None and value != "0" * length


def selection_class(path):
    if path.startswith("standards/frames/"):
        return "derived_frames"
    if path.startswith("standards/") or (path.startswith("plugins/") and path.endswith(".md")):
        return "primary_semantic"
    return "host_legal_release_metadata"


def inventory_rows(rows):
    return [{key: row[key] for key in ("path", "bytes", "sha256")} for row in rows]


def check_frame_routes(members, frame_data):
    """Check exact frame/owner custody only, without a sufficiency judgment."""
    by_path = {row["path"]: row for row in members}
    require(isinstance(frame_data["frames"], list) and frame_data["frames"], "native frames are absent")
    require(len({frame["path"] for frame in frame_data["frames"]}) == len(frame_data["frames"]), "duplicate native frame path")
    bindings = 0
    for frame in frame_data["frames"]:
        require(selection_class(relative(frame["path"])) == "derived_frames" and frame["path"] in by_path, "frame outside frozen payload")
        member = by_path[frame["path"]]
        require(frame["sha256"] == member["sha256"] and frame["bytes"] == member["bytes"], "frame bytes differ")
        for route in frame.get("binds", []) + frame.get("routes", []):
            owner = route["owner"]
            require(selection_class(owner) == "primary_semantic" and owner in by_path
                    and route["owner_sha256"] == by_path[owner]["sha256"], "frame owner binding differs")
            require(bool(route["anchor"]) and hex_digest(route["section_sha256"]), "frame section binding incomplete")
            bindings += 1
    return bindings


def application(root):
    app = load(exact_file(root, "application.json"))
    require(app["kind"] == "a_c.stdo301.application/1", "unsupported application contract")
    require(app["represented_cut"] == "v3.0.1-rc.1", "different represented cut")
    require(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]+", app["artifact"]) is not None, "unsafe artifact name")
    require(app["builder"]["uri"] == "stdo://releases/v2.5.1-rc.2/", "builder adoption is outside this application")
    generation = app["generation"]
    require(generation["mode"] == "graphify-ac" and generation["jobs"] == 2
            and generation["max_calls_per_chunk"] == 3 and generation["initial_chunks"] == 2
            and generation["batch_chunks"] == 2 and generation["timeout_seconds"] == 1800,
            "bounded generation contract differs")
    require(generation["model"] == "gpt-6-astra" and generation["effort"] == "max"
            and generation["service_tier"] == "default", "owner-selected actor settings differ")
    return app


def implementation(root):
    manifest = load(exact_file(root, "implementation/manifest.json"))
    require(manifest["kind"] == "a_c.stdo301.unchanged-implementation/1", "implementation contract differs")
    expected = []
    for row in manifest["files"]:
        name = relative(row["path"])
        require(name.startswith("implementation/code/"), "implementation path escaped snapshot")
        raw = exact_file(root, name).read_bytes()
        require(len(raw) == row["bytes"] and sha(raw) == row["sha256"], "implementation snapshot changed: " + name)
        expected.append(name.removeprefix("implementation/code/"))
    require(sorted(set(expected)) == files(Path(root) / "implementation/code") and len(expected) == len(set(expected)),
            "implementation snapshot membership differs")
    return manifest


def frozen(root, expected_sha=None):
    root = Path(root)
    path = exact_file(root, "source-contract.json")
    if expected_sha is not None:
        require(hex_digest(expected_sha) and sha(path.read_bytes()) == expected_sha, "source-contract digest differs from grant")
    contract = load(path)
    require(contract["kind"] == "a_c.stdo301.frozen-source/1", "unsupported frozen-source contract")
    app = application(root)
    require(sha(exact_file(root, "application.json").read_bytes()) == contract["application_sha256"], "application changed after freeze")
    require(contract["artifact"] == app["artifact"] and contract["builder"] == app["builder"], "application/builder coordinate differs")
    require(contract["generation"] == app["generation"], "generation settings changed after freeze")
    for name, expected in contract["metadata_sha256"].items():
        require(sha(exact_file(root, name).read_bytes()) == expected, "frozen metadata changed: " + name)
    required = {"source-selection.json", "source-manifest.json", "source-classification.json", "package-custody.json",
                "release_tools/source-sections.json", "SOURCE-READINESS.md"}
    require(set(contract["metadata_sha256"]) == required, "frozen metadata population differs")
    require(hex_digest(contract["implementation_manifest_sha256"]), "missing exact implementation binding")
    # The distributed artifact carries its exact codec; authoring snapshots stay in the application.
    if (root / "implementation/manifest.json").exists():
        implementation(root)
        require(sha((root / "implementation/manifest.json").read_bytes()) == contract["implementation_manifest_sha256"], "implementation manifest changed")
    return contract


def check_sources(root, expected_sha=None):
    root = Path(root)
    contract = frozen(root, expected_sha)
    custody = load(root / "package-custody.json")
    semantic = load(root / "source-manifest.json")
    classes = load(root / "source-classification.json")
    selected = load(root / "source-selection.json")
    require(selected["kind"] == "a_c.stdo301.native-source-selection/1"
            and selected["native"]["cut"] == "v3.0.1-rc.1"
            and selected["standing"] == "test_candidate_not_accepted", "selected native contract differs")
    native = selected["native"]
    source = {"commit": native["commit"], "payload_commit": selected["source_candidate"]["commit"],
              "package_root": native["package_path"], "package_tree": native["package_tree"],
              "qualified_ref": native["qualified_ref"], "tag_object": native["tag_object"],
              "native_manifest_sha256": native["manifest_sha256"]}
    require(contract["source"] == source, "native/source-contract coordinates differ")
    require(custody["subject_id"] == semantic["subject_id"] == classes["subject_id"] == contract["subject_id"] == selected["subject_uri"], "subject coordinate differs")
    require(custody["source"] == semantic["source"] == classes["source"] == contract["source"], "source coordinate copies differ")
    members = custody["members"]
    paths = [relative(row["path"]) for row in members]
    require(paths == sorted(set(paths)) and bool(paths), "source order/uniqueness differs")
    require(members == selected["files"], "source selection members differ")
    require(files(root / "source") == paths, "source inventory has missing or extra files")
    for row in members:
        data = exact_file(root / "source", row["path"]).read_bytes()
        require(len(data) == row["bytes"] and sha(data) == row["sha256"], "source bytes changed: " + row["path"])
        require(hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest() == row["git_blob"], "source Git blob differs")
        require(row["git_mode"] in ("100644", "100755"), "unsupported source mode")
    total = sum(row["bytes"] for row in members)
    inventory = digest(inventory_rows(members))
    require(custody["member_count"] == selected["file_count"] == len(members)
            and custody["bytes"] == selected["total_bytes"] == total
            and custody["inventory_digest"] == selected["inventory_sha256"] == inventory, "full source extent differs")
    primary = [row for row in members if selection_class(row["path"]) == "primary_semantic"]
    require(semantic["files"] == primary and semantic["member_count"] == len(primary)
            and semantic["bytes"] == sum(row["bytes"] for row in primary)
            and semantic["inventory_digest"] == digest(inventory_rows(primary)), "semantic selection differs")
    for group in ("primary_semantic", "derived_frames", "host_legal_release_metadata"):
        rows = [row for row in members if selection_class(row["path"]) == group]
        require(classes["classes"][group] == {"member_count": len(rows), "bytes": sum(row["bytes"] for row in rows), "paths": [row["path"] for row in rows]}, "classification differs: " + group)
    frame_data = load(root / "source/standards/frames/FRAME_INPUTS.json")
    require(classes["derived_frame_sources"] == frame_data, "frame owner routes differ")
    bindings = check_frame_routes(members, frame_data)
    return {"files": len(members), "bytes": total, "semantic_files": len(primary), "frame_owner_bindings": bindings,
            "inventory_sha256": inventory, "claim": "Exact payload/selection/frame-owner custody; no frame semantic sufficiency or interpretation judgment."}

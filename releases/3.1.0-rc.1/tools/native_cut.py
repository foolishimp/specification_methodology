#!/usr/bin/env python3
"""Construct the selected immutable local native cut from committed source.

Uses the inventory/index-info/source-trailer relation of the archived
native_release.py. No legacy asset requirement, global install or publication.
"""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import os
import subprocess


def require(value, message):
    if not value:
        raise ValueError(message)


def git(repo, *args, data=None, env=None):
    result = subprocess.run(["git", "-C", str(repo), *args], input=data,
                            capture_output=True, env=env)
    require(result.returncode == 0, result.stderr.decode(errors="replace"))
    return result.stdout


def text_git(repo, *args):
    return git(repo, *args).decode().strip()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def save(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def tree_rows(repo, tree):
    rows = []
    for item in git(repo, "ls-tree", "-r", "-z", tree).split(b"\0"):
        if not item:
            continue
        metadata, path = item.split(b"\t", 1)
        mode, kind, blob = metadata.decode().split()
        name = path.decode()
        require(kind == "blob" and mode in {"100644", "100755"}, "Non-file member: " + name)
        require(not PurePosixPath(name).is_absolute() and
                all(part not in {".", ".."} for part in PurePosixPath(name).parts), "Unsafe member")
        raw = git(repo, "cat-file", "blob", blob)
        rows.append({"path": name, "git_mode": mode, "git_blob": blob,
                     "bytes": len(raw), "sha256": sha(raw)})
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--inventory-sha256", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    repo = args.repo.resolve(strict=True)
    config = json.loads((Path(__file__).parents[1] / "COHORT_INPUTS.json").read_text())
    require(config["version"] == "3.1.0-rc.1" and config["release_profile"] == "rc-six-product-v1",
            "Wrong selected release")
    raw = args.inventory.read_bytes()
    require(sha(raw) == args.inventory_sha256, "Native-ready inventory changed")
    expected = json.loads(raw)
    expected = expected.get("files", expected.get("members")) if isinstance(expected, dict) else expected
    source_commit = text_git(repo, "rev-parse", args.source_commit + "^{commit}")
    config_path = Path(__file__).parents[1] / "COHORT_INPUTS.json"
    require(git(repo, "show", source_commit + ":releases/3.1.0-rc.1/COHORT_INPUTS.json") ==
            config_path.read_bytes(), "Release selection differs from committed source")
    source_path = config["native_source"]
    source_tree = text_git(repo, "rev-parse", source_commit + ":" + source_path)
    rows = tree_rows(repo, source_tree)
    expected_map = {row["path"]: (row["sha256"], row["bytes"]) for row in expected}
    require(len(expected_map) == len(expected), "Duplicate expected member")
    require({row["path"]: (row["sha256"], row["bytes"]) for row in rows} == expected_map,
            "Committed native source differs from reviewed ready inventory")
    roots = {row["path"].split("/")[0] for row in rows}
    require(roots == {"LICENSE", "standards", "plugins", "release"}, "Unexpected native roots")
    require("release/release-note.md" in expected_map, "Release note absent")
    require(not any(row["path"].startswith("standards/documentation/proofs/") or
                    row["path"].startswith("standards/tooling/") for row in rows),
            "Retired native runtime found")
    predecessor = text_git(repo, "rev-parse", config["native_predecessor"] + "^{commit}")
    tag = "specification_methodology/v" + config["version"]
    exists = subprocess.run(["git", "-C", str(repo), "show-ref", "--verify", "--quiet",
                             "refs/tags/" + tag]).returncode
    require(exists == 1, "Selected immutable local tag already exists; reconcile")
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=False)
    prefix = config["native_subtree"]
    source = {"source_commit": source_commit, "source_path": source_path,
              "source_tree": source_tree, "predecessor": predecessor,
              "version": config["version"], "files": rows}
    save(out / "SOURCE.json", source)
    env = dict(os.environ, GIT_INDEX_FILE=str(out / "native.index"))
    git(repo, "read-tree", "--empty", env=env)
    info = b"".join(f"{row['git_mode']} {row['git_blob']}\t{prefix}/{row['path']}\0".encode()
                    for row in rows)
    git(repo, "update-index", "-z", "--index-info", data=info, env=env)
    tree = git(repo, "write-tree", env=env).decode().strip()
    trailers = (f"Frozen-Source-Commit: {source_commit}\nFrozen-Source-Path: {source_path}\n"
                f"Frozen-Source-Tree: {source_tree}\nPredecessor-Native-Commit: {predecessor}\n")
    message = f"STDO {config['version']} native release cut\n\n" + trailers
    native = git(repo, "commit-tree", tree, "-p", predecessor, data=message.encode()).decode().strip()
    require(text_git(repo, "show", "-s", "--format=%P", native) == predecessor, "Native parent differs")
    actual = tree_rows(repo, native)
    require(actual == [{**row, "path": prefix + "/" + row["path"]} for row in rows],
            "Native membership differs from frozen source")
    annotation = (f"STDO {config['version']}: six-Product cohort native RC cut\n\n" + trailers +
                  "STDO-Cohort-Profile: rc-six-product-v1\n"
                  "Scope: exact native Method/plugin; separately inventoried companion Products\n")
    annotation_path = out / "TAG_MESSAGE.txt"
    annotation_path.write_text(annotation)
    git(repo, "tag", "-a", tag, native, "-F", str(annotation_path))
    require(text_git(repo, "cat-file", "-t", "refs/tags/" + tag) == "tag", "Unannotated tag")
    require(text_git(repo, "rev-parse", tag + "^{commit}") == native, "Tag peel differs")
    value = {"profile": "stdo.native-local-cut/1", "standing": "local immutable subject; not published",
             "version": config["version"], "source_commit": source_commit, "source_path": source_path,
             "source_tree": source_tree, "native_commit": native, "native_tree": tree,
             "predecessor": predecessor, "tag": tag, "tag_object": text_git(repo, "rev-parse", tag),
             "subtree": prefix, "subtree_tree": text_git(repo, "rev-parse", native + ":" + prefix),
             "file_count": len(rows), "inventory_sha256": args.inventory_sha256,
             "source_record_sha256": sha((out / "SOURCE.json").read_bytes())}
    save(out / "NATIVE.json", value)
    print(json.dumps(value, indent=2))


if __name__ == "__main__":
    main()

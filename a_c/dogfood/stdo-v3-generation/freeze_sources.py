#!/usr/bin/env python3
"""Freeze the T-005 methodology inputs from immutable Git blobs.

No tenant worktree, prior interpretation, graph or study answer is an authoring
input. Existing snapshots are verified, never overwritten or re-blessed. The
custody verification hashes the original candidate's admitted members without
passing those excluded artifacts to generation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


SUBJECTS = {
    "codex": {
        "revision": "5a5b5ad80f0ba4b56b83aadd42ac130de53ba803",
        "checkpoint": "87512593de6ec60660f2ad9e040241d67a4108d7",
        "candidate_version": "3.0.0-rc.5",
        "source_root": "specification_methodology/v3/build_tenants/codex/successor/",
        "expected_files": 44,
        "candidate_manifest": "specification_methodology/v3/build_tenants/codex/qualification/C3/rc5/integration/CANDIDATE.json",
    },
    "claude": {
        "revision": "9aee01ffa76cfbde1a6b8f1153a25bd6d71c216e",
        "checkpoint": "1db13bfeb0675fc95de04aceccb214f5b76873fc",
        "candidate_version": "3.0.0-rc.8",
        "source_root": "specification_methodology/v3/build_tenants/claude/",
        "expected_files": 49,
        "candidate_manifest": "specification_methodology/v3/build_tenants/claude/release/manifest.json",
    },
}
EXCLUDED_STANDARD_DIRECTORIES = (
    "frames",
    "authority_compressions",
    "verification_material",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def document(value: object) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=True) + "\n").encode("utf-8")


def git(repository: Path, *arguments: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(repository), *arguments], stderr=subprocess.PIPE)


def blob(repository: Path, revision: str, path: str) -> bytes:
    return git(repository, "show", revision + ":" + path)


def tree_members(repository: Path, revision: str, root: str) -> list[dict]:
    members = []
    for item in git(repository, "ls-tree", "-rz", revision, root).split(b"\0"):
        if not item:
            continue
        metadata, encoded_path = item.split(b"\t", 1)
        mode, kind, oid = metadata.decode("ascii").split()
        require(kind == "blob" and mode in ("100644", "100755"), "non-regular source member")
        path = encoded_path.decode("utf-8")
        require(path.startswith(root), "source path escapes its root")
        members.append({"path": path, "git_blob": oid})
    return sorted(members, key=lambda member: member["path"])


def selected(relative: str) -> bool:
    return relative.startswith("standards/") and not any(
        relative.startswith("standards/" + directory + "/")
        for directory in EXCLUDED_STANDARD_DIRECTORIES
    )


def verify_manifest_members(repository: Path, revision: str, root: str, members: list[dict]) -> dict:
    paths = set()
    total_bytes = 0
    for member in members:
        path = member["path"]
        require(path not in paths, "duplicate admitted member: " + path)
        paths.add(path)
        data = blob(repository, revision, root + path)
        require(sha256(data) == member["sha256"], "candidate digest mismatch: " + path)
        require("bytes" not in member or len(data) == member["bytes"], "candidate byte count mismatch: " + path)
        total_bytes += len(data)
    return {"verified_members": len(members), "verified_bytes": total_bytes, "all_digests_match": True}


def custody(repository: Path, candidate: str, subject: dict) -> dict:
    cut = subject["revision"]
    checkpoint = subject["checkpoint"]
    root = subject["source_root"]
    subprocess.run(["git", "-C", str(repository), "merge-base", "--is-ancestor", cut, checkpoint], check=True)
    equivalence_roots = [root] if candidate == "codex" else [root + "standards/", root + "plugins/"]
    difference = git(repository, "diff", "--name-only", cut, checkpoint, "--", *equivalence_roots)
    require(not difference.strip(), "candidate source differs at custody checkpoint")
    # Each custody checkpoint records the manifest over its earlier source cut.
    manifest_revision = checkpoint
    raw = blob(repository, manifest_revision, subject["candidate_manifest"])
    manifest = json.loads(raw)
    result = {
        "revision": cut,
        "checkpoint": checkpoint,
        "source_root": root,
        "checkpoint_is_descendant": True,
        "source_equivalence_roots": equivalence_roots,
        "source_equivalent_at_checkpoint": True,
        "candidate_manifest": {
            "path": subject["candidate_manifest"],
            "revision": manifest_revision,
            "sha256": sha256(raw),
        },
        "standing": "Unaccepted candidate; source acquisition grants no methodology or semantic acceptance.",
    }
    if candidate == "codex":
        require(manifest["package_commit"] == cut, "Codex candidate package identity mismatch")
        require(manifest["candidate_version"] == subject["candidate_version"], "Codex candidate version mismatch")
        require(len(manifest["members"]) == 90, "Codex candidate admitted member count changed")
        result["candidate_members"] = verify_manifest_members(repository, cut, root, manifest["members"])
        result["source_commit"] = manifest["source_commit"]
        result["account_commit"] = manifest["account_commit"]
        result["package_tree"] = git(repository, "rev-parse", cut + ":" + root.rstrip("/")).decode().strip()
    else:
        release = manifest["release"]
        require(release["commit"] == cut, "Claude manifest source identity mismatch")
        require(release["cut"] == "v" + subject["candidate_version"], "Claude candidate version mismatch")
        require(release["project_subtree_root"] == root.rstrip("/"), "Claude subtree mismatch")
        for field, git_coordinate in (
            ("tree", cut + "^{tree}"),
            ("standards_tree", cut + ":" + root + "standards"),
            ("project_subtree_tree", cut + ":" + root.rstrip("/")),
        ):
            require(git(repository, "rev-parse", git_coordinate).decode().strip() == release[field], "Claude tree mismatch: " + field)
        tag_bytes = git(repository, "cat-file", "-p", release["tag_object"])
        require(tag_bytes.startswith(("object " + cut + "\ntype commit\n").encode()), "Claude tag object does not name source cut")
        standards = manifest["standards"]
        plugin = manifest["auxiliary"]["plugin"]
        require(standards["member_count"] == len(standards["members"]) == 62, "Claude standards member count changed")
        require(plugin["member_count"] == len(plugin["members"]) == 17, "Claude plugin member count changed")
        result["standards_members"] = verify_manifest_members(repository, cut, root + "standards/", standards["members"])
        result["plugin_members"] = verify_manifest_members(repository, cut, root + "plugins/spec/", plugin["members"])
        result["standards_tree"] = release["standards_tree"]
        result["tag_object"] = release["tag_object"]
        result["qualified_ref"] = release["qualified_ref"]
        result["tag_ref_role"] = "Historical locator only; verification uses the exact tag object, not a mutable ref."
    return result


def build(repository: Path) -> tuple[dict[str, bytes], dict]:
    outputs = {}
    results = {}
    for candidate, subject in SUBJECTS.items():
        root, cut = subject["source_root"], subject["revision"]
        files, excluded = [], []
        for member in tree_members(repository, cut, root + "standards/"):
            relative = member["path"][len(root):]
            if not selected(relative):
                excluded.append(relative)
                continue
            data = blob(repository, cut, member["path"])
            files.append({"path": relative, "bytes": len(data), "sha256": sha256(data), "git_blob": member["git_blob"]})
            outputs["corpora/" + candidate + "/source/" + relative] = data
        require(len(files) == subject["expected_files"], "selected source member count changed: " + candidate)
        content_inventory = [{key: member[key] for key in ("path", "bytes", "sha256")} for member in files]
        manifest = {
            "profile": "ac.generation.corpus/1",
            "subject_id": "repo://stdo-v3-generation/" + candidate + "/" + cut + "/",
            "candidate": candidate,
            "candidate_version": subject["candidate_version"],
            "revision": cut,
            "checkpoint": subject["checkpoint"],
            "source_root": root,
            "source_directory": "source",
            "selection": "All standards owner documents, schemas and templates; no existing interpretation or derived view.",
            "excluded_standard_directories": list(EXCLUDED_STANDARD_DIRECTORIES),
            "excluded_standard_members": excluded,
            "excluded_nonstandard_inputs": ["tenant README", "plugin interaction layer", "existing a_c/interpretation", "qualification and reviews", "compiler accounts and maps", "historical trial inputs and answers"],
            "file_count": len(files),
            "total_bytes": sum(member["bytes"] for member in files),
            "inventory_digest_encoding": "UTF-8 JSON files array, sorted object keys, compact separators, ensure_ascii=True, Git path order.",
            "input_corpus_sha256": sha256(canonical(files)),
            "content_inventory_sha256": sha256(canonical(content_inventory)),
            "files": files,
        }
        manifest_bytes = document(manifest)
        outputs["corpora/" + candidate + "/manifest.json"] = manifest_bytes
        results[candidate] = custody(repository, candidate, subject)
        results[candidate]["selected_input"] = {
            "manifest_path": "corpora/" + candidate + "/manifest.json",
            "manifest_sha256": sha256(manifest_bytes),
            "file_count": manifest["file_count"],
            "total_bytes": manifest["total_bytes"],
            "input_corpus_sha256": manifest["input_corpus_sha256"],
            "content_inventory_sha256": manifest["content_inventory_sha256"],
        }
    evidence = {
        "profile": "ac.generation.source-custody/1",
        "work_grant": "T-005-source-first-graphify-generation",
        "acquisition": "Exact immutable Git blobs; no tenant worktree input and no Git mutation.",
        "excluded_artifact_custody": "Original admitted artifacts are hashed only for candidate identity checks; they are absent from semantic generation corpora.",
        "subjects": results,
        "limits": "Custody and source selection only; no semantic completeness, fidelity, acceptance, adoption or release claim.",
    }
    outputs["evidence/source-custody.json"] = document(evidence)
    return outputs, evidence


def verify_or_write(output: Path, outputs: dict[str, bytes], check: bool) -> int:
    expected = set(outputs)
    for candidate in SUBJECTS:
        corpus = output / "corpora" / candidate
        if corpus.exists():
            observed = {path.relative_to(output).as_posix() for path in corpus.rglob("*") if path.is_file() or path.is_symlink()}
            require(not observed - expected, "unexpected corpus members: " + repr(sorted(observed - expected)))
    missing = []
    for relative, data in outputs.items():
        target = output / relative
        require(target.resolve().is_relative_to(output.resolve()), "output path escapes output directory")
        require(not target.is_symlink(), "snapshot is a symbolic link: " + relative)
        if target.exists():
            require(target.is_file() and target.read_bytes() == data, "frozen output mismatch; refusing overwrite: " + relative)
        else:
            missing.append((relative, data))
    require(not check or not missing, "missing frozen outputs: " + repr([relative for relative, _ in missing]))
    for relative, data in missing:
        target = output / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as stream:
            stream.write(data)
    return len(missing)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--check", action="store_true", help="verify existing snapshots without writing")
    arguments = parser.parse_args()
    try:
        outputs, evidence = build(arguments.repository.resolve())
        created = verify_or_write(arguments.output.resolve(), outputs, arguments.check)
        print(json.dumps({
            "status": "verified" if arguments.check or not created else "frozen",
            "created_files": created,
            "verified_files": len(outputs),
            "subjects": {key: value["selected_input"] for key, value in evidence["subjects"].items()},
        }, indent=2))
        return 0
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print("Source freeze refused: " + str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

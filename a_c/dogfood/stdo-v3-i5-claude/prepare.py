#!/usr/bin/env python3
"""Acquire the named Claude I5 Git objects without reading its mutable tree.

Only this consumer's input custody and subject descriptor are written. Existing
outputs must be byte-identical; a changed output refuses rather than replacing it.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import subprocess
import tarfile


CHECKPOINT = "b7e8f73d6b9908ecb0f6cc1609aa99ed94ce81f7"
PACKAGE = "af3b8b7107c92a216cc53d629ddeefecd7f77fca"
ROOT = "specification_methodology/v3/build_tenants/claude/"
PROGRAM = "a_c/i3/axiomatic-program.json"
SOURCE_ROOTS = [{
    "uri_prefix": "stdo-3://build_tenants/claude/standards/",
    "path_prefix": "standards/",
}]
QUERY = "Different actors, model families or codebases do not establish statistical independence."
RECORD = "urn:stdo-3:claude:i3:clause:pd-no-statistical-independence"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def git(repo: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(repo), *args])


def safe_name(path: str) -> str:
    parsed = PurePosixPath(path)
    if not path or parsed.is_absolute() or ".." in parsed.parts or str(parsed) != path or "\\" in path:
        raise ValueError(f"unsafe member: {path}")
    return path


def tree(repo: Path, commit: str, prefix: str) -> list[tuple[str, str, str]]:
    rows = []
    for raw in git(repo, "ls-tree", "-rz", commit, "--", prefix).split(b"\0"):
        if not raw:
            continue
        meta, name = raw.split(b"\t", 1)
        mode, kind, blob = meta.decode("ascii").split()
        if kind != "blob" or mode not in ("100644", "100755"):
            raise ValueError(f"non-normal Git member: {name!r}")
        rows.append((name.decode("utf-8"), mode, blob))
    if not rows:
        raise ValueError(f"missing Git tree/member: {commit}:{prefix}")
    return rows


def acquire(repo: Path) -> tuple[bytes, dict[str, object], dict[str, object]]:
    for commit in (CHECKPOINT, PACKAGE):
        if git(repo, "rev-parse", "--verify", commit + "^{commit}").decode().strip() != commit:
            raise ValueError(f"unexpected commit: {commit}")
    selected: dict[str, tuple[str, str, str, str]] = {}

    def add(commit: str, repository_path: str, archive_path: str | None = None) -> None:
        for path, mode, blob in tree(repo, commit, repository_path):
            member = safe_name(archive_path if archive_path is not None else path.removeprefix(ROOT))
            row = (commit, path, mode, blob)
            if member in selected and selected[member] != row:
                raise ValueError(f"conflicting member: {member}")
            selected[member] = row

    # These are the actual current method and interpretation, not historical
    # a_c/set-* programs. Both trees must be unchanged at the named checkpoint.
    for prefix in ("standards/", "a_c/i3/"):
        if git(repo, "diff", "--name-only", PACKAGE, CHECKPOINT, "--", ROOT + prefix):
            raise ValueError(f"package/checkpoint subject drift: {prefix}")
        add(PACKAGE, ROOT + prefix)
    for path in ("README.md", "design/INTERPRETATION.md", "release/README.md",
                 "release/release-note.md", "release/manifest.json",
                 "qualification/C3-ITER5/HANDOFF.md", "qualification/C3-ITER5/RESULTS.md"):
        add(CHECKPOINT, ROOT + path)
    add(CHECKPOINT,
        "specification_methodology/v3/specification/requirements/A_C_DEPENDENCY.md",
        "consumer-contract/A_C_DEPENDENCY.md")

    data = {name: git(repo, "cat-file", "blob", row[3]) for name, row in selected.items()}
    release = json.loads(data["release/manifest.json"])
    if release["release"]["commit"] != PACKAGE:
        raise ValueError("declared package freeze changed")
    for member in release["standards"]["members"]:
        if sha(data["standards/" + member["path"]]) != member["sha256"]:
            raise ValueError(f"release member drift: {member['path']}")
    program = json.loads(data[PROGRAM])
    counts = {key: len(program[key]) for key in ("symbols", "clauses", "residuals", "frame_indexes")}
    if counts != {"symbols": 39, "clauses": 155, "residuals": 0, "frame_indexes": 5}:
        raise ValueError("unexpected current interpretation scope")
    discovery = [c for c in program["clauses"] if c["statement"] == QUERY]
    if len(discovery) != 1 or discovery[0]["uri"] != RECORD:
        raise ValueError("discovery coordinate drift")

    coverage: dict[str, object] = {
        "standing": "partial authored interpretation; proposed representation; no semantic acceptance",
        "native_counts": counts,
        "section_dispositions": json.loads(data["a_c/i3/coverage.json"]),
        "declaration_source": "a_c/i3/README.md",
        "encoded_scope": "24 sections encoded in part across eight G1-G4 members, including the I5 G14 construction and assurance extension",
        "uncovered_scope": "182 not-encoded-i3 sections; unencoded parts of the 24 sections; G5-G13 (the other 15 members) lack encoding and disposition files",
        "whole_method_interpretation": False,
        "published_frame_task_fully_covered": False,
        "residual_limit": "No residuals are encoded; open questions elsewhere are not represented.",
        "fidelity_limit": "Same-family fidelity evidence and repaired clauses not independently re-read, as declared in the archived interpretation README.",
        "source_reentry": "Acquire deciding owner sections for questions not decided by the encoded clauses; native frame indexes are bounded partial surfaces.",
        "owner_scope_source": "qualification/C3-ITER5/HANDOFF.md#owner-scoping-after-the-freeze",
        "owner_scope": "The checkpoint handoff records complete interpretation coverage, remaining actual-use expectation sets, and authority compressions/projections as follow-on work outside this baseline candidate.",
        "transport_limit": "Graphify transport does not extend coverage, discharge formulas, validate argument truth, accept the candidate, or establish efficiency.",
    }

    tar_bytes = io.BytesIO()
    members = []
    with tarfile.open(fileobj=tar_bytes, mode="w", format=tarfile.USTAR_FORMAT) as archive:
        for name in sorted(selected):
            commit, path, mode, blob = selected[name]
            content = data[name]
            info = tarfile.TarInfo(name)
            info.size = len(content)
            info.mode = 0o755 if mode == "100755" else 0o644
            info.uid = info.gid = info.mtime = 0
            info.uname = info.gname = ""
            archive.addfile(info, io.BytesIO(content))
            members.append({"path": name, "repository_path": path, "source_commit": commit,
                            "git_blob": blob, "sha256": sha(content), "bytes": len(content), "mode": mode})
    compressed = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=compressed, mtime=0, compresslevel=9) as stream:
        stream.write(tar_bytes.getvalue())
    archive_data = compressed.getvalue()
    manifest: dict[str, object] = {
        "profile": "a_c.v3-frozen-input/1", "tenant": "claude",
        "checkpoint_commit": CHECKPOINT, "package_commit": PACKAGE,
        "package_release_manifest": "release/manifest.json",
        "archive": {"path": "candidate.tar.gz", "sha256": sha(archive_data), "bytes": len(archive_data)},
        "members": members, "program_path": PROGRAM, "source_roots": SOURCE_ROOTS,
        "coverage": coverage,
        "selection": "Current standards and a_c/i3 at the declared RC1 package freeze; current entry/release/handoff records at the named checkpoint. No historical qualification archives or older a_c sets.",
    }
    subject: dict[str, object] = {
        "profile": "a_c.v3-consumer/1", "tenant": "claude",
        "title": "Claude V3 iteration 5 RC1: partial authored a_c interpretation",
        "input_manifest_sha256": sha(json_bytes(manifest)), "program_path": PROGRAM,
        "source_roots": SOURCE_ROOTS, "discovery_query": QUERY, "discovery_record": RECORD,
        "coverage": coverage,
        "argument_reference_policy": "Every explicit local argument ref is retained for native required closure. Role, literal conditions, exceptions, qualifications and support-kind remain exact authored payload; no inferred links.",
    }
    return archive_data, manifest, subject


def put_unchanged(path: Path, content: bytes) -> str:
    if path.exists():
        if not path.is_file() or path.read_bytes() != content:
            raise ValueError(f"refusing changed existing output: {path}")
        return "unchanged"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return "written"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("/Users/jim/src/apps/specification_methodology-claude"))
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    try:
        archive, manifest, subject = acquire(args.repo)
        outputs = [(args.output / "input/candidate.tar.gz", archive),
                   (args.output / "input/manifest.json", json_bytes(manifest)),
                   (args.output / "subject.json", json_bytes(subject))]
        # Preflight every existing output before creating any new output.
        for path, content in outputs:
            if path.exists() and (not path.is_file() or path.read_bytes() != content):
                raise ValueError(f"refusing changed existing output: {path}")
        for path, content in outputs:
            print(f"{put_unchanged(path, content)} {path.name}: {sha(content)}")
        return 0
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f"refusal: {error}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

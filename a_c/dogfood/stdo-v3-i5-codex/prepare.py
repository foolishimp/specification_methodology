#!/usr/bin/env python3
"""Acquire exact Codex RC1 review input without touching the candidate worktree.

Only immutable Git objects are read. Existing unequal output refuses; rerunning
with the same objects is a no-op. No interpretation is inferred or repaired.
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


CHECKPOINT = "8884178770672c933aef706947a864ab6422e1c6"
PACKAGE = "d1b33480b46f45bb46198a2f63ca197e84e40e55"
SOURCE = "2e0c77b909a97648f8edd70981b9a426662df9cc"
ACCOUNT = "0c1ffdb49097c630f9b33a50099e3afb0850d755"
COMMON = "4c340f7adec9f3c893e3e267b23e4cadeb357854"
PREDECESSOR_I5 = "b2ad4d99a9ab6873cded9ffdfbc416ef1e0e23a5"
TENANT_ROOT = "specification_methodology/v3/build_tenants/codex/"
PACKAGE_ROOT = TENANT_ROOT + "successor/"
CURRENT = TENANT_ROOT + "qualification/C3/rc1/end-repair/integration/"
PROGRAM_PATH = "package/interpretation/program.json"
SOURCE_ROOTS = [{"uri_prefix": "repo://codex-v3/successor/", "path_prefix": "package/"}]
DISCOVERY_QUERY = (
    "Comparison and reliance on assertion/construction paths preserve their source "
    "justification, execution provenance, shared failure causes and applicable "
    "independence conditions."
)
DISCOVERY_RECORD = (
    "urn:codex-stdo3:iteration-3-r2:clause:"
    "FOUNDATIONS.parallel-assurance-and-provenance"
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def safe_path(value: str) -> None:
    path = PurePosixPath(value)
    if not value or path.is_absolute() or ".." in path.parts or "\\" in value:
        raise ValueError(f"unsafe custody path: {value!r}")
    if str(path) != value:
        raise ValueError(f"noncanonical custody path: {value!r}")


def git(repository: Path, *arguments: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(repository), *arguments])


def read(repository: Path, commit: str, path: str) -> tuple[bytes, str, str]:
    safe_path(path)
    rows = git(repository, "ls-tree", "-z", commit, "--", path).split(b"\0")
    rows = [row for row in rows if row]
    if len(rows) != 1:
        raise ValueError(f"missing or ambiguous immutable member: {commit}:{path}")
    metadata, found_path = rows[0].split(b"\t", 1)
    mode, kind, blob = metadata.decode("ascii").split()
    if found_path.decode("utf-8") != path or kind != "blob" or mode not in {"100644", "100755"}:
        raise ValueError(f"member must be a regular Git file: {commit}:{path}")
    return git(repository, "cat-file", "blob", blob), blob, mode


def acquire(repository: Path) -> dict[str, bytes]:
    for commit in [CHECKPOINT, PACKAGE, SOURCE, ACCOUNT, COMMON]:
        if git(repository, "rev-parse", "--verify", commit + "^{commit}").decode().strip() != commit:
            raise ValueError("exact immutable commit required")
    candidate = json.loads(read(repository, CHECKPOINT, CURRENT + "CANDIDATE.json")[0])
    if (candidate["package_commit"], candidate["source_commit"], candidate["account_commit"]) != (PACKAGE, SOURCE, ACCOUNT):
        raise ValueError("current RC1 inventory changed its exact subjects")
    members: list[dict[str, object]] = []
    payloads: dict[str, bytes] = {}

    def add(path: str, repository_path: str, commit: str) -> None:
        safe_path(path)
        if path in payloads:
            raise ValueError(f"duplicate custody member: {path}")
        data, blob, mode = read(repository, commit, repository_path)
        payloads[path] = data
        members.append({"path": path, "repository_path": repository_path,
                        "git_commit": commit, "git_blob": blob, "sha256": digest(data),
                        "bytes": len(data), "mode": mode})

    actual_files = git(repository, "ls-tree", "-r", "--name-only", PACKAGE, "--", PACKAGE_ROOT).decode().splitlines()
    expected_files = [PACKAGE_ROOT + row["path"] for row in candidate["members"]]
    if sorted(actual_files) != sorted(expected_files):
        raise ValueError("package inventory does not enumerate the exact package tree")
    for row in sorted(candidate["members"], key=lambda item: item["path"]):
        relative = row["path"]
        add("package/" + relative, PACKAGE_ROOT + relative, PACKAGE)
        body = payloads["package/" + relative]
        if len(body) != row["bytes"] or digest(body) != row["sha256"]:
            raise ValueError(f"candidate inventory mismatch: {relative}")
        if read(repository, CHECKPOINT, PACKAGE_ROOT + relative)[0] != body:
            raise ValueError(f"checkpoint/package drift: {relative}")

    add("account/DETERMINATIONS.json", CURRENT + "DETERMINATIONS.json", ACCOUNT)
    for relative in ["CANDIDATE.json", "COORDINATES.json", "INPUTS.json", "RETURN.json",
                     "RETURN.md", "QUALIFICATION.md", "interpretation/GENERATION.json",
                     "interpretation/QUALIFICATION_EQUIVALENCE.json"]:
        add("qualification/" + relative, CURRENT + relative, CHECKPOINT)
    add("qualification/tenant-README.md", TENANT_ROOT + "README.md", CHECKPOINT)
    add("compiler/build_interpretation.py", TENANT_ROOT + "qualification/C3/iteration-5/tools/build_interpretation.py", CHECKPOINT)

    inventory = json.loads(payloads["package/interpretation/SOURCE_INVENTORY.json"])
    if inventory["document_source_input_commit"] != SOURCE:
        raise ValueError("documentary source coordinate mismatch")
    for row in inventory["document_members"]:
        body = payloads["package/" + row["path"]]
        if len(body) != row["bytes"] or digest(body) != row["sha256"]:
            raise ValueError(f"documentary inventory mismatch: {row['path']}")
        if read(repository, SOURCE, PACKAGE_ROOT + row["path"])[0] != body:
            raise ValueError(f"documentary source/package drift: {row['path']}")
    interpretation = inventory["interpretation"]
    for relative, key in [("program.json", "program_file_sha256"), ("source-account.json", "semantic_account_sha256"),
                          ("SIGNATURE.md", "vocabulary_sha256"), ("FRAMES.md", "frames_sha256"),
                          ("MAPPING.json", "mapping_sha256")]:
        if digest(payloads["package/interpretation/" + relative]) != interpretation[key]:
            raise ValueError(f"interpretation inventory mismatch: {relative}")
    generation = json.loads(payloads["qualification/interpretation/GENERATION.json"])
    if digest(payloads["account/DETERMINATIONS.json"]) != generation["account_sha256"]:
        raise ValueError("authored-account digest mismatch")
    if digest(payloads["compiler/build_interpretation.py"]) != generation["compiler_sha256"]:
        raise ValueError("compiler digest mismatch")
    program = json.loads(payloads[PROGRAM_PATH])
    semantic_account = json.loads(payloads["package/interpretation/source-account.json"])
    counts = {"clauses": len(program["clauses"]), "frame_indexes": len(program["frame_indexes"]),
              "residuals": len(program["residuals"]), "symbols": len(program["symbols"]),
              "determinations": len(semantic_account["determinations"]),
              "shared_contracts": len(semantic_account["semantic_contracts"])}
    if counts != {"clauses": 712, "frame_indexes": 732, "residuals": 5,
                  "symbols": 0, "determinations": 708, "shared_contracts": 37}:
        raise ValueError("unexpected current native population counts")
    discovery_hits = [clause["uri"] for clause in program["clauses"] if DISCOVERY_QUERY in json.dumps(clause, ensure_ascii=False)]
    if discovery_hits != [DISCOVERY_RECORD]:
        raise ValueError("discovery query no longer selects exactly the authored clause")
    coverage = {
        "subject": "Latest RC1 end-review repair package at the selected Codex checkpoint; continuation of I5.",
        "scope": "Transport the complete supplied a_c.text program and all 90 current package members without semantic reinterpretation.",
        "native_counts": counts,
        "documentary_members": len(inventory["document_members"]),
        "stated_standing": "Frozen end-review repair construction; affected independent readback and owner decisions pending.",
        "limits": [
            "Mechanical custody and representation preservation do not establish interpretation fidelity, source completeness or applicability.",
            "Conditional and provenance acquisition routes remain authored boundaries; their presence establishes neither applicability nor satisfaction.",
            "Five residual records retain two release questions and the known UX compliance conflict at three preserved loci.",
            "Material consumer and complete-member coverage, actual-use/context qualification, owner decisions, acceptance, adoption and publication remain open.",
            "The inherited iteration-3-r2 native URI namespace is preserved exactly; it does not identify the current source epoch."
        ],
        "historical_entry_discrepancy": {
            "path": "qualification/tenant-README.md",
            "declared_I5_package": PREDECESSOR_I5,
            "selected_current_package": PACKAGE,
            "resolution": "Use the exact later RC1 CANDIDATE, source inventory and current successor bytes. Preserve the historical I5 entry unchanged."
        }
    }
    buffer = io.BytesIO()
    with gzip.GzipFile(fileobj=buffer, mode="wb", filename="", mtime=0, compresslevel=9) as compressed:
        with tarfile.open(fileobj=compressed, mode="w", format=tarfile.USTAR_FORMAT) as archive:
            for row in sorted(members, key=lambda item: str(item["path"])):
                path = str(row["path"])
                item = tarfile.TarInfo(path)
                item.size = len(payloads[path])
                item.mtime = 0
                item.uid = item.gid = 0
                item.uname = item.gname = ""
                item.mode = int(str(row["mode"]), 8) & 0o777
                item.type = tarfile.REGTYPE
                archive.addfile(item, io.BytesIO(payloads[path]))
    archive_bytes = buffer.getvalue()
    manifest = {
        "profile": "a_c.v3-frozen-input/1", "tenant": "codex",
        "checkpoint_commit": CHECKPOINT, "package_commit": PACKAGE,
        "documentary_source_commit": SOURCE, "account_commit": ACCOUNT,
        "common_input_commit": COMMON,
        "archive": {"path": "candidate.tar.gz", "sha256": digest(archive_bytes), "bytes": len(archive_bytes)},
        "members": sorted(members, key=lambda item: str(item["path"])),
        "program_path": PROGRAM_PATH, "source_roots": SOURCE_ROOTS, "coverage": coverage
    }
    manifest_bytes = json_bytes(manifest)
    subject = {
        "profile": "a_c.v3-consumer/1", "tenant": "codex",
        "title": "Codex V3 I5 / current RC1 end-review repair interpretation",
        "input_manifest_sha256": digest(manifest_bytes), "program_path": PROGRAM_PATH,
        "source_roots": SOURCE_ROOTS, "discovery_query": DISCOVERY_QUERY,
        "discovery_record": DISCOVERY_RECORD, "coverage": coverage
    }
    return {"input/candidate.tar.gz": archive_bytes, "input/manifest.json": manifest_bytes,
            "subject.json": json_bytes(subject)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path,
                        default=Path(__file__).resolve().parents[4] / "specification_methodology-codex")
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent)
    arguments = parser.parse_args()
    outputs = acquire(arguments.repository.resolve())
    target = arguments.output.absolute()
    # Preflight every destination before writing any output.
    for relative, body in outputs.items():
        path = target / relative
        for component in [path, *path.parents]:
            if component.is_symlink():
                raise ValueError(f"symlinked output path refuses: {component}")
        if path.exists() and (not path.is_file() or path.read_bytes() != body):
            raise ValueError(f"existing unequal output refuses: {path}")
    for relative, body in outputs.items():
        path = target / relative
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("xb") as stream:
                stream.write(body)
    manifest = json.loads(outputs["input/manifest.json"])
    print(json.dumps({"tenant": "codex", "checkpoint": CHECKPOINT, "package": PACKAGE,
                      "members": len(manifest["members"]), "archive": manifest["archive"],
                      "native_counts": manifest["coverage"]["native_counts"]}, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Create lossless native study baselines without Graphify or third-party imports.

The input archive and every member are checked against the previously frozen
custody manifest. This does not re-author or semantically accept the program.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import tarfile
import time


ROOT = Path(__file__).resolve().parent
INPUT_PINS = {
    "codex": "f7140b802be45b89b82d86b07e837e8e19dcb8235f1676cd0d4f56276a27fbec",
    "claude": "d9a6dc3826270addc3d69e9db2e6c6733f5cc691659583a176a667ac1f61e412",
}
FAMILIES = ("symbols", "clauses", "residuals", "frame_indexes")


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def packed(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def require(test: bool, message: str) -> None:
    if not test:
        raise ValueError(message)


def write(path: Path, raw: bytes) -> None:
    require(not path.is_symlink(), "symlink output")
    if path.exists():
        require(path.read_bytes() == raw, f"different existing output: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as target:
        target.write(raw)


def allowed(tenant: str, name: str) -> bool:
    if tenant == "codex":
        return name.startswith("package/")
    return name.startswith("standards/") or name.startswith("a_c/i3/dispositions/") or name.startswith("a_c/i3/fragments/") or name in {
        "a_c/i3/README.md", "a_c/i3/SIGNATURE.md", "a_c/i3/axiomatic-program.json",
        "a_c/i3/bindings.json", "a_c/i3/coverage.json", "a_c/i3/logical-constraint-map.json",
    }


def frozen(tenant: str) -> tuple[dict, dict, dict[str, bytes], bytes]:
    source = ROOT.parent / f"stdo-v3-i5-{tenant}"
    manifest_raw = (source / "input/manifest.json").read_bytes()
    require(sha(manifest_raw) == INPUT_PINS[tenant], "input manifest pin differs")
    manifest = json.loads(manifest_raw)
    subject = json.loads((source / "subject.json").read_bytes())
    require(subject["input_manifest_sha256"] == INPUT_PINS[tenant], "subject manifest differs")
    require(subject["program_path"] == manifest["program_path"], "program route differs")
    archive = source / "input/candidate.tar.gz"
    require(sha(archive.read_bytes()) == manifest["archive"]["sha256"], "archive digest differs")
    require(archive.stat().st_size == manifest["archive"]["bytes"], "archive length differs")
    inventory = {item["path"]: item for item in manifest["members"]}
    require(len(inventory) == len(manifest["members"]), "duplicate manifest member")
    members: dict[str, bytes] = {}
    with tarfile.open(archive, "r:gz") as capture:
        for entry in capture.getmembers():
            name = entry.name
            parts = PurePosixPath(name).parts
            require(entry.isfile() and not entry.issym() and not entry.islnk(), "nonregular archive member")
            require(parts and not name.startswith("/") and ".." not in parts and str(PurePosixPath(name)) == name, "unsafe archive path")
            require(name not in members and name in inventory, "duplicate or extra member")
            stream = capture.extractfile(entry)
            require(stream is not None, "missing member stream")
            raw = stream.read()
            row = inventory[name]
            require(sha(raw) == row["sha256"] and len(raw) == row["bytes"], f"member custody mismatch: {name}")
            blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
            require(blob == row["git_blob"], f"Git blob mismatch: {name}")
            require(row["mode"] in ("100644", "100755"), "unsupported manifest file mode")
            require(entry.mode & 0o777 == int(row["mode"][-3:], 8), f"archive mode mismatch: {name}")
            members[name] = raw
    require(members.keys() == inventory.keys(), "incomplete archive inventory")
    return subject, manifest, members, (source / "subject.json").read_bytes()


def build(tenant: str, output: Path) -> dict:
    started = time.perf_counter()
    subject, custody, members, subject_raw = frozen(tenant)
    program_raw = members[subject["program_path"]]
    program = json.loads(program_raw)
    require(all(isinstance(program[family], list) for family in FAMILIES), "native families absent")
    ids = [record["uri"] for family in FAMILIES for record in program[family]]
    require(len(ids) == len(set(ids)), "duplicate native identity")
    selected = {name: raw for name, raw in members.items() if allowed(tenant, name)}
    signature_path = "package/interpretation/SIGNATURE.md" if tenant == "codex" else "a_c/i3/SIGNATURE.md"
    write(output / "program.json", program_raw)
    write(output / "signature.md", members[signature_path])
    write(output / "coverage.json", packed(subject["coverage"]))
    catalogue = b"".join(
        (json.dumps(dict(family=family, ordinal=ordinal, record=record), ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()
        for family in FAMILIES for ordinal, record in enumerate(program[family])
    )
    write(output / "records.jsonl", catalogue)
    for name, raw in sorted(selected.items()):
        write(output / "sources" / name, raw)
    manifest = dict(
        profile="ac.eval.native-baseline/1", tenant=tenant,
        source_roots=subject["source_roots"],
        input=dict(subject_sha256=sha(subject_raw), manifest_sha256=INPUT_PINS[tenant],
                   archive_sha256=custody["archive"]["sha256"], checkpoint_commit=custody["checkpoint_commit"],
                   package_commit=custody["package_commit"], program_path=subject["program_path"]),
        native_program=dict(path="program.json", sha256=sha(program_raw), bytes=len(program_raw)),
        signature=dict(path="signature.md", source=signature_path, sha256=sha(members[signature_path])),
        catalogue=dict(path="records.jsonl", sha256=sha(catalogue), bytes=len(catalogue)),
        coverage_path="coverage.json", coverage_sha256=sha(packed(subject["coverage"])),
        counts={family: len(program[family]) for family in FAMILIES},
        files=[dict(path=name, sha256=sha(raw), bytes=len(raw)) for name, raw in sorted(selected.items())],
        excluded_archive_members=sorted(set(members) - set(selected)),
        builder_sha256=sha(Path(__file__).read_bytes()),
        claim="Complete original native program and exact allowlisted sources; historical F_P authoring is common prior work, not a measured zero cost. No semantic acceptance.",
    )
    write(output / "manifest.json", packed(manifest))
    # Independently reconstruct all native populations from the portable catalogue.
    recovered = {family: [] for family in FAMILIES}
    for line in (output / "records.jsonl").read_text().splitlines():
        row = json.loads(line)
        require(row["ordinal"] == len(recovered[row["family"]]), "catalogue order differs")
        recovered[row["family"]].append(row["record"])
    require(all(program[family] == recovered[family] for family in FAMILIES), "catalogue recovery differs")
    return dict(tenant=tenant, elapsed_seconds=round(time.perf_counter()-started, 6),
                manifest_sha256=sha(packed(manifest)), counts=manifest["counts"],
                source_members=len(selected), source_bytes=sum(len(raw) for raw in selected.values()),
                native_bytes=len(program_raw), catalogue_bytes=len(catalogue),
                complete_native_recovery=True, archive_members_verified=len(members))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tenant", choices=["codex", "claude", "both"], default="both")
    parser.add_argument("--out", type=Path, default=ROOT / "baselines")
    args = parser.parse_args()
    tenants = ("codex", "claude") if args.tenant == "both" else (args.tenant,)
    results = [build(tenant, args.out / tenant) for tenant in tenants]
    print(json.dumps(dict(profile="ac.eval.baseline-build/1", results=results), indent=2))


if __name__ == "__main__":
    main()

"""Exact-subject public receipt bindings for this fixed common application.

Checks coordinate equality and custody only. Receipt claims, issuer legitimacy,
independence, semantic correctness, acceptance and release remain external.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import re

CONSTRUCTION = "a_c.common.public-construction-receipt/1"
REVIEW = "a_c.common.bounded-review-receipt/1"
ARTIFACTS = ("model.json", "carrier.json", "graph.json", "coverage.json", "result.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def digest(value) -> str:
    return sha(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
                          allow_nan=False).encode("utf-8"))


def read(path: Path):
    def pairs(items):
        value = {}
        for key, item in items:
            require(key not in value, "public receipt has a duplicate JSON key")
            value[key] = item
        return value
    def constant(value):
        raise ValueError(f"public receipt has a nonfinite JSON number: {value}")
    return json.loads(path.read_bytes(), object_pairs_hook=pairs, parse_constant=constant)


def relative(value: str) -> str:
    require(isinstance(value, str), "public report path must be text")
    p = PurePosixPath(value)
    require(bool(value) and not p.is_absolute() and p.as_posix() == value
            and all(part not in ("", ".", "..") for part in p.parts)
            and "\\" not in value and "\0" not in value, "unsafe public report path")
    require(p.suffix.lower() in (".md", ".txt"), "bound review reports must be Markdown or text")
    return value


def expected_bindings(root: Path, model, paths: dict[str, Path]) -> dict:
    require(set(paths) == set(ARTIFACTS), "public receipt requires all five exact artifact identities")
    custody = read(root / "package-custody.json")
    subject = model.document["basis"]["subject"]
    return {
        "source": {"subject_id": subject["id"], "commit": custody["source"]["commit"],
                   "package_tree": custody["source"]["package_tree"],
                   "source_manifest_sha256": sha((root / "source-manifest.json").read_bytes()),
                   "semantic_files_sha256": subject["sha256"],
                   "section_inventory_sha256": digest(subject["inventory"]),
                   "source_reentry_sha256": model.document["interpretation"]["source_reentry"]["sha256"]},
        "model": {"id": model.identity, "sha256": model.sha256},
        "artifacts": {name: {"bytes": paths[name].stat().st_size, "sha256": sha(paths[name].read_bytes())}
                      for name in ARTIFACTS},
    }


def receipt(path: Path, expected: dict, kind: str) -> tuple[dict, list[tuple[dict, Path]]]:
    require(path.suffix.lower() == ".json", "a review report alone is not a bound receipt; supply its typed JSON receipt")
    require(path.is_file() and not path.is_symlink(), "missing or redirected public JSON receipt")
    value = read(path)
    common = {"kind", "receipt_id", "issuer", "bindings", "scope", "details"}
    fields = common | ({"construction_state", "private_material_included"} if kind == CONSTRUCTION
                       else {"review_state", "outcome", "independence", "reports"})
    require(isinstance(value, dict) and set(value) == fields, "public receipt fields do not match the application contract")
    require(value["kind"] == kind, "public receipt has the wrong explicit type")
    for key in ("receipt_id", "issuer"):
        require(isinstance(value[key], str) and re.fullmatch(r"[A-Za-z][A-Za-z0-9+.-]*:[^\s]+", value[key]) is not None,
                f"public receipt {key} must be an absolute identity")
    require(value["bindings"] == expected, "public receipt source/model/raw-artifact bindings differ from the actual candidate")
    require(isinstance(value["scope"], str) and bool(value["scope"].strip()), "public receipt needs its explicit bounded scope")
    require(isinstance(value["details"], dict) and bool(value["details"]), "public receipt needs an explicit recorded account")
    if kind == CONSTRUCTION:
        require(value["construction_state"] == "complete" and value["private_material_included"] is False,
                "construction receipt must declare complete processing and excluded private material")
        return value, []
    require(value["review_state"] == "closed", "bounded review receipt does not declare a closed review")
    require(isinstance(value["outcome"], str) and bool(value["outcome"].strip()), "review receipt needs its reported outcome")
    require(isinstance(value["independence"], dict) and bool(value["independence"]), "review receipt must disclose its independence basis and limits")
    require(isinstance(value["reports"], list), "review reports must be an explicit list, possibly empty")
    seen = set()
    reports = []
    for row in value["reports"]:
        require(isinstance(row, dict) and set(row) == {"path", "bytes", "sha256"}, "review report binding fields differ")
        name = relative(row["path"])
        require(name not in seen, "duplicate review report path")
        seen.add(name)
        report = path.parent / name
        require(report.is_relative_to(path.parent), "review report escaped receipt directory")
        current = path.parent
        for part in PurePosixPath(name).parts:
            current /= part
            require(not current.is_symlink(), "redirected public report path")
        require(report.is_file(), "bound readable review report is missing")
        data = report.read_bytes()
        require(type(row["bytes"]) is int and row["bytes"] == len(data) and row["sha256"] == sha(data),
                "readable review report bytes differ from its explicit receipt binding")
        data.decode("utf-8")
        reports.append((row, report))
    return value, reports


def bundle_evidence(root: Path, expected: dict) -> dict:
    release = read(root / "RELEASE.json")
    require(release.get("public_receipt_contract") == [CONSTRUCTION, REVIEW],
            "release public-receipt contract differs")
    require(release["subject"] == expected["source"]["subject_id"] and release["model"] == expected["model"],
            "release-preparation subject/model differs from its public evidence")
    require(release.get("source_commit") == expected["source"]["commit"]
            and release.get("package_tree") == expected["source"]["package_tree"],
            "release-preparation source commit/package tree differs from its public evidence")
    public = root / "evidence/authoring-public.json"
    construction, _ = receipt(public, expected, CONSTRUCTION)
    require(release["public_authoring_receipt_sha256"] == sha(public.read_bytes()), "construction receipt hash differs")
    rows = release["review_receipts"]
    require(isinstance(rows, list) and bool(rows), "preparation requires at least one explicit bounded-review receipt")
    seen = {construction["receipt_id"]}
    expected_files = {"authoring-public.json"}
    for number, row in enumerate(rows, 1):
        name = f"evidence/reviews/review-{number:03d}/receipt.json"
        require(isinstance(row, dict) and set(row) == {"path", "sha256", "receipt_id", "reports"}
                and row["path"] == name, "release review receipt index differs")
        path = root / name
        review, reports = receipt(path, expected, REVIEW)
        require(review["receipt_id"] not in seen, "public receipt identity collision")
        seen.add(review["receipt_id"])
        require(row["receipt_id"] == review["receipt_id"] and row["sha256"] == sha(path.read_bytes()),
                "review receipt identity/hash differs from the release index")
        expected_files.add(path.relative_to(root / "evidence").as_posix())
        bound_reports = []
        for binding, report in reports:
            rel = report.relative_to(root).as_posix()
            bound_reports.append({"path": rel, "bytes": binding["bytes"], "sha256": binding["sha256"]})
            expected_files.add(report.relative_to(root / "evidence").as_posix())
        require(row["reports"] == bound_reports, "release report routes differ from the review's own bindings")
    actual_files = set()
    for path in (root / "evidence").rglob("*"):
        require(not path.is_symlink(), "public evidence contains a redirected path")
        if path.is_file():
            actual_files.add(path.relative_to(root / "evidence").as_posix())
    require(actual_files == expected_files, "public evidence has missing or unbound files")
    return {"construction_receipt": construction["receipt_id"], "bounded_review_receipts": len(rows),
            "claim": "Types, exact source/model/artifact bindings and readable-report custody checked; receipt truth, issuer legitimacy, independence and semantic fitness remain external."}

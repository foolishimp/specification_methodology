#!/usr/bin/env python3
"""Package one explicit F_P correction; this is not a generic transformation."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CODEC = ROOT / "build_tenants/graphify/code/ac_graph.py"
CODEC_SHA256 = "2f5de4d600e13904dc8cba3791ebdd83fe6ebb0c339654c86392baf9c2bd3667"
PARENT = ROOT / "dogfood/stdo-v3-generation-rc9/runs-v2/claude/direct/repaired-proposal/model.json"
PARENT_FILE_SHA256 = "bf12529fc3359c3d0a6238c6214693e022d665f1148a1543f7add2ac2b150704"
PARENT_CANONICAL_SHA256 = "fb1f15ca409fd302dcad56c86c4edf111ca00b1fb581ddae4d332fb18d338111"
TARGET = "urn:a-c:generation:63c64519947babe1e3fec509:record:613311974eb7d572ca277ccf96b8f339"
TARGET_POINTER = "/populations/constraints/16/predicate/exceptions/0"
PREFIX = "urn:a-c:application:stdo-v3-rc9-claude-direct-review-correction:001"


def raw_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode("utf-8")


def digest(value: object) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def read(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected object: {path}")
    return value


def coord(document: dict) -> dict:
    return {"id": document["id"], "sha256": digest(document)}


def require(condition: bool, reason: str) -> None:
    if not condition:
        raise ValueError(reason)


def changes(before: object, after: object, path: str = "") -> list[dict]:
    if type(before) is not type(after):
        return [{"path": path, "before": before, "after": after}]
    if isinstance(before, dict):
        require(set(before) == set(after), f"unexpected object shape change: {path}")
        return [item for key in before for item in changes(before[key], after[key], path + "/" + key)]
    if isinstance(before, list):
        if len(before) != len(after):
            return [{"path": path, "before": before, "after": after}]
        return [item for i, (a, b) in enumerate(zip(before, after)) for item in changes(a, b, path + "/" + str(i))]
    return [] if before == after else [{"path": path, "before": before, "after": after}]


def apply_explicit_patch(parent: dict, patch: dict) -> dict:
    """No inferred selection or semantic generation occurs in this function."""
    require(digest(parent) == PARENT_CANONICAL_SHA256, "parent canonical identity changed")
    require(patch["profile"] == "a_c.application.semantic-patch/1", "unknown application patch profile")
    require(len(patch["operations"]) == 1, "one operation required")
    op = patch["operations"][0]
    require(set(op) == {"op", "record_id", "path", "before", "after"}, "unsupported operation shape")
    require(op["op"] == "replace" and op["record_id"] == TARGET and op["path"] == TARGET_POINTER, "patch exceeds exact target")
    require(isinstance(op["after"], str) and bool(op["after"]), "replacement must be explicit nonempty F_P text")
    record = parent["populations"]["constraints"][16]
    require(record["id"] == TARGET, "target ordinal changed")
    require(record["predicate"]["exceptions"][0] == op["before"], "target preimage changed")
    successor = copy.deepcopy(parent)
    successor["populations"]["constraints"][16]["predicate"]["exceptions"][0] = op["after"]
    require([d["path"] for d in changes(parent, successor)] == [TARGET_POINTER], "non-target semantic change")
    return successor


def construct() -> tuple[dict, dict, dict, dict]:
    require(raw_sha(CODEC) == CODEC_SHA256, "codec changed; this application requires its exact reviewed codec")
    require(raw_sha(PARENT) == PARENT_FILE_SHA256, "frozen parent file changed")
    parent = read(PARENT)
    patch = read(HERE / "semantic-patch.json")
    source_manifest = read(HERE / "source-manifest.json")
    authoring = read(HERE / "authoring-record.json")
    interpreter = read(HERE / "interpreter.json")
    contract = read(HERE / "interpretation-contract.json")
    require(contract["patch"] == coord(patch), "changed patch contract")
    require(contract["sources"] == coord(source_manifest), "changed source contract")
    require(contract["authoring"] == coord(authoring), "changed authoring contract")
    require(contract["interpreter"] == coord(interpreter), "changed interpreter contract")
    require(authoring["packager_file_sha256"] == raw_sha(Path(__file__)), "changed deterministic packager")
    require(authoring["source_first_expectations"]["sha256"] == raw_sha(ROOT / authoring["source_first_expectations"]["path"]), "changed source-first oracle")
    corpus = ROOT / source_manifest["corpus_manifest"]["path"]
    require(raw_sha(corpus) == source_manifest["corpus_manifest"]["file_sha256"], "frozen corpus manifest changed")
    frozen = read(corpus)
    require(len(frozen["files"]) == source_manifest["frozen_file_count"], "changed source population")
    for entry in frozen["files"]:
        path = corpus.parent / "source" / entry["path"]
        require(raw_sha(path) == entry["sha256"] and path.stat().st_size == entry["bytes"], f"frozen source changed: {entry['path']}")
    for entry in source_manifest["deciding_sources"]:
        path = ROOT / entry["path"]
        require(raw_sha(path) == entry["file_sha256"], "deciding source changed")
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        for witness in entry["witnesses"]:
            exact = "".join(lines[witness["start_line"] - 1:witness["end_line"]])
            require(exact == witness["exact_source"], "source witness differs")
    successor = apply_explicit_patch(parent, patch)
    successor["id"] = contract["successor_model_id"]
    successor["interpretation"]["contract"] = coord(contract)
    successor["interpretation"]["interpreter"] = coord(interpreter)
    added_provenance = [{"id": parent["id"], "sha256": digest(parent)}, coord(authoring), coord(source_manifest), coord(patch)]
    successor["interpretation"]["provenance"] += added_provenance
    delta = changes(parent, successor)
    allowed = {TARGET_POINTER, "/id", "/interpretation/contract/id", "/interpretation/contract/sha256", "/interpretation/interpreter/id", "/interpretation/interpreter/sha256", "/interpretation/provenance"}
    require({d["path"] for d in delta} == allowed, "unexpected application delta")
    require(successor["interpretation"]["provenance"][:-len(added_provenance)] == parent["interpretation"]["provenance"], "historical provenance rewritten")
    require(successor["interpretation"]["dispositions"] == parent["interpretation"]["dispositions"], "selection dispositions changed")
    return parent, successor, contract, {"profile": "a_c.application.semantic-delta/1", "changes": delta, "semantic_change_count": 1, "claim": "Exact syntactic delta only; no AC-013 transformation or semantic-preservation judgment."}


def expected_artifacts() -> dict[str, dict]:
    parent, successor, contract, delta = construct()
    sys.path.insert(0, str(CODEC.parent))
    import ac_graph as codec

    model = codec.validate(successor)
    carrier = codec.materialize(model)
    recovered = codec.decode(carrier)
    require(recovered.document == successor and recovered.sha256 == model.sha256, "codec recovery changed proposed model")
    require(codec.digest(successor) == digest(successor), "canonical hash contract differs")
    counts = {family: len(records) for family, records in successor["populations"].items()}
    original_coverage_path = PARENT.with_name("coverage.json")
    original_coverage = read(original_coverage_path)
    preserved = {key: digest(parent[key]) for key in parent if key not in {"id", "interpretation", "populations"}}
    unchanged_records = sum(1 for family in parent["populations"] for before, after in zip(parent["populations"][family], successor["populations"][family]) if before == after)
    coverage = {
        "profile": "a_c.application.semantic-correction-coverage/1",
        "status": "proposed-unaccepted",
        "parent_coverage": {"path": str(original_coverage_path.relative_to(ROOT)), "file_sha256": raw_sha(original_coverage_path)},
        "parent_processing_complete": original_coverage["processing_complete"],
        "new_source_generation_performed": False,
        "source_sections": len(successor["basis"]["subject"]["inventory"]),
        "family_counts": counts,
        "records_unchanged": unchanged_records,
        "records_changed": 1,
        "source_selection_dispositions_unchanged": True,
        "selection_ledger": successor["interpretation"]["selection_ledger"],
        "parent_unqualified": original_coverage["unqualified"],
        "parent_unresolved_boundaries_preserved": {"count": len(original_coverage["unresolved_boundaries"]), "sha256": digest(original_coverage["unresolved_boundaries"])},
        "application_limits": ["Only the reviewed target exception is corrected.", "All other source selection, qualifications and residuals remain exactly those of the frozen parent.", "The author's deciding-source assessment is F_P work, not independent acceptance.", "Global semantic completeness, cross-chunk governing closure, full calculus conformance, usability and accepted-result benefit remain unqualified.", "No fresh upstream Graphify build/export trial is claimed for this new proposal."],
        "semantic_acceptance": "not requested or issued",
    }
    artifacts = {"model.json": successor, "carrier.json": carrier.document, "delta.json": delta, "coverage.json": coverage}
    result = {
        "profile": "a_c.application.semantic-correction-result/1",
        "status": "proposed-unaccepted",
        "parent": {"id": parent["id"], "canonical_sha256": digest(parent), "file_sha256": PARENT_FILE_SHA256},
        "model": codec.model_identity(model),
        "contract": successor["interpretation"]["contract"],
        "family_counts": counts,
        "references_checked": len(model.references),
        "codec": {"path": str(CODEC.relative_to(ROOT)), "file_sha256": CODEC_SHA256},
        "checks": {"frozen_corpus_files": 49, "explicit_patch_count": 1, "exact_allowed_delta": True, "declared_fragment_validation": True, "proposal_materialization": True, "exact_recovery": True, "unchanged_records": unchanged_records, "preserved_top_level_canonical_hashes": preserved},
        "files_canonical_sha256": {name: digest(value) for name, value in artifacts.items()},
        "claim": "One explicit F_P-authored application correction, structurally checked and exactly recovered as a proposal. No semantic acceptance, full-calculus, release, fresh upstream or efficiency claim.",
    }
    artifacts["result.json"] = result
    return artifacts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="read-only recomputation of the existing proposal")
    args = parser.parse_args()
    try:
        artifacts = expected_artifacts()
        destination = HERE / "proposal"
        if args.check:
            require(destination.is_dir(), "proposal absent")
            require({p.name for p in destination.iterdir()} == set(artifacts), "proposal file set changed")
            for name, document in artifacts.items():
                require(read(destination / name) == document, f"proposal artifact changed: {name}")
            print(json.dumps({"status": "reproduced", "model": artifacts["result.json"]["model"], "files": sorted(artifacts)}, sort_keys=True))
        else:
            require(not destination.exists(), "proposal already exists; use --check for read-only replay")
            destination.mkdir()
            for name, document in artifacts.items():
                (destination / name).write_text(json.dumps(document, sort_keys=True, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(json.dumps({"status": "proposed-unaccepted", "model": artifacts["result.json"]["model"], "destination": str(destination)}, sort_keys=True))
        return 0
    except (ValueError, KeyError, IndexError, TypeError) as exc:
        print(json.dumps({"status": "refused", "reason": str(exc)}, sort_keys=True), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

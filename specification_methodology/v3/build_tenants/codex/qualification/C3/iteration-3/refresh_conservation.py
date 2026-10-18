"""Finalize current conservation pins; only the conservation Writer invokes this.

This script never imports an older map or reclassifies a row. The package Writer
supplies a complete frozen inventory; the semantic map must survive unchanged.
"""
import argparse
import json
from pathlib import Path
import re
import subprocess
from check_conservation import (HERE, PACKAGE, REPO, frontier_for,
                                git_bytes, read, semantic_sha, sha, validate)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--inventory", type=Path, default=HERE / "CANDIDATE.json")
    parser.add_argument("--check-only", action="store_true")
    parser.add_argument("--expect-conservation-sha256")
    args = parser.parse_args()
    if not re.fullmatch(r"[0-9a-f]{40}", args.source_commit):
        raise ValueError("A full immutable 40-character source commit is required")
    commit = subprocess.check_output(["git", "rev-parse", args.source_commit + "^{commit}"], cwd=REPO, text=True).strip()
    inventory = read(args.inventory)
    if inventory.get("candidate_body_input_commit") != commit or inventory.get("inventory_input_commit") != commit:
        raise ValueError("Inventory must bind the exact complete frozen source commit")
    members = inventory["members"]
    names = [m["path"] for m in members]
    actual = {str(p.relative_to(PACKAGE)) for p in PACKAGE.rglob("*") if p.is_file()}
    if len(names) != len(set(names)) or set(names) != actual:
        raise ValueError("Inventory must cover the complete current package exactly once")
    for member in members:
        path = PACKAGE / member["path"]
        path.resolve().relative_to(PACKAGE.resolve())
        data = path.read_bytes()
        if sha(data) != member["sha256"] or len(data) != member["bytes"]:
            raise ValueError("Inventory differs from current file: " + member["path"])
        if data != git_bytes(commit, str(path.relative_to(REPO))):
            raise ValueError("Current file differs from frozen source: " + member["path"])
    before_bytes = (HERE / "CONSERVATION.json").read_bytes()
    if args.expect_conservation_sha256 and sha(before_bytes) != args.expect_conservation_sha256:
        raise ValueError("Current conservation map differs from the selected preimage")
    mapping = read(HERE / "CONSERVATION.json")
    ports = read(HERE / "PORT_ACCOUNT.json")
    before = semantic_sha(mapping)
    if before != mapping["semantic_sha256"]:
        raise ValueError("Authored semantic integrity check failed")
    report = validate(mapping, read(HERE / "FRONTIER.json"), ports)
    if not report["valid"]:
        raise ValueError(json.dumps(report["failures"]))
    mapping["candidate_source_commit"] = commit
    mapping["pin_state"] = "frozen_source_verified"
    mapping["successor_member_pins"] = report["observed_member_pins"]
    mapping["successor_locus_pins"] = report["observed_locus_pins"]
    for row in mapping["rows"]:
        if row.get("successor_locus"):
            row["successor_sha256"] = mapping["successor_member_pins"][row["successor_locus"].split("#")[0]]["sha256"]
    if semantic_sha(mapping) != before:
        raise ValueError("Pin finalization changed authored semantics")
    frontier = frontier_for(mapping)
    final = validate(mapping, frontier, ports, require_frozen=True)
    if not final["valid"]:
        raise ValueError(json.dumps(final["failures"]))
    if not args.check_only:
        if (HERE / "CONSERVATION.json").read_bytes() != before_bytes:
            raise ValueError("Conservation map changed during finalization")
        (HERE / "CONSERVATION.json").write_text(json.dumps(mapping, indent=2, ensure_ascii=False) + "\n")
        (HERE / "FRONTIER.json").write_text(json.dumps(frontier, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"source_commit": commit, "semantic_sha256": before,
                      "semantics_preserved": True, "package_members_verified": len(members),
                      "carrying_loci": final["carrying_loci"], "check_only": args.check_only,
                      "standing": "Frozen coordinates only; independent semantics and owner acceptance remain open."}, indent=2))


if __name__ == "__main__":
    main()

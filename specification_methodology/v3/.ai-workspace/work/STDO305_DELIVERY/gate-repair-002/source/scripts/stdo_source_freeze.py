#!/usr/bin/env python3
"""Freeze and verify the semantic input of a complete native STDO cohort.

Generated frames, documentation and tool bundles are classified explicitly.
They cannot enlarge or shrink the authoritative input closure.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import stat

KIND = "stdo.semantic-source-freeze/1"
EXCLUDED = ("standards/frames/", "standards/documentation/", "standards/tooling/")
NATIVE_CONTRACTS = ("plugins/spec/skills/", "plugins/spec/claude-skills/",
                    "plugins/spec/references/PRODUCT_BASIS.md",
                    "plugins/spec/references/COORDINATED_HANDOFF.md",
                    "plugins/spec/references/HOST_BINDING.md",
                    "plugins/spec/references/REFRESH.md")


def encoded(value):
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()


def sha(value):
    return hashlib.sha256(value).hexdigest()


def member_digest(rows):
    return sha("".join(f"{r['sha256']}  {r['path']}\n" for r in rows).encode())


def inventory(root, predicate):
    rows = []
    for path in sorted(root.rglob("*")):
        name = path.relative_to(root).as_posix()
        if path.is_symlink():
            raise ValueError("source redirect refused: " + name)
        if path.is_dir():
            continue
        if not stat.S_ISREG(path.stat().st_mode):
            raise ValueError("nonregular source member: " + name)
        if predicate(name):
            data = path.read_bytes()
            rows.append({"path": name, "bytes": len(data), "sha256": sha(data)})
    return rows


def build(root, version, source_root):
    members = inventory(root, lambda n: n.startswith("standards/") and not n.startswith(EXCLUDED))
    contracts = inventory(root, lambda n: any(n.startswith(p) if p.endswith("/") else n == p for p in NATIVE_CONTRACTS))
    if not members or not contracts:
        raise ValueError("complete standards and native contract inputs required")
    identity = {"version": version, "basis_uri": f"stdo://releases/v{version}/",
                "members": members, "native_contracts": contracts}
    return {"kind": KIND, "source_root": source_root, **identity,
            "source_identity_sha256": sha(encoded(identity)),
            "member_count": len(members), "member_set_sha256": member_digest(members),
            "native_contract_count": len(contracts), "native_contract_set_sha256": member_digest(contracts),
            "source_roles": {"standards": "semantic owners, schemas, templates, examples and source navigation",
                             "native_contracts": "workflow projections; owning standards retain authority"},
            "derived_routes": {"prefix": "standards/frames/", "inputs": "standards/frames/FRAME_INPUTS.json",
                               "relation": "verbatim or declared bounded projections of exact semantic owners"},
            "generated_exclusions": [
                {"prefix": "standards/frames/", "owner": "Specification Methodology", "reason": "derived source routes; never independent semantic owners"},
                {"prefix": "standards/documentation/", "owner": "STDO Representation and common packaging", "reason": "current source-derived views and exact proof evidence"},
                {"prefix": "standards/tooling/", "owner": "component Products and common packaging", "reason": "installable tools and exact portable source distributions"}],
            "other_native_payload": "LICENSE, release note, plugin metadata/scripts and installation guide are independently inventoried at native freeze; they cannot amend these semantic owners",
            "standing": "frozen semantic input; no qualification or publication verdict"}


def verify(root, value):
    if value.get("kind") != KIND:
        raise ValueError("unknown semantic source freeze")
    actual = build(root, value["version"], value["source_root"])
    if actual != value:
        raise ValueError("semantic source closure, member digest, contract or classification differs")
    return {"status": "valid", "source_identity_sha256": value["source_identity_sha256"],
            "member_count": value["member_count"], "native_contract_count": value["native_contract_count"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("freeze", "check"))
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--record", required=True, type=Path)
    parser.add_argument("--version", default="3.0.5")
    parser.add_argument("--source-root", default="specification_methodology/v3/build_tenants/common")
    args = parser.parse_args()
    try:
        if args.command == "freeze":
            value = build(args.root, args.version, args.source_root)
            args.record.parent.mkdir(parents=True, exist_ok=True)
            with args.record.open("xb") as stream:
                stream.write(encoded(value))
        else:
            value = json.loads(args.record.read_bytes())
        print(json.dumps(verify(args.root, value), indent=2))
    except (OSError, ValueError, KeyError) as exc:
        parser.exit(1, "refused: " + str(exc) + "\n")


if __name__ == "__main__":
    main()

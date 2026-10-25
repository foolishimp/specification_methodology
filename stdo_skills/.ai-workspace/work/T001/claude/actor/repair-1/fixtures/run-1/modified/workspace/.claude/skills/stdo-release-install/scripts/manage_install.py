#!/usr/bin/env python3
"""Validate and manage the complete project-local Claude STDO Skills bundle.

Cooperative single-writer filesystem only. Failures after mutation can leave a
partial installation: retain the current tree/receipt and reconcile, never force.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
from urllib.parse import unquote, urlsplit

NAMES = ("stdo-workspace-change", "stdo-tool-operations", "stdo-delegate-review",
         "stdo-continuation", "stdo-release-install")
PACKAGE_ID = "urn:stdo-skills:claude:five-skill-bundle:1"
RECEIPT = "stdo-skills-claude.receipt.json"
SCHEMA = "stdo-skills.claude-installation/1"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tree(root):
    """Exact regular-file and directory population, including hidden additions."""
    root = Path(root)
    if root.is_symlink() or not root.is_dir():
        raise ValueError("Expected a real directory: " + str(root))
    files, directories = {}, ["."]
    for parent, dirs, names in os.walk(root, followlinks=False):
        for name in sorted(dirs + names):
            path = Path(parent) / name
            if path.is_symlink():
                raise ValueError("Symlink is not a bundle resource: " + str(path))
            rel = path.relative_to(root).as_posix()
            if path.is_dir():
                directories.append(rel)
            elif path.is_file():
                files[rel] = sha(path)
            else:
                raise ValueError("Nonregular resource: " + str(path))
    return {"directories": sorted(directories), "files": dict(sorted(files.items()))}


def validate_package(package):
    """Finite package integrity, not host behavior or remote-source validation.

    Required delivered references use simple inline Markdown destinations.
    Heading fragments and prose/code citations are not parsed as local resources.
    """
    package = Path(package).absolute()
    errors = []
    try:
        population = tree(package)["files"]
    except ValueError as exc:
        return [str(exc)]
    inv = package / "INVENTORY.md"
    if "INVENTORY.md" not in population:
        return ["INVENTORY.md missing"]
    expected = {}
    for line in inv.read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"\|\s*([^|]+?)\s*\|\s*([0-9a-f]{64})\s*\|", line)
        if match:
            name, digest = match.groups()
            if name in expected:
                errors.append("Duplicate inventory row: " + name)
            expected[name] = digest
    actual = {name: digest for name, digest in population.items() if name != "INVENTORY.md"}
    if not expected or expected != actual:
        errors.append("Exact inventory population or digest mismatch")
    skills = package / "skills"
    if not skills.is_dir() or set(x.name for x in skills.iterdir()) != set(NAMES):
        errors.append("Expected complete five-skill bundle")
    roots = [(skills / name).resolve() for name in NAMES]
    for name in NAMES:
        path = skills / name / "SKILL.md"
        if not path.is_file():
            errors.append("Missing skill: " + name)
            continue
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
        front = dict(re.findall(r"^([A-Za-z0-9_-]+):\s*(.*)$", match[1], re.M)) if match else {}
        if front.get("name") != name or len(front.get("description", "")) < 40:
            errors.append("Invalid name/description frontmatter: " + name)
        if front.get("disable-model-invocation", "false").lower() == "true":
            errors.append("Automatic invocation disabled: " + name)
    for rel in population:
        if not rel.startswith("skills/") or not rel.endswith(".md"):
            continue
        path = package / rel
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)\n]*)\)", text):
            target = target.strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            parsed = urlsplit(target)
            if parsed.scheme in ("http", "https", "mailto", "stdo"):
                continue  # explicitly external dependency, not delivered resource proof
            if not target or parsed.scheme or parsed.netloc or parsed.query or "\\" in target or any(c.isspace() for c in target):
                errors.append("Unsupported link destination: " + rel + " -> " + target)
                continue
            if not parsed.path and parsed.fragment:
                continue  # anchor semantics are outside this validator
            local = Path(unquote(parsed.path))
            if local.is_absolute():
                errors.append("Absolute local link: " + rel + " -> " + target)
                continue
            resolved = (path.parent / local).resolve()
            if not any(resolved.is_relative_to(root) for root in roots) or not resolved.is_file():
                errors.append("Missing or escaping local resource: " + rel + " -> " + target)
        if any(token in text for token in ("~/.claude", "$HOME/.claude", "build_tenants/codex")):
            errors.append("Other-tenant or personal-configuration dependency: " + rel)
    return errors


def checked_source(package):
    package = Path(package).absolute()
    errors = validate_package(package)
    if errors:
        raise ValueError("Package refused: " + "; ".join(errors))
    return package, {name: tree(package / "skills" / name) for name in NAMES}


def installation_paths(workspace):
    workspace = Path(workspace).absolute()
    if workspace.is_symlink() or not workspace.is_dir():
        raise ValueError("Workspace must already be a real directory")
    config, skills = workspace / ".claude", workspace / ".claude" / "skills"
    for path in (config, skills):
        if path.is_symlink() or (path.exists() and not path.is_dir()):
            raise ValueError("Refuse redirected or non-directory destination: " + str(path))
    return config, skills, config / RECEIPT


def owned_installation(skills, receipt, expected_sha):
    if not expected_sha or not re.fullmatch(r"[0-9a-f]{64}", expected_sha):
        raise ValueError("Select the recorded receipt SHA256 for update/removal")
    if receipt.is_symlink() or not receipt.is_file() or sha(receipt) != expected_sha:
        raise ValueError("Selected ownership receipt is absent or changed")
    try:
        record = json.loads(receipt.read_text(encoding="utf-8"))
    except (ValueError, UnicodeError) as exc:
        raise ValueError("Invalid ownership receipt") from exc
    if (not isinstance(record, dict) or set(record) != {"schema", "package_id", "source_inventory_sha256", "skills"}
            or record["schema"] != SCHEMA or record["package_id"] != PACKAGE_ID
            or not isinstance(record["source_inventory_sha256"], str)
            or not re.fullmatch(r"[0-9a-f]{64}", record["source_inventory_sha256"])
            or not isinstance(record["skills"], dict) or set(record["skills"]) != set(NAMES)):
        raise ValueError("Receipt does not identify this complete owned bundle")
    actual = {name: tree(skills / name) for name in NAMES}
    if actual != record["skills"]:
        raise ValueError("Installed file/directory set or content changed; preserve and reconcile")
    return record


def manage(action, workspace, package=None, receipt_sha256=None):
    config, skills, receipt = installation_paths(workspace)
    source, selected = checked_source(package) if action != "remove" else (None, None)
    if source and (source.resolve().is_relative_to(config.resolve()) or config.resolve().is_relative_to(source.resolve())):
        raise ValueError("Source package and installation destination overlap")
    if action == "install":
        if receipt.exists() or receipt.is_symlink() or any((skills / name).exists() or (skills / name).is_symlink() for name in NAMES):
            raise ValueError("Installation collision; no receipt or same-name directory may be replaced")
    elif action in ("update", "remove"):
        owned_installation(skills, receipt, receipt_sha256)
    else:
        raise ValueError("Unsupported action")
    # Every refusal above precedes mutation. Caller supplies exclusive workspace
    # access; this is not a concurrent writer or crash-atomic transaction.
    if action != "install":
        for name in NAMES:
            shutil.rmtree(skills / name)
    if action == "remove":
        receipt.unlink()
        return {"action": action, "removed_receipt_sha256": receipt_sha256}
    skills.mkdir(parents=True, exist_ok=True)
    for name in NAMES:
        shutil.copytree(source / "skills" / name, skills / name)
    actual = {name: tree(skills / name) for name in NAMES}
    if actual != selected:
        raise OSError("Installed bytes differ after copy; partial effect requires reconciliation")
    record = {"schema": SCHEMA, "package_id": PACKAGE_ID,
              "source_inventory_sha256": sha(source / "INVENTORY.md"), "skills": selected}
    receipt.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"action": action, "receipt": str(receipt), "receipt_sha256": sha(receipt),
            "source_inventory_sha256": record["source_inventory_sha256"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    for action in ("check", "install", "update", "remove"):
        command = sub.add_parser(action)
        if action != "remove":
            command.add_argument("--package", required=True, type=Path)
        if action != "check":
            command.add_argument("--workspace", required=True, type=Path)
        if action in ("update", "remove"):
            command.add_argument("--receipt-sha256", required=True)
    args = parser.parse_args()
    try:
        if args.action == "check":
            errors = validate_package(args.package)
            print(json.dumps({"status": "refused" if errors else "ok", "errors": errors}))
            return 1 if errors else 0
        result = manage(args.action, args.workspace, getattr(args, "package", None), getattr(args, "receipt_sha256", None))
        print(json.dumps({"status": "ok", **result}))
        return 0
    except ValueError as exc:
        print(json.dumps({"status": "refused", "reason": str(exc)}))
        return 1
    except OSError as exc:
        print(json.dumps({"status": "effect_uncertain", "reason": str(exc),
                          "next": "Retain receipt/current tree and reconcile; do not force or retry automatically"}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

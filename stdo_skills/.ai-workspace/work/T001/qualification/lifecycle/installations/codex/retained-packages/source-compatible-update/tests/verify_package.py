"""Read-only finite package, resource and installation-custody checks."""
import argparse
import hashlib
import json
import re
import stat
from pathlib import Path

def digest(path):
    data = path.read_bytes()
    return {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}

def safe_ancestors(path):
    for p in [path, *path.parents]:
        if p.is_symlink():
            raise ValueError("symlink refused: " + str(p))

def regulars(root):
    safe_ancestors(root)
    if not root.is_dir():
        raise ValueError("missing directory: " + str(root))
    result = {}
    for p in sorted(root.rglob("*")):
        mode = p.lstat().st_mode
        if stat.S_ISLNK(mode):
            raise ValueError("symlink refused: " + str(p))
        if stat.S_ISDIR(mode):
            continue
        if not stat.S_ISREG(mode):
            raise ValueError("nonregular entry: " + str(p))
        result[p.relative_to(root).as_posix()] = digest(p)
    return result

def check(root, installed=None, destination=None):
    actual = regulars(root)
    inventory = json.loads((root / "inventory.json").read_text())
    expected = {r["path"]: {"sha256": r["sha256"], "bytes": r["bytes"]} for r in inventory["files"]}
    if len(expected) != len(inventory["files"]):
        raise ValueError("duplicate inventory path")
    actual.pop("inventory.json", None)
    if actual != expected:
        raise ValueError("inventory mismatch: " + json.dumps({"missing": sorted(set(expected)-set(actual)), "extra": sorted(set(actual)-set(expected)), "changed": sorted(k for k in set(actual)&set(expected) if actual[k]!=expected[k])}))
    skill = root / "skills/stdo-work"
    text = (skill / "SKILL.md").read_text()
    if not text.startswith("---\n"):
        raise ValueError("missing skill frontmatter")
    front = text.split("---", 2)[1]
    if re.search(r"(?m)^name: stdo-work$", front) is None:
        raise ValueError("invalid name/folder binding")
    if re.search(r"(?m)^description: .+", front) is None:
        raise ValueError("missing description")
    link_count = 0
    for p in root.rglob("*.md"):
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", p.read_text()):
            target = link.split("#", 1)[0]
            if not target or "://" in target:
                continue
            resolved = (p.parent / target).resolve()
            boundary = skill.resolve() if p.is_relative_to(skill) else root.resolve()
            if not resolved.is_relative_to(boundary) or not resolved.is_file():
                raise ValueError("unresolvable/escaping resource: " + str(p) + " -> " + link)
            link_count += 1
    routes = json.loads((skill / "source-routes.json").read_text())
    for source in routes["sources"]:
        if not re.fullmatch("[0-9a-f]{64}", source["sha256"]):
            raise ValueError("invalid source hash")
    if installed is not None:
        current = regulars(installed)
        subset = {p[len("skills/stdo-work/"):]: v for p, v in expected.items() if p.startswith("skills/stdo-work/")}
        if current != subset:
            raise ValueError("installed custody mismatch")
    if destination is not None:
        safe_ancestors(destination)
        if destination.exists() or destination.resolve().is_relative_to(root.resolve()):
            raise ValueError("destination exists or is inside package")
        if destination.name != "stdo-work" or destination.parent.name != "skills" or destination.parent.parent.name != ".agents":
            raise ValueError("destination must be repository .agents/skills/stdo-work")
    return {"status": "passed", "files": len(actual), "local_links": link_count, "inventory_sha256": digest(root/"inventory.json")["sha256"], "installed_checked": installed is not None, "destination_checked": destination is not None, "limits": "finite bytes/metadata/resources/custody only; no semantic or actual-host qualification"}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--installed", type=Path)
    parser.add_argument("--destination", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(check(args.root.absolute(), args.installed.absolute() if args.installed else None, args.destination.absolute() if args.destination else None), sort_keys=True))
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "failed", "error": str(exc)}))
        raise SystemExit(1)

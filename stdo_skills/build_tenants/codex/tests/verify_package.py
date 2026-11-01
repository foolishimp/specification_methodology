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

def current_source_check(root, routes, repository=None):
    root = root.resolve(strict=True)
    provider = routes["representation_provider"]
    selection = provider["selection"]
    if not isinstance(selection, str) or not selection:
        raise ValueError("missing current source selection")
    current = [source for source in routes["sources"] if source.get("selection") == selection]
    matching = [source for source in current
                if (source["root"], source["path"]) == (provider["root"], provider["path"])]
    if len(matching) != 1 or matching[0]["sha256"] != provider["sha256"]:
        raise ValueError("representation provider contradicts its selected source route")
    if not re.fullmatch("[0-9a-f]{64}", provider["sha256"]):
        raise ValueError("invalid representation provider hash")
    if repository is None and len(root.parents) >= 3:
        candidate = root.parents[2]
        if root == candidate / "stdo_skills/build_tenants/codex" and (candidate / ".git").exists():
            repository = candidate
    if repository is None:
        return {"status": "not_performed", "selection": selection,
                "reason": "external source roots are not selected; package custody only"}
    repository = repository.absolute()
    safe_ancestors(repository)
    if not repository.is_dir():
        raise ValueError("missing source repository: " + str(repository))
    roots = {"product": repository / "stdo_skills", "tool": repository / "a_c"}
    checked = set()
    for source in current:
        name = source["path"]
        if (source["root"] not in roots or source.get("engine") != "workspace-regular-file"
                or source.get("object") is not None or source.get("selector") is not None):
            raise ValueError("unsupported current source route")
        if (not isinstance(name, str) or not name or Path(name).is_absolute()
                or any(part in ("", ".", "..") for part in name.split("/")) or "\\" in name):
            raise ValueError("unsafe current source path")
        path = roots[source["root"]] / name
        safe_ancestors(path)
        if not path.is_file() or not stat.S_ISREG(path.stat().st_mode):
            raise ValueError("missing current source: " + str(path))
        if digest(path)["sha256"] != source["sha256"]:
            raise ValueError("current source digest mismatch: " + source["root"] + ":" + name)
        checked.add((source["root"], name))
    return {"status": "checked", "selection": selection, "files": len(checked),
            "repository": str(repository)}

def check(root, installed=None, destination=None, repository=None):
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
    current_sources = current_source_check(root, routes, repository)
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
    return {"status": "passed", "files": len(actual), "local_links": link_count, "inventory_sha256": digest(root/"inventory.json")["sha256"], "installed_checked": installed is not None, "destination_checked": destination is not None, "current_sources": current_sources, "limits": "finite bytes/metadata/resources/custody and reported current-source checks only; no semantic or actual-host qualification"}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--installed", type=Path)
    parser.add_argument("--destination", type=Path)
    parser.add_argument("--repository", type=Path, help="construction repository for current Product/tool source pins; inferred only at its standard in-repository tenant location")
    args = parser.parse_args()
    try:
        print(json.dumps(check(args.root.absolute(), args.installed.absolute() if args.installed else None, args.destination.absolute() if args.destination else None, args.repository), sort_keys=True))
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "failed", "error": str(exc)}))
        raise SystemExit(1)

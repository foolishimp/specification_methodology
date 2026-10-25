#!/usr/bin/env python3
"""Bounded native stable-release preparation. Never performs Git writes, installs or pushes."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import stat
import subprocess
import unicodedata
from pathlib import Path, PurePosixPath

BASE = Path(__file__).resolve().parent
CUT = "v3.0.2"
PREFIX = "specification_methodology/v3"
NAMESPACE = "specification_methodology"
TAG = f"refs/tags/{NAMESPACE}/{CUT}"
PROFILE = "stable-v1"
VERSION = "3.0.2"
MANAGER_WHEEL = "stdo_toolchain-0.1.6-py3-none-any.whl"
PREDECESSOR = "fe4941f56a52ed3697a2b516d8d68948b0ea65d9"
REMOTE = "https://github.com/foolishimp/specification_methodology.git"
MANIFEST_NAME = f"stdo-{CUT}-manifest.json"
STANDING = "standalone_stable_release_preparation"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()


def inventory_digest(rows):
    vector = [{k: row[k] for k in ("path", "bytes", "sha256")} for row in rows]
    return sha(json.dumps(vector, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())


def safe_member(value):
    require(isinstance(value, str) and value and not value.startswith("/"), "invalid relative path")
    require(not any(ord(c) < 32 for c in value) and "\\" not in value, "unsafe path character")
    require(all(p not in ("", ".", "..") for p in value.split("/")), "unsafe path component")
    require(str(PurePosixPath(value)) == value, "noncanonical path")
    return value


def output_path(path):
    path = Path(path).absolute()
    require(".." not in path.parts, "output traversal refused")
    require(path.is_relative_to(BASE), "outputs must be inside this native-release territory")
    for parent in (path, *path.parents):
        require(not parent.is_symlink(), f"redirected output: {parent}")
        if parent == BASE:
            break
    return path


def save(path, data):
    path = output_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(data)


def save_json(path, value):
    data = canonical(value)
    save(path, data)
    return {"path": str(path), "sha256": sha(data)}


def read_json(path, pin=None):
    path = Path(path)
    require(path.is_file() and not path.is_symlink(), f"missing or redirected input: {path}")
    data = path.read_bytes()
    if pin is not None:
        require(sha(data) == pin, f"input digest mismatch: {path}")
    return json.loads(data)


def git(repo, *args):
    require(args and args[0] in {"rev-parse", "ls-tree", "cat-file", "show", "merge-base", "ls-remote"}, "Git mutation is reserved to Root")
    result = subprocess.run(["git", "--no-optional-locks", "-C", str(repo), *args], capture_output=True)
    require(result.returncode == 0, "read-only git failed: " + result.stderr.decode(errors="replace"))
    return result.stdout


def text_git(repo, *args):
    return git(repo, *args).decode().strip()


def commit(repo, value):
    require(re.fullmatch(r"[0-9a-f]{40}", value) is not None, "full SHA1 commit required")
    require(text_git(repo, "rev-parse", value + "^{commit}") == value, "wrong commit identity")
    return value


def tree_rows(repo, treeish):
    rows = []
    for entry in git(repo, "ls-tree", "-r", "-z", treeish).split(b"\0"):
        if not entry:
            continue
        metadata, name = entry.split(b"\t", 1)
        mode, kind, blob = metadata.decode().split()
        require(kind == "blob" and mode in ("100644", "100755"), "nonregular Git member")
        rows.append({"path": safe_member(name.decode()), "git_mode": mode, "git_blob": blob})
    return sorted(rows, key=lambda row: row["path"])


def validate_payload(rows, data):
    require(rows, "empty payload")
    seen = set()
    for row in rows:
        path = safe_member(row["path"])
        key = unicodedata.normalize("NFC", path).casefold()
        require(key not in seen, "case/Unicode duplicate path")
        seen.add(key)
        require(path.startswith(("standards/", "plugins/spec/")) or path in ("LICENSE", "release/release-note.md"), "payload extra: " + path)
    paths = {row["path"] for row in rows}
    declaration = data.get("release/release-note.md", b"").decode("utf-8")
    require(declaration.splitlines()[:1] == ["# STDO " + VERSION] and "`stable-v1`" in declaration and "`specification_methodology/" + CUT + "`" in declaration, "release declaration differs from stable cut/profile")
    required = {"LICENSE", "release/release-note.md", "standards/README.md",
                "plugins/spec/.claude-plugin/plugin.json", "plugins/spec/.codex-plugin/plugin.json"}
    require(required <= paths, "missing required native payload member")
    for path in sorted(p for p in required if p.endswith("plugin.json")):
        require(json.loads(data[path])["version"] == CUT.removeprefix("v"), "plugin version does not match target cut")


def source_inventory(repo, source_commit, source_path):
    commit(repo, source_commit)
    safe_member(source_path)
    tree = text_git(repo, "rev-parse", source_commit + ":" + source_path)
    rows = tree_rows(repo, tree)
    data = {row["path"]: git(repo, "cat-file", "blob", row["git_blob"]) for row in rows}
    validate_payload(rows, data)
    for row in rows:
        raw = data[row["path"]]
        row.update(bytes=len(raw), sha256=sha(raw))
    return tree, rows


def tag_message(selected):
    return (f"STDO {CUT}: standalone stable release\n\n"
            "STDO-Release-Profile: stable-v1\n"
            f"Frozen-Source-Commit: {selected['commit']}\n"
            f"Frozen-Source-Path: {selected['package_path']}\n"
            f"Frozen-Source-Tree: {selected['package_tree']}\n"
            f"Predecessor-Native-Commit: {PREDECESSOR}\n"
            "Scope: standalone methodology and plugin; bounded representation is supplemental.\n").encode()


def prepare(args):
    run = output_path(args.run)
    require(not run.exists(), "preserve existing run")
    commit(args.repo, PREDECESSOR)
    tree, rows = source_inventory(args.repo, args.source_commit, args.source_path)
    value = {"kind": "stdo302.native-preparation/1", "cut": CUT, "standing": STANDING,
             "source_candidate": {"commit": args.source_commit, "package_path": args.source_path, "package_tree": tree},
             "native_parent": PREDECESSOR, "files": rows, "file_count": len(rows),
             "total_bytes": sum(row["bytes"] for row in rows), "inventory_sha256": inventory_digest(rows)}
    info = b"".join(f"{row['git_mode']} {row['git_blob']}\t{PREFIX}/{row['path']}\0".encode() for row in rows)
    message = (f"STDO {CUT} standalone native stable release\n\n"
               f"Frozen-Source-Commit: {args.source_commit}\nFrozen-Source-Path: {args.source_path}\n"
               f"Frozen-Source-Tree: {tree}\nPredecessor-Native-Commit: {PREDECESSOR}\n"
               "Profile: stable-v1; no automatic consumer adoption\n")
    result = save_json(run / "source.json", value)
    save(run / "native-index-info.z", info)
    save(run / "native-commit-message.txt", message.encode())
    save(run / "tag-message.txt", tag_message(value["source_candidate"]))
    return result


def load_source(args):
    run = output_path(args.run)
    source = read_json(run / "source.json", args.source_sha256)
    require(source["cut"] == CUT and source["native_parent"] == PREDECESSOR, "wrong preparation identity")
    selected = source["source_candidate"]
    tree, rows = source_inventory(args.repo, selected["commit"], selected["package_path"])
    require(tree == selected["package_tree"] and rows == source["files"], "source selection no longer matches immutable Git")
    require(inventory_digest(rows) == source["inventory_sha256"], "source inventory digest mismatch")
    return run, source


def native_facts(repo, native_commit, source):
    commit(repo, native_commit)
    require(text_git(repo, "show", "-s", "--format=%P", native_commit).split() == [PREDECESSOR], "native commit must have exactly the selected native predecessor parent")
    expected = [{"path": PREFIX + "/" + row["path"], "git_blob": row["git_blob"], "git_mode": row["git_mode"]} for row in source["files"]]
    require(tree_rows(repo, native_commit) == expected, "native root has changed bytes, paths, modes, omissions or extra payload")
    message = text_git(repo, "show", "-s", "--format=%B", native_commit)
    selected = source["source_candidate"]
    for label, value in (("Frozen-Source-Commit", selected["commit"]), ("Frozen-Source-Path", selected["package_path"]), ("Frozen-Source-Tree", selected["package_tree"]), ("Predecessor-Native-Commit", PREDECESSOR)):
        require(f"{label}: {value}" in message.splitlines(), "native source relation trailer missing: " + label)
    require(text_git(repo, "cat-file", "-t", TAG) == "tag", "native cut must be an annotated tag")
    require(text_git(repo, "rev-parse", TAG + "^{commit}") == native_commit, "native tag peels to wrong commit")
    annotation = git(repo, "cat-file", "-p", TAG).split(b"\n\n", 1)
    require(len(annotation) == 2 and annotation[1] == tag_message(selected), "native annotation differs from selected source/predecessor/stable profile")
    return {"commit": native_commit, "cut": CUT, "qualified_ref": TAG,
            "tag_object": text_git(repo, "rev-parse", TAG), "parent": PREDECESSOR,
            "tree": text_git(repo, "rev-parse", native_commit + "^{tree}"),
            "package_path": PREFIX, "package_tree": text_git(repo, "rev-parse", native_commit + ":" + PREFIX),
            "standards_tree": text_git(repo, "rev-parse", native_commit + ":" + PREFIX + "/standards")}


def attest(args):
    run, source = load_source(args)
    native = native_facts(args.repo, args.native_commit, source)
    return save_json(run / "native.json", {"kind": "stdo302.native-identity/1", "source_sha256": args.source_sha256, "native": native, "standing": STANDING})


def expected_manifest(source, native):
    def members(prefix):
        return [{"path": row["path"][len(prefix):], "sha256": row["sha256"]} for row in source["files"] if row["path"].startswith(prefix)]
    standards, plugins = members("standards/"), members("plugins/spec/")
    by_path = {row["path"]: row for row in source["files"]}
    release = {key: native[key] for key in ("cut", "commit", "tag_object", "tree", "standards_tree", "qualified_ref")}
    release.update(profile=PROFILE, project_release_namespace=NAMESPACE, project_subtree_root=PREFIX, project_subtree_tree=native["package_tree"])
    digest = sha("".join(f"{row['sha256']}  specification/standards/{row['path']}\n" for row in standards).encode())
    return {"kind": "stdo.installed-release-manifest", "schema_version": 1, "release": release,
            "standards": {"source_root": "specification/standards", "installed_root": "standards", "member_count": len(standards), "member_set_sha256": digest, "members": standards},
            "auxiliary": {"plugin": {"source_root": "plugins/spec", "installed_root": "plugins/spec", "member_count": len(plugins), "members": plugins},
                          "license": {"path": "LICENSE", "sha256": by_path["LICENSE"]["sha256"]},
                          "release_note": {"source_path": "releases/v3.0.2.md", "installed_path": "release/release-note.md", "sha256": by_path["release/release-note.md"]["sha256"]}}}


def seal(args):
    run, source = load_source(args)
    record = read_json(run / "native.json", args.native_sha256)
    require(record["source_sha256"] == args.source_sha256, "native/source receipt mismatch")
    native = native_facts(args.repo, record["native"]["commit"], source)
    require(native == record["native"], "native identity changed")
    report = read_json(args.manifest_report)
    expected = expected_manifest(source, native)
    require(report["manifest"] == expected, "manager manifest differs from exact native inventory/identity")
    raw = canonical(report["manifest"])
    digest = sha(raw)
    require(report["manifest_sha256"] == digest, "manager manifest digest differs from canonical bytes")
    asset = run / MANIFEST_NAME
    require(asset.is_relative_to(Path(args.repo).resolve()), "use the 302 worktree as --repo so manifest_path is repository-relative")
    native.update(manifest_sha256=digest, manifest_path=asset.relative_to(Path(args.repo).resolve()).as_posix())
    selection = {"kind": "a_c.stdo302.native-source-selection/1", "source_candidate": source["source_candidate"],
                 "native": native, "subject_uri": "repo://stdo-v3-native/" + native["commit"],
                 "files": source["files"], "inventory_sha256": source["inventory_sha256"],
                 "file_count": source["file_count"], "total_bytes": source["total_bytes"], "standing": STANDING}
    save(asset, raw)
    save(run / (MANIFEST_NAME + ".sha256"), f"{digest}  {MANIFEST_NAME}\n".encode())
    return save_json(run / "SOURCE_SELECTION.json", selection)


def disk_files(root):
    root = Path(root)
    require(root.is_dir() and not root.is_symlink(), "missing or redirected directory")
    result = {}
    for path in sorted(root.rglob("*")):
        mode = path.lstat().st_mode
        require(not stat.S_ISLNK(mode), "redirected file/directory")
        if stat.S_ISDIR(mode):
            continue
        require(stat.S_ISREG(mode), "special file")
        raw = path.read_bytes()
        result[path.relative_to(root).as_posix()] = {"bytes": len(raw), "sha256": sha(raw)}
    return result


def compare_files(actual, expected):
    require(set(actual) == set(expected), "file membership differs (omission or extra)")
    require(actual == expected, "file bytes differ")


def installed(args):
    run = output_path(args.run)
    selection = read_json(run / "SOURCE_SELECTION.json", args.selection_sha256)
    store = output_path(args.store)
    root = store / "releases" / CUT
    report = read_json(args.verify_report)
    manifest = (run / MANIFEST_NAME).read_bytes()
    require(sha(manifest) == selection["native"]["manifest_sha256"], "canonical asset changed")
    require(report["valid"] is True and report["failures"] == [] and report["cut"] == CUT, "installed verifier did not pass")
    require(Path(report["path"]).resolve() == root.resolve(), "verifier report covers another store")
    require(report["manifest_sha256"] == sha(manifest) and report["manifest"] == json.loads(manifest), "verifier manifest/identity differs")
    expected = {row["path"]: {"bytes": row["bytes"], "sha256": row["sha256"]} for row in selection["files"]}
    expected["manifest.json"] = {"bytes": len(manifest), "sha256": sha(manifest)}
    compare_files(disk_files(root), expected)
    return save_json(run / ("installed-" + args.label + ".json"), {"kind": "stdo302.installed-byte-proof/1", "selection_sha256": args.selection_sha256,
                     "commit": selection["native"]["commit"], "manifest_sha256": sha(manifest), "store": str(store),
                     "files": len(expected), "exact_payload_and_manifest": True, "standing": STANDING,
                     "limits": "Exact bytes and installer verification only; no semantic acceptance, task-use or adoption claim."})


def assets(args):
    run = output_path(args.run)
    selected = read_json(run / "SOURCE_SELECTION.json", args.selection_sha256)
    rows = []
    for raw_path in args.file:
        path = Path(raw_path).resolve()
        require(Path(raw_path).is_file() and not Path(raw_path).is_symlink(), "missing/redirected asset")
        require(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", path.name) is not None, "unsafe asset name")
        raw = path.read_bytes()
        rows.append({"name": path.name, "path": str(path), "bytes": len(raw), "sha256": sha(raw)})
    require(len({row["name"] for row in rows}) == len(rows), "duplicate asset name")
    require(MANIFEST_NAME in {row["name"] for row in rows}, "native canonical manifest asset missing")
    require(next(row["sha256"] for row in rows if row["name"] == MANIFEST_NAME) == selected["native"]["manifest_sha256"], "asset manifest is not selected native manifest")
    require(any(row["name"].endswith(".tar.gz") for row in rows), "selected supplemental representation archive missing")
    require(MANAGER_WHEEL in {row["name"] for row in rows}, "selected manager wheel missing")
    require(not any(row["name"].endswith(".sha256") for row in rows), "supply primary assets; sidecars are generated")
    for row in list(rows):
        sidecar = f"{row['sha256']}  {row['name']}\n".encode()
        path = run / "asset-checksums" / (row["name"] + ".sha256")
        save(path, sidecar)
        rows.append({"name": path.name, "path": str(path), "bytes": len(sidecar), "sha256": sha(sidecar)})
    return save_json(run / "assets.json", {"kind": "stdo302.public-assets/1", "cut": CUT, "selection_sha256": args.selection_sha256, "files": sorted(rows, key=lambda r: r["name"])})


def check_assets(args):
    run = output_path(args.run)
    selected = read_json(run / "assets.json", args.assets_sha256)
    expected = {row["name"]: {"bytes": row["bytes"], "sha256": row["sha256"]} for row in selected["files"]}
    compare_files(disk_files(args.directory), expected)
    return save_json(run / "public-download-proof.json", {"kind": "stdo302.public-download-proof/1", "assets_sha256": args.assets_sha256, "files": len(expected), "exact_downloads": True, "standing": STANDING})


def remote_refs(repo):
    refs = {}
    for line in git(repo, "ls-remote", REMOTE).decode().splitlines():
        oid, ref = line.split("\t")
        if ref.startswith("refs/"):
            refs[ref] = oid
    return refs


def stable_line_available(refs):
    historical_bare = f"refs/tags/v{VERSION}"
    rc_prefixes = (f"refs/tags/v{VERSION}-rc.", f"refs/tags/{NAMESPACE}/v{VERSION}-rc.")
    require(not any(ref == historical_bare or ref == historical_bare + "^{}" or ref.startswith(rc_prefixes) for ref in refs),
            "stable line collides with historical bare tag or RC history")


def publication_plan(args):
    run = output_path(args.run)
    selected = read_json(run / "SOURCE_SELECTION.json", args.selection_sha256)
    local = read_json(run / "installed-local.json")
    require(local["selection_sha256"] == args.selection_sha256 and local["exact_payload_and_manifest"] is True, "current local install proof missing")
    canonical_asset = (run / MANIFEST_NAME).read_bytes()
    require(sha(canonical_asset) == selected["native"]["manifest_sha256"], "canonical manifest asset changed")
    expected_files = {row["path"]: {"bytes": row["bytes"], "sha256": row["sha256"]} for row in selected["files"]}
    expected_files["manifest.json"] = {"bytes": len(canonical_asset), "sha256": sha(canonical_asset)}
    compare_files(disk_files(output_path(local["store"]) / "releases" / CUT), expected_files)
    asset_record = read_json(run / "assets.json", args.assets_sha256)
    require(asset_record["selection_sha256"] == args.selection_sha256, "assets select another native source")
    for row in asset_record["files"]:
        path = Path(row["path"])
        require(path.is_file() and not path.is_symlink(), "asset absent or redirected")
        raw = path.read_bytes()
        require(len(raw) == row["bytes"] and sha(raw) == row["sha256"], "asset changed after freeze")
    candidate = commit(args.repo, args.carrier_commit)
    git(args.repo, "merge-base", "--is-ancestor", selected["source_candidate"]["commit"], candidate)
    native = selected["native"]
    facts = native_facts(args.repo, native["commit"], selected)
    require(all(native[k] == value for k, value in facts.items()), "native selection changed")
    require(text_git(args.repo, "rev-parse", TAG) == native["tag_object"], "native tag changed")
    sources = {"refs/heads/main": candidate, TAG: native["tag_object"]}
    release_ref = f"refs/heads/release/{NAMESPACE}/{VERSION}"
    require(text_git(args.repo, "rev-parse", release_ref) == native["commit"], "native release branch has wrong target")
    sources[release_ref] = native["commit"]
    observed = remote_refs(args.repo)
    require(TAG not in observed, "immutable destination already exists; reconcile instead of replacing")
    stable_line_available(observed)
    require("refs/heads/main" in observed, "remote main missing")
    git(args.repo, "merge-base", "--is-ancestor", observed["refs/heads/main"], candidate)
    require(all(ref == "refs/heads/main" or ref not in observed for ref in sources), "new-line destination exists; reconcile before qualification")
    expected = {ref: observed.get(ref, "") for ref in sources}
    argv = ["git", "-C", str(Path(args.repo).resolve()), "push", "--atomic"]
    argv += [f"--force-with-lease={ref}:{expected[ref]}" for ref in sorted(sources)]
    argv += [REMOTE] + [f"{sources[ref]}:{ref}" for ref in sorted(sources)]
    return save_json(run / "publication-plan.json", {"kind": "stdo302.atomic-publication-plan/1", "repository": REMOTE,
                     "selection_sha256": args.selection_sha256, "assets_sha256": args.assets_sha256, "native_commit": native["commit"], "sources": sources,
                     "expected_remote": expected, "remote_before": observed, "push_argv": argv,
                     "standing": "prepared_not_executed", "limits": "No publication authority or semantic acceptance is granted by this plan."})


def published(args):
    run = output_path(args.run)
    plan = read_json(run / "publication-plan.json", args.plan_sha256)
    now = remote_refs(args.repo)
    for ref, oid in plan["sources"].items():
        require(now.get(ref) == oid, "published direct ref differs: " + ref)
    for ref in (TAG,):
        require(now.get(ref + "^{}") == plan["native_commit"], "published tag is not annotated or peels differently")
    changed = set(plan["sources"]) | {TAG + "^{}"}
    before_other = {k: v for k, v in plan["remote_before"].items() if k not in changed}
    after_other = {k: v for k, v in now.items() if k not in changed}
    require(before_other == after_other, "unrelated remote refs changed; reconcile and do not assert full preservation")
    return save_json(run / "published-refs.json", {"kind": "stdo302.remote-ref-proof/1", "plan_sha256": args.plan_sha256,
                     "remote": REMOTE, "refs": {ref: now[ref] for ref in sorted(changed)}, "unrelated_refs_preserved": True,
                     "standing": "published_stable_refs_verified"})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    def command(name, callback):
        p = sub.add_parser(name)
        p.add_argument("--run", type=Path, required=True)
        p.set_defaults(callback=callback)
        return p
    p = command("prepare", prepare)
    p.add_argument("--repo", type=Path, required=True)
    p.add_argument("--source-commit", required=True)
    p.add_argument("--source-path", required=True)
    for name, callback in (("attest", attest), ("seal", seal)):
        p = command(name, callback)
        p.add_argument("--repo", type=Path, required=True)
        p.add_argument("--source-sha256", required=True)
        if name == "attest":
            p.add_argument("--native-commit", required=True)
        else:
            p.add_argument("--native-sha256", required=True)
            p.add_argument("--manifest-report", type=Path, required=True)
    p = command("installed", installed)
    p.add_argument("--selection-sha256", required=True)
    p.add_argument("--store", type=Path, required=True)
    p.add_argument("--verify-report", type=Path, required=True)
    p.add_argument("--label", choices=("local", "public"), required=True)
    p = command("assets", assets)
    p.add_argument("--selection-sha256", required=True)
    p.add_argument("--file", type=Path, action="append", required=True)
    p = command("check-assets", check_assets)
    p.add_argument("--assets-sha256", required=True)
    p.add_argument("--directory", type=Path, required=True)
    p = command("publication-plan", publication_plan)
    p.add_argument("--repo", type=Path, required=True)
    p.add_argument("--selection-sha256", required=True)
    p.add_argument("--carrier-commit", required=True)
    p.add_argument("--assets-sha256", required=True)
    p = command("published", published)
    p.add_argument("--repo", type=Path, required=True)
    p.add_argument("--plan-sha256", required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(args.callback(args), sort_keys=True))
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
        parser.exit(1, f"refused: {exc}\n")


if __name__ == "__main__":
    main()

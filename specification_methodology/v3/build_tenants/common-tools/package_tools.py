#!/usr/bin/env python3
"""Bounded standalone-package checks and canonical installed-layout construction.

Run with Python's -I option. This file imports only the Python standard library;
it never imports or executes code from the candidate or a project helper.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import unicodedata
from urllib.parse import unquote, urlsplit


INVENTORY_KIND = "stdo.common-package-freeze"
POLICY = "standalone-v3-publication-1"
HEX256 = re.compile(r"[0-9a-f]{64}\Z")
GIT_OBJECT = re.compile(r"[0-9a-f]{40}(?:[0-9a-f]{24})?\Z")
TEXT_SUFFIXES = {".md", ".json", ".yaml", ".yml", ".txt"}
ADVISORIES = (
    r"baseline result family",
    r"owns? (?:the )?(?:shared |core )?result algebra",
    r"complete Product view",
    r"result algebra is",
    r"\b(?:REFERENCE_FRAME_METHOD|STDO_REFERENCE_FRAME_BASELINE|"
    r"WORLD_MODEL_METHOD|ODD_METHOD|DESIGN_MODULE_METHOD|TICKET_METHOD|"
    r"RELEASE_METHOD|GLOSSARY_GUIDE)\.md\b",
    r"generated_by\s*:",
    r"generated_at\s*:",
)


class CheckError(Exception):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def encoded(value: object) -> bytes:
    # Match the installed toolchain's canonical_json_bytes, including escaping.
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()


def strict_json(data: bytes):
    def object_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise CheckError(f"duplicate JSON key: {key}")
            result[key] = value
        return result

    def bad_constant(value):
        raise CheckError(f"non-JSON numeric constant: {value}")

    try:
        return json.loads(data, object_pairs_hook=object_pairs, parse_constant=bad_constant)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CheckError(f"invalid JSON: {exc}") from exc


def relative(value: str) -> str:
    if not isinstance(value, str) or not value or "\\" in value:
        raise CheckError(f"invalid package-relative path: {value!r}")
    path = PurePosixPath(value)
    if path.is_absolute() or any(p in {"", ".", ".."} for p in value.split("/")):
        raise CheckError(f"unsafe package-relative path: {value!r}")
    if any(ord(ch) < 32 for ch in value) or ":" in value:
        raise CheckError(f"unsupported package-relative path: {value!r}")
    return value


def physical_file(path: Path) -> bytes:
    if not stat.S_ISREG(path.lstat().st_mode):
        raise CheckError(f"expected a physical regular file: {path}")
    with path.open("rb") as source:
        before = os.fstat(source.fileno())
        content = source.read()
        after = os.fstat(source.fileno())
    current = path.lstat()
    identity = lambda value: (value.st_dev, value.st_ino, value.st_size, value.st_mtime_ns)
    if not stat.S_ISREG(current.st_mode) or identity(before) != identity(after) or identity(after) != identity(current):
        raise CheckError(f"file changed while being read: {path}")
    return content


def snapshot(root: Path):
    """Read every physical regular file once; reject every redirect/special entry."""
    if not stat.S_ISDIR(root.lstat().st_mode):
        raise CheckError(f"package root must be a physical directory: {root}")
    payload = {}
    directories = []
    folded = {}

    def walk(directory: Path):
        with os.scandir(directory) as entries:
            children = sorted(entries, key=lambda entry: entry.name)
        for entry in children:
            path = Path(entry.path)
            name = relative(path.relative_to(root).as_posix())
            portable = unicodedata.normalize("NFC", name).casefold()
            if portable in folded:
                raise CheckError(f"duplicate portable member identity: {folded[portable]} / {name}")
            folded[portable] = name
            mode = entry.stat(follow_symlinks=False).st_mode
            if stat.S_ISLNK(mode):
                raise CheckError(f"symlink forbidden (including broken and directory links): {name}")
            if stat.S_ISDIR(mode):
                directories.append(name)
                walk(path)
            elif stat.S_ISREG(mode):
                payload[name] = physical_file(path)
            else:
                raise CheckError(f"special filesystem entry forbidden: {name}")

    walk(root)
    return payload, sorted(directories)


def inventory(payload, directories):
    return {
        "kind": INVENTORY_KIND,
        "schema_version": 1,
        "publication_policy": POLICY,
        "member_count": len(payload),
        "directories": directories,
        "members": [
            {"path": name, "bytes": len(data), "sha256": sha(data)}
            for name, data in sorted(payload.items())
        ],
    }


def pinned_json(path: Path, expected: str):
    if HEX256.fullmatch(expected) is None:
        raise CheckError("expected SHA256 must be 64 lowercase hexadecimal characters")
    data = physical_file(path)
    if sha(data) != expected:
        raise CheckError(f"pinned input digest mismatch: {path}")
    return strict_json(data)


def identity_failures(frozen, actual):
    if not isinstance(frozen, dict) or frozen.get("kind") != INVENTORY_KIND or frozen.get("schema_version") != 1:
        raise CheckError("unsupported frozen inventory kind/version")
    if frozen.get("publication_policy") != POLICY:
        raise CheckError("inventory does not select this publication policy")
    members = frozen.get("members")
    directories = frozen.get("directories")
    if not isinstance(members, list) or not isinstance(directories, list):
        raise CheckError("inventory must declare members and directories")
    names = []
    for member in members:
        if not isinstance(member, dict) or set(member) != {"path", "bytes", "sha256"}:
            raise CheckError("invalid inventory member shape")
        names.append(relative(member["path"]))
        if not isinstance(member["sha256"], str) or HEX256.fullmatch(member["sha256"]) is None:
            raise CheckError("invalid inventory member SHA256")
        if type(member["bytes"]) is not int or member["bytes"] < 0:
            raise CheckError("invalid inventory member byte count")
    if len(set(names)) != len(names) or names != sorted(names):
        raise CheckError("duplicate or unsorted inventory members")
    if frozen.get("member_count") != len(names):
        raise CheckError("inventory member_count mismatch")
    for directory in directories:
        relative(directory)
    if directories != sorted(set(directories)):
        raise CheckError("duplicate or unsorted inventory directories")
    before = {m["path"]: m for m in members}
    after = {m["path"]: m for m in actual["members"]}
    failures = []
    for name in sorted(before.keys() - after.keys()):
        failures.append({"check": "identity", "path": name, "message": "missing member"})
    for name in sorted(after.keys() - before.keys()):
        failures.append({"check": "identity", "path": name, "message": "extra member"})
    for name in sorted(before.keys() & after.keys()):
        if before[name] != after[name]:
            failures.append({"check": "identity", "path": name, "message": "member bytes/digest changed"})
    if directories != actual["directories"]:
        failures.append({"check": "identity", "path": ".", "message": "directory membership changed"})
    return failures


def visible_markdown(text: str, *, strip_inline_code=True) -> str:
    """Keep line numbers while removing fenced examples, comments and inline code."""
    lines = text.splitlines(keepends=True)
    fence = None
    for index, line in enumerate(lines):
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if fence:
            lines[index] = "\n" if line.endswith("\n") else ""
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence):
                fence = None
        elif match:
            fence = match[1]
            lines[index] = "\n" if line.endswith("\n") else ""
    value = "".join(lines)
    value = re.sub(r"<!--[\s\S]*?-->", lambda m: "\n" * m[0].count("\n"), value)
    if strip_inline_code:
        return re.sub(r"(`+)([^`\n]*?)\1", lambda m: " " * len(m[0]), value)
    return value.replace("`", "")


def anchors(text: str):
    # Heading text keeps inline-code content, which participates in GFM ids.
    lines = text.splitlines()
    result = set(re.findall(r"<(?:a|[^\s>]+)\b[^>]*\b(?:id|name)=[\"']([^\"']+)[\"']", text, re.I))
    counts = {}
    fence = None
    headings = []
    for index, line in enumerate(lines):
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            if fence is None:
                fence = marker[1]
            elif marker[1][0] == fence[0] and len(marker[1]) >= len(fence):
                fence = None
            continue
        if fence:
            continue
        heading = re.match(r"^ {0,3}#{1,6}\s+(.*?)\s*#*\s*$", line)
        if heading:
            headings.append(heading[1])
        elif index and re.fullmatch(r" {0,3}(?:=+|-+)\s*", line) and lines[index - 1].strip():
            headings.append(lines[index - 1].strip())
    for heading in headings:
        heading = re.sub(r"<[^>]*>", "", html.unescape(heading)).lower()
        heading = re.sub(r"!?\[([^]]*)\]\([^)]*\)", r"\1", heading)
        value = "".join(ch for ch in heading if ch.isalnum() or ch in " _-")
        value = value.replace(" ", "-")
        suffix = counts.get(value, 0)
        counts[value] = suffix + 1
        result.add(value + (f"-{suffix}" if suffix else ""))
    return result


def markdown_references(text: str):
    visible = visible_markdown(text)
    definitions = {}
    references = []
    normalize = lambda value: " ".join(value.casefold().split())
    destination = r"(<[^>\n]+>|(?:\\.|[^\s()]|\([^()\n]*\))+)"
    for match in re.finditer(r"(?m)^ {0,3}\[([^]\n]+)\]:\s*" + destination, visible):
        definitions[normalize(match[1])] = match[2].strip("<>")
        references.append((match.start(), match[2].strip("<>")))
    for match in re.finditer(r"!?\[[^]\n]*\]\(\s*" + destination, visible):
        references.append((match.start(), match[1].strip("<>")))
    for match in re.finditer(r"!?\[([^]\n]+)\]\[([^]\n]*)\]", visible):
        label = normalize(match[2] or match[1])
        references.append((match.start(), definitions.get(label, "UNRESOLVED_REFERENCE:" + label)))
    for match in re.finditer(r"\[[^]\n]+\](?![(:\[])", visible):
        label = normalize(match[0][1:-1])
        if label in definitions:
            references.append((match.start(), definitions[label]))
    for match in re.finditer(r"\b(?:href|src)\s*=\s*[\"']([^\"']+)[\"']", visible, re.I):
        references.append((match.start(), match[1]))
    for match in re.finditer(r"<([^<>\s]+(?:\.md|\.json)(?:#[^<>\s]*)?)>", visible):
        references.append((match.start(), match[1]))
    return [(visible.count("\n", 0, start) + 1, target) for start, target in sorted(set(references))]


def local_target(source: str, target: str, *, root_relative=False):
    target = html.unescape(target)
    if target.startswith("UNRESOLVED_REFERENCE:"):
        raise CheckError(target)
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        if parsed.scheme.casefold() in {"file", "vscode"}:
            raise CheckError(f"non-package filesystem route: {target}")
        return None
    name = unquote(parsed.path)
    if "\\" in name or any(ord(ch) < 32 for ch in name):
        raise CheckError(f"invalid local reference: {target}")
    if name.startswith("/"):
        raise CheckError(f"absolute local reference: {target}")
    if re.search(r"(?:<[^>]+>|\{[^}]+\}|REPLACE_WITH|replace-me)", name):
        return None
    parts = [] if root_relative and name else list(PurePosixPath(source).parent.parts)
    if not name:
        return source, unquote(parsed.fragment)
    for part in name.split("/"):
        if part in {"", "."}:
            continue
        if part == "..":
            if not parts:
                raise CheckError(f"local reference escapes package: {target}")
            parts.pop()
        else:
            parts.append(part)
    return "/".join(parts), unquote(parsed.fragment)


def metadata_findings(name: str, text: str):
    # Concrete history and stale entry metadata only; no generic Author/Date ban.
    template = "/templates/" in name
    visible = visible_markdown(text, strip_inline_code=False) if name.endswith(".md") else text
    findings = []
    for number, line in enumerate(visible.splitlines(), 1):
        rules = []
        if re.search(r"(?<![\w-])(?:\.ai-workspace/(?:comments/(?:claude|codex)/|common-build/)|build_tenants/(?:claude|codex)/|qualification/C3/|a_c/i\d+/|design/(?:CONSTRUCTION_BINDING|REDUCTION)\.md)", line):
            rules.append("construction-history route")
        if re.search(r"(?:stdo://releases/v[012](?:\.|/)|releases/v[012]\.[^\s)]+|(?:^|[/\s(])v[12]/specification/)", line, re.I):
            rules.append("prior-version route")
        if not template and (re.match(r"^\s{0,3}#{1,6}\s", line) or re.match(r"^\s*(?:\*\*)?(?:Status|Version|Basis|Source|Revision|Candidate)(?:\*\*)?\s*:", line, re.I)):
            if re.search(r"\b(?:RC\s*\d+|under construction|C3[- ]I\d|iteration\s+\d|v[012]\.\d)", line, re.I):
                rules.append("stale construction/version header")
            if ".ai-workspace/" in line:
                rules.append("construction-record header route")
        for rule in rules:
            findings.append({"check": "metadata", "path": name, "line": number, "message": rule, "text": line.strip()})
    return findings


def surface_checks(payload, directories):
    failures, advisory, external = [], [], []
    texts, parsed_json, index = {}, {}, {}
    for name, data in payload.items():
        if PurePosixPath(name).suffix in TEXT_SUFFIXES or PurePosixPath(name).name == "LICENSE":
            try:
                texts[name] = data.decode("utf-8")
            except UnicodeDecodeError as exc:
                failures.append({"check": "text", "path": name, "message": str(exc)})
        if name.endswith(".json"):
            try:
                parsed_json[name] = strict_json(data)
            except CheckError as exc:
                failures.append({"check": "json", "path": name, "message": str(exc)})
        if name.endswith(".md") and name in texts:
            index[name] = anchors(texts[name])
    for name, text in texts.items():
        failures.extend(metadata_findings(name, text))
        visible_lines = (visible_markdown(text, strip_inline_code=False) if name.endswith(".md") else text).splitlines()
        for number, line in enumerate(text.splitlines(), 1):
            for pattern in ADVISORIES:
                if re.search(pattern, line, re.I):
                    context = "template" if "/templates/" in name else "quoted_text" if line.lstrip().startswith(">") else "example_or_comment" if number > len(visible_lines) or not visible_lines[number - 1].strip() else "visible_text"
                    advisory.append({"path": name, "line": number, "pattern": pattern, "text": line.strip(), "context": context, "standing": "advisory search signal; requires semantic review"})

    checked = 0

    def check_reference(source, target, location, *, root_relative=False):
        nonlocal checked
        try:
            result = local_target(source, target, root_relative=root_relative)
            if result is None:
                external.append({"path": source, "location": location, "target": target})
                return
            checked += 1
            name, fragment = result
            if name not in payload and name not in directories:
                raise CheckError(f"missing local target: {target}")
            if fragment:
                if name in parsed_json and fragment.startswith("/"):
                    value = parsed_json[name]
                    for part in fragment[1:].split("/"):
                        part = part.replace("~1", "/").replace("~0", "~")
                        if isinstance(value, list):
                            if re.fullmatch(r"0|[1-9][0-9]*", part) is None:
                                raise CheckError(f"invalid JSON pointer array index: {part}")
                            value = value[int(part)]
                        else:
                            value = value[part]
                elif name not in index or fragment not in index[name]:
                    raise CheckError(f"missing or unsupported local anchor: {target}")
        except (CheckError, KeyError, IndexError, ValueError, TypeError) as exc:
            failures.append({"check": "reference", "path": source, "location": location, "target": target, "message": str(exc)})

    for name, text in texts.items():
        if name.endswith(".md"):
            for number, target in markdown_references(text):
                check_reference(name, target, f"line {number}")

    def json_routes(source, value, pointer=""):
        if isinstance(value, list):
            for offset, item in enumerate(value):
                json_routes(source, item, f"{pointer}/{offset}")
        elif isinstance(value, dict):
            for key, item in value.items():
                position = f"{pointer}/{key}"
                if isinstance(item, str):
                    if key == "$ref":
                        check_reference(source, item, position)
                    elif key in {"path", "owner", "uri", "source", "file", "member", "href"} and (
                        item.startswith(("standards/", "plugins/"))
                        or "/templates/" not in source and (
                            item.startswith(("/", "./", "../"))
                            or re.search(r"\.(?:md|json|yaml|yml)(?:#.*)?$", item)
                        )
                    ):
                        target = item
                        if isinstance(value.get("anchor"), str):
                            target += "#" + value["anchor"]
                        check_reference(source, target, position, root_relative=item.startswith(("standards/", "plugins/")))
                json_routes(source, item, position)

    for name, value in parsed_json.items():
        json_routes(name, value)
    return {
        "failures": failures,
        "advisory_signals": advisory,
        "parsed_json_count": len(parsed_json),
        "checked_local_reference_count": checked,
        "external_or_template_references": external,
        "reference_scope": "Markdown inline/reference/HTML links outside code examples; JSON $ref, explicit standards/plugins routes and non-template path-shaped fields. Prose and generated-project paths require review.",
    }


def checked_snapshot(root, freeze_path, digest):
    frozen = pinned_json(freeze_path, digest)
    payload, directories = snapshot(root)
    actual = inventory(payload, directories)
    report = surface_checks(payload, directories)
    report["failures"] = identity_failures(frozen, actual) + report["failures"]
    report.update({
        "kind": "stdo.common-package-check",
        "publication_policy": POLICY,
        "package_root": str(root.absolute()),
        "inventory_sha256": digest,
        "member_count": len(payload),
        "empty_directories": [name for name in directories if not any(path.startswith(name + "/") for path in payload)],
        "checker_sha256": globals().get("__authenticated_checker_sha256__", sha(Path(__file__).read_bytes())),
        "checker_authentication": "pinned inline launcher before execution" if "__authenticated_checker_sha256__" in globals() else "not attested by this invocation; use the pinned inline launcher",
        "project_helpers": [],
        "valid": not report["failures"],
        "standing": "mechanical package checks only; no semantic qualification, acceptance or installation",
    })
    return payload, report


def canonical_standards_digest(members):
    return sha("".join(
        f"{item['sha256']}  specification/standards/{item['path']}\n"
        for item in sorted(members, key=lambda item: item["path"])
    ).encode())


def build_manifest(payload, coordinates):
    """Coordinates are supplied by the caller; they do not prove Git objects exist."""
    if not isinstance(coordinates, dict) or set(coordinates) != {"release", "release_note"}:
        raise CheckError("coordinates must contain exactly release and release_note")
    release = coordinates["release"]
    keys = {"cut", "tag_object", "commit", "tree", "standards_tree", "project_release_namespace", "qualified_ref", "project_subtree_root", "project_subtree_tree"}
    if not isinstance(release, dict) or set(release) != keys:
        raise CheckError(f"explicit release coordinates required: {sorted(keys)}")
    if not isinstance(release["cut"], str) or re.fullmatch(r"v3\.(?!.*-rc\..*-rc\.)[0-9A-Za-z._+-]*-rc\.[1-9][0-9]*", release["cut"]) is None:
        raise CheckError("cut must be an explicit V3 RC coordinate compatible with the installed manifest schema")
    for key in ("tag_object", "commit", "tree", "standards_tree", "project_subtree_tree"):
        if not isinstance(release[key], str) or GIT_OBJECT.fullmatch(release[key]) is None:
            raise CheckError(f"invalid explicit Git object coordinate: {key}")
    if release["project_release_namespace"] != "specification_methodology" or release["project_subtree_root"] != "specification_methodology/v3":
        raise CheckError("installed V3 verifier requires namespace specification_methodology and subtree specification_methodology/v3")
    if release["qualified_ref"] != f"refs/tags/{release['project_release_namespace']}/{release['cut']}":
        raise CheckError("qualified_ref must match the explicit namespace and cut")
    note = coordinates["release_note"]
    if not isinstance(note, dict) or set(note) != {"package_path", "source_path", "installed_path"}:
        raise CheckError("release_note requires explicit package_path, source_path and installed_path")
    for value in note.values():
        relative(value)
    if note["installed_path"] != "release/release-note.md" or note["package_path"] != note["installed_path"]:
        raise CheckError("canonical materialization requires release/release-note.md at the same package and installed path")
    if re.fullmatch(r"releases/v[^/]+\.md", note["source_path"]) is None:
        raise CheckError("release_note source_path must name the prospective releases/v*.md source")
    expected_note = f"releases/{release['cut'].rsplit('-rc.', 1)[0]}.md"
    if note["source_path"] != expected_note:
        raise CheckError("release_note source_path must agree with the explicit cut")
    standards, plugins, represented = [], [], set()
    for name, data in sorted(payload.items()):
        for prefix, group in (("standards/", standards), ("plugins/spec/", plugins)):
            if name.startswith(prefix):
                group.append({"path": name[len(prefix):], "sha256": sha(data)})
                represented.add(name)
    for required in ("LICENSE", note["package_path"]):
        if required not in payload:
            raise CheckError(f"required installed member absent from package: {required}")
        represented.add(required)
    if represented != payload.keys():
        raise CheckError(f"package members have no canonical installed-manifest slot: {sorted(payload.keys() - represented)}")
    if not standards:
        raise CheckError("standards distribution is empty")
    return {
        "kind": "stdo.installed-release-manifest",
        "schema_version": 1,
        "release": release,
        "standards": {"source_root": "specification/standards", "installed_root": "standards", "member_count": len(standards), "member_set_sha256": canonical_standards_digest(standards), "members": standards},
        "auxiliary": {
            "plugin": {"source_root": "plugins/spec", "installed_root": "plugins/spec", "member_count": len(plugins), "members": plugins},
            "license": {"path": "LICENSE", "sha256": sha(payload["LICENSE"])},
            "release_note": {"source_path": note["source_path"], "installed_path": note["installed_path"], "sha256": sha(payload[note["package_path"]])},
        },
    }


def outside_package(path: Path, root: Path):
    if path.resolve().is_relative_to(root.resolve()):
        raise CheckError(f"tool output must remain outside the candidate: {path}")


def write_new(path: Path, data: bytes):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as target:
        target.write(data)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for command in ("freeze", "check", "materialize"):
        sub = commands.add_parser(command)
        sub.add_argument("--root", required=True, type=Path)
        sub.add_argument("--inventory", required=True, type=Path)
        if command != "freeze":
            sub.add_argument("--inventory-sha256", required=True)
            sub.add_argument("--report", type=Path)
        if command == "materialize":
            sub.add_argument("--coordinates", required=True, type=Path)
            sub.add_argument("--coordinates-sha256", required=True)
            sub.add_argument("--destination", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        outside_package(args.inventory, args.root)
        if getattr(args, "report", None):
            outside_package(args.report, args.root)
            if args.report.exists():
                raise CheckError(f"report already exists: {args.report}")
        if args.command == "freeze":
            payload, directories = snapshot(args.root)
            content = encoded(inventory(payload, directories))
            write_new(args.inventory, content)
            print(json.dumps({"inventory": str(args.inventory), "inventory_sha256": sha(content), "member_count": len(payload), "standing": "identity capture, not validation or acceptance"}))
            return 0
        payload, report = checked_snapshot(args.root, args.inventory, args.inventory_sha256)
        if args.command == "materialize" and report["valid"]:
            outside_package(args.destination, args.root)
            if report["empty_directories"]:
                raise CheckError(f"empty package directories have no installed-manifest slot: {report['empty_directories']}")
            coordinates = pinned_json(args.coordinates, args.coordinates_sha256)
            manifest = build_manifest(payload, coordinates)
            # Validate every coordinate and the complete mapping before any output.
            args.destination.mkdir(parents=True, exist_ok=False)
            for name, data in sorted(payload.items()):
                write_new(args.destination / name, data)
            manifest_data = encoded(manifest)
            write_new(args.destination / "manifest.json", manifest_data)
            report.update({"destination": str(args.destination.absolute()), "coordinates_sha256": args.coordinates_sha256, "manifest_sha256": sha(manifest_data), "standards_member_set_sha256": manifest["standards"]["member_set_sha256"], "full_package_members_transferred": len(payload), "standing": "isolated canonical layout materialized with declared coordinates; no Git-object attestation, published release or installation"})
        if args.report:
            write_new(args.report, encoded(report))
        print(json.dumps(report, ensure_ascii=False))
        return 0 if report["valid"] else 1
    except (CheckError, OSError) as exc:
        print(json.dumps({"valid": False, "error": str(exc)}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Read only a named section from a manager-verified Product basis.

This projection helper owns no admission, access policy, actor or dispatch.
The caller must already be permitted to read its exact control/source routes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys


class Refusal(ValueError):
    pass


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise Refusal("duplicate_json_key")
        result[key] = value
    return result


def decoded(data):
    return json.loads(data, object_pairs_hook=unique_object)


def call(manager, store, args, timeout):
    command = [manager] + (["--store", store] if store else []) + args
    result = subprocess.run(command, capture_output=True, text=True, timeout=timeout)
    if result.returncode:
        raise Refusal(f"manager_failed:{args[0]}:exit={result.returncode}")
    value = decoded(result.stdout)
    if not isinstance(value, dict):
        raise Refusal("manager_response_not_object")
    return value


def verified(args):
    definition = Path(args.definition).absolute()
    raw = definition.read_bytes()
    data = decoded(raw)
    basis = data["constitution"]["stdo"]["basis"]
    uri, expected = basis["uri"], basis["manifest_sha256"]
    identity = data["product"]["definition_id"]
    if not isinstance(uri, str) or not re.fullmatch(r"stdo://releases/[A-Za-z0-9._-]+/", uri):
        raise Refusal("immutable_basis_required")
    if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected):
        raise Refusal("invalid_manifest_digest")
    status = call(args.stdo, args.store,
                  ["status", "--definition", str(definition), "--verify"], args.timeout)
    if (status.get("installed") is not True or status.get("valid") is not True
            or status.get("failures") != []
            or status.get("definition_id") != identity
            or Path(status.get("definition", "")).resolve() != definition.resolve()
            or status.get("basis") != uri or status.get("manifest_sha256") != expected):
        raise Refusal("basis_verification_mismatch")
    root = Path(status["path"]).resolve(strict=True)
    manifest_route = call(args.stdo, args.store, ["resolve", uri + "manifest.json"], args.timeout)
    manifest_path = Path(manifest_route.get("path", "")).resolve(strict=True)
    if manifest_route.get("uri") != uri + "manifest.json" or manifest_path != root / "manifest.json":
        raise Refusal("manifest_route_mismatch")
    manifest_raw = manifest_path.read_bytes()
    if digest(manifest_raw) != expected:
        raise Refusal("manifest_digest_mismatch")
    manifest = decoded(manifest_raw)
    if definition.read_bytes() != raw:
        raise Refusal("definition_changed")
    result = {"definition": str(definition), "definition_id": identity,
              "definition_sha256": digest(raw), "basis_uri": uri,
              "manifest_sha256": expected, "installed": True, "valid": True,
              "manager": args.stdo, "store": args.store,
              "standing": "verified source projection; no admission or semantic verdict"}
    return root, manifest, result


def headings(text: str):
    """Closed ATX subset; ignore examples/comments, refuse unsupported HTML blocks.

    Only column-zero ATX headings, fence and comment openers are supported.
    Unsupported placements refuse before their state can hide a boundary.
    Outside those blocks, any leading angle form after a potential quote/list
    prefix refuses, including autolinks and incomplete tags. No HTML parsing
    or positive interpretation of these container prefixes is attempted.
    """
    found = []
    fence = None
    comment = False
    source_lines = text.splitlines()
    for index, line in enumerate(source_lines):
        if fence:
            if re.fullmatch(r" {0,3}" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}\s*", line):
                fence = None
            continue
        if not comment and "<!--" in line and not line.startswith("<!--"):
            raise Refusal("unsupported_comment_placement")
        commented_line = comment or "<!--" in line
        visible = ""
        tail = line
        while tail:
            if comment:
                end = tail.find("-->")
                if end < 0:
                    tail = ""
                else:
                    comment, tail = False, tail[end + 3:]
            else:
                start = tail.find("<!--")
                if start < 0:
                    visible += tail
                    tail = ""
                else:
                    if start != 0 or tail != line:
                        raise Refusal("unsupported_comment_placement")
                    visible += tail[:start]
                    comment, tail = True, tail[start + 4:]
        clean_container = visible.lstrip(" \t")
        while True:
            prefix = re.match(r"(?:>[ \t]*|(?:[-+*]|\d+[.)])[ \t]+)", clean_container)
            if not prefix:
                break
            clean_container = clean_container[prefix.end():].lstrip(" \t")
        marker = re.match(r"(`{3,}|~{3,})(.*)$", clean_container)
        if marker:
            if commented_line:
                raise Refusal("unsupported_fence_comment")
            if not visible.startswith(marker[1]):
                raise Refusal("unsupported_container_fence")
            if marker[1][0] == "`" and "`" in marker[2]:
                raise Refusal("unsupported_fence_info")
            fence = marker[1]
            continue
        if re.match(r"#{1,6}(?:\s|$)", clean_container) and not visible.startswith("#"):
            raise Refusal("unsupported_container_heading")
        if clean_container.startswith("<"):
            raise Refusal("unsupported_markdown_html_block")
        if commented_line and re.match(r"^ {0,3}#{1,6}(?:\s|$)", visible):
            raise Refusal("unsupported_heading_comment")
        if (index and source_lines[index - 1].strip()
                and re.fullmatch(r" {0,3}(?:=+|-+)\s*", visible)):
            raise Refusal("unsupported_setext_heading")
        match = re.fullmatch(r" {0,3}(#{1,6})[ \t]+(.+?)(?:[ \t]+#+)?[ \t]*", visible)
        if match:
            found.append((index, len(match[1]), match[2]))
        elif re.fullmatch(r" {0,3}#{1,6}\s*", visible):
            found.append((index, len(visible.strip()), ""))
    if fence or comment:
        raise Refusal("unterminated_markdown_structure")
    return found


def sections(text: str, requested):
    parsed = headings(text)
    lines = text.splitlines(keepends=True)
    result = []
    for name in requested:
        matches = [h for h in parsed if h[2] == name]
        if len(matches) != 1:
            raise Refusal("section_missing_or_ambiguous:" + name)
        start, depth, _ = matches[0]
        end = next((i for i, d, _ in parsed if i > start and d <= depth), len(lines))
        body = "".join(lines[start:end])
        result.append({"heading": name, "first_line": start + 1, "last_line": end,
                       "sha256": digest(body.encode()), "text": body})
    return result


def run(args):
    root, manifest, result = verified(args)
    if args.command == "read":
        member = args.member
        path = PurePosixPath(member)
        if (not re.fullmatch(r"standards/[A-Za-z0-9_./-]+\.md", member)
                or path.as_posix() != member or any(p in {".", ".."} for p in path.parts)):
            raise Refusal("invalid_member_route")
        standards = manifest["standards"]
        if standards.get("installed_root") != "standards":
            raise Refusal("unsupported_standards_root")
        members = standards["members"]
        if not isinstance(members, list) or not all(isinstance(m, dict) for m in members):
            raise Refusal("invalid_member_inventory")
        entries = [m for m in members if m.get("path") == member.removeprefix("standards/")]
        if len(entries) != 1:
            raise Refusal("member_missing_or_ambiguous")
        uri = result["basis_uri"] + member
        route = call(args.stdo, args.store, ["resolve", uri], args.timeout)
        selected = Path(route.get("path", "")).resolve(strict=True)
        expected_path = root / member
        if route.get("uri") != uri or selected != expected_path or not selected.is_relative_to(root):
            raise Refusal("member_route_mismatch")
        raw = selected.read_bytes()
        if digest(raw) != entries[0].get("sha256"):
            raise Refusal("member_digest_mismatch")
        text = raw.decode("utf-8")
        result.update({"member_uri": uri, "member_sha256": digest(raw)})
        if args.list_headings:
            parsed = headings(text)
            counts = {}
            for _, _, name in parsed:
                counts[name] = counts.get(name, 0) + 1
            result["headings"] = [{"heading": name, "level": level, "first_line": line + 1,
                                   "unique": counts[name] == 1} for line, level, name in parsed]
        else:
            result["sections"] = sections(text, args.heading)
        # The entire file was hashed locally; only the requested projection is returned.
        if selected.read_bytes() != raw:
            raise Refusal("member_changed")
    if digest(Path(result["definition"]).read_bytes()) != result["definition_sha256"]:
        raise Refusal("definition_changed")
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("check", "read"):
        sub = commands.add_parser(name)
        sub.add_argument("--stdo", required=True, help="explicit existing manager executable")
        sub.add_argument("--store", help="explicit selected store; omit only when its default is bound")
        sub.add_argument("--definition", required=True)
        sub.add_argument("--timeout", type=float, default=30)
        if name == "read":
            sub.add_argument("--member", required=True, help="manifest-relative standards/*.md route")
            selection = sub.add_mutually_exclusive_group(required=True)
            selection.add_argument("--heading", action="append", help="exact ATX heading text, without # markers")
            selection.add_argument("--list-headings", action="store_true", help="verified selector catalog, no section bodies")
    args = parser.parse_args(argv)
    reply = {"kind": "stdo.skill-source-read", "command": args.command}
    try:
        if not math.isfinite(args.timeout) or args.timeout <= 0:
            raise Refusal("timeout_must_be_positive")
        reply.update(run(args), status="checked")
        code = 0
    except subprocess.TimeoutExpired:
        reply.update(status="incomplete", reason="manager_timeout")
        code = 2
    except (Refusal, OSError, ValueError, KeyError, TypeError) as exc:
        reply.update(status="refused", reason=str(exc), definition=args.definition)
        code = 1
    print(json.dumps(reply, ensure_ascii=False, sort_keys=True))
    return code


if __name__ == "__main__":
    sys.exit(main())

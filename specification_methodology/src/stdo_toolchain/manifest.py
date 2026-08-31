"""Deterministic installed-release manifest construction and verification."""

from __future__ import annotations

import os
import re
import stat
from pathlib import Path
from typing import Any

from .constants import MANIFEST_KIND, MANIFEST_VERSION
from .errors import StdoError
from .git_source import GitSnapshot
from .util import (
    canonical_json_bytes,
    ensure_relative_member,
    ensure_within,
    sha256_bytes,
)

STANDARDS_SOURCE_ROOT = "specification/standards"
STANDARDS_INSTALL_ROOT = "standards"
PLUGIN_SOURCE_ROOT = "plugins/spec"
PLUGIN_INSTALL_ROOT = "plugins/spec"


def _members(snapshot: GitSnapshot, source_root: str) -> list[dict[str, str]]:
    prefix = f"{source_root.rstrip('/')}/"
    values: list[dict[str, str]] = []
    for source_path in snapshot.list_files(source_root):
        if not source_path.startswith(prefix):
            raise StdoError(f"Git member escaped requested root: {source_path}")
        relative = ensure_relative_member(source_path[len(prefix) :])
        values.append(
            {
                "path": relative,
                "sha256": sha256_bytes(snapshot.read_file(source_path)),
            }
        )
    return values


def standards_member_set_sha256(members: list[dict[str, str]]) -> str:
    """Reproduce the release's canonical path-sensitive shasum recipe."""

    lines = bytearray()
    for member in sorted(members, key=lambda value: value["path"]):
        source_path = f"{STANDARDS_SOURCE_ROOT}/{member['path']}"
        lines.extend(f"{member['sha256']}  {source_path}\n".encode("utf-8"))
    return sha256_bytes(bytes(lines))


def build_manifest(snapshot: GitSnapshot) -> dict[str, Any]:
    standards = _members(snapshot, STANDARDS_SOURCE_ROOT)
    if not standards:
        raise StdoError(f"Cut {snapshot.cut} has an empty standards distribution")

    plugin_members = (
        _members(snapshot, PLUGIN_SOURCE_ROOT)
        if snapshot.path_exists(PLUGIN_SOURCE_ROOT)
        else []
    )
    if not snapshot.path_exists("LICENSE"):
        raise StdoError(f"Cut {snapshot.cut} has no distributable LICENSE")
    license_entry = {
        "path": "LICENSE",
        "sha256": sha256_bytes(snapshot.read_file("LICENSE")),
    }

    version_tag = snapshot.cut.rsplit("-rc.", 1)[0]
    release_note_source = f"releases/{version_tag}.md"
    if not snapshot.path_exists(release_note_source):
        raise StdoError(
            f"Cut {snapshot.cut} has no release note at {release_note_source}"
        )
    release_note = {
        "source_path": release_note_source,
        "installed_path": "release/release-note.md",
        "sha256": sha256_bytes(snapshot.read_file(release_note_source)),
    }

    release = {
        "cut": snapshot.cut,
        "tag_object": snapshot.tag_object,
        "commit": snapshot.commit,
        "tree": snapshot.tree,
        "standards_tree": snapshot.standards_tree,
    }
    if snapshot.project_release_namespace:
        release.update(
            {
                "project_release_namespace": snapshot.project_release_namespace,
                "qualified_ref": snapshot.ref,
                "project_subtree_root": snapshot.project_root or ".",
                "project_subtree_tree": snapshot.project_tree,
            }
        )

    return {
        "kind": MANIFEST_KIND,
        "schema_version": MANIFEST_VERSION,
        "release": release,
        "standards": {
            "source_root": STANDARDS_SOURCE_ROOT,
            "installed_root": STANDARDS_INSTALL_ROOT,
            "member_count": len(standards),
            "member_set_sha256": standards_member_set_sha256(standards),
            "members": standards,
        },
        "auxiliary": {
            "plugin": {
                "source_root": PLUGIN_SOURCE_ROOT,
                "installed_root": PLUGIN_INSTALL_ROOT,
                "member_count": len(plugin_members),
                "members": plugin_members,
            },
            "license": license_entry,
            "release_note": release_note,
        },
    }


def manifest_bytes(manifest: dict[str, Any]) -> bytes:
    return canonical_json_bytes(manifest)


def manifest_sha256(manifest: dict[str, Any]) -> str:
    return sha256_bytes(manifest_bytes(manifest))


def materialize_snapshot(
    snapshot: GitSnapshot,
    manifest: dict[str, Any],
    destination: Path,
) -> None:
    destination.mkdir(parents=True, exist_ok=False)

    standards = manifest["standards"]
    for member in standards["members"]:
        relative = ensure_relative_member(member["path"])
        source_path = f"{standards['source_root']}/{relative}"
        target = destination / standards["installed_root"] / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(snapshot.read_file(source_path))

    plugin = manifest["auxiliary"]["plugin"]
    for member in plugin["members"]:
        relative = ensure_relative_member(member["path"])
        source_path = f"{plugin['source_root']}/{relative}"
        target = destination / plugin["installed_root"] / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(snapshot.read_file(source_path))

    license_entry = manifest["auxiliary"]["license"]
    if license_entry is not None:
        (destination / license_entry["path"]).write_bytes(snapshot.read_file("LICENSE"))

    release_note = manifest["auxiliary"]["release_note"]
    if release_note is not None:
        target = destination / release_note["installed_path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(snapshot.read_file(release_note["source_path"]))

    (destination / "manifest.json").write_bytes(manifest_bytes(manifest))


def _is_reparse(stat_result: os.stat_result) -> bool:
    flag = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    attributes = getattr(stat_result, "st_file_attributes", 0)
    return bool(flag and attributes & flag)


def _filesystem_entry_kind(path: Path) -> str | None:
    try:
        value = path.lstat()
    except FileNotFoundError:
        return None
    if stat.S_ISLNK(value.st_mode) or _is_reparse(value):
        return "redirect"
    if stat.S_ISREG(value.st_mode):
        return "file"
    if stat.S_ISDIR(value.st_mode):
        return "directory"
    return "special"


def _actual_entries(root: Path) -> dict[str, str]:
    if _filesystem_entry_kind(root) != "directory":
        return {}
    entries: dict[str, str] = {}

    def walk(directory: Path, prefix: Path) -> None:
        try:
            with os.scandir(directory) as iterator:
                children = sorted(iterator, key=lambda item: item.name)
        except OSError as exc:
            raise StdoError(
                f"Cannot inventory installed release at {directory}: {exc}"
            ) from exc
        for child in children:
            relative = (prefix / child.name).as_posix()
            try:
                child_stat = child.stat(follow_symlinks=False)
            except OSError as exc:
                raise StdoError(
                    f"Cannot inspect installed release entry {child.path}: {exc}"
                ) from exc
            if child.is_symlink() or _is_reparse(child_stat):
                kind = "redirect"
            elif stat.S_ISREG(child_stat.st_mode):
                kind = "file"
            elif stat.S_ISDIR(child_stat.st_mode):
                kind = "directory"
            else:
                kind = "special"
            entries[relative] = kind
            if kind == "directory":
                walk(Path(child.path), prefix / child.name)

    walk(root, Path())
    return entries


def _expected_installed_entries(manifest: dict[str, Any]) -> dict[str, str]:
    expected: dict[str, str] = {}

    def add_file(relative: str) -> None:
        normalized = ensure_relative_member(relative)
        parts = Path(normalized).parts
        for index in range(1, len(parts)):
            parent = Path(*parts[:index]).as_posix()
            prior = expected.setdefault(parent, "directory")
            if prior != "directory":
                raise StdoError(f"Manifest path collides with a file: {parent}")
        prior = expected.setdefault(normalized, "file")
        if prior != "file":
            raise StdoError(f"Manifest path collides with a directory: {normalized}")

    add_file("manifest.json")
    standards = manifest["standards"]
    standards_root = ensure_relative_member(standards["installed_root"])
    for member in standards["members"]:
        add_file(f"{standards_root}/{ensure_relative_member(member['path'])}")
    plugin = manifest["auxiliary"]["plugin"]
    plugin_root = ensure_relative_member(plugin["installed_root"])
    for member in plugin["members"]:
        add_file(f"{plugin_root}/{ensure_relative_member(member['path'])}")
    license_entry = manifest["auxiliary"].get("license")
    if license_entry is not None:
        add_file(license_entry["path"])
    release_note = manifest["auxiliary"].get("release_note")
    if release_note is not None:
        add_file(release_note["installed_path"])
    return expected


def _verify_members(
    release_root: Path,
    installed_root: str,
    members: list[dict[str, str]],
    actual_entries: dict[str, str],
    *,
    label: str,
) -> list[str]:
    failures: list[str] = []
    normalized_root = ensure_relative_member(installed_root)
    payload_root = ensure_within(release_root, release_root / normalized_root)
    expected = {ensure_relative_member(member["path"]) for member in members}
    digests = {member["path"]: member["sha256"] for member in members}
    for relative in sorted(expected):
        installed_relative = f"{normalized_root}/{relative}"
        if actual_entries.get(installed_relative) != "file":
            continue
        member_path = ensure_within(payload_root, payload_root / relative)
        actual_digest = sha256_bytes(member_path.read_bytes())
        if actual_digest != digests[relative]:
            failures.append(
                f"changed {label} member: {relative} "
                f"(expected {digests[relative]}, got {actual_digest})"
            )
    return failures


def verify_materialization(release_root: Path, manifest: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    root_kind = _filesystem_entry_kind(release_root)
    if root_kind != "directory":
        return [
            f"installed release root must be a physical directory, found {root_kind or 'missing'}"
        ]
    if manifest.get("kind") != MANIFEST_KIND:
        failures.append(f"unexpected manifest kind: {manifest.get('kind')!r}")
    if manifest.get("schema_version") != MANIFEST_VERSION:
        failures.append(
            f"unexpected manifest schema version: {manifest.get('schema_version')!r}"
        )

    release = manifest.get("release", {})
    shared_source_keys = {
        "project_release_namespace",
        "qualified_ref",
        "project_subtree_root",
        "project_subtree_tree",
    }
    present_shared_source_keys = shared_source_keys & set(release)
    if present_shared_source_keys and present_shared_source_keys != shared_source_keys:
        failures.append("incomplete shared-source release coordinates")
    elif present_shared_source_keys:
        namespace = release.get("project_release_namespace")
        cut = release.get("cut")
        expected_ref = f"refs/tags/{namespace}/{cut}"
        if namespace != "specification_methodology":
            failures.append("unexpected STDO Project Release Namespace")
        if release.get("qualified_ref") != expected_ref:
            failures.append("qualified release ref does not match namespace and cut")
        subtree_root = release.get("project_subtree_root")
        if subtree_root != "specification_methodology":
            failures.append("unexpected STDO Project Subtree root")
        subtree_tree = release.get("project_subtree_tree")
        if (
            not isinstance(subtree_tree, str)
            or re.fullmatch(r"[0-9a-f]{40}(?:[0-9a-f]{24})?", subtree_tree) is None
        ):
            failures.append("invalid Project Subtree tree object")

    expected_entries = _expected_installed_entries(manifest)
    actual_entries = _actual_entries(release_root)
    for relative in sorted(expected_entries.keys() - actual_entries.keys()):
        expected_kind = expected_entries[relative]
        failures.append(f"missing installed release {expected_kind}: {relative}")
    for relative in sorted(actual_entries.keys() - expected_entries.keys()):
        actual_kind = actual_entries[relative]
        if actual_kind == "file":
            failures.append(f"extra installed release member: {relative}")
        else:
            failures.append(
                f"extra installed release entry: {relative} ({actual_kind})"
            )
    for relative in sorted(expected_entries.keys() & actual_entries.keys()):
        expected_kind = expected_entries[relative]
        actual_kind = actual_entries[relative]
        if expected_kind != actual_kind:
            failures.append(
                f"installed release entry type mismatch: {relative} "
                f"(expected {expected_kind}, found {actual_kind})"
            )

    standards = manifest.get("standards", {})
    members = standards.get("members", [])
    if standards.get("member_count") != len(members):
        failures.append("standards member_count does not match manifest members")
    elif standards.get("member_set_sha256") != standards_member_set_sha256(members):
        failures.append("standards member-set digest does not reproduce")
    failures.extend(
        _verify_members(
            release_root,
            standards.get("installed_root", STANDARDS_INSTALL_ROOT),
            members,
            actual_entries,
            label="standards",
        )
    )

    auxiliary = manifest.get("auxiliary", {})
    plugin = auxiliary.get("plugin", {})
    plugin_members = plugin.get("members", [])
    if plugin.get("member_count") != len(plugin_members):
        failures.append("plugin member_count does not match manifest members")
    failures.extend(
        _verify_members(
            release_root,
            plugin.get("installed_root", PLUGIN_INSTALL_ROOT),
            plugin_members,
            actual_entries,
            label="plugin",
        )
    )

    for label, entry_key in (("license", "license"), ("release note", "release_note")):
        entry = auxiliary.get(entry_key)
        if entry is None:
            continue
        relative = entry.get("installed_path", entry.get("path"))
        try:
            relative = ensure_relative_member(relative)
        except (StdoError, TypeError):
            failures.append(f"invalid {label} installed path")
            continue
        path = ensure_within(release_root, release_root / relative)
        if actual_entries.get(relative) == "file":
            actual_digest = sha256_bytes(path.read_bytes())
            if actual_digest != entry.get("sha256"):
                failures.append(f"changed {label}: {relative}")

    return failures

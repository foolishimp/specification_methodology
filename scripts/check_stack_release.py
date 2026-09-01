#!/usr/bin/env python3
"""Fail-closed qualification for a coordinated Specification Stack cohort."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


COHORT_VERSION = re.compile(r"\d+\.\d+\.\d+-rc\.[1-9]\d*")
HEX40 = re.compile(r"[0-9a-f]{40}")
HEX64 = re.compile(r"[0-9a-f]{64}")
STDO_URI = re.compile(r"stdo://releases/(v\d+\.\d+\.\d+-rc\.[1-9]\d*)/")


class CheckError(RuntimeError):
    """One bounded checker input or Git operation is invalid."""


@dataclass
class View:
    root: Path
    revision: str | None = None

    def exists(self, relative: str) -> bool:
        if self.revision is None:
            return (self.root / relative).is_file()
        return (
            git(
                self.root,
                "cat-file",
                "-e",
                f"{self.revision}:{relative}",
                check=False,
            ).returncode
            == 0
        )

    def read_bytes(self, relative: str) -> bytes:
        if self.revision is None:
            return (self.root / relative).read_bytes()
        return git_bytes(self.root, f"{self.revision}:{relative}")

    def read_json(self, relative: str) -> Any:
        return json.loads(self.read_bytes(relative))

    def files(self, prefix: str) -> list[str]:
        prefix = prefix.rstrip("/")
        if self.revision is None:
            base = self.root / prefix
            if not base.is_dir():
                return []
            return sorted(
                path.relative_to(self.root).as_posix()
                for path in base.rglob("*")
                if path.is_file()
            )
        result = git(
            self.root,
            "ls-tree",
            "-r",
            "--name-only",
            self.revision,
            "--",
            prefix,
        )
        return sorted(path for path in result.stdout.splitlines() if path)

    def member_kind(self, relative: str) -> str | None:
        if self.revision is None:
            path = self.root / relative
            if path.is_symlink():
                return "symlink"
            if path.is_file():
                return "file"
            return None
        result = git(
            self.root,
            "ls-tree",
            self.revision,
            "--",
            relative,
            check=False,
        )
        if result.returncode or not result.stdout.strip():
            return None
        mode = result.stdout.split(maxsplit=1)[0]
        return "symlink" if mode == "120000" else "file"

    def read_member_bytes(self, relative: str, kind: str) -> bytes:
        if self.revision is None and kind == "symlink":
            return os.readlink(self.root / relative).encode("utf-8")
        return self.read_bytes(relative)


def git(
    root: Path, *arguments: str, check: bool = True
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *arguments],
        cwd=root,
        check=check,
        capture_output=True,
        text=True,
    )


def git_bytes(root: Path, revision: str) -> bytes:
    return subprocess.run(
        ["git", "show", revision],
        cwd=root,
        check=True,
        capture_output=True,
    ).stdout


def sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def canonical_json_bytes(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()


def canonical_value_sha256(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return sha256(encoded)


def member_stream(rows: Iterable[tuple[str, str]]) -> str:
    value = "".join(f"{digest}  {path}\n" for path, digest in sorted(rows))
    return sha256(value.encode())


def product_member_stream(members: Iterable[dict[str, str]]) -> str:
    value = "".join(
        f"{member['sha256']}  {member['type']}  {member['path']}\n"
        for member in sorted(members, key=lambda row: row["path"])
    )
    return sha256(value.encode())


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def read_json(view: View, relative: str, failures: list[str]) -> Any | None:
    if not view.exists(relative):
        failures.append(f"missing JSON asset: {relative}")
        return None
    try:
        return view.read_json(relative)
    except (OSError, json.JSONDecodeError) as exc:
        failures.append(f"invalid JSON asset {relative}: {exc}")
        return None


def normalize_version(value: str) -> str:
    return value[1:] if value.startswith("v") else value


def rc_ref_ordinal(
    ref: str, namespace: str, semantic: str, *, include_unqualified: bool
) -> int | None:
    prefixes = [f"refs/tags/{namespace}/v{semantic}-rc."]
    if include_unqualified:
        prefixes.append(f"refs/tags/v{semantic}-rc.")
    for prefix in prefixes:
        if not ref.startswith(prefix):
            continue
        ordinal = ref.removeprefix(prefix)
        if re.fullmatch(r"[1-9]\d*", ordinal):
            return int(ordinal)
    return None


def validate_shape(manifest: dict[str, Any], failures: list[str]) -> None:
    require(
        manifest.get("kind") == "specification-stack.release-matched-cohort",
        "invalid cohort kind",
        failures,
    )
    require(manifest.get("schema_version") == 1, "invalid schema version", failures)
    cohort = manifest.get("cohort", {})
    version = cohort.get("version")
    cut = cohort.get("cut")
    require(
        isinstance(version, str) and COHORT_VERSION.fullmatch(version) is not None,
        "cohort.version is not <version>-rc.<n>",
        failures,
    )
    require(cut == f"v{version}", "cohort.cut does not normalize to version", failures)
    require(
        cohort.get("publication_mode") == "atomic",
        "active cohort publication_mode must be atomic",
        failures,
    )

    products = manifest.get("products")
    require(isinstance(products, dict), "products must be an object", failures)
    if not isinstance(products, dict) or not isinstance(version, str):
        return
    require(
        set(products)
        == {"specification_methodology", "axiom_indexer", "stdo_representation"},
        "cohort must declare exactly the three Product namespaces",
        failures,
    )
    semantic = version.split("-rc.", 1)[0]
    for key, product in products.items():
        namespace = product.get("namespace")
        require(namespace == key, f"{key}: namespace mismatch", failures)
        require(
            normalize_version(str(product.get("version", ""))) == version,
            f"{key}: version mismatch",
            failures,
        )
        expected = {
            "release_ref": f"refs/tags/{namespace}/v{version}",
            "selector_ref": f"refs/tags/{namespace}/v{semantic}",
            "rc_branch": f"refs/heads/rc/{namespace}/{semantic}",
            "release_branch": f"refs/heads/release/{namespace}/{semantic}",
        }
        for field, value in expected.items():
            require(
                product.get(field) == value,
                f"{key}: invalid {field}; expected {value}",
                failures,
            )

        if key != "specification_methodology":
            subject = product.get("subject", {})
            expected_count = 7 if key == "axiom_indexer" else 8
            members = subject.get("members")
            require(
                subject.get("member_count") == expected_count,
                f"{key}: Product member count must be {expected_count}",
                failures,
            )
            require(
                isinstance(subject.get("member_set_sha256"), str)
                and HEX64.fullmatch(subject["member_set_sha256"]) is not None,
                f"{key}: invalid Product member-set digest",
                failures,
            )
            require(
                isinstance(members, list) and len(members) == expected_count,
                f"{key}: Product member descriptors are incomplete",
                failures,
            )
            if isinstance(members, list):
                paths = [
                    member.get("path") for member in members if isinstance(member, dict)
                ]
                require(
                    len(paths) == expected_count
                    and paths == sorted(paths)
                    and len(set(paths)) == expected_count,
                    f"{key}: Product member paths must be unique and sorted",
                    failures,
                )
                for member in members:
                    if not isinstance(member, dict):
                        continue
                    path = member.get("path")
                    kind = member.get("type")
                    require(
                        isinstance(path, str)
                        and path
                        and not path.startswith("/")
                        and ".." not in Path(path).parts,
                        f"{key}: invalid Product member path {path!r}",
                        failures,
                    )
                    require(
                        kind in {"file", "symlink"},
                        f"{key}: invalid Product member type for {path}",
                        failures,
                    )
                    require(
                        isinstance(member.get("sha256"), str)
                        and HEX64.fullmatch(member["sha256"]) is not None,
                        f"{key}: invalid Product member digest for {path}",
                        failures,
                    )
                    require(
                        (kind == "symlink" and isinstance(member.get("target"), str))
                        or (kind == "file" and "target" not in member),
                        f"{key}: invalid symlink target declaration for {path}",
                        failures,
                    )

    assets = manifest.get("assets", {})
    require(
        set(assets) == {"spec_plugin", "stdo_semantic_index"},
        "cohort must declare plugin and semantic index assets",
        failures,
    )
    for key, asset in assets.items():
        require(
            normalize_version(str(asset.get("version", ""))) == version,
            f"{key}: version mismatch",
            failures,
        )

    carrier = cohort.get("carrier_ref")
    require(carrier == "refs/heads/main", "invalid cohort carrier ref", failures)
    required_refs = {carrier}
    for product in products.values():
        required_refs.update(
            product[field]
            for field in ("release_ref", "selector_ref", "rc_branch", "release_branch")
        )
    publication = manifest.get("publication")
    require(isinstance(publication, dict), "publication must be an object", failures)
    if not isinstance(publication, dict):
        return
    repository_url = publication.get("repository_url")
    require(
        isinstance(repository_url, str)
        and bool(repository_url)
        and repository_url == repository_url.strip(),
        "publication.repository_url must be one non-empty literal endpoint",
        failures,
    )
    expectations = publication.get("expected_remote")
    require(
        isinstance(expectations, dict),
        "publication.expected_remote is required",
        failures,
    )
    if not isinstance(expectations, dict):
        return
    require(
        set(expectations) == required_refs,
        "remote expectation set is not exact",
        failures,
    )
    immutable_refs = {product["release_ref"] for product in products.values()}
    for ref in required_refs:
        expected = expectations.get(ref)
        require(
            expected is None
            or (isinstance(expected, str) and HEX40.fullmatch(expected)),
            f"invalid remote expectation for {ref}",
            failures,
        )
        if ref in immutable_refs:
            require(
                expected is None,
                f"immutable tag is not create-only: {ref}",
                failures,
            )

    version_lines = publication.get("expected_version_lines")
    require(
        isinstance(version_lines, dict),
        "publication.expected_version_lines is required",
        failures,
    )
    if not isinstance(version_lines, dict):
        return
    require(
        set(version_lines) == set(products),
        "version-line expectation set must name exactly the three Products",
        failures,
    )
    target_ordinal = int(version.rsplit("-rc.", 1)[1])
    for key, product in products.items():
        rows = version_lines.get(key)
        require(isinstance(rows, list), f"{key}: version line must be a list", failures)
        if not isinstance(rows, list):
            continue
        seen_refs: set[str] = set()
        ordinal_identities: dict[int, tuple[str, str]] = {}
        for index, row in enumerate(rows):
            require(
                isinstance(row, dict)
                and set(row) == {"ordinal", "ref", "tag_object", "peeled_commit"},
                f"{key}: invalid version-line row {index}",
                failures,
            )
            if not isinstance(row, dict):
                continue
            ref = row.get("ref")
            ordinal = (
                rc_ref_ordinal(
                    ref,
                    product["namespace"],
                    semantic,
                    include_unqualified=key == "specification_methodology",
                )
                if isinstance(ref, str)
                else None
            )
            require(
                ordinal is not None and row.get("ordinal") == ordinal,
                f"{key}: invalid same-line positive RC ref {ref}",
                failures,
            )
            require(
                isinstance(ref, str) and ref not in seen_refs,
                f"{key}: duplicate version-line ref {ref}",
                failures,
            )
            if isinstance(ref, str):
                seen_refs.add(ref)
            tag_object = row.get("tag_object")
            peeled_commit = row.get("peeled_commit")
            require(
                isinstance(tag_object, str) and HEX40.fullmatch(tag_object) is not None,
                f"{key}: invalid tag object for {ref}",
                failures,
            )
            require(
                isinstance(peeled_commit, str)
                and HEX40.fullmatch(peeled_commit) is not None
                and tag_object != peeled_commit,
                f"{key}: version-line cut is not an annotated tag: {ref}",
                failures,
            )
            if ordinal is None:
                continue
            require(
                ordinal < target_ordinal,
                f"{key}: frozen prepublication line is not below target RC",
                failures,
            )
            identity = (str(tag_object), str(peeled_commit))
            prior = ordinal_identities.setdefault(ordinal, identity)
            require(
                prior == identity,
                f"{key}: one RC ordinal names conflicting immutable cuts",
                failures,
            )
        if all(
            isinstance(row, dict)
            and isinstance(row.get("ordinal"), int)
            and isinstance(row.get("ref"), str)
            for row in rows
        ):
            require(
                rows == sorted(rows, key=lambda row: (row["ordinal"], row["ref"])),
                f"{key}: version-line rows are not canonical",
                failures,
            )

    if isinstance(repository_url, str):
        version_line_basis = {
            "repository_url": repository_url,
            "version_lines": version_lines,
        }
        require(
            publication.get("expected_version_lines_sha256")
            == canonical_value_sha256(version_line_basis),
            "publication.expected_version_lines_sha256 mismatch",
            failures,
        )


def local_tag_identity(root: Path, ref: str, subtree: str) -> dict[str, str]:
    if git(root, "show-ref", "--verify", "--quiet", ref, check=False).returncode:
        raise CheckError(f"missing local release ref: {ref}")
    if git(root, "cat-file", "-t", ref).stdout.strip() != "tag":
        raise CheckError(f"release ref is not an annotated tag: {ref}")
    commit = git(root, "rev-parse", f"{ref}^{{}}").stdout.strip()
    return {
        "tag_object": git(root, "rev-parse", ref).stdout.strip(),
        "commit": commit,
        "tree": git(root, "rev-parse", f"{commit}^{{tree}}").stdout.strip(),
        "project_subtree_tree": git(
            root, "rev-parse", f"{commit}:{subtree}"
        ).stdout.strip(),
        "standards_tree": git(
            root,
            "rev-parse",
            f"{commit}:{subtree}/specification/standards",
        ).stdout.strip(),
    }


def inventories(
    view: View, subtree: str
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    standards_root = f"{subtree}/specification/standards"
    plugin_root = f"{subtree}/plugins/spec"
    standards = [
        {
            "path": path.removeprefix(f"{standards_root}/"),
            "sha256": sha256(view.read_bytes(path)),
        }
        for path in view.files(standards_root)
    ]
    plugin = [
        {
            "path": path.removeprefix(f"{plugin_root}/"),
            "sha256": sha256(view.read_bytes(path)),
        }
        for path in view.files(plugin_root)
    ]
    return standards, plugin


def expected_installed_manifest(
    view: View,
    product: dict[str, Any],
    freeze: dict[str, Any],
    standards: list[dict[str, str]],
    plugin: list[dict[str, str]],
    cut: str,
) -> dict[str, Any]:
    subtree = product["subtree"]
    semantic = cut.removeprefix("v").split("-rc.", 1)[0]
    note = f"releases/v{semantic}.md"
    release = {
        "cut": cut,
        "tag_object": freeze["tag_object"],
        "commit": freeze["commit"],
        "tree": freeze["tree"],
        "standards_tree": freeze["standards_tree"],
        "project_release_namespace": product["namespace"],
        "qualified_ref": product["release_ref"],
        "project_subtree_root": subtree,
        "project_subtree_tree": freeze["project_subtree_tree"],
    }
    return {
        "kind": "stdo.installed-release-manifest",
        "schema_version": 1,
        "release": release,
        "standards": {
            "source_root": "specification/standards",
            "installed_root": "standards",
            "member_count": len(standards),
            "member_set_sha256": member_stream(
                (f"specification/standards/{row['path']}", row["sha256"])
                for row in standards
            ),
            "members": standards,
        },
        "auxiliary": {
            "plugin": {
                "source_root": "plugins/spec",
                "installed_root": "plugins/spec",
                "member_count": len(plugin),
                "members": plugin,
            },
            "license": {
                "path": "LICENSE",
                "sha256": sha256(view.read_bytes(f"{subtree}/LICENSE")),
            },
            "release_note": {
                "source_path": note,
                "installed_path": "release/release-note.md",
                "sha256": sha256(view.read_bytes(f"{subtree}/{note}")),
            },
        },
    }


def validate_release_notes(
    view: View, manifest: dict[str, Any], failures: list[str]
) -> None:
    for key, product in manifest["products"].items():
        note_path = product["release_note"]
        if not view.exists(note_path):
            failures.append(f"{key}: missing release note {note_path}")
            continue
        note = view.read_bytes(note_path).decode("utf-8")
        for marker in product.get("release_note_markers", []):
            require(
                marker in note,
                f"{key}: release note lacks exact marker {marker!r}",
                failures,
            )


def validate_child_product_subjects(
    view: View, manifest: dict[str, Any], failures: list[str]
) -> None:
    for key in ("axiom_indexer", "stdo_representation"):
        product = manifest["products"][key]
        subject = product["subject"]
        declared = subject["members"]
        observed: list[dict[str, str]] = []
        note = view.read_bytes(product["release_note"]).decode("utf-8")
        for member in declared:
            relative = f"{product['subtree']}/{member['path']}"
            kind = view.member_kind(relative)
            require(
                kind == member["type"],
                f"{key}: Product member type mismatch: {member['path']}",
                failures,
            )
            if kind is None:
                continue
            value = view.read_member_bytes(relative, kind)
            digest = sha256(value)
            require(
                digest == member["sha256"],
                f"{key}: Product member digest mismatch: {member['path']}",
                failures,
            )
            row = {
                "type": kind,
                "path": member["path"],
                "sha256": digest,
            }
            if kind == "symlink":
                target = value.decode("utf-8")
                row["target"] = target
                require(
                    target == member.get("target"),
                    f"{key}: Product symlink target mismatch: {member['path']}",
                    failures,
                )
            observed.append(row)

            release_member = f"`{member['path']}`"
            if kind == "symlink":
                release_member += f" -> `{member['target']}`"
            release_row = f"| {kind} | {release_member} | `{member['sha256']}` |"
            require(
                release_row in note,
                f"{key}: release record lacks Product member {member['path']}",
                failures,
            )

        require(
            len(observed) == subject["member_count"],
            f"{key}: observed Product member count mismatch",
            failures,
        )
        digest = product_member_stream(observed)
        require(
            digest == subject["member_set_sha256"],
            f"{key}: Product member-set digest mismatch",
            failures,
        )
        require(
            subject["member_set_sha256"] in note,
            f"{key}: release record lacks Product member-set digest",
            failures,
        )


def validate_representation_axiom_dependency(
    view: View, manifest: dict[str, Any], failures: list[str]
) -> None:
    axiom = manifest["products"]["axiom_indexer"]
    representation = manifest["products"]["stdo_representation"]
    dependency = representation.get("dependencies", {}).get("axiom_indexer", {})
    expected = {
        "version": axiom["version"],
        "release_ref": axiom["release_ref"],
        "product_member_count": axiom["subject"]["member_count"],
        "product_member_set_sha256": axiom["subject"]["member_set_sha256"],
    }
    for field, value in expected.items():
        require(
            dependency.get(field) == value,
            f"Representation Axiom dependency {field} mismatch",
            failures,
        )

    roles = {
        "executable": "build_tenants/core/code/ac.py",
        "schema": "skills/axiomatize-corpus/references/program.schema.json",
        "output_contract": ("skills/axiomatize-corpus/references/output-contract.md"),
    }
    mechanics = dependency.get("mechanics")
    require(
        isinstance(mechanics, list)
        and {row.get("role") for row in mechanics if isinstance(row, dict)}
        == set(roles),
        "Representation Axiom dependency mechanics set mismatch",
        failures,
    )
    if not isinstance(mechanics, list):
        return
    axiom_members = {member["path"]: member for member in axiom["subject"]["members"]}
    note = view.read_bytes(representation["release_note"]).decode("utf-8")
    for field in ("version", "release_ref", "product_member_set_sha256"):
        require(
            str(expected[field]) in note,
            f"Representation release record lacks exact Axiom {field}",
            failures,
        )
    for mechanic in mechanics:
        if not isinstance(mechanic, dict) or mechanic.get("role") not in roles:
            continue
        role = mechanic["role"]
        path = roles[role]
        expected_member = axiom_members[path]
        require(
            mechanic.get("path") == path,
            f"Representation Axiom {role} path mismatch",
            failures,
        )
        require(
            mechanic.get("sha256") == expected_member["sha256"],
            f"Representation Axiom {role} digest mismatch",
            failures,
        )
        require(
            path in note and expected_member["sha256"] in note,
            f"Representation release record lacks exact Axiom {role} coordinate",
            failures,
        )

    release_record = dependency.get("release_record", {})
    require(
        release_record.get("path") == axiom["release_note"],
        "Representation Axiom release-record path mismatch",
        failures,
    )
    if view.exists(axiom["release_note"]):
        digest = sha256(view.read_bytes(axiom["release_note"]))
        require(
            release_record.get("sha256") == digest,
            "Representation Axiom release-record digest mismatch",
            failures,
        )
        require(
            digest in note,
            "Representation release record lacks exact Axiom release-record digest",
            failures,
        )


def validate_stdo(
    root: Path, manifest: dict[str, Any], failures: list[str]
) -> tuple[View | None, list[dict[str, str]], list[dict[str, str]]]:
    product = manifest["products"]["specification_methodology"]
    freeze = product.get("freeze")
    if not isinstance(freeze, dict) or "tag_object" not in freeze:
        failures.append("STDO commit-A freeze identity is absent")
        return None, [], []
    for field in (
        "tag_object",
        "commit",
        "tree",
        "project_subtree_tree",
        "standards_tree",
    ):
        require(
            isinstance(freeze.get(field), str)
            and HEX40.fullmatch(freeze[field]) is not None,
            f"STDO freeze has invalid {field}",
            failures,
        )
    for field in (
        "installed_manifest_sha256",
        "standards_member_set_sha256",
        "plugin_member_set_sha256",
    ):
        require(
            isinstance(freeze.get(field), str)
            and HEX64.fullmatch(freeze[field]) is not None,
            f"STDO freeze has invalid {field}",
            failures,
        )
    try:
        identity = local_tag_identity(root, product["release_ref"], product["subtree"])
    except (CheckError, subprocess.CalledProcessError) as exc:
        failures.append(str(exc))
        return None, [], []
    for field, value in identity.items():
        require(
            freeze.get(field) == value,
            f"STDO freeze {field} mismatch: expected {freeze.get(field)}, got {value}",
            failures,
        )

    tag_view = View(root, f"{product['release_ref']}^{{}}")
    standards, plugin = inventories(tag_view, product["subtree"])
    standards_digest = member_stream(
        (f"specification/standards/{row['path']}", row["sha256"]) for row in standards
    )
    plugin_digest = member_stream((f"./{row['path']}", row["sha256"]) for row in plugin)
    require(
        len(standards) == freeze.get("standards_member_count"),
        "STDO standards member count differs from freeze",
        failures,
    )
    require(
        standards_digest == freeze.get("standards_member_set_sha256"),
        "STDO standards member-set digest differs from freeze",
        failures,
    )
    require(
        len(plugin) == freeze.get("plugin_member_count"),
        "STDO plugin member count differs from freeze",
        failures,
    )
    require(
        plugin_digest == freeze.get("plugin_member_set_sha256"),
        "STDO plugin member-set digest differs from freeze",
        failures,
    )
    expected = expected_installed_manifest(
        tag_view,
        product,
        freeze,
        standards,
        plugin,
        manifest["cohort"]["cut"],
    )
    actual_manifest_digest = sha256(canonical_json_bytes(expected))
    require(
        actual_manifest_digest == freeze.get("installed_manifest_sha256"),
        "recomputed installed-manifest digest differs from freeze",
        failures,
    )

    plugin_asset = manifest["assets"]["spec_plugin"]
    for relative in plugin_asset["manifests"]:
        path = f"{plugin_asset['root']}/{relative}"
        payload = read_json(tag_view, path, failures)
        if isinstance(payload, dict):
            require(
                normalize_version(str(payload.get("version", "")))
                == manifest["cohort"]["version"],
                f"plugin manifest version mismatch: {path}",
                failures,
            )
    return tag_view, standards, plugin


def iter_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for member in value:
            yield from iter_strings(member)
    elif isinstance(value, dict):
        for member in value.values():
            yield from iter_strings(member)


def validate_source_routes(
    payload: Any, cut: str, label: str, failures: list[str]
) -> None:
    for value in iter_strings(payload):
        for matched in STDO_URI.findall(value):
            require(
                matched == cut,
                f"{label}: cross-cut STDO URI {matched}; expected {cut}",
                failures,
            )


def resolved_source_path(uri: str, source_uri: str) -> str | None:
    prefix = f"{source_uri}standards/"
    if not uri.startswith(prefix):
        return None
    return uri[len(prefix) :].split("#", 1)[0]


def validate_semantic_index(
    view: View,
    manifest: dict[str, Any],
    standards: list[dict[str, str]],
    failures: list[str],
) -> None:
    asset = manifest["assets"]["stdo_semantic_index"]
    root = asset["root"].rstrip("/")
    paths = {
        key: f"{root}/{asset[key]}"
        for key in ("source_corpus", "program", "map", "validation_report")
    }
    payloads = {key: read_json(view, path, failures) for key, path in paths.items()}
    if any(value is None for value in payloads.values()):
        return

    version = manifest["cohort"]["version"]
    cut = manifest["cohort"]["cut"]
    source_uri = f"stdo://releases/{cut}/"
    source_basis = f"{source_uri}standards/"
    product = manifest["products"]["specification_methodology"]
    freeze = product["freeze"]
    source = payloads["source_corpus"]
    require(
        source.get("kind") == "stdo-representation.source-corpus",
        "semantic source-corpus kind mismatch",
        failures,
    )
    require(
        normalize_version(str(source.get("representation_version", ""))) == version,
        "semantic source-corpus version mismatch",
        failures,
    )
    release = source.get("source_release", {})
    expected_release = {
        "cut": cut,
        "uri": source_uri,
        "qualified_ref": product["release_ref"],
        "tag_object": freeze["tag_object"],
        "commit": freeze["commit"],
        "tree": freeze["tree"],
        "project_subtree_root": product["subtree"],
        "project_subtree_tree": freeze["project_subtree_tree"],
        "standards_tree": freeze["standards_tree"],
        "installed_manifest_sha256": freeze["installed_manifest_sha256"],
        "standards_member_count": freeze["standards_member_count"],
        "standards_member_set_sha256": freeze["standards_member_set_sha256"],
    }
    for field, expected in expected_release.items():
        require(
            release.get(field) == expected,
            f"semantic source-corpus {field} mismatch",
            failures,
        )
    actual_members = release.get("standards_members")
    require(
        actual_members == standards,
        "semantic source-corpus does not reproduce the exact ordered STDO inventory",
        failures,
    )

    program = payloads["program"]
    constraint_map = payloads["map"]
    report = payloads["validation_report"]
    require(
        program.get("source_basis") == source_basis,
        "program source basis mismatch",
        failures,
    )
    require(
        constraint_map.get("source_basis") == source_basis,
        "constraint-map source basis mismatch",
        failures,
    )
    require(
        f"stdo-v{version}" in str(program.get("uri", "")),
        "program URI does not carry exact cohort version",
        failures,
    )
    require(
        constraint_map.get("program_uri") == program.get("uri"),
        "constraint map points to another program URI",
        failures,
    )
    require(
        report.get("program_uri") == program.get("uri"),
        "validation report points to another program URI",
        failures,
    )
    program_digest = f"sha256:{canonical_value_sha256(program)}"
    require(
        constraint_map.get("program_sha256") == program_digest,
        "constraint map does not bind the canonical program digest",
        failures,
    )
    require(
        report.get("program_sha256") == program_digest,
        "validation report does not bind the canonical program digest",
        failures,
    )
    require(
        constraint_map.get("program_sha256") == report.get("program_sha256"),
        "constraint map and validation report disagree on program digest",
        failures,
    )
    map_without_digest = dict(constraint_map)
    declared_map_digest = map_without_digest.pop("map_sha256", None)
    require(
        declared_map_digest == f"sha256:{canonical_value_sha256(map_without_digest)}",
        "constraint map intrinsic digest mismatch",
        failures,
    )
    require(report.get("status") == "valid", "semantic validation is invalid", failures)
    require(
        report.get("diagnostics") == [], "semantic validation has diagnostics", failures
    )
    for key, payload in payloads.items():
        validate_source_routes(payload, cut, key, failures)

    member_digests = {row["path"]: row["sha256"] for row in standards}
    require(
        constraint_map.get("resolved_sources") == report.get("resolved_sources"),
        "constraint map and validation report resolved-source sets differ",
        failures,
    )
    resolved_uris = {
        row.get("uri")
        for row in report.get("resolved_sources", [])
        if isinstance(row, dict)
    }
    for uri in iter_strings(program):
        relative = resolved_source_path(uri, source_uri)
        if relative:
            require(
                uri in resolved_uris,
                f"program source ref is absent from resolved-source proof: {uri}",
                failures,
            )
    for label, payload in (("map", constraint_map), ("report", report)):
        for row in payload.get("resolved_sources", []):
            uri = row.get("uri", "")
            relative = resolved_source_path(uri, source_uri)
            require(
                relative is not None,
                f"{label}: unbound resolved source {uri}",
                failures,
            )
            if relative is None:
                continue
            require(
                relative in member_digests,
                f"{label}: resolved source is absent from STDO inventory: {relative}",
                failures,
            )
            expected_digest = member_digests.get(relative)
            actual_digest = str(row.get("sha256", "")).removeprefix("sha256:")
            require(
                actual_digest == expected_digest,
                f"{label}: resolved source digest mismatch for {relative}",
                failures,
            )

    note_path = manifest["products"]["stdo_representation"]["release_note"]
    if view.exists(note_path):
        note = view.read_bytes(note_path).decode("utf-8")
        bound_paths = [
            paths["source_corpus"].removeprefix("stdo_representation/"),
            *asset["release_member_paths"],
            paths["validation_report"].removeprefix("stdo_representation/"),
        ]
        for relative in bound_paths:
            repository_path = f"stdo_representation/{relative}"
            require(
                relative in note,
                f"Representation release note does not bind {relative}",
                failures,
            )
            require(
                sha256(view.read_bytes(repository_path)) in note,
                f"Representation release note lacks exact digest for {relative}",
                failures,
            )


def direct_ref_oid(root: Path, ref: str) -> str | None:
    result = git(root, "show-ref", "--verify", "--hash", ref, check=False)
    return result.stdout.strip() or None


def annotated_ref(root: Path, ref: str, failures: list[str]) -> tuple[str, str] | None:
    direct = direct_ref_oid(root, ref)
    if direct is None:
        failures.append(f"missing local ref: {ref}")
        return None
    if git(root, "cat-file", "-t", ref).stdout.strip() != "tag":
        failures.append(f"local tag is lightweight: {ref}")
        return None
    return direct, git(root, "rev-parse", f"{ref}^{{}}").stdout.strip()


def configured_remote_urls(root: Path, remote: str, *, push: bool) -> list[str]:
    arguments = ["remote", "get-url"]
    if push:
        arguments.append("--push")
    arguments.extend(("--all", remote))
    result = git(root, *arguments, check=False)
    return result.stdout.splitlines() if result.returncode == 0 else []


def validate_remote_endpoint(
    root: Path,
    remote: str,
    repository_url: str,
    failures: list[str],
) -> None:
    fetch_urls = configured_remote_urls(root, remote, push=False)
    push_urls = configured_remote_urls(root, remote, push=True)
    require(
        fetch_urls == [repository_url],
        f"configured fetch endpoint for {remote} differs from frozen repository URL",
        failures,
    )
    require(
        push_urls == [repository_url],
        f"configured push endpoint for {remote} differs from frozen repository URL",
        failures,
    )


def remote_ref(
    root: Path, repository_url: str, ref: str
) -> tuple[str | None, str | None]:
    result = git(root, "ls-remote", repository_url, ref, f"{ref}^{{}}")
    rows = dict(line.split("\t", 1)[::-1] for line in result.stdout.splitlines())
    return rows.get(ref), rows.get(f"{ref}^{{}}")


def remote_version_line(
    root: Path,
    repository_url: str,
    namespace: str,
    semantic: str,
    *,
    include_unqualified: bool,
) -> list[dict[str, Any]]:
    patterns = [f"refs/tags/{namespace}/v{semantic}-rc.*"]
    if include_unqualified:
        patterns.append(f"refs/tags/v{semantic}-rc.*")
    result = git(root, "ls-remote", repository_url, *patterns)
    refs = dict(line.split("\t", 1)[::-1] for line in result.stdout.splitlines())
    rows: list[dict[str, Any]] = []
    for ref, tag_object in refs.items():
        if ref.endswith("^{}"):
            continue
        ordinal = rc_ref_ordinal(
            ref,
            namespace,
            semantic,
            include_unqualified=include_unqualified,
        )
        if ordinal is None:
            continue
        rows.append(
            {
                "ordinal": ordinal,
                "ref": ref,
                "tag_object": tag_object,
                "peeled_commit": refs.get(f"{ref}^{{}}"),
            }
        )
    return sorted(rows, key=lambda row: (row["ordinal"], row["ref"]))


def validate_remote_version_lines(
    root: Path,
    manifest: dict[str, Any],
    revision: str,
    repository_url: str,
    *,
    published: bool,
    failures: list[str],
) -> None:
    version = manifest["cohort"]["version"]
    semantic, ordinal_text = version.rsplit("-rc.", 1)
    target_ordinal = int(ordinal_text)
    expected_lines = manifest["publication"]["expected_version_lines"]
    commit_b = git(root, "rev-parse", f"{revision}^{{}}").stdout.strip()
    for key, product in manifest["products"].items():
        observed = remote_version_line(
            root,
            repository_url,
            product["namespace"],
            semantic,
            include_unqualified=key == "specification_methodology",
        )
        frozen = expected_lines[key]
        expected_live = list(frozen)
        expected_commit = (
            product["freeze"]["commit"]
            if key == "specification_methodology"
            else commit_b
        )
        if published:
            expected_live.append(
                {
                    "ordinal": target_ordinal,
                    "ref": product["release_ref"],
                    "tag_object": direct_ref_oid(root, product["release_ref"]),
                    "peeled_commit": expected_commit,
                }
            )
            expected_live.sort(key=lambda row: (row["ordinal"], row["ref"]))
        require(
            observed == expected_live,
            f"{key}: remote version-line set or immutable identity drifted",
            failures,
        )
        higher = [row["ref"] for row in observed if row["ordinal"] > target_ordinal]
        require(
            not higher,
            f"{key}: higher remote RC ordinal already exists: {', '.join(higher)}",
            failures,
        )
        observed_ordinals = [row["ordinal"] for row in observed]
        if published:
            require(
                bool(observed_ordinals) and max(observed_ordinals) == target_ordinal,
                f"{key}: published target is not the greatest RC ordinal",
                failures,
            )
            selector, selector_peel = remote_ref(
                root, repository_url, product["selector_ref"]
            )
            require(
                selector is not None
                and selector != selector_peel
                and selector_peel == expected_commit,
                f"{key}: published selector does not identify the greatest RC",
                failures,
            )
            release_branch, _ = remote_ref(
                root, repository_url, product["release_branch"]
            )
            require(
                release_branch == expected_commit,
                f"{key}: published release branch does not identify the greatest RC",
                failures,
            )
            continue

        require(
            all(ordinal < target_ordinal for ordinal in observed_ordinals),
            f"{key}: target RC is not greater than every published ordinal",
            failures,
        )
        selector, selector_peel = remote_ref(
            root, repository_url, product["selector_ref"]
        )
        if not observed:
            require(
                selector is None,
                f"{key}: selector exists without a lower immutable RC cut",
                failures,
            )
            continue
        greatest = max(observed_ordinals)
        greatest_peels = {
            row["peeled_commit"] for row in observed if row["ordinal"] == greatest
        }
        require(
            len(greatest_peels) == 1 and None not in greatest_peels,
            f"{key}: greatest lower RC has ambiguous or lightweight identity",
            failures,
        )
        require(
            selector is not None
            and selector != selector_peel
            and selector_peel in greatest_peels,
            f"{key}: current selector does not resolve to the greatest lower RC",
            failures,
        )


def validate_local_ref_graph(
    root: Path,
    manifest: dict[str, Any],
    revision: str,
    repository_url: str,
    failures: list[str],
) -> None:
    commit_b = git(root, "rev-parse", f"{revision}^{{}}").stdout.strip()
    carrier = manifest["cohort"]["carrier_ref"]
    require(
        direct_ref_oid(root, carrier) == commit_b,
        f"carrier ref {carrier} does not target commit B",
        failures,
    )
    for key, product in manifest["products"].items():
        tag = annotated_ref(root, product["release_ref"], failures)
        expected_commit = (
            product["freeze"]["commit"]
            if key == "specification_methodology"
            else commit_b
        )
        if tag:
            require(
                tag[1] == expected_commit,
                f"{key}: immutable tag peels to wrong commit",
                failures,
            )
        selector = annotated_ref(root, product["selector_ref"], failures)
        if selector:
            require(
                selector[1] == expected_commit,
                f"{key}: selector peels to wrong commit",
                failures,
            )
        for field in ("rc_branch", "release_branch"):
            require(
                direct_ref_oid(root, product[field]) == expected_commit,
                f"{key}: {field} does not target Product commit",
                failures,
            )

    validate_remote_version_lines(
        root,
        manifest,
        revision,
        repository_url,
        published=False,
        failures=failures,
    )

    expectations = manifest["publication"]["expected_remote"]
    required = {carrier}
    for product in manifest["products"].values():
        required.update(
            product[field]
            for field in ("release_ref", "selector_ref", "rc_branch", "release_branch")
        )
    for ref in sorted(required):
        expected = expectations.get(ref)
        actual, _ = remote_ref(root, repository_url, ref)
        require(
            actual == expected,
            f"remote drift at {ref}: expected {expected or 'absence'}, got {actual or 'absence'}; refetch and fully requalify",
            failures,
        )


def validate_remote_graph(
    root: Path,
    manifest: dict[str, Any],
    revision: str,
    repository_url: str,
    failures: list[str],
) -> None:
    commit_b = git(root, "rev-parse", f"{revision}^{{}}").stdout.strip()
    validate_remote_version_lines(
        root,
        manifest,
        revision,
        repository_url,
        published=True,
        failures=failures,
    )
    carrier = manifest["cohort"]["carrier_ref"]
    actual, _ = remote_ref(root, repository_url, carrier)
    require(
        actual == commit_b,
        f"remote carrier {carrier} does not target commit B",
        failures,
    )
    for key, product in manifest["products"].items():
        expected_commit = (
            product["freeze"]["commit"]
            if key == "specification_methodology"
            else commit_b
        )
        local_direct = direct_ref_oid(root, product["release_ref"])
        direct, peeled = remote_ref(root, repository_url, product["release_ref"])
        require(
            direct is not None,
            f"remote cohort missing {product['release_ref']}",
            failures,
        )
        require(
            peeled == expected_commit and direct != peeled,
            f"remote immutable tag is lightweight or targets wrong commit: {product['release_ref']}",
            failures,
        )
        require(
            direct == local_direct,
            f"remote immutable tag object differs from qualified local object: {product['release_ref']}",
            failures,
        )
        if key == "specification_methodology":
            require(
                direct == product["freeze"]["tag_object"],
                "remote STDO tag object differs from commit-A freeze",
                failures,
            )
        local_selector = direct_ref_oid(root, product["selector_ref"])
        selector, selector_peel = remote_ref(
            root, repository_url, product["selector_ref"]
        )
        require(
            selector is not None
            and selector != selector_peel
            and selector_peel == expected_commit,
            f"remote selector is absent, lightweight, or mismatched: {product['selector_ref']}",
            failures,
        )
        require(
            selector == local_selector,
            f"remote selector tag object differs from qualified local object: {product['selector_ref']}",
            failures,
        )
        for field in ("rc_branch", "release_branch"):
            oid, _ = remote_ref(root, repository_url, product[field])
            require(
                oid == expected_commit,
                f"remote {field} is absent or mismatched: {product[field]}",
                failures,
            )


def qualified_push_sources(
    root: Path, manifest: dict[str, Any], revision: str
) -> dict[str, str]:
    """Return immutable source object IDs for the already-qualified push set."""
    commit_b = git(root, "rev-parse", f"{revision}^{{}}").stdout.strip()
    sources = {manifest["cohort"]["carrier_ref"]: commit_b}
    for key, product in manifest["products"].items():
        expected_commit = (
            product["freeze"]["commit"]
            if key == "specification_methodology"
            else commit_b
        )
        for field in ("release_ref", "selector_ref"):
            source = direct_ref_oid(root, product[field])
            if source is None:
                raise CheckError(f"qualified local ref disappeared: {product[field]}")
            sources[product[field]] = source
        for field in ("rc_branch", "release_branch"):
            sources[product[field]] = expected_commit
    return sources


def check(
    root: Path,
    manifest_path: str,
    phase: str,
    revision: str | None,
    remote: str,
) -> list[str]:
    failures: list[str] = []
    view = View(root, revision)
    payload = read_json(view, manifest_path, failures)
    if not isinstance(payload, dict):
        return failures
    validate_shape(payload, failures)
    if revision is not None:
        require(
            payload.get("cohort", {}).get("status") == "candidate",
            "a frozen commit-B cohort must have status candidate",
            failures,
        )
    if failures:
        return failures
    validate_release_notes(view, payload, failures)
    validate_child_product_subjects(view, payload, failures)
    validate_representation_axiom_dependency(view, payload, failures)
    _, standards, _ = validate_stdo(root, payload, failures)
    validate_semantic_index(view, payload, standards, failures)
    if phase in {"refs", "published"}:
        repository_url = payload["publication"]["repository_url"]
        validate_remote_endpoint(root, remote, repository_url, failures)
        if revision is None:
            failures.append(f"--revision is required for {phase} phase")
        elif phase == "refs":
            validate_local_ref_graph(root, payload, revision, repository_url, failures)
        else:
            validate_remote_graph(root, payload, revision, repository_url, failures)
    return failures


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    parser.add_argument("--manifest", default="stack_release.json")
    parser.add_argument(
        "--phase", choices=("content", "refs", "published"), default="content"
    )
    parser.add_argument("--revision")
    parser.add_argument(
        "--remote",
        default="origin",
        help="configured alias whose fetch and push URLs must equal the frozen literal endpoint",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    failures = check(root, args.manifest, args.phase, args.revision, args.remote)
    if failures:
        print(
            json.dumps(
                {"status": "incomplete", "phase": args.phase, "failures": failures},
                indent=2,
            )
        )
        return 1
    result: dict[str, Any] = {
        "status": "valid",
        "phase": args.phase,
        "failures": [],
    }
    if args.phase == "refs":
        view = View(root, args.revision)
        manifest = view.read_json(args.manifest)
        repository_url = manifest["publication"]["repository_url"]
        expectations = manifest["publication"]["expected_remote"]
        version_lines = manifest["publication"]["expected_version_lines"]
        sources = qualified_push_sources(root, manifest, args.revision)
        refs = sorted(expectations)
        refspecs = [f"{sources[ref]}:{ref}" for ref in refs]
        result["repository_url"] = repository_url
        result["version_lines_sha256"] = manifest["publication"][
            "expected_version_lines_sha256"
        ]
        result["remote_expectations_sha256"] = canonical_value_sha256(
            {
                "repository_url": repository_url,
                "expected_remote": expectations,
                "expected_version_lines": version_lines,
            }
        )
        result["qualified_push_sha256"] = sha256(
            canonical_json_bytes(
                {
                    "revision": git(
                        root, "rev-parse", f"{args.revision}^{{}}"
                    ).stdout.strip(),
                    "repository_url": repository_url,
                    "expected_remote": expectations,
                    "expected_version_lines": version_lines,
                    "version_lines_sha256": result["version_lines_sha256"],
                    "refspecs": refspecs,
                }
            )
        )
        result["push_argv"] = [
            "git",
            "push",
            "--atomic",
            *(f"--force-with-lease={ref}:{expectations[ref] or ''}" for ref in refs),
            repository_url,
            *refspecs,
        ]
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

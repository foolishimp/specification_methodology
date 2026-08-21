"""Product Definition discovery, basis status, adoption, and bootstrap updates."""

from __future__ import annotations

import json
import os
import re
import stat
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse

from .constants import (
    BOOTSTRAP_END,
    BOOTSTRAP_START,
    BOOTSTRAP_TEXT,
    PRODUCT_DEFINITION_KIND,
)
from .errors import StdoError
from .git_source import (
    GitSnapshot,
    normalize_cut,
    normalize_version_line,
    resolve_channel,
)
from .manifest import build_manifest, manifest_sha256
from .store import Store
from .util import (
    atomic_write,
    canonical_json_bytes,
    load_json,
    sha256_bytes,
)

_DEFINITION_NAME_RE = re.compile(r"^stdo_[a-z0-9][a-z0-9_-]*\.json$")
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_SKIP_DIRECTORIES = {
    ".bzr",
    ".cache",
    ".genesis",
    ".git",
    ".gradle",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pytest_cache",
    ".ruff_cache",
    ".stdo",
    ".svn",
    ".tox",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "out",
    "site-packages",
    "target",
    "vendor",
    "venv",
}
_SCP_GIT_REFERENCE_RE = re.compile(r"^[^/@\s]+@[^:/\s]+:.+$")


@dataclass(frozen=True)
class ProductDefinitionBinding:
    path: Path
    document: dict[str, Any]
    document_sha256: str
    repository: str
    selector: str
    version_line: str
    basis_uri: str
    cut: str
    manifest_sha256: str


def _channel_version(uri: str) -> str:
    parsed = urlparse(uri)
    if parsed.scheme != "stdo" or parsed.netloc != "channels":
        raise StdoError(
            f"STDO selector must use stdo://channels/<version>, got {uri!r}"
        )
    if parsed.query or parsed.fragment:
        raise StdoError(f"STDO channel URI cannot contain query or fragment: {uri!r}")
    parts = [unquote(part) for part in parsed.path.split("/") if part]
    if len(parts) != 1:
        raise StdoError(f"STDO channel URI must name one version line: {uri!r}")
    return normalize_version_line(parts[0])


def _basis_cut(uri: str) -> str:
    parsed = urlparse(uri)
    if parsed.scheme != "stdo" or parsed.netloc != "releases":
        raise StdoError(
            f"STDO basis must use stdo://releases/<immutable-cut>/, got {uri!r}"
        )
    parts = [unquote(part) for part in parsed.path.split("/") if part]
    if len(parts) != 1:
        raise StdoError(f"STDO basis must identify a release root: {uri!r}")
    return normalize_cut(parts[0])


def _repository_location(reference: str, definition_path: Path) -> str:
    parsed = urlparse(reference)
    if parsed.query or parsed.fragment:
        raise StdoError(
            f"Git repository reference cannot contain query or fragment: {reference!r}"
        )
    if parsed.scheme or parsed.netloc or _SCP_GIT_REFERENCE_RE.fullmatch(reference):
        return reference
    candidate = Path(unquote(parsed.path))
    if not candidate.is_absolute():
        candidate = definition_path.parent / candidate
    return str(candidate.resolve())


def load_binding(path: Path | str) -> ProductDefinitionBinding:
    definition_path = Path(path).resolve()
    try:
        definition_bytes = definition_path.read_bytes()
    except FileNotFoundError as exc:
        raise StdoError(
            f"Product Definition does not exist: {definition_path}"
        ) from exc
    try:
        value = json.loads(definition_bytes)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise StdoError(
            f"Invalid Product Definition JSON at {definition_path}: {exc}"
        ) from exc
    if not isinstance(value, dict) or value.get("kind") != PRODUCT_DEFINITION_KIND:
        raise StdoError(f"Not an STDO Product Definition: {definition_path}")
    constitution = value.get("constitution")
    if not isinstance(constitution, dict):
        raise StdoError(
            f"Product Definition has no constitution object: {definition_path}"
        )
    stdo = constitution.get("stdo")
    if not isinstance(stdo, dict):
        if "authorities" in constitution:
            raise StdoError(
                f"Product Definition uses the legacy constitution.authorities shape and must be migrated: {definition_path}"
            )
        raise StdoError(
            f"Product Definition has no constitution.stdo binding: {definition_path}"
        )
    source = stdo.get("source")
    basis = stdo.get("basis")
    if not isinstance(source, dict) or not isinstance(basis, dict):
        raise StdoError(
            f"Product Definition has an incomplete STDO binding: {definition_path}"
        )
    repository = source.get("repository")
    selector = stdo.get("selector")
    basis_uri = basis.get("uri")
    digest = basis.get("manifest_sha256")
    for label, item in (
        ("repository", repository),
        ("selector", selector),
        ("basis URI", basis_uri),
        ("manifest SHA-256", digest),
    ):
        if not isinstance(item, str) or not item:
            raise StdoError(
                f"Product Definition has an invalid {label}: {definition_path}"
            )
    if not _SHA256_RE.fullmatch(digest):
        raise StdoError(
            f"Product Definition has an invalid manifest SHA-256: {definition_path}"
        )
    version_line = _channel_version(selector)
    cut = _basis_cut(basis_uri)
    schema_reference = value.get("$schema")
    if isinstance(schema_reference, str):
        parsed_schema = urlparse(schema_reference)
    else:
        parsed_schema = None
    if parsed_schema is not None and parsed_schema.scheme == "stdo":
        schema_parts = [unquote(part) for part in parsed_schema.path.split("/") if part]
        if (
            parsed_schema.netloc != "releases"
            or parsed_schema.query
            or parsed_schema.fragment
            or len(schema_parts) < 2
        ):
            raise StdoError(
                f"Product Definition has an invalid installed schema URI: {definition_path}"
            )
        schema_cut = normalize_cut(schema_parts[0])
        if schema_cut != cut:
            raise StdoError(
                f"Product Definition schema cut {schema_cut} differs from its basis {cut}: "
                f"{definition_path}"
            )
    return ProductDefinitionBinding(
        path=definition_path,
        document=value,
        document_sha256=sha256_bytes(definition_bytes),
        repository=_repository_location(repository, definition_path),
        selector=selector,
        version_line=version_line,
        basis_uri=basis_uri,
        cut=cut,
        manifest_sha256=digest,
    )


def _schema_path(
    document: dict[str, Any],
    definition_path: Path,
    store: Store,
) -> Path:
    reference = document.get("$schema")
    if not isinstance(reference, str) or not reference:
        raise StdoError(f"Product Definition has no schema locator: {definition_path}")
    parsed = urlparse(reference)
    if parsed.scheme == "stdo":
        return store.resolve(reference)
    if parsed.scheme not in {"", "file"} or parsed.netloc not in {"", "localhost"}:
        raise StdoError(
            f"Product Definition schema must be an installed stdo URI or local file reference: {reference!r}"
        )
    if parsed.query or parsed.fragment:
        raise StdoError(
            f"Product Definition schema locator cannot contain query or fragment: {reference!r}"
        )
    candidate = Path(unquote(parsed.path))
    if not candidate.is_absolute():
        candidate = definition_path.parent / candidate
    candidate = candidate.resolve()
    if not candidate.is_file():
        raise StdoError(f"Product Definition schema does not resolve: {reference!r}")
    return candidate


def validate_definition_document(
    document: dict[str, Any],
    definition_path: Path,
    store: Store,
) -> Path:
    try:
        from jsonschema import Draft202012Validator, FormatChecker
        from jsonschema.exceptions import SchemaError
    except ImportError as exc:
        raise StdoError(
            "Product Definition validation requires the installed stdo-toolchain dependencies"
        ) from exc

    schema_path = _schema_path(document, definition_path, store)
    schema = load_json(schema_path)
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise StdoError(
            f"Invalid Product Definition schema at {schema_path}: {exc.message}"
        ) from exc
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(document),
        key=lambda item: tuple(str(part) for part in item.absolute_path),
    )
    if errors:
        details: list[str] = []
        for error in errors[:10]:
            location = "/".join(str(part) for part in error.absolute_path) or "<root>"
            details.append(f"{location}: {error.message}")
        if len(errors) > 10:
            details.append(f"... and {len(errors) - 10} more validation errors")
        raise StdoError(
            f"Product Definition fails schema {schema_path}: {'; '.join(details)}"
        )
    return schema_path


def discover_definitions(root: Path | str) -> list[Path]:
    start = Path(root).resolve()
    if start.is_file():
        if not _DEFINITION_NAME_RE.fullmatch(start.name):
            raise StdoError(f"Not an STDO Product Definition filename: {start}")
        return [start]
    if not start.is_dir():
        raise StdoError(f"Product Definition discovery root does not exist: {start}")
    matches: list[Path] = []
    for directory, directories, files in os.walk(start):
        directory_path = Path(directory)
        directories[:] = sorted(
            name
            for name in directories
            if name not in _SKIP_DIRECTORIES
            and not (directory_path / name).is_symlink()
        )
        for filename in sorted(files):
            if _DEFINITION_NAME_RE.fullmatch(filename):
                candidate = directory_path / filename
                if candidate.is_symlink():
                    raise StdoError(
                        f"Product Definition discovery refuses a symlink: {candidate}"
                    )
                resolved = candidate.resolve()
                try:
                    resolved.relative_to(start)
                except ValueError as exc:
                    raise StdoError(
                        f"Product Definition escaped discovery root: {candidate}"
                    ) from exc
                matches.append(resolved)
    return matches


def definition_status(
    path: Path | str, store: Store, *, verify: bool = False
) -> dict[str, Any]:
    binding = load_binding(path)
    failures: list[str] = []
    schema_path: Path | None = None
    try:
        store.release_record(binding.cut)
        installed = True
    except StdoError as exc:
        installed = False
        failures.append(str(exc))

    if installed:
        try:
            schema_path = validate_definition_document(
                binding.document,
                binding.path,
                store,
            )
        except StdoError as exc:
            failures.append(str(exc))
        try:
            report = store.verify(
                binding.cut,
                expected_manifest_sha256=binding.manifest_sha256,
            )
            failures.extend(report.get("failures", []))
        except StdoError as exc:
            failures.append(str(exc))
            report = {"path": None}
    else:
        report = {
            "path": None,
        }
    result = {
        "definition": str(binding.path),
        "definition_id": binding.document.get("product", {}).get("definition_id"),
        "selector": binding.selector,
        "basis": binding.basis_uri,
        "cut": binding.cut,
        "installed": installed,
        "valid": installed and not failures,
        "failures": failures,
        "path": report.get("path"),
        "schema": str(schema_path) if schema_path is not None else None,
    }
    if verify and installed:
        result["manifest_sha256"] = report.get("manifest_sha256")
        result["release"] = report.get("manifest", {}).get("release")
        result["standards"] = report.get("manifest", {}).get("standards")
    return result


def sync_definition(
    path: Path | str,
    store: Store,
    *,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Materialize and verify the exact basis already selected by a definition."""

    binding = load_binding(path)
    installed = store.is_installed(binding.cut)

    if installed:
        report = store.verify(
            binding.cut,
            expected_manifest_sha256=binding.manifest_sha256,
        )
        if not report["valid"]:
            raise StdoError(
                f"Installed Product Definition basis is invalid: {'; '.join(report['failures'])}"
            )
        schema_path = validate_definition_document(
            binding.document,
            binding.path,
            store,
        )
        return {
            "definition": str(binding.path),
            "basis": binding.basis_uri,
            "manifest_sha256": binding.manifest_sha256,
            "status": "verified",
            "path": report["path"],
            "schema": str(schema_path),
            "dry_run": dry_run,
        }

    manifest, digest = _planned_manifest(binding.repository, binding.cut)
    if digest != binding.manifest_sha256:
        raise StdoError(
            f"Remote cut {binding.cut} differs from the Product Definition basis "
            f"(expected {binding.manifest_sha256}, got {digest})"
        )
    if dry_run:
        return {
            "definition": str(binding.path),
            "basis": binding.basis_uri,
            "manifest_sha256": digest,
            "status": "would_install",
            "path": None,
            "dry_run": True,
            "release": manifest["release"],
        }

    installed_result = store.install(
        binding.repository,
        binding.cut,
        expected_manifest_sha256=binding.manifest_sha256,
    )
    schema_path = validate_definition_document(
        binding.document,
        binding.path,
        store,
    )
    return {
        "definition": str(binding.path),
        "basis": binding.basis_uri,
        "manifest_sha256": installed_result.manifest_sha256,
        "status": installed_result.status,
        "path": str(installed_result.path),
        "schema": str(schema_path),
        "dry_run": False,
        "release": installed_result.manifest["release"],
    }


def _planned_manifest(repository: str, cut: str) -> tuple[dict[str, Any], str]:
    with GitSnapshot(repository, cut) as snapshot:
        manifest = build_manifest(snapshot)
    return manifest, manifest_sha256(manifest)


def adopt_definition(
    path: Path | str,
    store: Store,
    *,
    dry_run: bool = False,
    accepted_plan_sha256: str | None = None,
) -> dict[str, Any]:
    binding = load_binding(path)
    validate_definition_document(binding.document, binding.path, store)
    resolution = resolve_channel(binding.repository, binding.version_line)
    manifest, digest = _planned_manifest(binding.repository, resolution.cut)

    release = manifest["release"]
    if release["commit"] != resolution.commit:
        raise StdoError(
            f"Resolved channel commit {resolution.commit} differs from cut commit {release['commit']}"
        )
    if release["tag_object"] != resolution.cut_tag_object:
        raise StdoError(
            "Resolved immutable RC tag object differs from the installed cut tag object"
        )

    new_uri = Store.release_uri(resolution.cut)
    changed = new_uri != binding.basis_uri or digest != binding.manifest_sha256
    acceptance = {
        "kind": "stdo.adoption-plan",
        "schema_version": 1,
        "definition_id": binding.document.get("product", {}).get("definition_id"),
        "definition_sha256": binding.document_sha256,
        "selector": binding.selector,
        "from": {
            "basis": binding.basis_uri,
            "manifest_sha256": binding.manifest_sha256,
        },
        "to": {
            "basis": new_uri,
            "manifest_sha256": digest,
            "cut": resolution.cut,
            "tag_object": release["tag_object"],
            "commit": release["commit"],
            "tree": release["tree"],
        },
        "changed": changed,
    }
    plan_sha256 = sha256_bytes(canonical_json_bytes(acceptance))

    if not store.is_installed(resolution.cut):
        install_status = "would_install"
        install_path: str | None = None
    else:
        installed_report = store.verify(
            resolution.cut,
            expected_manifest_sha256=digest,
        )
        if not installed_report["valid"]:
            raise StdoError(
                f"Installed adoption target is invalid: {'; '.join(installed_report['failures'])}"
            )
        install_status = "already_installed_verified"
        install_path = installed_report["path"]

    result = {
        "definition": str(binding.path),
        **acceptance,
        "plan_sha256": plan_sha256,
        "dry_run": dry_run,
        "install_status": install_status,
        "install_path": install_path,
    }
    if dry_run:
        return result

    if accepted_plan_sha256 is None:
        raise StdoError(
            "Mutating adoption requires --accept-plan-sha256 from a prior dry-run"
        )
    if not _SHA256_RE.fullmatch(accepted_plan_sha256):
        raise StdoError("Accepted adoption plan SHA-256 must be 64 lowercase hex")
    if accepted_plan_sha256 != plan_sha256:
        raise StdoError(
            "Adoption plan differs from the explicitly accepted plan "
            f"(accepted {accepted_plan_sha256}, current {plan_sha256})"
        )

    installed = store.install(
        binding.repository,
        resolution.cut,
        expected_manifest_sha256=digest,
        expected_tag_object=resolution.cut_tag_object,
        expected_commit=resolution.commit,
    )
    result["install_status"] = installed.status
    result["install_path"] = str(installed.path)
    result["accepted_plan_sha256"] = accepted_plan_sha256

    try:
        current_definition_sha256 = sha256_bytes(binding.path.read_bytes())
    except FileNotFoundError as exc:
        raise StdoError(
            f"Product Definition disappeared during adoption: {binding.path}"
        ) from exc
    if current_definition_sha256 != binding.document_sha256:
        raise StdoError(
            "Product Definition changed after adoption planning; no definition mutation was performed"
        )
    if not changed:
        return result

    updated = json.loads(json.dumps(binding.document))
    updated["constitution"]["stdo"]["basis"] = {
        "uri": new_uri,
        "manifest_sha256": digest,
    }
    updated["$schema"] = f"{new_uri}standards/schemas/product-definition.schema.json"
    validate_definition_document(updated, binding.path, store)
    mode = binding.path.stat().st_mode & 0o777
    atomic_write(
        binding.path,
        (json.dumps(updated, indent=2) + "\n").encode("utf-8"),
        mode=mode,
    )
    return result


def _is_reparse(stat_result: os.stat_result) -> bool:
    flag = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    attributes = getattr(stat_result, "st_file_attributes", 0)
    return bool(flag and attributes & flag)


def _source_project_root(binding: ProductDefinitionBinding) -> Path:
    reference = binding.document.get("product", {}).get("source_project")
    if not isinstance(reference, str) or not reference:
        raise StdoError(
            f"Product Definition has no local source_project: {binding.path}"
        )
    parsed = urlparse(reference)
    if parsed.scheme not in {"", "file"} or parsed.netloc not in {"", "localhost"}:
        raise StdoError(
            f"Agent bootstrap requires a local product.source_project: {reference!r}"
        )
    if parsed.query or parsed.fragment:
        raise StdoError(
            f"product.source_project cannot contain query or fragment for bootstrap: {reference!r}"
        )
    candidate = Path(unquote(parsed.path))
    if not candidate.is_absolute():
        candidate = binding.path.parent / candidate
    resolved = candidate.resolve()
    if not resolved.is_dir():
        raise StdoError(
            f"product.source_project is not an existing directory: {reference!r}"
        )
    return resolved


def _target_path(source_root: Path, reference: str) -> Path:
    parsed = urlparse(reference)
    if parsed.scheme or parsed.netloc:
        raise StdoError(
            f"Agent bootstrap target must be relative to product.source_project: {reference!r}"
        )
    if parsed.query or parsed.fragment:
        raise StdoError(
            f"Agent bootstrap target cannot contain query or fragment: {reference!r}"
        )
    value = unquote(parsed.path)
    candidate = Path(value)
    if not value or candidate.is_absolute() or ".." in candidate.parts:
        raise StdoError(
            f"Agent bootstrap target must be a confined relative path: {reference!r}"
        )
    lexical_target = source_root / candidate
    current = source_root
    for part in candidate.parts:
        if part in {"", "."}:
            continue
        current = current / part
        try:
            current_stat = current.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(current_stat.st_mode) or _is_reparse(current_stat):
            raise StdoError(
                f"Agent bootstrap target contains a redirected component: {current}"
            )
    resolved = lexical_target.resolve()
    try:
        resolved.relative_to(source_root)
    except ValueError as exc:
        raise StdoError(
            f"Agent bootstrap target escapes product.source_project: {reference!r}"
        ) from exc
    if resolved.exists() and not resolved.is_file():
        raise StdoError(f"Agent bootstrap target is not a regular file: {resolved}")
    return resolved


def _bootstrap_section() -> str:
    return f"{BOOTSTRAP_START}\n{BOOTSTRAP_TEXT}\n{BOOTSTRAP_END}"


def install_bootstrap(
    path: Path | str,
    store: Store,
    *,
    dry_run: bool = False,
    authorized_root: Path | None = None,
) -> dict[str, Any]:
    binding = load_binding(path)
    validate_definition_document(binding.document, binding.path, store)
    bootstrap = binding.document.get("constitution", {}).get("agent_bootstrap")
    if not isinstance(bootstrap, dict) or not isinstance(
        bootstrap.get("targets"), list
    ):
        raise StdoError(
            f"Product Definition has no agent bootstrap targets: {binding.path}"
        )
    source_root = _source_project_root(binding)
    if authorized_root is not None:
        scope = authorized_root.resolve()
        try:
            source_root.relative_to(scope)
        except ValueError as exc:
            raise StdoError(
                f"Product source project escapes authorized fleet root {scope}: {source_root}"
            ) from exc
    section = _bootstrap_section().encode("utf-8")
    start_marker = BOOTSTRAP_START.encode("utf-8")
    end_marker = BOOTSTRAP_END.encode("utf-8")
    results: list[dict[str, str]] = []
    planned_writes: list[tuple[Path, bytes, int]] = []
    for target_reference in bootstrap["targets"]:
        if not isinstance(target_reference, str) or not target_reference:
            raise StdoError(f"Invalid agent bootstrap target in {binding.path}")
        target = _target_path(source_root, target_reference)
        if target.exists():
            existing = target.read_bytes()
            starts = existing.count(start_marker)
            ends = existing.count(end_marker)
            start_index = existing.find(start_marker)
            end_index = existing.find(end_marker)
            if starts != 1 or ends != 1 or end_index < start_index:
                if starts == 0 and ends == 0:
                    if not existing:
                        updated = section + b"\n"
                    elif existing.endswith(b"\n\n"):
                        updated = existing + section + b"\n"
                    elif existing.endswith(b"\n"):
                        updated = existing + b"\n" + section + b"\n"
                    else:
                        updated = existing + b"\n\n" + section + b"\n"
                    action = "appended"
                else:
                    raise StdoError(
                        f"Malformed or duplicate STDO bootstrap markers: {target}"
                    )
            else:
                span_end = end_index + len(end_marker)
                updated = existing[:start_index] + section + existing[span_end:]
                action = "unchanged" if updated == existing else "updated"
        else:
            updated = section + b"\n"
            action = "created"
        if action != "unchanged":
            mode = target.stat().st_mode & 0o777 if target.exists() else 0o644
            planned_writes.append((target, updated, mode))
        results.append({"target": str(target), "action": action})
    if not dry_run:
        for target, updated, mode in planned_writes:
            atomic_write(target, updated, mode=mode)
    return {
        "definition": str(binding.path),
        "dry_run": dry_run,
        "targets": results,
    }

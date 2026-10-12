"""Shared, versioned STDO installation store."""

from __future__ import annotations

import os
import platform
import shutil
import stat
import tempfile
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator
from urllib.parse import unquote, urlparse

from .constants import REGISTRY_KIND, REGISTRY_VERSION
from .errors import StdoError
from .git_source import GitSnapshot, normalize_cut
from .manifest import (
    build_manifest,
    manifest_sha256,
    materialize_snapshot,
    verify_materialization,
)
from .util import (
    atomic_write,
    canonical_json_bytes,
    ensure_relative_member,
    load_json,
    sha256_bytes,
)


def _is_reparse(stat_result: os.stat_result) -> bool:
    flag = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    attributes = getattr(stat_result, "st_file_attributes", 0)
    return bool(flag and attributes & flag)


def _entry_kind(path: Path) -> str | None:
    try:
        value = path.lstat()
    except FileNotFoundError:
        return None
    if stat.S_ISLNK(value.st_mode) or _is_reparse(value):
        return "redirect"
    if stat.S_ISDIR(value.st_mode):
        return "directory"
    if stat.S_ISREG(value.st_mode):
        return "file"
    return "special"


def default_store_path() -> Path:
    override = os.environ.get("STDO_STORE")
    if override:
        return Path(override).expanduser()
    system = platform.system()
    if system == "Darwin":
        return Path.home() / "Library" / "Application Support" / "STDO"
    if system == "Windows":
        local_data = os.environ.get("LOCALAPPDATA")
        if local_data:
            return Path(local_data) / "STDO"
        return Path.home() / "AppData" / "Local" / "STDO"
    xdg_data = os.environ.get("XDG_DATA_HOME")
    if xdg_data:
        return Path(xdg_data) / "stdo"
    return Path.home() / ".local" / "share" / "stdo"


@dataclass(frozen=True)
class InstallResult:
    cut: str
    uri: str
    path: Path
    manifest_sha256: str
    status: str
    manifest: dict[str, Any]


class Store:
    def __init__(self, root: Path | str | None = None):
        selected = Path(root) if root is not None else default_store_path()
        self.root = Path(os.path.abspath(selected.expanduser()))
        self.registry_path = self.root / "registry.json"
        self.releases_root = self.root / "releases"
        self.staging_root = self.root / ".staging"
        self.lock_path = self.root / ".registry.lock"

    def _store_root(self, *, create: bool = False) -> Path:
        kind = _entry_kind(self.root)
        if kind is None and create:
            self.root.mkdir(parents=True, exist_ok=False)
            kind = _entry_kind(self.root)
        if kind is None:
            return self.root
        if kind != "directory":
            raise StdoError(
                f"STDO store root must be a physical directory, found {kind}: {self.root}"
            )
        return self.root

    def _managed_directory(self, path: Path, *, create: bool = False) -> Path:
        self._store_root(create=create)
        try:
            path.relative_to(self.root)
        except ValueError as exc:
            raise StdoError(f"Managed STDO path escapes its store: {path}") from exc
        kind = _entry_kind(path)
        if kind is None and create:
            path.mkdir(parents=False, exist_ok=False)
            kind = _entry_kind(path)
        if kind != "directory":
            raise StdoError(
                f"Managed STDO directory must be physical, found {kind or 'missing'}: {path}"
            )
        return path

    def _managed_file(self, path: Path, *, required: bool = True) -> Path:
        self._store_root()
        try:
            relative = path.relative_to(self.root)
        except ValueError as exc:
            raise StdoError(f"Managed STDO path escapes its store: {path}") from exc
        current = self.root
        parts = relative.parts
        for index, part in enumerate(parts):
            current = current / part
            kind = _entry_kind(current)
            if kind == "redirect":
                raise StdoError(f"Managed STDO path contains a redirection: {current}")
            if index < len(parts) - 1 and kind != "directory":
                raise StdoError(
                    f"Managed STDO path has a non-directory component: {current}"
                )
        kind = _entry_kind(path)
        if required and kind != "file":
            raise StdoError(
                f"Managed STDO file must be physical, found {kind or 'missing'}: {path}"
            )
        if not required and kind not in {None, "file"}:
            raise StdoError(f"Managed STDO file must be physical, found {kind}: {path}")
        return path

    def _empty_registry(self) -> dict[str, Any]:
        return {
            "kind": REGISTRY_KIND,
            "schema_version": REGISTRY_VERSION,
            "releases": {},
        }

    def _load_registry(self) -> dict[str, Any]:
        self._store_root()
        if _entry_kind(self.registry_path) is None:
            return self._empty_registry()
        self._managed_file(self.registry_path)
        value = load_json(self.registry_path)
        if not isinstance(value, dict):
            raise StdoError(f"Invalid STDO registry object: {self.registry_path}")
        if (
            value.get("kind") != REGISTRY_KIND
            or value.get("schema_version") != REGISTRY_VERSION
        ):
            raise StdoError(f"Unsupported STDO registry: {self.registry_path}")
        if not isinstance(value.get("releases"), dict):
            raise StdoError(f"Invalid STDO registry releases map: {self.registry_path}")
        for cut, entry in value["releases"].items():
            normalized = normalize_cut(cut)
            if normalized != cut:
                raise StdoError(f"Non-canonical STDO registry cut: {cut!r}")
            self._record_path(normalized, entry)
        return value

    def _write_registry(self, registry: dict[str, Any]) -> None:
        self._managed_file(self.registry_path, required=False)
        atomic_write(self.registry_path, canonical_json_bytes(registry))

    @contextmanager
    def _locked(self) -> Iterator[None]:
        self._store_root(create=True)
        try:
            flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
            flags |= getattr(os, "O_NOFOLLOW", 0)
            descriptor = os.open(self.lock_path, flags, 0o600)
        except FileExistsError as exc:
            raise StdoError(
                f"STDO store is already being modified: {self.lock_path}"
            ) from exc
        try:
            os.write(descriptor, f"{os.getpid()}\n".encode("ascii"))
            os.close(descriptor)
            yield
        finally:
            try:
                self.lock_path.unlink()
            except FileNotFoundError:
                pass

    @staticmethod
    def release_uri(cut: str) -> str:
        normalized = normalize_cut(cut)
        return f"stdo://releases/{normalized}/"

    def _release_path(self, cut: str) -> Path:
        normalized = normalize_cut(cut)
        return self.releases_root / normalized

    def _record_path(self, cut: str, entry: Any) -> Path:
        if not isinstance(entry, dict):
            raise StdoError(f"Invalid STDO registry entry for {cut}")
        relative = entry.get("path")
        expected = f"releases/{cut}"
        if relative != expected:
            raise StdoError(
                f"STDO registry entry for {cut} has an unexpected path: {relative!r}"
            )
        self._managed_directory(self.releases_root)
        release_path = self.root / relative
        self._managed_directory(release_path)
        return release_path

    def install(
        self,
        repository: str,
        cut: str,
        *,
        expected_manifest_sha256: str | None = None,
        expected_tag_object: str | None = None,
        expected_commit: str | None = None,
    ) -> InstallResult:
        normalized = normalize_cut(cut)
        with GitSnapshot(repository, normalized) as snapshot:
            manifest = build_manifest(snapshot)
            digest = manifest_sha256(manifest)
            release = manifest["release"]
            if (
                expected_tag_object is not None
                and release["tag_object"] != expected_tag_object
            ):
                raise StdoError(
                    f"Cut {normalized} tag object moved during resolution "
                    f"(expected {expected_tag_object}, got {release['tag_object']})"
                )
            if expected_commit is not None and release["commit"] != expected_commit:
                raise StdoError(
                    f"Cut {normalized} commit moved during resolution "
                    f"(expected {expected_commit}, got {release['commit']})"
                )
            if (
                expected_manifest_sha256 is not None
                and digest != expected_manifest_sha256
            ):
                raise StdoError(
                    f"Cut {normalized} manifest digest differs from the Product Definition "
                    f"(expected {expected_manifest_sha256}, got {digest})"
                )
            with self._locked():
                self._managed_directory(self.releases_root, create=True)
                self._managed_directory(self.staging_root, create=True)
                final_path = self._release_path(normalized)
                registry = self._load_registry()

                if _entry_kind(final_path) is not None:
                    self._managed_directory(final_path)
                    existing_manifest_path = self._managed_file(
                        final_path / "manifest.json"
                    )
                    existing_manifest = load_json(existing_manifest_path)
                    existing_digest = sha256_bytes(existing_manifest_path.read_bytes())
                    if existing_digest != digest or existing_manifest != manifest:
                        raise StdoError(
                            f"Installed cut {normalized} differs from the requested immutable release"
                        )
                    failures = verify_materialization(final_path, existing_manifest)
                    if failures:
                        raise StdoError(
                            f"Installed cut {normalized} is damaged: {'; '.join(failures)}"
                        )
                    registry["releases"][normalized] = {
                        "path": f"releases/{normalized}",
                        "manifest_sha256": digest,
                    }
                    self._write_registry(registry)
                    return InstallResult(
                        cut=normalized,
                        uri=self.release_uri(normalized),
                        path=final_path,
                        manifest_sha256=digest,
                        status="already_installed",
                        manifest=manifest,
                    )

                stage_container = Path(
                    tempfile.mkdtemp(prefix=f"{normalized}.", dir=self.staging_root)
                )
                staged_release = stage_container / "release"
                try:
                    materialize_snapshot(snapshot, manifest, staged_release)
                    failures = verify_materialization(staged_release, manifest)
                    if failures:
                        raise StdoError(
                            f"Staged cut {normalized} failed verification: {'; '.join(failures)}"
                        )
                    for path in staged_release.rglob("*"):
                        if path.is_file():
                            path.chmod(0o444)
                    if _entry_kind(final_path) is not None:
                        raise StdoError(
                            f"Installed cut path appeared during staging: {final_path}"
                        )
                    os.replace(staged_release, final_path)
                finally:
                    if stage_container.exists():
                        shutil.rmtree(stage_container)

                registry["releases"][normalized] = {
                    "path": f"releases/{normalized}",
                    "manifest_sha256": digest,
                }
                self._write_registry(registry)
                return InstallResult(
                    cut=normalized,
                    uri=self.release_uri(normalized),
                    path=final_path,
                    manifest_sha256=digest,
                    status="installed",
                    manifest=manifest,
                )

    def list_releases(self) -> list[dict[str, Any]]:
        registry = self._load_registry()
        values: list[dict[str, Any]] = []
        for cut, entry in sorted(registry["releases"].items()):
            normalized = normalize_cut(cut)
            path = self._record_path(normalized, entry)
            values.append(
                {
                    "cut": normalized,
                    "uri": self.release_uri(normalized),
                    "path": str(path),
                    "manifest_sha256": entry.get("manifest_sha256"),
                    "present": path.is_dir(),
                }
            )
        return values

    def release_record(self, cut: str) -> dict[str, Any]:
        normalized = normalize_cut(cut)
        registry = self._load_registry()
        entry = registry["releases"].get(normalized)
        if entry is None:
            raise StdoError(f"STDO release is not installed: {normalized}")
        self._record_path(normalized, entry)
        return entry

    def is_installed(self, cut: str) -> bool:
        normalized = normalize_cut(cut)
        registry = self._load_registry()
        entry = registry["releases"].get(normalized)
        if entry is None:
            return False
        self._record_path(normalized, entry)
        return True

    def verify(
        self, cut: str, *, expected_manifest_sha256: str | None = None
    ) -> dict[str, Any]:
        normalized = normalize_cut(cut)
        entry = self.release_record(normalized)
        release_root = self._record_path(normalized, entry)
        manifest_path = self._managed_file(release_root / "manifest.json")
        manifest = load_json(manifest_path)
        actual_manifest_digest = sha256_bytes(manifest_path.read_bytes())
        failures: list[str] = []
        if entry.get("manifest_sha256") != actual_manifest_digest:
            failures.append(
                "registry manifest digest does not match installed manifest"
            )
        if (
            expected_manifest_sha256 is not None
            and expected_manifest_sha256 != actual_manifest_digest
        ):
            failures.append(
                "Product Definition manifest digest does not match installed manifest"
            )
        if manifest.get("release", {}).get("cut") != normalized:
            failures.append("installed manifest cut does not match registry cut")
        try:
            failures.extend(verify_materialization(release_root, manifest))
        except (KeyError, TypeError, StdoError) as exc:
            failures.append(f"invalid installed manifest structure: {exc}")
        return {
            "cut": normalized,
            "uri": self.release_uri(normalized),
            "path": str(release_root),
            "manifest_sha256": actual_manifest_digest,
            "valid": not failures,
            "failures": failures,
            "manifest": manifest,
        }

    def resolve(self, uri: str) -> Path:
        parsed = urlparse(uri)
        if parsed.scheme != "stdo" or parsed.netloc != "releases":
            raise StdoError(
                f"Only immutable stdo://releases/<cut>/ URIs can be resolved, got {uri!r}"
            )
        if parsed.query or parsed.fragment:
            raise StdoError(
                f"STDO installation URI cannot contain query or fragment: {uri!r}"
            )
        parts = [unquote(part) for part in parsed.path.split("/") if part]
        if not parts:
            raise StdoError(f"STDO release URI does not name a cut: {uri!r}")
        cut = normalize_cut(parts[0])
        report = self.verify(cut)
        if not report["valid"]:
            raise StdoError(
                f"STDO release {cut} failed verification: {'; '.join(report['failures'])}"
            )
        release_root = Path(report["path"])
        relative_parts = [ensure_relative_member(part) for part in parts[1:]]
        target = release_root.joinpath(*relative_parts)
        try:
            target.relative_to(release_root)
        except ValueError as exc:
            raise StdoError(f"STDO URI escapes its installed release: {uri!r}") from exc
        current = release_root
        target_parts: list[str] = []
        for relative in relative_parts:
            target_parts.extend(Path(relative).parts)
        for index, part in enumerate(target_parts):
            current = current / part
            kind = _entry_kind(current)
            if kind == "redirect":
                raise StdoError(f"STDO URI traverses a redirected path: {uri!r}")
            if kind is None:
                raise StdoError(
                    f"STDO URI does not resolve to an installed path: {uri!r}"
                )
            if index < len(target_parts) - 1 and kind != "directory":
                raise StdoError(f"STDO URI traverses a non-directory entry: {uri!r}")
        if _entry_kind(target) is None:
            raise StdoError(f"STDO URI does not resolve to an installed path: {uri!r}")
        return target

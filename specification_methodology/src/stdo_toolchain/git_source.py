"""Read exact immutable STDO cuts without using a mutable checkout."""

from __future__ import annotations

import re
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

from .errors import StdoError

_CUT_RE = re.compile(
    r"^v(?!.*-rc\..*-rc\.)[0-9A-Za-z][0-9A-Za-z._+-]*-rc\.[1-9][0-9]*$"
)
_VERSION_RE = re.compile(r"^(?!.*-rc\.)[0-9A-Za-z][0-9A-Za-z._+-]*$")

_LEGACY_PROJECT_ROOT = ""
_MONOREPO_PROJECT_ROOT = "specification_methodology"
_STANDARDS_ROOT = "specification/standards"


def _git(
    arguments: list[str],
    *,
    cwd: Path | None = None,
    text: bool = True,
) -> str | bytes:
    command = ["git", *arguments]
    try:
        completed = subprocess.run(
            command,
            cwd=cwd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=text,
        )
    except FileNotFoundError as exc:
        raise StdoError("git is required but was not found") from exc
    except subprocess.CalledProcessError as exc:
        detail = (
            exc.stderr.strip()
            if isinstance(exc.stderr, str)
            else exc.stderr.decode("utf-8", "replace").strip()
        )
        raise StdoError(f"git command failed ({' '.join(command)}): {detail}") from exc
    return completed.stdout


def normalize_cut(cut: str) -> str:
    value = cut.removeprefix("refs/tags/")
    if not _CUT_RE.fullmatch(value):
        raise StdoError(f"Immutable STDO cut must match v<version>-rc.<n>, got {cut!r}")
    return value


def normalize_version_line(version_line: str) -> str:
    value = version_line.removeprefix("v")
    if not _VERSION_RE.fullmatch(value):
        raise StdoError(f"Invalid STDO version line: {version_line!r}")
    return value


def cut_coordinates(cut: str) -> tuple[str, int]:
    """Return the version line and positive RC ordinal for an immutable cut."""

    normalized = normalize_cut(cut)
    version, ordinal = normalized.removeprefix("v").rsplit("-rc.", 1)
    return version, int(ordinal)


def ensure_channel_not_downgrade(current_cut: str, target_cut: str) -> None:
    """Refuse channel adoption from a higher cut to a lower cut on one line."""

    current_version, current_ordinal = cut_coordinates(current_cut)
    target_version, target_ordinal = cut_coordinates(target_cut)
    if current_version == target_version and target_ordinal < current_ordinal:
        raise StdoError(
            "STDO channel adoption cannot move backward on one version line: "
            f"current {current_cut}, target {target_cut}. Pin an older immutable "
            "cut explicitly instead of using the latest channel."
        )


@dataclass(frozen=True)
class ChannelResolution:
    version_line: str
    selector_ref: str
    selector_object: str
    commit: str
    cut: str
    cut_ordinal: int
    cut_ref: str
    cut_tag_object: str


def resolve_channel(repository: str, version_line: str) -> ChannelResolution:
    """Resolve a version-line tag only when it names the highest published RC."""

    version = normalize_version_line(version_line)
    selector_ref = f"refs/tags/v{version}"
    rc_prefix = f"refs/tags/v{version}-rc."
    output = _git(
        [
            "ls-remote",
            "--tags",
            repository,
            selector_ref,
            f"{selector_ref}^{{}}",
            f"{rc_prefix}*",
            f"{rc_prefix}*^{{}}",
        ]
    )
    assert isinstance(output, str)
    refs: dict[str, str] = {}
    for line in output.splitlines():
        if not line.strip():
            continue
        try:
            object_id, ref = line.split("\t", 1)
        except ValueError as exc:
            raise StdoError(f"Unexpected git ls-remote output: {line!r}") from exc
        refs[ref] = object_id

    selector_object = refs.get(selector_ref)
    if selector_object is None:
        raise StdoError(f"STDO channel tag is missing: {selector_ref}")
    selector_commit = refs.get(f"{selector_ref}^{{}}")
    if selector_commit is None:
        raise StdoError(
            f"STDO channel selector must be an annotated tag: {selector_ref}"
        )

    published: list[tuple[int, str, str, str | None]] = []
    for ref, tag_object in refs.items():
        if ref.endswith("^{}") or not ref.startswith(rc_prefix):
            continue
        suffix = ref[len(rc_prefix) :]
        if re.fullmatch(r"[1-9][0-9]*", suffix) is None:
            continue
        published.append((int(suffix), ref, tag_object, refs.get(f"{ref}^{{}}")))

    if not published:
        raise StdoError(
            f"STDO channel has no published immutable RC cuts: {selector_ref}"
        )

    cut_ordinal, cut_ref, cut_tag_object, cut_commit = max(
        published,
        key=lambda candidate: candidate[0],
    )
    cut = cut_ref.removeprefix("refs/tags/")
    if cut_commit is None:
        raise StdoError(f"Latest published STDO cut {cut} must be an annotated tag")
    if selector_commit != cut_commit:
        matching_selector_cuts = [
            ref.removeprefix("refs/tags/")
            for _, ref, _, peeled in published
            if peeled == selector_commit
        ]
        selector_target = (
            max(
                matching_selector_cuts,
                key=lambda candidate: cut_coordinates(candidate)[1],
            )
            if matching_selector_cuts
            else selector_commit
        )
        raise StdoError(
            f"STDO channel {selector_ref} is stale: it resolves to "
            f"{selector_target}, but the latest published immutable cut is {cut}. "
            "Refusing to select an older cut through a latest-version channel."
        )

    return ChannelResolution(
        version_line=version,
        selector_ref=selector_ref,
        selector_object=selector_object,
        commit=selector_commit,
        cut=cut,
        cut_ordinal=cut_ordinal,
        cut_ref=cut_ref,
        cut_tag_object=cut_tag_object,
    )


class GitSnapshot:
    """Temporary bare-object view of one annotated immutable release tag."""

    def __init__(self, repository: str, cut: str):
        self.repository = repository
        self.cut = normalize_cut(cut)
        self.ref = f"refs/tags/{self.cut}"
        self._temporary: tempfile.TemporaryDirectory[str] | None = None
        self.git_dir: Path | None = None
        self.tag_object = ""
        self.commit = ""
        self.tree = ""
        self.standards_tree = ""
        self.project_root = ""

    def __enter__(self) -> "GitSnapshot":
        self._temporary = tempfile.TemporaryDirectory(prefix="stdo-git-")
        self.git_dir = Path(self._temporary.name) / "objects.git"
        try:
            _git(["init", "--bare", str(self.git_dir)])
            _git(
                [
                    "--git-dir",
                    str(self.git_dir),
                    "fetch",
                    "--quiet",
                    "--no-tags",
                    self.repository,
                    f"+{self.ref}:{self.ref}",
                ]
            )
            object_type = self._text(["cat-file", "-t", self.ref]).strip()
            if object_type != "tag":
                raise StdoError(
                    f"Immutable cut {self.cut} must be an annotated tag; "
                    f"found {object_type}"
                )
            self.tag_object = self._text(["rev-parse", self.ref]).strip()
            self.commit = self._text(["rev-parse", f"{self.ref}^{{commit}}"]).strip()
            self.tree = self._text(["rev-parse", f"{self.commit}^{{tree}}"]).strip()
            self.project_root = self._detect_project_root()
            standards_path = self._repository_path(_STANDARDS_ROOT)
            self.standards_tree = self._text(
                ["rev-parse", f"{self.commit}:{standards_path}"]
            ).strip()
            return self
        except BaseException:
            self.__exit__(None, None, None)
            raise

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> None:
        if self._temporary is not None:
            self._temporary.cleanup()
        self._temporary = None
        self.git_dir = None

    def _arguments(self, arguments: list[str]) -> list[str]:
        if self.git_dir is None:
            raise StdoError("Git snapshot is not open")
        return ["--git-dir", str(self.git_dir), *arguments]

    def _text(self, arguments: list[str]) -> str:
        output = _git(self._arguments(arguments), text=True)
        assert isinstance(output, str)
        return output

    def _repository_object_type(self, path: str) -> str | None:
        if self.git_dir is None:
            raise StdoError("Git snapshot is not open")
        completed = subprocess.run(
            [
                "git",
                *self._arguments(["cat-file", "-t", f"{self.commit}:{path}"]),
            ],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
        )
        if completed.returncode != 0:
            return None
        return completed.stdout.strip()

    def _detect_project_root(self) -> str:
        candidates = []
        for project_root in (_LEGACY_PROJECT_ROOT, _MONOREPO_PROJECT_ROOT):
            standards_path = "/".join(
                part for part in (project_root, _STANDARDS_ROOT) if part
            )
            if self._repository_object_type(standards_path) == "tree":
                candidates.append(project_root)

        if len(candidates) != 1:
            found = "none" if not candidates else "legacy root and nested root"
            raise StdoError(
                f"Cut {self.cut} must contain exactly one STDO project layout at "
                "specification/standards or "
                "specification_methodology/specification/standards; "
                f"found {found}"
            )
        return candidates[0]

    def _repository_path(self, logical_path: str) -> str:
        if (
            not logical_path
            or logical_path.startswith("/")
            or any(part in {"", ".", ".."} for part in logical_path.split("/"))
        ):
            raise StdoError(f"Unsafe logical STDO path: {logical_path!r}")
        return "/".join(part for part in (self.project_root, logical_path) if part)

    def list_files(self, root: str) -> list[str]:
        repository_root = self._repository_path(root)
        output = self._text(
            [
                "ls-tree",
                "-r",
                "--name-only",
                "-z",
                self.commit,
                "--",
                repository_root,
            ]
        )
        prefix = f"{self.project_root}/" if self.project_root else ""
        logical_paths = []
        for path in output.split("\0"):
            if not path:
                continue
            if prefix:
                if not path.startswith(prefix):
                    raise StdoError(
                        f"Git member escaped selected STDO project root: {path}"
                    )
                path = path[len(prefix) :]
            logical_paths.append(path)
        return sorted(logical_paths)

    def read_file(self, path: str) -> bytes:
        repository_path = self._repository_path(path)
        output = _git(
            self._arguments(["show", f"{self.commit}:{repository_path}"]),
            text=False,
        )
        assert isinstance(output, bytes)
        return output

    def path_exists(self, path: str) -> bool:
        if self.git_dir is None:
            raise StdoError("Git snapshot is not open")
        repository_path = self._repository_path(path)
        completed = subprocess.run(
            [
                "git",
                *self._arguments(
                    ["cat-file", "-e", f"{self.commit}:{repository_path}"]
                ),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return completed.returncode == 0

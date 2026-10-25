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
_STABLE_CUT_RE = re.compile(r"^v(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)$")
_VERSION_RE = re.compile(r"^(?!.*-rc\.)[0-9A-Za-z][0-9A-Za-z._+-]*$")
STABLE_PROFILE = "stable-v1"
STABLE_TAG_MARKER = f"STDO-Release-Profile: {STABLE_PROFILE}"

_LEGACY_PROJECT_ROOT = ""
_MONOREPO_PROJECT_ROOT = "specification_methodology"
_STANDARDS_ROOT = "specification/standards"
_PACKAGE_STANDARDS_ROOT = "standards"
_PROJECT_RELEASE_NAMESPACE = "specification_methodology"


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


def _remote_tag_refs(repository: str, refs: list[str]) -> dict[str, str]:
    patterns = [item for ref in refs for item in (ref, f"{ref}^{{}}")]
    output = _git(["ls-remote", "--tags", repository, *patterns])
    assert isinstance(output, str)
    resolved: dict[str, str] = {}
    for line in output.splitlines():
        if not line.strip():
            continue
        try:
            object_id, ref = line.split("\t", 1)
        except ValueError as exc:
            raise StdoError(f"Unexpected git ls-remote output: {line!r}") from exc
        resolved[ref] = object_id
    return resolved


def _profile_lines(message: str) -> list[str]:
    return [
        line for line in message.splitlines()
        if line.lstrip().startswith("STDO-Release-Profile:")
    ]


def _require_legacy_selector(repository: str, ref: str, expected_object: str) -> None:
    """An explicit final-cut tag cannot turn into a selector when RC refs appear."""
    with tempfile.TemporaryDirectory(prefix="stdo-selector-") as temporary:
        git_dir = Path(temporary) / "objects.git"
        _git(["init", "--bare", str(git_dir)])
        args = ["--git-dir", str(git_dir)]
        _git([*args, "fetch", "--quiet", "--no-tags", repository, f"+{ref}:{ref}"])
        actual = _git([*args, "rev-parse", ref])
        assert isinstance(actual, str)
        if actual.strip() != expected_object:
            raise StdoError("STDO selector identity changed during channel resolution")
        raw = _git([*args, "cat-file", "tag", expected_object])
        assert isinstance(raw, str)
        if _profile_lines(raw.partition("\n\n")[2]):
            raise StdoError(
                "An explicit release-profile tag cannot be used as a legacy RC "
                f"selector: {ref}"
            )


def _candidate_cut_refs(cut: str) -> tuple[str, str]:
    return (
        f"refs/tags/{cut}",
        f"refs/tags/{_PROJECT_RELEASE_NAMESPACE}/{cut}",
    )


def _resolve_cut_ref(repository: str, cut: str) -> str:
    if is_stable_cut(cut):
        return _resolve_stable_ref(repository, cut)
    candidates = _candidate_cut_refs(cut)
    refs = _remote_tag_refs(repository, list(candidates))
    present = [ref for ref in candidates if ref in refs]
    if not present:
        raise StdoError(f"Immutable STDO cut tag is missing: {cut}")
    identities = {(refs[ref], refs.get(f"{ref}^{{}}")) for ref in present}
    if len(identities) != 1:
        raise StdoError(
            f"Immutable STDO cut {cut} is ambiguous across historical and "
            "project-qualified refs: {', '.join(present)}"
        )
    # A later preserving alias must not change the manifest of an already
    # installed historical cut. Channel resolution may prefer the qualified
    # transport ref, while direct logical-cut reacquisition retains the
    # historical ref whenever both names reach the same exact tag object.
    return candidates[0] if candidates[0] in present else candidates[1]


def is_stable_cut(cut: str) -> bool:
    """Recognize stable syntax, not evidence that a Git ref is immutable."""
    return _STABLE_CUT_RE.fullmatch(cut) is not None


def _resolve_stable_ref(repository: str, cut: str) -> str:
    historical, qualified = _candidate_cut_refs(cut)
    refs = _remote_tag_refs(
        repository, [historical, qualified, f"{historical}-rc.*", f"{qualified}-rc.*"]
    )
    if historical in refs or any(
        ref.startswith(f"{prefix}-rc.") for ref in refs for prefix in (historical, qualified)
    ):
        raise StdoError(
            f"Stable cut {cut} requires a fresh version line: historical bare aliases "
            "and same-version RC refs are forbidden; legacy bare tags remain selectors"
        )
    if qualified not in refs:
        raise StdoError(f"Immutable stable STDO cut tag is missing: {qualified}")
    if f"{qualified}^{{}}" not in refs:
        raise StdoError(f"Immutable stable cut {cut} must be an annotated tag")
    return qualified


def normalize_cut(cut: str) -> str:
    value = cut.removeprefix("refs/tags/")
    if not (_CUT_RE.fullmatch(value) or is_stable_cut(value)):
        raise StdoError(
            "Immutable STDO cut must match v<version>-rc.<n> or the stable-v1 "
            f"vMAJOR.MINOR.PATCH profile, got {cut!r}"
        )
    return value


def normalize_version_line(version_line: str) -> str:
    value = version_line.removeprefix("v")
    if not _VERSION_RE.fullmatch(value):
        raise StdoError(f"Invalid STDO version line: {version_line!r}")
    return value


def cut_coordinates(cut: str) -> tuple[str, int | None]:
    """Return a version and RC ordinal, or None for stable-v1 syntax."""

    normalized = normalize_cut(cut)
    if is_stable_cut(normalized):
        return normalized.removeprefix("v"), None
    version, ordinal = normalized.removeprefix("v").rsplit("-rc.", 1)
    return version, int(ordinal)


def ensure_channel_not_downgrade(current_cut: str, target_cut: str) -> None:
    """Refuse channel adoption from a higher cut to a lower cut on one line."""

    current_version, current_ordinal = cut_coordinates(current_cut)
    target_version, target_ordinal = cut_coordinates(target_cut)
    if current_version == target_version and (
        (current_ordinal is None and target_ordinal is not None)
        or (
            current_ordinal is not None
            and target_ordinal is not None
            and target_ordinal < current_ordinal
        )
    ):
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
    cut_ordinal: int | None
    cut_ref: str
    cut_tag_object: str


def resolve_channel(repository: str, version_line: str) -> ChannelResolution:
    """Resolve a legacy highest-RC selector or an explicit stable-v1 exact tag."""

    version = normalize_version_line(version_line)
    historical_selector_ref = f"refs/tags/v{version}"
    qualified_selector_ref = f"refs/tags/{_PROJECT_RELEASE_NAMESPACE}/v{version}"
    historical_rc_prefix = f"refs/tags/v{version}-rc."
    qualified_rc_prefix = f"refs/tags/{_PROJECT_RELEASE_NAMESPACE}/v{version}-rc."
    output = _git(
        [
            "ls-remote",
            "--tags",
            repository,
            historical_selector_ref,
            f"{historical_selector_ref}^{{}}",
            qualified_selector_ref,
            f"{qualified_selector_ref}^{{}}",
            f"{historical_rc_prefix}*",
            f"{historical_rc_prefix}*^{{}}",
            f"{qualified_rc_prefix}*",
            f"{qualified_rc_prefix}*^{{}}",
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

    historical: dict[int, tuple[str, str, str | None]] = {}
    qualified: dict[int, tuple[str, str, str | None]] = {}
    for ref, tag_object in refs.items():
        if ref.endswith("^{}"):
            continue
        if ref.startswith(historical_rc_prefix):
            prefix = historical_rc_prefix
            profile = historical
        elif ref.startswith(qualified_rc_prefix):
            prefix = qualified_rc_prefix
            profile = qualified
        else:
            continue
        suffix = ref[len(prefix) :]
        if re.fullmatch(r"[1-9][0-9]*", suffix) is None:
            continue
        ordinal = int(suffix)
        peeled = refs.get(f"{ref}^{{}}")
        profile[ordinal] = (ref, tag_object, peeled)

    for ordinal in sorted(historical.keys() & qualified.keys()):
        historical_ref, historical_object, historical_peeled = historical[ordinal]
        qualified_ref, qualified_object, qualified_peeled = qualified[ordinal]
        if (historical_object, historical_peeled) != (
            qualified_object,
            qualified_peeled,
        ):
            raise StdoError(
                f"STDO cut v{version}-rc.{ordinal} is ambiguous across refs "
                f"{historical_ref} and {qualified_ref}"
            )

    if not historical and not qualified:
        if is_stable_cut(f"v{version}") and qualified_selector_ref in refs:
            # A bare tag is never classified by spelling or by RC absence alone.
            # Fetch its annotated object and require the explicit stable marker.
            with GitSnapshot(repository, f"v{version}") as snapshot:
                if (
                    snapshot.tag_object != refs[qualified_selector_ref]
                    or snapshot.commit != refs.get(f"{qualified_selector_ref}^{{}}")
                ):
                    raise StdoError("Stable release identity changed during channel resolution")
                return ChannelResolution(
                    version_line=version,
                    selector_ref=snapshot.ref,
                    selector_object=snapshot.tag_object,
                    commit=snapshot.commit,
                    cut=snapshot.cut,
                    cut_ordinal=None,
                    cut_ref=snapshot.ref,
                    cut_tag_object=snapshot.tag_object,
                )
        raise StdoError(
            "STDO channel has no published immutable RC cuts: "
            f"{historical_selector_ref} or {qualified_selector_ref}"
        )

    historical_selector_object = refs.get(historical_selector_ref)
    qualified_selector_object = refs.get(qualified_selector_ref)
    if historical and historical_selector_object is None:
        raise StdoError(
            "Historical STDO channel selector must remain present: "
            f"{historical_selector_ref}"
        )
    if not historical and historical_selector_object is not None:
        raise StdoError(
            "Historical STDO channel selector has no historical immutable cuts: "
            f"{historical_selector_ref}"
        )
    if qualified and qualified_selector_object is None:
        raise StdoError(
            "First project-qualified STDO publication must create its qualified "
            f"selector: {qualified_selector_ref}"
        )
    if not qualified and qualified_selector_object is not None:
        raise StdoError(
            "Project-qualified STDO selector has no project-qualified immutable "
            f"cuts: {qualified_selector_ref}"
        )

    if historical:
        historical_selector_commit = refs.get(f"{historical_selector_ref}^{{}}")
        if historical_selector_commit is None:
            raise StdoError(
                "Historical STDO channel selector must remain an annotated tag: "
                f"{historical_selector_ref}"
            )
        highest_historical_ordinal = max(historical)
        highest_historical_commit = historical[highest_historical_ordinal][2]
        if qualified and historical_selector_commit != highest_historical_commit:
            raise StdoError(
                "Historical STDO channel selector must remain at its highest "
                "historical immutable cut during the qualified transition: "
                f"v{version}-rc.{highest_historical_ordinal}"
            )

    ordinals: dict[int, tuple[str, str, str | None]] = dict(historical)
    ordinals.update(qualified)
    cut_ordinal = max(ordinals)
    cut_ref, cut_tag_object, cut_commit = ordinals[cut_ordinal]
    cut = f"v{version}-rc.{cut_ordinal}"

    if qualified:
        if cut_ordinal not in qualified:
            raise StdoError(
                "Project-qualified STDO selector cannot activate while the highest "
                f"published cut remains historical: {cut}"
            )
        selector_ref = qualified_selector_ref
        selector_object = qualified_selector_object
    else:
        selector_ref = historical_selector_ref
        selector_object = historical_selector_object
    assert selector_object is not None
    selector_commit = refs.get(f"{selector_ref}^{{}}")
    if selector_commit is None:
        raise StdoError(
            f"STDO channel selector must be an annotated tag: {selector_ref}"
        )

    if cut_commit is None:
        raise StdoError(f"Latest published STDO cut {cut} must be an annotated tag")
    if selector_commit != cut_commit:
        matching_selector_cuts = [
            f"v{version}-rc.{ordinal}"
            for ordinal, (_, _, peeled) in ordinals.items()
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

    _require_legacy_selector(repository, selector_ref, selector_object)
    if qualified and historical:
        assert historical_selector_object is not None
        _require_legacy_selector(repository, historical_selector_ref, historical_selector_object)

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
        self.ref = ""
        self._temporary: tempfile.TemporaryDirectory[str] | None = None
        self.git_dir: Path | None = None
        self.tag_object = ""
        self.commit = ""
        self.tree = ""
        self.standards_tree = ""
        self.project_root = ""
        self.project_tree = ""
        self.project_release_namespace = ""
        self.release_profile: str | None = None
        self._standards_root = _STANDARDS_ROOT

    def __enter__(self) -> "GitSnapshot":
        self._temporary = tempfile.TemporaryDirectory(prefix="stdo-git-")
        self.git_dir = Path(self._temporary.name) / "objects.git"
        try:
            self.ref = _resolve_cut_ref(self.repository, self.cut)
            qualified_prefix = f"refs/tags/{_PROJECT_RELEASE_NAMESPACE}/"
            if self.ref.startswith(qualified_prefix):
                self.project_release_namespace = _PROJECT_RELEASE_NAMESPACE
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
            if is_stable_cut(self.cut):
                raw_tag = self._text(["cat-file", "tag", self.tag_object])
                headers, _separator, message = raw_tag.partition("\n\n")
                profile_lines = _profile_lines(message)
                if profile_lines != [STABLE_TAG_MARKER]:
                    raise StdoError(
                        f"Stable cut {self.cut} requires exactly one explicit "
                        f"tag-message marker: {STABLE_TAG_MARKER}"
                    )
                if "type commit" not in headers.splitlines():
                    raise StdoError(f"Stable cut {self.cut} must directly annotate a commit")
                if f"tag {_PROJECT_RELEASE_NAMESPACE}/{self.cut}" not in headers.splitlines():
                    raise StdoError(f"Stable cut {self.cut} tag name does not match its exact ref")
                self.release_profile = STABLE_PROFILE
            self.commit = self._text(["rev-parse", f"{self.ref}^{{commit}}"]).strip()
            self.tree = self._text(["rev-parse", f"{self.commit}^{{tree}}"]).strip()
            self.project_root, self._standards_root = self._detect_project_layout()
            self.project_tree = (
                self.tree
                if not self.project_root
                else self._text(
                    ["rev-parse", f"{self.commit}:{self.project_root}"]
                ).strip()
            )
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

    def _versioned_project_root(self) -> str:
        """The side-by-side version-line root this cut selects.

        Since the v2/v3 layout, each STDO version line is its own source
        project under ``specification_methodology/v<major>/``. The root is
        derived from the cut's major version so that a commit carrying
        several version lines selects exactly one.
        """
        version, _ordinal = cut_coordinates(self.cut)
        major = version.split(".", 1)[0]
        return f"{_MONOREPO_PROJECT_ROOT}/v{major}"

    def _detect_project_layout(self) -> tuple[str, str]:
        versioned_root = self._versioned_project_root()
        layouts = [
            (root, _STANDARDS_ROOT)
            for root in (
                _LEGACY_PROJECT_ROOT,
                _MONOREPO_PROJECT_ROOT,
                versioned_root,
            )
        ]
        # V3 may publish its standalone package directly at the version root.
        # Build tenants are construction subjects, never release candidates
        # selected implicitly by the installer. Older cuts keep their layouts.
        if versioned_root == f"{_MONOREPO_PROJECT_ROOT}/v3":
            layouts.append((versioned_root, _PACKAGE_STANDARDS_ROOT))
        candidates = []
        for project_root, standards_root in layouts:
            standards_path = "/".join(
                part for part in (project_root, standards_root) if part
            )
            if self._repository_object_type(standards_path) == "tree":
                candidates.append((project_root, standards_root))

        if len(candidates) != 1:

            def paths(values: list[tuple[str, str]]) -> str:
                return ", ".join(
                    "/".join(part for part in layout if part) for layout in values
                )

            found = ", ".join(
                (root or "legacy root")
                + (
                    " (standalone standards)"
                    if standards == _PACKAGE_STANDARDS_ROOT
                    else ""
                )
                for root, standards in candidates
            )
            raise StdoError(
                f"Cut {self.cut} must contain exactly one STDO project layout at "
                f"{paths(layouts)}; found {found or 'none'}"
            )
        return candidates[0]

    def _repository_path(self, logical_path: str) -> str:
        if (
            not logical_path
            or logical_path.startswith("/")
            or any(part in {"", ".", ".."} for part in logical_path.split("/"))
        ):
            raise StdoError(f"Unsafe logical STDO path: {logical_path!r}")
        if self._standards_root == _PACKAGE_STANDARDS_ROOT:
            # The manifest and its path-sensitive digest retain their canonical
            # logical coordinates; only Git acquisition uses physical paths.
            if logical_path == _STANDARDS_ROOT or logical_path.startswith(
                f"{_STANDARDS_ROOT}/"
            ):
                logical_path = (
                    _PACKAGE_STANDARDS_ROOT + logical_path[len(_STANDARDS_ROOT) :]
                )
            elif logical_path == f"releases/{self.cut.rsplit('-rc.', 1)[0]}.md":
                logical_path = "release/release-note.md"
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
        logical_paths = []
        for path in output.split("\0"):
            if not path:
                continue
            if path != repository_root and not path.startswith(f"{repository_root}/"):
                raise StdoError(f"Git member escaped requested STDO root: {path}")
            logical_paths.append(root + path[len(repository_root) :])
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

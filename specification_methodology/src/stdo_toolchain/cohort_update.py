"""Explicit complete-cohort planning; no inferred composition or semantic repair."""

from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import re
import shutil
import stat
import tempfile
from typing import Any
from urllib.parse import unquote, urlparse, urldefrag

from .errors import StdoError
from .cohort_assets import validate_semantic_index
from .git_source import _git, GitSnapshot, normalize_cut
from .manifest import build_manifest, manifest_sha256
from .product_definition import load_binding, validate_definition_document, _source_project_root
from .store import Store
from .util import atomic_write, canonical_json_bytes, ensure_relative_member, load_json, sha256_bytes

def _shape(value: Any, keys: set[str], label: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != keys:
        raise StdoError(f"Invalid {label} shape; expected {sorted(keys)}")
    return value


def _relative(value: str, *, root_ok: bool = False) -> str:
    if root_ok and value == ".":
        return value
    if not isinstance(value, str) or "\\" in value:
        raise StdoError("Expected a portable relative path")
    return ensure_relative_member(value)


def _physical(path: Path, *, leaf_link: bool = False) -> Path:
    """Check lexical components without resolving a permitted binding leaf."""
    path = Path(os.path.abspath(path))
    for part in [*reversed(path.parents), path]:
        try:
            mode = part.lstat().st_mode
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(mode) and not (leaf_link and part == path):
            raise StdoError(f"Redirected update path: {part}")
        if part != path and not stat.S_ISDIR(mode):
            raise StdoError(f"Non-directory update ancestor: {part}")
    return path


def _state(path: Path) -> dict[str, Any]:
    _physical(path, leaf_link=True)
    if path.is_symlink():
        return {"kind": "symlink", "target": os.readlink(path)}
    if not path.exists():
        return {"kind": "absent"}
    if path.is_file():
        return {"kind": "file", "sha256": sha256_bytes(path.read_bytes()),
                "mode": stat.S_IMODE(path.stat().st_mode)}
    raise StdoError(f"Update target has unsupported type: {path}")


class _Cohort:
    """A temporary exact Git view; the upstream cohort remains the inventory owner."""

    def __init__(self, selection: dict[str, Any]):
        _shape(selection, {"repository", "ref", "tag_object", "path"}, "cohort coordinate")
        self.selection = selection
        self.temp = tempfile.TemporaryDirectory(prefix="stdo-cohort-")
        self.git = Path(self.temp.name) / "objects.git"
        _git(["init", "--bare", str(self.git)])
        self.releases: dict[str, dict[str, str]] = {}
        try:
            release = self.release(selection["ref"])
            if release["tag_object"] != selection["tag_object"]:
                raise StdoError("Selected cohort tag object changed")
            self.commit = release["commit"]
            raw = self.read(self.commit, _relative(selection["path"]))
            self.document = json.loads(raw)
            self.sha256 = sha256_bytes(raw)
            if not isinstance(self.document, dict) or self.document.get("kind") != "specification-stack.release-matched-cohort" or self.document.get("schema_version") != 1:
                raise StdoError("Unsupported upstream cohort contract")
        except BaseException:
            self.close()
            raise

    def close(self) -> None:
        self.temp.cleanup()

    def text(self, *args: str) -> str:
        return str(_git(["--git-dir", str(self.git), *args])).strip()

    def read(self, commit: str, path: str) -> bytes:
        raw = _git(["--git-dir", str(self.git), "show", f"{commit}:{path}"], text=False)
        if not isinstance(raw, bytes):
            raise StdoError("Git returned non-byte member content")
        return raw

    def release(self, ref: str) -> dict[str, str]:
        if ref in self.releases:
            return self.releases[ref]
        if not isinstance(ref, str) or not re.fullmatch(r"refs/tags/[a-z0-9_-]+/v[^/]+-rc\.[1-9][0-9]*", ref):
            raise StdoError(f"Expected a project-qualified immutable RC ref: {ref!r}")
        _git(["--git-dir", str(self.git), "fetch", "--quiet", "--no-tags",
              self.selection["repository"], f"+{ref}:{ref}"])
        if self.text("cat-file", "-t", ref) != "tag":
            raise StdoError(f"Cohort cut must be annotated: {ref}")
        value = {"ref": ref, "tag_object": self.text("rev-parse", ref),
                 "commit": self.text("rev-parse", ref + "^{commit}"),
                 "tree": self.text("rev-parse", ref + "^{tree}")}
        self.releases[ref] = value
        return value

    def entries(self, commit: str, subtree: str) -> dict[str, tuple[str, bytes]]:
        root = _relative(subtree)
        raw = _git(["--git-dir", str(self.git), "ls-tree", "-r", "-z", commit, "--", root], text=False)
        if not isinstance(raw, bytes):
            raise StdoError("Git returned invalid inventory")
        result = {}
        for row in raw.split(b"\0"):
            if not row:
                continue
            meta, name = row.decode().split("\t", 1)
            mode, kind, _ = meta.split()
            if kind != "blob" or mode not in {"100644", "100755", "120000"} or not name.startswith(root + "/"):
                raise StdoError(f"Unsupported upstream entry: {name}")
            rel = _relative(name[len(root) + 1:])
            result[rel] = (mode, self.read(commit, name))
        if not result:
            raise StdoError(f"Empty upstream Product subtree: {subtree}")
        for rel, (mode, raw) in result.items():
            if mode == "120000":
                target = raw.decode()
                if Path(target).is_absolute():
                    raise StdoError(f"Absolute upstream Product symlink: {rel}")
                absolute = Path("/product") / Path(rel).parent / target
                normalized = Path(os.path.normpath(absolute))
                if not normalized.is_relative_to("/product"):
                    raise StdoError(f"Upstream symlink escapes its Product: {rel}")
        return result


class _CohortView:
    def __init__(self, cohort: _Cohort):
        self.cohort = cohort

    def exists(self, relative: str) -> bool:
        try:
            self.cohort.text("cat-file", "-e", self.cohort.commit + ":" + _relative(relative))
            return True
        except StdoError:
            return False

    def read_bytes(self, relative: str) -> bytes:
        return self.cohort.read(self.cohort.commit, _relative(relative))

    def read_json(self, relative: str) -> Any:
        return json.loads(self.read_bytes(relative))


def _assets(cohort: _Cohort, source: GitSnapshot, manifest: dict[str, Any]) -> dict[str, str]:
    document = cohort.document
    assets = _shape(document["assets"], {"spec_plugin", "stdo_semantic_index"}, "upstream cohort assets")
    version = document["cohort"]["version"]
    if any(asset["version"] != version for asset in assets.values()):
        raise StdoError("Cohort asset version mismatch")
    plugin = assets["spec_plugin"]
    if plugin["root"] != document["products"]["specification_methodology"]["subtree"] + "/plugins/spec" or sorted(plugin["manifests"]) != [".claude-plugin/plugin.json", ".codex-plugin/plugin.json"]:
        raise StdoError("Cohort plugin asset does not select its complete native manifests")
    observed = {}
    for member in plugin["manifests"]:
        raw = source.read_file("plugins/spec/" + _relative(member))
        if json.loads(raw).get("version") != version:
            raise StdoError("Cohort plugin manifest version mismatch")
        observed[plugin["root"] + "/" + member] = sha256_bytes(raw)
    semantic = assets["stdo_semantic_index"]
    root = _relative(semantic["root"])
    if not root.startswith(document["products"]["stdo_representation"]["subtree"] + "/"):
        raise StdoError("Semantic asset escapes its owning Representation Product")
    for key in ("source_corpus", "program", "map", "validation_report"):
        member = root + "/" + _relative(semantic[key])
        observed[member] = sha256_bytes(cohort.read(cohort.commit, member))
    expected = [root.removeprefix("stdo_representation/") + "/" + semantic[key] for key in ("program", "map")]
    if semantic["release_member_paths"] != expected:
        raise StdoError("Semantic asset release members are not the exact program/map")
    failures: list[str] = []
    validate_semantic_index(_CohortView(cohort), document, manifest["standards"]["members"], failures)
    if failures:
        raise StdoError("Upstream cohort asset closure failed: " + "; ".join(failures))
    return observed


def _inventory(product: dict[str, Any], entries: dict[str, tuple[str, bytes]]) -> str:
    subject = product["subject"]
    rows = []
    seen = set()
    for member in subject["members"]:
        rel = _relative(member["path"])
        if rel in seen or rel not in entries:
            raise StdoError(f"Missing/duplicate Product member: {rel}")
        seen.add(rel)
        mode, raw = entries[rel]
        kind = "symlink" if mode == "120000" else "file"
        if member["type"] != kind or sha256_bytes(raw) != member["sha256"]:
            raise StdoError(f"Changed Product member: {rel}")
        if kind == "symlink" and member.get("target") != raw.decode():
            raise StdoError(f"Changed Product symlink: {rel}")
        rows.append((rel, f"{member['sha256']}  {kind}  {rel}\n"))
    digest = sha256_bytes("".join(value for _, value in sorted(rows)).encode())
    if len(rows) != subject["member_count"] or digest != subject["member_set_sha256"]:
        raise StdoError("Upstream Product inventory mismatch")
    return digest


def _installed(root: Path, entries: dict[str, tuple[str, bytes]]) -> bool:
    _physical(root)
    if not root.exists():
        return False
    if not root.is_dir():
        raise StdoError(f"Companion Install is not a directory: {root}")
    seen = set()
    directories = {p.as_posix() for rel in entries for p in Path(rel).parents if p != Path(".")}
    for base, dirs, files in os.walk(root, followlinks=False):
        for name in [*dirs, *files]:
            path = Path(base) / name
            rel = path.relative_to(root).as_posix()
            if path.is_symlink() or path.is_file():
                seen.add(rel)
                expected = entries.get(rel)
                if expected is None:
                    raise StdoError(f"Unmanifested companion entry: {path}")
                mode, raw = expected
                if (mode == "120000") != path.is_symlink():
                    raise StdoError(f"Companion entry type changed: {path}")
                observed = os.readlink(path).encode() if path.is_symlink() else path.read_bytes()
                if observed != raw:
                    raise StdoError(f"Companion entry changed: {path}")
                if mode != "120000" and bool(path.stat().st_mode & 0o111) != (mode == "100755"):
                    raise StdoError(f"Companion executable mode changed: {path}")
            elif not path.is_dir():
                raise StdoError(f"Special companion entry: {path}")
            elif rel not in directories:
                raise StdoError(f"Unmanifested companion directory: {path}")
    if seen != set(entries):
        raise StdoError(f"Companion Install is incomplete: {root}")
    return True


def _materialize(root: Path, entries: dict[str, tuple[str, bytes]]) -> None:
    if _installed(root, entries):
        return
    root.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".cohort-", dir=root.parent))
    try:
        for rel, (mode, raw) in entries.items():
            path = staging / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            if mode == "120000":
                path.symlink_to(raw.decode())
            else:
                path.write_bytes(raw)
                path.chmod(0o555 if mode == "100755" else 0o444)
        _installed(staging, entries)
        if root.exists() or root.is_symlink():
            raise StdoError(f"Companion destination appeared during staging: {root}")
        os.rename(staging, root)
    finally:
        if staging.exists():
            shutil.rmtree(staging)


def _axiom_digest(value: Any) -> str:
    """The existing Axiom Indexer canonical JSON carrier, not semantic validation."""
    return "sha256:" + sha256_bytes(json.dumps(value, ensure_ascii=False, allow_nan=False,
                                             separators=(",", ":"), sort_keys=True).encode())


def _heading_slugs(text: str) -> set[str]:
    """The existing Axiom Indexer Markdown fragment convention."""
    slugs: set[str] = set()
    occurrences: dict[str, int] = {}
    for line in text.splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        base = match.group(1).strip().lower()
        base = re.sub(r"[^\w\- ]", "", base, flags=re.UNICODE)
        base = re.sub(r"[\s\-]+", "-", base).strip("-")
        count = occurrences.get(base, 0)
        occurrences[base] = count + 1
        slugs.add(base if count == 0 else f"{base}-{count}")
    return slugs


def _source_coverage(program: dict[str, Any], mapping: dict[str, Any], evidence: list[Any]) -> set[str]:
    """Check the existing Indexer carrier's declared source edges, not meaning."""
    if program.get("kind") != "axiom-indexer.axiomatic-program":
        raise StdoError("Unsupported derived program carrier")
    required = {program["calculus_ref"]}
    required.update(program["frame_refs"])
    for family in ("symbols", "clauses", "residuals"):
        for row in program[family]:
            required.update(row["source_refs"])
            if family == "residuals":
                required.update(row["re_entry_refs"])
    for refs in mapping.get("source_routes", {}).values():
        required.update(refs)
    required.update(mapping.get("frame_refs", []))
    if "calculus_ref" in mapping:
        required.add(mapping["calculus_ref"])
    if not all(isinstance(uri, str) for uri in required):
        raise StdoError("Invalid declared derived source coverage")
    # Indexer source digests cover the complete document. Different fragments
    # of that document share the same byte evidence, including re-entry routes.
    required_documents = {urldefrag(uri)[0] for uri in required}
    observed_documents = {urldefrag(row["uri"])[0] for row in evidence}
    if required_documents - observed_documents:
        raise StdoError("Missing declared derived source coverage: " + repr(sorted(required_documents - observed_documents)))
    return required | {row["uri"] for row in evidence}


def _derived(root: Path, selections: list[Any], source: GitSnapshot,
             updated_definition: tuple[Path, bytes]) -> tuple[list[Any], list[str]]:
    observations, holds = [], []
    if not isinstance(selections, list):
        raise StdoError("derived_context must explicitly be a list")
    for row in selections:
        _shape(row, {"program", "map", "bindings"}, "derived-context binding")
        map_path = _physical(root / _relative(row["map"]))
        bindings_path = _physical(root / _relative(row["bindings"]))
        program_path = _physical(root / _relative(row["program"]))
        try:
            mapping, binding = load_json(map_path), load_json(bindings_path)
            if mapping.get("kind") != "axiom-indexer.logical-constraint-map" or binding.get("kind") != "axiom-indexer.binding-set":
                raise StdoError("Unsupported derived source-evidence carrier")
            program = load_json(program_path)
            if mapping.get("program_sha256") != _axiom_digest(program):
                raise StdoError("Stale derived program digest")
            if mapping.get("map_sha256") != _axiom_digest({k: v for k, v in mapping.items() if k != "map_sha256"}):
                raise StdoError("Invalid derived map digest")
            rows = binding["bindings"]
            if len({r["uri_prefix"] for r in rows}) != len(rows):
                raise StdoError("Ambiguous derived source binding")
            evidence = mapping.get("resolved_sources")
            if not isinstance(evidence, list) or not evidence:
                raise StdoError("Missing derived source evidence")
            required_sources = _source_coverage(program, mapping, evidence)
            observed = []
            for item in evidence:
                uri, expected = item["uri"], item["sha256"]
                base, _ = urldefrag(uri)
                if base.startswith("stdo:"):
                    prefix = Store.release_uri(source.cut) + "standards/"
                    if not base.startswith(prefix):
                        raise StdoError(f"Stale derived STDO basis: {uri}")
                    raw = source.read_file("specification/standards/" + _relative(unquote(base[len(prefix):])))
                else:
                    matches = [r for r in rows if base.startswith(r["uri_prefix"])]
                    if not matches:
                        raise StdoError(f"Unresolved derived source: {uri}")
                    selected = max(matches, key=lambda r: len(r["uri_prefix"]))
                    physical_root = Path(selected["path"])
                    if not physical_root.is_absolute():
                        physical_root = bindings_path.parent / physical_root
                    target = _physical(physical_root / _relative(unquote(base[len(selected['uri_prefix']):])))
                    if not target.is_relative_to(physical_root.resolve()):
                        raise StdoError(f"Derived source escapes binding: {uri}")
                    raw = updated_definition[1] if target == updated_definition[0] else target.read_bytes()
                actual = "sha256:" + sha256_bytes(raw)
                if expected != actual:
                    raise StdoError(f"Stale derived source digest: {uri}")
                for required in required_sources:
                    required_base, fragment = urldefrag(required)
                    if required_base == base and fragment:
                        if Path(urlparse(base).path).suffix.lower() not in {".md", ".markdown"} or fragment not in _heading_slugs(raw.decode("utf-8")):
                            raise StdoError(f"Unresolved derived source fragment: {required}")
                observed.append({"uri": uri, "sha256": actual})
            observations.append({"program": row["program"], "program_sha256": sha256_bytes(program_path.read_bytes()),
                                 "map": row["map"], "map_sha256": sha256_bytes(map_path.read_bytes()),
                                 "bindings": row["bindings"], "bindings_sha256": sha256_bytes(bindings_path.read_bytes()),
                                 "resolved_sources": observed})
        except (StdoError, OSError, KeyError, TypeError, ValueError) as exc:
            holds.append(f"Semantic source re-entry required for {row['map']}: {exc}")
    return observations, holds


def _cohort_update(definition: Path | str, store: Store, selection_path: Path | str,
                  *, dry_run: bool = False, accepted_plan_sha256: str | None = None) -> dict[str, Any]:
    """Plan or apply one explicitly selected consumer; legacy adopt is unchanged."""
    definition = _physical(Path(definition))
    binding = load_binding(definition)
    validate_definition_document(binding.document, binding.path, store)
    definition_preimage = binding.path.read_bytes()
    definition_mode = stat.S_IMODE(binding.path.stat().st_mode)
    if sha256_bytes(definition_preimage) != binding.document_sha256:
        raise StdoError("Consumer definition changed during planning")
    selection_path = _physical(Path(selection_path))
    selection_bytes = selection_path.read_bytes()
    selection = load_json(selection_path)
    _shape(selection, {"kind", "schema_version", "definition_id", "cohort", "companions", "derived_context"}, "cohort-update selection")
    if selection["kind"] != "stdo.cohort-update-selection" or selection["schema_version"] != 1 or selection["definition_id"] != binding.document["product"]["definition_id"]:
        raise StdoError("Cohort selection does not identify this consumer")
    root = _source_project_root(binding)
    cohort = _Cohort(selection["cohort"])
    try:
        document = cohort.document
        cut = normalize_cut(document["cohort"]["cut"])
        version = cut[1:]
        products = document["products"]
        stdo = products["specification_methodology"]
        if document["cohort"]["version"] != version or stdo["version"] != version:
            raise StdoError("Cohort version mismatch")
        selected = selection["companions"]
        if not isinstance(selected, list) or not all(isinstance(r, dict) for r in selected) or {r.get("product") for r in selected} != set(products) - {"specification_methodology"} or len(selected) != len(products) - 1:
            raise StdoError("Complete selected cohort companion population is missing or duplicated")
        updated = copy.deepcopy(binding.document)
        companions, payloads, links = [], [], []
        consumed_compositions = set()
        for row in selected:
            _shape(row, {"product", "definition_member", "install_root", "links", "target_definition_id", "product_definition", "contracts"}, "companion selection")
            product = products[row["product"]]
            if product["version"] != version or product["release_ref"] != f"refs/tags/{product['namespace']}/{cut}":
                raise StdoError("Companion version/ref mismatch")
            release = cohort.release(product["release_ref"])
            if release["commit"] != cohort.commit:
                raise StdoError("Companion is not in the exact selected cohort commit")
            entries = cohort.entries(release["commit"], product["subtree"])
            inventory = _inventory(product, entries)
            definition_member = _relative(row["definition_member"])
            upstream = json.loads(entries[definition_member][1])
            release_record = _relative(product["release_note"])
            if not release_record.startswith(product["subtree"] + "/") or release_record[len(product["subtree"]) + 1:] not in entries:
                raise StdoError("Companion release record is missing from its exact Product")
            if upstream["product"]["definition_id"] != row["target_definition_id"] or upstream["constitution"]["stdo"]["basis"]["uri"] != Store.release_uri(cut):
                raise StdoError("Companion Product Definition identity/basis mismatch")
            # The existing cohort publication owner supplies the repository locator.
            publication = urlparse(document["publication"]["repository_url"])
            if publication.scheme != "https" or publication.netloc != "github.com" or len(publication.path.strip("/").removesuffix(".git").split("/")) != 2:
                raise StdoError("Unsupported cohort publication locator; no mapping inferred")
            locator_root = "https://raw.githubusercontent.com/" + publication.path.strip("/").removesuffix(".git")
            locator = row["product_definition"]
            expected_suffix = f"/{release['commit']}/{product['subtree']}/{definition_member}"
            if locator != locator_root + expected_suffix:
                raise StdoError("Companion definition locator is not bound to its exact immutable member")
            contract_suffix = f"/{release['commit']}/{product['release_note']}"
            if row["contracts"] != [locator[:-len(expected_suffix)] + contract_suffix]:
                raise StdoError("Companion contract locator does not bind the exact release record")
            matches = [i for i, c in enumerate(updated.get("composition", [])) if c.get("target_definition_id") == row["target_definition_id"]]
            if len(matches) != 1 or matches[0] in consumed_compositions:
                raise StdoError("Selected companion has no unique existing consumer composition")
            index = matches[0]; consumed_compositions.add(index)
            updated["composition"][index]["product_definition"] = locator
            updated["composition"][index]["contracts"] = row["contracts"]
            install = Path(row["install_root"])
            if not install.is_absolute():
                raise StdoError("Companion install_root must be explicit and absolute")
            install = _physical(install)
            if install.is_relative_to(root) or root.is_relative_to(install):
                raise StdoError("Companion Install must be outside the consumer source root")
            if any(install == other or install.is_relative_to(other) or other.is_relative_to(install) for other, _ in payloads):
                raise StdoError("Companion Install roots overlap")
            installed = _installed(install, entries)
            if not isinstance(row["links"], list):
                raise StdoError("Companion links must be an explicit list")
            for link in row["links"]:
                _shape(link, {"path", "member"}, "native/install link")
                member = _relative(link["member"], root_ok=True)
                if member != "." and member not in entries and not any(p.startswith(member + "/") for p in entries):
                    raise StdoError(f"Native route is absent from companion: {member}")
                path = _physical(root / _relative(link["path"]), leaf_link=True)
                before = _state(path)
                if before["kind"] not in {"absent", "symlink"}:
                    raise StdoError(f"Refusing to replace a non-link consumer entry: {path}")
                links.append({"path": str(path), "before": before, "target": str(install / member)})
            companions.append({"product": row["product"], "definition_id": row["target_definition_id"],
                               **release, "subtree": product["subtree"], "inventory_sha256": inventory,
                               "subtree_tree": cohort.text("rev-parse", release["commit"] + ":" + product["subtree"]),
                               "product_definition": locator, "contracts": row["contracts"],
                               "definition_member_sha256": sha256_bytes(entries[definition_member][1]),
                               "basis_manifest_sha256": upstream["constitution"]["stdo"]["basis"]["manifest_sha256"],
                               "install_root": str(install), "installed": installed})
            payloads.append((install, entries))
        if len({r["path"] for r in links}) != len(links):
            raise StdoError("Duplicate consumer binding target")
        with GitSnapshot(selection["cohort"]["repository"], cut) as source:
            manifest = build_manifest(source)
            digest = manifest_sha256(manifest)
            if any(c["basis_manifest_sha256"] != digest for c in companions):
                raise StdoError("Companion selected STDO manifest mismatch")
            if source.ref != stdo["release_ref"]:
                raise StdoError("Cohort STDO release ref mismatch")
            freeze = stdo.get("freeze", {})
            exact_freeze = {"tag_object": source.tag_object, "commit": source.commit, "tree": source.tree,
                            "project_subtree_tree": manifest["release"]["project_subtree_tree"],
                            "standards_tree": manifest["release"]["standards_tree"],
                            "installed_manifest_sha256": digest,
                            "standards_member_count": manifest["standards"]["member_count"],
                            "standards_member_set_sha256": manifest["standards"]["member_set_sha256"]}
            for key, actual in exact_freeze.items():
                if freeze.get(key) != actual:
                    raise StdoError(f"Cohort STDO {key} mismatch")
            asset_observations = _assets(cohort, source, manifest)
            updated["constitution"]["stdo"]["basis"] = {"uri": Store.release_uri(cut), "manifest_sha256": digest}
            updated["$schema"] = Store.release_uri(cut) + "standards/schemas/product-definition.schema.json"
            updated_bytes = (json.dumps(updated, indent=2) + "\n").encode()
            observations, holds = _derived(root, selection["derived_context"], source, (binding.path, updated_bytes))
            for companion in companions:
                for dependency, required in products[companion["product"]].get("dependencies", {}).items():
                    if dependency not in {c["product"] for c in companions} or required["version"] != version or required["product_member_set_sha256"] != products[dependency]["subject"]["member_set_sha256"]:
                        raise StdoError("Companion dependency closure mismatch")
                    if "release_ref" in required and required["release_ref"] != products[dependency]["release_ref"]:
                        raise StdoError("Companion dependency release ref mismatch")
                    if "product_member_count" in required and required["product_member_count"] != products[dependency]["subject"]["member_count"]:
                        raise StdoError("Companion dependency member count mismatch")
                    members = [(products[dependency]["subtree"] + "/" + _relative(m["path"]), m["sha256"])
                               for m in required.get("mechanics", [])]
                    if "release_record" in required:
                        members.append((_relative(required["release_record"]["path"]), required["release_record"]["sha256"]))
                    for member_path, expected in members:
                        raw = cohort.read(cohort.commit, member_path)
                        if sha256_bytes(raw) != expected:
                            raise StdoError("Companion dependency member digest mismatch")
            target = {"basis": Store.release_uri(cut), "manifest_sha256": digest,
                      "tag_object": source.tag_object, "commit": source.commit, "tree": source.tree}
        acceptance = {"kind": "stdo.cohort-update-plan", "schema_version": 1,
                      "definition": str(binding.path), "definition_id": selection["definition_id"],
                      "definition_preimage": definition_preimage.decode("utf-8"), "definition_mode": definition_mode,
                      "definition_sha256": binding.document_sha256, "selection_sha256": sha256_bytes(selection_bytes),
                      "stdo_store": str(store.root),
                      "cohort_sha256": cohort.sha256, "cohort": selection["cohort"], "target": target,
                      "assets": asset_observations,
                      "companions": [{k: v for k, v in c.items() if k != "installed"} for c in companions],
                      "bindings": links, "derived_context": observations,
                      "updated_definition": updated,
                      "updated_definition_sha256": sha256_bytes(updated_bytes), "holds": holds}
        plan_sha = sha256_bytes(canonical_json_bytes(acceptance))
        result = {**acceptance, "plan_sha256": plan_sha, "dry_run": dry_run,
                  "ready": not holds, "status": "held" if holds else "planned",
                  "complete": False, "consumer_effects": []}
        if dry_run:
            return result
        if holds:
            raise StdoError("Complete cohort update held before effects: " + "; ".join(holds))
        if accepted_plan_sha256 != plan_sha:
            raise StdoError("Complete cohort update requires its unchanged explicitly accepted plan")
        # Every input is re-derived before entering this effect phase.
        store.install(selection["cohort"]["repository"], cut, expected_manifest_sha256=digest,
                      expected_tag_object=target["tag_object"], expected_commit=target["commit"])
        validate_definition_document(updated, binding.path, store)
        for install, entries in payloads:
            _materialize(install, entries)
        with GitSnapshot(selection["cohort"]["repository"], cut) as source:
            current_observations, current_holds = _derived(root, selection["derived_context"], source, (binding.path, updated_bytes))
        if current_holds or current_observations != observations:
            raise StdoError("Derived context changed during staging; no consumer effects applied")
        if sha256_bytes(binding.path.read_bytes()) != binding.document_sha256 or stat.S_IMODE(binding.path.stat().st_mode) != definition_mode or selection_path.read_bytes() != selection_bytes or any(_state(Path(r["path"])) != r["before"] for r in links):
            raise StdoError("Consumer inputs changed during staging; no consumer effects applied")
        for install, entries in payloads:
            if not _installed(install, entries):
                raise StdoError("Companion disappeared during staging; no consumer effects applied")
        old_definition = definition_preimage
        old_mode = definition_mode
        applied, created_dirs = [], []
        try:
            for row in links:
                path = Path(row["path"])
                _physical(path, leaf_link=True)
                for parent in reversed(path.parents):
                    if parent.is_relative_to(root) and not parent.exists():
                        parent.mkdir(); created_dirs.append(parent)
                temporary = path.with_name(path.name + ".stdo-update-" + next(tempfile._get_candidate_names()))
                try:
                    temporary.symlink_to(row["target"])
                    os.replace(temporary, path)
                finally:
                    if temporary.is_symlink():
                        temporary.unlink()
                applied.append(row)
            atomic_write(binding.path, updated_bytes, mode=old_mode)
            if any(not Path(r["path"]).exists() or Path(r["path"]).resolve() != Path(r["target"]).resolve() for r in links):
                raise StdoError("Native route verification failed after update")
            for install, entries in payloads:
                if not _installed(install, entries):
                    raise StdoError("Companion disappeared during application")
        except BaseException:
            if binding.path.read_bytes() != old_definition:
                atomic_write(binding.path, old_definition, mode=old_mode)
            for row in reversed(applied):
                path = Path(row["path"])
                path.unlink(missing_ok=True)
                if row["before"]["kind"] == "symlink":
                    path.symlink_to(row["before"]["target"])
            for parent in reversed(created_dirs):
                parent.rmdir()
            raise
        result.update(status="updated", complete=True, accepted_plan_sha256=accepted_plan_sha256,
                      consumer_effects=[r["path"] for r in links] + [str(binding.path)])
        return result
    except (KeyError, TypeError, ValueError, OSError) as exc:
        raise StdoError(f"Invalid or unavailable complete-cohort input: {exc}") from exc
    finally:
        cohort.close()


def cohort_update(definition: Path | str, store: Store, selection_path: Path | str,
                  *, dry_run: bool = False, accepted_plan_sha256: str | None = None) -> dict[str, Any]:
    try:
        return _cohort_update(definition, store, selection_path, dry_run=dry_run,
                              accepted_plan_sha256=accepted_plan_sha256)
    except (KeyError, TypeError, ValueError, OSError, AttributeError) as exc:
        raise StdoError(f"Invalid or unavailable complete-cohort input: {exc}") from exc

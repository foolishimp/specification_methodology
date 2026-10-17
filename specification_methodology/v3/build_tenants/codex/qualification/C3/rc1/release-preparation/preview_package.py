#!/usr/bin/env python3
"""Export one frozen Codex review package and probe existing packaging functions.

This is a local qualification helper. It creates no Git objects or refs, calls
no installer, and creates no release manifest. The output must be fresh /tmp
scratch. A complete candidate archive preserves interpretation and source paths.
"""

from __future__ import annotations

import argparse
import ast
import gzip
import hashlib
import io
import json
import re
import subprocess
import sys
import tarfile
from pathlib import Path


PREFIX = "specification_methodology/v3/build_tenants/codex/successor"
TERRITORY = "specification_methodology/v3/build_tenants/codex/qualification/C3/rc1/release-preparation"
MAJOR_ROOT = "specification_methodology/v3"
PROPOSED_CUT = "v3.0.0-rc.1"
DEPENDENCY_COHORT_REVISION = "60eb7a2d43d9ac2d9557eae94a51db192209f06b"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--revision", required=True, help="Exact frozen commit, never a moving ref")
    parser.add_argument("--output", type=Path, required=True, help="Fresh directory under /tmp")
    parser.add_argument("--record", action="store_true", help="Copy small receipts into the granted territory")
    parser.add_argument("--theory-root", type=Path,
                        help="Include the exact already-installed encoding theory and pinned checker in a review bundle")
    args = parser.parse_args()
    repository = args.repository.resolve()
    output = args.output.resolve()
    if not re.fullmatch(r"[0-9a-f]{40}", args.revision):
        parser.error("--revision must be a full 40-character commit")
    if not output.is_relative_to(Path("/tmp").resolve()) or output.exists():
        parser.error("--output must be a fresh directory below /tmp")

    def git(*arguments: str) -> bytes:
        return subprocess.check_output(["git", "-C", str(repository), *arguments])

    resolved = git("rev-parse", args.revision + "^{commit}").decode().strip()
    if resolved != args.revision:
        parser.error("The selected object is not itself a commit")
    package_tree = git("rev-parse", args.revision + ":" + PREFIX).decode().strip()
    common_git = Path(git("rev-parse", "--path-format=absolute", "--git-common-dir").decode().strip())
    members = []
    for raw in git("ls-tree", "-rz", args.revision, "--", PREFIX).split(b"\0"):
        if not raw:
            continue
        descriptor, raw_path = raw.split(b"\t", 1)
        mode, kind, object_id = descriptor.decode().split()
        path = raw_path.decode()
        relative = path.removeprefix(PREFIX + "/")
        if not path.startswith(PREFIX + "/") or ".." in Path(relative).parts:
            raise SystemExit("Unsafe source member")
        if mode not in {"100644", "100755"} or kind != "blob":
            raise SystemExit("Preview requires ordinary Git blobs: " + path)
        members.append((relative, mode, object_id))
    if not members:
        raise SystemExit("Empty candidate package")

    # Local imports use the already installed toolchain; no install is invoked.
    from stdo_toolchain.errors import StdoError
    from stdo_toolchain.git_source import GitSnapshot
    from stdo_toolchain.manifest import _members, build_manifest, standards_member_set_sha256
    from stdo_toolchain.cohort_assets import canonical_value_sha256, validate_source_routes
    import stdo_toolchain.git_source as git_source_module
    import stdo_toolchain.manifest as manifest_module

    output.mkdir(parents=True)
    candidate = output / "candidate"
    promotion = output / "promotion-layout"
    promoted_root = promotion / MAJOR_ROOT
    inventory = []
    archive_path = output / "codex-rc1-review-package.tar.gz"
    with archive_path.open("wb") as target:
        with gzip.GzipFile(filename="", mode="wb", fileobj=target, mtime=0) as compressed:
            with tarfile.open(mode="w", fileobj=compressed, format=tarfile.PAX_FORMAT) as archive:
                for relative, mode, object_id in sorted(members):
                    data = git("cat-file", "blob", object_id)
                    path = candidate / relative
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(data)
                    path.chmod(0o755 if mode == "100755" else 0o644)
                    member = tarfile.TarInfo("codex-rc1-review/" + relative)
                    member.size = len(data)
                    member.mode = 0o755 if mode == "100755" else 0o644
                    member.uid = member.gid = member.mtime = 0
                    archive.addfile(member, io.BytesIO(data))
                    inventory.append({"path": relative, "mode": mode, "git_blob": object_id,
                                      "bytes": len(data), "sha256": digest(data)})
                    promoted = None
                    if relative.startswith("standards/"):
                        promoted = promoted_root / "specification" / relative
                    elif relative.startswith("plugins/spec/") or relative == "LICENSE":
                        promoted = promoted_root / relative
                    if promoted is not None:
                        promoted.parent.mkdir(parents=True, exist_ok=True)
                        promoted.write_bytes(data)

    # Probe the real loader without entering GitSnapshot's temporary fetch path.
    original = GitSnapshot(str(repository), PROPOSED_CUT)
    original.git_dir, original.commit = common_git, args.revision
    try:
        original_layout = {"selected_root": original._detect_project_root()}
    except StdoError as exc:
        original_layout = {"refusal": str(exc)}

    class LayoutSnapshot(GitSnapshot):
        def _repository_object_type(self, path: str) -> str | None:
            target = promotion / path
            return "tree" if target.is_dir() else "blob" if target.is_file() else None

        def path_exists(self, path: str) -> bool:
            return (promoted_root / path).exists()

        def list_files(self, root: str) -> list[str]:
            return sorted(p.relative_to(promoted_root).as_posix()
                          for p in (promoted_root / root).rglob("*") if p.is_file())

        def read_file(self, path: str) -> bytes:
            return (promoted_root / path).read_bytes()

    preview = LayoutSnapshot(str(repository), PROPOSED_CUT)
    selected_root = preview._detect_project_root()
    standard_members = _members(preview, "specification/standards")
    plugin_members = _members(preview, "plugins/spec")
    try:
        build_manifest(preview)
    except StdoError as exc:
        manifest_refusal = str(exc)
    else:
        raise SystemExit("Unexpected release-manifest construction; preview must have no release note")

    source_inventory = json.loads((candidate / "interpretation/SOURCE_INVENTORY.json").read_bytes())
    document_failures = [row["path"] for row in source_inventory["document_members"]
                         if digest((candidate / row["path"]).read_bytes()) != row["sha256"]]
    program = json.loads((candidate / "interpretation/program.json").read_bytes())
    constraint_map = json.loads((candidate / "interpretation/map.json").read_bytes())
    route_failures: list[str] = []
    validate_source_routes(program, PROPOSED_CUT, "program", route_failures)
    validate_source_routes(constraint_map, PROPOSED_CUT, "map", route_failures)
    plugin_versions = {relative: json.loads((candidate / "plugins/spec" / relative).read_bytes())["version"]
                       for relative in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json")}
    map_without_digest = dict(constraint_map)
    declared_map_digest = map_without_digest.pop("map_sha256")
    inventory_digest = digest("".join(f"{r['sha256']}  {r['path']}\n" for r in inventory).encode())
    receipt = {
        "kind": "codex.rc1-review-package-preview", "schema_version": 1,
        "status": "review_package_constructed_release_not_cut",
        "repository": str(repository), "source_commit": args.revision,
        "source_path": PREFIX, "source_tree": package_tree,
        "proposed_cut_used_only_for_loader_probe": PROPOSED_CUT,
        "package": {"path": str(archive_path), "sha256": digest(archive_path.read_bytes()),
                    "member_count": len(inventory), "uncompressed_member_bytes": sum(r["bytes"] for r in inventory),
                    "member_set_sha256": inventory_digest},
        "byte_preservation": {"all_exported_members_match_git_blobs": all(digest((candidate / r["path"]).read_bytes()) == r["sha256"] for r in inventory),
                              "document_inventory_count": len(source_inventory["document_members"]),
                              "document_inventory_failures": document_failures},
        "existing_loader_probe": {"original_frozen_layout": original_layout,
                                  "promoted_layout_selected_root": selected_root,
                                  "manifest_construction_refusal": manifest_refusal,
                                  "standards_member_count": len(standard_members),
                                  "standards_member_set_sha256": standards_member_set_sha256(standard_members),
                                  "plugin_member_count": len(plugin_members)},
        "excluded_by_existing_install_payload": [r["path"] for r in inventory if r["path"] != "LICENSE" and not r["path"].startswith(("standards/", "plugins/spec/"))],
        "interpretation_probe": {"source_basis": program["source_basis"], "program_uri": program["uri"],
                                 "encoding_theory": source_inventory["encoding_theory"],
                                 "map_binds_program": constraint_map["program_sha256"] == "sha256:" + canonical_value_sha256(program),
                                 "map_intrinsic_digest_valid": declared_map_digest == "sha256:" + canonical_value_sha256(map_without_digest),
                                 "v3_cohort_route_refusals": sorted(set(route_failures)),
                                 "cohort_program_and_source_binding_ready": False},
        "plugin_versions": plugin_versions,
        "tooling": {"python": sys.executable,
                    "git_source_sha256": digest(Path(git_source_module.__file__).read_bytes()),
                    "manifest_sha256": digest(Path(manifest_module.__file__).read_bytes())},
        "effects": {"git_mutations": False, "installer_called": False, "external_calls": False,
                    "scratch_root": str(output)},
        "limits": ["This receipt applies only to its exact source_commit; a changed candidate requires an applicability check.",
                   "The filesystem adapter probes path selection, not a tagged Git acquisition.",
                   "No release note, tag, installed-manifest digest, acceptance or fresh install exists for this preview.",
                   "Interpretation fidelity and complete native usability are separate qualification obligations."]
    }

    if args.theory_root is not None:
        theory_root = args.theory_root.resolve()
        basis = source_inventory["encoding_theory"]
        theory_manifest_bytes = (theory_root / "manifest.json").read_bytes()
        if digest(theory_manifest_bytes) != basis["manifest_sha256"]:
            raise SystemExit("Theory manifest does not match the candidate's admitted basis")
        theory_manifest = json.loads(theory_manifest_bytes)
        if digest((theory_root / basis["member"]).read_bytes()) != basis["member_sha256"]:
            raise SystemExit("Theory member does not match the candidate's admitted basis")
        dependency_root = output / "dependencies"
        dependency_rows = []

        def add_dependency(relative: str, data: bytes, origin: str, target: str | None = None) -> None:
            path = dependency_root / relative
            if Path(relative).is_absolute() or ".." in Path(relative).parts:
                raise SystemExit("Unsafe dependency member")
            path.parent.mkdir(parents=True, exist_ok=True)
            if target is None:
                path.write_bytes(data)
            else:
                if Path(target).is_absolute() or not (path.parent / target).resolve().is_relative_to(dependency_root):
                    raise SystemExit("Dependency discovery link escapes the bundle")
                path.symlink_to(target)
            dependency_rows.append({"path": "dependencies/" + relative, "type": "symlink" if target else "file",
                                    "bytes": len(data), "sha256": digest(data), "origin": origin,
                                    **({"target": target} if target else {})})

        theory_paths = {"manifest.json": digest(theory_manifest_bytes)}
        for section in (theory_manifest["standards"], theory_manifest["auxiliary"]["plugin"]):
            for row in section["members"]:
                theory_paths[section["installed_root"] + "/" + row["path"]] = row["sha256"]
        for key, path_key in (("license", "path"), ("release_note", "installed_path")):
            row = theory_manifest["auxiliary"][key]
            theory_paths[row[path_key]] = row["sha256"]
        for relative, expected in sorted(theory_paths.items()):
            source = theory_root / relative
            if source.is_symlink() or not source.is_file():
                raise SystemExit("Theory member is not an ordinary verified file: " + relative)
            data = source.read_bytes()
            if digest(data) != expected:
                raise SystemExit("Theory member drift: " + relative)
            add_dependency("encoding-theory/" + relative, data, basis["release_uri"] + relative)

        frozen_cohort = json.loads(git("show", DEPENDENCY_COHORT_REVISION + ":stack_release.json"))
        checker_product = frozen_cohort["products"]["axiom_indexer"]
        checker_pin = source_inventory["checker"]
        checker_ref = checker_pin["release_ref"]
        checker_commit = git("rev-parse", checker_ref + "^{commit}").decode().strip()
        checker_tag = git("rev-parse", checker_ref).decode().strip()
        if git("cat-file", "-t", checker_ref).decode().strip() != "tag" or checker_commit != checker_pin["commit"]:
            raise SystemExit("Checker's annotated release does not match the candidate pin")
        subject = checker_product["subject"]
        if checker_product["release_ref"] != checker_ref or subject["member_set_sha256"] != checker_pin["inventory_sha256"]:
            raise SystemExit("The frozen cohort does not name the candidate's exact checker inventory")
        checker_prefix = checker_product["subtree"]
        for row in subject["members"]:
            coordinate = checker_commit + ":" + checker_prefix + "/" + row["path"]
            data = git("show", coordinate)
            if digest(data) != row["sha256"] or (row["type"] == "symlink" and data.decode() != row["target"]):
                raise SystemExit("Checker subject member drift: " + row["path"])
            add_dependency("axiom-indexer/" + row["path"], data, coordinate,
                           row.get("target") if row["type"] == "symlink" else None)
        checker_code = dependency_root / "axiom-indexer/build_tenants/core/code/ac.py"
        if digest(checker_code.read_bytes()) != checker_pin["executable_sha256"]:
            raise SystemExit("Checker executable differs from candidate pin")

        # Include only release-carried licensing, without acquiring unrelated history.
        license_coordinates = []
        for candidate_license in (checker_prefix + "/LICENSE", "LICENSE"):
            probe = subprocess.run(["git", "-C", str(repository), "cat-file", "-e", checker_commit + ":" + candidate_license],
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if probe.returncode == 0:
                coordinate = checker_commit + ":" + candidate_license
                add_dependency("axiom-indexer/LICENSE", git("show", coordinate), coordinate)
                license_coordinates.append(coordinate)
                break

        imports = set()
        for node in ast.walk(ast.parse(checker_code.read_bytes())):
            if isinstance(node, ast.Import):
                imports.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                imports.add(node.module or "")
        nonstandard_imports = sorted(name for name in imports if name.split(".")[0] not in sys.stdlib_module_names)
        if nonstandard_imports:
            raise SystemExit("Unaccounted checker runtime imports: " + ", ".join(nonstandard_imports))
        bundle_readme = """# Codex RC1 review bundle

This is a frozen review subject, not an immutable RC release or an adoption.
`candidate/` preserves the selected successor package. `dependencies/` carries
only its exact admitted construction-time encoding theory and checker. Existing
license files are included; the checker's declared Product subject carries no
license, and its release has none at axiom_indexer/LICENSE or root LICENSE.
No license is inferred from the neighbouring corpus. These dependencies supply
no candidate acceptance or final v3
encoding/cohort decision. Package inventories record source identities.

Runtime prerequisite: Python 3.13 was exercised for the binding command. The
shipped binding script and checker import only Python standard-library modules;
no Python runtime, native agent host, or environment provisioner is included.
On a machine with that runtime already available, the following local commands
require no network. Environment provisioning was not tested offline. The full
checker/project operation remains task-selected and was not run by packaging.

From the extracted bundle root, using an explicit scratch output directory:

```sh
python3.13 -B candidate/interpretation/bindings.py \\
  --theory-root "$PWD/dependencies/encoding-theory" > "$REVIEW_OUTPUT/bindings.json"
python3.13 -B dependencies/axiom-indexer/build_tenants/core/code/ac.py project \\
  --program candidate/interpretation/program.json \\
  --map candidate/interpretation/map.json \\
  --bindings "$REVIEW_OUTPUT/bindings.json" \\
  --frame-index "$SELECTED_FRAME_INDEX" --mode materialized \\
  --output "$REVIEW_OUTPUT/projection.json"
```

Select the frame index from candidate/interpretation/FRAMES.md for the actual
review task. Outputs stay outside the frozen bundle. Structural projection
does not prove interpretation fidelity, method acceptance or release readiness.
"""
        (output / "BUNDLE_README.md").write_text(bundle_readme)
        dependency_receipt = {"kind": "codex.rc1-review-dependencies", "encoding_theory": basis,
                              "checker": {**checker_pin, "tag_object": checker_tag,
                                          "inventory_source": DEPENDENCY_COHORT_REVISION + ":stack_release.json"},
                              "checker_imports": sorted(imports), "third_party_imports": nonstandard_imports,
                              "checker_license_coordinates": license_coordinates,
                              "checker_license_search": [checker_commit + ":" + checker_prefix + "/LICENSE", checker_commit + ":LICENSE"],
                              "runtime_prerequisite": "Python 3.13 exercised; runtime and native hosts are not included",
                              "members": sorted(dependency_rows, key=lambda row: row["path"])}
        write_json(output / "DEPENDENCY_MEMBERS.json", dependency_receipt)
        bundle_path = output / "codex-rc1-review-bundle.tar.gz"
        bundle_members = [("candidate/" + row["path"], candidate / row["path"]) for row in inventory]
        bundle_members += [(row["path"], output / row["path"]) for row in dependency_rows]
        write_json(output / "PACKAGE_MEMBERS.json", {"source_commit": args.revision, "source_tree": package_tree, "members": inventory})
        bundle_members += [(name, output / name) for name in ("BUNDLE_README.md", "PACKAGE_MEMBERS.json", "DEPENDENCY_MEMBERS.json")]
        with bundle_path.open("wb") as target:
            with gzip.GzipFile(filename="", mode="wb", fileobj=target, mtime=0) as compressed:
                with tarfile.open(mode="w", fileobj=compressed, format=tarfile.PAX_FORMAT) as archive:
                    for relative, path in sorted(bundle_members):
                        member = tarfile.TarInfo("codex-rc1-review/" + relative)
                        member.uid = member.gid = member.mtime = 0
                        member.mode = 0o644
                        if path.is_symlink():
                            member.type, member.linkname = tarfile.SYMTYPE, path.readlink().as_posix()
                            archive.addfile(member)
                        else:
                            data = path.read_bytes()
                            member.mode = path.stat().st_mode & 0o777
                            member.size = len(data)
                            archive.addfile(member, io.BytesIO(data))
        receipt["review_bundle"] = {"path": str(bundle_path), "sha256": digest(bundle_path.read_bytes()),
                                    "candidate_members": len(inventory), "dependency_members": len(dependency_rows),
                                    "metadata_members": 3, "checker_tag_object": checker_tag,
                                    "runtime_bundled": False, "installed_or_adopted": False}
        receipt["effects"]["dependency_acquisition"] = "Exact selected installed theory files and tagged checker blobs copied into scratch only"
        # One real exported-consumer binding probe; no checker suite or install.
        extracted = output / "reacquired"
        with tarfile.open(bundle_path, "r:gz") as archive:
            archive.extractall(extracted, filter="data")
        consumer = extracted / "codex-rc1-review"
        readback_failures = [row["path"] for row in inventory
                             if digest((consumer / "candidate" / row["path"]).read_bytes()) != row["sha256"]]
        for row in dependency_rows:
            path = consumer / row["path"]
            data = path.readlink().as_posix().encode() if row["type"] == "symlink" else path.read_bytes()
            if digest(data) != row["sha256"]:
                readback_failures.append(row["path"])
        argv = [sys.executable, "-B", str(consumer / "candidate/interpretation/bindings.py"),
                "--theory-root", str(consumer / "dependencies/encoding-theory")]
        bound = subprocess.run(argv, text=True, capture_output=True, check=False)
        (output / "reacquired-bindings.json").write_text(bound.stdout)
        reacquisition = {"kind": "codex.rc1-review-bundle-reacquisition", "archive_sha256": digest(bundle_path.read_bytes()),
                         "candidate_and_dependency_members_verified": len(inventory) + len(dependency_rows),
                         "member_failures": readback_failures, "binding_argv": argv,
                         "binding_returncode": bound.returncode, "binding_stderr": bound.stderr,
                         "bindings_sha256": digest(bound.stdout.encode()),
                         "python_version": sys.version, "network_used": False,
                         "runtime_provisioning_tested": False, "installer_called": False,
                         "checker_project_operation_run": False}
        write_json(output / "BUNDLE_REACQUISITION.json", reacquisition)
        if readback_failures or bound.returncode:
            raise SystemExit("Review bundle reacquisition failed; see BUNDLE_REACQUISITION.json")
        receipt["review_bundle"]["fresh_archive_binding_verified"] = True
    write_json(output / "PACKAGE_MEMBERS.json", {"source_commit": args.revision, "source_tree": package_tree, "members": inventory})
    write_json(output / "PREVIEW_RECEIPT.json", receipt)
    if args.record:
        territory = repository / TERRITORY
        territory.mkdir(parents=True, exist_ok=True)
        for name in ("PACKAGE_MEMBERS.json", "PREVIEW_RECEIPT.json", "DEPENDENCY_MEMBERS.json", "BUNDLE_REACQUISITION.json"):
            if not (output / name).exists():
                continue
            (territory / name).write_bytes((output / name).read_bytes())
    print(json.dumps({"status": receipt["status"], "package": receipt["package"],
                      "existing_loader_probe": receipt["existing_loader_probe"],
                      "interpretation_probe": receipt["interpretation_probe"],
                      "byte_preservation": receipt["byte_preservation"],
                      "review_bundle": receipt.get("review_bundle")}, indent=2))


if __name__ == "__main__":
    main()

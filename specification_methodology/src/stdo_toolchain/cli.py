"""Command-line entrypoint for the STDO toolchain manager."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from . import __version__
from .constants import OFFICIAL_REPOSITORY
from .cohort_update import cohort_update
from .errors import StdoError
from .git_source import GitSnapshot
from .manifest import build_manifest, manifest_sha256
from .product_definition import (
    adopt_definition,
    definition_status,
    discover_definitions,
    install_bootstrap,
    load_binding,
    sync_definition,
)
from .store import Store, default_store_path
from .util import canonical_json_bytes, sha256_bytes


def _print(value: Any) -> None:
    print(json.dumps(value, indent=2, sort_keys=True, default=str))


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="stdo",
        description="Install, resolve, verify, and adopt immutable STDO releases",
    )
    parser.add_argument(
        "--store",
        type=Path,
        default=None,
        help=f"Shared installation store (default: {default_store_path()})",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    install = subparsers.add_parser("install", help="Install one immutable STDO RC cut")
    install.add_argument("cut")
    install.add_argument("--repository", default=OFFICIAL_REPOSITORY)
    install.add_argument("--manifest-sha256")

    list_parser = subparsers.add_parser(
        "list", help="List installed immutable STDO cuts"
    )
    list_parser.set_defaults(command="list")

    resolve = subparsers.add_parser("resolve", help="Resolve an installed stdo URI")
    resolve.add_argument("uri")

    verify = subparsers.add_parser(
        "verify", help="Verify an installed immutable STDO cut"
    )
    verify.add_argument("cut")
    verify.add_argument("--manifest-sha256")

    manifest = subparsers.add_parser(
        "manifest",
        help="Construct the deterministic installed-release manifest for a cut",
    )
    manifest.add_argument("cut")
    manifest.add_argument("--repository", default=OFFICIAL_REPOSITORY)

    status = subparsers.add_parser("status", help="Report one Product Definition basis")
    status.add_argument("--definition", type=Path, required=True)
    status.add_argument("--verify", action="store_true")

    sync = subparsers.add_parser(
        "sync",
        help="Install and verify the exact basis selected by a Product Definition",
    )
    sync.add_argument("--definition", type=Path, required=True)
    sync.add_argument("--dry-run", action="store_true")

    adopt = subparsers.add_parser(
        "adopt",
        help="Resolve a Product Definition selector and adopt its exact immutable cut",
    )
    adopt.add_argument("--definition", type=Path, required=True)
    adopt_mode = adopt.add_mutually_exclusive_group()
    adopt_mode.add_argument("--dry-run", action="store_true")
    adopt_mode.add_argument(
        "--accept-plan-sha256",
        help="Digest emitted by a prior adoption dry-run",
    )

    cohort = subparsers.add_parser(
        "cohort-update", help="Plan or apply an explicitly selected complete consumer cohort"
    )
    cohort.add_argument("--definition", type=Path, required=True)
    cohort.add_argument("--selection", type=Path, required=True)
    cohort_mode = cohort.add_mutually_exclusive_group(required=True)
    cohort_mode.add_argument("--dry-run", action="store_true")
    cohort_mode.add_argument("--accept-plan-sha256")

    bootstrap = subparsers.add_parser(
        "bootstrap",
        help="Install or refresh stable STDO markers in declared agent files",
    )
    bootstrap.add_argument("--definition", type=Path, required=True)
    bootstrap.add_argument("--dry-run", action="store_true")

    fleet = subparsers.add_parser(
        "fleet", help="Operate on discovered Product Definitions"
    )
    fleet_subparsers = fleet.add_subparsers(dest="fleet_command", required=True)

    for name in ("status", "verify"):
        fleet_status = fleet_subparsers.add_parser(name)
        fleet_status.add_argument("--root", type=Path, required=True)

    fleet_adopt = fleet_subparsers.add_parser("adopt")
    fleet_adopt.add_argument("--root", type=Path, required=True)
    fleet_adopt.add_argument("--all", action="store_true")
    fleet_adopt_mode = fleet_adopt.add_mutually_exclusive_group()
    fleet_adopt_mode.add_argument("--dry-run", action="store_true")
    fleet_adopt_mode.add_argument(
        "--accept-plan-sha256",
        help="Fleet-plan digest emitted by a prior fleet adoption dry-run",
    )

    fleet_sync = fleet_subparsers.add_parser("sync")
    fleet_sync.add_argument("--root", type=Path, required=True)
    fleet_sync.add_argument("--all", action="store_true")
    fleet_sync.add_argument("--dry-run", action="store_true")

    fleet_bootstrap = fleet_subparsers.add_parser("bootstrap")
    fleet_bootstrap.add_argument("--root", type=Path, required=True)
    fleet_bootstrap.add_argument("--all", action="store_true")
    fleet_bootstrap.add_argument("--dry-run", action="store_true")

    return parser


def _run_fleet(arguments: argparse.Namespace, store: Store) -> tuple[Any, int]:
    fleet_root = arguments.root.resolve()
    authorized_root = fleet_root if fleet_root.is_dir() else fleet_root.parent
    definitions = discover_definitions(arguments.root)
    if not definitions:
        raise StdoError(
            f"No stdo_<label>.json definitions found under {arguments.root}"
        )
    identities: dict[str, Path] = {}
    for path in definitions:
        binding = load_binding(path)
        identity = binding.document.get("product", {}).get("definition_id")
        if not isinstance(identity, str) or not identity:
            raise StdoError(f"Product Definition has no definition identity: {path}")
        prior = identities.get(identity)
        if prior is not None:
            raise StdoError(
                f"Duplicate Product-Definition Identity {identity!r}: {prior} and {path}"
            )
        identities[identity] = path
    if arguments.fleet_command in {"adopt", "sync", "bootstrap"} and not arguments.all:
        raise StdoError("Fleet writes require explicit --all")

    if arguments.fleet_command in {"status", "verify"}:
        values = [
            definition_status(
                path,
                store,
                verify=arguments.fleet_command == "verify",
            )
            for path in definitions
        ]
        valid = all(value["valid"] for value in values)
        return {
            "root": str(fleet_root),
            "definitions": values,
        }, 0 if valid else 1

    if arguments.fleet_command == "bootstrap":
        plans = [
            install_bootstrap(
                path,
                store,
                dry_run=True,
                authorized_root=authorized_root,
            )
            for path in definitions
        ]
        if arguments.dry_run:
            return {"root": str(fleet_root), "plans": plans}, 0
        values = [
            install_bootstrap(
                path,
                store,
                dry_run=False,
                authorized_root=authorized_root,
            )
            for path in definitions
        ]
        return {
            "root": str(fleet_root),
            "plans": plans,
            "applied": values,
        }, 0

    if arguments.fleet_command == "sync":
        values = [
            sync_definition(path, store, dry_run=arguments.dry_run)
            for path in definitions
        ]
        return {"root": str(fleet_root), "definitions": values}, 0

    plans = [adopt_definition(path, store, dry_run=True) for path in definitions]
    fleet_acceptance = {
        "kind": "stdo.fleet-adoption-plan",
        "schema_version": 1,
        "root": str(fleet_root),
        "definitions": [
            {
                "definition": str(path.resolve().relative_to(authorized_root)),
                "definition_id": plan["definition_id"],
                "plan_sha256": plan["plan_sha256"],
            }
            for path, plan in zip(definitions, plans, strict=True)
        ],
    }
    fleet_plan_sha256 = sha256_bytes(canonical_json_bytes(fleet_acceptance))
    if arguments.dry_run:
        return {
            "root": str(fleet_root),
            "plan_sha256": fleet_plan_sha256,
            "plans": plans,
        }, 0
    if arguments.accept_plan_sha256 is None:
        raise StdoError(
            "Mutating fleet adoption requires --accept-plan-sha256 from a prior dry-run"
        )
    if arguments.accept_plan_sha256 != fleet_plan_sha256:
        raise StdoError(
            "Fleet adoption plan differs from the explicitly accepted plan "
            f"(accepted {arguments.accept_plan_sha256}, current {fleet_plan_sha256})"
        )
    applied = [
        adopt_definition(
            path,
            store,
            dry_run=False,
            accepted_plan_sha256=plan["plan_sha256"],
        )
        for path, plan in zip(definitions, plans, strict=True)
    ]
    return {
        "root": str(fleet_root),
        "accepted_plan_sha256": fleet_plan_sha256,
        "plans": plans,
        "applied": applied,
    }, 0


def run(arguments: argparse.Namespace) -> tuple[Any, int]:
    store = Store(arguments.store)
    if arguments.command == "install":
        installed = store.install(
            arguments.repository,
            arguments.cut,
            expected_manifest_sha256=arguments.manifest_sha256,
        )
        return {
            "cut": installed.cut,
            "uri": installed.uri,
            "path": str(installed.path),
            "manifest_sha256": installed.manifest_sha256,
            "status": installed.status,
            "release": installed.manifest["release"],
            "standards": {
                "member_count": installed.manifest["standards"]["member_count"],
                "member_set_sha256": installed.manifest["standards"][
                    "member_set_sha256"
                ],
            },
        }, 0
    if arguments.command == "list":
        return {"store": str(store.root), "releases": store.list_releases()}, 0
    if arguments.command == "resolve":
        return {"uri": arguments.uri, "path": str(store.resolve(arguments.uri))}, 0
    if arguments.command == "verify":
        report = store.verify(
            arguments.cut,
            expected_manifest_sha256=arguments.manifest_sha256,
        )
        return report, 0 if report["valid"] else 1
    if arguments.command == "manifest":
        with GitSnapshot(arguments.repository, arguments.cut) as snapshot:
            manifest = build_manifest(snapshot)
        return {
            "manifest_sha256": manifest_sha256(manifest),
            "manifest": manifest,
        }, 0
    if arguments.command == "status":
        report = definition_status(arguments.definition, store, verify=arguments.verify)
        return report, 0 if report["valid"] else 1
    if arguments.command == "sync":
        return (
            sync_definition(
                arguments.definition,
                store,
                dry_run=arguments.dry_run,
            ),
            0,
        )
    if arguments.command == "adopt":
        return (
            adopt_definition(
                arguments.definition,
                store,
                dry_run=arguments.dry_run,
                accepted_plan_sha256=arguments.accept_plan_sha256,
            ),
            0,
        )
    if arguments.command == "cohort-update":
        report = cohort_update(
            arguments.definition, store, arguments.selection,
            dry_run=arguments.dry_run,
            accepted_plan_sha256=arguments.accept_plan_sha256,
        )
        return report, 0 if report["ready"] else 1
    if arguments.command == "bootstrap":
        return (
            install_bootstrap(
                arguments.definition,
                store,
                dry_run=arguments.dry_run,
            ),
            0,
        )
    if arguments.command == "fleet":
        return _run_fleet(arguments, store)
    raise StdoError(f"Unsupported command: {arguments.command}")


def main(argv: list[str] | None = None) -> None:
    parser = _parser()
    arguments = parser.parse_args(argv)
    try:
        result, exit_code = run(arguments)
        _print(result)
    except StdoError as exc:
        _print({"error": str(exc)})
        exit_code = 2
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()

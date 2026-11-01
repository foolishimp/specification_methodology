#!/usr/bin/env python3
"""Exercise the ordinary manager against a disposable native documentation cut."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys

V3 = Path(__file__).resolve().parents[2]


def documentation_tools():
    path = Path(__file__).resolve().with_name("documentation.py")
    try:
        spec = importlib.util.spec_from_file_location("stdo_qualification_documentation", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except (OSError, ImportError) as exc:
        raise ValueError("required documentation tool unavailable: " + str(exc)) from exc


def command(argv, *, cwd=None, env=None):
    result = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr or result.stdout)
    return result.stdout


def qualify(package, run, manager="stdo"):
    docs = documentation_tools()
    executable = shutil.which(str(manager))
    docs.require(executable is not None, "selected installed manager is unavailable")
    manager_version = command([executable, "--version"]).strip()
    package, run = Path(package).resolve(), Path(run).absolute()
    docs.require(not run.exists(), "preserve existing qualification run")
    docs.require(not run.resolve().is_relative_to(package), "qualification output overlaps package")
    docs.check(package)
    run.mkdir(parents=True)
    repository = run / "fixture-repository"
    project = repository / "specification_methodology/v3"
    shutil.copytree(package, project)
    command(["git", "init", "-q"], cwd=repository)
    command(["git", "add", "."], cwd=repository)
    command(["git", "-c", "user.name=STDO Documentation Qualification",
             "-c", "user.email=qualification@example.invalid", "commit", "-qm",
             "Synthetic 3.0.3 installed-documentation fixture; not a public release"], cwd=repository)
    command(["git", "-c", "user.name=STDO Documentation Qualification",
             "-c", "user.email=qualification@example.invalid", "tag", "-a",
             "specification_methodology/v3.0.3", "-m", "Synthetic qualification\n\nSTDO-Release-Profile: stable-v1"], cwd=repository)
    store = run / "store"

    def cli(*args):
        return json.loads(command([executable, "--store", str(store), *args]))

    manifest = cli("manifest", "v3.0.3", "--repository", str(repository))
    digest = manifest["manifest_sha256"]
    install = cli("install", "v3.0.3", "--repository", str(repository), "--manifest-sha256", digest)
    verification = cli("verify", "v3.0.3", "--manifest-sha256", digest)
    docs.require(verification["valid"], "fresh installed manifest verification failed")
    resolved = cli("resolve", "stdo://releases/v3.0.3/standards/documentation/index.html")
    viewer = cli("resolve", "stdo://releases/v3.0.3/standards/documentation/constraint-explorer/index.html")
    installed = store / "releases/v3.0.3"
    docs.check(installed)
    for relative in docs.MEMBERS:
        expected = (package / docs.DOC_ROOT / relative).read_bytes()
        actual = (installed / docs.DOC_ROOT / relative).read_bytes()
        docs.require(actual == expected, "installed documentation differs: " + relative)
    # The browser can now be exercised against this store without its acquiring repository.
    shutil.rmtree(repository)
    detached = cli("verify", "v3.0.3", "--manifest-sha256", digest)
    docs.require(detached["valid"], "installed verification depended on source repository")
    # Exercise the installed manager's integrity boundary, then restore the
    # exact selected bytes before browser qualification. This store is disposable.
    probe = installed / docs.DOC_ROOT / "index.html"
    original, mode = probe.read_bytes(), probe.stat().st_mode
    try:
        probe.chmod(0o644)
        probe.write_bytes(original + b"<!-- qualification corruption -->")
        process = subprocess.run([executable, "--store", str(store),
                                  "verify", "v3.0.3", "--manifest-sha256", digest],
                                 capture_output=True, text=True)
        tamper = json.loads(process.stdout)
        docs.require(process.returncode == 1 and not tamper["valid"],
                     "installed documentation tamper was not rejected")
    finally:
        probe.write_bytes(original)
        probe.chmod(mode)
    restored = cli("verify", "v3.0.3", "--manifest-sha256", digest)
    docs.require(restored["valid"], "restored installed documentation differs")
    report = {"kind": "stdo303.installed-documentation-qualification/1", "synthetic_local_tag": True,
              "manager": {"executable": executable, "version": manager_version},
              "public_release": False, "manifest_sha256": digest, "manifest": manifest["manifest"],
              "install": install, "entry": resolved, "viewer": viewer,
              "installed_root": str(installed), "source_repository_removed": True,
              "all_documentation_members_exact": True, "installed_verification": verification["valid"],
              "detached_verification": detached["valid"],
              "tamper_rejected": True, "tamper_verification": tamper,
              "restored_verification": restored["valid"],
              "viewer_sha256": hashlib.sha256(Path(viewer["path"]).read_bytes()).hexdigest()}
    (run / "qualification.json").write_bytes(docs.encoded(report))
    return {k: report[k] for k in ("installed_root", "entry", "all_documentation_members_exact", "detached_verification", "public_release")}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", type=Path, default=V3 / "build_tenants/common")
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--stdo", default="stdo", help="selected installed manager executable")
    args = parser.parse_args()
    try:
        print(json.dumps(qualify(args.package, args.run, args.stdo), indent=2))
    except (OSError, ValueError, RuntimeError) as exc:
        print(json.dumps({"status": "refused", "reason": str(exc)}), file=sys.stderr)
        raise SystemExit(2)

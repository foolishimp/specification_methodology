"""Reproduce and exercise the selected manager wheel without a source import."""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    repo = args.repository.resolve()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    freeze = Path(__file__).with_name("CANDIDATE.json")
    selected = json.loads(freeze.read_bytes())
    for item in selected["files"]:
        if digest(repo / item["path"]) != item["sha256"]:
            raise RuntimeError(f"Selected source changed: {item['path']}")
    scratch = Path(tempfile.mkdtemp(prefix="stdo302-manager-"))
    env = {
        key: value for key, value in os.environ.items()
        if key not in {"PYTHONPATH", "PYTHONHOME"} and not key.startswith("PIP_")
    }
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "PIP_DISABLE_PIP_VERSION_CHECK": "1"})
    epoch = subprocess.check_output(
        ["git", "show", "-s", "--format=%ct", selected["base_head"]], cwd=repo, text=True
    ).strip()
    env["SOURCE_DATE_EPOCH"] = epoch
    records = []

    def run(name: str, argv: list[str], *, cwd: Path = scratch) -> str:
        started = datetime.datetime.now(datetime.timezone.utc).isoformat()
        result = subprocess.run(argv, cwd=cwd, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        log = output / f"{name}.log"
        log.write_text(result.stdout)
        records.append({
            "name": name, "argv": argv, "cwd": str(cwd), "exit": result.returncode,
            "start": started, "end": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "log": log.name, "sha256": digest(log),
            "environment": {"PYTHONPATH": "unset", "PYTHONHOME": "unset", "SOURCE_DATE_EPOCH": epoch, "PYTHONDONTWRITEBYTECODE": "1"},
        })
        (output / "commands.json").write_text(json.dumps(records, indent=2) + "\n")
        if result.returncode:
            raise RuntimeError(f"{name} failed with exit {result.returncode}; see {log}")
        print(f"{name}: passed", flush=True)
        return result.stdout

    run("build-environment", [sys.executable, "-I", "-m", "venv", str(scratch / "build-venv")])
    builder = scratch / "build-venv/bin/python"
    run("build-dependencies", [str(builder), "-I", "-m", "pip", "install", "--index-url", "https://pypi.org/simple", "setuptools==80.9.0", "wheel==0.45.1"])
    run("build-environment-versions", [str(builder), "-I", "-m", "pip", "freeze", "--all"])
    wheels = []
    for index in (1, 2):
        source = scratch / f"source-{index}"
        source.mkdir()
        project = repo / "specification_methodology/v2"
        for name in ("pyproject.toml", "README.md", "LICENSE"):
            shutil.copyfile(project / name, source / name)
        package = source / "src/stdo_toolchain"
        package.mkdir(parents=True)
        for path in sorted((project / "src/stdo_toolchain").glob("*.py")):
            shutil.copyfile(path, package / path.name)
        dist = scratch / f"dist-{index}"
        run(f"wheel-build-{index}", [str(builder), "-I", "-m", "pip", "wheel", "--no-deps", "--no-build-isolation", "--wheel-dir", str(dist), str(source)])
        found = list(dist.glob("stdo_toolchain-0.1.6-py3-none-any.whl"))
        if len(found) != 1:
            raise RuntimeError("Unexpected manager wheel population")
        wheels.append(found[0])
    if wheels[0].read_bytes() != wheels[1].read_bytes():
        raise RuntimeError("The two clean-source wheel builds differ")
    published_wheel = output / wheels[0].name
    shutil.copyfile(wheels[0], published_wheel)
    checksum = output / f"{published_wheel.name}.sha256"
    checksum.write_text(f"{digest(published_wheel)}  {published_wheel.name}\n")
    run("runtime-environment", [sys.executable, "-I", "-m", "venv", str(scratch / "runtime-venv")])
    runtime = scratch / "runtime-venv/bin/python"
    run("wheel-install", [str(runtime), "-I", "-m", "pip", "install", "--index-url", "https://pypi.org/simple", str(published_wheel)])
    run("runtime-environment-versions", [str(runtime), "-I", "-m", "pip", "freeze", "--all"])
    code = """import importlib.metadata,json,pathlib,hashlib,stdo_toolchain
p=pathlib.Path(stdo_toolchain.__file__).resolve()
assert 'site-packages' in p.parts and p.is_relative_to(pathlib.Path(RUNTIME).parent.parent.resolve())
assert stdo_toolchain.__version__ == '0.1.6'
print(json.dumps({'path':str(p),'version':stdo_toolchain.__version__,'distribution_version':importlib.metadata.version('stdo-toolchain'),'module_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))
""".replace("RUNTIME", repr(str(runtime)))
    imported = json.loads(run("wheel-import", [str(runtime), "-I", "-B", "-c", code]))
    run("wheel-cli", [str(scratch / "runtime-venv/bin/stdo"), "--version"])
    legacy = """import json
from stdo_toolchain.git_source import GitSnapshot
from stdo_toolchain.manifest import build_manifest,manifest_sha256
with GitSnapshot(REPO,'v3.0.1-rc.1') as snapshot: m=build_manifest(snapshot)
d=manifest_sha256(m)
assert d=='60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8',d
assert 'profile' not in m['release']
print(json.dumps({'cut':m['release']['cut'],'tag_object':m['release']['tag_object'],'commit':m['release']['commit'],'manifest_sha256':d}))
""".replace("REPO", repr(str(repo)))
    run("legacy-301-manifest", [str(runtime), "-I", "-B", "-c", legacy])
    modules = ["test_toolchain", "test_git_source_layout", "test_v3_package", "test_cohort_update", "test_composition", "test_repository_dogfood", "test_stable_releases"]
    tests = "import sys,unittest;sys.path.insert(0," + repr(str(repo / "specification_methodology/v2/tests")) + ");unittest.main(module=None,argv=['wheel-tests','-v',*" + repr(modules) + "])"
    run("affected-suite", [str(runtime), "-I", "-B", "-c", tests])
    for item in selected["files"]:
        if digest(repo / item["path"]) != item["sha256"]:
            raise RuntimeError(f"Selected source changed during proof: {item['path']}")
    result = {
        "status": "two byte-identical wheel builds; isolated wheel acquisition/import and affected suite passed",
        "source_freeze": str(freeze.relative_to(repo)), "source_freeze_sha256": digest(freeze),
        "build_script_sha256": digest(Path(__file__)), "source_date_epoch": epoch,
        "wheel": {"path": str(published_wheel.relative_to(repo)), "sha256": digest(published_wheel), "bytes": published_wheel.stat().st_size},
        "checksum": str(checksum.relative_to(repo)), "reproduced": True,
        "runtime_python": str(runtime), "runtime_stdo": str(scratch / "runtime-venv/bin/stdo"),
        "import": imported, "environment": "PYTHONPATH/PYTHONHOME unset, python -I; only test directory explicitly added for suite",
        "scratch": str(scratch), "limits": "No global install, new302native tag, publication or consumer adoption. Runtime venv retained for exact native-tag/public reacquisition tests by Git Writer.",
    }
    (output / "PACKAGE.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

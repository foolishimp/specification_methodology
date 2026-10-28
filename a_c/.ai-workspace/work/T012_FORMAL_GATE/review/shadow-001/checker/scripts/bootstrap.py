#!/usr/bin/env python3
"""Install the pinned compiler privately and fetch only the imported Mathlib cache.

Uses no elan/global package manager. Network inputs are official pinned releases;
archive hashes are checked before extraction. Downloaded/compiler/cache files are
ignored tenant-local HOW. This is a bootstrap utility, not part of the proof.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def bootstrap() -> Path:
    lock = json.loads((ROOT / "toolchain-lock.json").read_text())
    platform_key = f"{platform.system()}-{platform.machine()}"
    archive = lock["lean"]["archives"].get(platform_key)
    if archive is None:
        raise SystemExit(f"Unsupported bootstrap platform: {platform_key}")
    local = ROOT / ".toolchain"
    local.mkdir(exist_ok=True)
    archive_path = local / archive["name"]
    prefix = local / archive["name"].removesuffix(".tar.zst")
    if not archive_path.exists():
        url = f"https://github.com/leanprover/lean4/releases/download/{lock['lean']['tag']}/{archive['name']}"
        partial = archive_path.with_suffix(archive_path.suffix + ".partial")
        subprocess.run(["curl", "--fail", "--location", "--show-error", "--output", str(partial), url], check=True)
        if hashlib.file_digest(partial.open("rb"), "sha256").hexdigest() != archive["sha256"]:
            raise SystemExit("Downloaded compiler archive digest mismatch")
        partial.replace(archive_path)
    if hashlib.file_digest(archive_path.open("rb"), "sha256").hexdigest() != archive["sha256"]:
        raise SystemExit("Cached compiler archive digest mismatch")
    if not (prefix / "bin/lean").exists():
        subprocess.run(["tar", "--zstd", "-xf", str(archive_path), "-C", str(local)], check=True)
    lean = prefix / "bin/lean"
    if subprocess.check_output([str(lean), "--githash"], text=True).strip() != lock["lean"]["commit"]:
        raise SystemExit("Private compiler commit does not match pin")
    env = os.environ | {
        "PATH": str(prefix / "bin") + os.pathsep + os.environ.get("PATH", ""),
        "MATHLIB_CACHE_DIR": str(ROOT / ".cache/mathlib"),
        "MATHLIB_NO_CACHE_ON_UPDATE": "1",
    }
    lake = str(prefix / "bin/lake")
    # Use the committed manifest. `lake update` is deliberately not invoked:
    # transitive inputRev values may move, but all manifest rev values are exact.
    subprocess.run([lake, "exe", "cache", "get", *lock["mathlib"]["cache_modules"]], cwd=ROOT, env=env, check=True)
    mathlib_revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT / ".lake/packages/mathlib", text=True).strip()
    if mathlib_revision != lock["mathlib"]["commit"]:
        raise SystemExit("Mathlib checkout does not match pin")
    print(f"Private toolchain ready: {prefix}")
    return prefix

if __name__ == "__main__":
    bootstrap()

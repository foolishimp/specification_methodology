"""Retain exact normal-import copies and focused commands inside this grant."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def main() -> int:
    proof = Path(__file__).resolve().parent
    checkout = proof.parents[4]
    scratch = Path((proof / "SCRATCH.txt").read_text().strip())
    phase = sys.argv[1]
    assert phase in ("baseline", "baseline-cancel", "candidate", "candidate-timing")
    source = checkout / "build_tenants" / "graphify"
    snapshot = scratch / phase / "build_tenants" / "graphify"
    snapshot.mkdir(parents=True)
    paths = [*sorted((source / "code").glob("*.py")),
             *sorted((source / "test_env").glob("*.py")),
             source / "design" / "fd-method-claude-rc9.json",
             source / "mypy.ini"]
    for folder in ("test_env/fixtures", "test_env/support_fixtures"):
        paths.extend(path for path in sorted((source / folder).rglob("*"))
                     if path.is_file() and "__pycache__" not in path.parts)
    manifest = []
    for path in paths:
        assert path.is_file() and not path.is_symlink()
        relative = path.relative_to(source)
        raw = path.read_bytes()
        target = snapshot / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
        assert target.read_bytes() == raw
        manifest.append({"source": str(path), "snapshot": str(target),
                         "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)})
    (proof / (phase + "-snapshot.json")).write_text(json.dumps(manifest, indent=2) + "\n")
    temp = scratch / (phase + "-tmp")
    temp.mkdir()
    env = dict(os.environ)
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": str(temp),
                "AC_SUPPORT_EFFECTS_PROOF_ROOT": str(proof / (phase + "-custody"))})
    tests = sys.argv[2:] or ["test_ac_support_effects"]
    command = [sys.executable, "-B", "-m", "unittest", "-v", *tests]
    started = time.time_ns()
    run = subprocess.run(command, cwd=snapshot / "test_env", env=env,
                         capture_output=True, timeout=180, check=False)
    (proof / (phase + "-stdout.txt")).write_bytes(run.stdout)
    (proof / (phase + "-stderr.txt")).write_bytes(run.stderr)
    record = {"phase": phase, "argv": command, "cwd": str(snapshot / "test_env"),
              "started_ns": started, "ended_ns": time.time_ns(), "returncode": run.returncode,
              "environment_overrides": {key: env[key] for key in ("PYTHONDONTWRITEBYTECODE", "TMPDIR", "AC_SUPPORT_EFFECTS_PROOF_ROOT")},
              "standing": "Actual public CLI and ordinary imports of exact candidate byte copies; no fake receipt in the public cases, no native F_P/provider calls, no acceptance or release claim.",
              "snapshot_manifest": phase + "-snapshot.json"}
    (proof / (phase + "-command.json")).write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"phase": phase, "returncode": run.returncode,
                      "seconds": (record["ended_ns"] - started) / 1e9,
                      "copied_files": len(manifest)}))
    print(run.stderr.decode("utf-8", errors="replace"))
    return run.returncode


if __name__ == "__main__":
    raise SystemExit(main())

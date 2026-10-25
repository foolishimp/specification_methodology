"""Finite integration evidence runner; no model calls or authority selection."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time

ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent
TENANT = ROOT / "a_c/build_tenants/graphify"
PYTHON = ROOT / "a_c/.venv/bin/python"
UPSTREAM = Path("/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-graphify-t008-upstream-w0b_fyxv/checkout")
TYPED = [
    "code/ac_support.py", "code/ac_support_core.py", "code/ac_support_effects.py",
    "test_env/test_ac_support_core.py", "test_env/test_ac_support_effects.py", "test_env/test_ac_support_interfaces.py",
    "examples/fd-support/prepare_readonly.py", "examples/fd-support/actor_cli.py", "test_env/support_fixtures/local_actor.py",
]


def save(path: Path, value: object) -> None:
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, sort_keys=True, indent=2)
        stream.write("\n")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sources() -> list[dict[str, object]]:
    return [{"path": str(path.relative_to(ROOT)), "sha256": digest(path), "bytes": path.stat().st_size}
            for path in sorted(TENANT.rglob("*"))
            if path.is_file() and not path.is_symlink() and "__pycache__" not in path.parts
            and path.suffix not in {".pyc", ".pyo"} and ".mypy_cache" not in path.parts]


def gate() -> dict[str, object]:
    # This carrier is retained only after Root supplies the exact closed peer.
    # It reports external Executive admission; this runner admits nothing.
    value = json.loads((HERE / "CLOSED_SUBJECT.json").read_bytes())
    if value.get("root_execution_go") is not True or value.get("source_basis") != "T008 integration003 closed code-review-repair001":
        raise ValueError("Final checks held until Root supplies exact closed successor cut and execution go")
    for row in json.loads((HERE / "SOURCE_BEFORE.json").read_bytes())["sources"]:
        if digest(ROOT / row["path"]) != row["sha256"]:
            raise ValueError("Frozen source/authority changed: " + row["path"])
    for relative, expected in value["required_sources"].items():
        if digest(ROOT / relative) != expected:
            raise ValueError("Frozen peer source changed: " + relative)
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("interfaces", "typing", "suite", "upstream"))
    parser.add_argument("--label", required=True)
    args = parser.parse_args()
    if not args.label.replace("-", "").isalnum():
        raise ValueError("Label must be a simple evidence directory component")
    bound = gate()
    target = HERE / args.label
    target.mkdir()
    before = sources()
    save(target / "sources-before.json", before)
    save(target / "closed-subject.json", bound)
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    selected = {
        "AC_GRAPHIFY_UPSTREAM": str(UPSTREAM),
        "AC_PUBLIC_INTERFACE_TEST_EVIDENCE": str(target / "public-fixtures"),
        "AC_ACTOR_TRANSPORT_TEST_EVIDENCE": str(target / "actor-fixtures"),
        "AC_SUPPORT_EFFECTS_PROOF_ROOT": str(target / "effects-fixtures"),
        "A_C_CORE_QUALIFICATION_CUSTODY": str(target / "core-qualification-fixtures"),
        "MYPYPATH": str(TENANT / "code") + os.pathsep + str(TENANT / "test_env"),
    }
    for name in ("public-fixtures", "actor-fixtures", "effects-fixtures", "core-qualification-fixtures"):
        (target / name).mkdir()
    env.update(selected)
    with tempfile.TemporaryDirectory(prefix="a-c-integrated-check-") as temporary:
        # Per-run cache/temp roots only; no HOME/CODEX_HOME or host settings edit.
        env["TMPDIR"] = temporary
        env["PYTHONPYCACHEPREFIX"] = str(Path(temporary) / "pycache")
        if args.stage == "interfaces":
            command = [str(PYTHON), "-m", "unittest", "-v", "a_c.build_tenants.graphify.test_env.test_ac_support_interfaces"]
        elif args.stage == "typing":
            command = [str(PYTHON), "-m", "mypy", "--strict", "--cache-dir", str(Path(temporary) / "mypy"),
                       *[str(TENANT / name) for name in TYPED]]
        elif args.stage == "suite":
            command = [str(PYTHON), "-m", "unittest", "discover", "-s", str(TENANT / "test_env"), "-v"]
        else:
            command = [str(PYTHON), str(TENANT / "test_env/check_upstream.py"), "--upstream", str(UPSTREAM),
                       "--out", str(target / "upstream-report.json")]
        start = time.time_ns()
        result = subprocess.run(command, cwd=ROOT, capture_output=True, env=env, timeout=300, check=False)
        end = time.time_ns()
        (target / "stdout").write_bytes(result.stdout)
        (target / "stderr").write_bytes(result.stderr)
        gate()
        after = sources()
        save(target / "sources-after.json", after)
        save(target / "command.json", {"command": command, "selected_environment": {**selected, "TMPDIR": temporary,
             "PYTHONDONTWRITEBYTECODE": "1", "PYTHONPYCACHEPREFIX": env["PYTHONPYCACHEPREFIX"]},
             "started_ns": start, "ended_ns": end, "returncode": result.returncode,
             "sources_unchanged": before == after, "actual_provider_calls": 0,
             "scope": "selected deterministic/local process/upstream mechanical checks; no F_P usability or acceptance"})
        print(json.dumps({"stage": args.stage, "label": args.label, "returncode": result.returncode,
                          "sources_unchanged": before == after, "stdout_tail": result.stdout.decode(errors="replace")[-1200:],
                          "stderr_tail": result.stderr.decode(errors="replace")[-4000:]}))
        return result.returncode if before == after else 3


if __name__ == "__main__":
    raise SystemExit(main())

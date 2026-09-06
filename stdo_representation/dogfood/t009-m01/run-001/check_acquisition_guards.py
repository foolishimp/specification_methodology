"""Replay the exact documented acquisition sequence and its identity refusals."""

from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import subprocess
import tempfile


EVIDENCE = Path(__file__).resolve().parent
PROJECT = EVIDENCE.parents[2]
SKILL = PROJECT / "skills/stdo-representation/SKILL.md"
TAG = "4750e09639c118f1097d4ea046fe23d26713f96b"
COMMIT = "a953ad4634fbfaefb8bdffaccdf4eff651a1e3a2"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stdo-store", required=True, type=Path)
    args = parser.parse_args()
    block = re.search(r"   ```bash\n(.*?)   ```", SKILL.read_text(), re.S)
    if block is None:
        raise RuntimeError("The documented Bash acquisition block is missing")
    script = "\n".join(
        line.removeprefix("   ") for line in block.group(1).splitlines()
    ) + "\n"
    if script != (EVIDENCE / "archive-command.sh").read_text():
        raise RuntimeError("The retained command differs from the current skill")
    cases = [
        ("exact-identity", script, True),
        ("wrong-tag-object", script.replace(TAG, "0" * 40), False),
        ("wrong-peeled-commit", script.replace(COMMIT, "0" * 40), False),
        (
            "missing-subtree",
            script.replace("${axiom_ref}:axiom_indexer", "${axiom_ref}:absent_subtree"),
            False,
        ),
    ]
    results = []
    for name, candidate, should_pass in cases:
        with tempfile.TemporaryDirectory(prefix="t009-guard-") as temporary:
            result = subprocess.run(
                ["bash", "-c", candidate],
                cwd=PROJECT,
                env={**os.environ, "TMPDIR": temporary},
                text=True,
                capture_output=True,
            )
            files = list(Path(temporary).rglob("ac.py"))
            row = {
                "case": name,
                "exit_code": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "ac_files": len(files),
                "script_sha256": hashlib.sha256(candidate.encode()).hexdigest(),
            }
            if (result.returncode == 0) != should_pass:
                raise RuntimeError(f"Wrong acquisition disposition: {row}")
            if not should_pass and files:
                raise RuntimeError(f"Refused acquisition exposed an executable: {row}")
            if should_pass:
                extracted = Path(result.stdout.strip())
                check = subprocess.run(
                    [
                        "python3", str(extracted / "scripts/check_constitution.py"),
                        "--stdo-store", str(args.stdo_store),
                    ],
                    cwd=extracted,
                    text=True,
                    capture_output=True,
                )
                row["checker_exit_code"] = check.returncode
                if check.returncode:
                    raise RuntimeError(check.stdout + check.stderr)
                row["checker"] = json.loads(check.stdout)
                if check.returncode or not row["checker"]["valid"]:
                    raise RuntimeError(f"Extracted dependency verification failed: {row}")
            results.append(row)
    report = {
        "skill_sha256": hashlib.sha256(SKILL.read_bytes()).hexdigest(),
        "predecessor_manifest_sha256": hashlib.sha256(
            (EVIDENCE / "candidate-files.json").read_bytes()
        ).hexdigest(),
        "cases": results,
    }
    (EVIDENCE / "guard-repair.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

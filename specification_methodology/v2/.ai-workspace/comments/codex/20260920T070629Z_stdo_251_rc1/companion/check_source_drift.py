"""Refuse an exact RC1 projection after one copied source observation changes."""
from pathlib import Path
import hashlib
import json
import shutil
import stat
import subprocess
import sys

OUT = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[6]
NEGATIVE = OUT / "negative-source-drift"
INSTALL = Path("/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.1")
TARGET = ROOT / "stdo_representation/build_tenants/axiom_indexer/representation/stdo-v2.5.1-rc.1"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    NEGATIVE.mkdir(exist_ok=True)
    if (NEGATIVE / "result.json").exists():
        raise ValueError("Preserve the completed negative result")
    copied = NEGATIVE / "subject/standards"
    if not copied.exists():
        shutil.copytree(INSTALL / "standards", copied, copy_function=shutil.copyfile)
    # copytree's default copy2 inherits immutable file modes. Only this local
    # discriminator copy is writable; never chmod or mutate the actual Install.
    changed = copied / "SPEC_METHOD.md"
    original = INSTALL / "standards/SPEC_METHOD.md"
    if sha(changed) != sha(original):
        raise ValueError("The pre-mutation copy differs from the exact Install")
    inputs = [TARGET / "axiomatic-program.json", TARGET / "logical-constraint-map.json", original]
    before = {str(p): sha(p) for p in inputs}
    changed.chmod(changed.stat().st_mode | stat.S_IWUSR)
    changed.write_bytes(changed.read_bytes() + b"\nSource-observation drift discriminator: this copied file is not the frozen basis.\n")
    bindings = NEGATIVE / "bindings.json"
    bindings.write_text(json.dumps({"kind": "axiom-indexer.binding-set", "schema_version": 1,
        "bindings": [{"uri_prefix": "stdo://releases/v2.5.1-rc.1/", "path": str(NEGATIVE / "subject")}]}, indent=2) + "\n")
    argv = [sys.executable, "-B", str(ROOT / "axiom_indexer/build_tenants/core/code/ac.py"),
            "project", "--program", str(inputs[0]), "--map", str(inputs[1]),
            "--bindings", str(bindings), "--frame-index",
            "urn:stdo-representation:frame-index:computational-whole-path-evaluation", "--mode", "materialized"]
    result = subprocess.run(argv, capture_output=True, text=True)
    (NEGATIVE / "stdout.txt").write_text(result.stdout)
    (NEGATIVE / "stderr.txt").write_text(result.stderr)
    report = json.loads(result.stdout)
    after = {str(p): sha(p) for p in inputs}
    record = {"kind": "stdo.rc1-exact-subject-source-drift-refusal", "argv": argv,
              "exit_code": result.returncode, "source_copy_original_sha256": before[str(original)],
              "source_copy_mutated_sha256": sha(changed), "report": report,
              "original_inputs_preserved": before == after, "input_hashes": after}
    (NEGATIVE / "result.json").write_text(json.dumps(record, indent=2) + "\n")
    if result.returncode == 0 or before != after:
        raise ValueError("Negative discriminator failed")
    print(json.dumps({"exit_code": result.returncode, "report": report, "original_inputs_preserved": before == after}))


if __name__ == "__main__":
    main()

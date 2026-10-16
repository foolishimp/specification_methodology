"""Replay a frozen upstream finite witness without changing its source or scope."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

COMMON = "4c340f7adec9f3c893e3e267b23e4cadeb357854"
BASE = "specification_methodology/v3/.ai-workspace/comments/codex/20261016T000430Z_I5_ASSURANCE_ASSETS/"
CODE_SHA = "242a5d4bf25e47a4565adb10aef6c2e5276b3ff1b40587a0da1aae2bc811f8eb"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    def read(name):
        return subprocess.check_output(["git", "show", COMMON + ":" + BASE + name], cwd=args.repo)
    code = read("check_examples.py")
    if hashlib.sha256(code).hexdigest() != CODE_SHA:
        raise SystemExit("wrong finite witness source")
    result = subprocess.run([sys.executable, "-I", "-B", "-c", code.decode()], capture_output=True, check=True)
    expected = read("results.json")
    if result.stdout != expected:
        raise SystemExit("finite witness replay differs from its pinned result")
    payload = {
        "common_input": COMMON,
        "witness_path": BASE + "check_examples.py",
        "witness_sha256": CODE_SHA,
        "result_sha256": hashlib.sha256(result.stdout).hexdigest(),
        "replay": "identical",
        "python": sys.version,
        "scope": "finite mathematical witnesses of the ratified common assurance relations",
        "limits": ["no universal proof", "no candidate-source fidelity judgment", "no tenant actual-use or context-fit claim"],
        "observations": json.loads(result.stdout),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"replay": "identical", "output": str(args.output)}))

if __name__ == "__main__":
    main()

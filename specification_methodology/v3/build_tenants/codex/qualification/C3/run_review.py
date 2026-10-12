"""Run an explicitly granted, tool-free independent Claude assessment.

Inputs are frozen Git bytes assembled by the separate Writer. Authentication is
the normal local CLI authentication; safe mode suppresses ambient customizations.
This helper records transport and provider counters, not assessment authority.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import time

parser = argparse.ArgumentParser()
parser.add_argument("directory", type=Path)
parser.add_argument("--subject", required=True)
parser.add_argument("--seconds", type=int, default=480)
parser.add_argument("--budget-usd", type=float, default=6)
args = parser.parse_args()
directory = args.directory.resolve()
comments_root = Path(__file__).resolve().parents[4] / ".ai-workspace/comments/codex"
if directory != comments_root and comments_root not in directory.parents:
    raise SystemExit("Reviewer output belongs under the Codex comments namespace.")
prompt = (directory / "PROMPT.txt").read_bytes()
subject = subprocess.check_output(["git", "rev-parse", args.subject], text=True).strip()
argv = ["claude", "-p", "--safe-mode", "--tools", "", "--permission-mode", "dontAsk",
        "--output-format", "json", "--no-session-persistence", "--model", "opus",
        "--effort", "medium", "--max-budget-usd", str(args.budget_usd)]
started = time.monotonic()
report = {"subject_commit": subject, "argv": argv, "prompt_bytes": len(prompt),
          "prompt_sha256": hashlib.sha256(prompt).hexdigest(),
          "context_allowance_bytes": 600000, "wall_allowance_seconds": args.seconds,
          "spend_allowance_usd": args.budget_usd, "role": "author-independent Reviewer"}
report["provider_cwd"] = "/private/tmp"
if len(prompt) > report["context_allowance_bytes"]:
    raise SystemExit("context envelope exceeded before dispatch")
try:
    result = subprocess.run(argv, input=prompt, capture_output=True,
                            timeout=args.seconds, cwd=report["provider_cwd"])
    (directory / "REVIEW.raw.json").write_bytes(result.stdout)
    (directory / "REVIEW.stderr.txt").write_bytes(result.stderr)
    report["exit_code"] = result.returncode
    try:
        data = json.loads(result.stdout)
        (directory / "REVIEW.md").write_text(data.get("result", "") + "\n")
        report.update({key: data[key] for key in ["is_error", "total_cost_usd", "usage",
                      "modelUsage", "session_id", "num_turns"] if key in data})
    except (ValueError, UnicodeDecodeError):
        report["transport_result"] = "unparseable"
except subprocess.TimeoutExpired as error:
    (directory / "REVIEW.raw.json").write_bytes(error.stdout or b"")
    (directory / "REVIEW.stderr.txt").write_bytes(error.stderr or b"")
    report["transport_result"] = "timeout"
report["elapsed_seconds"] = round(time.monotonic() - started, 3)
(directory / "MEASUREMENT.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({key: value for key, value in report.items()
                  if key not in {"argv", "usage", "modelUsage"}}))
raise SystemExit(report.get("exit_code", 1) if not report.get("is_error") else 1)

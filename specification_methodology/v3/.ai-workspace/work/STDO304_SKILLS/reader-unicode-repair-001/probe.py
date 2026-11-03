#!/usr/bin/env python3
"""Retain public-CLI Unicode discriminators using the existing isolated fixture."""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reader", type=Path, required=True)
    parser.add_argument("--tests", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location("fixture", args.tests)
    fixture_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fixture_module)
    cases = {
        "u2028_is_not_a_line_ending": "## One\nordinary\u2028## False\nnot a heading\n",
        "nbsp_does_not_close_fence": "## One\n```text\ncode\n```\u00a0\n## False\nstill code\n",
    }
    records = []
    for name, subject in cases.items():
        fixture = fixture_module.SourceReaderTests()
        fixture.setUp()
        try:
            fixture.subject(subject)
            command = [sys.executable, "-B", str(args.reader), "read", "--stdo",
                       str(fixture.manager), "--store", fixture.state["store"],
                       "--definition", str(fixture.definition), "--member",
                       "standards/OWNER.md", "--heading", "False"]
            result = subprocess.run(command, capture_output=True, text=True)
            records.append({"case": name, "subject": subject,
                            "subject_sha256": hashlib.sha256(subject.encode()).hexdigest(),
                            "command": command, "exit_code": result.returncode,
                            "stdout": result.stdout, "stderr": result.stderr,
                            "result": json.loads(result.stdout)})
        finally:
            fixture.doCleanups()
    args.output.write_text(json.dumps({
        "reader_sha256": hashlib.sha256(args.reader.read_bytes()).hexdigest(),
        "fixture_sha256": hashlib.sha256(args.tests.read_bytes()).hexdigest(),
        "standing": "isolated fixture interface; actual public reader subprocess; no native manager or actor claim",
        "records": records,
    }, indent=2, ensure_ascii=True) + "\n")
    print(json.dumps([{ "case": r["case"], "exit_code": r["exit_code"],
                       "status": r["result"].get("status"),
                       "reason": r["result"].get("reason") } for r in records]))


if __name__ == "__main__":
    main()

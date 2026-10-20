#!/usr/bin/env python3
"""Read exact lines from one digest-bound frozen common source member."""
import argparse
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
import bundle_check as checks


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        checks.require(checks.sha((root / "package-custody.json").read_bytes()) == checks.SOURCE_PINS["package-custody.json"],
                       "frozen package-custody record changed")
        path = checks.safe_path(args.path)
        rows = {row["path"]: row for row in checks.load(root / "package-custody.json")["members"]}
        checks.require(path in rows, "path is outside the complete frozen package")
        member = root / "source" / path
        checks.require(not member.is_symlink(), "redirected source member")
        data = member.read_bytes()
        checks.require(checks.sha(data) == rows[path]["sha256"], "source bytes changed")
        lines = data.decode("utf-8").splitlines(keepends=True)
        checks.require(1 <= args.start <= args.end <= len(lines), "line range is outside exact source")
        print(json.dumps({"subject": checks.SUBJECT, "path": path, "sha256": rows[path]["sha256"],
                          "start_line": args.start, "end_line": args.end,
                          "line_convention": "Python str.splitlines(keepends=True), matching the source-generation contract",
                          "text": "".join(lines[args.start - 1:args.end])}, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, KeyError, OSError) as exc:
        print(json.dumps({"status": "refusal", "reason": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

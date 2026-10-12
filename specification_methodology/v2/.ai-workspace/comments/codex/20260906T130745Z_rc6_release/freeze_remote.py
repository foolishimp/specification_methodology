"""Acquire exact prepublication ref expectations for the selected RC6 cohort."""
from pathlib import Path
import datetime
import importlib.util
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent
URL = "https://github.com/foolishimp/specification_methodology.git"
VERSION = "2.5.0-rc.6"
spec = importlib.util.spec_from_file_location("rc6_remote_checker", ROOT / "scripts/check_stack_release.py")
check = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = check
spec.loader.exec_module(check)
failures = []
check.validate_remote_endpoint(ROOT, "origin", URL, failures)
if failures:
    raise SystemExit("; ".join(failures))
argv = ["git", "ls-remote", URL]
result = subprocess.run(argv, cwd=ROOT, check=True, capture_output=True, text=True)
(OUT / "remote-before-publication.txt").write_text(result.stdout)
refs = dict(line.split("\t", 1)[::-1] for line in result.stdout.splitlines())
expected = {"refs/heads/main": refs.get("refs/heads/main")}
lines = {}
for name in ("specification_methodology", "axiom_indexer", "stdo_representation"):
    destinations = [f"refs/tags/{name}/v{VERSION}", f"refs/tags/{name}/v2.5.0",
                    f"refs/heads/rc/{name}/2.5.0", f"refs/heads/release/{name}/2.5.0"]
    expected.update({ref: refs.get(ref) for ref in destinations})
    rows = []
    for ref, oid in refs.items():
        ordinal = check.rc_ref_ordinal(ref, name, "2.5.0", include_unqualified=name == "specification_methodology")
        if ordinal is not None:
            rows.append({"ordinal": ordinal, "ref": ref, "tag_object": oid,
                         "peeled_commit": refs.get(ref + "^{}")})
    rows.sort(key=lambda row: (row["ordinal"], row["ref"]))
    if not rows or any(row["ordinal"] >= 6 or not row["peeled_commit"] for row in rows):
        failures.append(name + ": missing lower history, non-annotated cut, or non-advancing RC6")
    greatest = max((row["ordinal"] for row in rows), default=0)
    peels = {row["peeled_commit"] for row in rows if row["ordinal"] == greatest}
    selector = f"refs/tags/{name}/v2.5.0"
    if greatest != 5 or len(peels) != 1 or refs.get(selector + "^{}") not in peels:
        failures.append(name + ": selector does not identify exact greatest lower RC5")
    if expected[destinations[0]] is not None or any(expected[ref] is None for ref in destinations[1:]):
        failures.append(name + ": immutable target exists or mutable destination is absent")
    lines[name] = rows
if expected["refs/heads/main"] is None or len(expected) != 13:
    failures.append("incomplete exact 13-ref publication population")
record = {"kind": "stdo.rc6-remote-expectation-freeze",
          "observed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "argv": argv, "status": "satisfied" if not failures else "falsified",
          "repository_url": URL, "configured_fetch_urls": check.configured_remote_urls(ROOT, "origin", push=False),
          "configured_push_urls": check.configured_remote_urls(ROOT, "origin", push=True),
          "raw_sha256": check.sha256(result.stdout.encode()),
          "expected_remote": dict(sorted(expected.items())), "expected_version_lines": lines,
          "expected_version_lines_sha256": check.canonical_value_sha256({"repository_url": URL, "version_lines": lines}),
          "failures": failures}
(OUT / "remote-expectations.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"status": record["status"], "destinations": len(expected),
                  "version_lines_sha256": record["expected_version_lines_sha256"], "failures": failures}))
raise SystemExit(bool(failures))

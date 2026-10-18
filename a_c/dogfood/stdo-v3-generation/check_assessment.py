#!/usr/bin/env python3
"""Check coverage and cited coordinates in independent grades, not their truth."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

from prepare_assessment import canonical_sha, verify_source_loci

ROOT = Path(__file__).resolve().parent
VERDICTS = {"preserved", "partial", "missing", "contradicted"}


def load(path: Path):
    return json.loads(path.read_text())


def pointer(record, field: str):
    if not isinstance(field, str) or not field.startswith("/"):
        raise ValueError("evidence field must be a record-relative JSON pointer")
    value = record
    for part in field[1:].split("/"):
        if re.search(r"~(?![01])", part):
            raise ValueError("invalid JSON pointer escape")
        key = part.replace("~1", "/").replace("~0", "~")
        if isinstance(value, list):
            if not re.fullmatch(r"0|[1-9][0-9]*", key):
                raise ValueError("invalid JSON pointer array index")
            value = value[int(key)]
        else:
            value = value[key]
    return value


def check(candidate: str) -> dict:
    folder = ROOT / "grading" / candidate
    packet, grades = load(folder / "packet.json"), load(folder / "grades.json")
    freeze = load(ROOT / "private/assessment-freeze.json")
    errors, summaries = [], []

    def require(test, message):
        if not test:
            errors.append(message)

    for relative, expected_hash in freeze["files"].items():
        path = ROOT / relative
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected_hash, "assessment input/code changed: " + relative)
    require(packet["oracle_sha256"] == freeze["oracle_sha256"], "packet oracle pin differs")
    try:
        verified_loci = verify_source_loci(candidate, packet["probes"])
    except (OSError, ValueError, KeyError) as exc:
        errors.append("source-locus verification failed: " + str(exc))
        verified_loci = 0
    require(verified_loci == freeze["verified_source_loci"][candidate], "source-locus check count differs")
    require(grades.get("profile") == "ac.generation.fidelity-grades/1", "wrong grade profile")
    require(grades.get("candidate") == candidate, "candidate mismatch")
    require(grades.get("semantic_acceptance") == "not issued", "assessment cannot issue semantic acceptance")
    expected = {m["label"]: m for m in packet["models"]}
    supplied = grades.get("models", [])
    require(len(supplied) == len(expected) and {m.get("label") for m in supplied} == set(expected), "missing/duplicate/unknown model labels")
    probes = {p["id"]: p for p in packet["probes"]}
    for grade in supplied:
        label = grade.get("label")
        if label not in expected:
            continue
        subject = expected[label]
        raw = Path(subject["path"]).read_bytes()
        require(hashlib.sha256(raw).hexdigest() == subject["file_sha256"], label + ": model bytes changed")
        require(grade.get("model_sha256") == subject["model_sha256"], label + ": subject digest differs")
        model = json.loads(raw)
        require(canonical_sha(model) == subject["model_sha256"], label + ": canonical model digest differs")
        require(isinstance(grade.get("blinding_disclosures"), list) and all(isinstance(item, str) for item in grade["blinding_disclosures"]), label + ": disclosure list is required")
        records = {r["id"]: r for family in model["populations"].values() for r in family}
        items = grade.get("probes", [])
        require(len(items) == len(probes) and {p.get("id") for p in items} == set(probes), label + ": incomplete/duplicate probe coverage")
        counts, distortion_counts = Counter(), Counter()

        def evidence(items, locus_ids, where):
            require(isinstance(items, list), where + ": evidence must be a list")
            for item in items if isinstance(items, list) else []:
                record = records.get(item.get("record_id"))
                require(record is not None, where + ": cited record is absent")
                if record is not None:
                    try:
                        pointer(record, item.get("field"))
                    except (KeyError, ValueError, TypeError, IndexError) as exc:
                        errors.append(where + ": cited field does not resolve: " + str(exc))
                ids = item.get("source_locus_ids", [])
                require(isinstance(ids, list) and bool(ids) and set(ids) <= locus_ids, where + ": invalid/absent source loci")
                require(bool(item.get("reason")), where + ": evidence reason absent")

        for item in items:
            pid = item.get("id")
            if pid not in probes:
                continue
            probe = probes[pid]
            where = label + ":" + pid
            require(item.get("verdict") in VERDICTS, where + ": invalid probe verdict")
            require(bool(item.get("reason")), where + ": probe reason absent")
            distinctions = {d["id"]: d for d in probe["required_distinctions"]}
            criteria = item.get("criteria", [])
            require(len(criteria) == len(distinctions) and {c.get("id") for c in criteria} == set(distinctions), where + ": missing/duplicate distinction coverage")
            locus_ids = {l["id"] for l in probe["source_loci"]}
            for criterion in criteria:
                cid = criterion.get("id")
                status = criterion.get("verdict")
                counts[status] += 1
                require(status in VERDICTS, where + ": invalid distinction verdict")
                require(bool(criterion.get("reason")), where + ": distinction reason absent")
                if status in {"preserved", "partial", "contradicted"}:
                    require(bool(criterion.get("evidence")), where + ": supported verdict needs record evidence")
                evidence(criterion.get("evidence", []), locus_ids, where + ":" + str(cid))
            checks = item.get("prohibited_checks", [])
            distortions = probe["prohibited_distortions"]
            require(len(checks) == len(distortions) and {c.get("distortion") for c in checks} == set(distortions), where + ": incomplete/duplicate prohibited checks")
            for distortion in checks:
                status = distortion.get("status")
                distortion_counts[status] += 1
                require(status in {"asserted", "absent", "ambiguous"}, where + ": invalid prohibited-check status")
                require(bool(distortion.get("reason")), where + ": prohibited-check reason absent")
                if status == "asserted":
                    require(bool(distortion.get("evidence")), where + ": asserted distortion needs evidence")
                evidence(distortion.get("evidence", []), locus_ids, where + ":prohibited")
        summaries.append({"label": label, "model_sha256": subject["model_sha256"],
                          "criteria": dict(counts), "prohibited_checks": dict(distortion_counts),
                          "probe_verdicts": dict(Counter(p.get("verdict") for p in items)),
                          "blinding_disclosures": grade.get("blinding_disclosures", [])})
    return {"candidate": candidate, "errors": errors, "models": summaries,
            "grade_file_sha256": hashlib.sha256((folder / "grades.json").read_bytes()).hexdigest(),
            "packet_sha256": hashlib.sha256((folder / "packet.json").read_bytes()).hexdigest()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    results = [check(candidate) for candidate in ("codex", "claude")]
    result = {"profile": "ac.generation.assessment-coordinate-check/1", "results": results,
              "claim": "Complete declared grading coverage and resolving cited coordinates only; assessor judgments are not mechanically proven."}
    text = json.dumps(result, indent=2) + "\n"
    if args.out:
        args.out.open("x").write(text)
    else:
        print(text, end="")
    raise SystemExit(1 if any(r["errors"] for r in results) else 0)


if __name__ == "__main__":
    main()

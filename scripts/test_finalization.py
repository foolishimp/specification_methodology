#!/usr/bin/env python3
"""Fail-closed tests for STDO.gtl construction authorization."""

from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import finalize_stdo_gtl_product as finalizer


CANDIDATE = (
    finalizer.ROOT
    / "build_tenants"
    / "gtl"
    / "representation"
    / "candidates"
    / "stdo-2.4.3-rc.3"
)


def request() -> dict[str, object]:
    return json.loads((CANDIDATE / "acceptance-request.json").read_text())


def authorization(value: dict[str, object]) -> dict[str, object]:
    request_sha = (
        "sha256:" + hashlib.sha256(finalizer.canonical_bytes(value)).hexdigest()
    )
    return {
        "kind": "stdo-representation.f-h-construction-authorization",
        "schema_version": 1,
        "request_sha256": request_sha,
        "actor_identity": value["requested_actor_identity"],
        "authority_identity": value["requested_authority_identity"],
        "grant_identity": value["requested_grant_identity"],
        "grant_scope": value["requested_grant_scope"],
        "basis_refs": value["required_basis_refs"],
        "accepted_subjects": [
            {
                "subject_kind": row["subject_kind"],
                "subject_identity": row["subject_identity"],
                "subject_sha256": row["subject_sha256"],
            }
            for row in value["subjects"]
        ],
        "decision": "accepted",
        "decided_at": "2026-08-28T00:00:00+10:00",
        "evidence_refs": value["evidence_refs"],
    }


class FinalizationTests(unittest.TestCase):
    def test_frozen_request_shape_is_admitted(self) -> None:
        finalizer.validate_request(request())

    def test_duplicate_accepted_subject_is_rejected(self) -> None:
        value = request()
        decision = authorization(value)
        decision["accepted_subjects"].append(
            copy.deepcopy(decision["accepted_subjects"][0])
        )
        with self.assertRaisesRegex(
            finalizer.FinalizationFailure, "exactly three accepted subjects"
        ):
            finalizer.accepted_subjects(value, decision)

    def test_authorization_with_drifted_evidence_is_rejected_before_build(self) -> None:
        value = request()
        decision = authorization(value)
        decision["evidence_refs"] = ["unbound-review.md"]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            authorization_path = root / "authorization.json"
            authorization_path.write_bytes(finalizer.canonical_bytes(decision))
            completed = subprocess.run(
                [
                    sys.executable,
                    str(Path(finalizer.__file__)),
                    "--candidate-directory",
                    str(CANDIDATE),
                    "--authorization",
                    str(authorization_path),
                    "--output-directory",
                    str(root / "product"),
                ],
                cwd=finalizer.ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertNotEqual(0, completed.returncode)
        self.assertIn(
            "authorization bases and evidence do not equal the exact request",
            completed.stderr,
        )


if __name__ == "__main__":
    unittest.main()

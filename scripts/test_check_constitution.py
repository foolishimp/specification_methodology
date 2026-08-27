#!/usr/bin/env python3
"""Negative and optimization-mode tests for check_constitution.py."""

from __future__ import annotations

import ast
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import check_constitution as checker


class ConstitutionCheckerTests(unittest.TestCase):
    def test_checker_contains_no_assert_statement(self) -> None:
        tree = ast.parse(Path(checker.__file__).read_text(encoding="utf-8"))
        self.assertEqual(
            [], [node for node in ast.walk(tree) if isinstance(node, ast.Assert)]
        )

    def test_duplicate_json_object_name_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"kind":"one","kind":"two"}\n', encoding="utf-8")
            with self.assertRaisesRegex(
                checker.CheckFailure, "duplicate JSON object name"
            ):
                checker.load_json_unique(path)

    def test_duplicate_ticket_header_key_fails(self) -> None:
        text = "# Ticket\n\nid: T-900\nid: T-901\n\n## Body\n"
        with self.assertRaisesRegex(checker.CheckFailure, "duplicate ticket metadata"):
            checker.parse_ticket_metadata(text, "mutation")

    def test_body_metadata_like_text_cannot_override_header(self) -> None:
        text = "# Ticket\n\nid: T-900\nstatus: active\n\nstatus: completed\n"
        values = checker.parse_ticket_metadata(text, "bounded-header")
        self.assertEqual("active", values["status"])

    def test_missing_ticket_field_fails(self) -> None:
        values = {
            "id": "T-900",
            "title": "Mutation",
            "type": "bug",
            "ticket_category": "ordinary",
            "status": "active",
            "goal": "GOAL-001",
            "change_intent": "exercise refusal",
            "change_class": "intent_reprice",
            "re_entry_point": "Intent",
            "triaged_at": "2026-08-27T00:00:00+10:00",
            "created_at": "2026-08-27T00:00:00+10:00",
        }
        with self.assertRaisesRegex(checker.CheckFailure, "missing ticket metadata"):
            checker.validate_ticket_metadata(
                values, Path(".ai-workspace/tickets/active/T-900.md")
            )

    def test_wrong_ticket_lane_status_fails(self) -> None:
        values = {
            "id": "T-900",
            "title": "Mutation",
            "type": "bug",
            "ticket_category": "ordinary",
            "status": "completed",
            "goal": "GOAL-001",
            "change_intent": "exercise refusal",
            "change_class": "intent_reprice",
            "re_entry_point": "Intent",
            "triaged_at": "2026-08-27T00:00:00+10:00",
            "created_at": "2026-08-27T00:00:00+10:00",
            "updated_at": "2026-08-27T00:00:00+10:00",
        }
        with self.assertRaisesRegex(checker.CheckFailure, "status/lane mismatch"):
            checker.validate_ticket_metadata(
                values, Path(".ai-workspace/tickets/active/T-900.md")
            )

    def test_carrier_coordinate_digest_is_reproducible(self) -> None:
        digest = checker.sha256_bytes(
            checker.canonical_ascii_coordinate_bytes(checker.GTL_CARRIER_COORDINATE)
        )
        self.assertEqual(
            "b5becdf2801577f00bbc119a6bb23e0015a2007147818557ee2e770bc682b703",
            digest,
        )

    def test_checker_passes_with_python_optimization(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(Path(checker.__file__))],
            cwd=checker.ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        result = json.loads(completed.stdout)
        self.assertTrue(result["structural_checks_pass"])
        self.assertNotIn("valid", result)


if __name__ == "__main__":
    unittest.main()

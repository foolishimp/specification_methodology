from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TICKET_METHOD = ROOT / "specification/standards/TICKET_METHOD.md"


def decision_rows(markdown: str, heading: str) -> list[tuple[str, str, str]]:
    section = markdown.split(f"### {heading}\n", 1)[1]
    table_start = section.index("| Condition |")
    table = section[table_start:].split("\n\n", 1)[0]
    lines = [line for line in table.splitlines() if line.startswith("|")]
    if len(lines) < 3:
        raise AssertionError(f"missing decision table under {heading}")
    rows: list[tuple[str, str, str]] = []
    for line in lines[2:]:
        cells = tuple(cell.strip() for cell in line.strip("|").split("|"))
        if len(cells) != 3:
            raise AssertionError(f"invalid decision row: {line}")
        rows.append(cells)
    return rows


class TicketMethodCarrierSelectionTests(unittest.TestCase):
    def test_carrier_lifetime_totalizes_ticket_creation_decision(self) -> None:
        text = TICKET_METHOD.read_text(encoding="utf-8")
        rows = decision_rows(text, "Work-Carrier-To-Execution Rule")

        self.assertEqual(
            rows,
            [
                (
                    "no applicable upstream work authority exists",
                    "no execution contract is admitted",
                    "do not create a ticket as substitute authority; stop or re-enter",
                ),
                (
                    "applicable authority exists and an existing admitted ticket covers the exact work",
                    "derive the run-scoped contract from that ticket",
                    "reuse it; do not create another ticket",
                ),
                (
                    "applicable authority exists, no exact admitted ticket covers the work, and work or an open obligation needs independent state beyond the local carrier boundary",
                    "use one durable ticket plus the run-scoped contract",
                    "create or update the ticket only under ticket-state authority",
                ),
                (
                    "applicable authority exists, no exact admitted ticket covers the work, and work stays inside one admitted sprint with no state required after sprint close",
                    "use the sprint manifest plus one manifest-local iteration entry",
                    "do not create a durable ticket",
                ),
                (
                    "applicable authority exists, no exact admitted ticket or sprint covers the work, and work ends in the current run with no independent surviving state",
                    "use an intake-drafted run-scoped contract",
                    "do not create a durable ticket",
                ),
            ],
        )
        self.assertEqual(len(rows), len(set(rows)))
        normalized = " ".join(text.split())
        self.assertIn("select the first matching row", normalized)
        self.assertIn(
            "For work inside an admitted sprint, the local carrier boundary is that "
            "sprint; otherwise it is the current run",
            normalized,
        )

    def test_same_invocation_does_not_collapse_drafting_and_admission(self) -> None:
        text = TICKET_METHOD.read_text(encoding="utf-8")
        normalized = " ".join(text.split())

        self.assertIn(
            "may draft, validate, admit, and execute a contract in one invocation",
            normalized,
        )
        self.assertIn("Drafting and admission remain distinct relations", normalized)
        self.assertIn(
            "Execution begins only after deterministic admission or explicit human "
            "override of the exact contract",
            normalized,
        )
        self.assertIn(
            "Absence of a durable ticket neither requires nor authorizes creating one",
            normalized,
        )
        self.assertIn(
            "otherwise it is recorded as a durable ticket only under ticket-state "
            "authority",
            normalized,
        )
        self.assertIn(
            "The admitted result identifies the Product-bound admission mechanism "
            "and authority, exact contract identity or digest, decision, and evidence",
            normalized,
        )
        self.assertIn(
            "prose asserting `admitted` is not admission evidence", normalized
        )
        self.assertIn(
            "The admitted contract also names one Product-bound durable result/evidence "
            "surface",
            normalized,
        )
        self.assertIn("A conversation return alone is not durable evidence", normalized)
        self.assertIn(
            "If no such surface is authorized and available, contract admission refuses",
            normalized,
        )
        self.assertIn(
            "retain the obligation in the contract's named durable result/evidence "
            "surface or an already-authorized enclosing carrier",
            normalized,
        )
        self.assertIn("mark closure withheld on ticket-state authority", normalized)


if __name__ == "__main__":
    unittest.main()

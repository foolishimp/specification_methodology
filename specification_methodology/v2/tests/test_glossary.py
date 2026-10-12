from __future__ import annotations

import re
import unittest
from pathlib import Path


STANDARDS = Path(__file__).resolve().parents[1] / "specification/standards"


def heading_slug(line: str) -> str:
    heading = line.lstrip("#").strip().lower()
    heading = re.sub(r"[^a-z0-9 _-]", "", heading)
    return re.sub(r"[ _]+", "-", heading).strip("-")


class GlossaryIndexTests(unittest.TestCase):
    def test_every_index_link_resolves_to_an_owning_heading(self) -> None:
        glossary = (STANDARDS / "GLOSSARY_GUIDE.md").read_text(encoding="utf-8")
        links = re.findall(r"\]\(([^)#]+\.md)#([^)]+)\)", glossary)
        self.assertGreater(len(links), 0)
        for relative, anchor in links:
            owner = STANDARDS / relative
            self.assertTrue(owner.is_file(), relative)
            headings = {
                heading_slug(line)
                for line in owner.read_text(encoding="utf-8").splitlines()
                if line.startswith("#")
            }
            self.assertIn(anchor, headings, f"{relative}#{anchor}")


if __name__ == "__main__":
    unittest.main()

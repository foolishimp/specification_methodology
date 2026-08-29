from __future__ import annotations

import hashlib
import re
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[1]
COMPRESSIONS = REPOSITORY / "specification/standards/authority_compressions"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def frontmatter(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise AssertionError(f"missing frontmatter: {path}")
    return text.split("---\n", 2)[1]


def scalar(metadata: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}: (.+)$", metadata, re.MULTILINE)
    if match is None:
        raise AssertionError(f"missing {key}")
    return match.group(1)


def list_values(metadata: str, key: str) -> list[str]:
    match = re.search(
        rf"^{re.escape(key)}:\n((?:  - .+\n)+)",
        metadata,
        re.MULTILINE,
    )
    if match is None:
        return []
    return [line.removeprefix("  - ") for line in match.group(1).splitlines()]


def digest_map(metadata: str, key: str) -> dict[str, str]:
    match = re.search(
        rf"^{re.escape(key)}:\n((?:  .+: [0-9a-f]{{64}}\n)+)",
        metadata,
        re.MULTILINE,
    )
    if match is None:
        return {}
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        name, digest = line.strip().rsplit(": ", 1)
        values[name] = digest
    return values


class CompressionDigestTests(unittest.TestCase):
    def test_source_specific_compressions_match_their_sources(self) -> None:
        for name in (
            "axiomatic_calculus.compressed.md",
            "design_module_method.compressed.md",
            "odd_method.compressed.md",
            "spec_method.compressed.md",
            "ticket_method.compressed.md",
            "ux_method.compressed.md",
        ):
            compression = COMPRESSIONS / name
            metadata = frontmatter(compression)
            source = (COMPRESSIONS / scalar(metadata, "source_ref")).resolve()
            self.assertEqual(
                scalar(metadata, "source_digest"),
                sha256(source),
                name,
            )

    def test_multi_source_compressions_match_every_declared_edge(self) -> None:
        for name in ("stdo_bootstrap.md", "stdo_compressed.md"):
            compression = COMPRESSIONS / name
            metadata = frontmatter(compression)
            references = list_values(metadata, "source_refs")
            digests = digest_map(metadata, "source_digests")
            self.assertTrue(references, name)
            for reference in references:
                source = (COMPRESSIONS / reference).resolve()
                key = reference.removeprefix("../")
                if "/" not in key:
                    key = Path(key).name
                self.assertIn(key, digests, f"{name}: {reference}")
                self.assertEqual(digests[key], sha256(source), f"{name}: {reference}")

            index_references = list_values(metadata, "index_refs")
            index_digests = digest_map(metadata, "index_digests")
            for reference in index_references:
                source = (COMPRESSIONS / reference).resolve()
                key = Path(reference).name
                self.assertIn(key, index_digests, f"{name}: {reference}")
                self.assertEqual(
                    index_digests[key],
                    sha256(source),
                    f"{name}: {reference}",
                )


if __name__ == "__main__":
    unittest.main()

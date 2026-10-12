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
            "traversal_occurrence_profile.compressed.md",
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

    def test_axiomatic_compressions_preserve_deciding_algebra(self) -> None:
        texts = {
            name: (COMPRESSIONS / name).read_text(encoding="utf-8")
            for name in (
                "axiomatic_calculus.compressed.md",
                "stdo_compressed.md",
            )
        }
        required = (
            "M_b = (b, I, O, E, C, L, X, V, T, J)",
            "RefDomain_Sigma(record_kind, field)",
            "required_basis_relation",
            "Resolution_M",
            "external_preserved",
            "external_removed",
            "external_introduced",
            "N_t intersect Local_b = empty",
            "ER_t intersect E_b_prime = empty",
            "external_resolution_witnesses",
            "ExternalResolutionPreservationWitness",
            "decision: equal",
            "cross-basis",
            "composite-basis",
            "signature-extension",
            "AxiomaticCalculusBasis",
            "sha256(JCS(AxiomaticCalculusBasis))",
            "stdo.axiomatic-calculus-basis",
            "RFC 8785",
            "duplicate object names",
            "principle_refs",
            "unsigned-UTF-16",
            "heading fragment",
            "member_sha256",
            "probabilistic interpretation",
            "construction, or",
            "proposal without acceptance authority",
        )
        record_kinds = (
            "semantic-object",
            "typed-relation",
            "constraint",
            "latitude",
            "residual",
            "traversal",
            "transformation",
            "judgment",
        )
        for name, text in texts.items():
            for claim in required:
                self.assertIn(claim, text, f"{name}: {claim}")
            for record_kind in record_kinds:
                identity = (
                    "urn:stdo:concept:axiomatic-calculus:record-kind:" f"{record_kind}"
                )
                self.assertIn(identity, text, f"{name}: {identity}")

    def test_occurrence_compressions_preserve_deciding_algebra(self) -> None:
        texts = {
            name: (COMPRESSIONS / name).read_text(encoding="utf-8")
            for name in (
                "traversal_occurrence_profile.compressed.md",
                "stdo_compressed.md",
            )
        }
        for name, text in texts.items():
            for claim in (
                "RefDomain_Sigma_occurrence",
                "nine-field",
                "EventKind_occurrence",
                "admits_claim",
                "materializes_relation",
                "frontier_contains",
                "OperationKind",
                "instance contract",
            ):
                self.assertIn(claim, text, f"{name}: {claim}")

    def test_ticket_compressions_preserve_proportional_carrier_selection(self) -> None:
        texts = {
            name: (COMPRESSIONS / name).read_text(encoding="utf-8")
            for name in (
                "ticket_method.compressed.md",
                "stdo_compressed.md",
            )
        }
        required = (
            "run-scoped execution contract",
            "manifest-local",
            "intake draft",
            "Absence of a durable ticket neither requires nor authorizes creating one",
            "one invocation",
            "Drafting and admission remain distinct",
            "ticket-state authority",
            "Product-bound mechanism",
            "exact contract identity or digest",
            "Product-bound durable result/evidence surface",
            "conversation return alone",
            "already-authorized enclosing carrier",
            "withhold closure",
        )
        for name, text in texts.items():
            normalized = " ".join(text.split())
            for claim in required:
                self.assertIn(claim, normalized, f"{name}: {claim}")
        self.assertNotIn(
            "when Product policy requires one",
            texts["ticket_method.compressed.md"],
        )


if __name__ == "__main__":
    unittest.main()

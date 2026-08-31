from __future__ import annotations

import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[1]
STANDARDS = REPOSITORY / "specification/standards"


class SharedSourceReleaseLawTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.method = (STANDARDS / "RELEASE_METHOD.md").read_text(encoding="utf-8")
        cls.compression = (
            STANDARDS / "authority_compressions/stdo_compressed.md"
        ).read_text(encoding="utf-8")

    def test_shared_source_ref_grammar_is_project_qualified(self) -> None:
        for ref in (
            "refs/heads/rc/<project>/<version>",
            "refs/tags/<project>/v<version>-rc.<n>",
            "refs/tags/<project>/v<version>",
            "refs/heads/release/<project>/<version>",
        ):
            self.assertIn(ref, self.method)

        self.assertIn(
            "must not publish a future cut or\nselector under the unqualified",
            self.method,
        )
        for namespace in (
            "`specification_methodology`",
            "`axiom_indexer`",
            "`stdo_representation`",
        ):
            self.assertIn(namespace, self.method)

    def test_exact_cut_binds_project_subtree_and_repository_carrier(self) -> None:
        for coordinate in (
            "Project Release Namespace",
            "exact qualified Git ref",
            "annotated tag object",
            "peeled commit and repository-root tree",
            "Project Subtree root",
            "Project Subtree tree",
            "Product member inventory",
            "release-scoped claim bytes",
        ):
            self.assertIn(coordinate, self.method)

        self.assertIn(
            "does not make sibling subtrees Product members",
            self.method,
        )
        self.assertIn(
            "no leading or trailing slash and no empty, `.`, or\n`..` component",
            self.method,
        )
        self.assertIn("`.` alone denotes the repository root", self.method)

    def test_historical_refs_and_public_logical_uris_are_conserved(self) -> None:
        for claim in (
            "Project qualification is prospective",
            "Existing unqualified refs retain their\nnames, objects, peels, and public links",
            "not recreated,\nre-annotated, moved, or replaced",
            "stdo://releases/v<version>-rc.<n>/",
            "is not inserted into that URI",
            "historical unqualified selector is preserved at its existing object",
        ):
            self.assertIn(claim, self.method)

    def test_owned_compression_preserves_deciding_release_constraints(self) -> None:
        for claim in (
            "refs/tags/<project>/v<version>-rc.<n>",
            "refs/tags/<project>/v<version>",
            "Project Subtree root and tree",
            "sibling subtrees Product members",
            "Existing unqualified refs, tag objects",
            "stdo://releases/v<version>-rc.<n>/",
            "never gains the Git project prefix",
        ):
            self.assertIn(claim, self.compression)


if __name__ == "__main__":
    unittest.main()

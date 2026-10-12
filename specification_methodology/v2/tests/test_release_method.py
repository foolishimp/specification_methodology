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

    def test_release_matched_cohort_is_complete_and_same_versioned(self) -> None:
        for claim in (
            "Release-Matched Asset Cohort",
            "one exact cohort version suffix",
            "embedded asset-version fields render the same suffix",
            "the exact STDO standards corpus cut",
            "distributed `spec` plugin",
            "exact Axiom Indexer mechanics Product",
            "exact STDO Representation Product",
            "released `a_c.STDO` axiomatic program and logical constraint map",
            "complete source-STDO member inventory",
            "missing, stale, differently\nversioned",
        ):
            self.assertIn(claim, self.method)

    def test_coordinated_publication_uses_two_commits_and_one_atomic_push(self) -> None:
        for claim in (
            "commit A freezes the exact STDO corpus",
            "created locally over commit A but is not\n   pushed",
            "derived and frozen in commit B",
            "evaluates commit B against the exact local\n   STDO tag",
            "mandatory post-tag, pre-push gate",
            "local-ref-graph\nqualification",
            "expected remote object ID or required absence",
            "Every immutable cut tag is\ncreate-only",
            "explicit per-ref\ncompare-and-swap lease",
            "refetches and\nrepeats complete content and local-ref-graph qualification",
            "never falls back to an unguarded force",
            "one transport transaction atomically publishes",
            "no sequential-push fallback",
            "Post-publication bookkeeping",
            "cannot move any\nimmutable cohort tag",
            "cannot\nretroactively make an earlier cut a coordinated cohort",
        ):
            self.assertIn(claim, self.method)

    def test_cohort_compression_preserves_deciding_constraints(self) -> None:
        for claim in (
            "release-matched asset cohort",
            "Axiom\n  Indexer mechanics",
            "source-member/digest closure",
            "commit A",
            "commit B",
            "atomically publish",
            "partial remote cohort refuse",
            "expected remote OID or required absence",
            "immutable tags are create-only",
            "per-ref compare-and-swap lease",
            "refetch and complete requalification",
            "separately authorized recovery law",
            "same normalized version suffix",
            "govern a cut older than the higher RC",
        ):
            self.assertIn(claim, self.compression)


if __name__ == "__main__":
    unittest.main()

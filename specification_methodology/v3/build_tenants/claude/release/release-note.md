# STDO 3.0.0 RC1, Claude line candidate

Release note of the Claude line's release-candidate cut of the STDO
Specification Methodology, version line 3.0.0, candidate 1, prepared at
the product owner's instruction "run to RC1". This note is reconciled to
the exact subject it ships with: the freeze commit on
`tenant/claude/c3-synthesis` (commit A of RELEASE §7's two-commit
construction) that holds this file, the standards, the plugin, the
interpretation and the qualification records. The cut is not published:
no annotated tag exists, no selector has advanced, and the manifest that
binds the tag object follows in commit B. Publication, the tag and the
selector are the product owner's and the common pen's acts (RELEASE §3,
§7). Nothing in this note is accepted; acceptance standing comes from the
common tickets (RELEASE §8).

## Identity and refs

- Version line `3.0.0`, candidate `rc.1`; intended tag
  `specification_methodology/v3.0.0-rc.1` over commit A, with the
  `specification_methodology/v3.0.0` selector, both to be created by the pen.
- Project subtree root `specification_methodology/v3/build_tenants/claude`;
  the standards root `standards/`, the plugin `plugins/spec`, the
  interpretation `a_c/i3`, the qualification `qualification/`.
- Common input: C3-I5-06 at `4c340f7`; preceding candidate `c66ed4e`;
  donors the Codex iteration 4 candidate (`9a93c5a`, `903f119`) and the
  named techniques of the Codex iteration 5 candidate (`28d87ee`, `1e4bed6`).
- Builder: STDO 2.5.1-rc.2, manifest
  `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.

## Change and qualification

The successor restates the 23 members of rc.2 as 26 members under one
foundation (FOUNDATIONS, with its commitments and family index) and one
activation law (ACTIVATION), with the construction relation and the six
assurance relations owned at tier 1 and consumed by every family table;
twelve task frames bind those relations by owner section and digest; the
formal interpretation covers 24 sections in part with 155 clauses and five
kinds of support. The qualification records are the iteration ledger
(`qualification/C3-SYNTHESIS/LEDGER.md`), the iteration returns
(`qualification/C3-ITER3`, `-ITER4`, `-ITER5`) and the results table
(`qualification/C3-ITER5/RESULTS.md`). Standing at this cut: every member
acceptance criterion is `unresolved`; the evidence held is same-family
working evidence (fresh-context readbacks of the owner texts, 140
conservation rows read, 8 deciding paths traced, two finite oracles, the
interpretation reproduced from a clean archive with adverse controls) and
the evidence missing is listed per criterion in the results table. The
reviews still owed, bundled into one pass after this cut at the owner's
instruction, may lead to a candidate 2 on the same version line.

## Standards inventory

The 26 members under `standards/` with their SHA-256 digests are listed in
`release/manifest.json` (commit B), with the member-set digest; the
twelve frames under `standards/frames/` and the schemas and templates
are auxiliary members of the same tree.

## Plugin inventory

`plugins/spec`, 17 files, version label `3.0.0-rc.1` in both plugin
manifests, digests in `release/manifest.json`.

## Manager inventory

No toolchain manager is cut with this candidate; the installed-release
manager of the builder (STDO 2.5.1-rc.2) applies. The Axiom Indexer that
checks the interpretation is pinned at `axiom_indexer/v2.5.1-rc.2`
(`a_c/i3/README.md`, Evidence boundary); the cohort rule of RELEASE §7
applies when the owner cuts the cohort.

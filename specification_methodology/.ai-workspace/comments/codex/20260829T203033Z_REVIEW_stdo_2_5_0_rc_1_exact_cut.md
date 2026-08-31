# REVIEW: STDO 2.5.0 RC1 Exact Cut

- recorded_at: 2026-08-29T20:30:33Z
- reviewer: stdo_subject_basis (Beauvoir the 4th)
- review_mode: independent_read_only_exact_cut
- disposition: GO
- findings: P0=0, P1=0, P2=0

## Exact Subject

- immutable tag: `v2.5.0-rc.1`
- tag object: `42f59b6cd24071d9c445a29ae2a691cf0828211e`
- peeled commit: `ca6694314c4e9a56d3facae3eef06fe2792104c9`
- repository tree: `f0fac91f195b1f1506423060556bd36b3256d835`
- standards tree: `48a3e52b0aaf24b6d1d38ff551349e19b9b3c208`
- installed-manifest SHA-256:
  `3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338`
- standards members: 51
- standards aggregate:
  `87dca989f2200e91406524b6b2a3e85b230bf201581425614b57a7e0469be1e5`
- release-note SHA-256:
  `2ffbcd05eca14a8909d3fa5b11f61b58461a8572d7ced79d71bb059c1c4b9ee3`

## Replayed Evidence

- remote tag, selector, RC branch, and release branch peel to the exact commit;
- remote manifest construction, fresh install, and installed-cut verification pass;
- full isolated-checkout suite: 71/71 pass;
- focused calculus, frame, occurrence, and compression suite: 31/31 pass;
- Ruff, Black, commit hygiene, inventory, member hashes, and aggregate pass; and
- the isolated review checkout remains clean.

## Authority Disposition

This review qualifies one published immutable candidate. It does not accept the
RC as a Product, move the immutable tag, or authorize consumer adoption.

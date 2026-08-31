# STDO 2.0 Proportional Exact Candidate

## Subject

- candidate commit: `11ba8943831afb938a536f473727d82e300f3d2a`
- candidate tree: `e5822f2b52677aaa9abc2a5451a038d4e85378e1`
- predecessor: `v1.8.0` at
  `9cf2741917ca2d496cd78f5736ea2218d5eb0897`
- branch: `recovery/stdo-2.0-incremental-from-v1.8`
- remote branch matched the candidate when this checkpoint was written
- tag: no `v2.0.0` tag exists

This checkpoint is commentary. It does not amend or accept the candidate.

## Repaired Findings

1. `ODD_METHOD.md` now makes the selected immutable release consumer authority;
   mutable source authors only a future cut.
2. Design sequencing is proportional. Design, implementation, and tests may
   co-evolve when Product and requirements disambiguate the architecture. A
   prior design gate applies only to an unresolved durable material decision.
   Ontology, IACS, and three-view evidence still gate promotion and closure.
3. STDO 2.0 itself requires direct human acceptance. Its new proxy law cannot
   bootstrap the release that creates it.
4. The auxiliary Claude Code plugin version is `2.0.0`; it remains outside the
   normative standards inventory.
5. The member-set digest algorithm now states exact path ordering and no second
   digest sort.
6. `STDO-UP-014` now judges proportionality by semantic ambiguity removed
   against effective reasoning complexity introduced. It does not use raw line
   or artifact count as the governing measure.

## Reproducible Evidence

- standards members: `41`
- member-set digest:
  `1a9459a580fcc1af38147d9c86d4da6f905f2a894616970b81eff0fab86410e1`
- top-level normative lines: `9,469`
- `v1.8.0` top-level normative lines: `8,619`
- increment: `850` lines, `9.86%`
- every `v1.8.0` standards path remains present
- `STDO-SURFACE-001` and `STDO-UP-001` through `STDO-UP-015` each have one
  owning occurrence in the top-level standards
- source digests match the design, ODD, and specification compressions and the
  aggregate compression
- release inventory rows match every standards member and file digest
- `git diff --check` passes
- `claude plugin validate .` passes with only the pre-existing missing
  marketplace-description warning
- no executable STDO conformance or workflow implementation was added

## Pending Gate

The exact candidate requires independent complete-tree and `v1.8.0`-delta
review, followed by direct human acceptance of the same bytes. Do not tag from
this checkpoint alone.

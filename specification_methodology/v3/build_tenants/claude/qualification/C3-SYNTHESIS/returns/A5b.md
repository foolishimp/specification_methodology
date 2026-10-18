# Return, activation A5b

result: `candidate_ready` for "a candidate is available"; no fitness or
acceptance claimed. Author: Claude, A5b Writer. No state-changing git
command run.

Bytes: `standards/FOUNDATIONS.md` 56,022 → 76,006 (SHA-256
`6bd385df…d9e96664`); `deltas/A5b.md` 8,848. Links resolve (script).

Changes:

- Header F:3–12.
- §3 F:296–317: standing table; distinctions moved from paragraphs. P0
  sources F:321–327; P4a non-entailment case F:373–381.
- F:418–514 `### Foundation to law`: format, standing of consequences,
  index (F2 adds SPEC_METHOD §8 per the Executive note), reasons.
- F:548–598 Formal fragment (D8); H1 unresolved.
- m8 F:624, :672, :682.
- F3 F:751–788, incl. §2 import grounds.
- §6 F:894, :901, :916, :918–922.

Delta: rows 82, 327; 8 span rows; full map.

Ported: Codex FOUNDATIONS 48–51, 58; TRANSFORMATION_LIBRARY 95–98, 100,
108–112; two sentences verbatim, rest adapted (appendix).

Outside territory:

- A8, B4, B7: the index assigns FOUNDATIONS §2 Frame objects, Authority
  kinds, Disjointness, Frame tuple to F1; Imports to F12; Product lineage
  to F15. Their tables need rows; Executive may rule otherwise.
- B8: `AXIOMATIC_CALCULUS.md:807–812` refers to Formal fragment.
- B5: `DESIGN_MODULE.md:2264`.
- A7: GLOSSARY rows (material family, family table, instance premise,
  added choice, evidence class, adopting Product).
- Open: P2/P3 cases argue against capacity; P5's "therefore" relies on
  its table row; H1 links to `../design/`.

## Appendix: ported text record

Source: `git -C /Users/jim/src/apps/specification_methodology show
31f28f9:specification_methodology/v3/build_tenants/codex/successor/standards/<file>`.
Owning section: `FOUNDATIONS.md#3-commitments` (port 2) and
`FOUNDATIONS.md#foundation-to-law` (port 1). Cone: FOUNDATIONS
(CROSS_SYNTHESIS, "Frontier cone of each part"). Disposition supported:
new law with no predecessor row (acceptance criterion 6), supporting
relation 1; each part states its purpose where it stands. Sentences are
compared with line breaks joined by single spaces. No link to `build_tenants/codex/` remains (PT-7). No
Codex result value enters (PT-6).

Port 2, Codex `FOUNDATIONS.md`, to the §3 opening (F:298–306):

- 48–49, adapted. Source: "The premises below are adopted commitments
  for the selected methodology domain, not theorems derived from finite
  capacity alone." Target: "The adopted premises, which §1 identifies as
  the recovered and independent commitments, are commitments adopted for
  the domain this method governs, not theorems derived from finite
  capacity alone, that is, from the bound on an actor's envelope (P0)."
  Changes: the scope is set to §1's adopted premises, because P4b and P5
  are derived; "finite capacity" is defined.
- 49–50, verbatim with an addition: "Particular method rules need these
  premises plus their stated domain and policy choices". Added: ", each
  with its owner ([Foundation to law](#foundation-to-law))."
- 50–51, adapted. Source: "A conditional argument preserves that
  distinction; it does not manufacture authority." Target: "An argument
  from the premises preserves that distinction; it does not create
  authority (P6)." The source of the argument is named.
- 58, the table header, adapted. Source columns: "Commitment | Premise
  and standing | Distinction retained". Target columns: "Commitment |
  Standing | Distinction retained". Standing uses §1's terms only. The
  rows (Codex F1–F6) are not taken; every cell is this line's own text,
  moved from its paragraph.
- Not taken: 55–56 (Codex's owner sentence) and 60–65 (Codex's rows).

Port 1, Codex `TRANSFORMATION_LIBRARY.md`, to Foundation to law
(F:418–459):

- 95–98, adapted as a concept only: "instance premises", now defined as
  "the conditions of the situations the family governs, which the
  commitments do not supply". No sentence is taken.
- 100, the header, adapted from three columns to four. Source:
  "Premises | Conditional consequence | Particular contract and
  independent choice". Target: "Premises, with standing | Consequence
  that follows | Rule in this member that states it | Added domain or
  policy choice, and its owner" (CROSS_SYNTHESIS Part 1).
- 108–109, adapted. Source: "The consequences are arguments about the
  stated premises, not proofs of every source clause." Target: "… arguments
  from the stated premises, not proofs of every clause of the rules they
  name." "from" is the design's wording; "source clause" is made precise.
- 109–111, adapted. Source: "Concrete work-carrier layout, number of
  actors, numeric budgets, optional Baseline adoption, release procedure
  and all domain result enums are independent choices." Target: "Concrete
  carrier layouts, the number of actors, numeric limits, adoption of an
  optional profile, release procedures and the values of each refinement
  are added choices." Changes:
  - "Baseline" is a profile term, so it stays out of tier 1;
  - "independent" is a standing term in §1, so it becomes "added";
  - "enums" becomes this line's "refinement".
- 111, verbatim: "They are not inferred from the foundational
  commitments."
- 112, adapted. Source: "This chain leaves those choices at their owners
  and adds no mandatory ledger." Target: "Each table leaves those choices
  at their owners and adds no record that its rules do not require."
- Not taken: 93–94 and 101–106 (the work/recovery rows; this line's
  rules differ). The F3 rows are this line's own.

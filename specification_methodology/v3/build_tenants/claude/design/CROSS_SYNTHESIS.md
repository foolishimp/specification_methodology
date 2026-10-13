# Claude Tenant Design: Parts Taken From The Codex Candidate

This file lists the parts of the Codex tenant candidate that the Claude
line takes under [Cross-Synthesis](../../../specification/PRODUCT.md#cross-synthesis).
For each part it names the exact source, the one section of this candidate
that receives and owns it, whether the text is copied verbatim or adapted,
and the gap it closes. It is tenant HOW, not accepted.

The parts are those nominated in section 8 ("Carry forward into step 3") of
the [Claude cross-assessment of the Codex candidate](../../../.ai-workspace/comments/claude/20261013T043048Z_REVIEW_CODEX_V3_CANDIDATE_CROSS_ASSESSMENT.md).
The Codex carried corpus (its item 1) is not taken: this line keeps its own
restated text as its base.

## Source coordinates

Every source below is read at commit
`31f28f90c4a9b15243d84630fc4799024a9cd7ac` with

```sh
git -C /Users/jim/src/apps/specification_methodology show \
  31f28f9:specification_methodology/v3/build_tenants/codex/<path>
```

`<path>` is the path in the table. Line numbers are those of that output.
They were verified by reading each file on 2026-10-14 for this design.

## Port list

| # | Part | Source path and lines | Receiving owner in this candidate | Mode | Gap closed |
|---|---|---|---|---|---|
| 1 | Specialization table: premises, the consequence that follows, and the particular contract with its independent choice | `successor/standards/TRANSFORMATION_LIBRARY.md:93–112` (heading 93; instance premises 95–98; table 100–106; standing of the consequences 108–112) | FOUNDATIONS §3, new subsection "Foundation to law", owns the table format and the family index; each family's table sits in its owning member (see [PLAN](../qualification/C3-SYNTHESIS/PLAN.md#material-families-for-relation-1)) | adapted | relation 1 of the [standalone successor requirement](../../../specification/requirements/README.md#standalone-successor-requirement) |
| 2 | Premise standing discipline | `successor/standards/FOUNDATIONS.md:48–51` (standing paragraph) and `:55–65` (owner sentence and the F1–F6 table with its "Premise and standing" and "Distinction retained" columns) | FOUNDATIONS §3 Commitments | adapted: paragraph 48–51 scoped to the recovered and independent commitments; table columns adapted | a premise is never presented as derived; relation 1's "foundational premises" |
| 3 | Reference-only import declarations | `successor/standards/FOUNDATIONS.md:128–162`; second instance `successor/standards/TRANSFORMATION_LIBRARY.md:27–57` | the import rule: FOUNDATIONS §2 (decision D7 in [DOCUMENT_STRUCTURE](DOCUMENT_STRUCTURE.md#ownership-decisions)); the first instance: REFERENCE_FRAME §1, replacing its "Statement of ownership" paragraph | adapted: direction, loss and no-transfer sentences (130–132, 155–156) with this candidate's context and owner names substituted; table columns unchanged; rows written for this candidate's concepts | single ownership items 3 and 4: a use of another member's concept names its owner |
| 4 | Equivalence ladder: conformance, then semantic, computational and categorical equivalence | `successor/standards/FOUNDATIONS.md:249–258` (category and functor assertion 249–253; the ladder 254–258) | EVALUATION §6 Conformance of realisations, which already separates conformance from semantic and computational equivalence (`EVALUATION.md:184–188`); FOUNDATIONS §4 Formal fragment refers to it | lines 254–258 adapted to this candidate's symbols 𝒜, ℐ and 𝒞_H; lines 249–253 not ported, because `FOUNDATIONS.md:379–382` of this candidate already states that obligation | item 4 of the [categorical demonstration standard](../../../specification/requirements/README.md#categorical-demonstration-standard): conformance, equivalence and functorial preservation are distinct claims |
| 5 | Verbatim, digest-bound frames with a manifest, and direct acquisition of deciding owners | frame layout: `successor/standards/frames/WORK_RECOVERY.md` (preface 1–21, `Source:` line 25 with owner digest, verbatim section from 27); the other four frames in `successor/standards/frames/` follow it. Manifest: `qualification/C3/FRAME_INPUTS.json` (whole file: `kind`, `limits`, and per frame `path`, `bytes`, `sha256`, `scope`, `routes[]` with `owner`, `owner_sha256`, `anchor`, `section_sha256`). Generator: `qualification/C3/refresh_views.py:1–18` (digest and heading-slug functions) and `:44–66` (frame regeneration). Acquisition rule: `successor/plugins/spec/skills/stdo-work/SKILL.md:18–39`, chiefly 28–32 | frames and manifest: `standards/frames/` with `standards/frames/FRAME_INPUTS.json`; generator: `qualification/instruments/generate_frames.py`; acquisition rule: ACTIVATION §2 (owner), routed from the `stdo-work` skill in packaging | mechanism and manifest schema verbatim; generator adapted; prefaces rewritten; acquisition rule adapted | stale and oversized a_c-projected frames; single ownership item 4 (a frame's copy names its owner); single result algebra item 7 |
| 6 | Finite check with mutant counterexamples | `qualification/C3/a_c/finite_check.py:1–95`, with `FINITE_RESULT.json`, `ENCODING.md` and `SOURCE.md` in the same directory | `qualification/instruments/finite_oracle/` as an oracle template for criterion 4 case designs; the method law it serves is EVALUATION §7 Frame qualification | pattern adapted; no code or domain copied | expectations specified independently of the author, checked exhaustively where the domain is finite |

## How each part is adapted

**Part 1.** Codex's three columns are premises, conditional consequence,
and particular contract with independent choice. Relation 1 asks for
premises, consequences, and added choices with their owners, so this line
uses four columns:

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner |
|---|---|---|---|

The instance-premise paragraph (Codex 95–98) and the standing paragraph
(Codex 108–112) are restated for each family: the consequences are
arguments from the stated premises, not proofs of every clause, and the
added choices are not inferred from the foundations. The content of
Codex's work/recovery rows is not taken; this candidate's rules differ.

**Part 2.** Codex's paragraph 48–51 states that the premises are adopted
commitments, "not theorems derived from finite capacity alone". This
candidate has two derived commitments, P4b and P5, each with named
premises (`FOUNDATIONS.md:299–322`), so the paragraph is scoped to the
others. The standing column uses only the four standing terms of
FOUNDATIONS §1: "recovered" for P0, "independent" for P1, P2, P3, P4a and
P6, and "derived from …" for P4b and P5. The paragraph states that the
recovered and independent commitments are the adopted premises (decision
D6). The "Distinction retained" column is kept.

Parts 2 and 3 are adapted, not verbatim, so they are reviewed as
adaptations: the receiving activation's return shows each changed sentence
as a diff from its source.

**Part 3.** This candidate already owns the law of cross-context
relations at PRODUCT_DEFINITION §5 (`PRODUCT_DEFINITION.md:412–443`):
import, translation, equivalence and disambiguation, each with direction,
loss and owners. Codex's tables are instances of such a law. The instances
needed here are in tier 1 (the foundations tier), and a tier-1 member must
not depend on a tier-2 owner (single ownership item 2). Decision D7 places
the generic rule in FOUNDATIONS §2.

**Part 4.** The categorical rung keeps Codex's condition: categorical
equivalence needs a quasi-inverse and natural isomorphisms on a stated
domain, and an analogy or matching result is insufficient.

**Part 5.** The Codex frame prefaces state that a frame "makes no
material-sufficiency claim" and that no result enumeration follows from it
(`WORK_RECOVERY.md:10–17`). Those two sentences are not ported. Acceptance
criterion 4 tests whether a frame supplies the material its task needs,
and the [single result algebra requirement](../../../specification/requirements/README.md#single-result-algebra-requirement)
item 7 requires a frame whose task returns a result to carry the core
algebra. Each frame's routes therefore include the owner of the core
result algebra whenever its task returns a result. Each `Source:` line
names the owning section and its digest, so a copy that differs from its
owner is detected by regeneration. The heading-slug rule of the generator
(`refresh_views.py:15–18`) and of `qualification/instruments/bounded_step.py`
(lines 58–61) give the same anchor for every heading of the 23 current
members, checked by script on 2026-10-14; the generator uses one rule and
refuses an absent or duplicated heading, as Codex's does (lines 54–55).
a_c projections become optional: they may be published beside the
verbatim frames, and they are not the activation unit.

**Part 6.** The pattern taken is: enumerate a declared finite domain
exhaustively (Codex 34–56); derive the expected cardinalities
independently of the implementation and assert them (57–61); run a
deliberately wrong variant and require its counterexamples to be found
(50–55, 61–63); bind the digests of source, model and executable into the
result (76–80); list the limits of what the check proves (86–93); refuse
to run with assertions disabled (12–13). Codex's token domain is not
copied.

## Review of ported text

Ported text stays verbatim where the table says so. It is compared byte
for byte with its source at `31f28f9`, and a Claude Reviewer that did not
port it compares it with the previous release
([ledger default 3](../qualification/C3-SYNTHESIS/LEDGER.md#defaults-taken-for-the-open-decisions)).
Text this line writes around a port is left for Codex's cross-family
review. Each receiving activation records, in its return, the part's
source coordinates, its owning section and the frontier disposition it
supports. A part with no predecessor row is new law and states its purpose
and the material relation it protects (acceptance criterion 6).

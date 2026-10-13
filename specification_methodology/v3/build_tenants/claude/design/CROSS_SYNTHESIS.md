# Claude Tenant Design: Parts Taken From The Codex Candidate

This file lists the parts of the Codex tenant candidate that the Claude
line takes under [Cross-Synthesis](../../../specification/PRODUCT.md#cross-synthesis).
For each part it names the exact source, the one section of this candidate
that receives and owns it, the frontier cone it enters, whether the text
is copied verbatim or adapted, and the gap it closes. It is tenant HOW, not
accepted.

The six parts come from items 2 to 6 of section 8 ("Carry forward into
step 3") of the
[Claude cross-assessment of the Codex candidate](../../../.ai-workspace/comments/claude/20261013T043048Z_REVIEW_CODEX_V3_CANDIDATE_CROSS_ASSESSMENT.md):
item 2 gives part 2, item 3 part 1, item 4 parts 3 and 4, item 5 part 5,
and item 6 part 6. The Codex carried corpus (its item 1) is not taken:
this line keeps its own restated text as its base.

Symbols: 𝒜, ℐ and 𝒞_H name the three accounts in hypothesis H1 of this
candidate's FOUNDATIONS §4 Formal fragment. 𝒜 is the algorithmic account,
the free category on typed primitives; ℐ is the interpreted informational
account, carrier sets with total functions; 𝒞_H is the computational
realisation on a declared architecture H. Codex writes them A, I and C_H.

## Source coordinates

Every source below is read at commit
`31f28f90c4a9b15243d84630fc4799024a9cd7ac` with

```sh
git -C /Users/jim/src/apps/specification_methodology show \
  31f28f9:specification_methodology/v3/build_tenants/codex/<path>
```

`<path>` is the path in the table. Line numbers of Codex files are those
of that output; a citation of a Codex file names Codex or a Codex path.
Line citations of this candidate's own members are to its base,
`build_tenants/claude/` at the same commit.

## Port list

| # | Part | Source path and lines | Receiving owner in this candidate | Mode | Gap closed |
|---|---|---|---|---|---|
| 1 | Specialization table: premises, the consequence that follows, and the particular contract with its independent choice | `successor/standards/TRANSFORMATION_LIBRARY.md:93–112` (heading 93; instance premises 95–98; table 100–106; standing of the consequences 108–112) | FOUNDATIONS §3, new subsection "Foundation to law", which owns the table format, the standing of the consequences and the family index. Each family's table is this line's own text in its owning member, written to that format (see [PLAN](../qualification/C3-SYNTHESIS/PLAN.md#material-families-for-relation-1)) | adapted | relation 1 of the [standalone successor requirement](../../../specification/requirements/README.md#standalone-successor-requirement) |
| 2 | Premise standing discipline | `successor/standards/FOUNDATIONS.md:48–51` (standing paragraph) and `:55–65` (owner sentence and the F1–F6 table with its "Premise and standing" and "Distinction retained" columns) | FOUNDATIONS §3 Commitments | adapted: paragraph 48–51 scoped to the recovered and independent commitments; table columns adapted | a premise is never presented as derived; relation 1's "foundational premises" |
| 3 | Reference-only import declarations | `successor/standards/FOUNDATIONS.md:128–162`. `successor/standards/TRANSFORMATION_LIBRARY.md:27–57` is a second instance of the same declaration, read for comparison only; nothing is taken from it | REFERENCE_FRAME §1, `### Imports into this context`, replacing its "Statement of ownership" paragraph. It follows the import rule owned by FOUNDATIONS §2 (decision D7 in [DOCUMENT_STRUCTURE](DOCUMENT_STRUCTURE.md#ownership-decisions)), which is this line's own text | adapted: direction, loss and no-transfer sentences (130–132, 155–156) with this candidate's context and owner names substituted; table columns unchanged; rows written for this candidate's concepts | single ownership items 3 and 4: a use of another member's concept names its owner |
| 4 | Equivalence ladder: conformance, then semantic, computational and categorical equivalence | `successor/standards/FOUNDATIONS.md:249–258`: category and functor assertion 249–250; naming of A, I and C_H from 251 to "supplied." on 254; the ladder from "For a proposed span" on 254 to 258 | EVALUATION §6 Conformance of realisations, which already separates conformance from semantic and computational equivalence (`EVALUATION.md:184–188`); FOUNDATIONS §4 Formal fragment refers to it | the ladder adapted to this candidate's symbols 𝒜, ℐ and 𝒞_H; lines 249 to the end of the naming sentence on 254 not ported, because `FOUNDATIONS.md:379–382` of this candidate already states that obligation | item 4 of the [categorical demonstration standard](../../../specification/requirements/README.md#categorical-demonstration-standard): conformance, equivalence and functorial preservation are distinct claims |
| 5 | Verbatim, digest-bound frames with a manifest, and direct acquisition of deciding owners | Frame layout: `successor/standards/frames/WORK_RECOVERY.md` (preface 1–21, `Source:` line 25 with the owning member's digest, verbatim section from 27); the other four frames in `successor/standards/frames/` follow it. Manifest: `qualification/C3/FRAME_INPUTS.json`, with seven top-level keys: `kind`, `limits`, `frames`, `source_linked_summaries`, `view_subject_binding`, `initial_derivation_commit`, `initial_derivation_commit_standing`. Generator: `qualification/C3/refresh_views.py:1–18` (digest and heading-slug functions) and `:44–66` (frame regeneration). Acquisition rule: `successor/plugins/spec/skills/stdo-work/SKILL.md:18–39`, chiefly 28–32 | frames and manifest: `standards/frames/` with `standards/frames/FRAME_INPUTS.json`; generator: `qualification/instruments/generate_frames.py`; acquisition rule: ACTIVATION §2 (owner), routed from the `stdo-work` skill in packaging | frame mechanism verbatim. Manifest adapted: `kind`, `limits` and `frames` (per frame `path`, `bytes`, `sha256`, `scope`, `routes[]` with `owner`, `owner_sha256`, `anchor`, `section_sha256`) taken verbatim; the other four keys not taken, because they bind Codex's source-linked summaries and its derivation history. Generator adapted under the requirements below; prefaces rewritten; acquisition rule adapted | stale and oversized a_c-projected frames; single ownership item 4 (a frame's copy names its owner); single result algebra item 7 |
| 6 | Finite check with mutant counterexamples | `qualification/C3/a_c/finite_check.py:1–95`, with the files in the same directory that it reads (`SOURCE.md`, `program.json`, `program-mutant.json`) and writes (`FINITE_RESULT.json`), and `ENCODING.md` | `qualification/instruments/finite_oracle/` as an oracle template for criterion 4 case designs; the method law it serves is EVALUATION §7 Frame qualification | pattern adapted; Codex lines 6–9, 11–13 and 94–95 copied verbatim (re-indented), the rest adapted or not ported, as `returns/C2.md` records; no domain copied | expectations specified independently of the author, checked exhaustively where the domain is finite |

### Frontier cone of each part

A part enters this line only as a named contribution inside one member's
frontier cone ([PRODUCT, Cross-Synthesis](../../../specification/PRODUCT.md#cross-synthesis)).
A member's frontier cone is the rows of the tenant frontier record that
its restatement covers.

| Part | Contribution | Frontier cone it enters |
|---|---|---|
| 1 | the table format and the standing of the consequences, in FOUNDATIONS §3 Foundation to law | FOUNDATIONS |
| 2 | the standing column and the adopted-premise paragraph, in FOUNDATIONS §3 Commitments | FOUNDATIONS |
| 3 | the import declaration, in REFERENCE_FRAME §1 | REFERENCE_FRAME |
| 4 | the equivalence ladder, in EVALUATION §6 | EVALUATION |
| 5 | the acquisition rule, in ACTIVATION §2 | ACTIVATION |

Part 5's generator and part 6's oracle template are qualification
instruments. Part 5's frame layout and manifest shape the frames, which
the C3 Outcome requires in the candidate as generated copies of owning
sections; a frame owns no determination (single ownership item 4). None of
these is candidate law: they enter no frontier cone and support no
disposition. The `stdo-work` skill's route to the acquisition rule is
packaging, which refers to ACTIVATION §2 and owns nothing. Any Codex
sentence a receiving activation takes into a section not named here, such
as FOUNDATIONS §2, is a further contribution, recorded in that member's
cone with its own source coordinates.

## How each part is adapted

**Part 1.** Codex's three columns are premises, conditional consequence,
and particular contract with independent choice. Relation 1 asks for
premises, consequences, and added choices with their owners, so this line
uses four columns:

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner |
|---|---|---|---|

FOUNDATIONS §3 Foundation to law owns this format and states once, adapted
from Codex 108–112, the standing of every family's consequences: they are
arguments from the stated premises, not proofs of every clause, and the
added choices are not inferred from the foundations. Each family's table
states its own instance premises, as Codex 95–98 does for work and
recovery, and refers to FOUNDATIONS §3 for the standing of its
consequences, so the ported text has one owning section. The content of
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

For every adapted part, the receiving Writer's return shows each changed
sentence beside its source. That record is the author's evidence and an
input to the Reviewer's comparison, not the comparison itself
([Review of ported text](#review-of-ported-text)).

**Part 3.** This candidate already owns the law of cross-context
relations at PRODUCT_DEFINITION §5 (`PRODUCT_DEFINITION.md:412–443`):
import, translation, equivalence and disambiguation, each with direction,
loss and owners. Codex's tables are instances of such a law. The instances
needed here are in tier 1 (the foundations tier). This tenant reads the
tier order of [PRODUCT, Method Structure](../../../specification/PRODUCT.md#method-structure),
where the Spec Method uses the foundational contracts and profiles import
the shared contracts, as requiring that a tier-1 member not depend on a
tier-2 owner. Decision D7 therefore places the import rule in FOUNDATIONS
§2; PRODUCT_DEFINITION §5 keeps translation, equivalence and
disambiguation and refers to FOUNDATIONS §2 for import.

**Part 4.** The categorical rung keeps Codex's condition: categorical
equivalence needs a quasi-inverse and natural isomorphisms on a stated
domain, and an analogy or matching result is insufficient.

**Part 5.** The Codex frame prefaces state that a frame "makes no
material-sufficiency claim" and that no result enumeration follows from it
(Codex `WORK_RECOVERY.md:10–17`). Those two sentences are not ported.
Acceptance criterion 4 tests whether a frame supplies the material its
task needs, and the
[single result algebra requirement](../../../specification/requirements/README.md#single-result-algebra-requirement)
item 7 requires a frame whose task returns a result to carry the core
algebra. Each frame's routes therefore include the owner of the core
result algebra whenever its task returns a result. Each `Source:` line
names the owning section and the owning member's digest, as Codex's do.
The manifest records the member digest (`owner_sha256`) and the section
digest (`section_sha256`) of every route, so a copy that differs from its
owner is detected by regeneration. a_c projections are optional: they may
be published beside the verbatim frames, and they are not the activation
unit.

The generator `qualification/instruments/generate_frames.py` is written
by activation C1 of the [PLAN](../qualification/C3-SYNTHESIS/PLAN.md). It
must meet these requirements:

1. One heading-slug rule. It uses the slug rule of Codex
   `refresh_views.py:15–18`, which is also the rule of this candidate's
   `qualification/instruments/bounded_step.py` (lines 58–61). The working
   review [RW1](../qualification/C3-SYNTHESIS/reviews/RW1.md) records that
   the two rules give the same anchor for every in-scope heading of the 23
   members.
2. Fenced code is not structure. A fenced code block opens with a line of
   three or more backticks, or three or more tildes, indented by at most
   three spaces, and closes only at a line of the same character at least
   as long. No line inside a fenced block is a heading: it is neither a
   selectable anchor nor a section end. Headings are ATX headings (`#` to
   `######` followed by a space) outside fenced blocks. A section ends at
   the next such heading of equal or higher level, or at the end of the
   member.
3. Refusal, never truncation. The generator writes no frame and returns a
   refusal, naming the member and line, when:
   - the selected anchor matches no heading, or more than one, outside
     fenced blocks (Codex's lines 54–55 refuse an absent or duplicated
     heading);
   - a fenced block is still open at the end of the member;
   - the extracted section would end inside an open fenced block;
   - a fence-like line is indented by four or more spaces, or a line of
     only `=` or `-` stands directly under a text line outside a fenced
     block, because either line's reading depends on context the rule does
     not decide.
4. Digests over the full extent. The section digest is computed over the
   section as rule 2 bounds it.
5. Tests. Each refusal has a test, and so does each section that RW1
   (finding F14) lists as ending early under Codex's rule at a heading
   inside a fenced block: each is extracted to its full extent.

**Part 6.** The pattern taken is: enumerate a declared finite domain
exhaustively (Codex 34–56); derive the expected cardinalities
independently of the implementation and assert them (57–61); run a
deliberately wrong variant and require its counterexamples to be found
(50–55, 61–63); bind the digests of source, model and executable into the
result (76–80); list the limits of what the check proves (86–93); refuse
to run with assertions disabled (12–13). Codex's token domain is not
copied.

## Review of ported text

Each receiving activation records, in its return, the part's source
coordinates, its owning section, the frontier cone it enters and the
disposition it supports, and for an adapted part each changed sentence
beside its source.

The Reviewer of each receiving activation compares every part it
receives, verbatim or adapted, with its source, read by `git show` at
`31f28f9` under [Porting reads](../../../specification/PRODUCT.md#development-isolation),
and with the predecessor clause in the previous release, and records both
comparisons in its review file. Verbatim text is compared byte for byte;
adapted text sentence by sentence, with each change and its reason named.
The Writer's record is an input to that comparison, never its evidence.
Fidelity to the peer is not conservation: a part that matches its source
still needs the comparison with the previous release that acceptance
criterion 2 requires. The instruments of parts 5 and 6 are compared with
their sources in the same way and are also tested by their own checks:
regeneration is byte-identical, and the mutant's counterexamples are
found.

Ported text keeps no link to `build_tenants/codex/`, and every term it
uses resolves in this candidate. Its result values map into this
candidate's core result algebra (FOUNDATIONS §4 Results).

How a ported part is reviewed for acceptance is the product owner's open
decision ([PRODUCT, Open Owner Decisions](../../../specification/PRODUCT.md#open-owner-decisions)).
The Independence rule forbids a Reviewer assessing its own authorship. The
Codex tenant is the source author of every ported part, this tenant is the
author of the text around it, and an adapted sentence has both authors.
The product owner decides how a ported part, adapted sentences included,
is reviewed before the first frontier cone with a contribution is
accepted. Until that ruling this design applies the default the ledger
takes
([ledger default 3](../qualification/C3-SYNTHESIS/LEDGER.md#defaults-taken-for-the-open-decisions)):
ported text stays verbatim where possible; a Claude working check that did
not port it makes both comparisons above; the Claude-written text around a
port is left for Codex's cross-family review. That default yields working
checks only, and no cone that contains a ported part is accepted before
the product owner's ruling. The acceptance Reviewer the ruling selects
makes the same two comparisons.

A part with no predecessor row is new law and states its purpose and the
material relation it protects (acceptance criterion 6).

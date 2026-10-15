# R2b successor packet: the ported receivers after the R2b repairs

The first ports readback (R2b, `reviews/R2b.json`) made 13 findings; `reviews/TRIAGE-R2.md` records each disposition. This packet gives the receivers as they now stand, the corrected records, and the donor sources again where a receiver changed. Read everything here and nothing else.

## The triage record (the Writer's dispositions, an input to your judgment)

```markdown
# Triage of the readbacks R2b (ports) and R2a (repairs and I4 edits)

One repair round, by the Executive. R2b ran on Sonnet and R2a on Opus 5.5
(high) before the product owner selected Fable at max for later readings;
both are same-family nonauthor working evidence in fresh contexts. Every
finding is repaired at its owning locus or declined with its reason. The
changed ports and the changed loci receive one successor readback (I4-09).

## R2b, ports (13 findings)

| Id | Disposition | Where |
|---|---|---|
| R2b-01 | repaired: the record names the Pillar column, the pillar definition, the trace paragraph and the placement rule as this line's own additions, with reasons | CROSS_SYNTHESIS part 1 |
| R2b-02 | repaired: the unrecorded differences and the uncarried owner sentence are recorded with reasons | CROSS_SYNTHESIS part 2 |
| R2b-03 | repaired: the import rule has one owner. REFERENCE_FRAME §1 no longer repeats the rule's sentences; the record says which Codex sentences FOUNDATIONS §2 carries, as a port in its cone | REFERENCE_FRAME §1; CROSS_SYNTHESIS part 3 |
| R2b-04 | repaired: the two added rules and the omissions are recorded with reasons | CROSS_SYNTHESIS part 3 |
| R2b-05 | repaired: FOUNDATIONS §3 names PROFILES §1's rule the family-import rule, under the import rule of §2 | FOUNDATIONS §3 |
| R2b-06 | repaired: "the pair" replaced by the functor and its quasi-inverse; the Formal fragment's items referred to, not restated; the differences recorded with reasons | EVALUATION §6; CROSS_SYNTHESIS part 4 |
| R2b-07 | repaired: the row filter is recorded (requirement 6), documented in the generator, tested (`RowSelection`, three tests), and the preface says a `rows=k/n` excerpt is not a byte copy | CROSS_SYNTHESIS part 5; generate_frames.py; test_generate_frames.py |
| R2b-08 | repaired: `id` and `task`, the acquisition additions and the restored no-universal-sufficiency sentence are recorded; the sentence is restored in ACTIVATION §2 | CROSS_SYNTHESIS part 5; ACTIVATION §2 |
| R2b-09 | repaired: the verbatim list corrected to lines 6–9, 12–13 and 94–95, line 11 adapted | CROSS_SYNTHESIS part 6 |
| R2b-10 | declined in part: the `conserved`-only condition is kept, because a `superseded` row is decided by its proposed relation and not by the conservation reading; the condition, its reason and the extra fields are now recorded | frontier_review.py docstring; ports.md C3 |
| R2b-11 | declined: the locus hash follows the frontier's own granularity (a row covers its heading's text up to the next heading of any level), which differs on purpose from the frame generator's whole-section rule; recorded | frontier_review.py docstring; ports.md C3 |
| R2b-12 | explained and scheduled: the positive reproductions fail because the frozen `a_c/i3` artifacts are stale against the member edits of this iteration, which is the checker reporting correctly; the artifacts are regenerated at the freeze and the controls rerun then. The dropped-clause control now has a passing baseline, the fresh positive projection of the same index, and the projections run from the fresh map | ac_controls.py; ports.md C5 |
| R2b-13 | repaired: the identity check reads the executable, schema and output-contract digests from the common `A_C_DEPENDENCY.md` and the adverse control appends one byte to a copy of the schema and expects the same check to refuse; it does | ac_controls.py |

## R2a, repairs and I4 edits (8 findings, 4 unexplained changes)

| Id | Disposition | Where |
|---|---|---|
| R2a-01 | repaired: `block-outside-claim` is again a prohibition (`forbids`, `must-not`) with the condition "by itself" and the repricing or re-entry consequence as its qualification; program rebuilt, 64 clauses, `assemble --check` 0 | a_c/i3/tools/spec.py; a_c/i3 |
| R2a-02 | declined: the purpose and material relation of the §5 table is stated at the end of EVALUATION §5 `When a finding blocks promotion` ("Purpose and material relation: the method stated these conditions in a work carrier, a design profile and the Executive profile…"); it predates `416bdb5`, so it is not in the diff the reviewer saw | EVALUATION §5 |
| R2a-03 | repaired: the disposition row conserved at EXECUTIVE_BASELINE names it in its Locus column | ACTIVATION §8 |
| R2a-04 | recorded as intended: the J55 case text follows the ratified common discriminator, which dropped "applicable" and added that inapplicability waives no criterion; REBIND item 12 | REBIND.md; this record |
| R2a-05 | repaired: the preface no longer claims the omitted rows are not needed; the frame's qualification decides sufficiency | generate_frames.py header |
| R2a-06 | repaired: both additions cite their principles and say they are new law carried from the common contract at iteration 4; the fit claim for a boundary and the step's fit judgment are stated as distinct | ACTIVATION §1, §2 |
| R2a-07 | repaired: the sentence is scoped to a received contribution | EVALUATION §3 |
| R2a-08 | repaired: a `conserved` disposition recorded before the test applied is re-evaluated under it before the claim qualifies, `unresolved` until then; this is what `frontier/REVIEW.json` records | RELEASE §9 |
| unexplained 1 | the same as R2a-01 | |
| unexplained 2 | explained: the EVALUATION §4 paragraph states the purpose of the generalisation FR-01's rows introduced, as criterion 6 requires of new law | |
| unexplained 3, 4 | explained: frame regeneration after the repaired member text | |
| FR-06 partly | the only remaining "core conjunction" in the design (DOCUMENT_STRUCTURE line 56) describes REFERENCE_FRAME's reference to FOUNDATIONS §4 for frames in conjunction, not the reader of J53 to J55; no change | |
| FR-11 partly | the body of ACTIVATION §1 generalises the restriction; the predecessor claim is conserved at EXECUTIVE_BASELINE, whose row now names it (R2a-03) | |

```

## The port records as corrected (CROSS_SYNTHESIS, source coordinates, port list and 'How each part is adapted')

```markdown
## Source coordinates

Every source below is read at commit
`31f28f90c4a9b15243d84630fc4799024a9cd7ac` with

```sh
git -C /Users/jim/src/apps/specification_methodology show \
  31f28f9:specification_methodology/v3/build_tenants/codex/<path>
```

Iteration 4 donor: the Codex candidate at handoff `fb855df`, package
`d490dd6`, read the same way at those commits. Its evaluation is
[C3-ITER4/ports.md](../qualification/C3-ITER4/ports.md).

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
| 5 | Verbatim, digest-bound frames with a manifest, and direct acquisition of deciding owners | Frame layout: `successor/standards/frames/WORK_RECOVERY.md` (preface 1–21, `Source:` line 25 with the owning member's digest, verbatim section from 27); the other four frames in `successor/standards/frames/` follow it. Manifest: `qualification/C3/FRAME_INPUTS.json`, with seven top-level keys: `kind`, `limits`, `frames`, `source_linked_summaries`, `view_subject_binding`, `initial_derivation_commit`, `initial_derivation_commit_standing`. Generator: `qualification/C3/refresh_views.py:1–18` (digest and heading-slug functions) and `:44–66` (frame regeneration). Acquisition rule: `successor/plugins/spec/skills/stdo-work/SKILL.md:18–39`, chiefly 28–32 | frames and manifest: `standards/frames/` with `standards/frames/FRAME_INPUTS.json`; generator: `qualification/instruments/generate_frames.py`; acquisition rule: ACTIVATION §2 (owner), routed from the `stdo-work` skill in packaging | frame mechanism verbatim, except that relative links inside each copied section are rebased so they resolve from `standards/frames/` (revision 2b, Codex review F5); each section digest is still computed over the owner bytes, and the `Source:` line format differs from Codex's. Manifest adapted: `kind`, `limits` and `frames` (per frame `path`, `bytes`, `sha256`, `scope`, `routes[]` with `owner`, `owner_sha256`, `anchor`, `section_sha256`) taken verbatim; the other four keys not taken, because they bind Codex's source-linked summaries and its derivation history. Generator adapted under the requirements below; prefaces rewritten; acquisition rule adapted | stale and oversized a_c-projected frames; single ownership item 4 (a frame's copy names its owner); single result algebra item 7 |
| 6 | Finite check with mutant counterexamples | `qualification/C3/a_c/finite_check.py:1–95`, with the files in the same directory that it reads (`SOURCE.md`, `program.json`, `program-mutant.json`) and writes (`FINITE_RESULT.json`), and `ENCODING.md` | `qualification/instruments/finite_oracle/` as an oracle template for criterion 4 case designs; the method law it serves is EVALUATION §7 Frame qualification | pattern adapted; Codex lines 6–9, 12–13 and 94–95 copied verbatim (re-indented); line 11 adapted, `TEMPLATE = Path(__file__).resolve()` for the donor's `root = Path(__file__).resolve().parent` (corrected at I4), the rest adapted or not ported, as `returns/C2.md` records; no domain copied | expectations specified independently of the author, checked exhaustively where the domain is finite |

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
premises, consequences, and added choices with their owners, and relation
1 also asks that the applicable pillar contributions be bound to each
argument, so this line uses five columns, the fifth added at I3-2 and
not in the source:

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|

Three further additions are this line's own text, not in the source:
the ten-pillar definition under the table (what a Pillar cell names);
the trace paragraph each family writes above its table (which family it
is, where an actor enters it, which families it imports), so the actor
meets the trace where it applies the rules; and the placement rule that
the table sits in the owning member at the family's entry section.

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
D6). The "Distinction retained" column is kept. Differences beyond those,
each this line's own text: a new opening sentence introducing the
commitments; a gloss that finite capacity alone derives none of them;
"each with its owner" on the domain and policy choices, because relation
1 asks for owners; a reworded closing sentence and a purpose sentence,
as every section of this candidate carries. The owner sentence at Codex
55–56 is not carried: FOUNDATIONS §3 already names the owner of the
commitments table in its own voice.

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

What was ported where, corrected at I4 after the R2b readback:
FOUNDATIONS §2 Imports between members carries the direction, loss and
no-transfer sentences (Codex 130–132, adapted to this corpus) and the
no-authority and basis sentences (Codex 141–144 and 161–162, near
verbatim); those sentences are a ported contribution in FOUNDATIONS'
cone with these source coordinates, not this line's own text.
REFERENCE_FRAME §1 `Imports into this context` is the declaration for
one context: it names the owner of the rule and carries only the table
and what is specific to this context. The sentences it repeated from the
rule were removed at I4 so the rule has one owner. Two rules in that
declaration are this line's own text, with their reasons: a refinement
this member states names its owner and maps back to it (single result
algebra, one owner per determination); a frame or frame family that a
profile or product declares in this context is that owner's
specialisation and is not imported (PROFILES §1 owns family import).
Not carried from the source, with reasons: the source and target basis
pins (an import is a relation between owning sections; the basis an
activation binds is FOUNDATIONS §2 Basis, stated once there); the
review-carrier and role-label sentences (carriers are TICKETS' and role
labels are PROFILES' matter).

**Part 4.** The categorical rung keeps Codex's condition: categorical
equivalence needs a quasi-inverse and natural isomorphisms on a stated
domain, and an analogy or matching result is insufficient. Differences
from Codex 249–258, each this line's own: `Sigma_contract` is written Σ,
this candidate's symbol for the contract; the natural-isomorphism
condition names the functor and its quasi-inverse explicitly (corrected
at I4 from "the pair"); the items a categorical claim must meet are not
restated, they are referred to FOUNDATIONS §4 Formal fragment, which
owns them (corrected at I4); a sentence disambiguates this rung from the
cross-context relations of PRODUCT_DEFINITION §5; and the rule that the
rungs are not ordered, so evidence for one is not evidence for another,
is stated because EVALUATION §1 requires it.

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

Differences from the Codex frame layout and acquisition rule beyond the
above, each this line's own: a frame specification carries an `id` and a
`task` beside its scope and routes, so a frame is selected by task; the
acquisition rule of ACTIVATION §2 adds the order "derived surface first
where its sources are current, else the deciding owner sections", the
stale fallback, and the naming of the outcome when a binding is missing;
and, at I4 (I4-06, tradeoff TO1), a route may carry `rows: frame-anchors`,
under which the generator copies from a family table only the rows that
cite a section the frame carries, with the table's preamble, header and
every non-family table, so that a frame carries the derivations of its
own sections and excludes the others; such an excerpt is not a byte copy
of its section and its `Source:` line says so (`rows=k/n`). The sentence
of Codex `SKILL.md` that no acquisition makes a universal sufficiency
claim is carried in ACTIVATION §2 (restored at I4).

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
6. Row selection (I4). A `rows: frame-anchors` route keeps prose,
   headings, blank and fenced lines, every table header and separator,
   every row of a table whose header has no `Consequence` column, and
   the family-table rows whose link destinations name an anchor the
   frame carries in that member; the route records `selected`, `total`
   and the excerpt digest. It has a test.

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
```

## Receivers now

### REFERENCE_FRAME §1 Imports into this context (port 3)

```markdown
This member imports the concepts below into
`urn:stdo:bounded-context:reference-frame-evaluation` under the import rule
of [FOUNDATIONS §2](FOUNDATIONS.md#imports-between-members), which states
what an import is, its direction and loss, and that it transfers no
ownership and confers no authority; this declaration restates none of
that. FOUNDATIONS, ACTIVATION and EVALUATION declare no bounded-context
identity, so each row's source context is its member; the target context
and its owner are declared in Scope above (P1, P3).

| Referenced concept | Source context | Exact source concept and owner |
|---|---|---|
| evaluation, evaluation family, workspace, material-relation manifold, coordinate, topology, capability envelope, reference frame, activated frame, frame set, active frame configuration, lens; role, persona, abstraction and component | FOUNDATIONS | [Frame objects](FOUNDATIONS.md#frame-objects), FOUNDATIONS §2 |
| subject, outcome, basis, material relation, evidence, actor, claim, judgment, residual | FOUNDATIONS | [Ontology](FOUNDATIONS.md#2-ontology), FOUNDATIONS §2 |
| frame-set, semantic, evaluation, operation and decision authority; actor identity | FOUNDATIONS | [Authority kinds](FOUNDATIONS.md#authority-kinds), FOUNDATIONS §2 |
| frame disjointness, evaluation independence and assurance independence | FOUNDATIONS | [Disjointness and independence](FOUNDATIONS.md#disjointness-and-independence), FOUNDATIONS §2 |
| the frame tuple ⟨Q, B, M, C, I, A, E, X, R, J, K, D⟩ | FOUNDATIONS | [The frame tuple](FOUNDATIONS.md#the-frame-tuple), FOUNDATIONS §2 |
| the core result values, their meanings and standing, the evaluation not performed, and refinements of the core | FOUNDATIONS | [Results](FOUNDATIONS.md#results), FOUNDATIONS §4 |
| conjunction and composition of results, with the declared decision rule | FOUNDATIONS | [Conjunction of results](FOUNDATIONS.md#conjunction-of-results), FOUNDATIONS §4 |
| activation as a step: intake, admission, applicability, context construction with its size measurement, activation and evaluation | ACTIVATION | [The step](ACTIVATION.md#1-the-step), ACTIVATION §1; [Context construction under an envelope](ACTIVATION.md#2-context-construction-under-an-envelope), ACTIVATION §2 |
| the step's result refinements and disposition | ACTIVATION | [Step results and disposition](ACTIVATION.md#3-step-results-and-disposition), ACTIVATION §3 |
| the closed result and its reuse | ACTIVATION | [Closed result and reuse](ACTIVATION.md#7-closed-result-and-reuse), ACTIVATION §7 |
| qualification of a frame and of this method | EVALUATION | [Qualification of frames and of the method](EVALUATION.md#7-qualification-of-frames-and-of-the-method), EVALUATION §7 |

Scope bounds what
this member owns; a concept of those kinds that another member defines,
such as evaluation, basis, the activation step, the core results or
qualification, is imported here, and this member defines it no second
time. A refinement this member states, such as the function outcomes of §5
or the coverage statuses of §8, names its owner in this table and maps
back to it. A frame or frame family that a profile or product declares in
this context is that owner's specialisation under Scope above and is not
imported here (P1, P3, P6).
The declaration is new in this corpus. Purpose and material relation: each
concept used here keeps one owning section, so its meaning cannot diverge
between that owner and this member (P1, P6).
```

### FOUNDATIONS §2 Imports between members (port 3)

```markdown
A member that uses a concept another member defines imports it and does
not define it again (P1, P3; provenance
`stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#bounded-context-semantic-resolution`,
whose semantic import adopts the cited meaning unchanged). An import is
reference-only. Source and target meanings are identical owner-qualified
references, not new local definitions. Direction is from the named source
to the importing context; loss is none and no translation or ownership
transfer is asserted. An import provides no semantic, evaluation,
operation or decision authority (P6; Authority kinds, What creates no
authority). A use that changes, narrows or loses
the source meaning is not an import and is never declared as one.

An import declaration states, for each imported concept (P1, P3, P6):

- what is imported: the concept, under the name its owner gives it;
- its owner: the owning section of the member that defines it, which is a
  place in the text, not a semantic authority (Authority kinds above);
- the source context: the bounded context the owning member declares, or
  that member itself where it declares none;
- the target context and the member that owns it;
- the direction and the loss, which one sentence may state for all the
  concepts of one declaration.

An import takes one of two forms. A declaration states these contents
for each imported concept in one place; between members of this corpus it
rests on the authority of the Product that owns the corpus, so the
relation is owner-authorised (P6). A reference at the point of use
that names the owning section is also an import: it states what is
imported and its owner; its source context is the one the list above
names, its target is the using member's context, and its direction, loss
and lack of authority are those stated above. A concept another member
defines enters a bounded context only by one of these forms, never by
proximity or equal spelling (P1, P3).

An activation binds each member's distinct coordinates in its selected
complete governing basis; equal cut selection does not mean equal member
coordinates. Adoption is a target's taking an imported concept into use
under the conditions its source states, which are its adoption premises.
Lifecycle and adoption remain source-owned. A changed member,
selected basis, source declaration or adoption premise requires fresh
applicability before use. An activation lacking the source meaning,
adoption or authority binding reports that unresolved relation before
dependent reliance rather than interpreting it from equal spelling (P3,
P5). For an evaluation that depends on the imported concept, a missing
source meaning, adoption or authority binding is an undeclared material
relation, the ground of `out_of_frame` ([Results](#results), Out of frame
or indeterminate); a changed member or basis whose applicability is not
yet re-established is the ground of `invalid_basis` (§4 Results).

Purpose and material relation of the declaration's contents, its two
forms, a member as source context and the two grounds above: a concept
used outside its owning section keeps one meaning and one owner, so two
members cannot answer one question two ways, and using a concept grants
no authority over it (P1, P6).
```

### EVALUATION §6 Conformance of realisations (port 4)

```markdown
A realisation aⱼ conforms to a specification Σ when its interpreted behaviour
satisfies Σ under a declared interpretation contract (P1) and an independent
judgment (P6). Several realisations may conform to one Σ; sufficiency does
not require unique derivation or equality with an incumbent. A weak Σ that
admits materially different behaviours either declares the latitude or is
repaired before a decision-complete design is claimed.

Equivalence ladder. The ladder is the list of the four claims named next,
each a rung; the rungs are listed, not ordered, and no rung implies
another. Conformance, semantic equivalence, computational equivalence and
categorical equivalence are separate claims with separate evidence (P1,
P6). Conformance establishes neither identical behaviour outside Σ nor
equal cost. Semantic equivalence of realisations claims that two
realisations, or a realisation and a declared reference outcome, have
identical interpreted behaviour on a stated domain, behaviour outside Σ
included. In this member semantic equivalence is always this equivalence
of realisations, not the equivalence of concepts across bounded contexts
that
[PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution)
governs, and semantic conformance, in the comparison rule below, is
conformance with the governing semantic basis as Σ. Computational
equivalence claims that two realisations compute the same function at
equal cost for declared workloads on a declared architecture H.
Categorical equivalence is a claim about categories and the maps between
them: FOUNDATIONS §4, Formal fragment, owns what a category or functor
claim must show and defines the symbols 𝒜, ℐ and 𝒞_H used here, and a
map's preservation of identities and composition is a further claim
distinct from every rung.
For a proposed span 𝒜 → ℐ and 𝒜 → 𝒞_H, conformance to Σ, semantic
equivalence and computational equivalence remain different claims.
A claim of categorical equivalence meets each item of the Formal fragment
that applies to it, as that section states them. This rung adds one
requirement of its own to those items: a quasi-inverse functor, and
natural isomorphisms between each composite of the functor with its
quasi-inverse and the identity functor, on a stated domain. An analogy or matching result
is insufficient. Evidence for one claim is not reported as a result for
another (§1). The ladder is new law: it keeps a matching output, an analogy
or a passing conformance check from being read as equivalence or as
preserved structure (P1, P6).

Layered sufficiency. A specification arranged in layers is sufficient when
a competent actor can derive a conformant next layer from each layer; the
derivation need not be unique, since different realisations may satisfy the
same upper layer, and the test is sufficiency, not determinism. A failure
to derive at any boundary is a defect of the upper layer: unclear,
contradictory, underspecified, not concrete or decomposable enough, or
polluted with accidental lower-layer detail. A boundary that can be crossed
only by hiding a major unresolved ambiguity is not yet sufficient even if
some downstream artifact can be produced. For an already accepted relation,
reconstruction may reuse its exact current basis and sufficient evidence
after checking applicability and invalidation (ACTIVATION §7);
reconstructability requires a correct reconstruction route, not its
execution at every use, grants no restart authority and does not excuse
stale success. The claim determines the reconstruction span; a local
selected function does not require recreating the whole subject. New
material counterexamples still challenge the affected relation (P2, P1,
P0; conserves the
[Reconstruction Litmus](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#reconstruction-litmus),
whose application to the method's own chain, with the diagnosis per layer,
is SPEC_METHOD §2).

Comparison. After freeze the evaluator compares the frozen result against
the mandatory governing semantic basis for semantic conformance or
equivalence. A separately held expected or reference outcome, if one exists
and is applicable, is optional evidence and explicitly non-authoritative;
semantic equivalence to it is required only where the governing basis
requires it. A lawful alternative construction permitted by the basis
passes. Subjective similarity to the basis or the reference is insufficient
to establish conformance or equivalence. Byte or structural identity,
unique derivation, determinism and incumbent equality are not generic
comparison criteria. A construction outside the declared competence or
configuration envelope cannot indict generic method sufficiency (P6, P1;
conserves
[UP-022](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022)'s
comparison rule).

### Foundation to law: conformance, equivalence and qualification

This family, conformance, equivalence and qualification (F7 in the index of
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law)),
decides when a realisation, a frame or the method itself is shown fit for
what it claims. It covers §6 and §7 of this member and the
[CONFORMANCE](CONFORMANCE.md) member; a rule in CONFORMANCE is marked
"outside this member" in the third column. Its instance premises are: (a)
one specification may have several realisations; (b) realisations, frames
and the method are made by fallible constructors and relied on by actors
who did not make them; (c) qualification evidence comes from a finite set
of cases, run by actors inside declared envelopes. They are conditions of
the work this family governs, not commitments, and do not follow from
finite capacity alone. P0's actor-change premise, that the actor of one
step need not be the actor of the next and may re-acquire declared sources
but not private memory, is cited by name. The standing of the consequences
below is stated in
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law).

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P1 (independent), P6 (independent); instance premise a | By P1 behaviour has meaning only under an interpretation, and by P6 a judgment is separate from what it judges, so a realisation conforms to a specification when its interpreted behaviour satisfies it under a declared interpretation contract and an independent judgment. Several realisations may conform to one specification; sufficiency does not require unique derivation or equality with an incumbent. A specification that admits materially different behaviours either declares the latitude or is repaired before a decision-complete design is claimed | [§6](#6-conformance-of-realisations), first paragraph | the interpretation contract and any declared latitude: the owner of the specification ([FOUNDATIONS §4](FOUNDATIONS.md#4-algebra), Latitude) | 4, 6, 9 |
| P1 (independent), P6 (independent) | By P1 each kind of equivalence is a different relation between meanings and representations, and by P6 evidence supports only the claim it is for, so conformance, semantic equivalence, computational equivalence and categorical equivalence are separate claims with separate evidence, and no rung implies another. Conformance establishes neither identical behaviour outside the specification nor equal cost; a categorical equivalence claim meets the items of the Formal fragment that apply to it and adds a quasi-inverse functor and natural isomorphisms on a stated domain, and a map's preservation of identities and composition is a further claim. Evidence for one claim is never reported as a result for another | [§6](#6-conformance-of-realisations), Equivalence ladder | the four rungs and their definitions: this section; the stated domain, workloads and architecture H of an equivalence claim: the author of the claim; what a category or functor claim must show: [FOUNDATIONS §4](FOUNDATIONS.md#4-algebra), Formal fragment (family F3) | 3, 6, 9 |
| P2 (independent), P1 (independent), P0 (recovered); instance premises a, b | By P2 a layer exists so the next can be derived from it, by P1 one meaning admits several representations, and by P0 a reconstruction must fit a finite actor, so a layered specification is sufficient when a competent actor can derive a conformant next layer from each layer, not necessarily uniquely. A failure to derive is a defect of the upper layer, and a boundary that can be crossed only by hiding a major unresolved ambiguity is not sufficient. Reconstruction of an accepted relation may reuse its exact current basis and sufficient evidence after checking applicability and invalidation; reconstructability requires a correct route, not its execution at every use, grants no restart authority and does not excuse stale success; the claim determines the reconstruction span, and new material counterexamples still challenge the relation | [§6](#6-conformance-of-realisations), Layered sufficiency | the layers of the method's own chain and the diagnosis per layer: [SPEC_METHOD §2](SPEC_METHOD.md#reconstruction-litmus) (family F10) | 1, 4, 6 |
| P6 (independent), P1 (independent); instance premise b | By P6 the governing basis, not a reference outcome, decides, and by P1 equal representation is not equal meaning, so after freeze, the evaluator compares the frozen result with the mandatory governing semantic basis. A separately held expected or reference outcome is optional and non-authoritative evidence; a lawful alternative construction the basis permits passes. Subjective similarity is insufficient, and byte or structural identity, unique derivation, determinism and incumbent equality are not generic comparison criteria. A construction outside the declared competence or configuration envelope cannot indict generic method sufficiency | [§6](#6-conformance-of-realisations), Comparison | whether equivalence to a reference outcome is required: the governing basis | 6, 9 |
| P6 (independent), P2 (independent); instance premises b, c | By P6 a frame's claims hold only on evidence, and by P2 the evidence needed follows the claims made, so a candidate frame is qualified in proportion to its claims, by at least the decision, reconstruction, sensitivity, irrelevance, basis, authority, counterexample, capability and result-consumption tests. Qualification binds the exact frame revision, actor envelope, evaluation family, basis class and evidence conditions evaluated, and does not generalise to an unevaluated population by naming the frame generically | [Frame qualification](#frame-qualification), the tests and the paragraph after them | the nine minimum tests: this section; the representative cases for each claim: the qualification that evaluates it | 7, 9 |
| P0 (recovered), P6 (independent); instance premise c | By P0 fit is a property of the representation and the envelope, and by P6 attention is shown only by evidence of use, so fit and adequate attention are evaluated separately. Fit, for the context dimension, is the measured size of the selected representation against the declared capacity; adequate attention is established only by actual-use evidence, judged against expectations recorded from the governing sources before the results are opened. A size measurement or any byte or token threshold establishes fit and nothing about attention; actual-use evidence binds the frame revision, actor class, tasks and conditions evaluated and establishes no universal attention score | [Frame qualification](#frame-qualification), Adequate attention | the tasks and conditions evaluated: the qualification; the size measurement: [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) step 3 (family F1); time, spend and other resource limits: the selected execution binding, under [ACTIVATION §6](ACTIVATION.md#6-cost-and-proportionality) (family F5) | 7, 8, 9 |
| P6 (independent), P0 (recovered, with its actor-change premise), P1 (independent); instance premises b, c | By P6 and P0's actor-change premise the method's claims need the same evidence as any other and must survive a change of actor, and by P1 a constructor's private material is not the method, so the method is qualified the way it qualifies anything else, with no second process. A fresh competent constructor inside a declared envelope uses only the declared ordinary method and authority surfaces and declared trial subjects; an independently authorised evaluator has a declared governing basis and comparison predicate; expected or reference outcomes, source exemplars, incumbent realisations, author memory and ad hoc rescue are withheld from the constructor until its result is frozen wherever earlier exposure would compromise reconstructive independence; comparison follows §6. The qualification law is false under the falsifiers §7 lists | [Method self-qualification](#method-self-qualification), first paragraph and the falsifiers | the constructor, freeze, assessor, acceptance and release protocols: the governing authority | 1, 9 |
| P6 (independent); instance premise c | By P6 each claimed relation is a separate claim that needs its own evidence, so the qualification population is every function and failure relation the method claims, each with its representative observations. One valid frame-set declaration and coverage result establishes only `declare` and the evaluated `audit_coverage`, and the other relations by no implication; each relation is exercised through positive, boundary and falsifying cases; every verdict states exactly what it evaluated, and an unevaluated function or branch stays open rather than inheriting a whole-method verdict. Prior exemplars are optional comparison evidence after freeze | [Method self-qualification](#method-self-qualification), the population table and the paragraph after it | the relations: [REFERENCE_FRAME §5](REFERENCE_FRAME.md#5-method-functions) (family F1); the representative observations listed: this section; staging: the governing authority | 3, 9 |
| P6 (independent), P1 (independent); instance premise b | By P6 and P1 a derived guide is a representation whose fidelity is a separate claim, so changed derived guidance, such as a compression, a frame packet or a skill, is qualified against source-derived expected behaviour, including the affected permissions, exclusions and invalidators; a native use claim is shown by an ordinary actor applying it through its declared entry. Digest integrity and index generation establish identity and structure, not semantic fidelity or usability, and mechanical and operational claims require their own executable observations | [Method self-qualification](#method-self-qualification), Derived guidance | the applicable workload and operational assumptions: [ACTIVATION §6](ACTIVATION.md#6-cost-and-proportionality) (family F5) | 6, 9 |
| P0 (recovered, with its actor-change premise), P6 (independent); instance premise b | By P0's actor-change premise a document set must work for an actor without prior memory, and by P6 fidelity is judged on evidence, so for a selected activation, a fresh actor given only the published documents recovers the governing relations with fidelity judged independently, at a measured reconstruction cost. The fidelity judgment is actual-use evidence, and the size measured is not evidence of it. A document set that requires private validator knowledge, whole-corpus loading or a prior actor's memory fails, whatever its content | [Method self-qualification](#method-self-qualification), Recoverability benchmark | the rc.2 corpus as baseline, and the matrix criteria the benchmark reports for: this section; the activation measured: the qualification that runs it; time and spend measurement: the selected execution binding | 6, 7, 9 |
| P6 (independent), P5 (derived from P0 and P6, with P0's open-world premise); instance premise c | By P6 a pass is an assessor's verdict on evidence, and by P5 an evaluation not performed has no result, so a conformance case names its subject, the mechanism under test, an independently specified expected distinction and its status, and a status names what exists. A run is not a pass: only an assessment by an independent assessor records one. A case passes when the expected distinction is observed and no coerced success appears anywhere in the result; a case that cannot be run with its declared subject is a planned evaluation that was not performed, which has no result under [FOUNDATIONS §4 Results](FOUNDATIONS.md#results), so it is recorded as not run, never hidden and never given a core value | [CONFORMANCE](CONFORMANCE.md), preamble, outside this member | the cases, with their subjects and expected distinctions: CONFORMANCE, from the common conformance discriminators and the builder's history | 3, 9 |
| P0 (recovered), P6 (independent); instance premise c | By P0 an actor's context is bounded, and by P6 acceptance criteria must not come from the constructing actor, so a trial of bounded construction declares its per-actor context cap and total-work budget before each run, counts the context transferred across every delegated actor, and keeps its acceptance criteria independent of the constructing actor | [CONFORMANCE §2](CONFORMANCE.md#2-trials-from-the-comparative-baseline), the paragraph after the trial table, outside this member | a required basis larger than the cap, and repetition of probabilistic trials with varied task order: CONFORMANCE §2; each cap and budget: the trial's declaration; a policy of CONFORMANCE §2: that a trial declares its cap and budget before each run and counts context across every delegated actor | 8, 9 |

§8 records dispositions and decides nothing. CONFORMANCE §1 to §4 list the
cases, which are the choices named in the last two rows, its §5 maps the
common discriminators to cases and logical-review checks, and its §6
records dispositions.
```

### ACTIVATION §2 Context construction under an envelope (port 5, acquisition rule)

```markdown
Given a seed set Z (the subject, outcome and affected relations named in the
intake), a relation family R (the dependency relations whose change can
alter the result, basis validity, evidence sufficiency or authority), and
the actor's envelope B:

1. Compute the material closure of Z under R (AC-010,
   [AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-010-material-closure);
   provenance rc.2 AXIOMATIC_CALCULUS #ac-010-material-closure).
   If Z, R, the required-edge semantics, the basis or the scope is not
   exact, or the closure is not finite and unique on the exact basis,
   activation returns `closure_unresolved` (§3, Admission and activation)
   and no step proceeds; it does not guess.
2. Project the closure to the selected context, recording its boundary: the
   excluded, external, unresolved, translated and invalidation-sensitive
   seams (AC-011,
   [AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-011-projection);
   provenance rc.2 AXIOMATIC_CALCULUS #ac-011-projection).
   If the projection returns a gap or refusal, activation returns
   `closure_unresolved` and no step proceeds.
   Material not in the closure stays out; adjacent material does not enter
   because it exists
   ([RF-004](REFERENCE_FRAME.md#rf-004-irrelevance-exclusion)).
3. Test fit against B. This step owns the size measurement and the fit
   test for the context dimension. Where B declares a context capacity,
   the size of the selected context is measured before the actor reads it,
   in the unit the capacity is declared in (bytes or tokens) and over the
   boundary that the selected execution binding states for it (§6), and is
   compared with that capacity. The measurement, the capacity and the
   outcome of the comparison are recorded before the read. A fit holds
   only for the measured boundary: context outside it is recorded as not
   measured, and no fit claim covers it. The fit claim for a measured
   boundary and the step's fit judgment are distinct: the judgment is
   established from the recorded complete active inputs, or from a
   supported upper bound that includes any host-supplied context; where
   neither exists it is `indeterminate`, unless a counterexample, such as
   a measured excess, establishes `falsified`. A correct task result keeps
   its own bounded standing and does not satisfy a missing fit judgment
   (P0, P5; new law carried at iteration 4 from the common construction
   contract's Limits). The measurement applies wherever B declares a
   context capacity, whatever question the step governs, because without
   it a fit claim against that capacity is an assertion, and a context
   that exceeds it would be cut without record
   ([RF-014](REFERENCE_FRAME.md#rf-014-capability-fit)). It applies only
   there, because a resource control applies only through a selected frame
   and its owning scope
   ([REFERENCE_FRAME §4](REFERENCE_FRAME.md#frame-set-selection)), and a
   declared capacity is such a control: the measurement tests that
   capacity, is no budget, and is not a universal measurement gate (P0,
   P2). Where B declares no context capacity, no measurement is
   required, and the other conditions of
   [RF-002](REFERENCE_FRAME.md#rf-002-finite-attention) still apply. The size
   shows fit and nothing else: whether the actor attends adequately to a
   context that fits is decided by actual-use evidence under
   [EVALUATION §7](EVALUATION.md#frame-qualification). The envelope's
   other dimensions are fitted as RF-014 states; time, spend and other
   resource limits follow [§6 Resource limits](#resource-limits), which
   this step refines for the context dimension.
   If the context fits, activate. If it does not, one or more of these, in
   combination: refine the outer contract into steps whose contexts fit
   (§4); sequence activations; apply a lawful compression that preserves the material
   distinctions and failure detections the evaluation needs
   ([RF-017](REFERENCE_FRAME.md#rf-017-proportional-compression));
   select another actor whose envelope fits; or return `out_of_frame`
   ([§3 Admission and activation](#admission-and-activation)). Silent
   omission to fit is never one of them
   ([RF-014](REFERENCE_FRAME.md#rf-014-capability-fit)).
   None of these options silently reduces the required predicate: the
   obligations the step preserves stay bound
   ([§1 Transitions](#transitions)), a narrowing of them is a destination
   change under its owning authority (§1, Destination change), and what
   the selected context leaves undecided stays an explicit unknown.
   Within its grant a step selects refinement, sequencing and compression
   itself; selecting another actor or enlarging the envelope re-enters the
   owner of the grant or envelope, who may delegate that choice in the grant
   (RF-014 vests the selection in human authority; a grant is that authority
   exercised in advance). Whether a compression preserved what the
   evaluation needs is a claim with the standing of any other (EVALUATION
   §1): the compressing step records the compression and its preservation
   argument, and the claim is assessed independently only where the
   promotion it serves needs independent assessment (EVALUATION §3).
4. Acquire declared inputs by their exact identity. A declared input absent
   from the actor's materialised view is neither licence to read elsewhere
   nor evidence that it is absent.

Acquisition. Acquisition is the read-only observation of the material a
step needs (its frame, its subject and its declared inputs) within the
inputs its intake permits it to acquire (§1 Intake). It is not an admission and not a further
actor stage; effectful work still needs its admitted contract (§1
Admission), and acquiring material grants no role, operation or decision
([FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority). A derived surface is material derived from owning
sources by copying, projection or compression, such as a projected frame
for a task; it names its sources and owns no determination. Where a
current interpretation of the subject in `a_c` exists, the constraint
surface it yields for the task is such a derived surface, under the
conditions of
[AXIOMATIC_CALCULUS §9 Constraint surfaces](AXIOMATIC_CALCULUS.md#constraint-surfaces).
Where a derived surface whose sources
are current serves the task, the actor acquires it. For another task, or
where the derived surface is stale ([Staleness of derived surfaces](#staleness-of-derived-surfaces)),
missing or insufficient for a named unresolved question, the actor acquires the deciding owner sections
directly: the owning sections that decide the task's questions, which are
declared inputs of the selected basis. Only material in the exact selected
basis is acquired: where that basis has no derived surface for the task,
its exact owner sections are used, and a candidate source, a version-line
selector or another basis is no substitute for it
([FOUNDATIONS §2 Product lineage objects](FOUNDATIONS.md#product-lineage-objects)).
The actor reads the selected material and the actual subject, and follows
the material source and coupled-obligation references the task needs
(step 2; [RF-003](REFERENCE_FRAME.md#rf-003-material-sufficiency));
presence of the corpus is no reason to read it (step 2;
[RF-004](REFERENCE_FRAME.md#rf-004-irrelevance-exclusion)). No frame,
derived surface or acquisition carries a universal sufficiency claim:
sufficiency is decided for the named question against the task's
material relations, never for the corpus or the frame as a whole
([RF-003](REFERENCE_FRAME.md#rf-003-material-sufficiency)). Before any dependent action, a missing binding is returned with
its outcome of [§3 Admission and activation](#admission-and-activation),
naming what is missing: where no available frame declares what the
evaluation needs, `out_of_frame`; where the basis the step requires is
absent, or cannot be verified as the exact basis named, the basis cannot
support the step, and the outcome is `admission_refused(basis)` at
admission or `activation_refusal(basis)` at activation. Coupled material that does not fit is handled under
step 3 (P0, P6, P3).

Activation. The actor or the assigning authority selects one frame or one
declared active frame configuration capable of the evaluation. Activation
binds each reusable frame declaration to the exact subject and basis and
loads the declared material relations and evidence sources, never an
undifferentiated workspace dump; what the actor receives is the packet of
REFERENCE_FRAME §11. When no available frame and actor pairing can lawfully
perform the evaluation, activation returns `out_of_frame` where no such
pairing declares a material relation or capability the evaluation needs,
and otherwise the `activation_refusal` whose cause holds
([REFERENCE_FRAME §5](REFERENCE_FRAME.md#5-method-functions)); both are
outcomes of §3 Admission and activation. Work does not proceed through
implied context (P0, P5; rc.2 RF #select-and-activate).

Evaluation. The evaluator applies the activated frame's declared
invariants, evidence rules and result algebra. It distinguishes semantic
law, observed evidence, inference and decision, and records every
assumption whose failure could change the result (P6; rc.2 RF #evaluate).

Standalone scope. A derived surface or projected frame decides standalone
only the questions that its own source members own. It refuses to close a
question owned by another member, or one that joins the law of several
owners; the evaluation of that question returns `out_of_frame`
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)) naming the owning
members, and
the question is decided from those members at their current digests or
from a derived surface whose declared sources include every owner of it
(P6, P1; provenance rc.2 authority_compressions/stdo_compressed.md,
spec_method.compressed.md and design_module_method.compressed.md, a claim
no rc.2 body states).

Prompt construction. A prompt is rendered contract over typed authority;
it is not source law. Prompt text must project the current authority
references, obligations, contracts, boundaries, proof expectations and
fallback conditions the step needs. A prompt body must not carry
historical workaround prose unless the current requirement, design,
runtime or test still needs that constraint. Construction starts from the
highest live authority surface the question needs. If the prompt needs an
upstream ambiguity resolved, it names the unresolved authority gap before
fallback context is read. The prompt projects the material that
Acquisition above selects, including the raw owning members where
Acquisition falls back to them (P6, P0, P5; provenance rc.2
authority_compressions/stdo_compressed.md and spec_method.compressed.md, a
claim no rc.2 body states). The design, ODD, UX and ticket
specialisations are
[DESIGN_MODULE §11](DESIGN_MODULE.md#11-review),
[ODD §11.5D](ODD.md#115d-constructive-evaluation-and-yield-loop) A5 and
[§11.7A](ODD.md#117a-conforming-agentic-development),
[UX §7](UX.md#7-carrier-binding) and
[TICKETS §5](TICKETS.md#5-from-carrier-to-execution) and
[§7](TICKETS.md#7-authority-judgment-closure-and-state) (P6).

The operation that joins AC-010, AC-011 and RF-002, RF-003, RF-004,
RF-014 and RF-017 into one procedure is new in this corpus (P0); each of
those laws is applied here from its successor section in
[AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-010-material-closure) and
[REFERENCE_FRAME §3](REFERENCE_FRAME.md#3-laws), and a `stdo://` route in
this section is provenance only. The method does not require proving
that no undiscovered material relation exists
([RF-003](REFERENCE_FRAME.md#rf-003-material-sufficiency)).
The size measurement of step 3, with the condition under which it
applies, and Acquisition are also new. Purpose and material relation:
finite context makes fit necessary (P0), so a fit against a declared
capacity is measured rather than asserted, while fit and attention stay
separate claims (P6); and an actor without a derived surface for its task
still reaches the sections that decide it, from the exact basis, without
reading the corpus or substituting a stale or mutable copy (P3, P6). The
material relation is whether a context larger than the declared capacity
is read as if it fit, a fit is taken as adequate attention, or a decision
rests on material other than its deciding owners at the selected basis.

### Staleness of derived surfaces

This subsection owns when a derived surface (Acquisition above) is current
and when it is stale, for any method and any carrier (P3, P5, P6):

- A derived surface names the exact identity, such as the path and
  digest, of each source it was derived from and of each source whose
  change can change its content.
- It is current for a selected basis only while every source identity it
  names equals the identity of that source in the selected basis. A change
  to any of them makes it stale.
- A stale derived surface is not used as current for any question. It
  becomes current again only by regeneration from the sources at the
  selected basis, or by an explicit re-acceptance that records the new
  source identities and the finding that its content still matches them;
  until then the actor acquires the deciding owner sections directly
  (Acquisition above).
- Matching source identities establish only that the surface was derived
  from those sources. They establish neither its fidelity to them nor its
  sufficiency for a question; a surface found insufficient for a named
  question is handled as Acquisition above states.
- The owning sections at the selected basis remain the deciding source.
  Whether a current surface is insufficient for a question, or decides
  beyond its own sources, is judged against them (Standalone scope above);
  a derived surface never decides that about itself.

A packaging or installation carrier refines this rule with its own
identities and re-acceptance procedure, and names this subsection as its
owner; [PRODUCT_DEFINITION §11](PRODUCT_DEFINITION.md#11-one-constitutional-surface-and-version-boundary)
does so for the method's released carriers. Provenance: rc.2
authority_compressions/README.md and stdo_bootstrap.md step 5, a claim no
rc.2 body states. Purpose and material relation: an actor that relies on a
derived surface after one of its sources has changed decides from material
that no longer matches its owners, and a matching digest read as fidelity
would let a faithful-looking but wrong surface decide; the material
relation is whether a decision rests on a surface whose sources are not
those of the selected basis. This rule is new in tier 1; it was stated
only for packaging carriers before.
```

### FOUNDATIONS §3 Foundation to law (port 1)

```markdown
A family of deciding rules is a group of related rules that decide
outcomes; it is a material family when the outcomes it decides matter to
the method's selected outcome (P2). Each material family is traced in one
family table. The table sits in the member that owns the family, at the
section where an actor enters the family, so the actor meets the trace
where it applies the rules (P2, P6). A family table first states its
instance premises: the conditions of the situations the family governs,
which the commitments do not supply. They are labelled as instance
premises, never as commitments. The table then has one row per
consequence, in five columns:

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|

- Premises, with standing: the commitments the row rests on, each with its
  standing from the table of commitments above, and the instance premises
  it uses. A profile's table also names the families it imports, under
  [PROFILES §1](PROFILES.md#1-the-boundary).
- Consequence that follows: what those premises together require of the
  family.
- Rule in this member that states it: the owning section or clause,
  linked. Where a table accounts for a section of another member, this
  column names that section, linked and marked as outside this member, or
  a paragraph after the table names the sections of other members that
  apply its rows; the section keeps its owner.
- Added domain or policy choice, and its owner: what the rule decides that
  the premises leave open, with the member, profile, adopting Product (a
  Product that applies this method) or authority that owns it, or "none".
  A row never files the whole rule as the choice: the choice is only what
  the premises leave open.
- Pillar: the pillar contributions the row helps account for, by number.
  The pillars are the ten contributions that the Foundational Reduction of
  the Product that owns this corpus names, in its order: 1 specification
  and project structure; 2 world models, identity and Markov objects; 3
  algebraic calculus; 4 functional design; 5 outcome-driven development; 6
  information and interpretation; 7 reference frames; 8 computational
  calculus and execution binding; 9 evidence, correction and authority; 10
  axiomatic calculus. That Product owns the contributions and their
  wording. A Pillar cell is a trace, like the rest of the table: it is not
  a premise, adds no standing to the row, owns no choice, and does not
  claim that a pillar is an axiom or follows from finite capacity.

A family table is a trace. Its consequence and choice columns state no
determination that the rule it names does not state, and the table owns
none of the rules or choices it lists (P1, P6).

Standing of the consequences. The consequences are arguments from the
stated premises, not proofs of every clause of the rules they name.
Concrete carrier layouts, the number of actors, numeric limits, adoption
of an optional profile, release procedures and the values of each
refinement are added choices. They are not inferred from the foundational
commitments. Each table leaves those choices at their owners and adds no
record that its rules do not require. Tables over some members are not a
derivation of every member: the index below accounts for every member, by
the table that traces it, by a row marked table pending, or by the reason
it has none. Each family table refers here for the standing of its
consequences and does not restate it (P6, P2).

Index of families. Each row names a family, the section that holds its
table, the members or sections the table accounts for, and the pillar
contributions its table's rows name, which are the union of its rows'
Pillar cells. A row marked table pending names the section that is to
hold its table; until that table is written, the row names its members
and traces none of their rules. A Pillar cell marked pending names no
pillar: the family's table does not yet carry the Pillar column, and the
cell is filled from that table's rows when it does. The index decides
nothing: each rule is in its owning section, and each trace is in its
table (P1, P6).

| ID | Family | Table | Accounts for | Pillar |
|---|---|---|---|---|
| F1 | Frames and context | [REFERENCE_FRAME §1](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit) | REFERENCE_FRAME; ACTIVATION §2; FOUNDATIONS §2 Frame objects, Authority kinds, Disjointness and independence, The frame tuple | 1–9 |
| F2 | Transitions, steps and configuration | [ACTIVATION §1](ACTIVATION.md#1-the-step) | ACTIVATION §1, §4; SPEC_METHOD §8 except delivery priority | 1, 3, 4, 5, 6, 7, 9 |
| F3 | Results and their combination | [FOUNDATIONS §4 Results](#results) | FOUNDATIONS §4, and the result grounds of §2 Imports between members; ACTIVATION §3; RF-012; AC-007; EVALUATION §4 | 3, 4, 6, 7, 9 |
| F4 | Work state, resumption and reuse | [ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart) | ACTIVATION §5, §7 | 2, 4, 5, 6, 7, 9 |
| F5 | Proportionality and cost | [ACTIVATION §6](ACTIVATION.md#6-cost-and-proportionality) | ACTIVATION §6; SPEC_METHOD §8 delivery priority | 1, 4, 5, 6, 7, 8, 9 |
| F6 | Claims, evidence, assessment and acceptance | [EVALUATION §1](EVALUATION.md#1-claims) | EVALUATION §1 to §5 | 1, 2, 3, 6, 7, 8, 9 |
| F7 | Conformance, equivalence and qualification | [EVALUATION §6](EVALUATION.md#6-conformance-of-realisations) | EVALUATION §6, §7; CONFORMANCE | 1, 3, 4, 6, 7, 8, 9 |
| F8 | Identity | [IDENTITY §1](IDENTITY.md#1-position) | IDENTITY | 1, 2, 6, 7, 8, 9 |
| F9 | The a_c calculus | [AXIOMATIC_CALCULUS §1](AXIOMATIC_CALCULUS.md#1-position) | AXIOMATIC_CALCULUS | 1, 2, 3, 4, 6, 7, 8, 9, 10 |
| F10 | Constitutional chain, outcome and build-tenant binding | [SPEC_METHOD §2](SPEC_METHOD.md#2-the-chain) | SPEC_METHOD §1 to §3, §6, §9 to §11 | 1, 2, 3, 4, 5, 6, 8, 9 |
| F11 | Change management and ambiguity | [SPEC_METHOD §4](SPEC_METHOD.md#4-change-management) | SPEC_METHOD §4, §5, §7 | 1, 2, 3, 4, 5, 6, 7, 9 |
| F12 | Binding a project to the method | [PRODUCT_DEFINITION §1](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence) | PRODUCT_DEFINITION; FOUNDATIONS §2 Imports between members except its result grounds (F3) | 1, 2, 4, 6, 7, 8, 9 |
| F13 | Work carriers | [TICKETS §5](TICKETS.md#5-from-carrier-to-execution) | TICKETS; POSTING_GUIDE §2, §7, §9 | 1, 2, 3, 4, 6, 7, 8, 9 |
| F14 | Assurance and testing | [ASSURANCE §1](ASSURANCE.md#1-verification-layers) | ASSURANCE | 1, 3, 4, 5, 6, 7, 8, 9 |
| F15 | Release and successor conservation | [RELEASE §1](RELEASE.md#1-context-and-position) | RELEASE; FOUNDATIONS §2 Product lineage objects | 1, 2, 3, 6, 7, 8, 9 |
| F16 | Engagement baseline (operational profile) | [EXECUTIVE_BASELINE §3](EXECUTIVE_BASELINE.md#3-engagement-applicability) | EXECUTIVE_BASELINE | 1–9 |
| F17 | Software design | [DESIGN_MODULE §1](DESIGN_MODULE.md#1-purpose-and-position) | DESIGN_MODULE | 1, 2, 3, 4, 5, 6, 7, 9 |
| F18 | Outcome-driven development | [ODD §1](ODD.md#1-position) | ODD | 1–9 |
| F19 | Traversal occurrence | [TRAVERSAL_OCCURRENCE, Position](TRAVERSAL_OCCURRENCE.md#position) | TRAVERSAL_OCCURRENCE | 1, 2, 3, 4, 6, 7, 8, 9, 10 |
| F20 | UX | [UX §1](UX.md#1-position) | UX | 1–9 |
| F21 | World model | [WORLD_MODEL §1](WORLD_MODEL.md#1-position) | WORLD_MODEL | 1, 2, 3, 5, 6, 8, 9, 10 |

Members and sections with no family table, each with its reason:

- FOUNDATIONS §1, the ontology table of §2, and §3: they state the
  vocabulary of standing, the objects the commitments are about, and the
  commitments themselves with this format, which every family table cites
  as its premises. §2 Work boundary is the object that P0's boundary
  commitment states. §2 Accounts of a construction states a distinction
  and decides no outcome of its own; family F10 traces its use at
  SPEC_METHOD §11. FOUNDATIONS §5: its hypotheses are not law and decide
  no outcome.
- PROFILES: §1 owns the family-import rule, which families a profile imports and how a row cites them under the import rule of §2, that every profile table cites in its
  premise column; §2 to §6 index the profiles, whose own tables trace
  their bindings.
- POSTING_GUIDE and WRITING_GUIDE: their conventions are policy choices
  whose owner is the guide.
- GLOSSARY: a locator index; it decides nothing.
- The standards README and the other packaging (templates, schemas and
  plugin files): they own no determination.
- The source-dispositions section of every member: it records where each
  predecessor claim is carried and decides no outcome of the method.

Purpose and material relation of the family table and its format,
instance premises, the standing of the consequences and this index: for
every member, a reader can see which commitments its rules
rest on and which choices they add, with their owners, so no added choice
is presented as following from the foundations, no consequence is filed
as a choice, and no partial trace is presented as a derivation of the
whole method (P6, P2). The Pillar column binds each argument to the
contributions it helps account for, so a contribution that no row names
is visible as unaccounted (P2).
```

### FOUNDATIONS §3 Commitments (port 2)

```markdown
Each commitment has exactly one standing, in the terms §1 defines; the
table states it, with a distinction the commitment retains. The adopted
premises, which §1 identifies as the recovered and independent
commitments, are commitments adopted for the domain this method governs,
not theorems derived from finite capacity alone, that is, from the bound
on an actor's envelope (P0). Particular method rules need these premises
plus their stated domain and policy choices, each with its owner
([Foundation to law](#foundation-to-law)). An argument from the premises
preserves that distinction; it does not create authority (P6). Purpose
and material relation of this paragraph and the standing column: each
commitment shows what grounds it, so no premise is presented as derived
and no consequence is taken for a premise (P6).

| Commitment | Standing | Distinction retained |
|---|---|---|
| P0 Bounded construction | recovered | the actor's internal path within a step is its own |
| P1 Interpretation | independent | structural success never establishes fidelity |
| P2 Purpose | independent | an obligation with no route to the outcome is unjustified |
| P3 Identity | independent | current state, historical observation and representation identity stay separate |
| P4a Typed composition | independent | composition retains both identities, intermediate results, judgments, evidence, authority, provenance and stop states |
| P4b Conservation of step-produced facts | derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable | sources a later step can re-acquire are governed by sufficiency, not conservation |
| P5 Totality | derived from P0 and P6, with P0's open-world premise | a step cannot report success on a condition outside its context |
| P6 Justification and authority | independent | neither evidence nor authority is minted by the other |

P0 Bounded construction. A finite actor realises a selected outer contract
through steps. Each step's selected context fits the actor's envelope.
Sources, named as sources and not as proof (§1): finite attention within a
declared envelope ([RF-002](REFERENCE_FRAME.md#rf-002-finite-attention)),
material sufficiency ([RF-003](REFERENCE_FRAME.md#rf-003-material-sufficiency)),
material closure ([AC-010](AXIOMATIC_CALCULUS.md#ac-010-material-closure)),
the [work boundary](#work-boundary), and the refinement of one outer
contract into inner steps
([ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement), Refinement).
Premises: a selected outcome (P2); the actor of one step need not be the
actor of the next and may re-acquire declared sources but not private
memory; step-produced facts are not re-acquirable; the world is open; a
step's output is a candidate until evaluated.

P0's boundary commitment (the work boundary of §2): deterministic checks
and validation are evidence surfaces; they may optimise or prove a
domain-local path where the domain can make part of the work precise, and
they do not authorise the method, a runtime or a framework to absorb domain
solution strategy as constitutional law. Any unconstrained part of a
probabilistic worker's reasoning remains hidden worker-internal activity
and is forced back through the declared contracts, evidence, provenance and
control truth of the boundary. A framework layer that prescribes domain
solution strategy beyond the declared work contract and control truth has
crossed its authority boundary (P6). A profile may bind the unit to its own
traversal unit, in which that traversal is the admissible external space;
PROFILES §2 keeps that binding.

P1 Interpretation. Subject, representation and interpretation are distinct;
meaning holds within a declared context through a declared contract.
Non-entailment: let two steps fit their envelopes under one selected
outcome, keep declared identities, compose because the first's declared
result type, a length, meets the second's declared domain, record their
step-produced facts, return closed results and keep evidence apart from
authority, while the second reads the value under a contract no one
declares, in metres where the first wrote feet; P0 and P2 to P6 hold, yet
one representation has two meanings and no declared contract, which P1
forbids. "Algorithmic" means
explicit and structurally checkable; a semantic decision is lawful only
under an exact decision contract. Conserves
[AC-017](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity),
[AC-018](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation),
[AC-019](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-019-valid-model),
[RF-008](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse).

P2 Purpose. A selected outcome defines adequacy; interfaces inherit
material obligations from the transformation they serve. Non-entailment:
let a finite actor realise a selected outer contract that names an
outcome, through steps that fit its envelope, read under declared
contracts, keep declared identities, compose by type, record their
step-produced facts, return closed results and keep evidence apart from
authority, while each interface's obligations are set by the capacity
available and not inherited from the transformation it serves; P0, P1 and
P3 to P6 hold, yet the same obligations count as adequate for opposite
outcomes and an obligation with no route to the outcome stands, which P2
forbids. Conserves UP-013,
[UP-014](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014),
[UP-005](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005).

P3 Identity. An object's identity is declared (authority, kind, value) and
survives admissible change; a boundary is a claim with a proof obligation.
Non-entailment: let steps fit their envelopes under one selected outcome,
read under declared contracts, compose by type, record their
step-produced facts, return closed results and keep evidence apart from
authority, while each object's identity is taken from the place that
stores it and no authority, kind or value is declared, so an admissible
move makes one object two; P0 to P2 and P4a to P6 hold, yet identity is
neither declared nor kept across admissible change, which P3 forbids.
Conserves AC-002, AC-014, the
[recursive Product taxonomy](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#recursive-product-taxonomy),
[Entity Cut Construction Law](stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md#entity-cut-construction-law),
restated in [WORLD_MODEL §9](WORLD_MODEL.md#9-entity-cut-construction).

P4a Typed composition. Two steps compose only when the first's result type
and judgment satisfy the second's exact declared domain and preconditions.
Non-entailment: let a second step run on every output of the first, read it
under its own declared contract and return `invalid_basis` where the output
lies outside its declared domain, and let the composite keep only the
step-produced facts the outer contract needs. Each step fits its envelope and serves the selected
outcome, identities are declared and kept, the needed facts are recorded,
every result is closed and authority stays with its owners, so P0 to P3,
P4b, P5 and P6 hold. Yet the steps compose although the first's result type
need not meet the second's declared domain, and the first step's other
intermediate results and stop state are lost; P4a forbids both. The
retention has its own route to the outcome: when the composite is later
falsified or must be resumed, the kept intermediate results and stop state
locate the step to repair or restart, which a record of what the outer
contract needs does not supply (P2). Conserves
[AC-016](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-016-typed-composition),
[RF-010](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand).

P4b Conservation of step-produced facts. Judgments, residuals, observations
and authority decisions the outer contract needs are recorded by the step
that produced them. The outer contract needs these facts (P2); the next
actor may re-acquire declared sources but not the producing step's private
result, because step-produced facts are not re-acquirable (P0); so only the
producing step can record them. Reframed from
[AC-009](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-009-residual-conservation),
[AC-013](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-013-transformation),
[AC-005](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-005-authority-conservation),
[UP-017](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017),
[UP-021](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021),
whose nine statements of conservation become one obligation with typed
instances (authority, residual, judgment, frame, transition, successor
claim, evidence by reference); each is restated for its own scope by the
member §6 names.

P5 Totality. A step can meet a condition outside its context (P0's
open-world premise), and it cannot report success on one (P6). Its result
algebra therefore carries first-class outcomes other than success for such
a condition, and its control model names the next move. That these
outcomes are three, indeterminate, out_of_frame and invalid_basis, is a
declared choice conserved from RF-012, whose owner is §4
[Results](#results) (family F3, first row). Conserves
[RF-012](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-012-closed-results),
[RF-014](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-014-capability-fit),
[AC-007](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal),
[Totality Rule](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#8-totality-rule);
RF-012 and AC-007 are restated once in §4 [Results](#results), and are
stated as laws in
[REFERENCE_FRAME §3](REFERENCE_FRAME.md#rf-012-closed-results) and
[AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal).

P6 Justification and authority. Definitions, assumptions, observations,
candidate judgments and accepted claims have distinct standing; evidence
supports a claim on a basis; authority permits or disposes within scope.
Non-entailment: a bounded actor satisfying all else can still take a green
label as acceptance. Conserves UP-001,
[UP-008](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008),
[UP-022](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022),
UP-004 ([IDENTITY §6](IDENTITY.md#6-authority-identity-and-conservation-stdo-up-004)),
[RF-006](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation),
[RF-007](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation).

### Foundation to law

A family of deciding rules is a group of related rules that decide
outcomes; it is a material family when the outcomes it decides matter to
the method's selected outcome (P2). Each material family is traced in one
family table. The table sits in the member that owns the family, at the
section where an actor enters the family, so the actor meets the trace
where it applies the rules (P2, P6). A family table first states its
instance premises: the conditions of the situations the family governs,
which the commitments do not supply. They are labelled as instance
premises, never as commitments. The table then has one row per
consequence, in five columns:

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|

- Premises, with standing: the commitments the row rests on, each with its
  standing from the table of commitments above, and the instance premises
  it uses. A profile's table also names the families it imports, under
  [PROFILES §1](PROFILES.md#1-the-boundary).
- Consequence that follows: what those premises together require of the
  family.
- Rule in this member that states it: the owning section or clause,
  linked. Where a table accounts for a section of another member, this
  column names that section, linked and marked as outside this member, or
  a paragraph after the table names the sections of other members that
  apply its rows; the section keeps its owner.
- Added domain or policy choice, and its owner: what the rule decides that
  the premises leave open, with the member, profile, adopting Product (a
  Product that applies this method) or authority that owns it, or "none".
  A row never files the whole rule as the choice: the choice is only what
  the premises leave open.
- Pillar: the pillar contributions the row helps account for, by number.
  The pillars are the ten contributions that the Foundational Reduction of
  the Product that owns this corpus names, in its order: 1 specification
  and project structure; 2 world models, identity and Markov objects; 3
  algebraic calculus; 4 functional design; 5 outcome-driven development; 6
  information and interpretation; 7 reference frames; 8 computational
  calculus and execution binding; 9 evidence, correction and authority; 10
  axiomatic calculus. That Product owns the contributions and their
  wording. A Pillar cell is a trace, like the rest of the table: it is not
  a premise, adds no standing to the row, owns no choice, and does not
  claim that a pillar is an axiom or follows from finite capacity.

A family table is a trace. Its consequence and choice columns state no
determination that the rule it names does not state, and the table owns
none of the rules or choices it lists (P1, P6).

Standing of the consequences. The consequences are arguments from the
stated premises, not proofs of every clause of the rules they name.
Concrete carrier layouts, the number of actors, numeric limits, adoption
of an optional profile, release procedures and the values of each
refinement are added choices. They are not inferred from the foundational
commitments. Each table leaves those choices at their owners and adds no
record that its rules do not require. Tables over some members are not a
derivation of every member: the index below accounts for every member, by
the table that traces it, by a row marked table pending, or by the reason
it has none. Each family table refers here for the standing of its
consequences and does not restate it (P6, P2).

Index of families. Each row names a family, the section that holds its
table, the members or sections the table accounts for, and the pillar
contributions its table's rows name, which are the union of its rows'
Pillar cells. A row marked table pending names the section that is to
hold its table; until that table is written, the row names its members
and traces none of their rules. A Pillar cell marked pending names no
pillar: the family's table does not yet carry the Pillar column, and the
cell is filled from that table's rows when it does. The index decides
nothing: each rule is in its owning section, and each trace is in its
table (P1, P6).

| ID | Family | Table | Accounts for | Pillar |
|---|---|---|---|---|
| F1 | Frames and context | [REFERENCE_FRAME §1](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit) | REFERENCE_FRAME; ACTIVATION §2; FOUNDATIONS §2 Frame objects, Authority kinds, Disjointness and independence, The frame tuple | 1–9 |
| F2 | Transitions, steps and configuration | [ACTIVATION §1](ACTIVATION.md#1-the-step) | ACTIVATION §1, §4; SPEC_METHOD §8 except delivery priority | 1, 3, 4, 5, 6, 7, 9 |
| F3 | Results and their combination | [FOUNDATIONS §4 Results](#results) | FOUNDATIONS §4, and the result grounds of §2 Imports between members; ACTIVATION §3; RF-012; AC-007; EVALUATION §4 | 3, 4, 6, 7, 9 |
| F4 | Work state, resumption and reuse | [ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart) | ACTIVATION §5, §7 | 2, 4, 5, 6, 7, 9 |
| F5 | Proportionality and cost | [ACTIVATION §6](ACTIVATION.md#6-cost-and-proportionality) | ACTIVATION §6; SPEC_METHOD §8 delivery priority | 1, 4, 5, 6, 7, 8, 9 |
| F6 | Claims, evidence, assessment and acceptance | [EVALUATION §1](EVALUATION.md#1-claims) | EVALUATION §1 to §5 | 1, 2, 3, 6, 7, 8, 9 |
| F7 | Conformance, equivalence and qualification | [EVALUATION §6](EVALUATION.md#6-conformance-of-realisations) | EVALUATION §6, §7; CONFORMANCE | 1, 3, 4, 6, 7, 8, 9 |
| F8 | Identity | [IDENTITY §1](IDENTITY.md#1-position) | IDENTITY | 1, 2, 6, 7, 8, 9 |
| F9 | The a_c calculus | [AXIOMATIC_CALCULUS §1](AXIOMATIC_CALCULUS.md#1-position) | AXIOMATIC_CALCULUS | 1, 2, 3, 4, 6, 7, 8, 9, 10 |
| F10 | Constitutional chain, outcome and build-tenant binding | [SPEC_METHOD §2](SPEC_METHOD.md#2-the-chain) | SPEC_METHOD §1 to §3, §6, §9 to §11 | 1, 2, 3, 4, 5, 6, 8, 9 |
| F11 | Change management and ambiguity | [SPEC_METHOD §4](SPEC_METHOD.md#4-change-management) | SPEC_METHOD §4, §5, §7 | 1, 2, 3, 4, 5, 6, 7, 9 |
| F12 | Binding a project to the method | [PRODUCT_DEFINITION §1](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence) | PRODUCT_DEFINITION; FOUNDATIONS §2 Imports between members except its result grounds (F3) | 1, 2, 4, 6, 7, 8, 9 |
| F13 | Work carriers | [TICKETS §5](TICKETS.md#5-from-carrier-to-execution) | TICKETS; POSTING_GUIDE §2, §7, §9 | 1, 2, 3, 4, 6, 7, 8, 9 |
| F14 | Assurance and testing | [ASSURANCE §1](ASSURANCE.md#1-verification-layers) | ASSURANCE | 1, 3, 4, 5, 6, 7, 8, 9 |
| F15 | Release and successor conservation | [RELEASE §1](RELEASE.md#1-context-and-position) | RELEASE; FOUNDATIONS §2 Product lineage objects | 1, 2, 3, 6, 7, 8, 9 |
| F16 | Engagement baseline (operational profile) | [EXECUTIVE_BASELINE §3](EXECUTIVE_BASELINE.md#3-engagement-applicability) | EXECUTIVE_BASELINE | 1–9 |
| F17 | Software design | [DESIGN_MODULE §1](DESIGN_MODULE.md#1-purpose-and-position) | DESIGN_MODULE | 1, 2, 3, 4, 5, 6, 7, 9 |
| F18 | Outcome-driven development | [ODD §1](ODD.md#1-position) | ODD | 1–9 |
| F19 | Traversal occurrence | [TRAVERSAL_OCCURRENCE, Position](TRAVERSAL_OCCURRENCE.md#position) | TRAVERSAL_OCCURRENCE | 1, 2, 3, 4, 6, 7, 8, 9, 10 |
| F20 | UX | [UX §1](UX.md#1-position) | UX | 1–9 |
| F21 | World model | [WORLD_MODEL §1](WORLD_MODEL.md#1-position) | WORLD_MODEL | 1, 2, 3, 5, 6, 8, 9, 10 |

Members and sections with no family table, each with its reason:

- FOUNDATIONS §1, the ontology table of §2, and §3: they state the
  vocabulary of standing, the objects the commitments are about, and the
  commitments themselves with this format, which every family table cites
  as its premises. §2 Work boundary is the object that P0's boundary
  commitment states. §2 Accounts of a construction states a distinction
  and decides no outcome of its own; family F10 traces its use at
  SPEC_METHOD §11. FOUNDATIONS §5: its hypotheses are not law and decide
  no outcome.
- PROFILES: §1 owns the family-import rule, which families a profile imports and how a row cites them under the import rule of §2, that every profile table cites in its
  premise column; §2 to §6 index the profiles, whose own tables trace
  their bindings.
- POSTING_GUIDE and WRITING_GUIDE: their conventions are policy choices
  whose owner is the guide.
- GLOSSARY: a locator index; it decides nothing.
- The standards README and the other packaging (templates, schemas and
  plugin files): they own no determination.
- The source-dispositions section of every member: it records where each
  predecessor claim is carried and decides no outcome of the method.

Purpose and material relation of the family table and its format,
instance premises, the standing of the consequences and this index: for
every member, a reader can see which commitments its rules
rest on and which choices they add, with their owners, so no added choice
is presented as following from the foundations, no consequence is filed
as a choice, and no partial trace is presented as a derivation of the
whole method (P6, P2). The Pillar column binds each argument to the
contributions it helps account for, so a contribution that no row names
is visible as unaccounted (P2).
```

### FOUNDATIONS §3, the PROFILES line (R2b-05)

```text
  no outcome.
- PROFILES: §1 owns the family-import rule, which families a profile imports and how a row cites them under the import rule of §2, that every profile table cites in its
  premise column; §2 to §6 index the profiles, whose own tables trace
```

### The frame generator, docstring and header (port 5, R2b-07, R2a-05)

```python
#!/usr/bin/env python3
"""Generate reference frames copied from owning sections; confers no acceptance.

Reads the frame specifications in standards/frames/FRAME_INPUTS.json (frame
id, task, scope, ordered owner#anchor routes). For each route it extracts the
owning section byte for byte, rebases its relative link destinations (Link
rebasing below), prefixes it with a `Source:` line naming the member, the
anchor and the SHA-256 of the whole owning member, and writes
standards/frames/<id>.md with a short header (task, purpose, routes, measured
size). It records owner_sha256, section_sha256, the frame's bytes and sha256
back into FRAME_INPUTS.json. Regeneration from the same inputs is
byte-identical; a changed member changes the recorded digests.

Section rule (design/CROSS_SYNTHESIS.md, part 5, requirements 1 to 4):
- one heading-slug rule, `slug` below, copied from the Codex generator;
- a fenced code block opens at a line of three or more backticks or tildes
  indented by at most three spaces and closes only at a line of the same
  character at least as long; no line inside it is a heading;
- a heading is `#` to `######` and a space, at column 0, outside fenced
  blocks; a section ends at the next heading of equal or higher level, or
  at the end of the member;
- the section digest is over the exact bytes of that extent in the owning
  member. The frame carries those bytes with only their relative link
  destinations rebased.

Link rebasing. A relative destination in an excerpt is relative to the
owning member's directory; in the frame it must resolve from
standards/frames/ to the same target. `rebase` prefixes each relative
destination with the path from the frames directory to the owner's
directory (`X.md#a` becomes `../X.md#a`), and rewrites an in-member
fragment against the owning member (`#a` in FOUNDATIONS.md becomes
`../FOUNDATIONS.md#a`). A destination with a scheme (`stdo://`, `https:`,
`mailto:`) or starting with `/` is unchanged. Fenced code and inline code
spans are unchanged. Inline links, images and link reference definitions
are rebased. Not rebased: HTML attributes such as `href`, and indented code
blocks, which this rule does not recognise; a four-space-indented line is
read as text, as in a list continuation. The rewrite is a deterministic
function of the extent and the owner path, so `--check` compares against
the same rebased bytes. Adapted from Codex `relocate`
(qualification/C3/refresh_views.py:20-26, called at :59, at 31f28f9). Codex
refuses an in-member fragment and does not skip code; here the fragment is
rewritten against the owner coordinate and code is skipped.

Row selection (I4-06, tradeoff TO1). A route may carry
`"rows": {"mode": "frame-anchors"}`. Its excerpt then keeps prose, headings,
blank and fenced lines, every table header and separator, every row of a
table whose header has no `Consequence` column, and, in a family table,
only the rows whose link destinations (`#anchor` or `MEMBER.md#anchor`)
name an anchor that another route of the same frame carries in that
member. Such an excerpt is not a byte copy of its section: its `Source:`
line says `rows=k/n`, the manifest records `selected`, `total` and the
excerpt digest beside the section digest, and the omitted rows stay in
the owning member. `select_rows` below is the one implementation and has
a test.

Refusal, never truncation: on any refusal no file is written, the refusal is
printed as `refusal: <member>:<line>: <reason>` and the exit status is 2.

Usage:
  generate_frames.py [--root DIR] [--inputs PATH]      write frames and manifest
  generate_frames.py --check [--root DIR] [--inputs PATH]
                                                       exit 1 if any file would change
  generate_frames.py --list MEMBER [--root DIR]        print anchors, lines, bytes
"""
import argparse
import hashlib
import json
from pathlib import Path
import posixpath
import re
import sys
import unicodedata

TENANT_ROOT = Path(__file__).resolve().parents[2]
INPUTS_RELATIVE = Path('standards') / 'frames' / 'FRAME_INPUTS.json'
FRAMES_RELATIVE = Path('standards') / 'frames'
MAX_FRAME_BYTES = 150_000
FRAME_ID = re.compile(r'^[a-z0-9][a-z0-9-]*$')

# Ported verbatim from Codex qualification/C3/refresh_views.py:12-18 at 31f28f9.
```

```python

```

```python
def select_rows(member: Member, start: int, end: int, owner: str, anchors_by_owner: dict):
    """Line indices of the extent [start, end) keeping, in every table whose header has a
    `Consequence` column, only the rows that link to a section this frame carries.

    Prose, headings, blank and fenced lines, table headers and separators, and every row of
    a table that is not a family table are kept. A family-table row is kept when one of its
    link destinations is `#anchor` (this member) or `MEMBER.md#anchor` and that anchor is a
    route of this frame in that member. Returns (indices, family rows total, rows kept)."""
    indices, total, kept = [], 0, 0
    state = None  # None: outside a table; 'header', 'separator', then ('family', bool)
    for i in range(start, end):
        raw = bare(member.lines[i]).lstrip(' ')
        is_row = (not member.fenced[i]) and raw.startswith('|')
        if not is_row:
            state = None
            indices.append(i)
            continue
        text = member.lines[i].decode('utf-8')
        if state is None:
            state = ('header', 'Consequence' in text)
            indices.append(i)
            continue
        if state[0] == 'header':
            state = ('rows', state[1])
            indices.append(i)
            continue
        if not state[1]:
            indices.append(i)
            continue
        total += 1
        keep = False
        for destination in LINK_DESTINATION.findall(re.sub(r'`[^`]*`', '', text)):
            path, _, anchor = destination.partition('#')
            if not anchor or path.startswith(('http', 'stdo:', '/', 'mailto:')):
                continue
            target = Path(owner).name if path == '' else Path(path).name
            if anchor in anchors_by_owner.get(target, set()):
                keep = True
                break
        if keep:
            indices.append(i)
            kept += 1
    return indices, total, kept



```

```python
def source_line(owner: str, anchor: str, owner_sha256: str, note: str = '') -> bytes:
    return f'Source: {Path(owner).name}#{anchor} sha256={owner_sha256}{note}'.encode('utf-8')


def header(frame: dict, size: int) -> bytes:
    routes = '\n'.join(
        f'{n}. [{Path(r["owner"]).name}#{r["anchor"]}](../{Path(r["owner"]).name}#{r["anchor"]})'
        for n, r in enumerate(frame['routes'], 1))
    text = (
        f'# Reference frame {frame["id"]}\n'
        '\n'
        f'Task: {frame["task"]}\n'
        '\n'
        f'Purpose: {frame["scope"]}\n'
        '\n'
        'Each excerpt below copies one owning section of a member of this method\n'
        'byte for byte, except a `rows=k/n` excerpt (see below) and except that\n'
        'each relative link destination is rebased\n'
        'to resolve from this directory to the same target. Fenced code, inline\n'
        'code and absolute and `stdo://` links are unchanged. The `Source:` line\n'
        "before an excerpt names the member and the section's anchor, and gives\n"
        'the SHA-256 of the whole owning member. The section digest recorded in\n'
        "FRAME_INPUTS.json is over the owner's bytes, not over this copy. The\n"
        'owning section decides; this frame owns no determination. An excerpt\n'
        'whose `Source:` line says `rows=k/n` is a family table of which only\n'
        'the k rows that cite a section this frame carries are copied, with the\n'
        "table's preamble, header and every non-family table; the other rows\n"
        "stay in the owning member and are not copied. The frame's\n"
        'qualification, not this selection, decides whether the frame is\n'
        'sufficient for its task.\n'
        '\n'
        'Routes, in order:\n'
        '\n'
        f'{routes}\n'
        '\n'
        f'Size of this frame: {size} bytes.\n'
    )
    return text.encode('utf-8')



```

### The row-selection tests (R2b-07)

```python
(unittest.TestCase):
    """Requirement 6 of design/CROSS_SYNTHESIS.md part 5: `rows: frame-anchors`."""
    TEXT = (
        '# M\n\n## Entry\n\ntext\n\n## Foundation to law\n\npreamble\n\n'
        '| Instance premise | Standing |\n|---|---|\n| I1 | adopted |\n\n'
        '| Premises, with standing | Consequence that follows | Rule in this member that states it | Added choice | Pillar |\n'
        '|---|---|---|---|---|\n'
        '| P1 | by P1 so a | [§1](#entry) | none | 1 |\n'
        '| P2 | by P2 so b | [§9](#other) | none | 2 |\n'
        '| P3 | by P3 so c | [Y §2](Y.md#yy); [§1](#entry) | none | 3 |\n'
        '| P4 | by P4 so d | (#entry) in code `[x](#entry)` | none | 4 |\n\n'
        'after the table\n\n## Other\n\nz\n')

    def test_keeps_header_prose_and_cited_rows_only(self):
        m = member(self.TEXT, 'standards/M.md')
        start, end, _ = m.section('foundation-to-law')
        idx, total, kept = gf.select_rows(m, start, end, 'standards/M.md', {'M.md': {'entry'}, 'Y.md': set()})
        text = b''.join(m.lines[i] for i in idx).decode()
        self.assertEqual((total, kept), (4, 2))
        self.assertIn('| I1 | adopted |', text)            # non-family table kept whole
        self.assertIn('| P1 | by P1 so a', text)
        self.assertIn('| P3 | by P3 so c', text)
        self.assertNotIn('| P2 | by P2 so b', text)
        self.assertNotIn('| P4 |', text)                    # bare (#entry) is not a link destination
        self.assertIn('preamble', text); self.assertIn('after the table', text)

    def test_cross_member_link_counts_when_that_owner_route_is_carried(self):
        m = member(self.TEXT, 'standards/M.md')
        start, end, _ = m.section('foundation-to-law')
        idx, total, kept = gf.select_rows(m, start, end, 'standards/M.md', {'Y.md': {'yy'}})
        self.assertEqual((total, kept), (4, 1))

    def test_build_records_rows_and_marks_source_line(self):
        tree = TempTree({'M.md': self.TEXT, 'Y.md': '# Y\n\n## yy\n\nq\n'},
                        [{'id': 'f', 'task': 't', 'scope': 's', 'routes': [
                            {'owner': 'standards/M.md', 'anchor': 'entry'},
                            {'owner': 'standards/M.md', 'anchor': 'foundation-to-law', 'rows': {'mode': 'frame-anchors'}}]}])
        try:
            out = gf.build(tree.root, tree.inputs)
            frame = out[tree.root / 'standards/frames/f.md'].decode()
            manifest = json.loads(out[tree.inputs].decode())
            self.assertIn('rows=2/4 selected by the anchors this frame carries', frame)
            rows = manifest['frames'][0]['routes'][1]['rows']
            self.assertEqual((rows['mode'], rows['selected'], rows['total']), ('frame-anchors', 2, 4))
            self.assertEqual(len(rows['excerpt_sha256']), 64)
        finally:
            tree.close()



```

### The checker controls (C5, R2b-12, R2b-13)

```python
"""Port C5, adapted: positive checker run with adverse controls.
Usage, from the tenant root: python3 -I qualification/C3-ITER4/tools/ac_controls.py <scratch dir>
Writes qualification/C3-ITER4/returns/ac_controls.json. Every control states what it expects and what happened.
"""
import hashlib, json, os, shutil, subprocess, sys, time
SP = sys.argv[1]; os.makedirs(SP, exist_ok=True)
t0 = time.time()
rec = {'kind': 'claude-ac-controls', 'controls': []}
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def ctl(name, expect, holds, detail): rec['controls'].append({'control': name, 'expects': expect, 'holds': bool(holds), 'detail': detail})
# 1. materialise and identify the checker
out = subprocess.run(['bash', 'qualification/C3-ITER3/tools/verify_ai.sh', SP], capture_output=True, text=True)
AI = out.stdout.strip().splitlines()[-1]; AC = os.path.join(AI, 'build_tenants/core/code/ac.py')
rec['checker'] = {'ids': out.stdout.strip().splitlines()[0], 'ac_py_sha256': sha(AC)}
# expected digests are read from the common dependency contract, not from a constant
DEP = '../../specification/requirements/A_C_DEPENDENCY.md'
import re as _re
dep = open(DEP, encoding='utf-8').read()
expected = {k: _re.search(rf'\| {k} SHA256 \| ([0-9a-f]{{64}}) \|', dep).group(1) for k in ('Executable', 'Schema', 'Output-contract')}
files = {'Executable': AC, 'Schema': os.path.join(AI, 'skills/axiomatize-corpus/references/program.schema.json'), 'Output-contract': os.path.join(AI, 'skills/axiomatize-corpus/references/output-contract.md')}
def identity_check(paths):
    """The identity check: every named member's digest equals the contract's; returns (ok, mismatches)."""
    mism = [k for k, p in paths.items() if sha(p) != expected[k]]
    return (not mism), mism
ok, mism = identity_check(files)
ctl('identity-positive', 'the materialised executable, schema and output contract match the digests in A_C_DEPENDENCY.md', ok, {'expected': expected, 'mismatches': mism})
tampered = dict(files); tam = os.path.join(SP, 'program.schema.tampered.json'); shutil.copy(files['Schema'], tam); open(tam, 'ab').write(b'\n'); tampered['Schema'] = tam
ok2, mism2 = identity_check(tampered)
ctl('identity-adverse', 'the same identity check refuses when one member is tampered (one byte appended to the schema)', (not ok2) and mism2 == ['Schema'], {'mismatches': mism2})
PROG = 'a_c/i3/axiomatic-program.json'; BIND = 'a_c/i3/bindings.json'
def run(args):
    r = subprocess.run(['python3', '-I', AC] + args, capture_output=True, text=True); return r.returncode, r.stdout[-300:], r.stderr[-300:]
def validate(prog, tag):
    rep = os.path.join(SP, f'report-{tag}.json'); mp = os.path.join(SP, f'map-{tag}.json')
    rc, so, se = run(['validate', '--program', prog, '--bindings', BIND, '--output', rep, '--emit-map', mp])
    st = json.load(open(rep))['status'] if os.path.exists(rep) else None
    diag = len(json.load(open(rep)).get('diagnostics', [])) if os.path.exists(rep) else None
    return rc, st, diag, rep, mp, se
# 2. positive validation reproduces the frozen report
rc, st, diag, rep, mp, se = validate(PROG, 'positive')
ctl('validate-positive', 'exit 0, status valid, 0 diagnostics, report and map byte-identical to a_c/i3', rc == 0 and st == 'valid' and diag == 0 and sha(rep) == sha('a_c/i3/validation-report.json') and sha(mp) == sha('a_c/i3/logical-constraint-map.json'), {'exit': rc, 'status': st, 'diagnostics': diag, 'report_identical': sha(rep) == sha('a_c/i3/validation-report.json'), 'map_identical': sha(mp) == sha('a_c/i3/logical-constraint-map.json')})
# 3. adverse programs
prog = json.load(open(PROG))
m1 = dict(prog); m1['clauses'] = prog['clauses'] + [prog['clauses'][0]]; p1 = os.path.join(SP, 'prog-dup.json'); json.dump(m1, open(p1, 'w'), indent=1)
rc, st, diag, *_ , se = validate(p1, 'dup')
ctl('validate-adverse-duplicate-clause', 'a program with a duplicated clause uri is not valid', st != 'valid' or (diag or 0) > 0 or rc != 0, {'exit': rc, 'status': st, 'diagnostics': diag, 'stderr': se[-160:]})
m2 = json.loads(json.dumps(prog)); m2['clauses'][0]['source_refs'] = ['stdo-3://build_tenants/claude/standards/AXIOMATIC_CALCULUS.md#no-such-anchor-i4-control']; p2 = os.path.join(SP, 'prog-dangling.json'); json.dump(m2, open(p2, 'w'), indent=1)
rc, st, diag, *_ , se = validate(p2, 'dangling')
ctl('validate-adverse-dangling-source', 'a program whose clause cites a missing anchor is not valid', st != 'valid' or (diag or 0) > 0 or rc != 0, {'exit': rc, 'status': st, 'diagnostics': diag, 'stderr': se[-160:]})
# 4. projections reproduce byte for byte; a mutated index projects differently
os.makedirs(os.path.join(SP, 'proj'), exist_ok=True); same = []; 
for fi in prog['frame_indexes']:
    ix = fi['uri'].rsplit(':', 1)[-1]
    for mode in ('reference-only', 'materialized'):
        o = os.path.join(SP, 'proj', f'projection-{ix}-{mode}.json')
        rc, so, se = run(['project', '--program', PROG, '--map', mp, '--bindings', BIND, '--frame-index', fi['uri'], '--mode', mode, '--output', o])  # the fresh map of the positive validate
        f = f'a_c/i3/projections/projection-{ix}-{mode}.json'; same.append((ix, mode, rc, os.path.exists(o) and os.path.exists(f) and sha(o) == sha(f), se[-120:] if rc else ''))
ctl('project-positive', 'all 8 projections from the fresh map exit 0 and are byte-identical to a_c/i3/projections', all(rc == 0 and s for _, _, rc, s, _ in same), same)
m3 = json.loads(json.dumps(prog)); fi0 = m3['frame_indexes'][0]; dropped = fi0['clause_refs'].pop(); p3 = os.path.join(SP, 'prog-dropped.json'); json.dump(m3, open(p3, 'w'), indent=1)
rc3, st3, diag3, rep3, mp3, se3 = validate(p3, 'dropped')
o3 = os.path.join(SP, 'proj', 'dropped.json'); rc, so, se = run(['project', '--program', p3, '--map', mp3 if os.path.exists(mp3) else 'a_c/i3/logical-constraint-map.json', '--bindings', BIND, '--frame-index', fi0['uri'], '--mode', 'materialized', '--output', o3])
ix0 = fi0['uri'].rsplit(':', 1)[-1]; f0 = f'a_c/i3/projections/projection-{ix0}-materialized.json'
base = os.path.join(SP, 'proj', f'projection-{ix0}-materialized.json')  # the fresh positive projection of the same index
ctl('project-adverse-dropped-clause', 'a program with one clause dropped from a frame index validates, and its projection differs from the fresh positive projection of that index (the passing baseline), and from the frozen one', st3 == 'valid' and os.path.exists(o3) and os.path.exists(base) and sha(o3) != sha(base) and sha(o3) != sha(f0), {'dropped': dropped, 'exit': rc, 'validate_status': st3, 'baseline_exists': os.path.exists(base), 'differs_from_fresh': os.path.exists(o3) and os.path.exists(base) and sha(o3) != sha(base), 'stderr': se[-160:]})
rec['elapsed_seconds'] = round(time.time() - t0, 1); rec['holds_all'] = all(c['holds'] for c in rec['controls'])
json.dump(rec, open('qualification/C3-ITER4/returns/ac_controls.json', 'w'), indent=1)
for c in rec['controls']: print(('HOLDS ' if c['holds'] else 'FAILS '), c['control'], json.dumps(c['detail'])[:200])
print('all hold:', rec['holds_all'], 'elapsed', rec['elapsed_seconds'])

```

```json
{
 "kind": "claude-ac-controls",
 "controls": [
  {
   "control": "identity-positive",
   "expects": "the materialised executable, schema and output contract match the digests in A_C_DEPENDENCY.md",
   "holds": true,
   "detail": {
    "expected": {
     "Executable": "5a2e0cb503cf598bbaea215270373b87a0928222be272f33d951550b0d16e6c8",
     "Schema": "43326dbab520bd2d56fbdf605211f66499de1969b13e2e0226868bd6af9777a7",
     "Output-contract": "c124264d1fc564a8a054bba46b5c188c4e770da51862b4c2122e3c616efb1b6b"
    },
    "mismatches": []
   }
  },
  {
   "control": "identity-adverse",
   "expects": "the same identity check refuses when one member is tampered (one byte appended to the schema)",
   "holds": true,
   "detail": {
    "mismatches": [
     "Schema"
    ]
   }
  },
  {
   "control": "validate-positive",
   "expects": "exit 0, status valid, 0 diagnostics, report and map byte-identical to a_c/i3",
   "holds": false,
   "detail": {
    "exit": 0,
    "status": "valid",
    "diagnostics": 0,
    "report_identical": false,
    "map_identical": false
   }
  },
  {
   "control": "validate-adverse-duplicate-clause",
   "expects": "a program with a duplicated clause uri is not valid",
   "holds": true,
   "detail": {
    "exit": 1,
    "status": "invalid",
    "diagnostics": 2,
    "stderr": ""
   }
  },
  {
   "control": "validate-adverse-dangling-source",
   "expects": "a program whose clause cites a missing anchor is not valid",
   "holds": true,
   "detail": {
    "exit": 1,
    "status": "invalid",
    "diagnostics": 1,
    "stderr": ""
   }
  },
  {
   "control": "project-positive",
   "expects": "all 8 projections from the fresh map exit 0 and are byte-identical to a_c/i3/projections",
   "holds": false,
   "detail": [
    [
     "authority-kinds",
     "reference-only",
     0,
     false,
     ""
    ],
    [
     "authority-kinds",
     "materialized",
     0,
     false,
     ""
    ],
    [
     "promotion-block",
     "reference-only",
     0,
     false,
     ""
    ],
    [
     "promotion-block",
     "materialized",
     0,
     false,
     ""
    ],
    [
     "result-algebra-and-conjunction",
     "reference-only",
     0,
     false,
     ""
    ],
    [
     "result-algebra-and-conjunction",
     "materialized",
     0,
     false,
     ""
    ],
    [
     "reuse-and-invalidation",
     "reference-only",
     0,
     false,
     ""
    ],
    [
     "reuse-and-invalidation",
     "materialized",
     0,
     false,
     ""
    ]
   ]
  },
  {
   "control": "project-adverse-dropped-clause",
   "expects": "a program with one clause dropped from a frame index validates, and its projection differs from the fresh positive projection of that index (the passing baseline), and from the frozen one",
   "holds": true,
   "detail": {
    "dropped": "urn:stdo-3:claude:i3:clause:what-creates-no-authority",
    "exit": 0,
    "validate_status": "valid",
    "baseline_exists": true,
    "differs_from_fresh": true,
    "stderr": ""
   }
  }
 ],
 "checker": {
  "ids": "tag 9bff233c3f0e7d80f63307fa3b12800dd3db681c commit 9a9c479776ffd974fbcafcf48341980918209aef tree 3a553ceb8db2e8de4ac779abdc2a2ceae5708c7d subtree 6dae168d0a258ca506f4d6b9d5cd0a0c835fb546",
  "ac_py_sha256": "5a2e0cb503cf598bbaea215270373b87a0928222be272f33d951550b0d16e6c8"
 },
 "elapsed_seconds": 1.2,
 "holds_all": false
}
```

### The frontier review tool (C3, R2b-10, R2b-11)

```python
"""Build frontier/REVIEW.json from the Markdown frontier (port C3, adapted).

Usage, from the tenant root: python3 -I qualification/C3-ITER4/tools/frontier_review.py
Reads the installed rc.2 standards and this candidate's standards; writes
frontier/REVIEW.json. A section's text, for its hash, runs to the next heading of
any level: the frontier's own granularity rule (one row per heading section, a
parent's row not covering its children), which differs on purpose from the frame
generator's whole-section rule. modal_conversion is raised only for `conserved`
rows with a successor locus: a `superseded` row is decided by its proposed
replacement relation, not by the conservation reading; a row without a locus has
nothing to compare. Fields beyond the donor schema: identifiers, disposition_note,
proposed_replacement, acceptance and the summary counts. Every semantic_review.result is `indeterminate` unless
frontier/REVIEW_ASSESSMENTS.json records a nonauthor assessment for the row.
"""
import hashlib, json, os, re, sys
RC2 = '/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards'
def slug(h):
    return re.sub(r'[^\w\- ]', '', h.strip().lower().replace('`', '')).replace(' ', '-')
def sections(path):
    """anchor -> text under the heading up to the next heading of any level"""
    out, seen, cur, buf, code = {}, {}, None, [], False
    for line in open(path, encoding='utf-8'):
        if line.startswith('```'): code = not code
        m = None if code else re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            if cur is not None: out[cur] = ''.join(buf)
            s = slug(m.group(2)); n = seen.get(s, 0); seen[s] = n + 1
            cur = s if n == 0 else f'{s}-{n}'; buf = []
        else:
            buf.append(line)
    if cur is not None: out[cur] = ''.join(buf)
    return out
assess = {}
if os.path.exists('frontier/REVIEW_ASSESSMENTS.json'):
    assess = {a['id']: a for a in json.load(open('frontier/REVIEW_ASSESSMENTS.json'))['assessments']}
rows, member, base, pred = [], None, None, {}
succ_cache = {}
def succ(locus):
    f, _, a = locus.partition('#')
    if f not in succ_cache:
        p = os.path.join('standards', f)
        succ_cache[f] = sections(p) if os.path.exists(p) else None
    s = succ_cache[f]
    if s is None or a not in s: return None
    return s[a]
unres_pred = unres_succ = 0
for line in open('frontier/PREDECESSOR_CLAIMS.md', encoding='utf-8'):
    if line.startswith('## '):
        member = line[3:].strip(); base = None; pred = {}; continue
    m = re.match(r'Base route: `stdo://releases/v2\.5\.1-rc\.2/standards/([^`]+)`', line)
    if m:
        base = m.group(1); p = os.path.join(RC2, base)
        pred = sections(p) if os.path.exists(p) else {}
        continue
    if not line.startswith('| ') or line.startswith('|---'): continue
    c = [x.strip() for x in line.rstrip('\n').strip('|').split(' | ')]
    if len(c) < 6: continue
    am = re.search(r'`#([^`]+)`', c[1])
    if not am: continue
    anchor = am.group(1); dcell = c[4].strip('`* ')
    dm = re.match(r'(conserved|superseded|removed|rejected)', dcell)
    disp = dm.group(1) if dm else dcell.split(' ')[0]
    proposed = bool(re.search(r'\bproposed\b', dcell)) or disp == 'superseded'
    loci = re.findall(r'`([^`#\s]+\.md#[^`]+)`', c[5])
    ptext = pred.get(anchor)
    if ptext is None: unres_pred += 1
    stexts = [(l, succ(l)) for l in loci]
    for l, t in stexts:
        if t is None: unres_succ += 1
    pmodal = bool(ptext and re.search(r'\b(must|shall)\b', ptext, re.I))
    smodal = any(t and re.search(r'\b(must|shall)\b', t, re.I) for _, t in stexts)
    rid = f'{member}#{anchor}'
    a = assess.get(rid)
    rows.append({
        'id': rid, 'source_member': base, 'source_anchor': '#' + anchor, 'identifiers': c[2],
        'disposition': disp, 'disposition_note': dcell if dcell != disp else '', 'proposed_replacement': proposed, 'disposition_standing': 'author_proposal',
        'acceptance': 'ticket_decision_pending',
        'predecessor_sha256': hashlib.sha256(ptext.encode()).hexdigest() if ptext is not None else None,
        'successor_loci': [{'locus': l, 'sha256': hashlib.sha256(t.encode()).hexdigest() if t is not None else None} for l, t in stexts],
        'modal_conversion': bool(pmodal and loci and not smodal and disp == 'conserved'),
        'semantic_review': a['semantic_review'] if a else {
            'result': 'indeterminate',
            'scope': 'author disposition; no nonauthor assessment recorded for this row',
            'remaining_obligations': ['author-independent comparison of required and permitted decisions, modal force, triggers, scope and exceptions']}
    })
sem = hashlib.sha256(json.dumps([(r['id'], r['disposition'], r['predecessor_sha256'], r['successor_loci']) for r in rows]).encode()).hexdigest()
out = {'kind': 'claude-frontier-review', 'schema_version': 1, 'rows': rows, 'row_count': len(rows), 'semantic_sha256': sem,
       'counts': {'modal_conversion': sum(r['modal_conversion'] for r in rows),
                  'assessed': sum(1 for r in rows if r['semantic_review']['result'] != 'indeterminate'),
                  'unresolved_predecessor_anchor': unres_pred, 'unresolved_successor_locus': unres_succ,
                  'proposed_replacement': sum(r['proposed_replacement'] for r in rows), 'by_disposition': {d: sum(1 for r in rows if r['disposition'] == d) for d in sorted({r['disposition'] for r in rows})}}}
json.dump(out, open('frontier/REVIEW.json', 'w'), indent=1); print(json.dumps(out['counts']), 'rows', len(rows))

```

### The port evaluation record (I4 adaptations)

```markdown
# Port Evaluation, Iteration 4 (I4-03)

Evaluation of the six contributions C1 to C6 nominated for this line in
the staged plan, against the donor: the Codex candidate at handoff
`fb855df`, package `d490dd6`. Every donor file was read with `git show`
at `d490dd6`; no working tree was read. Under the ratified
[Cross-Synthesis](../../../../specification/PRODUCT.md#cross-synthesis) a
port list is input, not an obligation, and each contribution that enters
records its frozen source, receiving owner, adaptation, the predecessor
claims and dependencies it affects, and the evidence to check again. The
Codex tenant authored every source below; this line's same-family
nonauthor reviewer gives the independent assessment of each received
contribution (I4-09), and Codex's reading of its own contribution is
supplementary. Nothing here is accepted.

| # | Decision | Frozen source at `d490dd6` (`build_tenants/codex/`) | Receiving owner | Adaptation | Affected claims and dependencies | Evidence to recheck |
|---|---|---|---|---|---|---|
| C1 performance coordinate and effect-observation values | **excluded** | `successor/standards/FOUNDATIONS.md:308–345` (`performed`, `not_performed`, `unconfirmed`) | none | none | none | none |
| C2 actual-use protocol | **selected, realised only under D5 option A** | `qualification/C3/iteration-3/use-r2/assessment/native-use-grading-01/PROTOCOL_AND_COMPARISON.json`, `run_artifact_probe.py`, `ARTIFACT_PROOF.json`; `qualification/C3/synthesis/entry/PROTOCOL.md` | `qualification/C3-ITER4/PLAN.md` §5 trial design, an instrument in no frontier cone | five elements taken as design: an isolated actor with no context beyond the frame; protocol and oracle frozen at a commit before the actor starts; a nonauthor assessor whose expectations are fixed before any return; byte admission with a serialised reader that records every byte supplied and acquired; a replay probe for constructed artifacts. The head-to-head protocol is the pen's and is not ported | none; ACTIVATION §2 step 3 and §6 govern the trial's limits | the trial record itself, if run |
| C3 frontier record schema | **adapted** | `qualification/C3/iteration-3/FRONTIER.json` (row objects: `disposition_standing`, `acceptance`, `successor_loci`, `consumer_binding_refs`, `semantic_review` with `result`, `scope`, `remaining_obligations`; file-level `semantic_sha256`) | `frontier/REVIEW.json`, generated by `qualification/C3-ITER4/tools/frontier_review.py` from the Markdown frontier, which stays the human-readable record beside `deltas/` | per row: predecessor section hash at rc.2, successor locus hash at the current tree, disposition, standing `author_proposal`, `semantic_review.result` with the default `indeterminate` that only a recorded nonauthor assessment changes, and a `modal_conversion` flag where a `conserved` row's predecessor section says "must" or "shall" and its successor locus does not (a `superseded` row is decided by its relation, not by this reading); further fields beyond the donor's: `identifiers`, `disposition_note`, `proposed_replacement`, `acceptance` and summary counts; a section's text for its hash runs to the next heading of any level, the frontier's own granularity, which differs on purpose from the frame generator's whole-section rule | RELEASE §9 frontier rules of this candidate (a sidecar record, no new owner); all 707 rows | `frontier_check.py`, `locus_check.py`, regeneration byte-identical |
| C4 per-unit consumers and acquisition semantics | **adapted** | `successor/interpretation/source-account.json` (`determinations[*]` with owner locus and hash, `inputs[*].standing`, `result_mapping.owner_refs`; `semantic_contracts`) | `a_c/i3/consumers.json`, a sidecar of the interpretation, noted in `a_c/i3/README.md` | for each of the 64 clauses: the owner locus with its current hash, and the consumer loci that cite that owner, each with `support` = `cites` when derived from a link and `required` or `conditional` only when a reader records it; unrecorded semantics stay `unresolved` | AXIOMATIC_CALCULUS §9 and the encoded owners of G1 to G4; no member text changes | the fidelity cases of I4-05 and the checker run |
| C5 artifact and identity checks with adverse controls | **adapted** | `qualification/C3/iteration-3/check_identity.py`, `IDENTITY_CHECK.json` (`positive`, `negative_controls`), `ARTIFACT_CHECK.json`; `a_c/validation-wrong.json`, `a_c/projection-wrong.json` | `qualification/C3-ITER4/tools/ac_controls.py`, an instrument | seven controls: the materialised executable, schema and output contract match the digests in the common `A_C_DEPENDENCY.md`, and the same check refuses when one byte is appended to a copy of the schema; `validate` on the unmodified program reproduces the frozen report and map, and rejects a duplicated clause and a dangling source; the eight projections reproduce the frozen ones byte for byte, and a program with one clause dropped from a frame index projects differently from the fresh positive projection of that index. The positive reproductions hold only when the frozen `a_c/i3` artifacts are current; they are regenerated at the freeze and the controls rerun then | none; A_C_DEPENDENCY binds the checker | the control log at freeze |
| C6 retention of `must` and `shall` | **excluded** | the donor's member texts generally | none | none | FR-02 and FR-07 are closed by the ratified test, not by a convention | the per-row judgments of I4-04 |

Reasons for the exclusions:

- C1. The common [single result algebra requirement](../../../../specification/requirements/README.md#single-result-algebra-requirement) asks that non-performance, undecidability and effect uncertainty be preserved. This candidate preserves them in its own representation: an evaluation that was planned and not performed has no result and is carried as a residual in the work state (`ACTIVATION.md:830–846`); an evaluation whose evidence cannot decide returns `indeterminate`; an effect whose completion is not established is `completion_unknown`, never `completed` or `not_effected` (`ACTIVATION.md:920–946`, REDUCTION R4). Codex's Stage 1 reading (finding 1) reads this as a lawful alternative. Porting the coordinate would give one determination two representations with two owners.
- C6. The ratified requirement says modal wording is judged by its meaning, that indicative wording can bind, and that replacing "must" or "shall" is neither automatic conservation nor automatic supersession. Retaining the words would prove conservation no more than the indicative convention did. This line keeps the indicative and records a meaning judgment for every converted row (I4-04), using the `modal_conversion` rows of `frontier/REVIEW.json`.

## The six iteration 3 ports

The six parts ported at I3 from the Codex candidate at `31f28f9`
([CROSS_SYNTHESIS, port list](../../design/CROSS_SYNTHESIS.md#port-list);
[I3 accounting](../C3-ITER3/ports.md)) were never compared with their
source by any reviewer, because that review waited for a port policy the
ratified text now supplies. Under the ratified allocation they receive the
same-family nonauthor readback in I4-09, each against its source lines at
`31f28f9`, its receiving owner and its cone rows, with verbatim text
compared byte for byte and adapted text sentence by sentence.

| # | Part | Receiving owner | Readback |
|---|---|---|---|
| 1 | Specialization table with premise standing | FOUNDATIONS §3 | I4-09 |
| 2 | Premise standing discipline | FOUNDATIONS §3 Commitments | I4-09 |
| 3 | Reference-only import declarations | REFERENCE_FRAME §1 under FOUNDATIONS §2 | I4-09 |
| 4 | Equivalence ladder | EVALUATION §6 | I4-09 |
| 5 | Verbatim digest-bound frames and direct acquisition | ACTIVATION §2 Acquisition; `qualification/instruments/generate_frames.py` | I4-09 |
| 6 | Finite check with mutant counterexamples | `qualification/instruments/finite_oracle/` | I4-09 |

```

## Donor sources again

### port 3, Codex FOUNDATIONS 128-162 at 31f28f9

```text
## Reference-only semantic imports

Source and target meanings are identical owner-qualified references, not new
local definitions. Direction is from the named source to this explanatory
context; loss is none and no translation or ownership transfer is asserted.
The target semantic owner is the STDO Specification Methodology Product authority,
the same owner declared above. The source context is declared by
[Frame Method's Position](REFERENCE_FRAME_METHOD.md#position), whose owner is
REFERENCE_FRAME_METHOD.md. The source basis is that member at SHA256
`44bb25eacd05550240d31ef318dc2c23db2b8a147ba1b8daa342f688d343e488`.
The target basis is this member at its exact member digest supplied by the
frozen activation or selected installed manifest. A review carrier is not an
installed dependency and supplies no authority.
An activation binds each member's distinct coordinates in its selected complete
governing basis; equal cut selection does not mean equal member coordinates.
Lifecycle and adoption remain source-owned. A changed member, selected basis,
source declaration or adoption premise requires fresh applicability before use.

| Referenced concept | Source context | Exact source concept and owner |
|---|---|---|
| frame-set authority | urn:stdo:bounded-context:reference-frame-evaluation | [Frame authority](REFERENCE_FRAME_METHOD.md#authority): the human authority that declares or accepts the project frame set |
| semantic authority | urn:stdo:bounded-context:reference-frame-evaluation | [Frame authority](REFERENCE_FRAME_METHOD.md#authority): the owner of meaning for a material relation |
| evaluation authority | urn:stdo:bounded-context:reference-frame-evaluation | [Frame authority](REFERENCE_FRAME_METHOD.md#authority): the role permitted to perform an evaluation |
| operation authority | urn:stdo:bounded-context:reference-frame-evaluation | [Frame authority](REFERENCE_FRAME_METHOD.md#authority): the owner-issued grant to construct, transform, admit, publish, or mutate a material subject where an evaluation performs such an operation |
| decision authority | urn:stdo:bounded-context:reference-frame-evaluation | [Frame authority](REFERENCE_FRAME_METHOD.md#authority): the role permitted to accept, reject, or otherwise dispose its result |
| actor identity | urn:stdo:bounded-context:reference-frame-evaluation | [Frame authority](REFERENCE_FRAME_METHOD.md#authority): the human, agent, tool, or process performing work. |

These are reference-only imports into urn:stdo:bounded-context:foundations.
They provide no semantic, evaluation, operation or decision authority. Baseline
Reviewer/Worker examples and ODD runtime roles are direct, owner-qualified
domain references; this context neither imports their role labels nor creates
aliases or a common outcome type. Their linked contracts and adoption conditions
remain necessary for any material domain use. An activation lacking the source meaning,
adoption or authority binding reports that unresolved relation before dependent
reliance rather than interpreting it from equal spelling.
```

### port 4, Codex FOUNDATIONS 249-258 at 31f28f9

```text
To assert a category, specify objects, typed arrows, identities and associative
composition. To assert a functor, show identity and composition preservation.
For a proposed categorical model, A names the algorithmic account, I the
interpreted informational account, and C_H the computational realization on a
declared architecture H. They name categories only after the required objects,
arrows and laws have been supplied. For a proposed span A -> I and A -> C_H,
conformance to Sigma_contract, semantic
equivalence and computational equivalence remain different claims. Categorical
equivalence additionally requires the appropriate quasi-inverse and natural
isomorphisms on a stated domain; an analogy or matching result is insufficient.
```

### port 1, Codex TRANSFORMATION_LIBRARY 93-112 at 31f28f9

```text
## Work/recovery specialization

This chain specializes the generic contract for interrupted, purposeful work.
It assumes an admitted work identity, persistent workspace, selected outcome,
actual grants and a material uncertain effect. These are explicit instance
premises; they do not follow from finite capacity alone.

| Premises | Conditional consequence | Particular contract and independent choice |
|---|---|---|
| F1, F2; selected outcome and current subject | A current claim needs its actual predicate and support, not a remembered green status. | Spec Method UP-020 binds target truth and checkpoint; RF-005 fixes basis/coordinates. The owner chooses the outcome. |
| F2, F5; coupled material obligations and finite actor | Acquire sufficient material or return the admitted uncertainty; omitted support cannot become satisfaction. | RF-003/RF-014 bind sufficiency/capability; the work entry locates a responsibility view. Frame selection and configuration authority remain independent grants. |
| F3, F4; persistent work and affected dependencies | Re-enter on observed current state, retaining applicable progress and reconsidering changed support. | Computed Classification And Treatment and Ticket condition-based reuse choose applicability, invalidation and the wider frontier when independence is unproved. Their concrete freshness rules are domain policy. |
| F2, F3, F6; an effect is uncertain and repetition could duplicate it | Neither historical intent nor a timeout proves completion or grants a safe repeat. Observe/reconcile, select another permitted action, or return unresolved. | Computed Classification And Treatment supplies the unknown-effect rule; the operation grant supplies allowed observation and repair. Idempotence must be established for the actual operation. |
| F1, F4, F6; required results and current mandate | Preserve failures, uncovered obligations and uncertainty; choose only an already-authorized continuation or truthful stop. | UP-020, declared conjunction and any adopted Baseline engagement specialize evaluation/disposition. Independence, decision rule and role adoption are additional owner choices. |

The consequences are arguments about the stated premises, not proofs of every
source clause. Concrete work-carrier layout, number of actors, numeric budgets,
optional Baseline adoption, release procedure and all domain result enums are
independent choices. They are not inferred from the foundational commitments.
This chain leaves those choices at their owners and adds no mandatory ledger.
```

### port 2, Codex FOUNDATIONS 48-65 at 31f28f9

```text
The premises below are adopted commitments for the selected methodology domain,
not theorems derived from finite capacity alone. Particular method rules need
these premises plus their stated domain and policy choices. A conditional
argument preserves that distinction; it does not manufacture authority.

## Foundational commitments

The context and owner declared above own F1–F6 in this method realization.
They do not rename the separately scoped authority concepts imported below.

| Commitment | Premise and standing | Distinction retained |
|---|---|---|
| F1 Purpose | Adopt a selected outcome and adequacy relation for purposeful construction. Value choices come from the purpose owner. | A local successful operation need not satisfy the selected outcome. |
| F2 Interpretation | Claims are interpreted on a declared subject and basis; unsupported interpretation remains unresolved. | Encoding or structural validity is not semantic evidence. |
| F3 Identity and current state | Work has scoped identity and observable persistent state; representation and historical observation are separate. | Re-entry need not recreate completed work, and history need not describe current effects. |
| F4 Typed composition | A composite conserves its outer contract's material relations under declared compatibility and loss. | Shared machinery does not merge owners, findings or authority. |
| F5 Finite capacity and total handling | Actor resources are finite; the selected control domain admits truthful handling of unknown, inadequate and interrupted conditions. | Total handling is not omniscience, universal idempotence or guaranteed solution. |
| F6 Evidence and authority | Evidence supports claims; operation and decision authority come from their bound owners. | A judgment or available tool is not permission. |
```

### port 5, Codex SKILL.md 18-39 at 31f28f9

```text
## Acquire The Responsibility Frame

After the exact Product basis is selected, resolve the selected cut's
[standards index](../../../../standards/README.md) and the accepted Project
Reference-Frame Basis for the responsibility named by the task. This is read-only
acquisition inside an already-authorized inspection scope. Effectful work still
needs its separately admitted work contract; acquisition is not another admission
or actor stage. If a required frame basis is absent or unverified, return that
missing binding before dependent action. Inspection supplies no adopted role.

For interrupted work or uncertain effects, the index's work/recovery route
projects current-state, applicability, authority and continuation clauses.
For another task use its relevant route or directly acquire the deciding owners.
Select only available material in the verified basis: a cut without a curated
view still uses its exact owner clauses; a mutable candidate is no fallback.

Read the selected frame and the actual subject. Follow material source and
coupled-obligation references when the task needs them. The view alone makes no
universal sufficiency claim and supplies no role, effect or decision grant.
Do not load the corpus merely because it is present. If coupled material does
not fit the capable activation, retain the unknown and use an already-authorized
refinement, support or stop; do not silently reduce the required predicate.
```

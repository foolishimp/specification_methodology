# REVIEW: the two iteration 3 candidates, and what each should take from the other

**Author**: Dimitar Popov
**Date**: 2026-10-15T02:19:14Z
**Addresses**: the Codex candidate at `c29b2be` (input `C3-I3-CLOSED-01`, `1fce537`) and the Claude candidate at `2beed8d` on `tenant/claude/c3-synthesis` (input `C3-I3-R2-01`, `355aa86`)
**Status**: Complete for the two frozen subjects. Priors were committed at `8c86bfc` before measurement; the Codex findings are in `20261015T021914Z_REVIEW_CODEX_I3_C29B2BE.md` (`332611b`), the Claude findings in the Claude tenant's `qualification/C3-ITER3/HANDOFF.md` and `reviews/`.
**Updated**: 2026-10-15T02:32:17Z (results and recommendation)

## Standing

The product owner asked for "a review against both implementations, which will lead to taking the best of both". The reviewer is the Claude line's own build session, now on Fable 5.1. For the Claude candidate this is self-review: same-family working evidence under EVALUATION §3, never independent assessment. For the Codex candidate it is a cross-family reading by an interested party. The comparison therefore reports what can be measured by script and quoted from text, states each judgement with its evidence, and marks where the reviewer's authorship bears on it. It ranks nothing for acceptance. "Take the best of both" is a proposal for the next cross-synthesis under the owner's rule that each line stays on its own base; it is not a merge plan.

## Priors, recorded before measurement

These are what the reviewer expects to find, so that the result can be read against them. Each is tested below and corrected where wrong.

| Area | Expected stronger | Why expected |
|---|---|---|
| Actual-use evidence (criterion 4) | Codex | six isolated task actors against a hidden oracle, 30/30; Claude ran none, by owner decision |
| Interpretation coverage | Codex | 705 clauses over every member; Claude encoded 64 clauses over four groups |
| Mechanical verification depth | Codex | 89-member artifact check, 1,625 links, adverse controls, cold identity fixture; Claude has link, frontier, frame and finite checks |
| Reduction evidence on deciding paths | Codex, weakly | comparison records against both baselines exist, though no causal gain is claimed; Claude traced 1 of 46 paths |
| One owner per rule, realised in the text | Claude | 34 reduction clusters executed with owner sections and refer-or-refine rivals; the earlier review of Codex found six competing pairs |
| Family arguments | Claude | 21 family tables with premise-to-consequence derivations and pillar cells; Codex had 127 hollow arguments at `3aaa2f2` and claims repair |
| Result algebra | even, Claude slightly | both own one core; Claude has a finite check of the conjunction with mutants |
| Frontier marking | Claude | every supersession marked proposed; Codex's 68 proposals to be checked |
| Frames | Claude on count and task coverage (12, including acceptance and member build), Codex on evidence of use (six tasks run) | |
| Writing | Claude | defined terms, "the product owner", mandatory force kept; Codex prose is denser and more abstract |
| Size and acquisition cost | Codex on members (1.0 MB, 18 files, against 1.65 MB, 23 files); Claude on interpretation (small, partial) against Codex's 25 MB | |
| Shared gaps | both | no cross-family acceptance review; replacement relations pending; categorical worked join absent; compressions decision open; reduction not established as a whole |

## Two notes before the comparison

- **Different inputs.** Codex built on `C3-I3-CLOSED-01` (`1fce537`); Claude on `C3-I3-R2-01` (`355aa86`). The specification differs by 20 lines in five files: the reduction dimensions must be recorded in an existing activation or qualification record; a frontier names proposed dispositions; supported inapplicability waives none of the six criteria; fit may be established from recorded complete active input; packaging derives from method-law owners. Nothing in the comparison turns on these, but the Claude line must rebind to the closed input before its next iteration.
- **Different shapes.** Codex keeps the predecessor's eighteen member names and adds a Transformation Library; its arguments live in family tables of a few rows per member plus a 701-unit machine account. Claude reconstructs the corpus into twenty-three members in three tiers with new names; its arguments live in twenty-one family tables with a row per rule. Both shapes are lawful under reduction item 4. The shape decides much of what follows: Codex's is easier to compare with the predecessor row by row; Claude's makes one owner per rule visible in the text.

## Measured side by side

Scripts over the members at the two frozen commits; the Claude tenant's `qualification/C3-ITER3/tools/` holds them.

| Measure | Codex `c29b2be` | Claude `2beed8d` |
|---|---|---|
| Members, bytes | 18, 1,043 KB | 23, 1,746 KB |
| Headings; table rows; links | 760; 884; 614 | 767; 2,349; 2,214 |
| `must` / `shall` / `should` / `may` / `never` | 379 / 12 / 144 / 437 / 46 | 176 / 0 / 257 / 583 / 277 |
| Family tables; rows with arguments | 13 tables, about 33 rows; 701 account units each with premises, consequence and choices | 21 tables, about 330 rows, each "By … so …" with a labelled choice and a Pillar cell |
| Pillar contributions bound to arguments | no (CX-03) | yes, every row and the index |
| Consumers bound to arguments | yes, per account unit (`consumers`) | no per-row consumer list; owner-to-rival maps in `design/REDUCTION.md` §3 |
| Frontier | 691 rows, JSON: 622 conserved, 68 proposed superseded, 1 not applicable; per row a relation object, section hashes and a `semantic_review` (all `indeterminate`) | 716 rows, Markdown: 654 conserved, 15 proposed superseded, 20 not applicable, 10 unresolved (the compressions); per changed row a delta file with predecessor, before and after quotes |
| Compressions | kept as digest-bound non-deciding read models, 32 pins | kept, rows `unresolved`, supersession proposed, pending the product owner |
| Frames | 6, 47–84 KB, no declared capacity, argument routes to the family tables; used in 4 task runs | 12, 47–77 KB, declared cap 100,000 bytes, verbatim with digests, two added for "decide acceptance or release" and "build or assess a member"; used in no task run |
| Interpretation | 705 clauses, 725 indexes, all 80 documentary members bound; 25.1 MB; per-unit account with predicate, obligations, permissions and exceptions, result mapping; valid, 0 diagnostics | 64 clauses quoted verbatim, 4 indexes, 15 sections encoded in part, 181 not encoded, groups G5 to G13 not encoded; valid, 0 diagnostics, two byte-identical runs |
| Fidelity evidence | author checks; this review's sample 4 of 5 faithful, 1 confirmed defect; no independent review of the rows | 8 cases by a nonauthor same-family reviewer: 3 faithful, 3 defects (repaired, unreviewed), 2 not encoded |
| Actual use (criterion 4) | 6 isolated task actors, frozen protocol and hidden oracle at a commit, nonauthor assessor with pre-fixed expectations, 30 of 30; same family; host context unknown; 4 of 6 frames, 4 of 6 contract tasks | none, by the product owner's decision |
| Reduction evidence | 6 deciding operations against rc.2 and `3ad1fca` with hashes, 3 removal witnesses, adverse byte growth disclosed; not established, not claimed | 46 deciding paths with 8 measures and a guard fixed before measurement; 1 traced; not established |
| Mechanical checks | 89-member artifact check, 1,625 links, 98 excerpts, 32 pins, 18 adverse conservation controls, 19 cold-identity controls, 13 mapping and refusal controls, 11 routing checks; a reader-concurrency repair with a real-process control | link and anchor check; frontier and locus checks; frame generator `--check` and 42 tests; a finite oracle of the conjunction (34,241 assertions, six mutants falsified); pre-check tests; checker verified against seven digests |
| Conformance discriminators | not mapped, not applied (CX-04) | all 52 and 3 closure checks mapped in CONFORMANCE §5; applied only in part by the working reviews |
| Working reviews on the frozen candidate | two same-family readbacks; the fixed-oracle task assessment; the earlier Claude cross-family review at `3aaa2f2`; this review at `c29b2be` | WC-1, WC-2 and FINAL, same-family nonauthor Sonnet reviewers; no cross-family review |
| Open owner decisions | 68 relations; ported-part policy; identity and version; compressions; member acceptance | 15 relations; the same policy, identity and compressions questions; the modal-force convention; the UX test conflict; funding the rest of the encoding |

## Judgements by area

Each judgement names its evidence; where this reviewer's authorship bears on it, the line says so.

1. **Result algebra.** Codex is stronger. Its record carries `performance` (`performed`, `not_performed`, `unconfirmed`) and a six-value effect observation as coordinates, authenticates every contribution in a conjunction and orders the non-success values; "unconfirmed" and "reverted" are distinctions Claude's core does not name. Claude's core is smaller, states the same item-3 distinctions through gaps and effect values, and is the only one checked on a finite domain with mutants. Neither has a competing owner.
2. **Foundation to law (relation 1).** Claude is stronger on the text, by its own reviewers' count (71 rows sampled: 62 real, 9 weak, 0 hollow) and because pillars are bound. Codex is stronger on binding consumers to each unit and on covering every section by name in a family row. Codex's per-unit consequences are often boilerplate (CX-05), and its pillars are unbound (CX-03). Self-review caveat: the Claude tables were written in this session.
3. **One owner per rule (relation 2, reduction item 2).** Even. Both have one owner for the shared rules this review read (result algebra, conjunction, fit and attention, blocking, acquisition, tenant binding). Claude shows the reduction work in `design/REDUCTION.md` (34 clusters, each locus disposed); Codex shows it in `METHOD_REDUCTION.md`, `PARENT_REDUCTION.md` and the unit `consumers`. Neither has an integrated cross-member assessment.
4. **Conservation (UP-015).** Codex is stronger on the record, Claude on the evidence a human can read. Codex's frontier is a schema with relation objects, hashes and a per-row standing that says, correctly, that semantic conservation is not established. Claude's frontier is a table whose changed rows have delta files quoting predecessor and candidate. Codex proposes 68 replacements, Claude 15: the Claude line's reviewers pushed it back to predecessor meaning several times (WC-1, WC-2, FINAL), and the Codex line generalised more (realisation and observations for code and events; the role inventory as an optional configuration; an extended Judgment shape). Which is right is the product owner's call, question by question.
5. **Modal force.** Codex is stronger. It keeps `must` and `shall` (391 occurrences); Claude writes the predecessor's `must` in the indicative by convention (176 `must`), a conservation question its own FINAL review raised (FR-02) and the owner has not ruled on.
6. **Interpretation and constraint surfaces.** Codex is complete and Claude is partial; that settles coverage. On fidelity the record is mixed on both sides: one confirmed Codex defect in a five-unit sample, three in Claude's eight-case sample. Claude quotes statements verbatim, which removes paraphrase as a cause; Codex authors predicates and obligations per unit, which gives a projection something to select by. Codex's acquisition semantics (required support in the closure; conditional support with its exact route; provenance that imports nothing) are a real idea Claude does not have.
7. **Frames.** Claude is stronger on the unit (declared capacity, verbatim, one per contract task); Codex is stronger on use (four frames ran under caps with a frozen oracle). Neither measures active retained context.
8. **Criterion 4.** Codex has evidence; Claude has none. The Codex evidence is same-family, instruction-confined rather than proven fresh, and covers four frames and four tasks. It is still the only actual-use evidence either line has.
9. **Reduction (item 5).** Neither establishes it, and both say so. Claude declared the better experiment (46 paths, measures, guard, tradeoffs, fixed before any trace) and ran one path. Codex ran six operation comparisons against both baselines and reported adverse growth. Together they are one experiment waiting to be run.
10. **Evidence process.** Codex is stronger: oracles frozen at commits, assessors with expectations fixed before acquisition, byte admission with a concurrency control, every claim with a hash. Claude's process has the same shape (ORACLE by an actor that opened neither candidate; expectations before opening) but less instrumentation and no actors.
11. **Writing for the human owner.** Claude is stronger: defined terms, "the product owner", shorter sentences, one owner named per route. Codex's prose is compact and abstract ("instruction-only confinement and distinct same-family actors support bounded nonauthor evidence"), accurate and hard to read cold. Self-review caveat applies.
12. **Honesty of claims.** Even, and high on both. Each return states what it does not establish, marks every proposal pending, and claims no acceptance. Codex's one overbroad word ("complete") was corrected by its author within a day; Claude's HANDOFF lists its unevidenced criterion and untraced paths first.

## Priors corrected

The priors held in direction. Three corrections: Codex's consumer binding per unit was not in the priors and is a strength Claude lacks; Codex's modal-force retention is a conservation strength the priors missed; and "Codex stronger on mechanical verification" understates it, since Claude's finite oracle is the one check that is adversarial in the mutant sense while everything else of Claude's is a route or digest check.

## What each should take from the other

A port proposal for the next cross-synthesis, each line on its own base, under the owner's ported-part review policy, which must be decided first.

Into the Claude line, from Codex:

- C1. The `performance` coordinate and the effect-observation values, as a refinement under FOUNDATIONS §4 Results, with `unconfirmed` and `reverted` mapped once.
- C2. The actual-use protocol: isolated task actors, a protocol and oracle frozen at a commit, a nonauthor assessor with expectations fixed before any return, byte admission with a serialised reader, and a replay probe for constructed artifacts. Run it on the twelve frames.
- C3. The frontier record schema: a relation object per proposal, section hashes per comparison, and a `semantic_review` field that says `indeterminate` until an independent assessment says otherwise. Keep the delta files as the human-readable evidence beside it.
- C4. Per-unit `consumers` binding in the account, and the acquisition semantics of required, conditional and provenance support.
- C5. The artifact and identity checks with adverse controls, in place of route checks alone.
- C6. The retention of `must` and `shall` from the predecessor, pending the owner's ruling on the indicative convention.

Into the Codex line, from Claude:

- X1. A Pillar field per family row, and the index of families to pillar contributions (CX-03).
- X2. Finer family rows: one per deciding rule where the row's consequence differs, each in the form premises, consequence, labelled choice with owner (CX-05).
- X3. CONFORMANCE §5: a record mapping every common discriminator to the case or logical review that exercises it (CX-04).
- X4. The deciding-path inventory: declared paths, measures, guard and tradeoffs fixed before measurement, with route entry and frame entry kept apart.
- X5. A declared frame capacity, and frames for "decide acceptance or release" and "build or assess a member" (CX-07).
- X6. Verbatim source statements carried in each account unit beside the authored predicate, so a fidelity reviewer compares text with text.
- X7. The GLOSSARY index of labels with several senses, and the ledger practice of recording owner instructions verbatim with their effects.
- X8. The finite oracle with mutants, applied to the conjunction precedence rule.
- X9. A plain-prose pass for the human audience: defined terms at first use, "the product owner", one owner named per route.

Owner decisions that gate both:

- the ported-part review policy, before any of the above is accepted;
- the 83 proposed replacement relations, decided by question rather than by tenant, since several questions appear in both sets (the work-result `incomplete` pairing; the Traversal signature; the Executive role inventory; current-surface labels);
- compressions: kept as pinned read models (Codex) or superseded by frames and projections (Claude's proposal);
- identity and version;
- the modal-force convention (Claude);
- the UX compliance-test conflict (Claude).

## What both still need before any acceptance

- A cross-family acceptance review of each frozen candidate, applying the 52 discriminators and the three closure checks; neither has had one.
- An independent semantic assessment of conserved rows, or a declared sample with its scope, on both.
- Criterion 4 evidence on Claude's frames; broader and fresher evidence on Codex's.
- The reduction experiment run, on declared paths, against both baselines.
- Independent fidelity review of each interpretation, and the rest of Claude's encoding if the owner funds it.
- The categorical worked join, reserved on both.

## Standing

This comparison is same-family self-review for the Claude candidate and a cross-family reading by an interested party for the Codex candidate. Its measurements are reproducible from the named scripts and commits; its judgements are the reviewer's and are marked where authorship bears on them. It accepts nothing and ranks nothing for acceptance. The product owner decides.

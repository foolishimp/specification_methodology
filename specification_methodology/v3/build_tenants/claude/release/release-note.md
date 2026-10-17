# STDO 3.0.0 RC4, Claude line candidate

Release note of the Claude line's fourth release-candidate cut of the STDO
Specification Methodology, version line 3.0.0, candidate 4. It is
reconciled to the exact subject it ships with: the freeze commit on
`tenant/claude/c3-synthesis` (commit A of RELEASE §7's two-commit
construction) that holds this file. The cut is not published: the local
tag over commit A is tenant-namespaced, no product tag or selector exists,
and the manifest that binds commit A follows in commit B. Publication, the
product's tag and the selector are the product owner's and the common
pen's acts (RELEASE §3, §7). Nothing in this note is accepted. Every count
below is read from the record (`qualification/C3-ITER5/COUNTS.json`).

## Identity and refs

- Version line `3.0.0`, candidate `rc.4`; local tag
  `specification_methodology-claude/v3.0.0-rc.4` over commit A. Candidates
  1, 2 and 3 stay immutable at `af3b8b7`, `ba882bc` and `9e90169` with their
  tags `specification_methodology-claude/v3.0.0-rc.1`, `-rc.2` and `-rc.3`.
- Project subtree root `specification_methodology/v3/build_tenants/claude`.
- Common input: C3-I5-06 at `4c340f7`; preceding candidate on this line:
  candidate 3, `9e90169`.
- Builder: STDO 2.5.1-rc.2, manifest
  `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.

## Changes since candidate 3

Repairs of the four findings of the affected readback of candidate 3
(main checkout, `.ai-workspace/comments/codex/20261017T092019Z_REVIEW_CLAUDE_CANDIDATE3_FIXES/REVIEW.md`),
accepted on source by this line:

- C3-01. ODD A4: every typed no-action returns its own result for the
  selection predicate by cause, after a closure decision as on
  `initial_selection`; the closure decision keeps its own value for the
  edge predicate, and an earlier result stands for a no-action only where
  it decided the same predicate on the current basis.
- C3-02. The interpretation's control run exits 1 when a control fails, and
  the freeze script fails on any failed step or control; a forced failure
  stops the freeze before its consumers step.
- C3-03. DESIGN_MODULE imports F13, work carriers, for the recurrence rule
  it refines.
- C3-04. The interpretation entry counts five task scopes.

Found by this line's root-cause review of the Codex RC1 repair and included
at the product owner's choice: SPEC_METHOD's constitutional chain, renewal
path and gap procedure re-enter a constitutional gap at the layer its change
class names, writing new goals or intent where the work wave, direction or
scope changes. rc.2 sent every constitutional gap to new goals or intent
beside its own `requirement_reprice`. The three rows are proposed
supersessions pending the product owner's acceptance (Q19), and the two
earlier readings of those sections are marked for reread.

## Changes since candidate 1

Repairs of the seven findings of the independent content review of
candidate 1 (main checkout, `.ai-workspace/comments/codex/20261017T042437Z_REVIEW_CLAUDE_RC1_INTENT_AND_PRODUCT/REVIEW.md`),
accepted on source by this line:

- R1. The manifest admits the whole standards tree: 23 members,
  2 schemas, 24 templates and 13 frame
  files, so bootstrap can copy its template and validate against its schema
  from the installed cut.
- R2. ASSURANCE asks for further evidence only where the observation
  cannot separate subjects on which the assessed predicate takes opposite
  truth values, as its owner FOUNDATIONS §4 states.
- R3. DESIGN_MODULE §4 keeps its preferences and prohibitions binding, with
  the departures its own rules permit (necessary mutable carriers, §10).
- R4. TICKETS §6 owns the recurrence rule as ticket law, as the predecessor's
  ticket method did; DESIGN_MODULE §10 refines it for design review.
- R5. ODD maps a typed no-action to the core result algebra by its cause;
  candidate 4 extends this to a no-action after a closure decision (C3-01).
- R6. CONFORMANCE states its §5 as a qualification map whose expected
  distinctions the construction specification owns, with correct counts and
  no link to the construction specification.
- R7. The interpretation entry describes the current interpretation.

Clean-up of the candidate 2 repairs, found by the author's checks after
that freeze:

- DESIGN_MODULE §4 cites §10 Immutable carriers by its number.
- ASSURANCE §11 no longer adds a clause its owner FOUNDATIONS §4 does not
  state.
- ODD's `evaluate_next` row shows the core result of a typed no-action.
- TICKETS' family table carries the recurrence rule's consequence.
- The frontier note for ODD §11.5D matches the repaired text; the review
  record is regenerated; three earlier readings of sections the repairs
  changed are marked for reread.
- The interpretation's freeze script passes on an unchanged rerun.

Record corrections: candidate 1's note stated 26 members (the manifest
admitted 23) and 505 unread conservation rows (the record had 471); the
interpretation README stated 182 uncovered sections (the record has 183).

## Standing

Every member acceptance criterion is `unresolved`, stated per criterion in
`qualification/C3-ITER5/RESULTS.md`. The product owner put complete
interpretation coverage, the remaining actual-use expectation sets and the
authority compressions out of scope for the baseline.

## Standards inventory

62 files under `standards/`: 23 members, 2 schemas,
24 templates and 13 frame files, each with its SHA-256 in
`release/manifest.json` (commit B) and the member-set digest.

## Plugin inventory

`plugins/spec`, 17 files, version label `3.0.0-rc.4` in both plugin
manifests, digests in `release/manifest.json`.

## Manager inventory

No toolchain manager is cut with this candidate; the installed-release
manager of the builder (STDO 2.5.1-rc.2) applies. The Axiom Indexer that
checks the interpretation is pinned at `axiom_indexer/v2.5.1-rc.2`.

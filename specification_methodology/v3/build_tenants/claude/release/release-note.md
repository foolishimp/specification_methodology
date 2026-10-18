# STDO 3.0.0 RC8, Claude line candidate

Release note of the Claude line's eighth release-candidate cut of the STDO
Specification Methodology, version line 3.0.0, candidate 8. It is
reconciled to the exact subject it ships with: the freeze commit on
`tenant/claude/c3-synthesis` (commit A of RELEASE §7's two-commit
construction) that holds this file. The cut is not published: the local
tag over commit A is tenant-namespaced, no product tag or selector exists,
and the manifest that binds commit A follows in commit B. Publication, the
product's tag and the selector are the product owner's and the common
pen's acts (RELEASE §3, §7). Nothing in this note is accepted. Every count
below is read from the record (`qualification/C3-ITER5/COUNTS.json`).

## Identity and refs

- Version line `3.0.0`, candidate `rc.8`; local tag
  `specification_methodology-claude/v3.0.0-rc.8` over commit A. Candidates
  1, 2, 3 and 5 stay immutable at `af3b8b7`, `ba882bc`, `9e90169` and
  `4a63c92` with their tags `specification_methodology-claude/v3.0.0-rc.1`,
  `-rc.2`, `-rc.3` and `-rc.5`. Candidate 4, `7c64978` with its tag `-rc.4`
  and manifest commit `336b264`, was superseded before review by
  candidate 5. Candidates 6, `9905497` with its tag `-rc.6` and manifest
  commit `d3d8d8c`, and 7, `7cea510` with its tag `-rc.7` and manifest
  commit `ede430e`, were superseded before review by candidate 8.
- Project subtree root `specification_methodology/v3/build_tenants/claude`.
- Common input: C3-I5-06 at `4c340f7`; last reviewed candidate on this
  line: candidate 5, `4a63c92`.
- Builder: STDO 2.5.1-rc.2, manifest
  `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.

## Changes since candidate 5

Repairs of the two findings of the reciprocal review of candidate 5
(main checkout, `.ai-workspace/comments/codex/20261017T135555Z_REVIEW_CLAUDE_CANDIDATE5/REVIEW.md`),
accepted on source by this line:

- C5-01. DESIGN_MODULE §5 Proportional design sequencing takes repeated or
  cross-cutting material surprises as evidence for diagnosis under
  ACTIVATION §1 Feedback and diagnosis. One bounded `design_reframe`
  follows only where the diagnosis establishes that the affected design cut
  is underconstrained; a realisation that alone deviates from a
  decision-complete accepted design is repaired as a
  `realization_refactor`. The family row and the generated Design frame
  carry the same rule.
- C5-02. The interpretation's checker run exits 1 and logs the failure when
  its frame-index enumeration fails or returns no index.

The same class at four more places, which this line's review of Codex RC4
named and Codex's reciprocal addendum (main `06f2cf19`) confirmed: the
eleventh spec-drivenness condition, the persistent-delta drift signal,
ASSURANCE's scenario-writing and scenario-failure sentences and the first
failure-classification row each decided a cause or a re-entry from the
symptom alone. The addendum also named the scenario-writing sentence, which
took a capability for which no scenario can be written as not yet real;
candidate 6 had left it. Each now routes through diagnosis, under
SPEC_METHOD §4 Universal intake triage, ASSURANCE §12 Counterexample
localisation or ACTIVATION §1 Feedback and diagnosis. With C5-01 this adds
four proposed supersessions and extends the drift-signals row, all pending
the product owner's acceptance; Q19 now covers eight rows. No stored reading
covers the changed sections.

The consumers paragraphs of the three diagnosis owners now name the
sections that route to them: ACTIVATION's feedback-and-diagnosis row names
DESIGN_MODULE §5 Proportional design sequencing, EXECUTIVE_BASELINE §20 and
ASSURANCE §1; ASSURANCE's counterexample-localisation row names §1; and
SPEC_METHOD's first change-management row names the constitutional chain,
the renewal path, the eleventh spec-drivenness condition and the drift
signals. The determination record carries the same consumers.

Found by this line's final check: the interpretation's freeze script wrote
the README's artifact digests before its consumers step regenerated
`consumers.json`, so one run could leave that digest stale. It now writes
the digests last.

## Changes since candidate 3

Repairs of the four findings of the affected readback of candidate 3
(main checkout, `.ai-workspace/comments/codex/20261017T092019Z_REVIEW_CLAUDE_CANDIDATE3_FIXES/REVIEW.md`),
accepted on source by this line:

- C3-01. ODD A4: every typed no-action returns its own result for the
  selection predicate by cause, after a closure decision as on
  `initial_selection`; the closure decision keeps its own value for the
  edge predicate, and an earlier result stands for a no-action only where
  it decided the same predicate on the current basis.
- C3-02. The interpretation's control run exits 1 when a control fails and
  refuses a forcing variable that names no control; the freeze script fails
  on any failed step or control, and its checker run fails on any failed
  checker command; a forced failure stops the freeze before its consumers
  step.
- C3-03. DESIGN_MODULE imports F13, work carriers, for the recurrence rule
  it refines.
- C3-04. The interpretation entry counts five task scopes.

The C3-02 class in the verification tools, found by this line's final
check: the link, locus, frontier, frontier-review, install and consumers
checks printed the failures they found and exited 0. Each now exits 1 on a
failure it reports. The two `X_v` notation links and the 17 predecessor
anchors that resolve to no heading by construction (15 clause-split child
rows, 2 common-frontier anchors) are named exactly, so a new one fails.

Found by this line's root-cause review of the Codex RC1 repair and included
at the product owner's choice: SPEC_METHOD's constitutional chain, renewal
path, gap procedure and tenth drift signal re-enter a constitutional gap at
the layer its change class names, writing new goals or intent where the
work wave, direction or scope changes. rc.2 sent every constitutional gap to
new goals or intent beside its own `requirement_reprice`. The four rows are
proposed supersessions pending the product owner's acceptance (Q19), and
the two earlier readings of those sections are marked for reread.

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
  this cut extends this to a no-action after a closure decision (C3-01).
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

`plugins/spec`, 17 files, version label `3.0.0-rc.8` in both plugin
manifests, digests in `release/manifest.json`.

## Manager inventory

No toolchain manager is cut with this candidate; the installed-release
manager of the builder (STDO 2.5.1-rc.2) applies. The Axiom Indexer that
checks the interpretation is pinned at `axiom_indexer/v2.5.1-rc.2`.

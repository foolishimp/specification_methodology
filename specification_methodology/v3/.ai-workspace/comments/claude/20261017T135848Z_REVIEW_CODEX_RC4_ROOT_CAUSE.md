# Review: Codex RC4 root-cause repair, cross-family readback

Author: the Claude tenant session, at the product owner's instruction ("ok
check each others work"). It authored the rival Claude candidate and the
root-cause result that RC4 answers, and none of RC4.

Hypothesis, fixed at 20261017T135848Z after reading Codex's own review record and
before reading the RC4 diff:

- H1: the intake rule that rc.2 holds in several places survives at a site
  Codex did not name. It could be in the standards, the hand-written
  compressions, the plugin or the interpretation's clause statements; the
  constitutional-chain and renewal-path diagrams are the likeliest places.
- H2: a section whose predecessor decision changed is recorded as
  `conserved`. The likeliest is the authorship rule (UP-007), if its
  distinction between reporting a defect and authoring a repair is new law.
- H3: a check that Codex cites as a gate prints a failure and exits 0.
- H4: an item that this line's root-cause result left open has no repair.

Each of H1 to H4 is the class found in this line's own candidate 4 or in
the root-cause result. The review rejects a hypothesis when its test comes
back clean.

## Verdict

**Yes: RC4 repairs the intake root cause at every site this review found,
and its authorship repair holds. Four Low findings remain.**

The predecessor's competing intake rule, that a constitutional gap writes
new Goals or Intent, no longer decides anywhere in the package. The
deciding family now consumes Universal Intake Triage, the owner of change
class and re-entry. The authorship source and its account are repaired.

The nearest miss is in a hand-written compression. RC4 rewrote its
Reviewer sentence to forbid less than the unchanged source, and because the
digest pins match, no identity check can see it. Other clauses of the same
compression still decide the cases tested, which leaves a corner case
(finding 1).

| Coordinate | Value |
|---|---|
| Reviewed package | `92fdb01c52bc4c6c7a7e265f92a668d0adb65098`; branch head `3d2708ef` adds records only, `successor/` identical |
| Predecessor package | `ad384bbeb1e4b19f8d1dd081dbe2d4221f4cc3f6` |
| Review answered | this line's root-cause result, `f3f60f21` |
| Common input; builder | C3-I5-06 `4c340f7`; installed `v2.5.1-rc.2` |

This is a cross-family, source-first readback by a nonauthor of RC4. It
accepts nothing. Codex's review, return and check records were read as
claims and pointers, not as evidence. Every figure below comes from this
reviewer's own reads and scripts at the exact commits.

## Findings

**1. Low: the Reviewer compression narrows its source.** RC4 changed
`standards/authority_compressions/stdo_compressed.md` from "It does not
edit, direct repair, apply an STDO disposition, or authorize continuation"
to "The Reviewer does not implement repairs, direct repair operations,
apply an STDO disposition, or authorize continuation". Its source,
STDO_REFERENCE_FRAME_BASELINE "Reviewer Result And Triage Projection", is
unchanged: "It does not edit the candidate, direct the repair, or authorize
continuation". The Baseline's other two sites also keep "direct repair".

The compression lists `evaluate_review_grade` among its target prompt
families. On the two cases tested, its other clauses still decide as the
source does:

- A Reviewer chooses which of two lawful repairs the Writer makes. The
  unchanged triage clause bars it: "It assigns no priority,
  promotion-boundary effect, disposition, repair, or continuation".
- A Reviewer without a write grant edits the candidate. On this reviewer's
  reading, "missing, ambiguous, or out-of-territory authority refuses" bars
  it.

What remains is a Reviewer that holds a write grant and makes an edit that
repairs nothing and adds no material wording. The source forbids that edit;
the compression no longer does. Codex's readback records that the changed
body preserves the "lawful defect-report/recheck distinction". That holds,
but the readback does not mention the edit bar the body dropped. Owner:
that Baseline section, with FOUNDATIONS Independent assessment.

**2. Low: the Worked Binding is recorded as conserved, though its decision
changed.** REFERENCE_FRAME_METHOD's Worked Binding wrote "invalid_basis on
stale or substituted basis". It now maps stale support under an
interpretable basis to `indeterminate`, and it drops "substituted". That
follows RF-005's replacement, which is proposed and pending. The row says
`conserved` and shows the dependency only by listing RF-005 among its
loci. The example states that it is non-normative, which limits the harm.

**3. Low: the tenth drift signal no longer names a drift.** It now reads
"intake selects the owning layer whose meaning must change". The symptom,
"a code hack", is gone from the list of drift signals. The rule against it
survives in the Method Families row: a lower surface cannot close an
upstream gap by making tests agree. The row is a proposed supersession.

**4. Low: three items from the root-cause result have neither a repair nor
a disposition.**

- The one-actor-several-roles permission still lives only in the optional
  Baseline.
- AC-005's non-transfer of authority is still only implicit.
- The Design Totality Rule still omits continuation and recovery.

Codex's evaluation of the root-cause review does not mention them. The
foundation-to-law finding stands as disputed.

## Hypothesis results

- **H1 rejected.** The sweeps ran in two directions.
  - From the predecessor side, 48 rc.2 members held 86 sentences that send
    a gap, drift, delta, surprise, scenario or failure to re-entry,
    repricing, a reframe or new Goals or Intent. Of these, 25 are changed
    or gone. The 61 that survive verbatim all route through an owner,
    through triage or through "the appropriate constitutional surface".
  - From the successor side, the standards, compressions and plugin, with
    lines joined, give 4 hits on the intake rule and 60 on the wider
    family. None decides re-entry unconditionally, and both diagrams now
    end in "intake-selected re-entry or observation".
  - The interpretation's clause statements are labels only. Its 709
    account determinations hold one hit, and it is compatible.
- **H2 held, narrowly: finding 2.** The account was read for all 16
  successor sections that RC4 changed. Three are new sections with no
  predecessor. Ten carry the changed decisions as proposed
  supersessions: litmus, chain, scenarios, renewal, drift signals, gap
  procedure, design sequencing, Baseline status boundary, failure route
  and anti-patterns. The other three are recorded as conserved:
  UP-007, the Worked Binding, and Independent assessment through the rows
  bound to it.

  rc.2 decides no reporting or recheck case: its UP-007 says only "the
  reviewer is not the author of the reviewed subject". The new permission
  comes from the common C3 contract, PRODUCT.md Independence at `4c340f7`,
  which states it for this construction. The change to rc.2's Baseline
  anti-pattern, "Reviewer edits or directs repair while retaining
  independent-review status", is a proposed supersession. UP-007's own
  conserved row therefore stands.
- **H3 rejected, by reading.**
  - `qualification/C3/rc4/integration/integrate.py verify` and the
    inherited `check_package.py` raise at every failed step. They write
    `writer_result: satisfied` only after all checks pass.
  - `validate_patch.py` fails by `assert`, under Python without `-O`.
  - No adverse run was made. Running the gate writes into Codex's `rc4`
    records and needs its toolchain.
- **H4 held: finding 4.**

## Checked independently

- **The authored diff in full:** six members and five compressions. Every
  intake and authorship item of the root-cause result has a hunk except
  finding 4. The extra hunks fix the shortcuts that this line's readers
  reported: litmus item 11, the scenario explanation, the persistent-delta
  signal, Baseline's wrong-Product route and the design-surprise gate.
- **Identity, by this reviewer's own scripts:**
  - 120 of 120 frame excerpts equal their owner sections, with correct
    member digests. A one-word change to an excerpt was caught.
  - 31 of 31 compression pins match, across all ten compressions.
  - 81 of 81 `SOURCE_INVENTORY` entries match their hash and size.
- **The authorship family across the live surfaces:** no "materially
  authored" text and no generic disclosure duty remain. Nothing in the
  plugin conflicts. The only divergence is finding 1.

## Same class in the Claude line

Claude candidate 5 (`4a63c92`) still carries the five shortcuts that RC4
repaired:

- SPEC_METHOD:329, litmus item 11;
- ASSURANCE:58, the scenario-failure sentence;
- SPEC_METHOD:600, the persistent-delta signal;
- EXECUTIVE_BASELINE:1690, the wrong-Product route;
- DESIGN_MODULE:554, the design-surprise trigger.

Candidate 5's sweeps searched for goals-or-intent wording and did not
reach them, and its package's readback scope leaves them out. Its
Anti-Patterns item 10 (EXECUTIVE_BASELINE:1740) keeps rc.2's wording and has
no recheck rule beside it to conflict with.

## Limits

Not assessed:

- the whole candidate;
- the account's semantic fidelity beyond the sweeps above;
- the gates under an adverse run;
- the numbers Codex reports without a source here, such as the 2,250
  local links.

The hypothesis was committed together with this result, unlike the
root-cause plan (`3c6fc135`), so only this record shows that it preceded
the diff. Codex's line citations served as pointers only. Elapsed time and
token spend are not instrumented.

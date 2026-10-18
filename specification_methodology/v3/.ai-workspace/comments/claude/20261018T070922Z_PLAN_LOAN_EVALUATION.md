# Plan: which Codex elements the Claude baseline should borrow

Author: the Claude tenant session. It wrote the receiving line, so its
interest lies in finding little worth borrowing. The guard below is set
against that interest.

The owner ruled: "we will baseline off claude because its better
structurally for future expansion, and then use codex for loaning". Codex is
running "a full eval on that model to idenfity which elements i should loan
from codex to apply to claude", and the owner asked this session: "i want
you to do the same excercise". This session has not opened Codex's
evaluation directories and will not open them before its result is
committed. This post is commentary. It borrows, accepts, merges or releases
nothing.

## Subjects

| Role | Exact subject |
|---|---|
| Receiving line | Claude commit A `c2cfa9b908d1722ae3f26c32fa4ece691083bdc3` (commit B `3a209713`), label `3.0.0-rc.9` |
| Donor | Codex checkpoint `c46e9f96381097245a6714164f03b72ad32116c0`, package `5592168e`, content identical to `5a5b5ad8` |
| Common input; predecessor | C3-I5-06 `4c340f7`; rc.2 at `c45a6c67` |

Scope, from the owner: a baseline v3 without a_c ("a_c evaluation is out of
scope"). The authority compressions, complete interpretation coverage and the
remaining expectation sets come after the baseline.

## Areas, fixed now

1. **Dispositions.** Both records dispose all 636 body rows of the common
   inventory. They differ on 97:
   - 73 that Claude conserves and Codex supersedes. Codex's record tags 40
     of them with one or more of three shared causes, all from the single
     result algebra: I3-R2-R003 (judgment), R012 (result record) and R015
     (conjunction);
   - 18 that Claude marks not applicable and Codex conserves;
   - 5 that Claude supersedes and Codex conserves;
   - 1 that Claude marks not applicable and Codex supersedes.
2. **Routing and frames.** Codex's entry, task rows and seven frames,
   checked against what the RC9 traces found in the Claude line:
   - no route for evaluating and reusing results (S5);
   - two frames missing from the entry's frame table;
   - route labels that land one hop short;
   - whole-section routes through derivation tables.

   Claude read 362 KB more than Codex on the ten scenarios, mostly on S3
   (+77 KB), S8 (+76 KB), S4 (+54 KB), S9 (+53 KB) and S1 (+51 KB).
3. **Members the lines carry differently.** Codex's TRANSFORMATION_LIBRARY
   (37 KB, with no Claude member of that name), its FOUNDATIONS (85 KB
   against Claude's 146 KB) and its verification material.
4. **Gates and records.** Codex's package check compares:
   - every member with its frozen commit;
   - the frames with a fresh reproduction;
   - 2,250 local links;
   - 32 compression pins;
   - 19 negative identity controls.

   It is set against Claude's 13 commands. Codex's machine record also
   carries the 55 non-body members, which Claude disposes only in its prose
   frontier.
5. **After the baseline.** The interpretation, the compressions and their
   packaging. Codex's 709 determinations are bound to spans of Codex's text,
   so only tooling and packaging structure can transfer.

## Outcomes for a differently disposed claim

Meaning test: a successor changes a claim's meaning when it changes any of:

- an obligation;
- its modal force;
- an exception;
- its scope or applicability;
- which owner holds the claim exclusively.

Moving a rule without changing any of these conserves it
([Cross-Synthesis](../../../specification/PRODUCT.md#cross-synthesis)).

For a claim Claude conserves and Codex supersedes:

- (a) both texts make the same change, and it changes meaning. Claude's
  `conserved` is wrong. Claude borrows Codex's successor relation, records
  the row superseded and adds it to the owner's replacement decisions;
- (b) both texts make the same move, and meaning is preserved. Claude's
  disposition stands;
- (c) Codex's text adds substance that Claude's lacks. This is a content
  loan with a replacement decision;
- (d) Codex's change departs from the common input. It is not borrowed.

For a claim Claude marks not applicable and Codex conserves:

- (e) the claim applies. Claude must carry it, by loan or by restatement;
- (f) Claude's not applicable stands.

For a claim Claude supersedes and Codex conserves:

- (g) Claude's replacement is needed, so it stands;
- (h) conservation suffices. Claude borrows the conservation and withdraws
  its replacement.

The result reports the owner's replacement decisions on the Claude line as
28 + (a) + (c) − (h).

## Classes for each element

- `baseline loan`;
- `owner decision`: a changed meaning, a new member or a withdrawn
  replacement;
- `after-baseline loan`;
- `do not loan`;
- `Claude-only repair`: a Claude gap that no Codex element fills.

## Guard against the author's interest

- Where an advantage is shown and fit is uncertain, the class is
  `baseline loan`. The uncertainty is recorded as evidence to check again.
- `do not loan` needs a cited reason: a lost clause or claim, a conflict
  with the common input, a second owner for a determination, or a measured
  cost.
- 26 of the 73 rows had earlier nonauthor readings, from the same model
  family and without the consumer bindings. They are context only, and
  those rows are read again.

## Each loan record

It carries the fields that Cross-Synthesis requires:

- the frozen source;
- the receiving owner;
- the adaptation;
- the predecessor claims and material dependencies affected;
- the evidence to check again;
- the review that covers it: the receiving line's same-family nonauthor
  Reviewer, with Codex's reading as supplementary.

It also states the byte impact on the frames that quote the receiving owner.
The largest Claude frame holds 144,806 of its 160,000 bytes.

## Readers

Each reader runs on Fable at maximum effort, one at a time, and reads only
its packet:

- A1: the three shared causes, the 40 tagged rows and the 24 rows of the
  other three patterns;
- A2: the 33 untagged rows;
- B: areas 2 and 3.

The disposition packet holds, for each row:

- the rc.2 section;
- each line's record;
- each line's successor loci, as line ranges in full scrubbed copies of its
  members at the exact commits.

It also holds the common PRODUCT, requirements README and ASSURANCE. The
lines are labelled A and B by a key drawn at random and sealed. The seal is
the SHA-256 of `A=…;B=…;salt=…`:
`1c8089fb11c2ef058c26c4b8270c55ac3a3b1f9a3b0e23c9ba9df77638a41e3f`. Member
names and record styles still identify the lines, so the blinding is weak.

This session does areas 4 and 5 and the measurements. The builder, the
measurement scripts and the 251 packet hashes are in
[assets/20261018T070922Z_LOAN_EVALUATION/](assets/20261018T070922Z_LOAN_EVALUATION/).

## Not covered

- actual use;
- acceptance;
- any change to either line;
- Codex's own evaluation.

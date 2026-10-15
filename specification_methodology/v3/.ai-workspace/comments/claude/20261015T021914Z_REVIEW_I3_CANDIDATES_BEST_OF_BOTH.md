# REVIEW: the two iteration 3 candidates, and what each should take from the other

**Author**: Dimitar Popov
**Date**: 2026-10-15T02:19:14Z
**Addresses**: the Codex candidate at `c29b2be` (input `C3-I3-CLOSED-01`, `1fce537`) and the Claude candidate at `2beed8d` on `tenant/claude/c3-synthesis` (input `C3-I3-R2-01`, `355aa86`)
**Status**: Expectations recorded before measurement. Results and the recommendation follow under a later commit.

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

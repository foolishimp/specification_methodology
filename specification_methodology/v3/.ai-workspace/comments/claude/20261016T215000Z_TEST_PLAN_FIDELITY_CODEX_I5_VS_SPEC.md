# Test plan: fidelity of the Codex I5 candidate against the specification, read blind beside the Claude candidate

Author: the Claude tenant session, acting at the product owner's instruction
as test manager for the Codex candidate ("act as codex's test manager and
do the work"; "a clean comparison against specification, not either of you
checking your own homework"). Written before any result of the reads below
was seen. The reads are performed by fresh-context Fable actors that
authored neither candidate; the candidates are presented to them as A and
B with tenant names replaced, and the key is held by this session and
disclosed with the results. Same-family evidence for the Claude candidate
is disclosed as such; no cross-family actor is available to this session.
Nothing here accepts or ranks a candidate; the product owner decides.

## Subjects

- Specification: C3-I5-06 at `4c340f7` (requirements/README Universal
  Construction Requirement; PRODUCT Construction And Context Management,
  Universal Construction Model, the six criteria; requirements/ASSURANCE;
  REFERENCE_FRAME_BASIS; requirements/PREDECESSOR_CLAIMS).
- Codex candidate: documentary source `1e4bed6` (`successor/standards/`),
  conservation record from the return `28d87ee` (`CONSERVATION.json`, 691 rows).
- Claude candidate: `733ccd2` on `tenant/claude/c3-synthesis`
  (`standards/`, `frontier/REVIEW.json`, 647 rows, with the frontier table).
- Predecessor text: the installed release `stdo://releases/v2.5.1-rc.2/`.

## Tests

1. **Owner-text fidelity.** One actor reads the specification first and
   fixes at least 45 expectations, one per obligation sentence of the
   construction and assurance requirements and the frame basis; then reads
   each candidate's owner sections for the construction relation and the
   assurance relations, blind, and records per expectation `present`,
   `changed` (how) or `absent`, plus contradictions and binding additions;
   tallies and a judgment. Launched at 2026-10-16T21:48Z.
2. **Conservation sample.** 28 predecessor claims selected by a fixed rule
   (every 23rd row of the common claim tables from the twelfth row, in file
   order; 636 rows parsed), each presented with the rc.2 text and both
   candidates' recorded disposition and the text at their successor loci.
   The actor judges, per claim and candidate, whether the meaning is
   conserved, changed, absent or not locatable, and whether the candidate's
   own disposition is right. Packet SHA-256 `9e0decd334da2b9e81dd85256281a4cb68f87ec3ed62fc4f500811db76b971af`
   (415,217 bytes). Run in two halves, one actor each, after test 1.
3. **Consumers of unowned determinations (Codex only), if budget allows.**
   20 of the 389 determinations the Codex record lists without a consumer,
   chosen by the same stepping rule: does the candidate text carry an
   actual consumer, and does the record's absence claim hold?

What the tests cannot show: the reading quality of the rest of either
corpus beyond the samples; actual use, which only the criterion-4 trial
shows; any acceptance standing.

## Results

Posted separately when the reads close, with the A/B key.

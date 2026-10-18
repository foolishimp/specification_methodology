# Plan: evaluation of the two RC9 candidates, fixed before the blind reads

Author: the Claude tenant session, author of the Claude line, at the product
owner's instruction: "we have two stdo v3 RC9 candidates from claude & codex
given our last major comparison I want a full evaluation between the two
implementations, and which one should I take to V3 released", and "you are
both running in parallel and the quality of each evaluation is a factor".
The owner runs Codex's evaluation of the same subjects in parallel; it
supplies the other model family. Its working directory
`comments/codex/20261018T040150Z_RC9_COMPARISON/` is present, uncommitted, in
the main checkout. This session has not opened it and will not open it
before its own result is committed.

## Subjects

| Line | Exact subject |
|---|---|
| Codex | package `5592168e26759f37e730aed12c030a6061709ec4` (content of `5a5b5ad8` with five label and coordinate files changed); records checkpoint `c46e9f96` on `tenant/codex/c3-iteration-5` |
| Claude | commit A `c2cfa9b908d1722ae3f26c32fa4ece691083bdc3`, local tag object `ac905d6`, commit B `3a209713` on `tenant/claude/c3-synthesis` |
| Common input; builder | C3-I5-06 `4c340f7`; installed `v2.5.1-rc.2` |

## Already observed, before this plan

These are this session's own runs on Git objects, not blind, and are reported
in the result:

- the identity of each RC9 against its reviewed predecessor;
- each line's reproduction suite in a disposable clone, with one-word fault
  injections;
- corpus and frame sizes against rc.2;
- interpretation coverage computed from each line's artifacts;
- verbatim rc.2 retention;
- release-manifest membership;
- conservation-record standing.

## Blind reads

The reader is a fresh-context general-purpose subagent on Fable at maximum
effort. It authored neither candidate. Readers run one at a time. Each reads
only its packet directory.

Readers are Claude family, the same family as the Claude line. That is a
disclosed limit, and the owner's parallel Codex evaluation is its
counterpart.

Blinding:

- A and B were drawn at random. The key is sealed as the SHA-256 of
  `A=<line>;B=<line>;salt=<hex>`:
  `16e4156b2ba31a8c92e67e47a0abe90b65177dc34f39fff2443910a073eb0507`.
- Tenant names are scrubbed from candidate and common text.
- Member names, structure and style can still identify the lines, so the
  blinding is weak.

The packet hashes are in
[PACKET_SHA256.txt](assets/20261018T042139Z_RC9_COMPARISON/PACKET_SHA256.txt)
(SHA-256 `342dead4…`). The builder and measurement scripts sit beside it.

1. **Owner-text fidelity.** This re-runs I5 test 1 with the same 65
   expectations, fixed at I5 by a fresh reader from the common text
   ([EXPECTATIONS_65.md](assets/20261018T042139Z_RC9_COMPARISON/EXPECTATIONS_65.md)),
   and the same owner-section locators. It gives a direct I5-to-RC9 change
   on both lines.
2. **Ten scenario walkthroughs, by route, on both candidates.** Two readers
   run them: S1 to S5, then S6 to S10. Entry is each candidate's installed
   `standards/README.md`. The reader records hops, bytes acquired, the
   reconciliations it had to make and decisions it could not reach. It
   grades each scenario after tracing all of them
   ([SCENARIOS.md](assets/20261018T042139Z_RC9_COMPARISON/SCENARIOS.md),
   [EXPECTED.md](assets/20261018T042139Z_RC9_COMPARISON/EXPECTED.md)).
   - S1 to S5 are the five scenarios of this line's RC1 review of Codex.
   - S6 and S7 test classes found against the Codex line: intake re-entry,
     and a generic assessment that names code.
   - S8 and S9 test classes found against the Claude line: observation
     sufficiency, and what a reported failure shows.
   - S10 is acceptance with a pending replacement.
   - Expected distinctions are quoted from the common conformance tables,
     the common requirements or rc.2. The test manager wrote the ten
     situations and three readings marked as such.

These are desk traces. Under Candidate Comparison they cannot satisfy
criterion 4.

## Hypotheses

- **H1.** On the 65 expectations, the I5 gap of 13 `present` has narrowed
  to at most 5, because Codex's RC1 repair restored the seven dropped
  construction conditions. Neither candidate contradicts the
  specification.
- **H2.** Each candidate delivers at least 8 of the 10 scenarios. Neither
  is `not delivered` on S1 to S5.
- **H3.** After their repairs, the Codex line delivers S6 and S7, and the
  Claude line delivers S8 and S9.
- **H4.** Claude's median bytes acquired per trace exceed Codex's, and
  Claude's median hops are no more than Codex's.

## How the answer is decided

The qualified answer follows from the ratified rule: no qualified choice.
Every criterion is `unresolved` on both candidates, and the shared protocol
has not run.

The basis recommendation weighs two things:

- (a) distance to a release that meets the written Product;
- (b) matched method quality from H1 to H4.

Already measured under (a):

- **Codex leads on:**
  - complete interpretation in its package;
  - compressions carried;
  - an identity gate over every member;
  - a clean cross-family readback of its final content;
  - a smaller corpus.
- **Claude leads on:**
  - recorded nonauthor conservation reading;
  - fewer replacement decisions.

The reads decide the recommendation as follows:

- If they show parity or a Codex lead on decision correctness, the
  recommendation is Codex.
- A material Claude lead is any of:
  - at least two more scenarios delivered;
  - a Codex decision graded `not delivered` that Claude delivers;
  - at least 8 more `present` expectations.

  In that case, the result states the tradeoff and each path's cost to
  release, and does not default to the author's line.

## Not covered

- actual use;
- conservation beyond the existing samples;
- interpretation fidelity;
- acceptance, merge, release or any change to either candidate.

# Exact-Cut Review: STDO `v2.2.0-rc.1`

- reviewer: claude (independent)
- date: 2026-07-25T05:30Z
- subject: annotated tag `v2.2.0-rc.1` (`bb4a2c0b`) → commit
  `5326562f075d60052806d0d2c79d3db49671a8ea`, tree `dd6a473b`
- predecessor: released `v2.0.0` at `94ccf4fa`
- carriers on origin: `rc/2.2.0` and
  `codex/stdo-2.2-continued-growth-authority`, both at `5326562f`

## Verdict

**Mechanically exact; release-law self-reference resolves lawfully; one
unevidenced claim; coverage limits stated.** I am the reviewer, not the
acceptance authority — this record is an input to F_H acceptance, not a
substitute for it.

## Verified Exactly

| Claim | Result |
|---|---|
| Aggregate digest | `ca6dc3d5094fc5473380df45d76da3c52263c5c21c52a3af62f542c97db2f86c` — recomputed from `git archive v2.2.0-rc.1`, **exact match** to the claim and to the note |
| Member count | 41 / 41; no member added, removed, or renamed |
| Declared changed members | **17/17 hashes verify**; declared changed-set **exactly equals** actual changed-set |
| Conserved members | note claims 24; **24 found, 0 differ** from `v2.0.0` |
| Line count | 9,792 (declared 9,792) vs 9,482 — +310, 3.27% |
| Compression bindings | **13/13** `source_digest`/`source_digests` verify; no stale compression |
| Whitespace | trailing 0, tabs 0, CRLF 0, missing-final-newline 0 |
| Ancestry | `v2.0.0` **is** an ancestor; 7 commits; previously reviewed `14261467` is an ancestor |
| Tag | annotated, tagger Dimitar Popov, points at `5326562f` |
| Single-copy risk | **retired** — RC tag, `rc/2.2.0`, and authoring branch all on origin |

## The Load-Bearing Question: Which Release Law Governs This Publication?

`RELEASE_METHOD.md` is itself a changed member in this RC. The cut amends the
release law under which it is being published, and the procedure proposed for
publishing it (zero-delta final at the RC commit; work-state closure recorded
afterward) is authorized by the **new** law — which is not yet operative.

I checked this against **operative `v2.0.0`** law and it holds:

1. v2.0.0's Candidate Flow steps 10–11 require release-scoped assets updated
   and the release note finalized before the release commit. The RC's note has
   been rewritten with a **Publication Boundary** section: "It carries no
   mutable candidate, review, acceptance, branch, or tag-existence state."
   I grepped it — there is no status or tag-existence claim anywhere in it.
   Nothing in the note becomes false at tap, so steps 10–11 are satisfied with
   no edit and the RC commit *is* a lawful release cut.
2. `specification/GOALS.md` still carries `M3 active` / `M4 pending` /
   "No `v2.2.0` release exists," which do become false at tap. But GOALS is
   **not** a release-scoped asset under v2.0.0's own enumeration (release
   notes, RC/known-limitation notes, release manifests, version references in
   release-facing docs, install/operator guidance, branch and tag references).
   It is source-project work state.

So zero-delta publication at `5326562f` is lawful under the predecessor law,
and the new law reaches the same result by explicitly declaring GOALS
milestone cells and T-002 bookkeeping as excluded state. The self-reference
does not create a circularity.

Making the note status-free is the correct fix to a real paradox in v2.0.0's
sequence — the old flow guaranteed the reviewed RC could never be
byte-identical to the final. Worth recording as sound.

## Prior Findings

- **N1 (admission surface) — FIXED, and well.** SPEC_METHOD now reads
  "further material work requires a new admission by the owning authority or
  its explicitly bounded proxy," with an anti-laundering clause ("Drafting or
  validating a ticket or execution contract, retaining active status, or
  holding a prior admission cannot create, extend, or renew the basis").
  Stronger than the one-line repair I proposed.
- **N2a — addressed**; the truncated "exhausted or falsified" phrasing is gone.
- **N2b — open (trivial).** `ticket_method.compressed.md:44` still says
  "exposes competing authority," dropping "or ambiguous."
- **H1 — open.** Still no `package.json`, `Makefile`, `gates/`, or CI. The
  compression staleness predicate and the member/whitespace checks remain
  reviewer-run, not machine-run.

## F1 (Process): The Three Exact-Tag Reviews Have No Durable Record

The publication request states "Three exact-tag reviews: ACCEPT, no P0/P1/P2
findings." I cannot find them.

- `git ls-tree -r v2.2.0-rc.1 -- .ai-workspace/` returns five files: two
  2.0-era codex checkpoints, the 2.0 human DECISION, T-002, and completed
  T-001. **No 2.2 review record.**
- The working tree adds only my own two untracked reviews and a codex strategy
  post.
- Repo-wide, the only files referencing `5326562f`, `v2.2.0-rc.1`, or
  `ca6dc3d5` are my two reviews and the release note.

This is the third appearance of this claim shape today: "three independent
audits: clean" (this morning, no record), H2 in my 04:29Z review (no committed
review record for 2.2), and now three exact-tag ACCEPTs. Each time the
mechanical claims that *can* be checked have held — I am not alleging the
reviews didn't happen. The defect is evidentiary, and it now bites, because
this RC's own **Tap Criteria** add "the immutable RC has passed required
exact-cut review," and its Candidate Flow step 7 requires "independent
exact-cut review of that immutable RC." Those criteria are satisfied by
records, not by assertion.

Cheap fix: land the review records on the continuing source branch. The RC's
own new law explicitly permits this without moving the tag.

## Coverage Limits Of This Review

The increment from my last reviewed subject (`14261467`) to the RC is 504
insertions / 213 deletions across 16 members — two new supersession families
(five total, up from three). I verified **all identity, all hashes, the
complete `RELEASE_METHOD` diff, the fifth-family text, the note's
status-purity, N1's repair, and the GLOSSARY/POSTING mapping** to declared
family 2.

I did **not** line-by-line verify: `ODD_METHOD.md` (+98), `TICKET_METHOD.md`
(100), `IDENTITY_METHOD.md` (38), the remaining `SPEC_METHOD.md` changes (41),
or compression content fidelity for the two new families. Those rest on
digest binding and declared-supersession mapping, not on my reading.

If the three claimed reviews cover that content, this review composes with
them and the gap closes. If they cannot be produced, that content has not been
independently read by anyone whose record exists, and I should finish it
before tap.

## Recommendation

Nothing I found blocks the release subject. The remaining gate is evidentiary
and procedural, not defect-driven:

1. Produce the three exact-tag review records, or commission the increment
   review to close the coverage gap above.
2. Land review records on the continuing source branch (lawful without moving
   the tag).
3. F_H acceptance of the exact subject, final carrier, and final-delta
   relation — Jim's decision, not the reviewer's.

# Independent Review: STDO `v2.2.1-rc.2` Acceptance Gate

- reviewer: claude (this session — see disambiguation below)
- date: 2026-07-27T02:00Z
- subject: annotated tag `v2.2.1-rc.2` (`cad1a07b`) → commit `05f8edab`,
  tree `9e93c6a6`
- predecessor: released `v2.2.0` at `5326562f`

## Verdict

**The subject is sound and final-ready. Both of my findings on the earlier
candidate were resolved, one of them better than I proposed. I have no
blocking finding.**

I am not issuing the requested ruling. Acceptance is F_H's seat, and this
release's own law binds "the exact release subject, final carrier identity,
and final-delta relation" to direct human authority. A reviewer signing it
would collapse the two seats the 2.2 line was written to keep apart. What
follows is the review input to that ruling.

## Disambiguation — Which Claude Review Is Which

The evidence cites
`claude/20260726T155448Z_REVIEW_stdo_2_2_1_rc2_exact_cut.md`. **I did not
write that file.** It self-describes as "a heterogeneous read-only review,"
i.e. a separately-instanced Claude. That is lawful decorrelation and good
practice — but it means "heterogeneous Claude reviews" in the report should not
be read as this session having already cleared RC2. **This is my first review
of RC2.** My prior STDO reviews are the 2.2.0 RC review and the `c412cf15`
candidate review.

## Identity And Ancestry — Exact

| Check | Result |
|---|---|
| `v2.2.1-rc.2` → commit | `05f8edab` — **exact** |
| Tree | `9e93c6a6` — **exact** |
| Standards aggregate | `df1064de…20aed` — **recomputed exact** |
| Release-note SHA-256 | `900a05d5…705b` — **exact** |
| RC tag on origin | present (`cad1a07b`), plus `rc.1` |
| Final `v2.2.1` / `release/2.2.1` | **absent**, as stated |
| `v2.2.0` is an ancestor | **yes**, 7 commits |
| Rejected lineages (`c6c085a`, both archives) | **not** ancestors |
| Abandoned `origin/main` | **not** an ancestor |

## Qualification Conditions — All Verified

| Condition | Result |
|---|---|
| 41 members, no add/remove/rename | **41**, path set identical to `v2.2.0` |
| 9 changed / 32 conserved | **9 / 32** — declared set equals actual |
| All 9 declared member hashes | **9/9 reproduce** |
| 13 compression bindings | **13/13, 0 stale** |
| Whitespace: trailing / tabs / CRLF / final newline | 0 / 0 / 0 / 0 |
| Line growth | **9,991 vs 9,792 = 199 = 2.03%** — note states exactly this |

Note the growth is 199 lines / 2.03%, not the 142 / 1.45% quoted for the
earlier candidate. That is correct — the RC1→RC2 repairs added law. The note
carries the current figures; the report simply did not restate them.

## Zero-Byte Final Delta — Verified Independently

The branch has advanced three commits past RC2 (`f1347cc` qualification
record, `255edac` reviews, `d2f9ac5` final-delta proof). I recomputed at
current `HEAD`:

- standards aggregate: `df1064de…20aed` — **identical to RC2**
- release-note digest: `900a05d5…705b` — **identical to RC2**

The post-RC commits touch only `.ai-workspace/` and `specification/GOALS.md`,
and the note explicitly declares GOALS milestone state and ticket bookkeeping
as excluded source-project state. So publishing `release/2.2.1` and `v2.2.1`
**at `05f8edab`** preserves the reviewed subject byte-for-byte, and the
zero-delta claim holds under the release law 2.2.0 established.

## My Two Prior Findings — Both Resolved

**F1 (supersession classification) — resolved, and better than I asked.** I
argued the co-evolution admissibility change read as a supersession while
being classified a clarification. RC2 now states plainly:

> The co-evolution admissibility predicate is a bounded supersession. `v2.2.0`
> permitted retained design, implementation, and tests to co-evolve while
> material design relations outside its unresolved-architecture test were still
> being discovered, provided they were reconciled before promotion. Under
> `v2.2.1`, retained co-evolution inside an adopted Design Module Method
> boundary requires `decision_complete(B)` across the complete `M(B)`…

It also closes the scope gap I raised in the same finding: "Outside an adopted
Design Module Method boundary, the retained generic
no-unresolved-material-design-decision test applies." I asked for a
"This supersedes" sentence; what landed is an exact before/after statement
plus explicit preservation of the predecessor test outside the new scope.

**F2 (durable review record) — resolved.** The three evidence records are
committed (`255edac`, `d2f9ac5`). They are *not* inside the RC2 tag, which is
correct rather than a gap: a review of an immutable RC cannot live inside its
own subject, and the release law provides for recording it afterward on the
continuing source branch without moving the tag.

This is the finding I raised eight times across STDO and ABG. In 2.2.1 it
became law, and the same release now satisfies that law on itself.

## Main Reconciliation

The requested ruling includes "reconciliation of main without merging the
abandoned remote-main line." That matches what I verified on the earlier
candidate and re-confirmed here: `origin/main` does not descend from `v2.2.0`,
and its two method commits' content was already replayed into the release
lineage. So the reconciliation is a **ref decision, not a content merge** —
correct as worded.

## Recommendation

Nothing blocks. If Jim accepts, the sequence is: publish `release/2.2.1` and
`v2.2.1` **at `05f8edab`** (not at current `HEAD`), then record
publication-caused work-state closure afterward on the continuing branch
without moving the tag.

Two things I would not want lost in the acceptance: the growth figure is
199 lines / 2.03%, not the 142 / 1.45% in the report; and the cited Claude
review is a different instance than this one.

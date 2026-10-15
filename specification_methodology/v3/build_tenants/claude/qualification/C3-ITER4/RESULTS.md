# Results of the iteration 4 candidate against the six criteria (I4-09)

Standing of the Claude line's iteration 4 candidate under the six member
acceptance criteria of the ratified C3 construction contract and the
three integrated closure checks, in the ratified vocabulary: an
obligation is `satisfied`, `falsified` or `unresolved`. Every assessment
named here is same-family working evidence unless it says otherwise; a
missing assessment leaves the obligation `unresolved` and never counts as
`falsified`. The exact candidate is the freeze commit named in the
handoff. This file is updated at that freeze.

| Criterion | Evidence held | What is missing | Standing |
|---|---|---|---|
| 1. One disposition per row; loci resolve to the required text | 645 section rows and 9 child rows, each with exactly one disposition (`frontier_check.py`); 754 loci resolve to headings (`locus_check.py`); `frontier/REVIEW.json` binds each row to its predecessor and successor section hashes | a reviewer's check that each named locus carries the whole claim, not only a heading | `unresolved` (structural checks pass) |
| 2. Conservation, author-independent comparison | the I4-04 reading of the 140 rows in `reassess/` by a same-family nonauthor (results in `frontier/REVIEW_ASSESSMENTS.json` and `REVIEW.json`); WC-2's 30 verified rows at I3 | the same reading for the other conserved rows; cross-family comparison; the product owner's decisions on the proposed relations that conserved rows depend on | `unresolved` |
| 3. Superseded rows name an accepted relation | 15 rows and 10 compressions proposed, listed by question for the pen (`main` `708dfb9`) | the product owner's decisions | `unresolved` (no relation accepted) |
| 4. Frames fit, fresh actor uses them correctly, judged against independent expectations | 12 frames with family rows, `--check` exit 0, declared capacity 150,000 bytes, largest 147,702; fit rule in ACTIVATION §2 step 3 | any actual use: D5 is undecided, so no fresh actor has used a frame; fit of a frame in an actual actor context is unmeasured, so fit is `indeterminate` | `unresolved` |
| 5. Discriminators hold under source-first review; interpretation preserves owned determinations | CONFORMANCE §5 maps the 52 discriminators and J53 to J55 to loci on the successor; the checker returns `valid` with adverse controls; 8 fidelity cases at I3 with 3 repairs read back in R2a; `consumers.json` binds consumers to the 64 clauses | required coverage: 64 clauses cover the shared-owner determinations of G1 to G4 only; 15 sections `encoded-in-part`, 181 `not-encoded-i3`, G5 to G13 not encoded; the consumer semantics beyond citation are unread; the source-first review of the discriminators on the successor is the R1, R2a and R2b readings only | `unresolved` |
| 6. Reduction within the cone; deciding-path comparisons | REDUCTION §3 (34 clusters) and §4 (46 paths, dimensions, outcome rule, tradeoffs; TO1 realised and disclosed); DP-43 traced on three subjects at I3 | DP-43 is `indeterminate` against both baselines; 45 paths untraced; no frame-entry trace; preceding candidate now `2beed8d`, against which no path is traced | `unresolved` |
| J53 integrated reduction | as criterion 6 | the integrated assessment | `unresolved` |
| J54 no proposal presented as accepted | every `superseded` row and every relation says proposed and pending; the ledger and handoff claim no acceptance | a reader's confirmation | `unresolved` (no counterexample known) |
| J55 five satisfied and the sixth missing | not reached: no member has five criteria `satisfied` | | `unresolved` |

Eligibility under the ratified comparison rule: a candidate qualifies
only when all six criteria and the integrated obligations are
`satisfied` on the exact candidate. This candidate does not qualify at
this freeze. Nothing above is a `falsified` result: no assessment has
defeated an obligation; the obligations are unassessed or depend on the
product owner's decisions.

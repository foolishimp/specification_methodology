# Results of the iteration 4 candidate against the six criteria (I4-09)

Standing of the Claude line's iteration 4 candidate under the six member
acceptance criteria of the ratified C3 construction contract and the
three integrated closure checks, in the ratified vocabulary: an
obligation is `satisfied`, `falsified` or `unresolved`. Every assessment
named here is same-family working evidence unless it says otherwise; a
missing assessment leaves the obligation `unresolved` and never counts as
`falsified`. The exact candidate is the freeze commit named in the
handoff.

| Criterion | Evidence held | What is missing | Standing |
|---|---|---|---|
| 1. One disposition per row; loci resolve to the required text | 707 keyed rows of the common inventory present once, plus 11 child rows, each with one disposition (`frontier_check.py`); 759 loci resolve (`locus_check.py`); `frontier/REVIEW.json` binds each row to its predecessor and successor section hashes; Codex's review reproduced the 12 frame pins and 195 frame-owner pins | a cross-family check that each named locus carries the whole claim | `unresolved` (structural checks pass) |
| 2. Conservation, author-independent comparison | 140 rows read by same-family nonauthor Fable activations in fresh contexts: 137 `conserved`, 3 the clause split to a proposed-replacement child row (`frontier/REVIEW_ASSESSMENTS.json`); the repaired `#constitutional-chain` row read back; WC-2's 30 verified rows at I3 | the same reading for the other 505 conserved rows (author disposition only); cross-family comparison; the product owner's decisions on the proposed relations that conserved rows depend on | `unresolved` |
| 3. Superseded rows name an accepted relation | 17 rows and 10 compressions proposed, listed by question for the pen (`main` `708dfb9`, supplement in `reassess/REPLACEMENTS-SUPPLEMENT.md`) | the product owner's decisions | `unresolved` (no relation accepted) |
| 4. Frames fit, fresh actor uses them correctly, judged against independent expectations | 12 frames with family rows, `--check` exit 0, capacity 150,000 bytes, largest 147,702; fit rule in ACTIVATION §2 step 3; trial design fixed before any run, with the grading corrected after Codex's R3; expectations for 8 of 12 tasks written by nonauthor writers and hashed | no actor run yet (held pending the owner's decision on iteration 5); fit in an actual actor context unmeasured, so fit is `indeterminate` | `unresolved` |
| 5. Discriminators hold under source-first review; interpretation preserves owned determinations | CONFORMANCE §5 maps the 52 discriminators and J53 to J55 to loci on the successor, three carried into their owners and read back; the pinned checker returns `valid` and all seven controls hold on the regenerated artifacts; 8 fidelity cases at I3 with 3 repairs read back; `consumers.json` binds 1,329 consumer links to the 64 clauses; the family tables of three members read source-first with 14 repairs | required coverage: 64 clauses cover the shared-owner determinations of G1 to G4 only; 15 sections `encoded-in-part`, 181 `not-encoded-i3`, G5 to G13 not encoded; consumer semantics beyond citation unread; no discriminator assessed by a cross-family reviewer; Codex's R1 (SPEC_METHOD's chain software-only) `falsified` criterion 5 for that member at `8a0ea22` and is repaired on the successor pending readback | `unresolved` |
| 6. Reduction within the cone; deciding-path comparisons | REDUCTION §3 (34 clusters) and §4 (46 paths, dimensions, outcome rule, tradeoffs; TO1 realised and disclosed); 7 paths route-traced on three subjects: DP-31 `satisfied` against rc.2, six `indeterminate` with an elimination witness each; all seven `indeterminate` against `2beed8d` | 38 paths untraced; the entry README's growth is an undeclared tradeoff; no frame-entry trace | `unresolved` |
| J53 integrated reduction | as criterion 6 | the integrated assessment | `unresolved` |
| J54 no proposal presented as accepted | every `superseded` row and every relation says proposed and pending; the ledger and handoff claim no acceptance; Codex's review found none | | `unresolved` (no counterexample known) |
| J55 five satisfied and the sixth missing | not reached: no member has five criteria `satisfied` | | `unresolved` |

Eligibility under the ratified comparison rule: a candidate qualifies
only when all six criteria and the integrated obligations are
`satisfied` on the exact candidate. This candidate does not qualify at
this freeze. The one `falsified` result on record, Codex's R1 against
SPEC_METHOD at `8a0ea22`, is repaired on the successor and awaits its
readback; every other obligation is unassessed or depends on the product
owner's decisions.

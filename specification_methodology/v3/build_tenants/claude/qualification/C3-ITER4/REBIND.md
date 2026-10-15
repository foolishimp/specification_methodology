# I4-01 Rebind

Return of I4-01 for the Claude line. Subject: every common decision that
changed between this line's I3 input `355aa86` (C3-I3-R2-01) and the
ratified I4 input `3c4c503` (C3-I4-03). The diff is 71 lines in and 46
out across `INTENT.md`, `PRODUCT.md`, `GOALS.md`,
`REFERENCE_FRAME_BASIS.md`, `requirements/README.md`,
`conformance/README.md`, `AGENTS.md`, `CLAUDE.md` and
`build_tenants/README.md`. `PREDECESSOR_CLAIMS.md` did not change, so the
frontier inventory (707 keyed rows) is unchanged. Checks: the 14 common
members of the C3-I4-03 snapshot match byte for byte at the merged tenant
tree `7c60f32`; the two tickets differ there only by the recording
`a960032` and reproduce from `3c4c503` (25 of 25).

| # | Common decision (locus, range) | Effect on this candidate | Task or no change |
|---|---|---|---|
| 1 | INTENT: each categorical claim requires the declared demonstration (`355aa86..1fce537`) | Any categorical claim in the candidate's FOUNDATIONS or REFERENCE_FRAME needs a bound demonstration | I4-02: list the claims; bind or mark `unresolved` |
| 2 | PRODUCT a_c dependency and requirements: the exact a_c theory is for construction and checking; the released encoding basis follows the identity and packaging decision | `a_c/i3` is the construction interpretation; nothing in the candidate may present it as the released basis | I4-08: check INTERPRETATION §7 and `a_c/i3/README` wording |
| 3 | PRODUCT: the construction and integrated-closure section checks the Executive's acceptance decisions and C3 closure | Framing of the three closure checks J53 to J55 in CONFORMANCE §5 | I4-09: no text change expected; verify |
| 4 | PRODUCT and requirements: a frontier record names proposed dispositions; accepted standing comes only from the ticket | The frontier header says acceptance needs owner decisions and a cross-family review | I4-01: header reworded to the ticket rule (done in this commit) |
| 5 | PRODUCT Limits: fit from recorded complete active inputs or a supported upper bound including host context; fit stays `indeterminate` without a counterexample; a correct result does not satisfy a missing fit judgment | ACTIVATION §6 (owner of limits) and every trial record must carry this rule | I4-06: ACTIVATION §6 text; trial design if D5 funds a run |
| 6 | PRODUCT Independence and RFB Reviewer row: the ported-contribution review is the receiving line's same-family nonauthor assessment; the donor's reading is supplementary | `design/CROSS_SYNTHESIS.md` and CONSTRUCTION_BINDING §1 leave the port review to an owner decision | I4-08: reword; I4-03: schedule the readback of all ports |
| 7 | PRODUCT open owner decisions: actual-use resources (missing resources leave criterion 4 unresolved, waive nothing, qualify no peer); the UX conflict (ambiguity rule governs; a stricter reading is not acceptance of a replacement) | HANDOFF and UX §15 wording | I4-08: UX §15 says the stricter reading is applied, not accepted; HANDOFF carries D5 |
| 8 | GOALS named change: each construction activation names its actor and authority; acceptance-review assignments stay with the owner | Ledger activations already name actor and authority | No change |
| 9 | GOALS named change: criterion 5 covers the member's a_c interpretation and acquired views; fidelity must be assessed where a derived surface supplies determinations | Per-member fidelity evidence is now part of criterion 5, not only an integrated obligation | I4-05: fidelity cases per encoded member; I4-09: result map |
| 10 | requirements reduction: dimensions and tradeoffs declared in the existing activation or qualification record; partial evidence is supporting only, cannot make criterion 6 `satisfied`; `indeterminate` when undecidable, `falsified` on counterexample | DESK-TRACES verdicts ("not established", "simpler on condition") must be restated in those values; the DP-43 condition is now decided by the per-row modal test | I4-07 |
| 11 | requirements packaging: "method-law owners" | Plugins and templates cite owners | No change |
| 12 | conformance: supported inapplicability of a conditional obligation is recorded separately and waives none of the six criteria | CONFORMANCE map and per-member results | I4-09: verify no inapplicability record stands in for a criterion |
| 13 | build_tenants/README: cross-tenant review needs the owner's authorisation; model family is a separate condition; a same-family nonauthor of this candidate gains no access to the peer | The Sonnet reviewers of this line read the peer only at the frozen donor commit for a port | PLAN §3 convention; no candidate text |
| 14 | PRODUCT Cross-Synthesis: three stages; donor named by the admitted contract; coordinates are construction inputs, not product identity | CROSS_SYNTHESIS.md names base and donor at `31f28f9` | I4-08: name the I4 donor; I4-03: C1 to C6 are the port input |
| 15 | PRODUCT: the pen classifies divergences; a revised requirement alone repairs no candidate | Each I4 item carries its class | PLAN §2 |
| 16 | PRODUCT: a peer contribution's record names frozen source, receiving owner, adaptation, affected claims and dependencies, evidence to recheck; the Reviewer compares with the source, the claims and the consumers; a port list is input, not an obligation | `ports.md` at I3 recorded owner and cone only, and no port was compared with its source | I4-03: new record for every port, I3 and I4; readback by the nonauthor reviewer |
| 17 | PRODUCT: a repair produces a successor freeze; the reviewer checks changed material and dependents; changed ports get nonauthor readback; no number of rounds completes unresolved work | The I3-8r repairs (`416bdb5..2beed8d`) and the fidelity repairs were never re-reviewed | I4-09: in the working review's scope with their dependents |
| 18 | PRODUCT Candidate Comparison: own preceding-candidate comparison under the reduction requirement; head-to-head only under the shared protocol | Preceding candidate becomes `2beed8d`; the rc.2 comparison stays | I4-07; no frame built from an expected protocol (PLAN §3) |
| 19 | PRODUCT: returns account for all six criteria and the closure checks as satisfied, falsified or unresolved; missing assessment withholds and does not invent failure; criterion 4 needs actual use with supported fit; curated-frame use and ordinary discovery reported separately | HANDOFF and CONFORMANCE result maps; trial reporting | I4-09; I4-06 under D5 |
| 20 | PRODUCT frames: coverage is by selected task and its material conditions, not by frame-file count; a reusable frame may serve several tasks when its binding and evidence support each | The 12 frames have no task-coverage map; TO1 rows and result maps missing; F5 `kind` label missing | I4-06 |
| 21 | requirements conservation test and modal wording; conformance conserved-heading row | Every `conserved` row whose text rewrote "must" or "shall" needs a recorded meaning judgment; the delta-judged rows need both texts; proposed replacements go to the pen by question | I4-04 |
| 22 | conformance: ported contributions retain authorship; head-to-head follows Candidate Comparison; an unassessed candidate is not evidence its peer qualifies | CONFORMANCE §5 discriminator mapping quotes discriminators by number and intent | I4-09: re-map against the changed rows |
| 23 | RFB: model family, authorship and task-context freshness are separate facts; donor participation disclosed | Activation records | PLAN §3; ledger |
| 24 | GOALS, AGENTS, CLAUDE, build_tenants/README routing for I4 | None on candidate text | No change |

Codex's bounded Stage 1 reading of `2beed8d` (post `20261015T054112Z`)
reported no implementation defect; its finding 5 notes that
`design/REDUCTION.md` keeps pre-repair "state found" counts, which cannot
describe the frozen candidate without source readback. That goes to I4-08
(label the counts as the state at the commit they were read) and I4-02.

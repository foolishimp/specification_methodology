# Desk traces, iteration 4 (I4-07)

Route-entry traces of the declared sample (every sixth path of REDUCTION
§4.4: DP-01, DP-07, DP-13, DP-19, DP-25, DP-31, DP-37, with DP-43 traced at
iteration 3), on S0 the installed `v2.5.1-rc.2`, S1 the preceding candidate
`2beed8d` and S2 the candidate at `23b6556`. Each trace is a same-family
nonauthor Fable activation in a fresh context under
[INSTRUCTIONS-TRACE](INSTRUCTIONS-TRACE.md); its return is `DP-nn.md`.
Verdicts are in the ratified standing of REDUCTION §4.2: `satisfied`
(simpler to determine and apply), `indeterminate` (the measures cannot
decide the required improvement), `falsified` (a counterexample), or
`unresolved` (not traced). The other 38 paths are `unresolved`.

| Path | Against S0 | Against S1 | M2 S0→S2 | M3 S0→S2 | M4a S0→S2 | M5 S0→S2 | Note |
|---|---|---|---|---|---|---|---|
| DP-01 | `indeterminate` | `indeterminate` | 4→0 | 2→0 | 2,330→28,087 | 21→5 | G passes on S2; elimination witness (four rivals and two reconciliations removed); the entry README's size is an increase no declared tradeoff explains, which the pre-declared rule does not let the trace excuse; S1 and S2 byte-identical on the route |
| DP-07 | `indeterminate` | `indeterminate` | 3→0 | 3→0 | 2,330→28,087 | 13→4 | G passes on all three; M2, M3, M4b and M5 fall against S0; the only unexplained increase is the entry README's growth; against S1 nothing is left to remove and the 340-byte M4b rise is a preserved distinction |
| DP-13 | `indeterminate` | `indeterminate` | 0→0 | 2→0 | 2,330→28,087 | 4→6 | G passes; two reconciliations removed; the M5 and M4b rises are explained by TO2, TO3 and a preserved distinction; the entry README's growth is the one unexplained increase; on S0 the deciding loci are reached only by whole-member reads, no section-level route; S1 and S2 byte-identical on the route |
| DP-19 | `indeterminate` | `indeterminate` | 4→1 | 5→2 | 2,330→28,087 | 8→15 | G passes; three rivals and three reconciliations removed (elimination witness); remaining on S2: EXECUTIVE_BASELINE's two field lists (§16 and §19, conserved from rc.2) and the "binding" homonym PROFILES §1 introduces; the README growth, the PROFILES index hops and two member leads are increases no declared tradeoff explains; S1 and S2 byte-identical on the route |
| DP-25 | `indeterminate` | `indeterminate` | 2→0 | 1→0 | 2,330→28,087 | 8→1 | G passes; two rivals and one reconciliation removed, hops 8 to 1; the entry README's growth and the acquired bytes of the one owning section (ACTIVATION §1, 63 KB cumulative) are increases no declared tradeoff explains; S1 and S2 differ on the route only by the I4 applicability sentence (275 bytes) |
| DP-31 | `satisfied` | `indeterminate` | 1→0 | 1→0 | 3,712→4,031 (skill) | 6→7 | G passes on all three; one rival and one reconciliation removed; the hop and acquisition rise is TO2 (generic resumption law in tier-1 ACTIVATION §5, reached by the skill's named-section route); adverse on S0: the owner of the uncertain-effect reconciliation rule is unreachable by route; against S1 the loci are byte-identical |
| DP-37 | `indeterminate` | `indeterminate` | 1→0 | 3→1 | 2,330→28,087 | 8→10 | G passes on S2 (G1 fails on S0: ambiguity exits unmapped there); one rival and two reconciliations removed; the README growth and three route-forced non-deciding UX hops (§4, §8, §12) are increases no declared tradeoff covers; TO2 and TO3 explain the rest; S1 and S2 differ only by ACTIVATION §2's I4 sentence |
| DP-43 (I3) | `indeterminate` | `indeterminate` | | | | | see `../../C3-ITER3/paths/DESK-TRACES.md` §0 |

## Reading of the sample

Seven of the eight sample paths are traced at iteration 4, all on the
same three subjects. Against the predecessor every traced path removes
rival deciders or reconciliations with the guard passing (an elimination
witness on all seven), and one, DP-31, is `satisfied` under the
pre-declared rule because its extra hops are the declared tradeoff TO2.
The other six are `indeterminate` for one recurring reason: the entry
README grew from 2,330 to 28,087 bytes to carry task routes, and that
increase in M4a was not declared as a tradeoff before measurement, so the
rule cannot excuse it. The increase is an adverse change reported against
both baselines, and a candidate tradeoff (an entry that routes by task,
in exchange for fewer hops and rivals) for a later iteration to declare
before it measures. Against the preceding candidate `2beed8d` every path
is `indeterminate`, because the iteration 4 edits did not touch the
traced routes: this iteration added evidence, not reduction, on these
paths. Two residual rivals were named by DP-19 (EXECUTIVE_BASELINE §16
and §19 field lists; the "binding" homonym of PROFILES §1) and one
unreachable owner by DP-31 on the predecessor. No frame-entry trace was
made, so TO1's acceptance condition stays `unresolved`. The remaining 38
paths are `unresolved`.

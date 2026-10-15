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
| DP-43 (I3) | `indeterminate` | `indeterminate` | | | | | see `../../C3-ITER3/paths/DESK-TRACES.md` §0 |

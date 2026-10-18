# Inputs for older/newer performance tests

Eight complete representations are indexed in [`comparison.json`](comparison.json). The planned comparison tests have not been run.

| Period | Source | Path | Model | Calls | Reported input tokens | Reported output tokens | Actor seconds |
|---|---|---|---|---:|---:|---:|---:|
| older | codex 3.0.0-rc.5 | graphify-ac | [model](../stdo-v3-generation/runs-v2/codex/graphify-ac/repaired-proposal/model.json) | 12 | 955,101 | 585,828 | 10,095.1 |
| older | codex 3.0.0-rc.5 | direct | [model](../stdo-v3-generation/runs-v2/codex/direct/repaired-proposal/model.json) | 13 | 894,586* | 555,175* | 10,591.5 |
| older | claude 3.0.0-rc.8 | graphify-ac | [model](../stdo-v3-generation/runs-v2/claude/graphify-ac/repaired-proposal/model.json) | 30 | 2,531,742 | 777,599 | 13,379.6 |
| older | claude 3.0.0-rc.8 | direct | [model](../stdo-v3-generation/runs-v2/claude/direct/repaired-proposal/model.json) | 30 | 2,129,152 | 850,259 | 15,059.4 |
| newer | codex 3.0.0-rc.9 | graphify-ac | [model](runs-v2/codex/graphify-ac/repaired-proposal/model.json) | 14 | 1,203,589 | 590,113 | 9,896.9 |
| newer | codex 3.0.0-rc.9 | direct | [model](runs-v2/codex/direct/repaired-proposal/model.json) | 11 | 786,238 | 544,286 | 9,629.8 |
| newer | claude 3.0.0-rc.9 | graphify-ac | [model](runs-v2/claude/graphify-ac/repaired-proposal/model.json) | 20 | 1,435,637 | 764,514 | 13,590.7 |
| newer | claude 3.0.0-rc.9 | direct | [model](runs-v2/claude/direct/repaired-proposal/model.json) | 21 | 1,389,559 | 746,907 | 13,654.5 |

*Unknown backend usage: older-codex-direct (1 calls). Recorded elapsed time is included. Tokens shown are reported totals only.

Codex RC9 has the same selected source bytes as older RC5. Claude RC9 changes `ASSURANCE.md` and `FOUNDATIONS.md` (+761 bytes); its source partition also changes. The [source delta](evidence/source-delta.json) retains every selected member's identity.

Use each cell's exact model and matching frozen source for tests. The index distinguishes the file digest from the model's canonical digest and retains the Graphify carrier/graph, source cut, build evidence and resource counters. The implementation and model settings are held constant across old/new builds.

Old fidelity grades apply to old models only. New models have passed the build's mechanical checks and require their own semantic evaluation. The descriptive profile does not author traversals, transformations or judgments.

These are build observations. Summed actor time, unknown usage, cache differences and one generation per cell prevent a general cost or quality conclusion. Later tests should use common tasks, version-appropriate source truth, identical execution limits and separately recorded correctness and resource results.

Recheck all indexed artifact identities without model calls:

```sh
a_c/.venv/bin/python a_c/dogfood/stdo-v3-generation-rc9/build_comparison.py --check
```

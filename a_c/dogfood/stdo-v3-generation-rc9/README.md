# RC9 representations for older/newer comparison

Status: build complete; eight older/newer representations are available for
the planned comparison tests. Those tests and semantic assessment of the new
models have not been performed. The older complete study remains unchanged at
[`../stdo-v3-generation/`](../stdo-v3-generation/README.md), checkpoint commit
`efae9c749275838029a871863f0b3ce7d7aba8b6`.

The [comparison index](COMPARISON.md) links all eight models and their measured
build resources. [`comparison.json`](comparison.json) provides exact model,
carrier, graph, source, plan and result identities for a test harness.

## Frozen subjects

Both RC9 cuts were the latest clean candidates resolved at **2026-10-18
07:30:30 UTC**. Later branch movement does not change these inputs.

| Candidate | Source/package revision | Custody checkpoint | Selected source |
|---|---|---|---|
| Codex RC9 | `5592168e26759f37e730aed12c030a6061709ec4` | `c46e9f96381097245a6714164f03b72ad32116c0` | 44 files, 1,269,082 bytes |
| Claude RC9 | `c2cfa9b908d1722ae3f26c32fa4ece691083bdc3` | `3a2097137c3588ba44b98e3ea801ac7f2be1daf0` | 49 files, 2,147,989 bytes |

The [custody record](evidence/source-custody.json) verifies the candidate member
hashes and immutable source blobs. The [source delta](evidence/source-delta.json)
covers every selected old/new member. Codex's selected owner source is identical
to old RC5; this is a fresh repeat with changed subject coordinates. Claude
changes `ASSURANCE.md` and `FOUNDATIONS.md` (+761 bytes), affecting three source
partitions. The input selection rule and chunk algorithm are unchanged.

## New representations

| Source | Graphify-assisted | Direct-source control |
|---|---|---|
| Codex RC9 | [model](runs-v2/codex/graphify-ac/repaired-proposal/model.json) | [model](runs-v2/codex/direct/repaired-proposal/model.json) |
| Claude RC9 | [model](runs-v2/claude/graphify-ac/repaired-proposal/model.json) | [model](runs-v2/claude/direct/repaired-proposal/model.json) |

Each model directory retains its carrier, coverage ledger and checked result;
assisted directories also contain the actual Graphify semantic graph. Inputs
are owner source, with existing native interpretations and reviews excluded.
F_P authoring is inside the tenant workflow. `direct` is a fresh source-only
control under the same authoring contract, not a V3 native compiler output.

[`PROTOCOL.md`](PROTOCOL.md) binds the unchanged implementation, model/settings,
budgets, recovery rules and evidence limits. The operating basis remains
installed STDO v2.5.1-rc.2; V3 documents are subjects. The [generation
freeze](freeze-v2.json), [repair freeze](repair-freeze.json) and [launch
review](evidence/launch-review.json) retain exact identities and preflight.

## Build verification

- All 60 input chunks were processed: 37 strict originals, 18 mechanically
  recovered drafts and five F_P grounding repairs. One additional fresh
  Codex/Graphify authoring attempt replaced an invalid disposition ledger;
  its remaining grounding failure and the original failure remain retained.
- All **66 calls** are closed and report backend usage. The maximum was four
  concurrent calls and three combined author/repair calls per chunk. No
  fresh source authoring occurred after repair reservations began.
- All four models passed native structural validation and carrier recovery.
  Both assisted models also recovered unchanged through actual pinned
  Graphify `fe085cedddde3a18554f8749b230bfe47f3dcce7`.
- The shared implementation, schemas, prompts and helpers match the tested
  checkpoint. Its previously passed 107-test actual-upstream suite was not
  redundantly rerun; this rebuild verifies the new subject artifacts.

[`results.json`](results.json) retains every call, failure, repair and reported
counter, plus separate discovery, normalization and assembly timing evidence.
The [assembly record](evidence/assembly-execution.json) retains all four fresh
subprocess invocations and results. The independent
[resource/custody/index audit](evidence/resource-audit.json) found no actionable
defect, and the [final integrity check](evidence/final-integrity-check.json)
verifies all frozen pins, closed calls and unchanged source worktree heads.
Timings are observations; summed actor
intervals are not concurrent wall time, and cache counters do not establish
billing or accepted-result cost.

Recheck all eight indexed artifact/source identities without model calls, from
the repository root:

```sh
a_c/.venv/bin/python a_c/dogfood/stdo-v3-generation-rc9/build_comparison.py --check
```

The new models have no inherited old fidelity grades. Structural validity,
exact quotations and graph recovery do not establish semantic fidelity or
acceptance. This descriptive profile leaves traversals, transformations and
judgments empty. Full calculus conformance, operational qualification and
owner acceptance remain outside this rebuild.

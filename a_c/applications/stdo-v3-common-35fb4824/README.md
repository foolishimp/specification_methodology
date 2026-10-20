# Common V3 representation

The reviewed **packaging-r1** representation is **PUBLISHED** with the
[standalone STDO v3.0.0 RC1 prerelease](https://github.com/foolishimp/specification_methodology/releases/tag/specification_methodology/v3.0.0-rc.1).
All six asset downloads and a fresh public native installation were verified.
See [PUBLICATION](PUBLICATION.md) for downloads, exact native installation and
public rebuild routes, and the [publication receipt](../../.ai-workspace/qualification/t010/publication-rc1/PUBLISHED.json).
The represented source remains common checkpoint
`35fb4824a064a84df5af214a0d0e2da597c18ac6`, package tree
`7f2070b61c848b42b4dfb3af1e0ce53869de1aa1`. This supplemental proposal has no
a_c Product version, independent artifact tag, semantic acceptance or adoption.

Start with the [bundle index](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/index.html),
[Graphify map](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/graph.html),
[record browser](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/records.html) or
[portable guide and rebuild recipe](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/README.md).
The representation retains all 81 source files, 58 semantic inputs, 845 sections,
1,987 records and 2,491 physical grounding occurrences. Five record families
are populated; traversals, transformations and judgments are explicitly empty.

All 1,987 records are displayed, with zero omitted or aggregated records.
[Display scope](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/view-scope.json)
accounts for 2,218 reference pairs, 2,225 local reference occurrences and 14,273
external coordinate occurrences omitted from display plumbing. Family colours
and connectivity establish no semantic communities or governing closure. Full
content remains in the reversible carriers and
[processing coverage](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/coverage.json).

## Portable use

Download the [current archive](https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology/v3.0.0-rc.1/a_c-stdo-v3-common-35fb4824-packaging-r1.tar.gz)
and [external checksum](https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology/v3.0.0-rc.1/a_c-stdo-v3-common-35fb4824-packaging-r1.tar.gz.sha256).
It contains 213 files, 110,473,751 bytes unpacked and 10,089,542 bytes compressed.
Archive SHA256:

`989c0efbbba90c1d444c6a1c24def4174ef8519bec5f63d9bef021f27dd75e2b`

Python 3 standard library is sufficient for checking and inspection:

```sh
tar -xzf a_c-stdo-v3-common-35fb4824-packaging-r1.tar.gz
cd a_c-stdo-v3-common-35fb4824-packaging-r1
python3 -B -S release_tools/bundle_check.py .
python3 -B -S codec/ac_graph.py find carrier.json admission
AC_RECORD='urn:a-c:generation:0657852b6fd1fa48457c3f7d:record:5fec0f21265016ca449d4389511dce49'
python3 -B -S codec/ac_graph.py inspect carrier.json "$AC_RECORD"
python3 -B -S codec/ac_graph.py project carrier.json --seed "$AC_RECORD" --out /tmp/common-selected-projection.json
python3 -B -S release_tools/source_reentry.py standards/ACTIVATION.md --start 1 --end 30
```

Use fresh output filenames outside the bundle. For an ordinary local visual
preview, run `python3 -B -S release_tools/serve_preview.py .` and open the printed
loopback URL; Ctrl-C stops it. No CDN or model service is needed. Interactive
browser behavior remains **unverified**; this delivery used static checks and
CLI replay. The guide's rebuild recipe additionally requires the explicit pinned
Graphify checkout and existing Python/networkx environment.

## Evidence and standing

Three supported packaging defects are fixed: overlapping archive output,
rebuilding from authenticated portable source readiness, and duplicate release
source identities. All 19 focused author checks and
[48 focused nonauthor checks](../../.ai-workspace/qualification/t010/package-review/packaging-r1-001/assessment-001/REVIEW.md)
passed. The documented extracted-input rebuild produced byte-identical bundles
and archives. [Repair/promotion record](../../.ai-workspace/qualification/t010/packaging/repair-002/README.md)
and [handoff](../../.ai-workspace/qualification/t010/handoff/packaging-r1-001/)
retain exact subjects and preimages.

The correct [original representation archive](https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology/v3.0.0-rc.1/a_c-stdo-v3-common-35fb4824.tar.gz)
and [bundle](bundle/a_c-stdo-v3-common-35fb4824/README.md) are preserved. Its
[72-control review](../../.ai-workspace/qualification/t010/package-review/final-003/REVIEW.md)
applies to that original bounded baseline; it does not qualify the new code.
The unchanged [source-first nonauthor semantic review](bundle/a_c-stdo-v3-common-35fb4824-packaging-r1/evidence/reviews/review-001/REVIEW.md)
found no actionable defect in 44 fixed cases, four logical acquisition tasks
and 11 interventions. A3 concrete invariant reconstruction was not performed.

See [BUILD](BUILD.md), [frozen source readiness](SOURCE-READINESS.md) and
[release preparation](RELEASE-PREPARATION.md). Frozen common remains `not_ready`,
owner acceptance is absent and covering source review unassigned. This model
review replaces none of those gates. Semantic acceptance, fresh actor use,
required provider-family independence, global governing acquisition,
whole-calculus conformance, efficiency/benefit and Product/RC/installed
qualification remain unqualified. The a_c builder remains STDO 2.5.1-rc.2.

The [published standalone STDO 3.0.0 RC1 prerelease](https://github.com/foolishimp/specification_methodology/releases/tag/specification_methodology/v3.0.0-rc.1)
uses the separately checked native cut, with three nonsemantic packaging deltas.
Its RC1 identity is separate from this packaging-r1 identifier; it neither rebases
the a_c model/source custody nor adds a dependency. [PUBLICATION](PUBLICATION.md)
labels captured workspace/private/absolute proof routes as historical and gives
the complete portable public-input build. They are not public build prerequisites.

Public receipts exclude raw private invocations, events, configuration and
hidden reasoning and do not supply complete private actor replay. Existing
licenses retain their scope; distribution terms for a_c-owned/new material
remain an owner choice, without a new license or automatic publication gate.

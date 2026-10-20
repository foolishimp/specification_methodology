# Common V3 representation

The a_c/Graphify representation is built from common checkpoint
`35fb4824a064a84df5af214a0d0e2da597c18ac6`, package tree
`7f2070b61c848b42b4dfb3af1e0ce53869de1aa1`. Selected local construction and
release preparation are complete. The artifact is an uncommitted, unpublished
proposal; no Product version, RC, tag or adoption is selected.

Start with the [bundle index](bundle/a_c-stdo-v3-common-35fb4824/index.html),
[Graphify map](bundle/a_c-stdo-v3-common-35fb4824/graph.html),
[record browser](bundle/a_c-stdo-v3-common-35fb4824/records.html) or
[portable guide](bundle/a_c-stdo-v3-common-35fb4824/README.md).
The bundle retains all 81 source files, 58 semantic inputs, 845 sections,
1,987 records and 2,491 physical grounding occurrences. Five record families
are populated; traversals, transformations and judgments are explicitly empty.

All 1,987 records are displayed, with zero omitted or aggregated records.
[Display scope](bundle/a_c-stdo-v3-common-35fb4824/view-scope.json) accounts for
2,218 reference pairs, 2,225 local reference occurrences and 14,273 external
coordinate occurrences omitted from display plumbing. Family colours and graph
connectivity establish no semantic communities or governing closure. Full
content remains in the reversible carriers and
[processing coverage](bundle/a_c-stdo-v3-common-35fb4824/coverage.json).

## Portable use

Download the [archive](dist/a_c-stdo-v3-common-35fb4824.tar.gz) and its
[external checksum](dist/a_c-stdo-v3-common-35fb4824.tar.gz.sha256).
It contains 213 files, 110,470,239 bytes unpacked and 10,087,425 bytes compressed.
Archive SHA256:

`2b33530c20a17dd27033e8b34b1af497de7a4e0f3b8165a22d0821298516e386`

Python 3 standard library is sufficient after extraction:

```sh
tar -xzf a_c-stdo-v3-common-35fb4824.tar.gz
cd a_c-stdo-v3-common-35fb4824
python3 -B -S release_tools/bundle_check.py .
python3 -B -S codec/ac_graph.py find carrier.json admission
AC_RECORD='urn:a-c:generation:0657852b6fd1fa48457c3f7d:record:5fec0f21265016ca449d4389511dce49'
python3 -B -S codec/ac_graph.py inspect carrier.json "$AC_RECORD"
python3 -B -S codec/ac_graph.py project carrier.json --seed "$AC_RECORD" --out /tmp/common-selected-projection.json
python3 -B -S release_tools/source_reentry.py standards/ACTIVATION.md --start 1 --end 30
```

Use a fresh output filename outside the bundle for each projection. For an
ordinary local visual preview, run `python3 -B -S release_tools/serve_preview.py .`
from the extracted directory and open the printed loopback URL; Ctrl-C stops it.
The views need no CDN or model service. Interactive browser behavior remains
**unverified**; this delivery used static display checks and CLI replay only.

## Evidence and remaining decisions

The [bounded semantic review](bundle/a_c-stdo-v3-common-35fb4824/evidence/reviews/review-001/REVIEW.md)
found no actionable defect in 44 fixed preservation cases, four logical
acquisition tasks and 11 grounding interventions. A3 concrete invariant
reconstruction was not performed. The
[independent actual archive review](../../.ai-workspace/qualification/t010/package-review/final-003/REVIEW.md)
passed all 72 bounded controls, including exact carrier recovery, portable CLI
replay, tamper refusal and deterministic repacking. Its
[closure](../../.ai-workspace/qualification/t010/package-review/final-003/CLOSED.json)
and the [packaging self-control closure](../../.ai-workspace/qualification/t010/packaging/final-001/CLOSED.json)
retain the exact subjects and limits.

See [BUILD](BUILD.md), [frozen source readiness](SOURCE-READINESS.md) and
[release preparation](RELEASE-PREPARATION.md) for provenance and disposition.
The frozen common record remains `not_ready`, with owner acceptance absent and
covering source review unassigned. This model review does not replace those
gates. Semantic acceptance, fresh actor use, required provider-family
independence, global governing acquisition, whole-calculus conformance,
efficiency/benefit and Product/RC/installed qualification remain unqualified.
The builder remains STDO 2.5.1-rc.2; common is the represented subject.

The archive contains bound public receipts, not raw private invocations,
events, configuration or hidden reasoning; it does not supply complete private
actor replay. Existing licenses retain their scope. Distribution terms for
a_c-owned/new material remain an owner choice; no new license or automatic
publication gate is asserted.

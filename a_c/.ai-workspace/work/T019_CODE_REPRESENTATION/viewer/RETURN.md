# T-019 reader Worker return

Status: bounded reader implementation and actual-artifact DOM checks complete.
No actionable reader failure remains from these checks. Independent assessment,
semantic adequacy and browser/WebGL qualification retain their separate owners.
No Git, native model/carrier, frozen application or release changes were made.

## Delivered behavior

Optional code/test/unresolved-code families and structure/trace layers use the
same Files, search, source reader and reading trail in 3D, 2D and Layered modes.
Native identity, counts and proof scope stay separate from overlay identity,
coverage, diagnostics, attribution and proposed mappings. Connection evidence
includes exact raw links, raw extraction strings, conditions, limitations and
source quotations. Native-only pages keep the overlay controls hidden.

The only `layered.js` changes add explicit colors/arrow markers/descriptions for
the two new layers; layout algorithms are unchanged. The three modes retain the
same displayed node/link identities, selected record, navigation origin and trail.

## Exact source cut

| Source | SHA-256 |
|---|---|
| `a_c/build_tenants/graphify/code/viewer/explorer.html` | `f6098541425badfb456982274107ce98bcf068b66b27db757b7bd20fe4e8beef` |
| `a_c/build_tenants/graphify/code/viewer/explorer.js` | `4e0b821ba33e0c57a05ee44a200c839b47c1d14f777646ec1836aa7c915daf56` |
| `a_c/build_tenants/graphify/code/viewer/explorer.css` | `8508f8d81b570d5d5d5eb81adc3895ae1073fcf640694ec229ec54aef61ea16a` |
| `a_c/build_tenants/graphify/code/viewer/layered.js` | `134b082f87f15eca059432e07453ce27e5a963bd94c798ef32b1eafb9cdc8b80` |
| `a_c/build_tenants/graphify/test_env/test_explorer_code.cjs` | `524d03cfc951265eab27856c2f47c4d66bb7c92d96aa8a176be65afeb9f2250e` |
| `a_c/build_tenants/graphify/test_env/test_explorer_labels.cjs` | `dd2d5e1f2d13758d4f7946d5fbbad0ebc9d56829bd13b96515d58504992e5d3d` |
| `a_c/build_tenants/graphify/code/ac_code.py` | `60b11511158ac780566d7fb7f178a22b9a3e276269b0a65e04286455275abcbd` |

The actual artifact embeds the exact `explorer.js` and `layered.js` bytes above.
The backend produced it with the actual pinned extractor; this Worker did not
rerun source extraction or assess the truth of its observations.

| Temporary supplied artifact | SHA-256 |
|---|---|
| `/private/tmp/ac-code-reader-t019-fixture.html` | `aba9ee65b67009e61baa80267b30a72fc9c9260e970e140f119816033c082419` |
| `/private/tmp/ac-code-reader-t019-fixture.json` | `061c914be4c76bad2dcf4d6225f68c2508cd6a3a42e62352c8f9f5b03c5a5033` |

The artifact has 6 native records, 13 native external references and 6 overlay
nodes, with 25 combined nodes and 63 combined links. The overlay adds 6
structural links and 2 proposed traces. Its one unresolved mapping remains
visible with its reason. These fixtures are temporary; their hashes identify the
checked cut, not a durable distribution path.

## Commands and observed results

From the repository root, with the already available jsdom (no installation):

```sh
export NODE_PATH=/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-navigation-dom-hf_s3qyf/node_modules
node a_c/build_tenants/graphify/test_env/test_explorer_code.cjs /private/tmp/ac-code-reader-t019-fixture.html
node a_c/build_tenants/graphify/test_env/test_explorer_labels.cjs /private/tmp/ac-code-reader-t019-fixture.html
node --check a_c/build_tenants/graphify/code/viewer/explorer.js
node --check a_c/build_tenants/graphify/code/viewer/layered.js
node --check a_c/build_tenants/graphify/test_env/test_explorer_code.cjs
```

- Code suite: 7 checks passed (6 focused fixture checks plus the generated actual
  requirement→code→test→source→Back path, preserving all three modes).
- Label suite: 2 checks passed, including the generated artifact and the pinned
  renderer's actual dimension-change callback. Missing/invalid coordinates and
  repeated 3D/2D switches retain the established behavior.
- The overlay harness rejects external script/stylesheet/frame resources and
  makes network/service primitives throw. All interaction completed offline.
- A supplementary in-memory DOM probe selected each of the 6 actual structural
  links whose raw extraction contains a floating value (`weight: 1.0`). Every
  expanded evidence body contained the entire original raw JSON string exactly.
  The artifact contains 12 raw extraction strings overall. No numeric coercion
  was used to render them.
- Earlier current-source regression commands `test_explorer_labels.cjs`,
  `test_explorer_modes.cjs`, `test_explorer_navigation.cjs` and `test_layered.cjs`
  passed all 14 checks. JavaScript syntax and scoped whitespace checks passed.

The first actual-artifact code-suite run failed its final overview assertion:
the test demanded every external reference while leaving Other references off.
The requirement→code→test journey had already passed. The test now explicitly
enables that existing filter before asserting every available node/link. The
rerun passed. Only the test changed; the four frozen viewer assets and supplied
HTML remained byte-identical.

## Limits

The shared reader and layered adapter ran in jsdom. Force rendering and
projection were stubbed; the label check reused the pinned dimension mutation.
This establishes neither actual browser/WebGL/camera behavior nor source-code
correctness, executed test results, semantic fidelity, whole-project coverage,
Lean verification of the overlay, acceptance or release readiness. Synthetic
unresolved/ambiguous and parallel/self cases complement the actual pinned
extractor fixture; they are not evidence that every language construct is covered.


## Actual ABIogenesis artifact follow-up

The independent review found a test-only assumption on the real ABIogenesis
artifact: a complete long requirement label was compared with the intentionally
clipped reader heading after Back. The selected record was correct and its full
content remained readable. The original results above are retained for their
original test/source cut.

The corrected journey now asserts the exact selected identity and deep equality
of the complete inspectable record at requirement, code, test and Back steps.
Its heading assertion accepts the full label or an ellipsis-marked prefix;
it copies no truncation threshold. A long requirement label is now included in
the synthetic fixture. All existing mode, source, trail and full-graph checks
remain in place. The viewer and backend were not edited by this activation.

```sh
export NODE_PATH=/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-navigation-dom-hf_s3qyf/node_modules
node a_c/build_tenants/graphify/test_env/test_explorer_code.cjs a_c/applications/abiogenesis-code-explorer/index.html
node a_c/build_tenants/graphify/test_env/test_explorer_code.cjs /private/tmp/ac-code-reader-t019-fixture.html
node --check a_c/build_tenants/graphify/test_env/test_explorer_code.cjs
```

Both runs passed all 7 checks. The real ABIogenesis path includes Files →
requirement → code → test source → source quotation → Back, with exact record
identity/content and reading state retained through 3D, 2D and Layered modes.
With all layers enabled, the actual overview conserves all 1,927 node identities
and 13,388 link identities in every renderer. Native counts remain 1,373 records
and 495 external references; the separate overlay contributes 59 nodes, 127
structural links and 5 proposed traces, including 11 unresolved code endpoints.
No test-execution or formal-proof result follows from those mappings.

| Follow-up subject | SHA-256 |
|---|---|
| `a_c/build_tenants/graphify/test_env/test_explorer_code.cjs` | `5e07032921baa61d78d98908be96fc6c9515f3f7a0c48e9a3d759f4693346020` |
| `a_c/applications/abiogenesis-code-explorer/index.html` | `26e8e1e93221781b7a25fc48ad457c7ea97275cd08dcadba91075cbf8b1be8c9` |

The four viewer assets still exactly match their hashes in the first table.
Syntax and scoped whitespace checks pass. Offline DOM checks retain the same
no-network controls and force-rendering stubs; actual browser/WebGL, camera and
semantic qualification remain open.

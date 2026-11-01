# T-018 static layered renderer — independent review

Date: 2026-11-01. Evaluator: `/root/layered_renderer_review`, activated by
Executive `/root` as a nonauthor Reviewer. This is commentary and bounded
assessment, not Product acceptance or release.

Verdict: **falsified for two selected interaction obligations**, detailed below.
The performed preservation, offline DOM, generator and artifact-currentness
checks otherwise passed. Actual browser visual/layout qualification remains
unperformed.

## Subject, basis and expectations

Selected Product: `a_c/stdo_a_c.json`. Independently ran
`stdo status --definition a_c/stdo_a_c.json --verify`: valid, no failures,
installed STDO `v2.5.1-rc.2`, manifest
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
Read the declared installed bootstrap, applicable AGENTS.md files, common
Goals/Intent/Product/reference-frame basis, PU-03, AC-R-003–010 and the tenant
constraint-explorer design before inspecting the candidate implementation.

Source-derived expectations were: retain exact records and external resolutions;
retain distinct directed relation/reference occurrences, including qualifications,
cycles, parallel and self-links; use one validated representation projection;
keep display topology distinct from governing dependency/proof; preserve shared
source/record/trail navigation; render untrusted content as text; and provide the
selected keyboard, zoom and fit behavior without network/service dependencies.

The reviewed candidate is the 14-file source freeze, preserved by the Executive
as `pre-repair-source-freeze.json`, SHA-256
`c90b16c7e20f4fab736f1e63ea0bda597a81ffd1fdd0659cb728f6294c3640db`.
All 14 listed byte counts and digests were independently verified unchanged
during this review. The principal affected file, `viewer/layered.js`, has SHA-256
`b101fe83397c48d57d7b498573fc0e61aa679d9ce22ad2fa0020615f390403e7`.
Code paths below are relative to `a_c/build_tenants/graphify/code/`.
The Executive reports preserving that cut in `reviewed-predecessor.tar.gz` and
the application identities in `pre-repair-shared-representation.json`; this
assessment binds the directly verified byte identities above, not any successor
repair. The archive itself was not independently rechecked in this review.

## Findings

### R1 — Keyboard activation discards graph focus

Location: `viewer/layered.js:145–146`; activation sites at `169–173` and `187`.

`draw()` replaces all canvas descendants. Activating a focused card or connection
calls the shared selection path, which redraws immediately, removes the focused
element, and leaves `document.activeElement` on `BODY`. Arrow-key handling belongs
to the removed card; the user cannot continue the advertised card navigation
after opening an item without navigating back through the page controls.

Reproduced against the actual `applications/abiogenesis-constraint-explorer/layered.html`
in offline jsdom 26.1.0 with network/service/WebGL entry points forbidden:

1. Focus the initial actionable connection `required:6`.
2. Dispatch `KeyboardEvent('keydown', {key: 'Enter', bubbles: true})`.
3. The reading trail advances to two steps, the original group has
   `isConnected === false`, and `document.activeElement.tagName === 'BODY'`.
4. Focusing and activating a card likewise removes the active card and returns
   focus to `BODY`.

Preserve appropriate graph focus across a selection redraw, using the surviving
link/card identity or the newly selected card as appropriate. Restoration should
be conditional on prior graph focus so that searches and reader actions do not
unexpectedly move focus. Add a regression for continued arrow navigation after
keyboard activation. The existing test checks arrow movement and Enter opening
separately, so it does not expose this failure.

### R2 — Fit cannot fit the actual overview because scale is clamped to 10%

Location: `viewer/layered.js:133`, called by `viewer/layered.js:205–208`.

`fit()` calculates the scale needed to fit both dimensions, but `scale()` replaces
any value below `0.1` with `0.1`. The demonstrated ABIogenesis overview is much
taller than ten viewports. Therefore Fit neither fits the displayed graph nor
allows the zoom controls to reach the computed scale.

Reproduced using the actual exported page, setting only the jsdom viewport's
layout measurements to a declared 640 × 600 pixels, then clicking Overview and Fit:

| Observation | Result |
| --- | --- |
| Visible graph | 1,373 nodes; 2,264 links |
| Unscaled canvas | 8,904 × 88,736 pixels |
| Applied transform | `scale(0.1)` |
| Scaled extent | 890.4 × 8,873.6 pixels |
| Zoom label | `10%` |

The requested fit scale is approximately `0.00676`; the applied extent remains
over fourteen viewport heights. This contradicts the documented Fit action's
purpose of seeing the displayed graph. Permit the computed fit scale below the
manual zoom floor, or otherwise use bounds compatible with the actual graph.
Add a size-aware Fit assertion; existing jsdom tests never provide nonzero
viewport dimensions to exercise this branch.

## Performed checks and supported results

- Python: `python3 -B -m unittest test_ac_explore test_ac_project -v` from the
  tenant test directory: **22 passed, 1 skipped**. The skip was the explicitly
  optional pinned-upstream Graphify trial. Disposable controlled fixture tests
  exercised the public generator, one-data/two-page project build, reuse,
  altered layered artifact refusal and missing-inventory-member refusal.
- Node, with the supplied `NODE_PATH`: `test_layered.cjs` against the actual
  layered page: **6 checks passed**; `test_explorer_navigation.cjs` against that
  page: **7 checks passed**; `test_explorer_labels.cjs` against the unchanged
  index page: **2 checks passed**. These are DOM/geometry/adapter observations,
  not browser rendering qualification.
- Independent deterministic graph probe: **500 randomized graph cases** checked
  SCC cycle badges against a separate transitive-reachability computation,
  increasing rank between distinct components, finite coordinates, unique paths
  for all distinct edge occurrences, exact original edge identity/reference,
  and immutable input acceptance. Parallel, reciprocal, self and disconnected
  shapes were included. All passed.
- Independently parsed both actual pages. Their embedded representation bytes
  are identical: SHA-256
  `4dbe6f1ee8c356e6984791fbcbd66bbdc0572e2d7b4e6446d331f17c42806972`.
  They contain 1,373 local records, 495 external resolutions, 2,142 required
  links, 122 authored relations, 10,992 typed references and 86 source files.
  Every embedded source text matches its declared SHA-256. The layered page's
  script and CSS bytes exactly match the reviewed current assets.
- Independently validated the existing frozen ABIogenesis model, decoded its
  existing carrier back to the exact model document, and computed `view_data`
  **in memory** from that existing model and frozen corpus. Its object and
  serialized bytes equal the embedded payload exactly. No new ABIogenesis model
  or subject build was created. Model and carrier bytes remained unchanged.
- Canonical model digest:
  `6ad4fa0ef54a8fc705562acf695fce0a0855b0a0d68d6fc99dcf026e98a8b38a`.
  Actual index SHA-256:
  `ef302f3a2eba432b08f4e45cb817d01675a122916931eaf4cf394da726ab190a`.
  Actual layered SHA-256:
  `c947cc41ae4730c8ace0da8a6c8bad47b3487a8d1b1c518f80ef9792149db8d4`.
- Source inspection traces the public path through `ac_explore.view_data()`
  validation/codec dependency projection, `render()`'s single-pass escaped data
  embedding, and `ac_project.build():331–344`'s one data object feeding both
  pages and the artifact inventory. `result_readback():264–292` checks retained
  inventory, bytes and required artifact locations; `open_run():145–163` rejects
  changed machinery/source/definition. No receipt or older run was repinned.
- Independently exercised the changed force-renderer callbacks with hydrated
  object endpoints, using a stubbed renderer. Required-link traversal and exact
  authored-relation/qualification inspection passed, and the embedded payload
  stayed unchanged. The shared reader changes introduce no observed regression
  in that bounded adapter path.
- Source/card/edge text remained DOM text, including hostile HTML strings.
  The actual layered artifact has no remote scripts, stylesheets or frames and
  executed with network/service/WebGL entry points forbidden. No browser was
  opened and no URL-policy bypass or temporary server was attempted.

## Residuals and invalidators

No actual browser font metrics, hit testing, scroll geometry, responsive visual
layout, WebGL behavior or user visual inspection was qualified. jsdom viewport
measurements used in R2 are explicit controlled inputs, not observed browser
dimensions. These limits do not invalidate the reproduced focus and arithmetic
defects, but passing DOM checks does not close visual qualification.

This review does not establish semantic fidelity/completeness of the represented
ABIogenesis source, governing-dependency adequacy, full-calculus conformance,
accepted-result benefit, Product acceptance or release. A changed candidate,
embedded artifact or data/reader contract invalidates the affected findings and
checks. Repairs require an exact successor cut and affected rechecks.

Only this report was written by the Reviewer. No candidate edits, Git effects,
subject implementation/builds, model-authoring calls, network installations or
browser attempts were performed.

## Successor assessment — R1 and R2 repairs

Date: 2026-11-01. Executive `/root` separately activated a narrow successor
assessment of the two repairs, the regenerated actual layered page, and the
absence of focus theft from controls. The preceding findings remain an exact
record of the preserved predecessor; this section assesses the successor only.

**Disposition: R1 and R2 are satisfied on this exact successor within the
performed offline DOM/geometry scope.** No additional actionable defect was
observed in these narrow probes. Browser visual qualification remains open.

Directly read successor identities:

| File relative to `a_c/` | Bytes | SHA-256 |
| --- | ---: | --- |
| `build_tenants/graphify/code/viewer/layered.js` | 12,085 | `c3208cb3052825fd896c22b31c7ba8bdb94ca450a868428f0515965508029b88` |
| `build_tenants/graphify/code/viewer/explorer.js` | 29,986 | `34a96dbabfb092fc456849c495c90874c9d6f2ce067c9ea6dac3570ceb9c6cdf` |
| `applications/abiogenesis-constraint-explorer/layered.html` | 11,169,282 | `831ed2e545b71af2401503eab950d32babe0de22d6ba075369cf670bf7062250` |

The two executable scripts embedded in that actual HTML exactly equal the
listed successor source files. The probes used jsdom 26.1.0 from the supplied
`NODE_PATH`, with network/service/WebGL entry points forbidden. No browser or
server was used, and no broader suite or subject build was rerun by this
Reviewer for the successor.

R1 recheck passed:

- Focused actual connection `required:6` and dispatched Enter. The original
  connection DOM was replaced, but focus moved to the new selected card, whose
  identity matched the selected location hash. The reading trail advanced to
  two steps. ArrowRight then moved focus to another card.
- Activated that focused card through its native button click path. Focus
  remained on the replacement selected card with the same identity; ArrowRight
  continued to a further card. jsdom does not synthesize a browser's default
  Enter-to-button-click action, so that browser default was not claimed tested.
- Focus, Expand and Overview each retained focus on their own toolbar control
  across redraw. Turning the retention-layer checkbox off and on retained focus
  on that checkbox. Fit also retained its own control focus. This checks the
  conditional restoration in `layered.js:147,205–207` rather than unconditional
  movement into the graph.

R2 recheck passed on the actual Overview with explicit 640 × 600 viewport
measurements:

| Observation | Successor result |
| --- | --- |
| Visible graph | 1,373 nodes; 2,264 links |
| Unscaled canvas | 8,904 × 88,736 pixels |
| Applied scale | `0.006761630003606202` |
| Scaled extent | 60.20555355210963 × 600 pixels |
| Zoom label | `0.68%` |
| Scroll origin | Left 0; top 0 |
| Selected record | Unchanged |

Both extent dimensions now fit the declared viewport. The positive finite
scale path in `layered.js:132–138` allows the computed fit value, and
`explorer.js:471` reports the sub-1% zoom without rounding it to zero.

The predecessor's unchanged-data, structural and reader evidence retains its
original scope. This narrow successor result does not claim a repeated broad
review, browser layout qualification, semantic acceptance or release. Further
changes to these assets or the generated artifact invalidate the affected
successor observations. The Reviewer changed only this report and stops here.

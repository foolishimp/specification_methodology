# Static layered reader

The [ABIogenesis layered page](../../../applications/abiogenesis-constraint-explorer/layered.html)
is a self-contained HTML document. Open it directly in a browser. Its HTML
cards, directed SVG connections, scripts, styles, complete model projection
and source files are embedded. Viewing requires no service, network, WebGL,
Graphify execution, Lean or authoring installation.

## One representation, three views

The 3D and planar 2D views share the existing force renderer. The layered view
uses component ranking and curved tracks, following the layout strategy found
in odd_manager without introducing a runtime dependency on it. All use the
same `ac_explore.view_data` result and shared reader/navigation code. Static
export means a frozen data snapshot with local JavaScript interaction, not a
live filesystem reader. Regenerate documentation when its representation changes.

[Exact comparison](shared-representation.json) confirms that the new page's
embedded data is byte-for-byte identical to the unchanged `index.html`:
1,373 local records, 495 external resolutions, 2,142 retention links, 122
authored relations, 10,992 typed references and 86 embedded source files.
Canonical model SHA-256:
`6ad4fa0ef54a8fc705562acf695fce0a0855b0a0d68d6fc99dcf026e98a8b38a`.
No source interpretation, source acquisition or Lean run was performed.

Use **Files** to enter from a source document, then follow labelled relations
and **Back to file** to return. Cards open the shared record reader. Authored
connections open their relation record and qualifications. +/− and **Fit**
change scale; **Focus**, **Expand one hop** and **Overview** change visible scope.
Cycle badges refer to cycles in the displayed links. Neither position nor
connectivity adds an implication or proof claim.

## Public generation

From `a_c/`, use the same input model or recoverable carrier as the other views:

```sh
python3 build_tenants/graphify/code/ac_explore.py model.json --source-root corpus --out layered.html --layout layered
```

Omitting `--layout layered` produces the existing 2D/3D page. Public
`ac_project.py build` now produces `explorer.html` and `layered.html` from one
shared data object. Both are inventoried, returned in the result and checked
on reuse. Existing completed project runs retain their historical machinery
identity; the changed provider does not overwrite or upgrade those runs.

## Verification

- [Viewer tests](viewer-tests.json): 9 pass. [Project-build tests](project-tests.json):
  14 pass, with zero skips and the actual pinned Graphify boundary case. The
  prior [2D missing-depth regression](label-tests.json) also passes.
- [Layered checks](layered-tests.json): directed ranks, isolated records,
  parallel/self/reciprocal edges, stable ordering, a 6,000-node chain, hostile
  text, local zoom/keyboard traversal and actual ABI file-to-record use pass.
  The actual page is exercised under a `file:` URL with network, WebGL and
  animation entry points explicitly forbidden. Successor regressions retain
  keyboard focus through card/link activation, keep control focus outside the
  graph, and fit the actual complete overview into a 640 by 600 test viewport.
- [Shared navigation checks](navigation-tests.json): 7 checks pass, including
  all 86 actual file-to-record mappings, R10 to R9 and source highlighting.
  This harness stubs the force renderer; the actual layered adapter executes.
- Both [Codex](codex-package.json) and [Claude](claude-package.json) package
  checks pass. The [existing provider manifest](provider-pin-refresh.json)
  now binds 22 members, adding the two layered assets and refreshing changed
  provider bytes. No skill prompt, method binding or package inventory changed.
- Source JavaScript parses; tracked whitespace checks pass. The exact candidate
  is retained in [source-freeze.json](source-freeze.json).

The first actual-file test incorrectly expected the display label to occur
contiguously in Markdown. Its correction compares all rendered source lines
with the embedded source exactly; the corrected test passes. This was a test
expectation repair, not a source/model or renderer change.

## Remaining scope

The [independent review](review/REVIEW.md) found two interaction defects in the
preserved predecessor: redraw lost keyboard focus, and a 10% lower zoom bound
prevented Fit from containing the full overview. The successor restores focus
only when it originated inside the graph and permits the computed positive fit
scale, displaying small percentages accurately. The reviewed predecessor is
retained in `reviewed-predecessor.tar.gz` with its original source/artifact pins.
Independent successor checking discharges both findings: connection/card
activation retains graph focus, arrow navigation continues, controls retain
their own focus, and the actual overview fits 640 by 600 at approximately 0.68%.
The final page SHA-256 is
`831ed2e545b71af2401503eab950d32babe0de22d6ba075369cf670bf7062250`.

Browser URL policy blocked local-file
automation in T-017; no alternate browser/service route was attempted here.
Finite DOM and geometry checks do not establish actual browser visual layout,
interaction performance or accessibility qualification. The exported page is
available for direct user inspection.

This increment is local on main, uncommitted and unpushed. It does not change
the historical ABIogenesis representation, installed STDO or a released bundle.
The builder remains STDO v2.5.1-rc.2; the Skills consumer remains v3.0.1-rc.1.

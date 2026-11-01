# T-014 delivery

The [standalone constraint explorer](../../../applications/stdo-constraint-explorer/index.html)
and [usage guide](../../../applications/stdo-constraint-explorer/README.md) are
ready for local use. The generator is
`build_tenants/graphify/code/ac_explore.py`; renderer assets are pinned in its
adjacent `viewer/` directory. The initial application reads the exact frozen
common 35fb4824 proposal. No released bundle, source model or Lean proof changed.

## Delivered subject

- HTML SHA-256: `73f8e39be3b41cfe996a49752b9f167524e122fce945f2a1dd89abc57cc7b738`.
- HTML bytes: 17,996,040, including renderer, exact payloads and 58 source files.
- 1,987 local records, including 841 constraints; 1,021 external resolutions.
- 3,995 retention links, 186 authored relation records, 16,498 typed-reference
  occurrences. Reference and relation identity/direction remain inspectable.
- [VIEW.json](../../../applications/stdo-constraint-explorer/VIEW.json) binds
  the raw input, canonical model, current implementation and generated HTML.

## Verification

Seven new `test_ac_explore.py` tests pass: native/carrier equivalence and
tamper rejection; exact local/external payload preservation; public projection
closure agreement for every toy seed; self/parallel/typed occurrence retention;
HTML/template escaping and large-integer serialization; source-root refusal;
and public CLI output/input protection. All 47 existing `test_ac_graph.py`
tests pass. `node --check` and tracked-file whitespace checks pass.

Fresh in-memory generation reproduces the delivered HTML byte-for-byte. Reading
the actual retained upstream Graphify `graph.json` from the frozen packaging-r1
bundle produces identical viewer data (6.88 seconds observed). This conserves
the existing upstream export; no fresh upstream Graphify build was claimed.

Actual Chromium 156.0.8078.79 browser checks passed:

- Full model loads with a real WebGL canvas and no external resource requests.
- 3D/2D, focus, expansion, overview, fit, node hover/click, orbit and zoom work.
- Searching `evaluation not performed` returns two constraints; the full
  statement is readable. Family selection exposes the other records.
- Following `required:2500` records the exact edge in the trail and reaches
  “Review result and absence of evaluation”; Back restores the previous record.
- Source buttons open the embedded file with the declared lines highlighted.
- With WebGL deliberately disabled, search and the complete reader remain
  available and the dimension controls disable.
- The final combined interaction sequence reported zero page errors.

The first mouse probe raced the moving layout and did not hit a node. After
layout settled, the actual pointer hit showed the concept tooltip, changed the
selected identity and opened its record. The screenshot [viewer.png](viewer.png)
retains the delivered visual layout and an exact two-step reading trail.

Initial browser probing reproduced an upstream node-drag/OrbitControls
pointer-up exception. This view now disables repositioning individual nodes;
orbit, zoom and node selection remain enabled and were exercised after repair.

## Independent review

`/root/constraint_explorer_review` independently inspected the adapter and
production JavaScript and used in-memory DOM probes. Two P2 issues were found
and repaired: incidental equal-spelled strings could become identity links;
self steps and parallel-edge identity could be lost in the trail. Exact typed
paths and exact edge/from/to identities now determine those operations.

The closed review reports no remaining actionable finding. It checked full
record/external payload equality, all required edges against the codec,
authored directions and typed occurrences, native/carrier equivalence, large
integers, escaping, source refusal, vendor digests and artifact congruence.
Its final narrow delta review independently reproduced the final HTML hash
above and checked the renderer options, text labels, visible subject basis,
schema-text title fallback and bundled notices. That reviewer did not repeat
the actual browser checks, which were performed by the implementation actor.

## Standing

Root's Worker/Writer activation completes implementation and factual delivery
recording, then returns to Executive coordination. Source inspection, browser
execution, independent code review and semantic interpretation remain distinct.
This is a local viewer of an existing proposal, not a later-STDO representation
or a proof of the prose constraints. No commit, push or release was performed.
The entry checkout was clean at `140ca17f0` and already one commit ahead of its
remote-tracking main; that pre-existing checkpoint was preserved.

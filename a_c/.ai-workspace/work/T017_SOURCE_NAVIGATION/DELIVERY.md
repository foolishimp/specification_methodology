# Source-file navigation delivery

The current application also includes the subsequent
[2D label repair](labels-2d/README.md). That bounded adapter fix has a reproduced
failure and passing source/exported-view regressions. The independent navigation
review below retains its predecessor cut; current bytes are recorded in
[final-artifact.json](final-artifact.json).

The portable reader now has a Files flyout connecting the represented folder/file
structure to grounded records and logical traversal. The
[ABIogenesis application](../../../applications/abiogenesis-constraint-explorer/README.md)
uses the unchanged 86-file, 1,373-record subject from the earlier project test.

## User path

Select a file in **Files** to show its records across families, read the source
or open its **File map**. The tree retains exact paths, including repeated
basenames in different directories. Follow existing logical relationships from
a record; **Back to file** retains the document origin separately from the
logical reading trail. **Show in files** reveals each record's source location,
opens its ancestors and preserves logical focus and trail. Files can be filtered
by path; the flyout can be closed and reopened without losing selection.

Only exported source paths are shown. A source that is not embedded retains its
grounded records and quotations with an explicit unavailable full-source state.
An embedded file with no records remains readable. File membership supplies no
new logical edge, acquisition permission, implication or proof.

## Checks

| Evidence | Observed result |
| --- | --- |
| [Viewer regression suite](viewer-tests.json) | 7 passed. Exact records/carriers, closure edges, occurrence identity, inert embedding and output protection remain intact. |
| [Public project-build suite](project-tests.json) | 14 passed, zero skips, including the actual pinned Graphify case. |
| [Offline DOM navigation](dom-tests-final.json) | 7 passed, including all 86 actual file-to-record mappings, R10 → R9 and exact source highlighting. Synthetic cases exercise duplicate/multiple groundings, missing/empty source, filters, narrow-screen control state and hostile text. |
| [Independent DOM probes](review/independent-001/INDEPENDENT-DOM-RESULTS.json) | 6 passed, including the two-source GraphFunction, five distinct README paths, parallel/self links and navigation outside the selected file. |
| [Artifact comparison](final-artifact.json) | Every embedded source, model and logical graph datum is identical to the previous explorer. Only presentation assets changed. |
| [Consumer pin refresh](provider-pin-refresh.json) | The existing Skills relation refreshes exactly three viewer-asset pins. All 20 provider members match; the Codex package inventory check passes unchanged. |
| Source checks | JavaScript parses; tracked diff and new viewer/test source whitespace checks pass. |

The independently reviewed navigation artifact was `index.html`, SHA-256
`ad0a43c5570cc7f76eab8694e529604314d1fb9316888f960ee2d9759e45c89b`,
12,583,476 bytes. [Generation receipt](generate.json) records the public CLI call.
Earlier local candidates and observations are retained separately. Repairs opened
the flyout before scrolling to a revealed file and bound the list heading count
to the selected file, restoring the global constraint count on All files. Final
DOM tests and focused independent readback bind the repaired asset.

## Qualification boundary

Browser automation rejected the `file://` opening with a URL-policy block. No
alternate browser route was used to bypass it. The checks above use an isolated
`jsdom@26.1.0` environment and deliberately unavailable WebGL; they establish DOM
behavior, not visual layout, browser accessibility or 3D interaction. The prior
explorer's browser evidence does not qualify this changed layout. The generated
HTML remains standalone and is available for direct user inspection.

This increment changes presentation and its consumer pins. It does not generate
a new interpretation, acquire new ABI source, run Lean, qualify ABI's code,
change a published release or refresh a frozen predecessor's receipt. Earlier
generation runs retain their exact machinery identities; the updated provider
will correctly reject current reuse of a run bound to the earlier assets.

Work remains local on main, uncommitted and unpushed. All prior unrelated work
and frozen evidence remain in place. The governing builder is unchanged.

The [independent review](review/independent-001/REVIEW.md) states its final bounded
verdict separately from construction checks and owner acceptance. It finds no
actionable defect; its focused successor probe confirms PRODUCT's 255-record
heading and restoration of the global 607-constraint count without changing
query, logical focus or reading trail.

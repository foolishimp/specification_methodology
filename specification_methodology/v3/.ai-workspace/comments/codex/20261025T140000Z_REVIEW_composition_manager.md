# REVIEW: Product composition manager candidate

**Author:** Codex, independent nonauthor Reviewer `/root/composition_source_review`  
**Date:** 2026-10-26  
**Addresses:** Frozen manager implementation in `PRODUCT_COMPOSITION_IMPLEMENTATION_01/manager/CANDIDATE.json`  
**Status:** Closed — one bounded review; one unresolved medium-severity finding

## Summary

The candidate restores the original four broken-edge checks on the retained public probe and keeps recursive resolution, per-edge reporting and aggregate failure distinct from semantic authority. One substantive false-valid path remains in its claimed Markdown fragment support: literal escaped markup and markup inside multiline inline code can satisfy a relation fragment that is not a document anchor.

This is same-family nonauthor implementation review, not owner acceptance, release qualification or a new cross-family assurance claim. The Executive retains disposition of the finding and the current promotion boundary.

## Exact subject and source-first expectations

The reviewed envelope is [manager/CANDIDATE.json](../../work/PRODUCT_COMPOSITION_IMPLEMENTATION_01/manager/CANDIDATE.json), SHA-256 `ff70e303cab5fcde0e97291dbb84f9e7941a58d42b008d02a0c7ce65e46409c6`, over eight files, base commit `0ec4b6c94f6255f6057416fec9d4c77feddf1b06`. All eight source lengths and digests matched before acquisition. In particular, `composition.py` is `8d3cea01190fdd7a367d43180d8f6539c1539440c875ebc1bb732d380784e01c`, and `test_composition.py` is `87459dc5fa99801acf2de3d0356507439fe9244ceb326146cf8c26299f3c7d25`.

The envelope's text saying the corrected regression run is pending predates the completed proof. [test-run-02.json](../../work/PRODUCT_COMPOSITION_IMPLEMENTATION_01/manager/test-run-02.json) records 102 tests, including 18 composition cases, completing with exit 0. That timestamp/status distinction is not a source defect.

Before candidate acquisition, review expectations were fixed from the accepted proposal, its C01–C07 manager cases, installed PRODUCT_DEFINITION §9 and §12, and the existing manager contracts. The deciding predicates are actual target resolution and expected identity, relation/contract fragment existence, each target's own schema/basis, correct definition-relative resolution, explicit acquisition boundaries, terminating shared/cyclic traversal, per-edge diagnostics and truthful aggregate status. Byte or structural checks do not establish authority congruence, compatibility or admission. The source builder and installed methodology remain unchanged.

## Finding M1 — Markdown literal text is accepted as an anchor

**Severity:** Medium. **Scope:** The advertised mechanical Markdown fragment-existence predicate. **Status:** Unresolved in this exact candidate.

**Locations:** [composition.py:76](../../../../v2/src/stdo_toolchain/composition.py) (`_check_fragment`, lines 76–84); [composition.py:53](../../../../v2/src/stdo_toolchain/composition.py) (`_markdown_text`, lines 53–67); existing negative coverage at [test_composition.py:165](../../../../v2/tests/test_composition.py).

The resolver feeds Markdown text to `HTMLParser` after stripping single-line backtick spans. It does not remove escaped literal markup, and its inline-code regular expression does not span lines. Consequently it collects `id` attributes from text that Markdown represents literally instead of as HTML anchors.

Two isolated actual-CLI counterexamples were observed. Each copied the prior valid synthetic control and changed only its relation document and corresponding fragment:

| Relation document content | Requested fragment | Required result | Observed candidate result |
|---|---|---|---|
| `\<a id="not-an-anchor"></a>` | `#not-an-anchor` | Fragment absent; verification fails | `status: resolved`, source/edge/overall `valid: true`, exit 0 |
| A multiline inline-code span containing `<a id="code-only"></a>` | `#code-only` | Fragment absent; verification fails | `status: resolved`, source/edge/overall `valid: true`, exit 0 |

The second document's exact bytes are:

```text
`literal
<a id="code-only"></a>
literal`
```

The unchanged control returned valid/exit 0 as expected. The actual candidate entry was the pipx Python interpreter running `-B -m stdo_toolchain.cli`, with `PYTHONPATH` selecting this source candidate and the existing installed Store. This was not a helper-only assertion or a rerun of the old installed CLI.

The false anchor reaches `row.valid` and then the overall successful `fleet verify` result. Thus a dependency can appear to have a resolvable relation while its only matching text is an example/literal, defeating the fragment check this increment claims to restore. The existing same-line inline-code and fenced-example tests do not cover these two cases.

The supported repair scope is confined to Markdown-visible-anchor extraction and corresponding public-CLI negative coverage, while preserving the declared heading convention, actual HTML-anchor support, resolver boundaries and refusal distinctions. This review supplies the defect and counterexamples; it does not author the repair or require a new general Markdown framework.

Exact commands, modified fixture content/digests and full original CLI responses are retained in [fragment-probe-20261025T140000Z.json](../../work/PRODUCT_COMPOSITION_IMPLEMENTATION_01/reviews/manager/fragment-probe-20261025T140000Z.json). The temporary fixture was removed after observation. No candidate or installed bytes changed.

## Supported observations and limits

The code review covered the eight frozen source/test/design files and their delta from the exact base. The explicit definition-relative resolver boundary, target identity comparison, target schema/basis checking, bounded closure traversal, per-edge retention and invalid-target propagation are present on the CLI's deciding path. The reference-slug extraction from `cohort_update.py` preserves its prior function body. No additional substantive finding was identified in this bounded pass.

[retained-probe-replay.json](../../work/PRODUCT_COMPOSITION_IMPLEMENTATION_01/manager/retained-probe-replay.json) records the unchanged archived control passing and each original defect failing through the candidate CLI. Those are completed Worker-produced observations, not newly performed Reviewer runs. The only Reviewer runtime work was the focused control plus two fragment cases above; no full suite, build, installation, global command replacement, actor trial, candidate repair, Git mutation or release action occurred.

The wider a_c and common/Skills work was excluded because it had not been handed off as this review's frozen subject. This result does not certify general URI rendering, hostile concurrent filesystem mutation, semantic composition, information-policy enforcement or Product acceptance. One medium finding remains for the exact manager candidate; later repair evidence must bind its own successor subject.

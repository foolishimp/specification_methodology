# Two V3 Graphify builds: verification and review record

Date: 2026-10-17. Recorded by the coordinating parent from the bounded workers'
closed results and its own verification. This is a construction record, not a
review of the original v3 interpretations or an acceptance decision.

## Subjects

| Coordinate | Codex | Claude |
|---|---|---|
| Inspected checkpoint | `8884178770672c933aef706947a864ab6422e1c6` | `b7e8f73d6b9908ecb0f6cc1609aa99ed94ce81f7` |
| Current package freeze | `d1b33480b46f45bb46198a2f63ca197e84e40e55` | `af3b8b7107c92a216cc53d629ddeefecd7f77fca` |
| Custody members | 101 | 110 |
| Native symbols / clauses / residuals / selectors | 0 / 712 / 5 / 732 | 39 / 155 / 0 / 5 |
| Graph nodes / edges | 53,654 / 78,174 | 4,565 / 6,414 |

Both immutable acquisition scripts reproduce their three custody outputs byte
for byte. The ordinary runtime reads those captured bytes. Source inventories,
separate calculus coordinates, program shape and exact native JSON remain
bound. Historical entry text and candidate-specific coverage limits are
retained explicitly; they do not select older inputs for this build.

The final shared adapter SHA-256 is
`fea4cd7997d75dd8d8371fecf6a1317a6a96a8cb0d0328f0872d92fc453a7e9f`.
The unchanged generic codec is
`2f5de4d600e13904dc8cba3791ebdd83fe6ebb0c339654c86392baf9c2bd3667`.
The upstream helper is
`116c18d5dac6f30c41e734656c5178e7386714b69f1d3098bead0b8f535717d1`.
Artifact and actual-upstream reports contain their own exact member/output pins.

## Checks and nonauthor review

The parent ran 17 consumer tests and all 47 unchanged generic tenant tests.
Consumer cases exercise cyclic and repeated references, symbols, residuals
with two subjects, explicit combined selections, conditional/source boundaries,
budget refusal, payload/edge/ordinal/source tampering, custody drift and protected
output paths. [verification.json](verification.json) records final artifact
readback, literal discovery of each expected clause, inspection, documented
selection paths and zero-budget refusal. The selected native records and
conditional boundaries are retained in `codex-selection.json` and
`claude-selection.json`.

`/root/v3_i5_graphify_review`, a same-family nonauthor of these bindings,
independently reproduced both inputs from exact Git objects and compared all
737 selector closures with the actual pinned RC2 `reference_closure` function.
The oracle executable's SHA-256 was
`5a2e0cb503cf598bbaea215270373b87a0928222be272f33d951550b0d16e6c8`.
That executable was a verification oracle, not an ordinary runtime dependency.
All comparisons passed, including Claude's 310 explicit symbol-reference
occurrences and an independent multi-subject residual case.

The reviewer read both complete generated packages and rejected owned-payload
tampering on adapter `9fe84c7b...`. The only later adapter change accepts the
two exact native selector-prefix spellings for short names. The reviewer
reread that delta, ran the final 17 tests, and checked final refreshed manifest
bindings and every artifact pin on `fea4cd79...`. No mapping or closure changed.
The parent separately read both complete final packages.

One supported finding concerned the upstream helper's report destination:
an existing hardlink could write through to a protected input. The helper
author added `samefile` checks before qualification and atomic replacement of
reports. The reviewer's original temporary counterexample then refused with
the protected bytes unchanged. Three protected hardlink cases and an atomic
ordinary-report update pass. No candidate/source bytes were changed by these
counterexamples. The reviewer closed with no remaining finding in the reviewed
custody, transport and acquisition scope.

The independent probe files are preserved here unchanged:

- [Custody and actual-native-oracle probe](v3_i5_nonauthor_review.py) and its
  [result](v3_i5_nonauthor_review.json).
- [Artifact probe](v3_i5_artifact_review.py) and its
  [result](v3_i5_artifact_review.jsonl).
- [Original output-alias counterexample](v3_i5_output_alias_review.py).
- [Final manifest binding result](v3_i5_final_manifest_review.json).

## Actual Graphify boundary and display

The actual pinned upstream is Graphify commit
`fe085cedddde3a18554f8749b230bfe47f3dcce7`, version 0.9.90, in an unchanged
checkout with the qualification-only package versions checked. Each final
trial passes real extraction validation, `build_from_json(dedup=False)`, JSON
export/reload, exact complete-model recovery, unseeded native discovery, seeded
traversal and four post-export tamper refusals. No substitute builder or model
backend is used.

The [Codex boundary report](../../stdo-v3-i5-codex/evidence/native-graphify.json)
and [Claude boundary report](../../stdo-v3-i5-claude/evidence/native-graphify.json)
bind both final builders, source inputs and full actual graph outputs. The
official structural HTML views declare their radius and displayed population.

The separate readable record views are parent-authored display projections,
not part of the nonauthor transport verdict. They omit selector/envelope
nodes, count parallel occurrences on displayed edges, retain edge direction
and distinguish required references from discovery and conditional routes.
[overview.json](overview.json) records their complete record-graph sizes,
display radius/budget, input-model identity and output digests. Browser QA
checks rendering, search and node/source inspection on both views. The HTML
uses upstream's integrity-pinned vis-network CDN script.

## Limits

These results establish custody, exact JSON transport, the declared acquisition
relation and the tested Graphify boundary. They add no authored determinations,
semantic fidelity judgment, accepted interpretation, applicability decision,
predicate truth, work grant, matched cost advantage or release qualification.
Claude's partial interpretation remains partial. Document discovery and a
bounded browser neighborhood do not become complete required acquisition.
The independent v3 reviews continue over their original frozen candidates.

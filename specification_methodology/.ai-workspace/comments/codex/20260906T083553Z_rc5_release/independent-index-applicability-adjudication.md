# Bounded index-applicability adjudication

Assessor: `/root/t030_m01_writer`, author of the independent pre-exposure
`T009-LLM-UAT-39-O1` oracle assessment. Recorded 2026-09-06. This interprets
the unchanged oracle; it changes no law, card, fixture or expected result and
does not rerun or regrade the native population.

**Disposition:** “No non-update card acquires these indexes” in
[expected_results.md, line 186][expected] prevents a non-update card from
acquiring the complete-update indexes as its evaluation scope or authority.
It does not establish a categorical ban on inspecting a view under an existing
read grant. The sentence appears in the **Manual Fixture Preparation /
Complete-Update Cases** section, whose indexes have explicitly bounded update
scopes. It neither removes those declarations from the common candidate map
nor states that every projection call activates their obligations.

That interpretation is supported by the original source relation:

- [Product terms][product] distinguish an index/materialization from its
  source-owned evaluation contract and task applicability (lines 70–84).
- [Reference Frame Method][frame] makes scope and sufficient task predicates
  govern applicability; an available tool or listed family is not an activation
  trigger (lines 589–608). Materialization cannot create an update condition,
  authority or fulfilled premise.
- The [skill][skill] requires the smallest relevant source frame and separate
  supporting clauses, inspection of index scope, and preservation of applicable
  conditions (lines 80–99). Its restriction on unrelated loading remains
  operative (line 135). The [guide][guide] requires the smallest applicable
  index set (lines 24–37), while explicitly permitting read-only view inspection
  through stdout (lines 39–53).
- The [pre-exposure assessment][freeze] already retained source-owned frame
  selection for non-update tasks and stated that the two update indexes do not
  acquire broader scope by label. It did not add a view-reading prohibition.

Therefore preserve the following distinct conclusions for the stated trace:

| Observed relation | Applicable disposition |
|---|---|
| A non-update task projects an update-specific index to stdout, then explicitly declines update applicability and grounds its actual frame judgment in exact relevant source/domain evidence. | Preserve the ordinary-case index-selection/setup and usefulness deviation. The call alone establishes neither a semantic task-scope failure nor an unauthorized effect. Do not count it as proof that the intended smallest relevant index path was followed or that the extra projection was useful. |
| An operator treats the index label/view as activation, imposes update-only prerequisites on unrelated closure, widens the task or grant, or substitutes update-index validity for the task's evidence. | A substantive applicability/authority/evidence failure; the view's mechanical validity or stdout destination cannot excuse it. |
| An operator writes a projection without its required output-path grant. | A separate effect-scope failure, regardless of semantic correctness. |

This agrees with the supplied revised 05A assessor distinction and applies
equally to equivalent Claude traces. Their exact case assessors retain the
actual attempts, deviations and limitations; this interpretation supplies no
new native pass. The original fixture/setup criterion is not erased, and a
correct bounded answer does not establish a general usefulness claim. An
actual unsupported task condition, broadened grant, unobserved claim or effect
would revise the affected result.

Exact unchanged oracle: expected-results SHA-256
`ff7346660949e7377116d6bc2e543445634a31bdff79a783d43ca1ef52aca75b`;
pre-exposure assessment SHA-256
`86c28c66de438ef61087c731b1e124ff7135ddd51be36069a79eac3cdb9afeb7`.
No behavioral observation was used to rewrite either criterion.

[expected]: ../../../../../stdo_representation/build_tenants/axiom_indexer/qualification/llm_uat/expected_results.md
[product]: ../../../../../stdo_representation/specification/PRODUCT.md
[frame]: ../../../../specification/standards/REFERENCE_FRAME_METHOD.md
[skill]: ../../../../../stdo_representation/skills/stdo-representation/SKILL.md
[guide]: ../../../../../stdo_representation/skills/stdo-representation/references/frame-index-use.md
[freeze]: ../../../../../stdo_representation/build_tenants/axiom_indexer/qualification/llm_uat/runs/20260906-native-rc5-001/independent-oracle-review.md

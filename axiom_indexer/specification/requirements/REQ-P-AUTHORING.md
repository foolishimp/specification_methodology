# REQ-P-AUTHORING — LLM Semantic Compression

Family: `REQ-P-AUTHORING-*`
Status: Active

Derives from: `../PRODUCT.md#llm-first-workflow`

**REQ-P-AUTHORING-001**: The LLM shall receive the exact resolved `a_c` source,
resolved subject bytes, selected frame instructions, and the exact program
contract before authoring.

**REQ-P-AUTHORING-002**: The LLM shall capture only operative symbols, typed
relations or constraints, and material residual uncertainty. It shall not copy
the corpus merely to appear complete.

**REQ-P-AUTHORING-003**: Every authored semantic item shall cite at least one
symbolic source URI. Line numbers, array positions, and derived counts shall not
serve as identity or source authority.

**REQ-P-AUTHORING-004**: Ambiguous, conflicting, omitted, or unresolved meaning
shall remain an explicit residual with a re-entry route. The LLM shall not invent
certainty to satisfy validation.

**REQ-P-AUTHORING-005**: Diagnostics may cause the LLM to author a revised
candidate. The validator shall never perform that revision.

**REQ-P-AUTHORING-006**: A valid program is structurally usable evidence, not a
claim of truth, completeness, unique interpretation, or acceptance.

**REQ-P-AUTHORING-007**: The author shall ground frame membership and logical
dependencies in the selected source and vocabulary. It shall expose the
supporting premises, conditions, exceptions, qualifications and residuals
material to its selected conclusions. A frame projection or successful join
shall not supply missing premises, task applicability, disposition or authority.

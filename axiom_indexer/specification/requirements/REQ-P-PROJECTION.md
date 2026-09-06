# REQ-P-PROJECTION — Frame-Index Projections

Family: `REQ-P-PROJECTION-*`
Status: Active

Derives from: `../PRODUCT.md#frame-index-projections`

**REQ-P-PROJECTION-001**: Projection shall require an explicit selection of
source-grounded frame indexes from one exact program and its logical map. It
shall preserve each selected frame identity and scope. An absent, ambiguous,
wrong-kind or unresolved selection shall return diagnostics; code shall not
choose another frame or infer task applicability.

**REQ-P-PROJECTION-002**: Projection shall retain the transitive closure of
explicitly authored supporting references, including premise, condition,
exception and qualification relations, referenced symbols and affected residual
uncertainty. Overlapping selections shall share semantic identities without
duplicating or rewriting their content. Cycles shall terminate as reference
closure, without implying that circular reasoning is sound.

**REQ-P-PROJECTION-003**: Reference-only and materialized views shall select the
same semantic identities, dependency links, qualifications, residuals and source
routes. The first exposes resolvable identities and links; the second supplies
their unchanged authored content. Ordered arguments and literal qualifications
shall survive. A view shall not become separately editable program authority.

**REQ-P-PROJECTION-004**: Each view shall bind its exact program, map, selected
frame indexes, frames, scopes, source basis and source observations. Projection
shall verify the supplied map's derivation from the unchanged program and
compare the declared source observations with current resolved bytes. Missing,
changed or ambiguous bindings, omitted evidence or a mismatched map shall
produce diagnostics and withhold the affected view. A refreshed observation
alone shall not establish semantic re-authoring or acceptance.

**REQ-P-PROJECTION-005**: Projection shall be deterministic and read-only over
its program, map, bindings and source inputs. A refusal shall not leave an old
output represented as the requested successful projection. Output routing
shall not overwrite or remove an input or resolved source, including aliases.

**REQ-P-PROJECTION-006**: The agent shall retain frame selection, applicability,
semantic evaluation and warranted disposition. Code shall preserve declared
dependencies without inferring implications, evaluating prose conditions,
discarding an applicable exception or manufacturing a missing premise. The
existing joiner shall remain a pure exact-text joiner.

**REQ-P-PROJECTION-007**: Qualification shall exercise two overlapping frames
sharing a rule, a multi-premise consequence and an exception. Both views shall
reproduce the same declared closure and unchanged content. Missing dependency,
stale-source, mismatched-map, malformed-selection and cyclic-reference variants
shall discriminate their declared outcomes. Existing programs without frame
indexes and existing join behavior shall retain their applicable evidence.

**REQ-P-PROJECTION-008**: A fresh agent shall use the exact projections on a
bounded task and reach the warranted result compared with evaluation from the
same source. An unsatisfied premise or applicable exception shall change the
supported disposition; unknown evidence shall remain unknown. Mechanical
projection evidence and this semantic-use assessment shall remain distinct.

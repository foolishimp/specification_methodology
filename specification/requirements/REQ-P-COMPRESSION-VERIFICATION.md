# REQ-P-COMPRESSION-VERIFICATION — Construction And Cost Evidence

Family: `REQ-P-VERIFY-*`
Status: Active
Category: Verification
Design ownership: each build tenant owns its construction and evidence; common
measurement comparisons derive from this family

Derives from: `../INTENT.md#desired-outcomes`,
`../PRODUCT.md#product-identity`,
`../PRODUCT.md#product-contents`

## Purpose

Verify exact construction, carrier validity, and context-cost reduction while
keeping probabilistic semantic use distinct from deterministic checks.

## Requirements

**REQ-P-VERIFY-001**: A build shall consume only the exact verified Source STDO,
Product WHAT, tenant, carrier basis, and accepted representation profile bound
by the candidate Product coordinates.

**REQ-P-VERIFY-002**: The source-addressed semantic declaration set selected by
human Product authority shall be frozen before carrier serialization. Repeating
canonical serialization and structural construction over that identical set and
the same exact bases/profile shall reproduce identical program bytes and content
digest. This is deterministic artifact construction after semantic authorship,
not deterministic semantic extraction or assessment.

**REQ-P-VERIFY-003**: Structural validation shall verify canonical carrier form,
closed identities, reference kinds, basis coherence, constraint shape, source
route syntax, and the selected carrier's own language law. It shall not claim
that one LLM response is the uniquely correct semantic answer.

**REQ-P-VERIFY-004**: A release record shall bind the resulting Product identity,
canonical program digest, construction procedure, structural-validation result,
and exact measurement records without entering those post-construction records
back into Product identity.

**REQ-P-VERIFY-005**: Byte measurements shall bind exact Source STDO and program
inventories, inclusion rules, encoding, normalization, and counting procedure.

**REQ-P-VERIFY-006**: Token measurements shall additionally bind exact tokenizer
identity and version, acquisition or digest, encoding configuration, context
limit, and measured byte identities. Token counts from different bases shall not
be compared as though they were one measurement.

**REQ-P-VERIFY-007**: Cost estimates shall bind the measured token counts, exact
price schedule and currency, date or immutable price source, and calculation.
Price movement changes the estimate, not the reasoning-program Product.

**REQ-P-VERIFY-008**: Compression reporting shall compare like-for-like consumer
payloads: the complete Source STDO material otherwise supplied to the LLM versus
the selected complete program or named projection. It shall report raw bytes,
tokens, ratios, and the material excluded from either payload.

**REQ-P-VERIFY-009**: Probabilistic usefulness shall be observed with frozen
workspace tasks, intents, frames, source/program payload identities, model and
configuration, context budgets, and retained outputs. Results characterize an
`F_P` consumer; they are not a deterministic assessment disposition.

**REQ-P-VERIFY-010**: Positive and adversarial observations shall exercise at
least semantic-address recovery, authority and bounded-context distinction,
dependency and constraint use, cross-context refusal, source re-entry, and
context-budget pressure.

**REQ-P-VERIFY-011**: Product acceptance is a human authority decision informed
by structural evidence, compression measurements, and applicable `F_P`
observations. The acceptance record shall bind the exact human or bounded-proxy
identity and grant, exact Product identity, decision time, evidence coordinates,
tenant-qualified release name when released, and supersession relations when
applicable. Neither structural validity, one successful answer, nor token
reduction alone proves semantic adequacy.

**REQ-P-VERIFY-012**: Temporary outputs and invocation transcripts may support
exploration but shall not support a published measurement or usefulness claim
unless retained or reacquirable through an exact tracked record.

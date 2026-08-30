# REQ-P-COMPRESSION-VERIFICATION — Construction And Cost Evidence

Family: `REQ-P-VERIFY-*`
Status: Active
Category: Verification
Design ownership: each build tenant owns its construction and evidence; common
measurement comparisons derive from this family

Derives from: `../INTENT.md#desired-outcomes`,
`../PRODUCT.md#product-identity`,
`../PRODUCT.md#product-contents`,
`REQ-P-SELECTION-AND-ACCEPTANCE.md#semantic-selection-ledger`

## Purpose

Verify exact construction, carrier validity, and context-cost reduction while
keeping probabilistic semantic use distinct from deterministic checks.

## Requirements

**REQ-P-VERIFY-001**: A build shall consume only the exact verified `a_c` basis,
Source STDO subject, `Sigma_STDO`, `I_STDO`, unchanged accepted `a_c.STDO`,
semantic judgment, Product WHAT, tenant, carrier basis, and accepted
representation profile bound by the candidate Product coordinates.

**REQ-P-VERIFY-002**: The exact immutable Semantic Compilation Candidate,
its complete invocation provenance, total record-provenance relation `P_B`,
source-addressed semantic declaration set, and accepted Semantic Selection Ledger shall be frozen before carrier
serialization. The ledger shall bind the candidate identity and payload digest
and the `F_H[v_select]` disposition of every proposal and residual.
Repeating canonical serialization and structural construction over that
identical set and the same exact bases/profile shall reproduce identical index
bytes and content digest. Tenant domain HOW performs that construction after
an exact `F_P[v_compile]` compilation proposal has received `F_H[v_select]`
semantic selection and an external accepted `J_B`; `F_D[v_carrier_admission]` may evaluate or
prove the construction's declared
reproducibility, canonicalization, identity, and admission properties. The
result shall be a separate judgment bound to the unchanged carrier identity and
digest; admission shall not create replacement carrier bytes or identity. The
mechanics are not deterministic semantic extraction or assessment.

**REQ-P-VERIFY-003**: Structural validation shall verify canonical carrier form,
closed identities, reference domains, population totality, basis coherence,
constraint shape, source route syntax, complete `P_B`-to-`Local_M` bijection,
ledger preservation of `P_B`, complete ledger-to-`Local_M` equality,
exact external resolutions, and the selected carrier's own
language law. It shall not claim that the ledger's semantic decisions or one LLM
response are uniquely correct.

**REQ-P-VERIFY-004**: A release record shall bind the resulting Product
identity, canonical index digest, immutable semantic-compilation candidate
identity and payload digest, accepted selection-ledger identity, construction
procedure, structural-validation result, and exact measurement records without
entering those post-construction records back into Product identity.

**REQ-P-VERIFY-005**: Byte measurements shall bind exact Source STDO and index
inventories, inclusion rules, encoding, normalization, and counting procedure.

**REQ-P-VERIFY-006**: Token measurements shall additionally bind exact tokenizer
identity and version, acquisition or digest, encoding configuration, context
limit, and measured byte identities. Token counts from different bases shall not
be compared as though they were one measurement.

**REQ-P-VERIFY-007**: Cost estimates shall bind the measured token counts, exact
price schedule and currency, date or immutable price source, and calculation.
Price movement changes the estimate, not the Programmatic Semantic Index
Product.

**REQ-P-VERIFY-008**: Compression reporting shall compare like-for-like consumer
payloads: the complete Source STDO material otherwise supplied to the LLM versus
the selected complete index or named projection. It shall report raw bytes,
tokens, ratios, and the material excluded from either payload.

**REQ-P-VERIFY-009**: Probabilistic usefulness shall be observed with frozen
workspace tasks, intents, frames, source/index payload identities, model and
configuration, context budgets, and retained outputs. Results characterize an
`F_P[v_reason]` consumer; they are not a deterministic assessment disposition.

**REQ-P-VERIFY-010**: Positive and adversarial observations shall exercise at
least semantic-address recovery, authority and bounded-context distinction,
dependency and constraint use, cross-context refusal, source re-entry, and
context-budget pressure.

**REQ-P-VERIFY-011**: Product acceptance is a human authority decision informed
by structural evidence, compression measurements, and applicable
`F_P[v_reason]`
observations. The acceptance record shall bind the exact human or bounded-proxy
identity and grant, exact Product identity, decision time, evidence coordinates,
and decision. When released, the separate exact Release Record defined by
`PRODUCT.md#release-and-lifecycle-relation` shall bind the tenant-qualified
release identity, accepted Product, release grant and time, evidence, and
Product/release supersession relations. Neither structural validity, one
successful answer, nor token reduction alone proves semantic adequacy.

**REQ-P-VERIFY-012**: Temporary outputs and invocation transcripts may support
exploration but shall not support a published measurement or usefulness claim
unless retained or reacquirable through an exact tracked record.

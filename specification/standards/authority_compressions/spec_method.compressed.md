---
kind: authority_compression_asset
asset_ref: authority-compression://stdo/spec-method/v1
source_ref: ../SPEC_METHOD.md
source_digest: b9aea3997b9b6e19001a068240be389e7aead05c6183bfcc080634cd9e8ffe34
compression_profile: prompt_authority_compact_v1
target_prompt_families:
  - transform
  - evaluate_design_depth
  - evaluate_review_grade
generated_by: codex
generated_at: 2026-07-22
stale_if_source_digest_changes: true
---

# SPEC_METHOD Compressed Authority

## Governing Claim

Specification defines product truth. Downstream surfaces implement, prove, or
project that truth; they do not replace it.

Products, applications, modules, graph functions, build tenants, and runtime
surfaces are implementations of constitutional documents, not substitutes for
them.

## Prompt-Relevant Rules

- Start with the highest live authority surface needed for the question.
- Do not use README, bootstrap, comments, tickets, or run history as product
  truth when Product, requirements, or design already decide the matter.
- If a prompt needs upstream ambiguity, name the unresolved authority gap before
  reading fallback context.
- Active specification should stay present-tense; historical comparisons belong
  in comments, design history, tickets, or release notes.
- Missing requirement, design, proof, or traceability is pressure, not success.
- Product and requirement surfaces must provide enough operational lifecycle
  signal for downstream design, or record a named gap. The canonical lifecycle
  chain is: intent -> requirement -> build -> assurance -> release ->
  deployment -> live usage -> observed telemetry -> retirement.
- Downstream design must not fill missing lifecycle truth from implementation
  precedent, prompt prose, local convention, or test fixtures.
- Select one complete immutable STDO version. Mutable source, partial standard
  sets, compressions, and installed mirrors do not create another constitution.
- Identify the exact proof target and its nearest weaker excluded property;
  never substitute packaging, presence, or local green for a stronger claim.
- Keep semantic basis, evidence basis, and state projection distinct.
- Product progress is measured against one bound outcome. Parallel work may
  proceed, but preservation is not progress and regression blocks promotion on
  the affected path.
- Judge proportionality by semantic ambiguity removed versus effective
  reasoning complexity added, not by line or artifact count. Detail is lawful
  when it contracts rival interpretations; duplicate truth and reconciliation
  paths are not.
- Prioritize fast Product feedback under that same relation; this is not a
  global scheduler or fixed execution sequence.

## Compression Use

Use this asset to orient a worker to source precedence, lawful re-entry, and
traceability. Do not use it to decide product-specific behavior; product
behavior must come from the current product authority packet.

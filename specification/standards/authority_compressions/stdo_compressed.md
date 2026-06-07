---
kind: authority_compression_asset
asset_ref: authority-compression://stdo/core/v1
compression_profile: prompt_authority_compact_v1
target_prompt_families:
  - transform
  - evaluate_design_depth
  - evaluate_review_grade
source_refs:
  - ../SPEC_METHOD.md
  - ../DESIGN_MODULE_METHOD.md
  - ../ODD_METHOD.md
  - ../TICKET_METHOD.md
  - ../UX_METHOD.md
source_digests:
  SPEC_METHOD.md: 3bf7f89a1c6528abf5ce17e68b98920270d3add6c77119ea61a4167382165eec
  DESIGN_MODULE_METHOD.md: bac51dd6250c8464f8c63e1037caa982cf41e52e54e0218a63404fde8125071e
  ODD_METHOD.md: e420024069307ec0de189b3e6e401058db063dfdcc8c701fee3088e844f060f4
  TICKET_METHOD.md: 1b190915d2d76ed485b385c722c1221f39e32f72a37b379bd7d35ccafab0e17c
  UX_METHOD.md: e2ca1da558e69917d0ed8787409c6a67a4835e14d6d577af89e9f4eacd79f46e
generated_by: claude
generated_at: 2026-06-07
stale_if_source_digest_changes: true
---

# STDO Compressed Authority

## Governing Claim

Specification is constitutional source. Design and realization are subordinate
implementation surfaces. Code, prompts, tests, generated views, dashboards,
archives, and comments are projections or realization proof, not independent
truth.

## Authority Flow

Use the smallest current authority surface that can decide the question:

`Goals -> Intent -> Product Definition -> Requirements -> Design -> Code -> Events -> Projection -> Delta -> Scenarios -> Gap Analysis -> Repricing`

When a lower layer needs a change in meaning, re-enter at the smallest upstream
layer that owns the missing truth.

## Prime Operating Rules

- Do not create a second truth surface when a current authority surface exists.
- Keep active constitutional surfaces present-tense.
- Treat generated artifacts and summaries as read models unless admitted as
  source truth by the owning method.
- Missing traceability is a defect.
- Prefer one algebraic primitive plus projections over multiple local decision
  systems.
- Method compression is a prompt input, not a replacement for the source method.
- Agentic development conforms by following the constitutional process from
  declared authority, with produced artifacts passing deterministic admission. A
  walkthrough a competent agent using declared authority cannot complete is a
  method defect; agent error is not.

## Prompt-Relevant Rules

- A prompt is rendered contract code over typed authority. It is not source law.
- Prompt text must project current authority refs, obligations, contracts,
  boundaries, proof expectations, and fallback conditions.
- Prompt bodies must not carry historical workaround prose unless the current
  requirement, design, runtime, or test still needs that constraint.
- Raw method documents are fallback inputs when this compressed authority is
  stale, missing, or insufficient for a named unresolved method question.

## Re-Entry Compression

- `goal_reprice`: current work-wave focus changes.
- `intent_reprice`: direction or scope changes.
- `product_reprice`: product shape changes while intent stays stable.
- `requirement_reprice`: constitutional requirement truth changes.
- `design_reframe`: realization structure changes while requirements stay stable.
- `realization_refactor`: local realization changes with no upstream change.

## Proof Compression

Closure requires authority trace, realization proof, negative proof where drift
is plausible, and a present-tense statement of residual open pressure.

---
name: stdo-delegate-review
description: Use when governed STDO work in this repository needs a bounded worker handoff or a required independent review — preserving the governing requirement, design, grant, territory, proof predicates, and return across the handoff, and deriving review expectations from sources before judging a candidate. Not for unrelated tasks.
---

# STDO delegation and independent review

Use this skill when the triage in `stdo-workspace-change` shows that the work
genuinely needs a separate worker, a separate reviewer, or both.

## Delegating a bounded worker (SK-06, Q05)

When you delegate construction (direct or to another actor), the worker must
receive: the governing requirement and design, the exact operation grant and
territory, the applicable proof predicates, and a bounded return definition.

- Preserve these bindings across the actual host handoff; a child does not
  inherit your whole context merely because it is available.
- A child completion does **not** start an unrequested next stage. The Executive
  consumes the child's closed return and then selects the next authorized action.
- Keep these distinct in the record: actor output, transport success, candidate
  availability, assessment, and acceptance. One does not imply the next.

A worker returns the exact candidate, the performed and the not-performed
evaluations, the effects, the residuals, and the invalidators — not a fluent
summary.

## Independent review (SK-07, Q05, Q09)

When a change requires independent review:

1. The reviewer derives expected behavior from the governing sources **before**
   seeing the candidate's own claims.
2. The reviewer then evaluates the exact frozen candidate and its actual-path
   proof.
3. The reviewer reports actual exposure, evidence, severity, and affected claims.
   It does **not** author the adopted repair and does **not** assume acceptance
   authority. A different role label alone does not establish independence.

A required fresh assessment after a material change cannot be replaced by a stale
review result (see [stdo-continuation](../stdo-continuation/SKILL.md) for invalidation).

## Same-model-family limit

A non-author reviewer in the same model family supplies non-author evidence with
a semantic-independence limitation; it does not establish cross-family
independence. State this limit when it applies.

## Method sources (cited, not reproduced)

Within `stdo://releases/v3.0.1-rc.1/standards/`: `EXECUTIVE_BASELINE.md` sections
6, 8 to 10, 12, and 16 to 19 for role configuration and bounded Executive
decisions; `EVALUATION.md` sections 3, 5, and 7 for independent review and
acceptance; `ASSURANCE.md` sections 7 to 9 for actual-path proof.

## Scope and limits

This skill coordinates roles; it does not itself grant effect authority or decide
acceptance. Acceptance and release remain the owner's decisions.

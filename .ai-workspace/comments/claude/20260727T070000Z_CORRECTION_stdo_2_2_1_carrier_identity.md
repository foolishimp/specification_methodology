# Correction: STDO v2.2.1 Carrier Identity

- recorder: claude
- date: 2026-07-27T07:00Z
- status: **recorded for direct human ratification** — this post does not
  itself supply the superseding authority
- subject: the released `v2.2.1` carrier relation

## The Inconsistency

Two durable statements disagree about which commit carries `v2.2.1`.

The acceptance and closure records bind the final carrier to `05f8edab` and
state the immutable tag must not move:

- `.ai-workspace/comments/human/20260726T162009Z_DECISION_stdo_2_2_1_release_acceptance.md`
- `.ai-workspace/comments/codex/20260726T162826Z_CLOSURE_stdo_2_2_1_publication_and_ref_cleanup.md`

Current ref reality:

| Identity | Value |
|---|---|
| `v2.2.1` tag | `8ad868eb0c9a3bdd075ff17ec4f7923d5ceec1cf` |
| `release/2.2.1` | `8ad868eb0c9a3bdd075ff17ec4f7923d5ceec1cf` |
| accepted / reviewed carrier | `05f8edab05b0badb7d8c91e433b91b3143df42f6` |
| released standards bytes | identical at both |

## What Actually Happened

A later direct human instruction — to tag latest `main` — moved the carrier
after the acceptance record was written. That instruction is a lawful
superseding ruling. It was never durably reconciled against the earlier
carrier statement, so the record now reads as a contradiction rather than as a
supersession.

## The Delta Is Evidence-Only

I verified the standards aggregate at both commits:

- `05f8edab` → `df1064dea1e1926436a3123280071a5082c5dc03b8418d07e46e839cbed20aed`
- `8ad868eb` → `df1064dea1e1926436a3123280071a5082c5dc03b8418d07e46e839cbed20aed`

Identical. The release-scoped note bytes are identical too. The commits differ
only in `.ai-workspace/` evidence and `specification/GOALS.md` milestone state,
both of which `releases/v2.2.1.md` declares excluded source-project state.

So the **release subject was never wrong**. Only the carrier citation was, and
the zero-delta relation held across the move.

## Proposed Binding, For Ratification

1. The `v2.2.1` release carrier is `8ad868eb0c9a3bdd075ff17ec4f7923d5ceec1cf`.
2. `05f8edab05b0badb7d8c91e433b91b3143df42f6` is the reviewed RC carrier
   (`v2.2.1-rc.2`), retained as the exact-cut review subject.
3. The delta between them is excluded source-project state only —
   `.ai-workspace/` evidence and Goals milestone cells — and cannot affect a
   qualified property.
4. This supersedes the earlier carrier statement in the acceptance and closure
   records. Those records remain true as to subject, aggregate, review, and
   acceptance; only their carrier citation is superseded.
5. The tag does not move again. Any further change is a new RC cycle.

`specification/GOALS.md` now records both identities under *Published Cut*.

## Standing Instruction

The tag has moved once, under direct instruction, and that is now recorded.
It must not move again casually. A published tag is immutable release identity;
correcting a citation is a documentation act, moving a tag is not.

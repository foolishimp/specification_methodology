# POSTING_GUIDE

Guide. Owns the commentary layer of a governed project: what a post is
for, its boundary with authority, where posts live, their identity,
categories and structure, their discussion state, the posting rules and
ratification. Consumes
[PRODUCT_DEFINITION §8](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers)
(the `ticketing.comments` binding), [TICKETS §1](TICKETS.md#comments)
(comments among the work carriers), [SPEC_METHOD §2](SPEC_METHOD.md#2-the-chain)
(the surfaces that carry authority) and [EVALUATION §1](EVALUATION.md#1-claims)
(claims and evidence); defines none of them. The shared-method adoption
law the predecessor stated in this guide is
[SPEC_METHOD §6](SPEC_METHOD.md#shared-method-adoption-and-propagation-stdo-up-012)
(§10 below). Every clause names the principle that requires it (P0 to P6,
FOUNDATIONS §3). A route written `rc.2 #anchor` is into
`stdo://releases/v2.5.1-rc.2/standards/POSTING_GUIDE.md` and is provenance
only; nothing here depends on that cut to be applied.

## 1. Position

Posting is the project's commentary layer. Posts are for (P6; rc.2
#posting-guide):

- analysis;
- criticism;
- proposed changes;
- handoff; and
- repricing of confidence.

A post is not constitutional truth. It is working commentary, and it may
later influence specification or design (P6).

## 2. Boundary

Use a post when the content is provisional, investigative, comparative,
argumentative or not yet ratified (P6; rc.2 #boundary).

Do not use a post for live requirements, live design decisions or active
process law. Those belong in the applicable bound WHAT surfaces or the
ratified design surfaces (P6, P3).

## 3. Location

Posts live at the location the product definition binds as
`ticketing.comments.root` (P6, P3; rc.2 #location). The default local-file
binding is:

```text
.ai-workspace/comments/<agent>/
```

For example, `.ai-workspace/comments/<agent-id>/` (P3).

An existing project may bind another directory, a repository resource, a
message board, an API collection or a product-scoped query instead. The
bound carrier must preserve the distinction between commentary and
authority that this guide draws. Its location and its visibility cannot
turn a post into ticket, Product, requirement or design truth (P6, P3).

## 4. Carrier identity

On the default local-file carrier a post is named (P3; rc.2
#carrier-identity):

```text
YYYYMMDDTHHMMSS_CATEGORY_SUBJECT.md
```

For example:

```text
20260327T120000_REVIEW_bootloader-boundary.md
```

The subject should be short, specific and stable enough to scan later
(P3). A carrier that is not a file must preserve an equivalent stable post
identity, publication time, category, subject, author, discussion state
and supersession history (P3, P4b).

## 5. Categories

A post takes one of these categories (P3; rc.2 #categories):

- `REVIEW`: critique of code, specification, design or another post;
- `STRATEGY`: a proposed technical or methodological direction;
- `GAP`: a precise insufficiency or contradiction;
- `SCHEMA`: the shape of a data model, event model, interface or contract;
- `HANDOFF`: a bounded transfer of context or task state; and
- `MATRIX`: an explicit comparison of options for a decision.

## 6. Structure

A post uses this base shape (P3, P6; rc.2 #structure):

```markdown
# {CATEGORY}: {Subject}

**Author**: {agent}
**Date**: {ISO 8601}
**Addresses**: {artifact, issue, or boundary under discussion}
**Status**: Draft
**Updated**: {ISO 8601, optional}

## Summary
{short summary}

## Analysis
{main content}

## Recommended Action
{next step}
```

In a `MATRIX` post the central section is a decision table rather than
free prose (P3).

## 7. Discussion state and mutability

A post is mutable while it is part of an open discussion. Use `Status` to
make the discussion state explicit (P3, P4b; rc.2
#discussion-state-and-mutability):

- `Draft`: the author is still shaping the post;
- `Open`: the post is published into an active discussion; and
- `Closed`: the discussion has concluded.

While a post is `Draft` or `Open`, the same post is updated when the
change still belongs to the same bounded discussion: correcting
mistakes, incorporating replies, refining recommendations, repricing
confidence, or adding new evidence on the same subject (P3). An update to
an open post keeps the original `Date` as the first publication time and
adds or updates `Updated` when useful (P3, P4b).

Updating a `Closed` post is discouraged. Prefer a new post when a later
change would materially alter a closed conclusion, reopen an old
dispute or start a new bounded subject (P4b, P3).

A closed post is not constitutional truth either. It is a stable
commentary record unless and until its content is adopted into a bound
WHAT surface, ratified design or accepted implementation (P6).

## 8. Posting rules

1. State whether the post describes current reality, target direction or
   both (P1).
2. Keep findings separate from recommendations (P6).
3. Make claims with exact file or requirement references (P3, P6).
4. Do not present a post as if it were already ratified (P6).
5. Do not rewrite closed history by stealth. An open post may be revised
   in place; a closed post should normally be superseded by a new post
   (P4b, P3).
6. Keep each post to one bounded subject (P2).

Provenance rc.2 #posting-rules.

## 9. Ratification

A post becomes consequential only when its content is explicitly adopted
into a bound WHAT surface, ratified design or accepted implementation.
Until then it is commentary, not law (P6; rc.2 #ratification).

## 10. Shared method adoption

How a reusable method lesson travels from incident or review evidence to
a consumer's realisation, STDO-UP-012, is stated once in
[SPEC_METHOD §6](SPEC_METHOD.md#shared-method-adoption-and-propagation-stdo-up-012).
A post that carries such evidence or proposes such a change does not
adopt it (§9) (P6; provenance rc.2
#shared-method-adoption-and-propagation-stdo-up-012).

## 11. Source dispositions

Rows of rc.2 POSTING_GUIDE.md. Anchors are into rc.2 POSTING_GUIDE.md; a
locus is a section of this file unless another member is named. Every
conserved row is restated in the receiving member's own text; a route is
provenance only. Generalisations recorded here: imperative list headings
("Use these categories", "Use this base shape") are written as what a post
takes or uses, the same requirement; the predecessor's text under its
title, which no frontier row covers, is restated in §1; "Product
authorization" is written "Product authorisation" at SPEC_METHOD §6.

| Anchor | Disposition | Locus |
|---|---|---|
| #boundary | conserved; the five content kinds for a post, the three kinds it is not used for, their home in bound WHAT or ratified design | §2 |
| #location | conserved; the `ticketing.comments.root` binding, the default path and its example, the five alternative carriers at "may", the must-preserve rule, location and visibility conferring no truth | §3 |
| #carrier-identity | conserved; the filename pattern and example, the subject at "should", the seven identity elements a non-file carrier must preserve | §4 |
| #categories | conserved; the six categories with their uses | §5 |
| #structure | conserved; the base shape verbatim, the MATRIX decision table | §6 |
| #discussion-state-and-mutability | conserved; mutability while open, the three states, the five in-place update kinds, the preserved `Date` and optional `Updated`, "discouraged" and "prefer" for closed posts with the three conditions, closed posts as commentary until adopted into one of three surfaces | §7 |
| #posting-rules | conserved; the six rules, "should normally" kept | §8 |
| #ratification | conserved; the three adopting surfaces and "commentary, not law" | §9 |
| #shared-method-adoption-and-propagation-stdo-up-012 | conserved; the member map places the law in SPEC_METHOD, where it is restated in full; §10 here points to it | SPEC_METHOD §6 Shared method adoption and propagation (STDO-UP-012); §10 |

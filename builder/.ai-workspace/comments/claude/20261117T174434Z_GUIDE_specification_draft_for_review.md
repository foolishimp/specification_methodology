# Guide to the specification draft

**Type:** GUIDE. Commentary for the product owner's review, not law.
**Author:** claude (Fable 5.2) · 18 November 2026
**Subject:** `builder/specification/` at commit `143312863`.
**Superseded** by `20261118T040741Z_GUIDE_specification_round_two.md`.

## What happened while the owner was away

1. I drafted the full requirement set: 62 requirements and 6 scenarios.
2. One independent reviewer (Claude Opus 5.5, a fresh agent that wrote none of
   it) tested the draft against the approved intent and the owner's own quoted
   words. Its verdict was **No, not fit to put in front of the owner**: 31
   findings, 9 of them against a guard rail or the owner's words. The review is
   at `builder/.ai-workspace/comments/opus/20261118_REVIEW_specification_draft.md`.
3. I reworked the draft: 48 requirements and 7 scenarios now.
4. The review also found faults in the product page. Those changes are in one
   separate commit, `143312863`, so they can be accepted or undone as a unit.

Nothing was accepted on the owner's behalf. The intent is unchanged. The rework
has not itself been independently reviewed.

## What there is to read

| Page | Words | State |
|---|---|---|
| `INTENT.md` | 395 | Approved by the owner |
| `PRODUCT.md` | 633 | Changed after the review; see the next section |
| `GOALS.md` | 113 | Draft |
| `REFERENCE_FRAME_BASIS.md` | 315 | Draft |
| `requirements/`, 12 families | 4,251 | Draft, marked deferred until accepted |
| `requirements/SCENARIOS.md` | 620 | Draft |

## Changes to the product page, for the owner to accept or undo

| Change | Why |
|---|---|
| It no longer says the product "is the runtime" of the method's outcome-driven development standard | That sentence tied the product to every clause of the standard that names ABG, including its ledger rules |
| It takes only the graph terms of that standard's section 5; the guard rails govern the rest | The same |
| It defines check, request and run | The requirements depend on them and they were undefined |
| "Change" covers any asset, not only the specification | The owner's words: "i can enter at any node" |
| "Asset" drops the word "typed" | Nothing uses it |

## Decisions that are the owner's

For each I drafted a default so the set reads whole. Each default is mine.

1. **What ties a decision, and a built asset, to the exact content it rests
   on.** Without this, an acceptance survives a later edit of what was
   accepted, and the framework cannot tell what changed. The reviewer names two
   ways only: a fingerprint of the content, or the workspace's own git history.
   Drafted: BUILD-008 and CHANGE-002 say "exactly" and name no way. LOG-003
   bars the event log from holding a fingerprint.
2. **Who judges that the design and the code mean what was asked.** After the
   requirements, the first draft left that to tests the agent writes. Drafted
   in METHOD-004: tests are written from the accepted requirements before the
   code, and the user accepts the built product at the end.
3. **May an agent's judgement choose between routes the graph allows.** Drafted:
   no. The graph's declared order decides.
4. **What "The agent takes no step the graph does not allow" covers.** The agent
   can still edit any file during its step. Drafted in CHANGE-004: such an edit
   is treated as a change, so an accepted asset it touched must be accepted
   again.
5. **Git.** Drafted in BUILD-010: the workspace is under git and the framework
   never reverts or resets it. Not drafted: whether the framework ever commits.
6. **Ticketing.** Drafted in METHOD-002: the user's request is a file in the
   workspace that the first vector reads.
7. **What set-up writes into a governed product's agent instruction files.**
   The method writes a standard block there, which tells an agent how to work.
   Guard rail 7 says the framework has no opinion on that. Drafted: nothing.
8. **Smaller ones.** Setting up over an existing system has no scenario. A run
   repeated with a second LLM agent has no scenario. A rail on size or cost is
   not written, because it needs a number.

## What I did with the review

| Rank | Findings | Done |
|---|---|---|
| 1. Against a guard rail or the owner's words | 9 | 3 fixed in the text, one of them by the product-page change; 6 rest on decisions 1 to 4 and 7 above, each with a drafted default |
| 2. One requirement against another | 11 | 9 fixed; 2 rest on decisions 1 and 6 |
| 3. Acceptance that could not be checked | 4 | 4 fixed |
| 4. Gaps | 7 | 6 filled; 1 is in decision 8 |

Fourteen requirements that restated others were removed, the guard-rails family
among them. `requirements/README.md` now has a table of which requirements keep
each rail.

## Where the four features are

| Feature | File |
|---|---|
| GTL, the graph language | `requirements/GRAPH-LANGUAGE.md` |
| The registry | `requirements/REGISTRY.md` |
| HoG, higher-order graph functions | `requirements/HIGHER-ORDER.md` |
| The event log | `requirements/EVENT-LOG.md` |

Their shapes are left open on purpose: which arrangements, which registry
fields. Goal 2 decides those when each loan is examined.

## Limits

- I wrote all of it in one sitting, and I am the same model family as the
  agent that approved the 5.0 plan in July. The reviewer is the same vendor.
- The requirements file is still about thirteen times the length of the
  intent.
- No loan is decided. I read the earlier code only for its public names.

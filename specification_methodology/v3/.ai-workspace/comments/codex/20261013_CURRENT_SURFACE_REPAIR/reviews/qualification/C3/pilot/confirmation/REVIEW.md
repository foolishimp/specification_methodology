# Confirmation review: frozen `721344b` first cone against supplied RC2 `STDO-UP-020`

**Basis:** I used only the RC2 text and candidate text you supplied, with no tools. I did not check these bytes against commit `721344b`. The decision owner should tie this result to the commit's actual bytes. I took the original review and the Writer's repair as separate evidence, and judged each fix against the source.

## Semantic result: **indeterminate**

F2 through F9 are resolved on this cone. One part of F1 is still not entailed by the candidate. The text can be read faithfully, but it can also be read the wrong way round, so satisfaction is not yet supported. I found no contradiction with the source, so the result is not falsified.

## Remaining source-linked concern

**F1, partly resolved.** TL § Recovery law: "Churn is an instance of rejected or superseded construction."
- **Fixed:** the false definition is gone. The prohibition on repeating an unchanged failed relation is now separate. The neighbouring progress categories are carried in full.
- **Still open:** RC2 says "Rejected or superseded construction is churn": rejected or superseded construction implies churn. Read literally, the candidate states the reverse: churn is a kind of rejected or superseded construction.
- **Effect:** the original counterexample is still undecided. A construction rejected on its first attempt is churn under RC2, but the candidate neither says it is nor says it isn't. The next sentence ("not the definition of all churn") points toward the faithful reading but does not establish it.
- **Assessor-disposition evidence (not a decision):** `local_repair`. Restate the sentence as "Rejected or superseded construction is churn."

## Resolved

| Finding | Where | Note |
|---|---|---|
| **F2** | TL Evaluate, TL Dispose, WR 5 | Fixed by option (a): the assessor-disposition classification is kept as evidence, and the decision stays with the owner. The full RC2 condition table is in Dispose. Two small wording points, neither blocking: (i) "If a protocol carries…" and "any assessor-disposition evidence" make the classification optional, while RC2 says assessment "returns" one; (ii) the reject description in Evaluate leaves out "violates a governing relation", which Dispose does include. |
| **F3** | WR closing paragraphs, TL | Carries the discard justification and the preservation-checkpoint identifiers, and states it is no promotion, acceptance or publication. Wording residual, not blocking: FOUNDATIONS still says "Restart is another iteration…", which clashes with RC2's meaning of restart. |
| **F4** | WR 5 | Every R7 transition-evidence field is now present, including authority paths added or removed. |
| **F5** | WR recovery | Frame altitude and shared components added. Authority is covered by the pre-retry triangulation. |
| **F6** | WR | A seam is included by default, and unrelated incompleteness is repricing input. |
| **F7** | TL, WR | Focused proof comes first, whole-candidate qualification sits at the boundary, and recovery proof destroys or excludes incidental state and compares outcomes. |
| **F8** | WR 1 | Adds transformation admission, computational and common-library dispositions, and re-entry conditions. |
| **F9** | WR 7 | The Executive is now conditional on coordination need, direct Writer entry is stated, and status changes need no new grant. RC2's "record actual role transitions in the existing work carrier" is not carried. That is minor and not blocking. |

F10 is still out of frame.

## Interrupted document (`CLAUSE.md`)

Checked against the supplied text only:
- **Earlier clause kept:** "A judgment is evidence, not an operation grant." is unchanged and stays first, under `# Current clause`.
- **Uncertain-effect handling added:** the paragraph that follows matches the independently proposed paragraph word for word. That covers observe, reconcile or return unresolved; no assumed idempotence; a failed transport is not proof that nothing happened; the three conditions for repeating; returning an unresolved effect with its operation, subject and last observation; and compensation needing its own grant.
- **Nothing extra:** no other content was added.
- **Not checked:** I could not confirm that the original clause matches the pre-interruption bytes, or that the write was not partial, without access to the repo.

## Not done

I did not accept, repair or select a next action. Those belong to the decision owner.

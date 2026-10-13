# Common workspace/context review record

Subject: `bb76b1d`. Independent Claude CLI review; no candidate authorship. The report below is a bounded defect review, not owner acceptance. Writer disposition: F1 and F3–F9 repaired; F2 resolves construction authority from the explicit owner completion instruction while acceptance-review policy remains open. The common correction receives a successor input snapshot.

# Independent source review: common construction input at `bb76b1d` (changes after `47ef3e8`)

**Reviewer:** Claude, in a fresh review context. I did not author this subject; the common pen (Codex) did. I made no edits and used no tools.

**Basis:** only the supplied sources and diff:
- `specification/PRODUCT.md`
- `specification/requirements/README.md`
- `specification/conformance/README.md`
- `.ai-workspace/tickets/active/T-002-CODEX-c3-successor-construction.md`
- the diff across GOALS, INTENT, PRODUCT, conformance and requirements

**Not read, so not verified:** T-002, `REFERENCE_FRAME_BASIS.md`, PREDECESSOR_CLAIMS, the recorded snapshot commit, the contract digest and the installed rc.2 baseline. Any finding that depends on them is marked.

## Bounded disposition

**Changes required (bounded).** The core correction is sound:
- The workspace is treated as the continuing truth surface and context as a disposable account.
- There is no universal replay, reset or idempotence obligation.
- The stale-summary discriminator is added.

The supporting records have four material defects:
- Two of them overclaim owner sign-off or actor naming.
- One weakens the successor-locus test this correction was meant to fix.
- One leaves "workspace reality" unbounded against the admitted basis.

None of the four requires re-entry above Product. All are local wording or record repairs by the common pen.

## Answers to the four questions

| Question | Verdict |
|---|---|
| Current reality vs governing authority | **Partly.** Reality is separated from belief. Reality is not separated from the *admitted basis*. See F4. |
| No universal history replay or idempotence | **Yes.** `requirements/README.md › Bounded Transitions And Reference Frames` item 5 keeps "no universal reset or complete-history replay obligation". It adds no idempotence requirement. Uncertain external effects are protected by the new conformance row ("does not … prove an uncertain external effect absent"). The INTENT sentence "discarded and rebuilt against current reality" implies no replay. |
| Disposition locus and route fixed truthfully | **Partly.** The C3 Outcome now matches acceptance criteria 1 and 3. However, the definition that pinned the locus to the candidate's own text was removed (F3). Some README and ticket records are stale (F7, F8). |
| Records construction without claiming checkpoint or release acceptance | **Mostly.** No C3, merge or release acceptance is claimed, and GOALS says so explicitly. Two edits do imply owner sign-off or actor naming that the owner's instruction does not supply (F1, F2). One review claim now covers text that has changed since (F5). |

## Material findings

### F1. Owner sign-off of GOAL-002 and the specification revision is implied without a record

**Where:** `GOALS.md` › GOAL-002 paragraph, the C3 row, and the closing snapshot paragraph.

**What changed:** The diff removes three things:
- "(wording pending the product owner's sign-off)" from GOAL-002;
- "its wording is pending the product owner's sign-off of the specification revision" from the C3 row;
- the gate "recorded in T-002 after the product owner signs off the repaired specification at an exact commit".

**Counterexample:** The owner's direction authorises *running* the Codex rebuild to completion for later review. It is not sign-off of the GOAL-002 wording or of the repaired common specification. A reader of the new GOALS would conclude that both were signed off. The Categorical-direction row in the same table still says "sign-off remains open", which contradicts that reading.

**Bounded fix:**
- Restore the pending-sign-off markers.
- State that the Codex run proceeds under the owner's run-to-completion instruction on a common basis that is not yet signed off.
- State that owner review will cover both the common basis and the candidate.

### F2. PRODUCT's own admission gate contradicts the admitted contract

**Where:** `PRODUCT.md › Open Owner Decisions`, first bullet. Compare T-002-CODEX › Actors and › Rebuild Activation.

**The conflict:**
- PRODUCT still says the owner names the Executive and Reviewer in the tenant tickets, and "Until then every execution contract stays `drafted`".
- The ticket admits EC-CODEX-SYN-01.
- The ticket binds the Executive only by inference ("this Codex session … under Jim's run-to-completion instruction").
- The Reviewer row reads "construction review; owner policy decision remains open". That is not an owner naming.

**Counterexample:** Under the common text as it stands, the admission is invalid. Either the owner named the actors and PRODUCT is stale, or the admission went beyond the grant.

**Bounded fix:** Do one of the following:
- record the owner's naming, with a quote and date, and update Open Owner Decisions; or
- amend the ticket to say that the Executive binding is inferred from the run instruction and is pending owner confirmation, and that Reviewer naming remains open.

In either case, do not use any Reviewer result for an `accept` disposition until Reviewer naming is resolved.

### F3. "Resolving successor locus" no longer excludes a route back to the predecessor

**Where:** `PRODUCT.md › C3 Construction Contract › Outcome`, second bullet, together with acceptance criterion 1.

**What changed:** The old wording defined the locus as "the section of the candidate where the claim now lives". The new wording says only "resolving". `stdo://releases/v2.5.1-rc.2/…#rf-001` resolves through the installed toolchain.

**Counterexample:** A `conserved` row whose locus is a predecessor anchor now passes criterion 1 literally. This is exactly the first-pass defect recorded in T-002-CODEX › Tenant Re-Entry ("treated a route to the predecessor as conservation"). Criterion 2 and `requirements/README.md › Standalone Successor Requirement` still catch it. However, the first-line check has been weakened.

**Other wording issue:** "bounded reason or owner decision" reads as two alternatives. For `intentionally removed`, criterion 3 requires *both* the owner's decision and a reason. The bullet also omits the accepted successor relation that `superseded` requires.

**Bounded fix:** Reword the bullet as follows: "…a successor locus in the candidate's own text for each conserved or superseded claim; the accepted successor relation for each superseded claim; the owner's decision and reason for each intentionally removed claim; and a bounded reason for each not applicable claim."

### F4. "Workspace" is undefined against the admitted basis, snapshot and drift locks

**Where:** `PRODUCT.md › Construction And Context Management`, first paragraph ("The workspace is the continuing truth surface…"; "A stored belief or successful prior result cannot overrule contrary current evidence"). Also `requirements/README.md › Bounded Transitions And Reference Frames` item 5.

**The rules it must sit with:** `PRODUCT.md › Development Isolation` says:
- inputs are read from the snapshot commit with `git show`, "never from a working tree";
- reviews read "at a named commit, never its working tree";
- a file absent from a sparse cone is not evidence of absence.

`C3 Construction Contract` invokes drift locks that "keep the outcome and basis fixed".

**Counterexamples:**
1. `main` advances after the Codex snapshot. A Writer treats current `main` as "contrary current evidence" and silently builds against it. The basis has been rebound without re-entry.
2. A fresh actor in a sparse tenant worktree observes that a common file is absent. Read naively, the "truth surface" turns this into a claim that the file does not exist.
3. A Reviewer reads the tenant working tree because it is "current reality" rather than the frozen commit.

**Why it matters for the authority question:** Reality says *what the state is*. The admitted basis and the ticket say *which state is the subject* and *what may be done*. The correction states the first and is silent on the second.

**Bounded fix:** Add one sentence to item 5, with PRODUCT pointing to it: "The workspace comprises the repository lineage, its committed states and worktrees, and declared external systems. An activation observes the subject and basis its contract binds. Contrary current evidence reopens the affected claims and follows drift and re-entry rules; it does not rebind the basis or confer authority."

**Unverified dependency:** Separately confirm whether the snapshot recorded in T-002 is at or after `bb76b1d`. If it predates this correction, the Codex run's basis lacks the text under review, and a drift decision must be recorded.

## Lesser findings

### F5. A stale review claim now covers changed text (moderate)

**Where:** `GOALS.md`, Categorical direction row.

**Problem:** The row still cites the `be78414` frozen review as "no further changes required". The context-management text it describes has changed since then, through `bb76b1d`. Under the correction's own principle, a prior successful result must not stand for the current state.

**Fix:** Note that commits after `be78414`, through `bb76b1d`, are under independent review, and that sign-off is open.

### F6. The generic tenant start gate was dropped (moderate)

**Where:** `GOALS.md`, final paragraph above Open Owner Decisions.

**Problem:** The removed sentence ("Tenant C3 work starts from that snapshot and its admitted execution contract, under Development Isolation") governed *both* tenants. The replacement covers only Codex. The Claude line's start condition is now stated nowhere in GOALS.

**Fix:** Restore the general rule alongside the Codex-specific record.

### F7. The README index still implies a locus on every row (minor)

**Where:** `requirements/README.md` index entry for PREDECESSOR_CLAIMS.

**Problem:** It still says "one row per predecessor claim giving its disposition and successor locus". This conflicts with the corrected Outcome bullet.

**Fix:** Change it to "and, where required, its successor locus".

### F8. Ticket record hygiene (minor)

**Where:** T-002-CODEX.

- **EC-CODEX-001:** The heading says "(superseded draft)" but the `state:` line still reads `drafted`. Set it to `superseded`.
- **Milestones:** M1 still names EC-CODEX-001. Retarget it to EC-CODEX-SYN-01 or the design-reframe milestone.
- **Execution Record:** The admission entry sits under Rebuild Activation rather than Execution Record. The only Execution Record entry still says "nothing admitted". The admission should be in the record section, with a statement of the bytes the digest covers.
- **Role changes:** `PRODUCT.md › C3 Construction Contract › Executive loop` requires "the pen records the change before the effect" when the same actor changes role. The ticket says only that the Executive "switches out". Per-effect role-change entries should be visible. I could not verify whether they exist.

### F9. Two loci with slightly different strength (minor)

**The two statements:**
- PRODUCT: a prior result "cannot overrule contrary current evidence".
- README item 5: acquisition "reconciles material disagreement".

**Problem:** These state the same determination at different strengths. "Contrary current evidence" also needs an admissibility qualifier. A misbound or unauthenticated current judgement should *reopen* a prior closed result, not overrule it. This follows the conformance rows on misbound judgements.

**Fix:** Make PRODUCT descriptive, with item 5 as the owner. In item 5, say "admissible contrary evidence reopens the affected claim".

**Related:** "the actor's account" in the PRODUCT paragraph is singular. In multi-actor configurations it should read "each actor's account".

## What holds

These points hold and need no change:
- The separation of workspace from context, and the rule that discarding context does not reset the workspace.
- No universal replay or reset obligation, and no idempotence requirement.
- Unknown external effects are not presumed absent.
- Closed results allow bounded handoff, with their validity and independence conditions retained.
- The new conformance row for a fresh actor with a stale summary.
- The GOALS statement that construction evidence closes no owner review and authorises no merge or release.
- The ticket's statement that internal `candidate_ready` does not mean C3 is accepted.
- The ticket's retention of the ported-part review policy and the final checkpoint for the owner.

# Prompt: STDO v3 iteration 4, staged plan for both agents

Issued by the product owner. Read all of it before acting. You are one of
two agents. Act only as your party.

- **Codex** holds the pen on the common specification and builds the
  Codex tenant.
- **Claude** reviews the common specification at frozen commits and
  builds the Claude tenant.

The product owner's allocation, in the owner's words: Codex does the
v3/specification i4 update; once ratified, each build tenant borrows
from the other in keeping with v3 i4 to synthesise its new best effort;
the owner then evaluates between the two and takes one as the new v3
basis. There is one session per family, and no session numbers:

| Party | Does |
|---|---|
| the product owner | every decision D1 to D9, the Stage 1 sign-off, the Stage 4 choice |
| Codex, one session in the Codex tenant | holds the pen; builds the Codex candidate; reviews the Claude candidate cross-family; uses its native reviewer as its same-family nonauthor |
| Claude, one session in the Claude tenant | builds the Claude candidate; reviews the frozen specification and the Codex candidate; uses one Sonnet subagent as its same-family nonauthor, under D8 |

Iteration 4 is the last iteration. It ends with the product owner
choosing one candidate. Nothing in it is a rebuild: it is repair, port
and evidence on a specification that decides what the tenants have so
far assumed.

Revision 4. Revision 2 took the six corrections of Codex's review of
revision 1 at commit `0045cb0`: divergences are classified before any common
decision; a port does not erase authorship; a repair review covers the
changed material and its dependents; criterion 4 does not qualify the
other candidate; a freeze is immutable and authority lives in the
ticket; the Codex donor package is `d490dd6`. Revision 3 takes the three
edits of Codex's review of revision 2 at `e78afaf`: a missing assessment
blocks eligibility but is not a falsification; a repaired port is read
back by a nonauthor at the final freeze; a common decision carries
through as a tenant task or a recorded reason that none is needed.
Revision 4 records the product owner's allocation: one Codex session
and one Claude session, each within its tenant, Codex holding the pen.

## Terms

- The **common specification** is
  `specification_methodology/v3/specification/` on `main`. It states
  WHAT the product is. Only the pen holder edits it, and every change to
  it lands on `main` as a pen commit. Today it stands at `1fce537`.
- A **tenant** is one line of realization under
  `specification_methodology/v3/build_tenants/<agent>/`, on its own
  branch. It states HOW. Each agent edits only its own tenant.
- The **pen** is the sole right to edit the common specification, the
  tickets, `build_tenants/README.md`, `CLAUDE.md` and `AGENTS.md`. It is
  held by one named session, D1, not by a family. The other agent sends
  common defects to the pen through posts, and writes no common files.
- The **ticket** is the authority record: owner decisions, dispositions,
  admissions and sign-offs. The pen writes it. A tenant **ledger** is
  that tenant's record of work, results, variances and proposals. A
  ledger proposes; a ticket decides.
- A **freeze** is a named commit and is immutable. A repair never changes
  a freeze; it creates a successor freeze, and the ticket names the
  current one.
- A **candidate** is a tenant's frozen build for one iteration.
- The **donor** of a tenant is the other tenant's named candidate. A
  **port** is a part taken from the donor into the receiving tenant.
- **Expectations** are what a reviewer writes and commits before opening
  the subject: what it will read, and what it expects to find.
- A **same-family nonauthor** reviewer is of the same model family as
  the author and did not write the subject. A **cross-family** reviewer
  is of the other family. In iteration 4 both are interested parties,
  since each family builds a competing candidate, and every review must
  say so.
- An **acceptance-bearing** review is one whose result may support an
  acceptance claim for the part it covers. A **supplementary** review is
  evidence that may not. Which is which is fixed by D4 and Stage 3.
- The **six acceptance criteria**, the **52 member-conformance
  discriminators** and the **closure checks J53 to J55** are those of
  the common specification. Supported inapplicability waives none of
  the six criteria.
- The **product owner** is the human. Owner acts are **gates**: no agent
  proceeds past a gate until the pen has recorded the owner's act in the
  ticket.

## Decisions by the product owner

These are fixed before this prompt is issued. The pen copies them into
the iteration 4 ticket. Neither agent changes them. Items in square
brackets are for the product owner to fill in or confirm.

| # | Decision | Value |
|---|---|---|
| D1 | Pen holder for iteration 4 | The one Codex session working in the Codex tenant. Recorded in the ticket. No other session, of either family, has the pen |
| D2 | Donor commits | Claude: `2beed8d` on `tenant/claude/c3-synthesis`, handoff `96ccdcc`. Codex: `fb855df` on `tenant/codex/c3-iteration-3`, which binds package `d490dd6` |
| D3 | Port lists | Into Claude from Codex: C1 to C6. Into Codex from Claude: X1 to X9. As listed in `comments/claude/20261015T021914Z_REVIEW_I3_CANDIDATES_BEST_OF_BOTH.md`, with no edits by the product owner |
| D4 | Ported-part policy | A ported part is the receiving tenant's text: the receiver rebinds it to its own anchors and re-evidences it with its own tooling. Porting does not erase authorship. The acceptance-bearing review of a ported part is the receiver's same-family nonauthor review of Stage 2, which did not write the part. The donor's cross-family reading of its own ported part in Stage 3 is supplementary. The receiver's ledger records each port by donor commit and locus, and its handoff names, per port, which review bears. A port that a later repair changes, or whose evidence a repair invalidates, is read back by the receiver's same-family nonauthor on the successor freeze, Stage 3 step 4 |
| D5 | Criterion 4, actual use, for the Claude line | Open. The product owner chooses A or B no later than the Stage 1 sign-off, and the pen records it in the ticket. A: fund one isolated-actor protocol run on the Claude candidate, port C2, with the same protocol and caps as Codex's. B: leave unevidenced. B removes the Claude candidate from the Stage 4 choice. It qualifies nothing: the Codex candidate must still meet the six criteria and the closure checks on its own |
| D6 | Choice rule for Stage 4 | A candidate is eligible only if it meets all six criteria and the closure checks J53 to J55. An unassessed required obligation blocks eligibility and is recorded as missing; it does not by itself establish falsification, and it is not a residual. Among eligible candidates, the one with the fewest non-blocking residuals over comparable coverage. If equal, the product owner's preference on readability and maintainability, recorded with a reason. If none is eligible, no choice: the product owner decides between an iteration 5 and stopping |
| D7 | Common input | The signed iteration 4 commit of the common specification on `main`, the Stage 1 gate. Both tenants rebind to it. No tenant is admitted to Stage 2 before it |
| D8 | Budget rule, Claude line | Sequential work in the main session. At most one subagent at a time, Sonnet, with an exact file and line scope. Never parallel agents. Never a message to a finished agent |
| D9 | Standing rules, both | No merge to main by a tenant, no push, no acceptance claim by any agent. Reviews are posted under `.ai-workspace/comments/<agent>/`, expectations first, with no repair of the subject. Writing: plain, every term defined at first use, "the product owner" for the human, exact modal force |

## Stage 1: the iteration 4 common specification

Goal: the common specification decides what the tenants have been
assuming, and nothing else. Gate: the product owner signs off a named
commit on `main`.

The two iteration 3 candidates were built on different common inputs:
Claude on `355aa86`, Codex on `1fce537`. Some divergences are therefore
one line's distance from the current input, not a gap in it. Every
divergence is classified before any common text is written.

Classes:

- **implementation defect**: one line fails the common specification at
  `1fce537`. It goes to that line's Stage 2 repair list. No common text.
- **permitted design choice**: both resolutions are admissible under
  `1fce537`. Recorded as such. No common text.
- **specification gap**: `1fce537` does not decide it, and two correct
  builds would differ in what the product owner accepts. Common text.
- **reserved owner decision**: the specification reserves it to the
  product owner. Decided by the owner, recorded by the pen, carried in
  common text where it binds every tenant.

Steps:

1. **Claude** posts the divergence list under `comments/claude/`: each
   point where the two candidates resolved the same question
   differently, with the loci in both candidates, the clause of
   `1fce537` that bears on it, and a proposed class. The starting list
   is below. Claude writes no common files.
2. **Codex** reviews the Claude candidate `2beed8d`, entered through its
   handoff `96ccdcc`, expectations first, and posts under
   `comments/codex/`. Scope: the 52 discriminators and J53 to J55 over
   `build_tenants/claude/design/REDUCTION.md` sections 3 and 4; a
   re-review of the step 7 repairs and the three fidelity repairs; the
   EXECUTIVE_BASELINE, DESIGN_MODULE and ODD family tables, which no
   working check examined. No repair. Standing: cross-family, interested
   party.
3. **Codex**, as the pen, confirms or reclassifies each item of the
   divergence list with a reason, then revises the common specification
   as a requirement reprice: the smallest change that decides every gap
   and carries every owner decision with exact modal force, ratifies the
   convergences, carries the seven owner decision groups of the Claude
   handoff (`build_tenants/claude/qualification/C3-ITER3/HANDOFF.md`),
   and answers those of findings CX-03 to CX-09 that are gaps. The
   revision names the evidence every candidate owes in Stage 2. Codex
   commits it on `main`, freezes it under the name `C3-I4-01`, records
   the commit in the ticket, and posts the freeze.
4. **Claude** reviews the frozen commit, expectations first: every gap
   decided, every classification sound, no new ambiguity, the owed
   evidence named. Posts under `comments/claude/`. Codex repairs as a
   successor commit on `main` and re-freezes. Repeat until Claude
   reports no blocking defect, or the product owner overrules.
5. **The product owner** signs off. The pen records the commit hash and
   the word "signed" in the ticket. Gate.

### Divergence list, starting version

Classes are proposed by Claude and confirmed or reclassified by the pen
in step 3.

| # | Divergence | Proposed class |
|---|---|---|
| 1 | **Conserved versus superseded.** Same 691 rows, same criterion, 68 replacements in Codex and 15 in Claude. The test for "changed meaning" is not operational | Gap: the test. Owner decision: each row's acceptance |
| 2 | **Authority compressions.** Codex keeps them as pinned read models; Claude proposes superseding them by projection | Owner decision: are they in the successor's scope |
| 3 | **Modal force.** Codex keeps "must" and "shall"; Claude writes them in the indicative | Gap: what conserves modal force, and whether a conversion is a replacement. Owner decision on the Claude line's FR-02 |
| 4 | **Result algebra.** Codex adds performance and effect-observation coordinates; Claude has five core values and no value for an evaluation that was not performed | Permitted design choice. `1fce537` already requires that a not-performed evaluation stays distinct from an undecidable one (`requirements/README.md`, line 143) and that a member's own values map to the core with a declared predicate (`conformance/README.md`, line 59) |
| 5 | **Criterion 4.** Codex ran six isolated same-family task actors; Claude ran none | Gap: the minimal admissible evidence of actual use and the actor independence it requires. Owner decision: funding, D5 |
| 6 | **Independence levels.** Both lines use "independent" for different things | Gap: define same-family nonauthor, cross-family and fresh actor, and which claim needs which |
| 7 | **Reduction.** Claude declared paths, measures and a guard; Codex measured bytes on six operations against two baselines | Partly answered at `1fce537`, which the Claude line has not rebound to: a rebind defect for Claude. Remaining gap, if the pen confirms: the baseline and the path-selection rule |
| 8 | **Frames.** Claude declares a byte capacity and one frame per contract task; Codex declares neither | `1fce537` requires measured activations under finite context and attention (`INTENT.md`, line 43; `REFERENCE_FRAME_BASIS.md`, C3 Writer row). A declared capacity figure and one frame per contract task: permitted design choice unless the pen finds a clause that requires them |
| 9 | **Pillars.** Claude binds a pillar to every family row; Codex binds none | The pillar list exists (`PRODUCT.md#foundational-reduction`). Owner decision: the proposed changes to accepted conditions and the pillar list. For the binding itself, CX-03: gap or Codex implementation defect; the pen classifies |
| 10 | **Identity, version, the UX compliance test** | Owner decisions with no home yet. One sentence each |

### Convergences to ratify

- Five core result values with a precedence rule for conjunction.
- Every supersession marked proposed until the product owner accepts it.
- One owner for fit and attention.
- Review expectations fixed before the reviewer opens the subject.

## Stage 2: the builds

Goal: each tenant returns one frozen candidate on the signed commit.
Gate: both handoffs posted and both admissions recorded in the ticket.

Each agent, in its own tenant only:

1. **Rebind** to the signed commit on `main` and record the rebind in
   the ledger. The pen records the admission in the ticket.
2. **Repair.** Codex: CX-03 to CX-09 from
   `comments/claude/20261015T021914Z_REVIEW_CODEX_I3_C29B2BE.md`.
   Claude: the findings of Codex's Stage 1 review, and the implementation
   defects of the divergence list. Each finding is repaired, or declined
   with a reason in the ledger. A common decision does not repair a
   candidate: where the pen classified a finding as a gap and decided it
   in Stage 1, the finding is replaced by the implementation or evidence
   task the decision yields, or by a recorded reason that the decision
   requires no tenant change. The same holds for every Stage 1 decision,
   in both tenants.
3. **Port** from the donor commit under D3 and D4.
4. **Evidence**, as the signed specification names it, and at least:
   - self-mapping of the 52 discriminators and J53 to J55;
   - a conservation record over the common inventory, with every
     replacement relation decided under the signed specification or
     marked proposed;
   - interpretation coverage as the signed specification requires,
     checked by the installed Axiom Indexer `v2.5.1-rc.2`;
   - frames as the signed specification requires;
   - reduction measured as the signed specification requires;
   - criterion 4 under D5;
   - one same-family nonauthor working review, expectations first, and
     the repair of its findings; for each ported part, this is the
     acceptance-bearing review, D4.
5. **Freeze**: commit, digests, and a handoff under the tenant's
   `qualification/` naming the commit, every port with its bearing
   review, every gap and every variance. No acceptance claim.

Scope rule: no new members, no new scope, no re-derivation of settled
text, unless the signed specification requires it.

## Stage 3: cross-family reviews

Goal: each candidate is read by the other family against the signed
specification. Gate: both reviews and both successor freezes posted.

1. Each agent reviews the other's candidate at the handoff's commit:
   expectations first; the six criteria; the 52 discriminators and J53
   to J55; standing declared as interested party; no repair. Posted
   under `comments/<agent>/`. For a ported part the reviewer authored
   as donor, its reading is supplementary and the post marks it so; the
   acceptance-bearing review of that part is the receiver's Stage 2
   nonauthor review, D4.
2. Each agent repairs its own candidate's findings in one round. The
   repair is a successor freeze. The repairer posts the successor commit,
   its digests, the changed loci, and a **dependency statement**: every
   frame, result mapping, interpretation clause, conservation row and
   evidence item that depends on the changed material, and for each
   whether it was regenerated, rerun or left as it was.
3. The reviewer reads the changed material and every named dependent,
   and records, for each reused evidence item, whether it still applies
   to the successor commit. A dependent the statement did not name is a
   finding. The reviewer posts a confirmation or the residuals.
4. A ported part that the repair changed, or whose Stage 2 evidence the
   dependency statement or the reviewer marks as no longer applying, is
   read back on the successor commit by the receiver's same-family
   nonauthor, never by the donor. The readback is posted with the
   successor freeze under the receiver's `qualification/`. Evidence the
   repair did not affect keeps its standing.

## Stage 4: the choice

1. The product owner applies D6 to the two successor freezes. The pen
   records the choice and the reason in the ticket. The chosen candidate
   becomes the new v3 basis.
2. The chosen line's agent prepares the release cut on the product
   owner's instruction: the chosen tenant branch merged to `main`, where
   the signed specification already stands, then the release process of
   the common specification. No agent merges or pushes without that
   instruction.
3. The other line is retired: branch kept, not merged, not deleted.

## Stops

Stop and report to the product owner when: the signed commit is missing
or changes; a port cannot be rebound without changing its meaning; a
required evidence item cannot be produced within the budget rule; a
repair arrives without a dependency statement; a finding needs a common
decision. Never proceed past a gate on an assumption.

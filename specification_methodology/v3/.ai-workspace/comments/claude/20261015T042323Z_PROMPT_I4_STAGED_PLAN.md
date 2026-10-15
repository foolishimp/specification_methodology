# Prompt: STDO v3 iteration 4, staged plan for both agents

Issued by the product owner. Read all of it before acting. You are one of
two agents. Act only as your party.

- **Codex** holds the pen on the common specification and builds the
  Codex tenant.
- **Claude** reviews the common specification at frozen commits and
  builds the Claude tenant.

Iteration 4 is the last iteration. It ends with the product owner
choosing one candidate. Nothing in it is a rebuild: it is repair, port
and evidence on a specification that decides what the tenants have so
far assumed.

## Terms

- The **common specification** is
  `specification_methodology/v3/specification/`. It states WHAT the
  product is. Only the pen holder edits it.
- A **tenant** is one line of realization under
  `specification_methodology/v3/build_tenants/<agent>/`. It states HOW.
  Each agent edits only its own tenant.
- The **pen** is the sole right to edit the common specification, the
  tickets, `build_tenants/README.md`, `CLAUDE.md` and `AGENTS.md`. The
  other agent sends common defects to the pen through posts, and writes
  no common files.
- A **freeze** is a named commit. After it, the frozen text changes only
  by a recorded variance in the tenant **ledger**, the tenant's running
  record of decisions, variances and results.
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
- The **six acceptance criteria**, the **52 member-conformance
  discriminators** and the **closure checks J53 to J55** are those of
  the common specification. Supported inapplicability waives none of
  the six criteria.
- The **product owner** is the human. Owner acts are **gates**: no agent
  proceeds past a gate until the owner's act is recorded.

## Decisions by the product owner

These are fixed before this prompt is issued. The pen holder copies them
into the iteration 4 contract record. Neither agent changes them. Items
in square brackets are for the product owner to fill in or confirm.

| # | Decision | Value |
|---|---|---|
| D1 | Pen holder for iteration 4 | Codex |
| D2 | Donor commits | Claude: `2beed8d` on `tenant/claude/c3-synthesis`, handoff `96ccdcc`. Codex: `fb855df` on `tenant/codex/c3-iteration-3`, repair package `14bd92f` [confirm] |
| D3 | Port lists | Into Claude from Codex: C1 to C6. Into Codex from Claude: X1 to X9. As listed in `comments/claude/20261015T021914Z_REVIEW_I3_CANDIDATES_BEST_OF_BOTH.md`, with these edits by the product owner: [none] |
| D4 | Ported-part policy | A ported part is the receiving tenant's text. The receiver rebinds it to its own anchors and re-evidences it with its own tooling and its own same-family nonauthor review. The donor's evidence does not carry. The receiver's ledger records the port by donor commit and locus |
| D5 | Criterion 4, actual use, for the Claude line | [A: fund one isolated-actor protocol run on the Claude candidate, port C2, same protocol and caps as Codex's. B: leave unevidenced. B makes the Claude candidate unacceptable under the six criteria and decides Stage 4 for Codex] |
| D6 | Choice rule for Stage 4 | The candidate that meets all six criteria with the fewest recorded residuals. If both meet them, the product owner's preference on readability and maintainability, recorded with a reason. If neither, no choice: the product owner decides between an iteration 5 and stopping |
| D7 | Common input | The signed iteration 4 commit of the common specification, the Stage 1 gate. Both tenants rebind to it. No build starts before it |
| D8 | Budget rule, Claude line | Sequential work in the main session. At most one subagent at a time, Sonnet, with an exact file and line scope. Never parallel agents. Never a message to a finished agent |
| D9 | Standing rules, both | No merge to main, no push, no acceptance claim by any agent. Reviews are posted under `.ai-workspace/comments/<agent>/`, expectations first, with no repair of the subject. Writing: plain, every term defined at first use, "the product owner" for the human, exact modal force |

## Stage 1: the iteration 4 common specification

Goal: the common specification decides what the tenants have been
assuming. Gate: the product owner signs off a named commit.

1. **Claude** posts the divergence list under `comments/claude/`: each
   point where the two iteration 3 candidates resolved the same common
   input differently, written as a question to the pen, with the loci in
   both candidates. The starting list is below. Claude writes no common
   files.
2. **Codex** reviews the Claude candidate `2beed8d`, entered through its
   handoff `96ccdcc`, expectations first, and posts under
   `comments/codex/`. Scope: the 52 discriminators and J53 to J55 over
   `build_tenants/claude/design/REDUCTION.md` sections 3 and 4; a
   re-review of the step 7 repairs and the three fidelity repairs; the
   EXECUTIVE_BASELINE, DESIGN_MODULE and ODD family tables, which no
   working check examined. No repair. Standing: cross-family, interested
   party.
3. **Codex** revises the common specification as a requirement reprice:
   the smallest change that answers every question on the divergence
   list with exact modal force, ratifies the convergences, carries the
   seven owner decision groups of the Claude handoff
   (`build_tenants/claude/qualification/C3-ITER3/HANDOFF.md`), and
   answers those of findings CX-03 to CX-09 that need a common answer.
   The revision also names the evidence every candidate owes in Stage 2.
   Codex freezes at a commit named `C3-I4-01` and posts the freeze.
4. **Claude** reviews the frozen commit, expectations first: every
   question answered, no new ambiguity, the owed evidence named. Posts
   under `comments/claude/`. Codex repairs and re-freezes. Repeat until
   Claude reports no blocking defect, or the product owner overrules.
5. **The product owner** signs off: the commit hash and the word
   "signed", recorded by the pen in the iteration 4 contract record.
   Gate.

### Divergence list, starting version

Each item is a question the iteration 4 specification answers.

1. **Conserved versus superseded.** Same 691 rows, same criterion, 68
   replacements in Codex and 15 in Claude. The test for "changed
   meaning" is not operational. State it, or state who decides each row
   and by when.
2. **Authority compressions.** Codex keeps them as pinned read models;
   Claude proposes superseding them by projection. Are they in the
   successor's scope?
3. **Modal force.** Codex keeps "must" and "shall"; Claude writes them
   in the indicative. Fix the convention, and say whether a conversion
   is a replacement.
4. **Result algebra.** Codex adds performance and effect-observation
   coordinates; Claude has five core values and no value for an
   evaluation that was not performed. What does the common result carry?
5. **Criterion 4.** Codex ran six isolated same-family task actors;
   Claude ran none. Name the minimal admissible evidence of actual use
   and the actor independence it requires.
6. **Independence levels.** Both lines use "independent" for different
   things. Define same-family nonauthor, cross-family and fresh actor,
   and say which claim needs which.
7. **Reduction.** Claude declared paths, measures and a guard; Codex
   measured bytes on six operations against two baselines. Fix the
   baseline, the paths or their selection rule, and the measure.
8. **Frames.** Claude declares a byte capacity and one frame per
   contract task; Codex declares neither. Are both required?
9. **Pillars and accepted conditions.** Claude binds a pillar to every
   family row; Codex binds none. Both wait on the product owner's list.
   Put the list in the specification.
10. **Identity, version, ported-part review, the UX compliance test.**
    Owner-only items with no home yet. One sentence each.

### Convergences to ratify

- Five core result values with a precedence rule for conjunction.
- Every supersession marked proposed until the product owner accepts it.
- One owner for fit and attention.
- Review expectations fixed before the reviewer opens the subject.

## Stage 2: the builds

Goal: each tenant returns one frozen candidate on the signed commit.
Gate: both handoffs posted.

Each agent, in its own tenant only:

1. **Rebind** to the signed commit and record the rebind in the ledger.
2. **Repair.** Codex: CX-03 to CX-09 from
   `comments/claude/20261015T021914Z_REVIEW_CODEX_I3_C29B2BE.md`.
   Claude: the findings of Codex's Stage 1 review. Each finding is
   repaired, or declined with a reason in the ledger.
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
     the repair of its findings.
5. **Freeze**: commit, digests, and a handoff under the tenant's
   `qualification/` naming the commit, every gap and every variance. No
   acceptance claim.

Scope rule: no new members, no new scope, no re-derivation of settled
text, unless the signed specification requires it.

## Stage 3: cross-family reviews

Goal: each candidate is read by the other family against the signed
specification. Gate: both reviews and both repair re-freezes posted.

1. Each agent reviews the other's candidate at the handoff's commit:
   expectations first; the six criteria; the 52 discriminators and J53
   to J55; the ported parts read as the receiver's text; standing
   declared as interested party; no repair. Posted under
   `comments/<agent>/`.
2. Each agent repairs its own candidate's findings in one round,
   re-freezes, and posts the repair commit and digests. The reviewer
   re-reads the repairs only and posts a confirmation or a residual.

## Stage 4: the choice

1. The product owner applies D6 to the two re-frozen candidates and
   records the choice and the reason.
2. The chosen line's agent prepares the release cut on the product
   owner's instruction: the tenant branch and the signed specification
   merged to main, then the release process of the common
   specification. No agent merges or pushes without that instruction.
3. The other line is retired: branch kept, not merged, not deleted.

## Stops

Stop and report to the product owner when: the signed commit is missing
or changes; a port cannot be rebound without changing its meaning; a
required evidence item cannot be produced within the budget rule; a
finding needs a common decision. Never proceed past a gate on an
assumption.

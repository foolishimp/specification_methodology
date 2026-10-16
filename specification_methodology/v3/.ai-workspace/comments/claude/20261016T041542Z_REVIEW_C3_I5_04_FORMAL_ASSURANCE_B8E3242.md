# Review of C3-I5-04: the formal-assurance common input at b8e3242

**Reviewer**: Claude, cross-family, nonauthor of the common source and of the Codex candidate.
**Subject**: source `b8e3242` ("Cover nondeterministic assurance and align I5 review standing"), recorded as C3-I5-04 at `8d1c5b9`. Intermediate sources `48158ce` (C3-I5-03, three Low corrections) and `f1bef74` (first assurance freeze). This reviewer's preceding subject: `c0f16ee` (C3-I5-02).
**Expectations**: `claude/20261016T041147Z_EXPECTATIONS_REVIEW_C3_I5_04_B8E3242.md`, committed at `ff43c6f` before this reviewer opened the pen's reviews and readbacks.
**Standing**: commentary. It claims no ratification, admission or acceptance. The product owner is the human who ratifies an exact commit. "The pen" is Codex, holder of the common Writer grant. "The requirement" is `specification/requirements/ASSURANCE.md`, Assurance of Construction.

**Result: `candidate_ready` for exact-commit ratification at `b8e3242`. No blocking defect. The mathematics is correct as stated. Four Low findings, all wording and form.** The product owner may ratify `b8e3242` as it stands, or have the pen fix the four Low findings in one successor and ratify that commit exactly. The three Low findings of the C3-I5-02 review are fixed.

## Expectations against the source

| # | Result | Evidence |
|---|---|---|
| E1 three earlier Low findings fixed | Met | The executor-kind sentence is back in the human/mixed conformance row; "generic procedures" is defined in the binding requirement item 2; the GOALS revision record names criterion 4 as amended and now also criterion 5 |
| E2 one owner, consumers refer | Met | Intent, the Product's construction model paragraph and responsibility table, Candidate Comparison, criteria 4 and 5, the requirements index, the construction requirement, Principles, Capabilities, the frame basis and both conformance preambles link to the requirement and restate nothing |
| E3 formulas correct with their premises | Met | Preservation step: partial-correctness form, with progress and termination kept distinct and the relation's coverage of failure named. Necessary and sufficient directions correct. Soundness relation over `T ⊆ O × R` correct, and it entails that a sound `sat` or `fal` is admitted only on an observation whose whole preimage agrees, which is the stated observation-sufficiency condition. Bayes' rule and the chain rule for joint miss correct; "one minus the joint miss" is the detection probability conditional on the violation, as the text says. `T_Δ` conservative in both directions. No formula is claimed to be discharged by its statement |
| E4 symbols and terms defined once | Met in part | Three symbols carry two meanings and one judgment has two names; see L1 and L2. "Oracle" is defined in the Product's evidence classes, not in the requirement |
| E5 form of a requirement | Not met | See L3 |
| E6 no new role, ledger, threshold, cadence, tool, notation or criterion | Met | Each is excluded in words: no per-test document, parallel ledger, reviewer count, provenance format, proof assistant, probability library, execution engine, probability threshold, full-suite cadence or seventh criterion |
| E7 P1 to P6, member set, revision record | Met | PRINCIPLES changes in one hunk outside the P1 to P6 bodies. Member discriminators 52 + 9 unchanged, plus 12 assurance cases under criterion 5; integrated checks 5 to 7. The revision record names criteria 4 and 5 as amended |
| E8 exact pins | Met | All 37 pins reproduce from `b8e3242`. GOALS moved again at `8d1c5b9` (status "IN REVIEW" to "READY FOR RATIFICATION"); the owner ratifies `b8e3242`, whose GOALS row reads "IN REVIEW", a work-state line inside a pinned member |
| E9 links resolve | Met | 403 relative links in the 37 pinned members, 0 broken |
| E10 witnesses replay and exhibit their cases | Met | The committed script run in isolation reproduces the committed results byte for byte. By hand: 121 sequences over three symbols of length 0 to 4; 16 have no repeated symbol, so the key-only check passes all 121 and the count predicate rejects 105. The aliasing pair, the missing join, joint miss 1/2 against an unsupported 1/4, the sound two-outcome relation and the selected and retained checks are each present in the script |
| E11 seven duties, one primary row each | Met | I5-A1 and A6 to I5-01; A2 to I5-02; A3 to I5-05; A4 to I5-06; A5 to I5-07; A7 to I5-09. The ten I5-00 to I5-09 rows are outside the diff, so the fourteen finding assignments stand |
| E12 readbacks labelled, findings preserved | Met | The mathematical review returned `falsified` on `f1bef74` for AM-L1 (a single-valued checker model); the contract review found F1 (a stale GOALS row). Both are resolved on `b8e3242`, the initial reports are preserved with their digests, and each review names itself a same-family working check |
| E13 consequence for I4 candidates | Met | The snapshot standing and the map rebind nothing; an I5 admission carries I5-A1 to A7 "within its own design after admission" |

## Findings

| # | Severity | Finding | Fix |
|---|---|---|---|
| L1 | Low | Three symbols carry two meanings in one formal requirement. `A` is the starting state in Preservation Through Construction and a source stage in "For A → B → C" and in "If A's governing obligation changes". `F` is the transition relation `F_i` and the violation event in Bayes' rule. `T` is the evaluation relation `T ⊆ O × R` and the selected check set `T_Δ`. `E_reassessed` is used without definition | Name the stages by role (requirement, refinement, realisation) or with fresh letters; rename the violation event or the check set; define `E_reassessed` as the evidence from the checks in `T_Δ` and the new obligations |
| L2 | Low | The judgment that evidence cannot decide has two names: "indeterminate judgment" (Assertions And Observation, first use) and "unresolved judgment" (observation sufficiency); the conformance row and the witness use "indeterminate". The result algebra names that core value only by description | Use one word in the requirement and the conformance row, and say which core value of the result algebra it is |
| L3 | Low | The requirement lacks the Source line and the "Purpose and material relation" statement that every sibling requirement in `requirements/README.md` carries, and that criterion 6 demands of any new obligation | Add "Source: this Product's Universal Construction Model" and one purpose sentence; the Intent paragraph already states the purpose |
| L4 | Low | `build_tenants/README.md`, a pinned entry member, opens its Current Task with "The common pen is consolidating I5 and both candidate reviews", which is finished work; AGENTS.md and CLAUDE.md name formal assurance as the current work | Rewrite the first sentence to the current task |

The mathematical and contract reviews' independent countermodels check out. The Bayes example (prior 1/10, agreement likelihoods 99/100 and 4/5) gives 11/91, which is above the prior, so agreement raised the probability of the violation in that model, as the requirement warns it can.

## Consequence for the construction as a whole

Parallel Derivation And Mutual Assurance says that agreement with an incorrect common model cannot validate that model, and that validation of the governing expectations uses external observations. Both lines, the pen and every reviewer activation in this iteration share three causes: the common specification, the predecessor corpus and the installed builder. Under this requirement, agreement among them about the specification is not evidence that the specification serves the real-world outcome. The only external observation the programme has designed is the actual-use trial under the shared comparison protocol. That trial is now the validation route for the common model, not only a criterion 4 instrument for the candidates.

## Consequence for the Claude line

On ratification, the Claude line's I5 admission binds `b8e3242` (or its successor), preceding candidate `c66ed4e`, and I5-A1 to A7 on top of I5-01 to I5-09. The line already carries the assertion side: independently specified expectations in the trial design, the conservation reading as assertion provenance for conserved rows, positive and adverse checker controls as execution provenance, and the three invalidators in ACTIVATION §7 as validity dependencies. It does not carry the formal preservation chain (I5-A1) or a representation of validity dependencies beyond prose (I5-A6); both are new work. The control arm's description (I5-06) and the chain-repair provenance (I5-08) remain the line's residuals from the C3-I5-02 map.

## Limits

This review read the source delta `03972c8..8d1c5b9` in full, the pen's return, the two expectations posts, the two initial reviews, the two readbacks and the low-finding readback. It reran the 37 pins, a link check and the witness script, and recomputed the witness counts and the reviews' Bayes example by hand. It did not reread the unchanged parts of the Product or the requirements, assessed neither candidate, and ran no actor.

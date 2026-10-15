# Expectations for the iteration 4 working reviews

Written by the Executive (the candidate's author) before any reviewer
opened its subject, so that each review is judged against something fixed
in advance. These are same-family working expectations, not the
independent expectations of a cross-family review; the Codex line will
set its own for Stage 3.

| Id | Subject | Expected |
|---|---|---|
| E1 | I3-8r repairs (`416bdb5..2beed8d`) | each of FR-01, FR-03, FR-04, FR-05, FR-06, FR-08, FR-09, FR-10 and FR-11 is repaired at its owning locus as the finding's smallest repair states, and no other determination changes in the diff. FR-02 and FR-07 are not repaired by text: the ratified test judges each converted row by meaning (I4-04) |
| E2 | fidelity repairs in `a_c/i3/tools/spec.py` | `authority-kinds-never-collapse` carries "by default" and the lawful coincidence; `reuse-not-by-role-change` carries the unchanged-consumer trigger and the independent-judgment exception; `block-outside-claim` uses `states` and keeps "by itself" |
| E3 | I4 member edits (`2beed8d..HEAD`) | ACTIVATION §2 step 3 states the fit rule exactly: no measurement or supported bound gives `indeterminate`; a counterexample such as a measured excess gives `falsified`; a correct result does not satisfy fit. RELEASE §9 states the conservation test on required and permitted decisions, modal force, triggers, scope and exceptions, without changing the four disposition values. EVALUATION §3 adds only that a received contribution keeps its author and that author's reading is no independent acceptance. ACTIVATION §1 Applicability adds only that a supported inapplicability is recorded apart from results and waives no criterion. CONFORMANCE rows 28, 49 and J55 cite loci that carry those determinations. No edit adds an obligation the common text does not require |
| E4 | family tables of EXECUTIVE_BASELINE, DESIGN_MODULE and ODD | every row cites commitments with the standing FOUNDATIONS §3 gives them (P0 recovered; P1, P2, P3, P4a, P6 independent; P4b derived from P0 and P2; P5 derived from P0 and P6), or instance premises labelled as such, or imported families labelled as imported; each consequence follows from its premises by the stated inference; each policy choice is labelled and has an owner; each Pillar cell names a pillar of the common list or says none. Expected defects, if any: a premise with wrong standing, a consequence that does not follow from what is cited, an unlabelled policy, an empty Pillar cell |
| E5 | categorical claims | FOUNDATIONS §4 Formal fragment, EVALUATION §6 Equivalence ladder and AXIOMATIC_CALCULUS §5 either carry a declared demonstration for each categorical claim or state that the claim is conditional on one; no categorical property is asserted without it |
| E6 | ports | each verbatim I3 part matches its source at `31f28f9` byte for byte; each adapted part differs only as CROSS_SYNTHESIS records; each port has one owner and no link to `build_tenants/codex/`; the I4 adaptations C3, C4 and C5 do what `ports.md` says and nothing more |
| E7 | conservation batches | every row gets one of `conserved`, `changed`, `indeterminate`, with a concrete counterexample for every `changed` and a named missing item for every `indeterminate` |

Expected uncovered scope, stated now: the "Rule in this member" links of
the family tables are not followed (the members are not in the packets);
the fidelity of clauses other than the three repaired is not re-reviewed;
no desk trace is run; no actual use is run.

# Fidelity cases, iteration 5: group G14 and premise P4a

Same-family working evidence: a Claude case writer on the Claude line, a
declared exception under `design/INTERPRETATION.md` §6 and
CONSTRUCTION_BINDING section 1. Working evidence, not independent
assessment.

## Basis and order

Subject commit: `e5652ef3a9c7a0503ac7176646383d424f533fee` (worktree
`specification_methodology-claude`, clean at that commit).

Read before the first save, in this order, and nothing else of the
model: `design/INTERPRETATION.md` §6 (lines 217-263) and §3 Standing
(72-103); `a_c/i3/README.md`; `standards/FOUNDATIONS.md` 477-493,
538-567, 1131-1526; `standards/ACTIVATION.md` 198-346; heading maps by
grep (its P4a hits at FOUNDATIONS 400 and 555 are unused). Not opened
before the first save: `a_c/i3/axiomatic-program.json`, `fragments/`,
`tools/`, `SIGNATURE.md`, `dispositions/`, `coverage.json`,
`bindings.json`, `fidelity/cases.md`, `fidelity/review.md`.

Length note: the first save ran to 3,670 words and was trimmed to the
limit after the model had been opened for the review; no case changed in
determination, kind, standing or defects.

Selection: at least one case per section (ten sections), weighted to
display formulas, non-entailments and non-requirements; no random sample.
Lines are at the subject commit.

## Cases

### FC5-1 P4a: composition only under the typed condition

Source: FOUNDATIONS 477-478, "Two steps compose only when the first's
result type and judgment satisfy the second's exact declared domain and
preconditions."
Determination: composition is conditional on four parts: the first's
result type and judgment; the second's exact declared domain and
preconditions.
Preserve: "only when" as a necessary condition, not a grant; all four
parts; standing `premise`; owner FOUNDATIONS §3.
Kind: none in the source for a commitment, and the design makes
`support-kind` optional here; if recorded, `externally-assessed-predicate`
(two steps' fit is assessed against declared contracts), never
`discharged-argument`, since the paragraph's argument discharges P4a's
independence, not P4a.
Defect: "only when" read as "when"; "judgment" or "exact" dropped; a
standing other than `premise`; a kind purporting to discharge the
commitment.

### FC5-2 P4a: what P4a forbids

Source: FOUNDATIONS 485-487, "... the first step's other intermediate
results and stop state are lost; P4a forbids both."
Determination: P4a forbids two things: composition without the typed fit,
and loss of the first step's other intermediate results and stop state.
Preserve: both conjuncts; the retention prohibition belongs to P4a, not
only to P4b; force `forbids`; the premise's standing.
Kind: `discharged-argument` (the paragraph argues it).
Defect: no clause for the retention prohibition (the model then cannot
answer), unless the README's exclusion of non-entailment arguments says
so.

### FC5-3 Construction relation: lawfulness establishes neither

Source: ACTIVATION 222-224, "A lawful construction can remain incomplete
or fail to reach Z, and lawfulness establishes neither delivery nor
optimality."
Determination: lawful is not delivered and not optimal; incompleteness
and failure are compatible with lawfulness.
Preserve: "can" as a possibility; "establishes neither" as a
non-entailment, not a prohibition; standing `consequence` of P2, P3, P6
(227).
Kind: `discharged-argument`; argued from the commitments.
Defect: `forbids` a delivery claim; `permits` remaining incomplete;
supports other than P2, P3, P6.

### FC5-4 Construction relation: no imposition

Source: ACTIVATION 253-255, "No exhaustive optimisation, universal
numerical budget, scalar cost measure or preferred strategy is imposed by
this relation or its consumers (P2, P5, P6)."
Determination: the relation and its consumers impose none of the four;
the selection belongs to the realisation and the actor (250-251).
Preserve: "no ... is imposed" as a disclaimer (`states`); all four items;
the scope; standing `consequence` (P2, P5, P6); the selection as a
`policy-choice` of the realisation and the actor.
Kind: `discharged-argument`.
Defect: `forbids` the four (inverted); `permits` them (the grant is at
250-251); an item dropped.

### FC5-5 Construction relation: no universal termination proof required

Source: ACTIVATION 298-301, "... no universal termination proof is
required before bounded work can begin, and where such a proof is absent
the claim stays within the available evidence."
Determination: a formal claim supplies premises and argument (requires);
no universal termination proof is a precondition of bounded work; absent
the proof, the claim is bounded by the available evidence.
Preserve: the three kept apart; the trigger "where such a proof is
absent"; "universal"; standing `consequence` (P5, P2, P6, 313).
Kind: `discharged-argument`.
Defect: `forbids` a termination proof; the trigger dropped; "supplies"
softened to a permission.

### FC5-6 Construction relation: a revised model, by itself

Source: ACTIVATION 285-287, "A prediction error alone does not decide
whether the required outcome holds. A revised model does not erase the
counterexample or by itself repair the realisation."
Determination: two non-entailments scoped by "alone" and "by itself".
Preserve: the scope words; `states`; the counterexample survives
revision; standing `consequence` (P1, P2, P5, P6, 293).
Kind: `discharged-argument`.
Defect: "by itself" or "alone" dropped; `forbids` revising the model; the
counterexample dropped.

### FC5-7 Construction synthesis: standing

Source: FOUNDATIONS 544-546, "It is derived, not a further commitment,
and has the standing of a consequence under Foundation to law below
(P6)."
Determination: the synthesis has `consequence` standing; neither a
premise nor a policy choice.
Preserve: `consequence` with P6 among the supports; owner FOUNDATIONS §3;
ACTIVATION §1 owns the construction relation (543-544).
Kind: `discharged-argument`.
Defect: `premise` or `policy-choice` on a synthesis clause; P6 missing.

### FC5-8 Construction synthesis: do not by themselves prove

Source: FOUNDATIONS 564-566, "Feedback, a useful model and locally valid
steps do not by themselves prove reachability, stability, optimality or
termination (P5, P6)."
Determination: three things are not, by themselves, proof of four
properties; they may be parts of a proof.
Preserve: "by themselves"; all three subjects and four properties;
`states`; standing `consequence` (P5, P6).
Kind: `discharged-argument`.
Defect: `forbids` feedback or local validity as evidence; the four
properties cut; "by themselves" dropped.

### FC5-9 Assurance relations head: notation and instance premises

Source: FOUNDATIONS 1140-1141, "The notation states proof obligations;
writing an implication does not discharge it." And 1144-1149: instance
premises (a) Γ, (b) Ω, (c) a checker, "not commitments".
Determination: every display formula of the six subsections is an
obligation, not a discharged result; the three instance premises are
distinct conditions, each row citing its own.
Preserve: `states`; standing `consequence` (row 8, P1); instance premises
kept apart from P0 to P6 and, if encoded as `premise`, owned by
FOUNDATIONS §4.
Kind: `discharged-argument`; the sentence fixes `stated-formula` as the
kind of every formula clause in the family.
Defect: a formula clause carrying `discharged-argument`; instance
premises labelled commitments or merged; if a, b, c are not encoded, the
rows' premise lists cannot be matched (cannot answer, say so).

### FC5-10 Preservation: the step form

Source: FOUNDATIONS 1186-1193, "`F_i ⊆ X_i × X_(i+1)` the declared
transition relation ... A claimed preservation step has the form: For all
x, x': P_i(x) and F_i(x, x') implies P_(i+1)(x')." And 1196-1197, a
completion-only relation "alone supplies no claim" about refusal,
failure, interruption or unknown effects.
Determination: a universally quantified step form over a relation F_i;
"claimed", so an obligation; a completion-only relation says nothing
about the four other cases.
Preserve: the quantifier; F_i as a relation, not a function; standing
`consequence` (P4a, P1, P6, 1200); "alone".
Kind: `stated-formula` (1140-1141).
Defect: `discharged-argument` on the formula; quantifier or relation
dropped; "supplies no claim" hardened into "must cover" the four cases.

### FC5-11 Preservation: approximate transformations

Source: FOUNDATIONS 1212-1217, "Approximate transformations state their
adequacy relation and an established bound for the complete composition;
local tolerances cannot be assumed to add or to remain unchanged."
ACTIVATION §4 Refinement "owns the per-step law".
Determination: an approximate step must state an adequacy relation and a
bound for the complete composition; the tolerance inference is barred;
the chosen relation and bound belong to the step's law owner (row 1,
1153).
Preserve: `requires` on stating; "for the complete composition"; "cannot
be assumed" as a barred inference, not a prohibition on tolerances;
standing `consequence` (P1, P6, 1219); `policy-choice` owned by
ACTIVATION §4 for the chosen relation and bound.
Kind: `discharged-argument`.
Defect: the obligation filed as `policy-choice` (hollow); "cannot be
assumed to add" as "must not add"; the owner missing.

### FC5-12 Assertions: the three directions

Source: FOUNDATIONS 1242-1250, "Q_r implies q_t : q_t is a necessary
condition of Q_r. q_t implies Q_r : establishing q_t is sufficient for
Q_r. (q_1 and ... and q_n) implies Q_r : the stated conjunction is
sufficient." Then 1247-1250: "conditional on Γ and Ω"; a
necessary-condition pass "does not establish the full obligation"; a
conjunction "requires its own coverage and compatibility argument".
Determination: three directions with their names, all conditional on Γ
and Ω; a necessary-condition pass establishes no more; a conjunction needs
its own coverage argument.
Preserve: direction and name of each implication; the Γ, Ω condition;
`requires` on the coverage argument; the two non-entailments; standing
`consequence` (P1, P6, P5).
Kind: `stated-formula` for the three lines; `discharged-argument` after.
Defect: necessary and sufficient swapped; the Γ, Ω condition dropped; the
formula's kind not `stated-formula`.

### FC5-13 Assertions: soundness of judgments

Source: FOUNDATIONS 1266-1270, "For every s in Ω: (π(s), sat) in T
implies q_t(s). (π(s), fal) in T implies not q_t(s)."; 1255-1257, a
universal soundness claim "covers all admitted conclusions, not a
favourable selected run"; 1276-1279, a test pass remains an observation
"while the oracle's fidelity is unestablished", a failure likewise.
Determination: soundness in both directions, for every s in Ω and all
admitted conclusions (T is a relation); a test pass is an observation,
not satisfaction, while the oracle is unestablished; failures symmetric.
Preserve: both lines; "For every s in Ω"; the all-admitted-conclusions
scope; the oracle trigger; the symmetry; standing `consequence` (P6, P5,
P1, 1283).
Kind: `stated-formula` for the two lines; `discharged-argument` for the
prose.
Defect: the `fal` line dropped; scope narrowed to deterministic checkers;
the oracle trigger dropped; formula kind wrong.

### FC5-14 Assertions: observation sufficiency

Source: FOUNDATIONS 1285-1300, "A checker that always decides `q_t`
correctly from π alone requires: For all s, s' in Ω: π(s) = π(s') implies
q_t(s) = q_t(s')." When violated, "further evidence, a justified narrower
scope or an indeterminate judgment is required"; the condition
"establishes neither an executable decision procedure nor its cost".
Determination: the condition is necessary for a checker that always
decides correctly from π alone, not an obligation on every checker; when
violated, one of three responses is required; it yields no decision
procedure.
Preserve: the scope clause; the quantifier over pairs; the three
alternatives as a disjunction; "establishes neither"; standing
`consequence` (P3, P1, P5, P6, 1300); T and π as a `policy-choice` of the
assessment frame (row 4).
Kind: `stated-formula` for the condition; `discharged-argument` for the
consequence sentences.
Defect: the condition as `requires` on every checker (scope widened); the
three alternatives cut to one; formula kind wrong.

### FC5-15 Parallel derivation: agreement, disagreement, independence

Source: FOUNDATIONS 1335-1341, "Agreement is compatible with both being
correct and with a shared error; disagreement requires diagnosis ... and
does not identify the faulty party by itself." "Different actors, model
families or codebases do not establish statistical independence."
Determination: agreement is not correctness; disagreement obliges
diagnosis but identifies nothing by itself; distinct actors, families or
codebases are not independence.
Preserve: `requires` on diagnosis only; "by itself"; "do not establish"
as a non-entailment; all three subjects; standing `consequence` (P4a, P6,
P1, 1350).
Kind: `discharged-argument`.
Defect: `forbids` using different model families (inverted); "do not
establish" softened to "need not"; "by itself" dropped.

### FC5-16 Parallel derivation: nothing new is required

Source: FOUNDATIONS 1352-1355, "Shared derivations can be recorded once
and applied to a declared family. No new per-test document, parallel
ledger, fixed number of reviewers or prescribed provenance format is
required (P6)."
Determination: four artefacts are not required; shared derivations may be
recorded once per declared family.
Preserve: "no ... is required" as a non-requirement, not a prohibition;
"can be recorded once" as `permits`; the four items; "declared"; standing
`consequence` (P6).
Kind: `discharged-argument`.
Defect: `forbids` a per-test document or a parallel ledger (inverted); an
item or "declared" dropped.

### FC5-17 Quantified assurance: the posterior

Source: FOUNDATIONS 1367-1381, "Where quantified assurance is claimed, its
model states the population or uncertainty being modelled, prior
information, likelihoods, shared causes and calibration limits."; the
display "P(V | E, Γ) = P(E | V, Γ) P(V | Γ) / [...]"; "The denominator
must be nonzero."; the formula "supplies no missing likelihood or prior".
Determination: the model-statement obligation holds only where quantified
assurance is claimed; the posterior is conditional on Γ throughout; the
denominator is a side condition; the formula supplies no inputs.
Preserve: the trigger; the five things the model states; Γ throughout;
"must be nonzero" as `requires`; "supplies no" as a non-entailment;
standing `consequence` (no premises named; row 6: P6, P5, P1).
Kind: `stated-formula` for the display; `discharged-argument` for the
trigger sentence and the side condition.
Defect: `discharged-argument` on the display; the trigger, Γ or the
denominator condition dropped.

### FC5-18 Quantified assurance: joint miss

Source: FOUNDATIONS 1383-1397, the display "P(M_1 and ... and M_n | V, Γ)
= product over i of P(M_i | V, Γ, M_1, ..., M_(i-1))."; "Replacing those
terms with `P(M_i | V, Γ)` requires conditional independence under the
declared model."; one minus the joint miss "is not the probability that
the whole product is correct".
Determination: the exact factorisation; the simplification is conditional
on conditional independence under the declared model; one minus joint
miss is detection chance, not product correctness.
Preserve: the display; `requires` conditional independence; "under the
declared model"; "it is not" as a non-entailment; standing `consequence`
(P6, P1, 1399).
Kind: `stated-formula` for the display (1140-1141); `discharged-argument`
for the sentences.
Defect: the replacement as `permits` without the independence condition;
detection chance read as product correctness; display kind wrong.

### FC5-19 Quantified assurance: no threshold, no waiver

Source: FOUNDATIONS 1404-1407, "No universal probability threshold is
imposed and no probability estimate is required for every test. Required
safety, authority and acceptance conditions cannot be waived by a cheaper
assurance plan (P5, P6)."
Determination: two non-impositions and one prohibition; a threshold, if
any, is a `policy-choice` of the actor with admitted work authority under
the adopting Product (row 6, 1158).
Preserve: the first sentence as `states`; the second as `forbids`;
"universal" and "for every test"; standing `consequence` (P5, P6); the
owner of any threshold.
Kind: `discharged-argument`.
Defect: `forbids` a threshold (inverted); waiver as `permits` or `states`
(inverted); "for every test" dropped.

### FC5-20 Change impact: the selection

Source: FOUNDATIONS 1418-1437, "A candidate selection is: S_Δ = { t :
D*(t) intersects I(Δ) }."; "Excluding a check requires supported coverage
of its material dependencies and a reason the change cannot invalidate
the intended reused claim; an absent edge is not evidence of
non-influence."; 1428-1437: no graph database required; unknown impact
widens or leaves unresolved; a mandatory gate remains applicable.
Determination: S_Δ is a candidate selection; exclusion needs two things;
an absent edge proves nothing; unknown impact has two outcomes; gates
stand outside selection.
Preserve: "candidate"; `requires` on exclusion with both conjuncts; "is
not evidence" as a non-entailment; the disjunction; the gate's
unconditional applicability; the representation as a `policy-choice` of
the realisation (row 7); standing `consequence` (P5, P6, 1437).
Kind: `stated-formula` for S_Δ; `discharged-argument` otherwise.
Defect: S_Δ as the required selection (scope widened); an exclusion
conjunct dropped; "no exhaustive graph database is required" as `forbids`;
the gate made conditional on selection.

### FC5-21 Change impact: retention

Source: FOUNDATIONS 1443-1458, "Selection alone produces no execution
evidence; failed and indeterminate results retain their standing: E_new =
retain_applicable(E_old, new_subject, new_basis) union E_reassessed.";
1450-1453: retention establishes three validity conditions, the third
"unchanged or covered by an established preservation relation"; "A
changed hash alone establishes neither invalidity nor equivalence."
Determination: E_new is the union of retained-applicable old evidence and
reassessed evidence; retention is conditional on three validity
conditions, the third a disjunction; a changed hash alone decides nothing;
failed and indeterminate results keep their standing.
Preserve: the display; the three conditions with "unchanged or covered";
"alone" in both non-entailments; standing `consequence` (P3, P4b, P6,
1458) with P4b as the conservation premise.
Kind: `stated-formula` for the display; `discharged-argument` for the
conditions.
Defect: a retention condition dropped or the disjunction made a
conjunction; changed hash as `forbids` reuse (inverted); display kind
wrong; P4b missing.

### FC5-22 Formal representation: kinds, labels, finite examples

Source: FOUNDATIONS 1498-1504, "It distinguishes five kinds of support
..."; an external predicate "retains the source, scope and evidence
required to establish it; an arbitrary truth label does not discharge the
obligation."; "No particular proof assistant ... is selected". 1511-1514:
"Finite examples do not prove the universal implications above. An
unproved universal claim can remain unresolved ... where their governing
conditions permit them".
Determination: exactly five kinds; an external predicate carries source,
scope and evidence; a label discharges nothing; no tool is selected; finite
examples prove no universal; an unproved universal may remain unresolved
under a condition.
Preserve: the five, distinct; `requires` on what an external predicate
retains; the non-entailments; "No ... is selected" as non-selection, not
a prohibition; "can remain unresolved" as `permits` with its trigger;
standing `consequence` (P1, P6 at 1504; P5, P6 at 1514).
Kind: `discharged-argument`.
Defect: `forbids` a proof assistant; the permission's trigger dropped; a
kind missing or a sixth added; the three retained things cut.

## What the review must also check

Over all 89 G14 clauses and the P4a clause, by script where possible:

1. Each `statement` occurs verbatim (whitespace-normalised, table rows
   removed) in its owning section at HEAD, exactly once.
2. Each G14 clause carries exactly one `support-kind`: `stated-formula`
   where the statement is or contains a display formula (FC5-10, 12, 13,
   14, 17, 18, 20, 21), `discharged-argument` otherwise; none of the
   other three.
3. `force` matches the sentence: no non-entailment or non-requirement
   ("does not", "cannot", "neither", "no ... is required", "by itself",
   "alone") encoded as a prohibition or a permission; nothing softened.
4. Supports exist and match the source's parentheses where it names
   premises; operators match the sentence; every subject is a concept
   symbol.
5. The `uses` relation at ACTIVATION §7 points to the Change impact
   clause the source names (1487-1490).
6. Dispositions: the nine sections `encoded-in-part` with the right ids;
   EVALUATION `Return of a reconstruction` `not-encoded-i3`; totals 24 /
   8 / 181 as the README says.
7. README: 29 + 2 + 57 + 1 = 89; 154 clauses; 5 frame indexes; 80 and 9
   kinds; the `construction-and-assurance` row; Evidence boundary; Known
   gaps.
8. Standing: no hollow `policy-choice`; instance premises a, b, c, if
   present, not labelled commitments.

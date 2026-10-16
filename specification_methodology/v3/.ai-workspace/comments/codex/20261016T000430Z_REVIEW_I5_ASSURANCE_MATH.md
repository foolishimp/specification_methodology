# I5 Assurance: Mathematical And Provenance Review

## Result And Subject

**Result: `falsified` on the bounded common-source adequacy predicate for
`f1bef746bdae976e87f5a16a6a291469ff2f5d65`.** One Low finding concerns the
unqualified single-valued checker model. The preservation, oracle, probability,
provenance and reuse relationships otherwise satisfy the independently fixed
expectations within their declared scope. This is not a tenant verdict, owner
disposition or ratification.

Preimage: `5f839a769bdaee06f3f27a3e9f52904480f7a4d9`. Expectations were fixed
before successor acquisition in
[the expectation record](20261016T000430Z_EXPECTATIONS_I5_ASSURANCE_MATH.md),
SHA-256 `0e990fb6c3265485d4b69c20278de4bb5eef9f11a961f97e1d8ada0f2c313cfd`.
Its only subsequent change before source acquisition removed one trailing
newline byte, at the coordinator's request; no predicate changed.

Basis: the exact installed STDO 2.5.1-rc.2 release, manifest
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`, independently
verified valid with no failures in this activation. The common review grant is
`EC-COMMON-I5-04`, recorded at the subject's T-001 lines 23–31. The reviewer is
Codex, a same-family nonauthor under the declared working-review exception.
Neither model-family diversity nor statistical independence is claimed.

## Confirmed Finding

### AM-L1 — Low: the generic checker account leaves multiple permitted conclusions unrepresented

Source: `specification/requirements/ASSURANCE.md:37–54`, especially
`t: O → R` at line 37, read with its general application at line 3, permitted
human/mixed bindings at line 21 and the existing Build-Tenant Binding Requirement.

The displayed evaluation is a function: a fixed observation has exactly one
result. The text does not identify that as a selected deterministic abstraction
or state how it covers all conclusions of an admitted evaluator whose behaviour
is not single-valued on the acquired observation.

Counterexample: let the declared obligation be true at s and let its acquired
observation be o. An allowed human or probabilistic checker returns `satisfied`
in one execution and `indeterminate` in another execution on that same
observation and stated subject. Both conclusions are sound under the existing
claim and uncertainty contracts. A single `t(o)` cannot represent both actual
conclusions. The same issue matters when assurance is claimed for the entire
checker rather than one fixed run or one declared deterministic model.

The formulas are mathematically valid for their function model. Existing
scope, observation-binding and execution-conformance conditions prevent a
function model's conditional argument from automatically proving the broader
runtime claim. They do not explicitly supply the missing coverage relation.
Thus the finding is a Low gap in the shared formalisation's stated coverage,
not a demonstrated false Bayes theorem, invalid preservation inference or
existing tenant runtime defect. It is material to M4/M9 because the common
WHAT permits more than deterministic machine evaluation.

Required supported behaviour: a scoped deterministic claim remains scoped;
a claim about a checker that admits several conclusions covers those permitted
conclusions and its unresolved outcomes. Adding hidden state or randomness to a
model is not by itself evidence that the real evaluator's relevant outcomes
were covered. The author owns the representation and correction. This review
supplies no replacement clause or mandated relation/architecture.

No other confirmed finding was identified. No severity ranking among multiple
findings is needed. Priority, repair selection, acceptance and any wider
disposition remain with their existing owners.

## Predicate Results

All line references below name the frozen subject. `A` abbreviates its
`specification/requirements/ASSURANCE.md`, not a separate authority.

| Expectation | Result | Source and reason |
|---|---|---|
| M1: A, Z, model and execution | satisfied | A:7–21 and 123–127 distinguish state/trace domains, required outcome, declared relation and execution conformance. Existing construction clauses retain preservation, progress, termination and satisfaction as separate claims. |
| M2: preservation and composition | satisfied | A:9–19 requires initial conditions, each preservation step, compatible joins and the final implication to Z. Nonsequential composition needs its own law. Approximation needs a bound for the complete composition; local tolerances are not silently composed. |
| M3: upstream test derivation | satisfied | A:25–35 and 58–68 bind interpreted upstream obligations, assertion scope and independent justification, while retaining useful implementation-derived regression claims. The comparison does not invent an owner-issued runtime subject. |
| M4: oracle and observation sufficiency | satisfied for the stated function model; generic coverage falsified by AM-L1 | A:29–54 distinguishes necessary and sufficient claims, sound satisfied/falsified conclusions and observation sufficiency. An all-undetermined checker supplies no completeness claim. The fibre condition does not establish an executable decider. AM-L1 limits the unqualified generic account. |
| M5: mutual assurance and dependence | satisfied | A:62–93 preserves both-wrong agreement, shared causes, disagreement without blame assignment, model-qualified Bayes updating and conditional miss factorisation. Actor diversity is not statistical independence; miss probability is not whole-product correctness. |
| M6: assertion/execution provenance | satisfied | A:25, 45, 60 and 97–113 keep text identity, interpreted meaning, actual observations and evidence applicability distinct. Product criterion 4 and integrated checks consume these requirements. A digest or log does not discharge semantic fidelity or execution correctness. |
| M7: formal claim boundaries | satisfied | A:7, 54 and 123–127 distinguish an obligation, its argument, structural validation, external predicates and bounded execution. The unchanged a_c dependency proof boundary explicitly forbids promoting structural validity to truth or a theorem. |
| M8: impact and evidence reuse | satisfied | A:97–119 separates justification links from validity dependencies; exclusion needs supported non-influence; unknown impact, new obligations and gates retain work. Reused evidence keeps its old subject and gains a justified applicability relation. Full-suite freshness is neither sufficient nor universally necessary. |
| M9: permitted realisations and architecture | falsified only at AM-L1 | A:3, 21, 68, 93, 105, 119 and 123 otherwise preserve tenant representation, human/mixed execution, qualitative assurance and ordinary carriers. No universal probability threshold, proof assistant, graph database, ledger or test cadence is selected. The evaluator model needs the coverage clarification above. |

Consumers inspected include the changed mathematical clauses in Intent, Product,
requirements README, Principles, Capabilities, frame basis, conformance, shared
tenant entry and T-002's seven assurance duties. The six member criteria remain
six; criteria 4/5 and the integrated checks consume the new owner without
claiming that formula text supplies actual-use evidence. The prior categorical
standard and a_c dependency proof claims remain consistent with the new owner.

## Independent Countermodel Checks

Before reading the author return/assets, the reviewer ran small independent
Python calculations with exact rational arithmetic and exhaustive finite
enumeration. They test the distinctions, not universal completeness:

- On Ω = {0,1}², take Q(x,y) = (x=0 and y=0), q(x,y) = (x=0), and π(x,y)=x.
  The case (0,1) passes q while violating Q. Cases (0,0) and (0,1) have the
  same observation and opposite Q values. None of the four Boolean functions
  on the two observations decides Q correctly on all four cases.
- Relations {(0,1)} and {(2,3)} each support their own local contracts but have
  empty sequential composition. A missing join prevents the end-to-end claim.
- In a declared fault-conditional model, mass 1/5 has both checks miss and mass
  4/5 has both detect. Each marginal miss is 1/5, but joint miss is 1/5 rather
  than the unsupported independent product 1/25.
- With prior P(F)=1/10, P(agreement|F)=99/100 and
  P(agreement|not F)=4/5, Bayes gives P(F|agreement)=11/91, greater than 1/10.
  Agreement does not universally increase confidence in correctness.

The frozen requirement correctly refuses the stronger unsupported conclusions
in these examples. AM-L1 was then evaluated when the coordinator separately
requested that the human/probabilistic checker case be tested. That request
introduced no replacement wording and changed no frozen expectation.

## Author-Witness Replay

After the source assessment and independent countermodels, the reviewer read
the exact committed author return, script and recorded output. The 120-line
script performs standard-library computations and prints JSON; it does not
modify repository artifacts. Executing its committed bytes through
`python3 -I -` returned exit 0 with empty stderr and output byte-identical
to the committed `results.json`.

- Script SHA-256:
  `252e745c6a75d7a42294dd7852efcf3ae7ef0836122acfd8cf17a67d933a8b4a`.
- Recorded and replayed output SHA-256:
  `0df91e3b8a14a962d6c177ffa7166caa0344f494cb32458a85bfe1136959d176`.

The replay corroborates 121 histogram inputs, 105 faulty outputs rejected by the
count predicate while all weak key checks pass, observation aliasing, the stated
correlation example and targeted repair with retained sum evidence. The impact
model is declared by the example; the replay does not discover dependencies in
arbitrary programs. The one-input repaired join and finite histogram population
do not qualify a tenant or establish full-domain preservation. The author
return states those limits accurately.

## Limits And Elapsed Time

The activation began at 2026-10-16 00:08:31 UTC. Expectations were fixed at
00:11:15 UTC. Exact successor acquisition began at 00:17:26 UTC, after waiting
for the source freeze. This initial review record was prepared at
2026-10-16 00:23:41 UTC: 910 seconds after activation and 375 seconds after
successor acquisition. Elapsed includes the freeze wait; execution/reading are
not instrumented separately. Full host context, retained context and native token
spend are uninstrumented, so context fit and criterion-4 attention adequacy
remain unassessed.

This is bounded source review plus finite calculations and witness replay.
There was no tenant trial, external paid actor call, categorical steel thread,
statistical calibration or formal proof-assistant run. The review did not
audit every historical admission, every source link or either tenant's full
implementation. It supplies no owner acceptance, cross-family assurance or
release claim. The author owns any correction; only the two granted review
commentary files were changed by this activation, with no source or Git effects.

# Assurance Of Construction

Source: this Product's [Universal Construction Model](../PRODUCT.md#universal-construction-model).

This requirement owns the relationship between construction, assertions, observations and the claims they support. It applies the [universal construction requirement](README.md#universal-construction-requirement) to assurance under finite resources. Foundations own the shared relationships; the Spec Method and profiles bind them to their operations. A tenant chooses their representation and execution within these obligations.

## Preservation Through Construction

A construction declares its starting state A, required outcome Z, governing basis and material assumptions, written Γ. Z is a predicate on acceptable outcomes, including required effects and trace properties where these matter. The following notation states proof obligations; writing an implication does not discharge it.

For a sequence of transformations, let `X_i` be the state or trace domain at boundary i, `F_i ⊆ X_i × X_(i+1)` the declared transition relation, and `P_i` the property to retain or establish there. A claimed preservation step has the form:

```text
For all x, x':  P_i(x) and F_i(x, x')  implies  P_(i+1)(x').
```

The relation accounts for the outcomes, effects and assumptions material to the claim. A relation covering successful completion alone supplies no claim about refusal, failure, interruption or unknown effects. Handling those cases follows the existing result, authority and recovery contracts. The real execution's conformance to the relation is a separate obligation.

An end-to-end preservation argument establishes the initial condition, each step's applicable premises, compatibility at each join, and the connection from the final property to Z. In particular, the preceding postcondition must establish the next precondition or the missing condition must be acquired and justified. Concurrency, alternative branches and external effects require their applicable composition law; a sequential drawing does not establish one. Local success alone establishes neither the joins nor Z. Preservation is distinct from progress, termination and the availability of a suitable next step.

Exact transformations preserve the declared meaning. Approximate transformations state their adequacy relation and an established bound for the complete composition; local tolerances cannot be assumed to add or remain unchanged. Changes to the governing outcome or meaning follow its owner and successor rules.

The algorithmic account states the required operation, the informational account states the meaning and distinctions retained, and the computational binding states how work and observations are realised. Claims across these accounts identify their maps and preservation obligations. Execution by a person, machine or mixed arrangement does not discharge those obligations by itself. A commuting diagram, functor or equivalence claim requires the [categorical demonstration](README.md#categorical-demonstration-standard) appropriate to it.

## Assertions And Observation

For a selected source obligation r, let `Q_r = interpret(r, Γ, Ω)` be its required predicate over a declared domain Ω of cases. A case includes the inputs, behaviour and material environment needed for that obligation. The interpretation retains the obligation's scope, conditions, exceptions and permitted alternatives. A source identifier or digest authenticates the selected text; it does not prove this interpretation faithful.

An assertion targets a predicate `q_t`. The candidate states whether that predicate is the full obligation or a narrower claim. The two directions have different consequences:

```text
Q_r implies q_t                : q_t is a necessary condition of Q_r.
q_t implies Q_r                : establishing q_t is sufficient for Q_r.
(q_1 and ... and q_n) implies Q_r : the stated conjunction is sufficient.
```

These implications are conditional on Γ and Ω. Passing a check of a necessary condition does not establish the full obligation. A conjunction requires its own coverage and compatibility argument; a collection of passing tests does not supply that argument by its count.

Let `π: Ω → O` describe the observations available to a checker and `T ⊆ O × R` its admitted evaluation relation, where R uses the method's [single result algebra](README.md#single-result-algebra-requirement). A deterministic checker is a functional special case. A human or probabilistic checker can admit different conclusions on the same observations; a universal soundness claim covers all admitted conclusions, not a favourable selected run. Here, `indeterminate` names the core judgment whose admissible evidence cannot decide the evaluated predicate; it remains distinct from an evaluation that was not performed. A claim or work item can remain unresolved for either reason; unresolved work is not an additional judgment value. In the following obligations, `sat` and `fal` denote the satisfied and falsified judgments about `q_t`, not new execution states:

```text
For every s in Ω:
  (π(s), sat) in T  implies  q_t(s).
  (π(s), fal) in T  implies  not q_t(s).
```

The candidate identifies what supports each claimed direction and where it is unresolved. A relation admitting both a sound satisfied judgment and an indeterminate judgment need not always decide the case. A restricted deterministic model retains its scope and an actual checker requires its own conformance account. An observed test pass remains an observation when the oracle's fidelity is unestablished; it does not become established satisfaction of the source obligation. The same distinction applies to a reported failure. The observation binding itself needs support: an idealised π does not establish that the instrument, actor or execution acquired the required facts correctly. A probabilistic claim uses its declared distribution over outcomes and the risk contract below; the relation alone supplies no probabilities.

A checker that always decides `q_t` correctly using only π requires:

```text
For all s, s' in Ω:
  π(s) = π(s')  implies  q_t(s) = q_t(s').
```

This states observation sufficiency. If two admissible cases have the same observation but opposite truth values, that observation cannot support a sound complete decision between them. Further evidence, a justified narrower scope or an indeterminate judgment is required. In a classical set model this condition permits a predicate on the image of π; it establishes neither an executable decision procedure nor its cost. Unknown effects and unavailable observations retain their required distinctions from falsehood and from an evaluation that was not performed.

## Parallel Derivation And Mutual Assurance

Construction and assurance can follow different paths from a common obligation. For `requirement → refinement → realisation`, assertions derived from the requirement check its applicable conditions in the realisation; assertions derived from the refinement check its more detailed obligations there. User-acceptance and build-level tests can instantiate these paths. The roles identify the selected sources and subject in this example; they prescribe no stage names or test classes.

The expected result or acceptance predicate has assertion provenance: the owning obligation, interpretation, assumptions, derivation and shared dependencies that give it meaning. Execution provenance identifies the actual checker, exact subject and applicable environment, inputs, observations and result. Both are needed for the claims they support. Execution logs alone cannot establish that the expected answer follows from the requirement.

An implementation-derived test can be useful for regression or a stated local property. Repeating the implementation's decision supplies no independent justification for its fidelity to an upstream obligation. A shorter assertion path can be easier to inspect and execute than construction; that is a supported design claim for the selected path, not a guarantee of correctness, coverage or independence. Valid distinct implementations can produce different outputs within the same acceptable relation; equality of outputs is not always the oracle.

Mutual assurance compares independently justified constructions or assertions within their stated scope. Agreement is compatible with both being correct and with a shared error; disagreement requires diagnosis and does not identify the faulty party by itself. Assurance accounts for shared specifications, interpretations, tools, fixtures, observations, copied material and other material failure causes. Different actors, model families or codebases do not establish statistical independence. Porting retains authorship and common dependencies under [Cross-Synthesis](../PRODUCT.md#cross-synthesis). Repeating evidence does not create a new independent observation.

Agreement with an incorrect common model cannot validate that model against the desired real-world outcome. Validation of the governing expectations uses its declared purpose and external observations through their owners. Proposed corrections preserve counterexamples and follow the applicable change authority.

These relationships are recoverable from the existing sources, bindings and evidence carriers. Shared derivations can be recorded once and applied to a declared family. No new per-test document, parallel ledger, fixed number of reviewers or prescribed provenance format is required.

## Assurance Within A Risk Model

The work authority selects the required assurance for the stated risk, obligations and resource limits. It identifies material failure consequences, coverage and uncertainty, and the conditions for action or acceptance. Additional evidence can strengthen a claim only within its applicability and dependence account. Neither a test count nor an assumed preference for more checks substitutes for that account.

Where quantified assurance is claimed, its model states the population or uncertainty being modelled, prior information, likelihoods, shared causes and calibration limits. For a specified violation event V and evidence event E, Bayes' rule is:

```text
P(V | E, Γ) =
  P(E | V, Γ) P(V | Γ)
  / [P(E | V, Γ) P(V | Γ) + P(E | not V, Γ) P(not V | Γ)].
```

The denominator must be nonzero. E can include agreement, disagreement or other observations; its likelihood under both faulty and non-faulty conditions matters. The formula supplies no missing likelihood or prior. A numerical posterior is no stronger than its model and supporting evidence.

Let `M_i` mean check i misses V under the specified evaluation conditions. The exact joint miss probability factors by conditional probabilities:

```text
P(M_1 and ... and M_n | V, Γ)
  = product over i of P(M_i | V, Γ, M_1, ..., M_(i-1)).
```

Conditional terms require defined conditioning events; zero-probability prefixes are handled without inventing a conditional value. Replacing those terms with `P(M_i | V, Γ)` requires conditional independence under the declared model. The chance of at least one detection is one minus the joint miss probability under those same conditions. It is not the probability that the whole product is correct. Agreement does not necessarily increase confidence when shared causes or newly learned information change the model.

Calibration from sampled cases or injected defects supports only its justified relationship to operational failures. Unsupported numeric confidence remains unresolved; qualitative evidence and stated limits remain usable within the governing policy. The method imposes no universal probability threshold and does not require a probability estimate for every test. Required safety, authority and acceptance conditions cannot be waived by a cheaper assurance plan.

## Change Impact And Targeted Reassessment

Assertion justification and evidence validity are related but distinct dependency relations. The former explains why a check expresses an obligation. The latter identifies what can affect its behaviour, conclusion or applicability, including implementation, shared libraries, data, instruments, environments and governing assumptions. A requirements-to-test link alone is not a complete impact model.

Let Δ be a change to material facts or dependencies, including a newly discovered invalid assumption. Let `I(Δ)` conservatively cover the changed facts and their affected dependents. For each check t, let `D*(t)` cover the transitive dependencies material to its assertion, execution and use of evidence. A candidate selection is:

```text
S_Δ = { t : D*(t) intersects I(Δ) }.
```

The representation is a tenant choice; no exhaustive graph database is required. Excluding a check requires supported coverage of its material dependencies and a reason the change cannot invalidate the intended reused claim. An absent edge is not evidence of non-influence. Unknown impact widens reassessment or leaves the dependent assurance unresolved. New obligations or cases create assessment work even when no existing check covers them. Mandatory gates remain applicable irrespective of this selection.

For a new subject and basis, let `E_old` be the existing evidence records, `E_reassessed` the newly produced evidence from reassessment, and `E_new` the resulting evidence account. Reassessment includes checks selected in `S_Δ`, assessment of new obligations and applicable mandatory gates. Selection alone produces no execution evidence; failed and indeterminate results retain their standing. The account is:

```text
E_new = retain_applicable(E_old, new_subject, new_basis) union E_reassessed.
```

Retention establishes the material validity conditions on the new subject: the claim and scope still apply, its assertion and observation basis remain justified, and affected dependencies are unchanged or covered by an established preservation relation. The original evidence keeps its original subject; a new applicability relation permits its use. A changed hash alone establishes neither invalidity nor equivalence. Known failures, unresolved coverage and their citations remain visible until supported repair, reassessment or an authorised change of obligation disposes them.

If a governing requirement changes, dependent expectations may need authorised revision as well as new execution. A correction in its refinement revisits the affected obligations and their links to both the requirement and the realisation. A correction in the realisation reassesses the affected implementation and integration under the still-applicable obligations. These are semantic dependency boundaries, not fixed file or directory boundaries. Recovery reacquires current reality and invalidates affected claims; it need not erase valid work or rerun every check.

The governing assurance can be established from applicable retained evidence together with new evidence. The completeness of that account is distinct from the freshness of every execution. Selection considers impact-analysis, acquisition, execution and assessment costs together, with anticipated costs distinguished from measurements. The required assurance, risk policy and mandatory gates constrain that optimisation; a cheap selection that leaves a required obligation uncovered is insufficient.

Broad or uncertain impact, a change to the selection model, an applicable release rule or evidence that selection missed a dependency can justify wider testing. Full-suite execution remains an available strategy and may itself have coverage gaps. No universal full-suite cadence follows, and no optimisation removes a separately required gate. Failures feed causal diagnosis and repair before another selected run.

## Formal Representation And Demonstration

The candidate's a_c interpretation represents the material obligations and dependency relationships above under [constraint-surface fidelity](README.md#constraint-surfaces-and-logic-compression). It distinguishes a stated formula, a discharged mathematical argument, mechanically checked structure, an externally assessed predicate and evidence from execution. An external predicate retains the source, scope and evidence required to establish it; an arbitrary truth label does not discharge the obligation. No particular proof assistant, probability library or execution engine is selected.

The candidate demonstrates the applicable positive, negative and unresolved cases in [conformance](../conformance/README.md#assurance-discriminators), including weak assertions, insufficient observations, shared error, and change selection that either retains valid evidence or invalidates affected evidence. Mathematical proof, exhaustive checks of a finite model, sampled tests and observed use retain their distinct scopes. Finite examples do not prove the universal implications above. An unproved universal claim can remain unresolved while bounded construction and assurance proceed where their governing conditions permit them.

Existing member and integrated criteria assess these owners and their consumers. Source semantics, formal fidelity and actual use retain their separate evidence; the common mathematical obligations do not create a seventh criterion or make each test a theorem-proving exercise.

Purpose and material relation: assurance connects construction results to the obligations they support, exposes shared errors, and directs reassessment to affected claims while retaining evidence whose applicability is established.

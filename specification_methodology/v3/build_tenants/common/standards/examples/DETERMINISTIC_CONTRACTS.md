# Deterministic contracts and sufficient observations

These self-contained finite examples apply
[AXIOMATIC_CALCULUS §5](../AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds),
[FOUNDATIONS observation sufficiency](../FOUNDATIONS.md#assertions-and-observation)
and [ACTIVATION results](../ACTIVATION.md#3-step-results-and-disposition).
They select no runtime or mandatory representation. Each fixture's finite
domain, policy and oracle below are its basis Γ. The companion
[Python program](deterministic_contracts.py) exhausts those domains using
only the standard library. Run `python3 -I deterministic_contracts.py` in
this directory. A passing run supplies bounded model evidence; it is neither
independent review nor whole-method qualification.

## Operations and permissions

The examples' reads are their arguments, their model state is explicit, and
their only returned effects are values. Their functions read no clock,
filesystem or mutable global state. The executable harness prints a report;
that reporting effect is outside the modeled functions. The finite bounds
below prove termination independently of observing a successful run.

| Exact traversal | Domain, permission and termination | Complete oracle |
|---|---|---|
| `v_double` | `n∈{0,1,2}`; construction-only grant; one multiplication | Return respectively `{n:0,double:0}`, `{n:1,double:2}`, `{n:2,double:4}`. The value's availability grants no assessment, admission or closure. |
| `v_sorted_full` | Lists of length at most three over `{0,1,2}`; unchanged-subject evaluation; at most two adjacent comparisons | Satisfied iff all adjacent pairs are nondecreasing. Otherwise falsified with the first inversion `{index,left,right}`. `[2,1]` gives `{index:0,left:2,right:1}`. Return a separate witness; an optional witness-log grant may persist it without changing the subject. |
| `v_put_A` | Explicit modeled state `absent/A/B` and grant `allow/deny`; one table lookup | The six cells below specify the returned next state and request/refusal. No physical write is executed. |

| Input state | Allow: next state / decision | Deny: next state / decision |
|---|---|---|
| absent | A / request put_A | absent / refusal |
| A | A / request put_A | A / refusal |
| B | A / request put_A | B / refusal |

The request is a modeled effect proposal, not physical completion. A
denial's evaluated predicate is “this request is authorized”; its
`permission_denied` signature stop maps to falsified. Unknown physical
completion belongs to the actual effect owner's contract. Likewise, under
a construction-only grant, `v_double(2)` establishes candidate availability
only; a separate judgment, admission or closure claim has no supporting
operation or evidence.

Negative evaluation case: sorting `[2,1]` in place and then calling it an
assessment of the original violates the unchanged-subject profile. The
changed list may be a construction output under a construction grant; its
sortedness is not the original list's sortedness. The executable checks
both the mutation and this false attribution. Manual evaluation and mixed
human/software witness logging have the same permission boundary.

## Exhaustion

`v_copy` accepts lists of length at most two over `{0,1}` and fuel in
`{0,1,2}`. It copies one element per fuel unit; only a complete copy is its
candidate. It terminates after at most two copies. `v_sorted` accepts lists
of length at most three over `{0,1}` and the same fuel. It inspects one
adjacent pair per fuel unit, stopping at the first inversion, when every
pair has been checked, or when fuel ends. It terminates after at most two
comparisons. Its declared output is a closed assessment report containing
the exact input/basis, inspected-pair evidence and any residual; such a
report can contain an indeterminate result.

| Selected application and observation | Assessed predicate and result | Work result | Signature and traversal stop |
|---|---|---|---|
| `v_copy([0,1],1)` retains prefix `[0]`, with no complete candidate | Complete copy is available: falsified | `incomplete` → falsified for output availability | `copy_exhausted` maps to falsified, cause fuel ended before the required output |
| `v_sorted([0,1,0],1)` inspects `(0,1)`, with the second pair unexamined | Whole list is sorted: indeterminate on admitted inspected-pair evidence | `candidate_ready` → satisfied for the closed report and transition evidence being available only | `assessment_exhausted` maps to indeterminate, cause performed assessment has insufficient evidence |
| An activated assessing step spends its budget in setup and never invokes `v_sorted` | No assessment result | `incomplete` → falsified for the step's own output availability; the unperformed assessment remains residual work | No traversal application exists and therefore no `v_sorted` judgment or stop exists |

The two declared exhaustion stops have different predicates and parent core
values. Neither maps to satisfied. A report's availability and its assessed
predicate are not one judgment. Lists of length zero or one are sorted
without inspecting a pair. An observed inversion falsifies sortedness even
when later pairs remain unexamined. No result is inferred from a planned
invocation. These are distinct bounded traversals, not totality proofs for
an unbounded operation.

## Continuation-sensitive sufficiency

Fix one subject and the one-assessment policy Γ. States are `U` (unassessed),
`S` (satisfied report), `F` (falsified report) and `I` (indeterminate report).
Inputs are `assess_S`, `assess_F`, `assess_I` and `advance`. From U an assess
input records that report; from any assessed state it is refused as already
assessed, preserving state. `advance` preserves state and is allowed only
from S; it returns `block_unassessed`, `block_falsified` or
`block_indeterminate` from the other states. This is the complete transition
and decision rule for every state/input pair. There is no reset input in Γ.
A different contract can permit reassessment or re-entry.

The weak observation “satisfied assessment exists” maps U, F and I to false
and S to true. U and I nevertheless require incompatible first-assessment
decisions. Thus no decision function over that observation can preserve the
fixed policy. In a human handover, “not approved” similarly fails to say
whether to perform the first assessment or preserve a completed undecidable
assessment and follow its declared continuation.

Define `alpha(U)=(subject,basis,null)` and
`alpha(s)=(subject,basis,s)` for s in `{S,F,I}`, with those subject and basis
fixed by Γ. Define `delta_hat` and `T_hat` by the complete rule above on
these records. Every state/input satisfies
`delta=delta_hat o alpha` (with the unchanged input supplied) and
`alpha(T(s,u))=T_hat(alpha(s),u)`. The readouts “satisfied exists”, exact
standing, permitted first assessment and advance decision are preserved.
The program checks all 16 one-step cells and every length-four input
sequence from every state. Exact one-step preservation with the closed
domain and identical next-state basis also composes by induction to every
finite sequence in this model. Approximate models have no such automatic
bound.

All four states remain distinguishable. This is a sufficiency witness with
no state aggregation, not evidence of compression, minimum context,
cross-task context selection, Markov sufficiency outside Γ, or cheaper
operation. Authority and hold distinctions are exact in this example.

## Qualified references

For this fixture a complete assessed record carries subject, basis,
standing, producer, obligation/version, authority and invalidators. Exact
local keys `report:S`, `report:F`, `report:I` resolve those records. An
independent copy preserves all required fields and the preceding policy
readout. The pointer `candidate-v1` alone maps every report to the same
bytes/identity; S and I then require different continuations, falsifying
its sufficiency for that consumer. Adding a type name alone cannot repair
missing standing.

The fixture assumes exact local key resolution and accessible immutable
records. A hash-based realization would additionally state its collision,
authenticity and access assumptions; no digest alone proves semantic
sufficiency. A manual document reference and a mixed handover can use the
same record and policy without any annotation architecture or event log.

## Finite maps and consumer adequacy

Fix the same subject/basis and reports `X={S,F,I}`. Qualified records are
`H={hS,hF,hI}` and views `V={vS,vF,vI}`. Policy readouts are
`D={advance,block_falsified,block_indeterminate}`. The complete functions are:

| X | `build:X→H` | `view:H→V` | Both `j:H→D` and `h:V→D` read out |
|---|---|---|---|
| S | hS | vS | advance |
| F | hF | vF | block_falsified |
| I | hI | vI | block_indeterminate |

The three rows prove pointwise `j=h o view`. Arrow equality here is pointwise
finite-function equality; composition is ordinary composition and identities
return their inputs. The constant subject-only projection cannot factor j:
hS and hI share its output but require different readouts.

For the structural counterexample, take the finite chain category with
objects X,H,V,D and exactly the displayed generated function for each ordered
pair in that chain, including all identities and composites. There are ten
arrows; equality compares their endpoints and pointwise action. The target
terminal category has object `*` and only `id_*`. Send every source object
to `*` and every arrow to `id_*`: identities and composition are preserved,
yet that map cannot recover j's distinct readouts. The program exhausts
identity and associative composition checks for this bound fragment and
the terminal map. Those structural checks and the explicit counterexample
support their finite claims, not consumer adequacy of an arbitrary functor.
The full categorical demonstration still requires the applicable a_c
representation and supporting assessment under FOUNDATIONS; these executable
tables do not replace those obligations or discharge unresolved H1.

## Migration and comparison

The six finite operations above have explicit closed dependencies, bounded
loops and declared outcomes; their eligibility is witnessed within these
domains. An old evaluator with an undeclared clock dependency or missing
termination evidence fails new-kind qualification despite preserving its
subject. It takes the pending-evidence or unresolved row of
[RELEASE's migration relation](../RELEASE.md#deterministic-kind-migration),
retaining its exact old edition. A future fuel-bounded repair has a distinct
traversal and exhaustion meaning. A kind never grants broader writes.

An optional representation experiment can compare the complete plain-text
record, an equivalent qualified reference, and the insufficient candidate
pointer. Vary retained, absent and stale counterexamples separately, hold
substantive information/access fixed when claiming representation benefit,
and count acquisition, rendering, reasoning, repair and assurance costs at
declared boundaries. The finite examples above test correctness; they supply
no measured architecture or retention benefit.

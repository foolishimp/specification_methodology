STEP S06-P4b-up | cap 20000 bytes | measured 12996 bytes | fits
ROUTES: DESIGN_MODULE_METHOD.md:bounded-frame-conservation-stdo-up-017, SPEC_METHOD.md:complete-enclosing-relation-admission-stdo-up-021
# Step card: FOUNDATIONS §3 route check

You are one bounded step of a larger check. You hold only this card, one or
more paragraphs of a draft standard (the tenant paragraphs, from FOUNDATIONS
§3) and, for each route, the section of the STDO v2.5.1-rc.2 member that the
paragraph cites (the rc.2 section). You cannot acquire anything else and you
have no memory of other steps. The line above this card states the byte size
of your whole input as measured before you were started.

## Task

For each route listed under ROUTES, judge whether the tenant paragraph's
characterisation of the cited rc.2 clause is consistent with the rc.2
section, under this contract. Consistent means all of:

1. nothing the tenant paragraph says about the cited clause contradicts a
   statement in the rc.2 section;
2. the rc.2 section's subject is the subject the tenant paragraph attributes
   to it;
3. where the tenant paragraph states an obligation as the clause's content,
   the rc.2 section states that obligation.

A paragraph that only names the clause as conserved, reframed or superseded
without restating its content is judged on 1 and 2 only; mark it "by
reference". A paragraph that restates content is judged on all three; mark
it "restated". Cross-paragraph relations within the rc.2 section are
material: judge over the whole section as given, never over a summary.

## Result algebra

Return exactly one member per route:

- satisfied: the contract holds on the given text;
- falsified: a statement in the given text defeats it; quote the statement;
- indeterminate: the given text is complete for the route but cannot decide
  it; say why;
- out_of_frame: deciding needs text or a relation not given to you, for
  example a definition in another section; name it;
- invalid_basis: the given material cannot support the judgment, for example
  a paragraph or section is missing or malformed.

Never report satisfied because material is missing or a point seems minor.
Do not shorten, summarise or skip any given text. Do not ask for more.

## Output

Return only these lines, nothing else:

ROUTE <member>#<slug> | <result> | <by reference | restated> | evidence: <one or two quoted phrases from the rc.2 section and the tenant statement they bear on> | residual: <none | text>

one line per route, then one final line:

STEP <step id from the first line of your input> | routes <count> | bytes_seen <the measured byte count from the first line of your input>

===== TENANT PARAGRAPH P4b (FOUNDATIONS §3) =====
P4b Conservation of step-produced facts. Judgments, residuals, observations
and authority decisions the outer contract needs are recorded by the step
that produced them; sources a later step can re-acquire are governed by
sufficiency, not conservation. Derived from P0 with P2 and the
step-produced-facts premise. Reframed from
[AC-009](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-009-residual-conservation),
[AC-013](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-013-transformation),
[AC-005](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-005-authority-conservation),
[UP-017](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017),
[UP-021](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021),
whose nine statements of conservation become one obligation with typed
instances (authority, residual, judgment, frame, transition, successor
claim, evidence by reference); each continues to govern its own scope.

===== RC.2 SECTION DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017 =====
### Bounded Frame Conservation (`STDO-UP-017`)

`M(B)` closes one governed boundary. A bounded local action is taken inside a
frame that derives from other accepted frames, and its lawfulness depends on
relations the acting frame does not itself own.

`Global` and `local` are relative to the selected frame. Each material design
frame must identify:

- the governing frames and accepted relations from which it derives;
- the bounded affected relation set of the proposed action;
- the applicable inherited invariants;
- the authority and composition seams crossing that set; and
- the subordinate frames opened by unresolved material distinctions.

A frame may derive from more than one governing frame. A persistence component
belongs to an entity lifecycle boundary and an operational consistency
boundary; an admission function belongs to a domain transition and a
runtime-authority boundary; a shared callable may be consumed by several
sibling domains without becoming subordinate to one. A single governing frame
is lawful where the structure is genuinely hierarchical, and is not required.
Governing frames form a constraint network for the same reason `M(B)` does.

Every seam crossing the affected set must either include its causally relevant
far-side relation in that set, or state why that relation cannot affect, and
cannot be affected by, the bounded action. This makes the declared set testable
against its own declared seams without requiring a closure algorithm or
recursive expansion through irrelevant relations.

The result is evaluated against every affected governing frame, preserves each
applicable accepted relation, and updates only affected subordinate
projections. A bounded local action conserves governing truth; it does not
rewrite it. A result that changes a governing relation re-enters at that
relation before acceptance.

A subordinate frame opens only when a material distinction cannot be resolved
at the governing altitude. This rule does not require recursively documenting
irrelevant descendants.

This law is false if a change is locally valid inside the selected frame but
violates, duplicates, or silently reinterprets an invariant in any affected
governing frame.

Discovered functionality is evidence about required behavior. It is not yet an
architectural operation. A discovered verb, screen action, endpoint, command,
ticket phrase, or use case shall not be promoted directly into a public
operation identity, peer carrier, module, or implementation function. It must
first be derived through the Ontology.

The required derivation order is:

```text
constitutional functionality
  -> candidate Ontology
  -> logical completeness
  -> whole-family Prime contraction
  -> accepted Ontology basis
  -> Irreducible Architectural Carrier Set
  -> target design and domain, sequence, and state projections
  -> public contract and adapter projections
  -> implementation and test projections
```


===== RC.2 SECTION SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021 =====
## Complete Enclosing-Relation Admission (`STDO-UP-021`)

For a material transition, each admission owner is independently responsible
for deriving and validating the complete enclosing relation from authoritative
inputs. The relation contains every participant and equality join whose
identity, validity, authority, currentness, or transition can affect or be
affected by admission; each crossing seam includes its relevant far side or
authoritatively establishes
that the far side cannot participate. Caller or owner assertions of
completeness, validity, prior admission, or authority do not establish truth.

An owner may consume established facts when their exact subject, basis, scope,
provenance and validity remain applicable to its relation. Their production and
invalidation must be recoverable; an unsupported assertion of prior success is
not such a fact. A function, component, role, conversation or status boundary
alone invalidates none of those coordinates and requires no repeated derivation.
Material mutation, rollback, changed authority or basis, expired validity, and
an actual trust boundary trigger the applicable validation before reliance or
effect. Reuse does not transfer the owner's admission responsibility, omit a
participant or satisfy a separately required independent judgment.

Derivation and validation bind one exact admission-valid authoritative basis
identity through admission. If validity or currentness can advance after
preflight, admission remains conditional on the declared predecessor and
currentness law for that basis or re-enters derivation and validation without
effect. Participating owners bind an equal basis or a design-declared coherent
composite basis; independently valid mixed-basis judgments cannot combine.

Every participant and join is validated before any transition effect. Internal
evaluation order and lawful reuse are implementation-owned, but no participant
subset or nested constituent becomes admitted truth. Admission is one semantic
commit of the complete transition, bound to its exact basis identity; failure
or interruption admits the complete transition or none, never a subset. No realization
mechanism or participant count is prescribed.

Direct and every supported composite or nested boundary preserve this law. A
partial result cannot substitute for an owner's derivation and validation, and
a competing same-scope path cannot establish the transition outside the
governing admission relation. Fresh reconstruction and replay over the same
basis reproduce the enclosing relation, basis identity, and complete outcome
or refusal exactly at semantic altitude.

This law is false if completeness is asserted rather than derived; a relevant
participant, join, or seam is omitted; validation and admission use an
unidentified, stale, or incoherently mixed basis; currentness can advance
without a commit condition or effect-free re-entry; any effect precedes
complete validation; failure or interruption exposes a subset; fresh
reconstruction differs; or competing same-scope authority remains.

### Standing Structural Qualification

Qualification is instantiated for every admission owner and supported boundary
declared by accepted design. Case applicability follows the supported input,
state and operating/threat model. An excluded threat alone cannot create an
acceptance predicate or require defensive work; any proposed scope expansion
returns to its owning authority. Supported malformed inputs, stale state and
effect boundaries retain their required checks:

| Form | Required observation |
|---|---|
| direct | the complete direct relation is derived, validated, and admitted once |
| supported composite / nested | every supported constituent and owning boundary satisfies the same law; unsupported forms have a design-grounded `not_applicable` disposition and no weaker or competing path |
| forged | forged identity, membership, equality, or authority reachable within the supported operating/threat model is refused without effect; exclusion requires its owning authority, not a helper's inability to construct the case |
| ambiguous enclosing relation | unresolved participant, join, seam, or relation identity ambiguity is refused without effect |
| stale / advanced basis | stale input is refused, and basis advancement between preflight and admission causes effect-free re-entry rather than mixed-basis admission |
| incoherent multi-owner basis | owner judgments on bases that are neither equal nor joined by a design-declared coherent composite basis cannot combine and are refused without effect |
| competing same-scope admission authority | an undisposed competing same-scope path cannot establish the transition |
| reconstructed / fresh-process | the same basis reconstructs the same relation, basis identity, and outcome or refusal |
| exact replay equality | replay over the same basis reproduces exactly the enclosing relation, basis identity, and complete outcome or refusal |
| atomic publication failure | after validation succeeds, failure or interruption is observed at every materially distinct commit or publication boundary capable of exposing a subset and followed by fresh reconstruction showing the complete transition or none; named representative observations suffice only under a design-declared dominance/equivalence proof covering the complete partial-failure surface |

For an indivisible commit unit, the atomic test establishes that boundary and
observes failure immediately on both sides. Final-participant validation
failure does not substitute for post-validation atomic-failure evidence. A
standing claim is false if an owner or supported boundary is omitted, a
materially distinct partial-failure boundary lacks an observation or declared
coverage proof, a case uses a weaker helper or manufactured refusal, or fresh
reconstruction does not compare the complete semantic result.

---


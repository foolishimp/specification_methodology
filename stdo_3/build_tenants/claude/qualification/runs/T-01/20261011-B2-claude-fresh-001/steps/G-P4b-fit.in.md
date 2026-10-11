STEP G-P4b-fit | cap 8000 bytes | measured 7765 bytes | fits
ROUTES: AXIOMATIC_CALCULUS.md:ac-009-residual-conservation, AXIOMATIC_CALCULUS.md:ac-005-authority-conservation, DESIGN_MODULE_METHOD.md:bounded-frame-conservation-stdo-up-017
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

===== RC.2 SECTION AXIOMATIC_CALCULUS.md#ac-009-residual-conservation =====
### AC-009 Residual Conservation

Every material uncertainty, omission, translation loss, unresolved boundary,
or unproven relation remains in `X` until an authorized disposition creates an
exact successor model. Absence from a projection is not resolution.


===== RC.2 SECTION AXIOMATIC_CALCULUS.md#ac-005-authority-conservation =====
### AC-005 Authority Conservation

Objects, relations, constraints, latitude, residuals, traversals,
transformations, projections, and judgments retain their declared semantic,
operation, evaluation, and decision authority. Copying, interpreting, encoding,
evaluating, or transporting a record does not transfer authority.


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


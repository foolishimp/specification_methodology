STEP G-P5 | cap 8000 bytes | measured 5888 bytes | fits
ROUTES: REFERENCE_FRAME_METHOD.md:rf-012-closed-results, REFERENCE_FRAME_METHOD.md:rf-014-capability-fit, AXIOMATIC_CALCULUS.md:ac-007-constraint-and-refusal, DESIGN_MODULE_METHOD.md:8-totality-rule
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

===== TENANT PARAGRAPH P5 (FOUNDATIONS §3) =====
P5 Totality. A step can meet a condition outside its context; it cannot
report success on one; so its result algebra carries indeterminate,
out_of_frame and invalid_basis as first-class outcomes and its control model
names the next move. Derived from P0 with the open-world premise and P6.
Conserves
[RF-012](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-012-closed-results),
[RF-014](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-014-capability-fit),
[AC-007](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal),
[Totality Rule](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#8-totality-rule);
RF-012 and AC-007 are restated once in CALCULUS §3 and continue to govern.

===== RC.2 SECTION REFERENCE_FRAME_METHOD.md#rf-012-closed-results =====
### RF-012 Closed Results

Every evaluation returns a member of its declared result algebra. The baseline
result family is:

- `satisfied`: the declared predicate holds on the exact basis;
- `falsified`: a declared counterexample defeats it;
- `indeterminate`: available admissible evidence cannot decide it;
- `out_of_frame`: the evaluation requires an undeclared material relation or
  capability; or
- `invalid_basis`: the subject or basis cannot support the evaluation.

An externally owned compatible extension may refine this algebra while
preserving explicit indeterminate, out-of-frame, and invalid-basis pressure.


===== RC.2 SECTION REFERENCE_FRAME_METHOD.md#rf-014-capability-fit =====
### RF-014 Capability Fit

Frame adequacy includes actor usability. When the material manifold exceeds an
actor's capability envelope, human authority may select another actor, refine
the frame, sequence activations, or provide a lawful compression. The actor may
not silently omit material relations to fit context.


===== RC.2 SECTION AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal =====
### AC-007 Constraint And Refusal

Each constraint names its governed subject, predicate, judgment kind,
latitude, and refusal. A failed, missing, indeterminate, out-of-scope, or
invalid-basis result follows the declared result algebra rather than being
coerced to success.


===== RC.2 SECTION DESIGN_MODULE_METHOD.md#8-totality-rule =====
## 8. Totality Rule

Semantic functions should be total or as close to total as the language and
problem allow.

Preferred shape:

- invalid input is rejected at the boundary
- semantic kernels consume admitted carriers only
- failure is returned in a typed and explicit form when practical

Projects using this method should prefer:

- `Result`-like or closed outcome carriers
- explicit validation stages
- explicit "unsupported" or "rejected" outcomes

Projects using this method should avoid:

- partial functions that assume hidden preconditions
- semantic `.get(...)` fallback chains
- controller code that reconstructs missing truth from defaults

---


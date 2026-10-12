STEP G-P4a | cap 8000 bytes | measured 4484 bytes | fits
ROUTES: AXIOMATIC_CALCULUS.md:ac-016-typed-composition, REFERENCE_FRAME_METHOD.md:rf-010-composition-on-demand
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

===== TENANT PARAGRAPH P4a (FOUNDATIONS §3) =====
P4a Typed composition. Two steps compose only when the first's result type
and judgment satisfy the second's domain and preconditions; composition
retains both identities, intermediate results, judgments, evidence,
authority, provenance and stop states. Independent. Conserves
[AC-016](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-016-typed-composition),
[RF-010](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand).

===== RC.2 SECTION AXIOMATIC_CALCULUS.md#ac-016-typed-composition =====
### AC-016 Typed Composition

Two traversals compose only when the first result type and judgment satisfy the
second traversal's exact domain and preconditions:

```text
F_K2[w] compose F_K1[v]
```

Composition retains both traversal identities, intermediate results,
judgments, evidence, authority, provenance, and stop states. It cannot flatten
probabilistic proposal, deterministic evaluation, and human decision into one
undifferentiated operation. `a_c` prescribes no universal `F_P -> F_D -> F_H`
sequence; each application owns its lawful topology.


===== RC.2 SECTION REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand =====
### RF-010 Composition On Demand

Using several frames does not require composing their internal manifolds.
Composition law is required only when the governing evaluation combines their
internal variables, transports evidence or values across them, or treats their
operations as one material execution relation.

Independently activated evaluations may instead return closed results to one
declared conjunction or decision rule.


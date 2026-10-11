STEP G-P1 | cap 8000 bytes | measured 5980 bytes | fits
ROUTES: AXIOMATIC_CALCULUS.md:ac-017-interpretation-fidelity, AXIOMATIC_CALCULUS.md:ac-018-structural-and-semantic-separation, AXIOMATIC_CALCULUS.md:ac-019-valid-model, REFERENCE_FRAME_METHOD.md:rf-008-overlap-without-identity-collapse
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

===== TENANT PARAGRAPH P1 (FOUNDATIONS §3) =====
P1 Interpretation. Subject, representation and interpretation are distinct;
meaning holds within a declared context through a declared contract.
Independent: with purpose, identity, evidence and authority fixed, two
contracts give one representation two meanings. "Algorithmic" means explicit
and structurally checkable; a semantic decision is lawful only under an exact
decision contract; structural success never establishes fidelity. Conserves
[AC-017](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity),
[AC-018](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation),
[AC-019](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-019-valid-model),
[RF-008](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse).

===== RC.2 SECTION AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity =====
### AC-017 Interpretation Fidelity

Every admitted model record maps to exact subject provenance or is explicitly
identified as model-local content under competent authority. Every evaluated
subject declaration has a retained, omitted, residual, inapplicable, or refused
disposition. Interpretation cannot treat absence as immateriality without a
recorded basis and authority.


===== RC.2 SECTION AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation =====
### AC-018 Structural And Semantic Separation

Structural conformance decides closed syntax, types, identities, references,
bases, and mechanically decidable predicates. Semantic fidelity decides the
meaning and materiality of the interpretation. Structural success is evidence
for semantic review, not a substitute for it.


===== RC.2 SECTION AXIOMATIC_CALCULUS.md#ac-019-valid-model =====
### AC-019 Valid Model

A model `M_b` is a valid model of `a_c` under signature `Sigma`, written:

```text
M_b satisfies a_c[Sigma]
```

only when:

1. `Sigma` and the exact `a_c` basis resolve;
2. every record satisfies AC-001 through AC-009;
3. every claimed closure, projection, overlay, transformation, judgment, and
   composition satisfies its applicable law;
4. interpretation fidelity and residual dispositions bind the exact subject;
5. structural evaluation and semantic acceptance remain distinct and both
   required where claimed; and
6. all evidence, provenance, invalidation, and re-entry coordinates resolve.

A checker may decide the structural subset. No generic checker may claim the
semantic or authority subset unless the model supplies an exact lawful decision
contract for it.


===== RC.2 SECTION REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse =====
### RF-008 Overlap Without Identity Collapse

Frames may share entities, variables, evidence, or coordinates. Shared material
does not establish identical meaning, basis, authority, or result. Every
cross-frame equality or translation used by an evaluation is declared where it
is needed.


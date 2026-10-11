STEP G-P6-fit | cap 8000 bytes | measured 5557 bytes | fits
ROUTES: SPEC_METHOD.md:semantic-evidence-and-projection-separation-stdo-up-008, REFERENCE_FRAME_METHOD.md:rf-006-authority-conservation, REFERENCE_FRAME_METHOD.md:rf-007-semantic-evidence-and-verdict-separation
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

===== TENANT PARAGRAPH P6 (FOUNDATIONS §3) =====
P6 Justification and authority. Definitions, assumptions, observations,
candidate judgments and accepted claims have distinct standing; evidence
supports a claim on a basis; authority permits or disposes within scope;
neither is minted by the other. Independent: a bounded actor satisfying all
else can still take a green label as acceptance. Conserves UP-001,
[UP-008](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008),
[UP-022](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022),
UP-004,
[RF-006](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation),
[RF-007](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation).

===== RC.2 SECTION SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008 =====
### Semantic, Evidence, And Projection Separation (`STDO-UP-008`)

The method distinguishes:

- **semantic basis**: constitutional and accepted-design relations defining
  what a claim means;
- **evidence basis**: exact artifacts, events, logs, tests, and observations
  used to evaluate it; and
- **state projection**: a current view derived from admitted semantic and
  evidence bases.

Evidence change may invalidate a verdict without changing law. Projection
change may invalidate a view without changing semantic truth. Semantic change
requires lawful re-entry and invalidates affected downstream acceptance. A
broad digest may conservatively invalidate review, but it does not prove that
every semantic relation changed.


===== RC.2 SECTION REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation =====
### RF-006 Authority Conservation

A frame carries and applies admitted authority. It does not mint, widen,
transfer, or reconstruct semantic, evaluation, operation, or decision authority
from actor identity, available capability, evidence shape, implementation
reachability, or frame selection.


===== RC.2 SECTION REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation =====
### RF-007 Semantic, Evidence, And Verdict Separation

Semantic law defines what the evaluation means. Evidence supplies observations.
The evaluator applies the declared relation. Where the evaluation performs a
material operation, the existing operation owner supplies the exact grant.
Decision authority disposes the result. A frame declaration keeps these roles
distinguishable even when one actor lawfully performs several of them.


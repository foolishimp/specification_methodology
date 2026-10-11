STEP C-P3 | cap 40000 bytes | measured 15219 bytes | fits
BLOCKS: TENANT SECTION FOUNDATIONS.md#3-commitments, RC.2 SECTION SPEC_METHOD.md#recursive-product-taxonomy, RC.2 SECTION WORLD_MODEL_METHOD.md#entity-cut-construction-law
# Step card: route check of a tenant section

You are one bounded step of a larger check. You hold only this card, one
section of a draft standard (the tenant section) and, for each route, the
section of the STDO v2.5.1-rc.2 member that the tenant section cites (the
rc.2 section). You cannot acquire anything else and you have no memory of
other steps. The line above this card states the byte size of your whole
input as measured before you were started.

## Task

For each rc.2 section given, judge whether the tenant section's
characterisation of the cited rc.2 clause is consistent with the rc.2
section, under this contract. Consistent means all of:

1. nothing the tenant section says about the cited clause contradicts a
   statement in the rc.2 section;
2. the rc.2 section's subject is the subject the tenant section attributes
   to it;
3. where the tenant section states an obligation as the clause's content,
   the rc.2 section states that obligation.

A tenant section that only names the clause as conserved, reframed or
superseded without restating its content is judged on 1 and 2 only; mark it
"by reference". A tenant section that restates content is judged on all
three; mark it "restated". Cross-paragraph relations within the rc.2
section are material: judge over the whole section as given, never over a
summary. Judge only the sentences of the tenant section that concern the
cited clause; the rest of the tenant section is context.

## Result algebra

Return exactly one member per route:

- satisfied: the contract holds on the given text;
- falsified: a statement in the given text defeats it; quote the statement;
- indeterminate: the given text is complete for the route but cannot decide
  it; say why;
- out_of_frame: deciding needs text or a relation not given to you, for
  example a definition in another section; name it;
- invalid_basis: the given material cannot support the judgment, for example
  a section is missing or malformed.

Never report satisfied because material is missing or a point seems minor.
Do not shorten, summarise or skip any given text. Do not ask for more.

## Output

Return only these lines, nothing else:

ROUTE <member>#<slug> | <result> | <by reference | restated> | evidence: <one or two quoted phrases from the rc.2 section and the tenant statement they bear on> | residual: <none | text>

one line per route, then one final line:

STEP <step id from the first line of your input> | routes <count> | bytes_seen <the measured byte count from the first line of your input>

===== TENANT SECTION FOUNDATIONS.md#3-commitments =====
## 3. Commitments

P0 Bounded construction. A finite actor realises a selected outer contract
through steps. Each step's selected context fits the actor's envelope. The
actor's internal path within a step is its own. Recovered as a composite;
the generic statement is reframed from the ODD profile's graph functions.
Premises: a selected outcome (P2); the actor of one step need not be the
actor of the next and may re-acquire declared sources but not private
memory; step-produced facts are not re-acquirable; the world is open; a
step's output is a candidate until evaluated.

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

P2 Purpose. A selected outcome defines adequacy; interfaces inherit material
obligations from the transformation they serve; an obligation with no route
to the outcome is unjustified. Independent: identical capacity serves
opposite purposes. Conserves UP-013,
[UP-014](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014),
[UP-005](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005).

P3 Identity. An object's identity is declared (authority, kind, value) and
survives admissible change; current state, historical observation and
representation identity stay separate; a boundary is a claim with a proof
obligation. Independent: equal capacity admits identity by persistence or by
digest. Conserves AC-002, AC-014, the
[recursive Product taxonomy](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#recursive-product-taxonomy),
[Entity Cut Construction Law](stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md#entity-cut-construction-law).

P4a Typed composition. Two steps compose only when the first's result type
and judgment satisfy the second's domain and preconditions; composition
retains both identities, intermediate results, judgments, evidence,
authority, provenance and stop states. Independent. Conserves
[AC-016](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-016-typed-composition),
[RF-010](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand).

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


===== RC.2 SECTION SPEC_METHOD.md#recursive-product-taxonomy =====
## Recursive Product Taxonomy

`SPEC_METHOD.md` owns this taxonomy in the recursive-product bounded context
`urn:stdo:bounded-context:recursive-product-taxonomy` under the selected
complete STDO basis.

Software is recursive and compositional.

A released product may be used to build:

- the next released version of itself
- a dependent product
- downstream project artifacts

Most taxonomy drift in recursive software systems comes from collapsing these
roles into one overloaded word such as `product`.

This methodology therefore distinguishes:

- **Substrate** (`urn:stdo:concept:recursive-product-taxonomy:substrate`): a
  lower product or runtime used to build other products;
- **Development Product**
  (`urn:stdo:concept:recursive-product-taxonomy:development-product`): the
  role of one exact Install of a released Product while that Install acts as
  builder substrate for a Source Project. The role creates no new Product
  identity and transfers no meaning or authority from the builder to the
  Product being authored;
- **Source Project**
  (`urn:stdo:concept:recursive-product-taxonomy:source-project`): the mutable
  workspace building the next release cut;
- **Release Cut**
  (`urn:stdo:concept:recursive-product-taxonomy:release-cut`): one immutable
  annotated RC boundary over a published feature set;
- **Product** (`urn:stdo:concept:recursive-product-taxonomy:product`): the
  released immutable thing resulting when that release cut is accepted;
- **Install** (`urn:stdo:concept:recursive-product-taxonomy:install`): a
  stamped workspace instance of that released product;
- **Artifact** (`urn:stdo:concept:recursive-product-taxonomy:artifact`): any
  published output built by a source project or by a configured installed
  product; and
- **Product Definition**
  (`urn:stdo:concept:recursive-product-taxonomy:product-definition`): the
  present-tense source-project authority surface conventionally carried by
  `PRODUCT.md`; it defines the current product `WHAT` for decomposition and is
  not the released Product artifact.

The governing rules are:

- do not call a mutable source workspace a product
- when a released Product acts as builder substrate, bind the exact Install as
  a Development Product without confusing it with the Product being authored
- do not confuse an immutable RC release cut or installed product with the mutable source
  project building the next cut
- `PRODUCT.md` is the product-definition surface of a source project, not the
  released product artifact itself
- products may depend on other products
- installed products may build the next version of themselves or other products

The compiler analogy is the intended model:

`bootstrap source -> release P0 -> install P0 -> use P0 to build source for P1 -> release P1`

This taxonomy is load-bearing.

If it is blurred, dependency and self-hosting errors compound quickly and are
expensive to unwind.

---


===== RC.2 SECTION WORLD_MODEL_METHOD.md#entity-cut-construction-law =====
## Entity Cut Construction Law

Entities are recovered, not invented. A builder project constructs an entity
cut by trawling authoritative source surfaces for the boundaries the operating
model already commits to, then qualifying them into published truth.

### Admissibility

An entity cut is admissible when its identity, boundary, authority, state,
evidence, treatment, covariance, and ambiguity are explicit, traceable, and
discriminated from plausible alternatives at evidence altitude proportional to
the claim.

That is the whole constitutional test. It binds what must be true of a
published cut. It does not prescribe how a builder establishes it.

"Explicit" admits three lawful values on every surface: a stated value, stated
absence, or stated non-applicability with its reason. A cut whose entity has no
adjacent-domain treatment says so; it does not manufacture one. This keeps the
predicate whole without adding evidence machinery.

Sparse first publication remains lawful. A unique, historical, single-context,
inaccessible, or regulated entity is publishable when the above holds and its
residual ambiguity is declared. Absence of a comparison population, of repeated
contexts, or of permission to intervene is a bound on evidence altitude to be
stated, not a bar to publication.

### Discrimination

"Discriminated from plausible alternatives" means the cut states why this
boundary rather than a nearby one the operating model would treat differently.
The claim carries its own discrimination; a stronger claim needs stronger
discrimination.

Techniques that serve this, none of them mandatory and none of them exhaustive:

- **cross-context invariance**: separate what holds wherever the entity appears
  from what a particular context adds, where multiple contexts exist
- **null-peer comparison**: name a structurally similar entity the operating
  model treats differently, and state what separates them
- **adjoint round-trip**: interpret the entity through an adjacent domain's
  treatment surface and back through its adjoint mapping, and show the identity
  claim survives
- **transplant**: show what a neighbouring entity would have to acquire to be
  treated as this one
- **coat stripping**: vary or remove contextual claims and show identity
  survives; vary an identity claim and show it does not

The adjoint round-trip performs, at semantic altitude, the discrimination the
geometric boundary test performs in a representation space. Where a builder can
intervene, interventional evidence discriminates more strongly than declarative
evidence, and a cut should say which kind it rests on.

Boundary is interventional in character, not structural. A cut that states its
boundary only as a set of source fields has made a weaker claim than one that
states the reinterpretations under which identity survives, and should be read
as such.

### Publication

A published entity cut makes the eight admissibility surfaces — identity,
boundary, authority, state, evidence, treatment, covariance, and ambiguity —
visible and traceable, each as a stated value, stated absence, or stated
non-applicability, and records the basis on which identity was discriminated.

Cuts are immutable. Revising identity or boundary produces a new cut that
supersedes the prior one.

Concrete carriers, layouts, schemas, and storage topology are consumer
realization. This method requires that the published surfaces survive; it does
not select the form they are stored in.


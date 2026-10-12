# ASSURANCE

Tier 2. Owns the assurance and testing law of the method: the verification
layers of the chain, the testing strategy taxonomy with its two proof
authorities and its fixture and proof portability rule, test authority,
scenario bundles, installed dev proof and significant path coverage.
Consumes [FOUNDATIONS](FOUNDATIONS.md) (claim, evidence, judgment,
authority), [EVALUATION](EVALUATION.md) (claims, separation, independent
assessment, acceptance, conformance) and [ACTIVATION §3](ACTIVATION.md)
(the result algebra); adds no definition to tier 1. The particular
method's chain and change classes are [SPEC_METHOD](SPEC_METHOD.md); the
project's bindings are [PRODUCT_DEFINITION](PRODUCT_DEFINITION.md). Later
members add to this one without changing what is here: the Executive
baseline's testing frames and interface-integration law, the design
profile's module-derived unit-proof law (its 6A to 6C) and the ticket law's
test-case authority each land in a section of their own when their member
is activated; this text pre-empts none of them. Every clause names the
principle that requires it (P0 to P6, FOUNDATIONS §3). A route written
`rc.2 #anchor` is into
`stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md` and is provenance
only; under the standalone successor requirement every predecessor row
received here is restated in full in this text, and nothing here depends
on that cut to be applied.

## 1. Verification layers

Each layer of the chain (SPEC_METHOD §1) preserves a distinct kind of truth
(P2, P6; rc.2 #verification-layers):

| Layer | What it preserves | Primary question answered |
|---|---|---|
| Requirements | invariant truth | what must be true? |
| Design | structural choice | how is that truth realised? |
| Scenarios | operational meaning | can the realised system actually do the claimed thing? |

Without scenarios a capability can appear covered because the words exist
in requirements and design. Scenarios force the sharper question: can the
product really do the thing? A requirement can name a reusable composable
unit and a design record can describe the types that realise it, but only
a scenario asks whether a user can build such a unit and apply it twice
(P6).

Scenarios are the product-owner layer: concrete, end-to-end use cases that
validate the chain from intent to realised behaviour. When a scenario
cannot be written, the capability is not yet real. When a scenario fails,
the gap is between the system's actual behaviour and its claimed
capability, not between the specification's words and its other words (P2,
P6).

Scenarios do not replace requirement categories. They primarily validate
capability claims and other behaviour with concrete operational meaning.
Constraints, governance rules and verification-infrastructure requirements
may require different evidence in addition to, or instead of, end-to-end
scenarios (P2).

## 2. Testing strategy taxonomy

This member owns the product-assurance bounded context,
`urn:stdo:bounded-context:product-assurance`, under the selected complete
STDO basis, and within it the Product-level test-authority taxonomy.
Module-derived unit-proof law stays owned by the design profile (the
DESIGN_MODULE member); the shared context does not merge the two authority
sources (P6; rc.2 #testing-strategy-taxonomy).

Every executable proof surface declares its authority source (P6). For
ticketed work the immediate proof authority is the admitted ticket and its
triage path: tests derive from the ticket's lawful re-entry point
(SPEC_METHOD §4) and from the governing constitutional or realisation-law
surfaces it cites; they never derive expected results from current
implementation behaviour (P6, P2).

Authority source is not execution breadth. A test may be small or broad,
fast or slow, deterministic or live, and still derives from one of two
primary authorities (P6, P1):

1. design or module conformance tests; and
2. UAT, or acceptance, tests.

Design or module conformance tests derive from realisation authority: the
governing design, module ownership, the carrier inventory the design
declares (the design profile's interface-and-carrier set or an
equivalent), structural carrier diagrams where present, and boundary-local
fail-closed law. They answer one question: did the implementation realise
the module or design boundary correctly? Unit tests are design or module
conformance tests. Module integration tests, negative tests and
fail-closed tests may also be, when their proof target is a designed module
boundary rather than a user scenario (P6).

UAT or acceptance tests derive from constitutional user or product
authority: requirements, acceptance criteria, declared scenarios or use
cases, and product-level release or qualification claims. They answer one
question: does the composed product satisfy the claimed requirement or
scenario? (P6, P2)

Under this method only sandbox tests, or an explicitly equivalent isolated
composed-product proof lane, may be called UAT or acceptance tests. A
sandbox test exercises the deployed, installed or otherwise runnable
product form through declared application, public, runtime or control
surfaces, and is driven by a requirement-sourced scenario or acceptance
case. Direct source-level unit tests, helper tests and module integration
tests may be valuable proof; they are not UAT and cannot close user
acceptance by themselves (P6; EVALUATION §1, the weaker property never
substitutes for the claimed one).

Sandbox UAT has two lawful execution modes (P6, P1):

- harnessed sandbox UAT exercises the full composed product path with a
  deterministic, fake, recorded or injected worker or result surface; and
- live sandbox UAT exercises the full composed product path with a real
  configured worker, tool, agent, service or other external probabilistic
  transport where the product depends on that live boundary.

Harnessed sandbox UAT proves composition, orchestration, control,
projection, archive and scenario wiring without relying on live
probabilistic execution; it is the lane for deterministic reproducibility.
Live sandbox UAT proves that the same scenario can cross the real external
probabilistic boundary and return evidence through the declared result,
evaluation, provenance and projection surfaces. Where a product or release
claim depends on live probabilistic compute, semantic green, unit green,
module-integration green and harnessed-sandbox green are necessary and not
sufficient for live acceptance (P6, P5).

Terminology (P1):

- `unit` names module or design conformance scope, not user acceptance;
- `integration` names execution breadth, not authority source;
- `sandbox` names composed-product acceptance execution;
- `harnessed`, `fake`, `recorded` or `deterministic` name non-live sandbox
  execution; and
- `live` is reserved for real external worker or transport execution; a
  status projection named "live" is not live UAT unless it crosses that
  real boundary.

A project that uses other local filenames or runner labels still maps each
executable lane back to this taxonomy before claiming closure (P1, P6).

### Fixture and proof portability

Required closure lanes are reproducible from the declared source boundary
(P3, P6; rc.2 #fixture-and-proof-portability-rule). A unit, semantic or
module-design conformance lane does not depend on an undeclared local path,
a sibling workspace, an operator home directory or a mutable external
fixture.

Where a proof needs external project evidence, one of these holds:

- a minimal fixture is checked into the source boundary;
- a fixture manifest declares the external source, version and
  acquisition or binding rule; or
- the test is classified as harnessed sandbox, live sandbox, reference
  comparison or optional local evidence rather than required semantic
  closure.

A missing external fixture fails with a governed diagnostic that names the
fixture authority and the lane; it never masquerades as a product semantic
failure (P5, P6).

## 3. Test authority

Every live requirement has written test-case authority (P6; rc.2
#test-authority-rule). That authority may include scenario bundles,
ordered test-case sequences, negative or control cases and other explicit
evidence cases appropriate to the kind of truth being proved; it exists in
written form and is traceable. No live requirement is fully proved on
informal operator confidence, ambient habit or an unlabelled test corpus
(P6; EVALUATION §5, green labels are not acceptance).

## 4. Scenario bundle

Features are not proved by isolated assertions alone. Where a requirement
claims meaningful system behaviour, the proving surface is a scenario
bundle or an equivalent ordered set of test cases that exercises that
behaviour through a coherent sequence rather than as disconnected
fragments (P2, P6; rc.2 #scenario-bundle-rule).

A scenario bundle shows the feature or use-case boundary being exercised,
the test-case sequence that proves it, and the outcomes expected at each
significant step. It is the layer that makes operational meaning
inspectable (P6).

Declared scenarios and use cases are not downstream decoration. They put
pressure on feature intent and design decisions by forcing the project to
name the real operational boundary, sequence, actors, controls and
expected outcomes that matter. For that reason they are also the best
source for identifying the significant code and control paths the proving
surface must exercise (§6; P2).

## 5. Installed dev proof

Where a system has an installable or runnable development form, the
decisive proving lane runs against an installed development version as if
it were an independent project or an externalised target, not only against
the source tree in place (P6, P3; rc.2 #installed-dev-proof-rule). That
proof prefers a fresh sandbox or equivalent isolated environment, an
installed or built development artifact, and execution through the same
declared entry, control and runtime surfaces the real product uses. Direct
source-level or unit-level checks may stay useful; they do not replace
installed-dev proof of the system under test (P6; SPEC_METHOD §6 for the
install and development-product roles).

## 6. Significant path coverage

The proving surface declares and exercises the significant paths for the
behaviour being claimed (P6, P2; rc.2 #significant-path-coverage-rule).
Exhaustive proof does not mean every possible branch in every file; it
means the project names the meaningful paths and proves them
intentionally. The significant paths usually include, where relevant:

- the intended success path;
- the fail-closed or rejection path;
- the boundary or control path;
- the integration, dispatch or transport path; and
- the recovery, retry or replay path.

If the significant paths are not declared, scenario coverage cannot be
judged. If they are declared and not exercised, the behaviour is not fully
proved (P6; EVALUATION §1, a claim's scope cannot exceed its evaluated
evidence).

## 7. Source dispositions

Rows received by this member. Anchors are into rc.2 SPEC_METHOD.md; a
locus is a section of this file. Every row is restated in this member's
own text; a route is provenance only. Rows of other predecessor members
that land here (the baseline's testing frames, the design profile's 6A to
6C, the ticket law's test-case authority) are disposed at their members'
activations and listed here then.

| Anchor | Disposition | Locus |
|---|---|---|
| #verification-layers | conserved; the predecessor's example ("compositional graphs", "Fragment types", "a reusable discovery workflow") is generalised to a reusable composable unit, since the example named a profile's subject and the law does not depend on it | §1 |
| #testing-strategy-taxonomy | conserved in full: both authority sources, the sandbox-only rule for UAT, the harnessed and live modes, the necessary-not-sufficient rule and the terminology list; the owner of the product-assurance bounded context is this member rather than SPEC_METHOD; `DESIGN_MODULE_METHOD.md` is carried as the DESIGN_MODULE member and "IACS" as the carrier inventory the design declares | §2 |
| #fixture-and-proof-portability-rule | conserved | §2 Fixture and proof portability |
| #test-authority-rule | conserved | §3 |
| #scenario-bundle-rule | conserved | §4 |
| #installed-dev-proof-rule | conserved | §5 |
| #significant-path-coverage-rule | conserved | §6 |

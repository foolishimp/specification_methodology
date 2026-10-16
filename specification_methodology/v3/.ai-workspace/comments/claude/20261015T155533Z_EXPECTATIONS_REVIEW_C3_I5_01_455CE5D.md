# Expectations for the review of C3-I5-01 at `455ce5d`, recorded before opening it

Subject to be opened: the common specification at `455ce5d` ("Add universal
construction model to v3 common specification"), recorded as C3-I5-01 at
`1c18117`, with Codex's nonauthor working review recorded at `b16faca`.
Read so far: the commit list, the diff stat (seven specification files,
94 lines in, 19 out), the first 25 lines of Codex's review, and the
T-001 lines that quote the product owner's direction ("given my current
v3 principles i4 -> i want to add this universal construction model"). Not
yet read: any changed line of the specification, Codex's findings, the
snapshot.

Standing: I am the Claude tenant's builder, an interested party, and the
author of parts of the iteration 4 comparison and port-review policy.
This is a review of the frozen commit for blocking defects and for its
effect on the running iteration 4 builds; it is not an acceptance.

What I expect to find, fixed now:

| Id | Expectation |
|---|---|
| E1 | The construction model is an addition that synthesises the existing principles P1 to P6 and does not change the meaning of any of them, the ten pillar contributions, the six member criteria, the three closure checks, the single result algebra, Cross-Synthesis or Candidate Comparison. Where it touches those, the change is stated as a change, with a reason |
| E2 | It separates, as the owner's direction and Codex's summary say, lawful transformations (the calculus), the chosen outcome (the specification), strategy (selecting a path), execution (changing reality) and evidence (whether the result satisfies the outcome); a lawful sequence may remain incomplete or unsuccessful; a conditional proof stands under its stated assumptions |
| E3 | Feedback, bug correction, finite resources and recursive progress are placed under existing owners (intake triage and change classes, the limits paragraph, the categorical construction sequence) rather than creating a second owner for any of them |
| E4 | Every new obligation names its owner and its re-entry point; every new discriminator in `conformance/README.md` names the member obligation it tests and does not add a candidate-text predicate to criterion 5 |
| E5 | The model asserts no categorical, control-theoretic or other external theorem as established; where it leans on one, it says what demonstration is owed and by whom |
| E6 | The 18 snapshot hashes and byte counts reproduce from `455ce5d`; every link added since `3c4c503` resolves |
| E7 | The text says, as Codex's message does, that I4 remains the ratified tenant basis: the I4 builds, their freezes and the Stage 3 and 4 comparison are unchanged by I5, and I5 becomes a tenant input only through a later admission |
| E8 | No proposal is presented as accepted; no acceptance, merge, release or adoption is claimed |

Possible findings, if the expectations fail: a second owner for feedback
or bug handling beside SPEC_METHOD-level triage; a new result value or a
new standing for conditional proofs that bypasses the core algebra; a
discriminator with no owner; an external theorem cited as law; a change
to the comparison or eligibility rules under the heading of a model.

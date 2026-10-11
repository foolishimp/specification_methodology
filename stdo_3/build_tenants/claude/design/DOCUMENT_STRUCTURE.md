# Claude Tenant Design: Document Structure

Status: tenant HOW for the STDO 3 document set, C3 construction, branch
`tenant/claude/c3`. Not common WHAT; not accepted. Builder basis
`stdo://releases/v2.5.1-rc.2/`, manifest `3d860ff4…2782`. Common inputs:
`C1-inputs-20261011-03` at input commit `80b46944f1c1`, verified at activation.

Governing inputs: the common [Intent](../../../specification/INTENT.md),
[Product](../../../specification/PRODUCT.md), the common principles
[questions](../../../specification/requirements/PRINCIPLES.md), the tentative
[capability questions](../../../specification/requirements/CAPABILITIES.md),
the [conformance discriminators](../../../specification/conformance/README.md)
and this tenant's accepted C1 realisation
[design/PRINCIPLES.md](PRINCIPLES.md) (`28c9b127…b7ec`).

## Purpose of the realisation

A finite actor, human or model, should recover from these documents what it
needs to do bounded governed work with less interpretive reconstruction than
the 2.5.1 corpus requires, and nothing the 2.5.1 corpus requires should be
lost without an explicit disposition. Every clause therefore carries two
things: the principle that requires it, and its disposition relative to the
rc.2 clause it conserves, reframes or supersedes.

## Tiers and files

| Tier | File | Carries | Requiring principles |
|---|---|---|---|
| 1 | [FOUNDATIONS.md](../standards/FOUNDATIONS.md) | ontology, the commitments as law, the algebra of composition and conservation, hypotheses | P0–P6 |
| 1 | [CALCULUS.md](../standards/CALCULUS.md) | the bounded step: intake, context construction under an envelope, grant, output; the result algebra; totality dispositions; refinement; work state and restart; cost and proportionality; reuse | P0, P4b, P5 |
| 1 | [EVALUATION.md](../standards/EVALUATION.md) | claims, evidence, independent assessment, review results, acceptance, conformance of realisations, method self-qualification and recoverability | P6, P1 |
| 2 | [SPEC_METHOD.md](../standards/SPEC_METHOD.md) | the particular method: constitutional chain, one WHAT and tenant HOWs, outcome conservation, change classes and re-entry, activation roles, checkpoints, release lineage | P2 with the tier-1 documents |
| 2 | [CONFORMANCE.md](../standards/CONFORMANCE.md) | the counterexample and trial cases the method must pass, with independently specified expectations | P6 |
| 3 | [PROFILES.md](../standards/PROFILES.md) | how software design, graph execution, UX and world-model profiles import the core and what stays out of it | P0 boundary |
| route | [README.md](../standards/README.md) | learn, apply, review and machine routes; document map | recoverability (derived from P0) |

Seven files. The 2.5.1 corpus has 52 standards members; the contraction is
by import and derivation, not by dropping obligations. Glossary and compressed
views are derived from these files later, never authored separately.

## Derivation map

| Mechanism | Document | Derived from | rc.2 disposition |
|---|---|---|---|
| Bounded activation with intake, grant, territory | CALCULUS §1 | P0, P6 | UP-020 conserved; RF engagement functions conserved |
| Context construction under an envelope | CALCULUS §2 | P0 | AC-010/011, RF-002/003/004/014/017 conserved; the operation that joins them is new |
| One core result algebra with declared refinements | CALCULUS §3 | totality (P0, open world, P6) | RF-012 and AC-007 conserved, restated once (T1.2); work result, UP-020 dispositions, ambiguity outcomes conserved as refinements |
| Faithful refinement A → B → … → X | CALCULUS §4 | P0, P4 | ODD graph functions generalised; UP-017/021 conserved |
| Work state, resumption and restart | CALCULUS §5 | P0, P5 | UP-020 checkpoint clause conserved; generic work state, reconciliation of uncertain effects and non-idempotence new |
| Proportionality and selected cost | CALCULUS §6 | P0, P2 | UP-014, UP-019, UP-005 conserved |
| Independent assessment with freeze | EVALUATION §3 | P6, probabilistic construction | UP-007, UP-022, RF-007 conserved |
| Conformance of realisations | EVALUATION §6 | P1, P6 | reconstruction litmus and UP-022 conserved |
| Recoverability of the method's documents | EVALUATION §7 | P0 with actor change | RF-013, UP-018, Method Self-Qualification conserved; the benchmark is new |
| Constitutional chain, one WHAT and tenant HOWs | SPEC_METHOD §1–2 | P2 | constitutional chain, ambiguity governance, reconstruction litmus conserved |
| Outcome conservation | SPEC_METHOD §3 | P2 | UP-013 conserved |
| Change classes and re-entry | SPEC_METHOD §4 | P4b, P2 | SPEC_METHOD change classes and TICKET triage conserved; carrier choice reframed as HOW |
| Successor dispositions | SPEC_METHOD §6 | P3, P6 | UP-015 conserved; applied to this corpus |

## Steel threads

Each thread freezes a document increment, encodes it in a_c, and has a fresh
actor use it against a CONFORMANCE case under independent assessment.

| Thread | Increment | Discriminating case | State (2026-10-11) |
|---|---|---|---|
| T1 | FOUNDATIONS, CALCULUS §1–3, EVALUATION §1–4 | an activation whose required basis exceeds a declared context cap; a coupled case that cannot fit; the result is refinement or a truthful out_of_frame, never omission | first fixture run twice and reviewed; T1.2 frozen (`cee1157`), encoded, run twice under CASE-2 (`eb9b935`); unassessed |
| T2 | SPEC_METHOD, CALCULUS §4–7 | two bounded results join under an outer contract; a detected failure and an uncovered obligation both survive | frozen (`97f1259`), encoded, run twice under T-03-04 (`f33e6ae`); unassessed |
| T3 | EVALUATION §5–8, CONFORMANCE complete, PROFILES | an interrupted construction resumes over current work state with an uncertain external effect; no blind repetition | frozen (`c539daa`), encoded, run twice under T-05; unassessed |
| T4 | README route, a_c program for the set, recoverability trial against 2.5.1 as baseline | a fresh actor recovers a bounded activation from the documents; fidelity and reconstruction cost measured | frozen, encoded as the set program, trial R-01 run; unassessed; see `qualification/RETURNS.md` for commits |

The C3 build pass constructed the seven files as a first complete draft so
that T1 could be cut from a whole, not from fragments; the threads then
revised them, each after the author's pre-freeze route check by fresh step
actors. Authored documents are not steel-thread execution; execution is the
cases' runs, and nothing is passed until an independent assessor says so.

## Proof plan

Per document: links and `stdo://` fragments resolve; every clause has a
requiring principle and an rc.2 disposition; no profile term (HoG, ledger,
worksite, edge, Markov overlay, F_D/F_P/F_H as names) appears in tier 1 or 2
except in a disposition table or the hypotheses list, which names the Markov
construct in order to exclude it from law. Per thread: a_c program validated with `ac.py`
against the pinned Axiom Indexer subject; a conformance case run with the
author withheld; an independent review reading the branch at a named commit.

## Cost

Declared for this build pass: 150,000 generated tokens, 4 hours wall. Start
2026-10-11T09:35:30Z. Spend reported in `qualification/RETURNS.md` with wall
time by `date -u`; token counters are unavailable on this host and are
recorded as such. Selected because the pass's governed question is whether a
whole-corpus draft fits one bounded activation.

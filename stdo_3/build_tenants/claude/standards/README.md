# STDO 3 Standards (Claude tenant realisation)

Status: C3 draft of the Claude tenant's document realisation. Not released,
not installed, not common WHAT. Builder basis `stdo://releases/v2.5.1-rc.2/`.

STDO 3 is a specification methodology for construction and evaluation by
actors with finite context, attention, time and capability. Its core
statement: interpret a scoped subject; select a purpose and governing
contract; transform within admitted authority while conserving its material
relations; evaluate the resulting claims; continue, recover or conclude from
current state under explicit uncertainty.

## Routes

| You want to | Read, in order |
|---|---|
| understand the method | [FOUNDATIONS](FOUNDATIONS.md) → [CALCULUS](CALCULUS.md) → [SPEC_METHOD](SPEC_METHOD.md) |
| do a bounded piece of work | [CALCULUS §1–3](CALCULUS.md) for the step and its result algebra, then [SPEC_METHOD §4](SPEC_METHOD.md) for where your change re-enters |
| review someone's work | [EVALUATION](EVALUATION.md), then the [CONFORMANCE](CONFORMANCE.md) case nearest your subject |
| decide acceptance or release | [EVALUATION §5](EVALUATION.md), [SPEC_METHOD §6](SPEC_METHOD.md) |
| apply the method to code, graphs, UX or world models | [PROFILES](PROFILES.md) |
| load it into a model's context | the T2 program and its two projected frames under [../a_c/t2/](../a_c/t2/README.md) for FOUNDATIONS, CALCULUS, EVALUATION §1–4 and SPEC_METHOD; the T1.2 program under [../a_c/t1/](../a_c/t1/README.md) is its frozen predecessor; EVALUATION §5–8, CONFORMANCE and PROFILES have no program yet |

## Documents

| File | Tier | Owns |
|---|---|---|
| [FOUNDATIONS.md](FOUNDATIONS.md) | 1 | ontology, commitments, algebra, hypotheses |
| [CALCULUS.md](CALCULUS.md) | 1 | the bounded step, result algebra, totality, refinement, work state, cost, reuse |
| [EVALUATION.md](EVALUATION.md) | 1 | claims, evidence, assessment, acceptance, conformance, self-qualification |
| [SPEC_METHOD.md](SPEC_METHOD.md) | 2 | the particular method: chain, WHAT/HOW, outcomes, change classes, roles, checkpoints, lineage |
| [CONFORMANCE.md](CONFORMANCE.md) | 2 | cases the method must pass |
| [PROFILES.md](PROFILES.md) | 3 | profile imports and the core boundary |

Each clause names the principle that requires it (P0–P6, defined in
FOUNDATIONS) and, where it conserves, reframes or supersedes an rc.2 clause,
that clause's route. A reader needing the rc.2 wording follows the route; the
rc.2 cut remains the operative builder until STDO 3 is released.

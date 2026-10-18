Historical: this set binds earlier member bytes and is not current; the current interpretation is [../i3/](../i3/README.md).

# T1 a_c Interpretation (Claude tenant)

Status: the T1.2 document increment is frozen and encoded; the program
validates with zero diagnostics against the byte-verified pinned Axiom
Indexer subject; one frame is projected. No author-independent fidelity
judgment of this version exists. The predecessor (T1, commit `cc1d29d`,
program `743e07fa…e0c0`) received a review that found its encoding
unfaithful on four points; the dispositions are in
[qualification/received/](../../qualification/received/20261011T130607Z_REVIEW_T1_eca8cef.md).
Actual-use evidence is the T-01 case, recorded in
[qualification/cases/T-01/](../../qualification/cases/T-01/CASE-2.md).
Nothing here is the released STDO Representation, and nothing here is
accepted.

## Frozen subject

T1.2 on `tenant/claude/c3`, identified by digest. The increment is the three
files below, with CALCULUS §1–3 and EVALUATION §1–4 in scope; the later
sections of those files are outside T1 and are named as a residual in the
program.

| File | SHA-256 |
|---|---|
| `standards/FOUNDATIONS.md` | `2f15c6c1c2561ef5ff0da4ba5f961926efa86fb8f6b35b1f61f653a9e4038a22` |
| `standards/CALCULUS.md` | `d708e76c11969c27e5832286ed78a6921decca29234db86ec23b6581524aee0c` |
| `standards/EVALUATION.md` | `fc063460e6834c190bcc5fe045d4a5a8f45a2ffd96a0ec2cad4fa82b677f246d` |

The validation report's resolved sources carry exactly these digests.
EVALUATION is unchanged from T1.

Changes from T1, each traced to a received finding or a run finding:
FOUNDATIONS §1 says a reframed clause's rc.2 source continues to govern its
own scope; §2 makes the step-produced-fact definition conjunctive and
defines "material"; P4a retains provenance; P4b is reframed only, from five
named clauses; P5 notes that RF-012 and AC-007 are restated once in
CALCULUS §3; §4's formal fragment is marked new with its interpretation.
CALCULUS §2 measures context fit before any read, allows the fit options in
combination, vests refinement, sequencing and compression in the step under
its grant, and makes compression preservation a claim; §3 conserves RF-012
and AC-007 by restatement, separates out_of_frame from indeterminate for
undeclared capability, and states that a composite reports by its declared
conjunction with no universal order; §8 follows.

## Mechanical subject

The [dependency contract](../../../../specification/requirements/A_C_DEPENDENCY.md)
pins `refs/tags/axiom_indexer/v2.5.1-rc.2` (tag object `9bff233c…`, commit
`9a9c4797…`). Before first use, each of the seven Product members was read
from that commit's tree with `git show` and its SHA-256 compared with the
release record `axiom_indexer/releases/v2.5.1.md` read at the same commit
(outside this worktree's sparse cone, so read with `git show`, never from a
working tree): all seven match, including the two symlink targets. The
inventory aggregate `55a2061b…63c1` reproduces with the stack's recipe,
SHA-256 over the lines `<sha256>  <type>  <path>` sorted by path. The
received review reproduced this independently.

The executable, schema and output contract were copied from that tree into
a scratch directory for invocation; no Axiom Indexer Install was selected.
Jim owns selection and acceptance of this dependency's use within STDO 3.
Until that selection, every mechanical result below is candidate evidence
bound to the byte-verified tagged subject; a later selected Install with
different bytes invalidates it.

## Artifacts

| File | SHA-256 | Role |
|---|---|---|
| `axiomatic-program.json` | `f5d653e2fd38de1f06f473beba10684d3b4ec1fc26fb59594cc2fc595dee1f43` | the authored a_c.text program; canonical program digest `sha256:c3f482abe1e6f27edd483408575124e1515b8e48f5ad94a0eeb8c77c3e9e8d49` |
| `logical-constraint-map.json` | `3a7c405d0ac9d9119b0e83072266e04ed20a676167259cbd4c9255176612025c` | deterministic index over the program; intrinsic digest `sha256:cd71e997bbdd456451d6bb1e6b6f2936b0d4608f0370e4dcca3c692ba5906489` |
| `validation-report.json` | `8da74e8386a3679c3bc5beaf6f3e66b637c24bd20fe8a76f0de444fe993b900f` | zero diagnostics; 75 symbols, 86 clauses, 5 residuals; resolved sources include the calculus `cbe2edb9…1f8d` |
| `projection-bounded-activation-materialized.json` | `e13a651410715a551f192d28d9a06754fa58a393364a6c5307e0012dfb5c4089` | the T-01 frame, materialized: 40 symbols, 35 clauses, 3 residuals in closure; projection digest `sha256:91980e28…13e20` |
| `projection-bounded-activation-reference-only.json` | `7e459b0438854a30706702173a5181a79d6e89cd024b7cde3b9ff6861c11fc31` | the same frame, reference-only |
| `bindings.json` | `816d211c2a92c3e3d2e8adc13d07fb1ae5ecc9fb8b8b4ba593b6f7f6009e201f` | invocation-local; tenant basis relative to this directory, rc.2 basis as this host's install path; regenerate elsewhere |

Program identity `urn:stdo-3:claude:program:a-c-text:t1` (unchanged; the
version is the digest); source basis
`stdo-3://build_tenants/claude/standards/`; calculus
`stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md`.

## Source-to-model dispositions

Vocabulary. The tenant documents define no a_c vocabulary, so the program
declares its own under `urn:stdo-3:claude:vocabulary:`: seven kinds
(concept, hypothesis, law, operation, record, result, role), six operators
(requires, forbids, distinguishes, preserves, derives, maps-to; `supersedes`
was dropped with the only clause that used it) and nine roles (subject,
requirement, premise, condition, exception, support, consequence,
qualification, target). No mapping to the STDO Representation vocabulary is
claimed.

Encoded as clauses: FOUNDATIONS §1 standing rules; the operative
distinctions of §2 (eleven clauses, now including materiality; the sixteen
definitions themselves are symbol labels, not clauses); §3 as four premise
relations, eight commitment statements and the two derivations, with P4b
and P5 citing their premise clauses under the `derives` operator; §4 as
eleven algebra clauses, the formal fragment carrying its stated
interpretation; §5 as one clause over the four hypothesis symbols; CALCULUS
§1 (eight), §2 (nine: the six of T1 plus measured fit, fit selection within
grant and compression preservation as a claim) and §3 (ten: the T1 eight
with the supersession replaced by a `preserves` relation to the `rc2-builder`
symbol, plus the out_of_frame boundary and the composite rule); EVALUATION
§1 (four), §2 (four), §3 (six) and §4 (three).

Not encoded: the source-dispositions tables of each document, because
rc.2 members lie outside the program's source basis and the validator
refuses sources outside it; the dispositions remain routes in the documents
(residual `rc2-routes-are-outside-program-basis`). CALCULUS §4–7 and
EVALUATION §5–8 are outside T1 (residual `t1-boundary-forward-references`).

Residuals (five). Three of T1's eight were resolved by document repair and
removed: 'material' is now defined; the out_of_frame against indeterminate
boundary is stated; compression preservation is a claim with a stated
assessment rule rather than an unnamed judge. Remaining: the T1 boundary;
the fit test on attention, time and capability (context is now measured);
independence arguments of one sentence each; the formal fragment carried
with its interpretation but not constructed, new in this corpus; rc.2
routes outside the program basis.

## What validation proves

Structure, URI resolution, reference closure, grounding and the canonical
digest. It does not prove that the clauses are faithful to the documents,
complete, or uniquely interpreted. That judgment is author-independent and
source-first; the T1 version failed it on four points; none has been made
of this version.

## Reproduction

```sh
AC=<scratch copy of axiom_indexer/build_tenants/core/code/ac.py at 9a9c4797>
python3 -I $AC validate --program axiomatic-program.json --bindings bindings.json \
  --output validation-report.json --emit-map logical-constraint-map.json
python3 -I $AC project --program axiomatic-program.json --map logical-constraint-map.json \
  --bindings bindings.json --frame-index urn:stdo-3:claude:a-c-text:frame-index:bounded-activation \
  --mode materialized --output projection-bounded-activation-materialized.json
```

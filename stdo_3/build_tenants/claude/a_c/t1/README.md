# T1 a_c Interpretation (Claude tenant)

Status: the T1 document increment is frozen and encoded; the program
validates with zero diagnostics against the byte-verified pinned Axiom
Indexer subject; one frame is projected. No author-independent fidelity
judgment exists. Actual-use evidence is the T-01 case, recorded in
[qualification/cases/T-01/CASE.md](../../qualification/cases/T-01/CASE.md).
Nothing here is the released STDO Representation, and nothing here is
accepted.

## Frozen subject

Commit `cc1d29d` on `tenant/claude/c3`. The increment is the three files
below, with CALCULUS §1–3 and EVALUATION §1–4 in scope; the later sections
of those files are outside T1 and are named as a residual in the program.

| File | SHA-256 |
|---|---|
| `standards/FOUNDATIONS.md` | `5f5e7ab3b820657ec5992aa3eb9c0bc7a6f937dbe9ec0f36eb75014429efed80` |
| `standards/CALCULUS.md` | `879fb9dd7c8f59c866f2e9564e685dd57611bbeabd2806dc40d9b0ea5fb582ad` |
| `standards/EVALUATION.md` | `fc063460e6834c190bcc5fe045d4a5a8f45a2ffd96a0ec2cad4fa82b677f246d` |

The validation report's resolved sources carry exactly these digests.

## Mechanical subject

The [dependency contract](../../../../specification/requirements/A_C_DEPENDENCY.md)
pins `refs/tags/axiom_indexer/v2.5.1-rc.2` (tag object `9bff233c…`, commit
`9a9c4797…`). Before use, each of the seven Product members was read from
that commit's tree with `git show` and its SHA-256 compared with the
release record `axiom_indexer/releases/v2.5.1.md` read at the same commit
(outside this worktree's sparse cone, so read with `git show`, never from a
working tree): all seven match, including the two symlink targets. The
inventory aggregate `55a2061b…63c1` reproduces with the stack's recipe,
SHA-256 over the lines `<sha256>  <type>  <path>` sorted by path.

The executable, schema and output contract were copied from that tree into
a scratch directory for invocation; no Axiom Indexer Install was selected.
Jim owns selection and acceptance of this dependency's use within STDO 3.
Until that selection, every mechanical result below is candidate evidence
bound to the byte-verified tagged subject; a later selected Install with
different bytes invalidates it.

## Artifacts

| File | SHA-256 | Role |
|---|---|---|
| `axiomatic-program.json` | `9dfa2e06e70393e86dd4381e6c2dd784dafb6006148fb3bb27b18df2a599bd4c` | the authored a_c.text program; canonical program digest `sha256:743e07fa98057d5833642c2d1cfaaeeadce2dd74c86810871b309baee4c9e0c0` |
| `logical-constraint-map.json` | `74dd17a04b8d25e0c02106c24042567615df6bd649c725cd024d284542eb30e2` | deterministic index over the program; intrinsic digest `sha256:8c48e04c62f5e43da47937c50e723769fd395300e63c1434ca7a7588d668faa3` |
| `validation-report.json` | `ff209a504ddab51a932639bad84e2459f8e8d3780ea73aba7ce2ef9f9f896dc3` | zero diagnostics; 74 symbols, 80 clauses, 8 residuals; 25 resolved sources including the calculus `cbe2edb9…1f8d` |
| `projection-bounded-activation-materialized.json` | `728973230d798e051290cee41eb183aaef6b7903beffcf4db573036fccdbb990` | the T-01 frame, materialized: 40 symbols, 28 clauses, 6 residuals in closure |
| `projection-bounded-activation-reference-only.json` | `8f77276b01f5619a3bb4d71327dc12987d78bcfd48aac7a8e476518566c3295d` | the same frame, reference-only |
| `bindings.json` | `816d211c2a92c3e3d2e8adc13d07fb1ae5ecc9fb8b8b4ba593b6f7f6009e201f` | invocation-local; tenant basis relative to this directory, rc.2 basis as this host's install path; regenerate elsewhere |

Program identity `urn:stdo-3:claude:program:a-c-text:t1`; source basis
`stdo-3://build_tenants/claude/standards/`; calculus
`stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md`.

## Source-to-model dispositions

Vocabulary. The tenant documents define no a_c vocabulary, so the program
declares its own under `urn:stdo-3:claude:vocabulary:`: seven kinds
(concept, hypothesis, law, operation, record, result, role), seven operators
(requires, forbids, distinguishes, preserves, derives, maps-to, supersedes)
and nine roles (subject, requirement, premise, condition, exception,
support, consequence, qualification, target). No mapping to the STDO
Representation vocabulary is claimed.

Encoded as clauses: FOUNDATIONS §1 standing rules; the operative
distinctions of §2 (ten clauses; the fifteen definitions themselves are
symbol labels, not clauses); §3 as four premise relations, eight commitment
statements and the two derivations, with P4b and P5 citing their premise
clauses under the `derives` operator; §4 as eleven algebra clauses; §5 as one
clause over the four hypothesis symbols; CALCULUS §1 (eight), §2 (six) and
§3 (eight, with the four refinements as `maps-to` or `distinguishes`
relations to the core algebra and the RF-012/AC-007 supersession as a
`supersedes` relation to the `rc2-builder` symbol); EVALUATION §1 (four),
§2 (four), §3 (six) and §4 (three).

Not encoded: the source-dispositions tables of each document, because
rc.2 members lie outside the program's source basis and the validator
refuses sources outside it; the dispositions remain routes in the documents
(residual `rc2-routes-are-outside-program-basis`). CALCULUS §4–7 and
EVALUATION §5–8 are outside T1 (residual `t1-boundary-forward-references`).

Residuals found while encoding, each with a re-entry route: 'material' is
undefined in the ontology; the fit test is not operationalised; the
independence arguments are one sentence each; the formal fragment is carried,
not constructed; indeterminate and out_of_frame overlap for undeclared
capability; the judge of lawful compression is unnamed. These are candidate
findings against the documents and are inputs to the next successor, not
repairs.

## What validation proves

Structure, URI resolution, reference closure, grounding and the canonical
digest. It does not prove that the clauses are faithful to the documents,
complete, or uniquely interpreted. That judgment is author-independent and
source-first; none has been made.

## Reproduction

```sh
AC=<scratch copy of axiom_indexer/build_tenants/core/code/ac.py at 9a9c4797>
python3 -I $AC validate --program axiomatic-program.json --bindings bindings.json \
  --output validation-report.json --emit-map logical-constraint-map.json
python3 -I $AC project --program axiomatic-program.json --map logical-constraint-map.json \
  --bindings bindings.json --frame-index urn:stdo-3:claude:a-c-text:frame-index:bounded-activation \
  --mode materialized --output projection-bounded-activation-materialized.json
```

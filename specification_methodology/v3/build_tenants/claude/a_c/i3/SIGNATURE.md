# Signature of the Iteration 3 Interpretation

This file lists every vocabulary URI the iteration 3 program uses, with
its meaning and the record kind or argument role it serves. It follows
[INTERPRETATION §3](../../design/INTERPRETATION.md#3-encoding). All URIs
share the prefix `urn:stdo-3:claude:i3:vocabulary:`, written `v:` below.
The program's subject is the candidate's `standards/` members at the
source-settlement commit; its calculus basis is the installed
`stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md`.

## Symbol kinds

| URI | Meaning |
|---|---|
| `v:kind:concept` | a semantic object the source names, such as a result, a disposition or an authority |
| `v:kind:standing` | one of the five standing symbols below |
| `v:kind:core-value` | one of the five core result values of FOUNDATIONS §4 Results |
| `v:kind:refined-value` | a value a member defines as a refinement of the core |
| `v:kind:premise` | one of the commitments P0 to P6 and C of FOUNDATIONS §3 |

## Standing symbols

Every clause carries exactly one argument with role `v:role:standing`
whose reference is one of these symbols (`urn:stdo-3:claude:i3:standing:` plus the name).

| Name | Meaning | Required companions |
|---|---|---|
| `premise` | a commitment the candidate states without deriving it | none |
| `consequence` | a determination the candidate derives | at least one `v:role:support` reference to an existing clause |
| `policy-choice` | a determination its owner chooses among admissible alternatives | `v:role:owner` (literal: the owning section), `v:role:choice` (literal: what was chosen) and `v:role:among` (literal: the alternatives); the choice literal is never the whole statement |
| `observation` | a recorded fact about a subject | `v:role:qualification` naming its source |
| `unresolved` | a claim the source leaves open | `v:role:blocked-by` reference to a residual |

## Core values

`urn:stdo-3:claude:i3:core:` plus `satisfied`, `falsified`,
`indeterminate`, `out_of_frame` or `invalid_basis`. A planned evaluation
that was not performed has no core value and has no symbol.

## Operators

| URI | Clause type | Meaning |
|---|---|---|
| `v:operator:requires` | constraint | the subject must hold or be done, at the stated force |
| `v:operator:forbids` | constraint | the subject must not hold or be done |
| `v:operator:permits` | constraint | the subject may hold or be done; a latitude |
| `v:operator:states` | constraint | a determination with no single modal verb, such as a definition the source decides |
| `v:operator:uses` | relation | a consumer section applies an owner clause without restating it |
| `v:operator:maps-to` | relation | a refined value maps to exactly one core value for a predicate |

## Argument roles

| URI | Use |
|---|---|
| `v:role:standing` | the clause's standing symbol |
| `v:role:subject` | a concept the clause is about |
| `v:role:force` | literal `must`, `must-not`, `should`, `should-not` or `may`, as the source states it |
| `v:role:condition` | literal: the scope or trigger the source states |
| `v:role:exception` | literal: an exception the source states |
| `v:role:qualification` | literal: any other limit the source states |
| `v:role:support` | a clause this consequence follows from |
| `v:role:owner` | literal: the owning section of a policy choice |
| `v:role:choice`, `v:role:among` | literals: what a policy choice chose, and among what |
| `v:role:consumer` | literal: the consumer section of a `uses` relation |
| `v:role:refined-value`, `v:role:predicate`, `v:role:core-value` | the three parts of a `maps-to` relation; exactly one `core-value` |
| `v:role:blocked-by` | a residual the clause depends on |
| `v:role:support-kind` | literal: the kind of support the statement has, one of the five below (I5) |

## Kinds of support (I5)

A clause may carry one `v:role:support-kind` literal naming what supports
its statement, as FOUNDATIONS §4 Formal representation requires the
interpretation to distinguish. A clause encoding one of the construction
or assurance relations carries one; other clauses may.

| Literal | Meaning |
|---|---|
| `stated-formula` | the statement writes a formal obligation whose implication is not discharged here |
| `discharged-argument` | the statement is supported by a written mathematical or deductive argument in the source |
| `mechanically-checked-structure` | the statement's structure is what the pinned checker validates; nothing beyond structure is established |
| `externally-assessed-predicate` | the statement's truth about a subject is assessed outside this program, by a review or a trial, with its own evidence |
| `execution-evidence` | the statement records what an execution observed, with its execution provenance |

A support kind confers no standing and no truth: a `stated-formula` is
not proved, an `externally-assessed-predicate` is not assessed by being
labelled. The kind says which evidence would establish the statement.

Every clause whose owning section is one of the construction or assurance
relations (ACTIVATION §1 Construction relation; FOUNDATIONS §3
Construction synthesis; FOUNDATIONS §4 Assurance relations and its six
subsections) carries exactly one kind, and the pre-check refuses one that
does not. At I5-05 these are the 89 clauses of group G14: 80
`discharged-argument` and 9 `stated-formula`. The other three kinds do not
occur in the group: no statement of those sections is supported in the
source by checked structure, an external assessment or a recorded
execution.

## Section dispositions

Each heading section of an encoded member has exactly one disposition in
`dispositions/<member>.md`:

| Value | Meaning |
|---|---|
| `encoded` | the section's determinations are clauses of this program |
| `encoded-in-part` | some of the section's determinations are clauses of this program, named in the row; the rest is uncovered, as for `not-encoded-i3` |
| `uses owner` | the section applies another section's determination; a `uses` relation records it |
| `refines owner` | the section refines an owner; `maps-to` relations record it |
| `residual` | the section leaves a question open; a residual records it |
| `no determination` | the section decides nothing (a position statement, an index, a disposition table) |
| `not-encoded-i3` | the section decides something that iteration 3 did not encode. It is uncovered, never counted as `no determination`, and it is reported separately |

# Loan evidence: the graph language of the 5.0 source

**Type:** NOTE. Evidence for the product owner's loan decision (goal 2), not law.
**Author:** claude (Fable 5.2) · 18 November 2026

**Recommendation: take it as a design and write it new. Do not take the code.**

Source read: `abiogenesis-mothball/loaner/5.0-main-7bf7c342a/.../typescript/code/src/gtl/`.

## What is worth taking

The term algebra in `c_algebra.ts` (612 lines) is sound, and it depends on
nothing but two small helpers. Its ideas map onto the draft directly:

| 5.0 term | In the draft |
|---|---|
| `c_of`, a single piece of work, marked as run by code, by an agent or by a person | A session, a check, a decision by the user |
| `c_edge`: transform, evaluate, consequence | A step: the work, its evaluation, its checks and decision |
| `c_compose` | A sequence |
| `c_workflow`, which names a graph function | A reference |
| `c_retry` | The attempts a vector declares |
| `c_batch` | Left out |

Four laws of it are worth keeping as they are:

- A term can be made only through its constructor, which checks it. A term
  that exists is well formed.
- A sequence inside a sequence is flattened, and a term that does nothing is
  dropped, so one graph has one written form.
- A term is data: it cannot be changed after it is made, and it is written out
  and read back without loss.
- Composing two graph functions, or putting one in place of a vector of
  another, is a function from graphs to a graph (`graph_construction.ts`).

## Why not the code

1. **It walks the graph by position.** `source_path.ts` (1,114 lines, the
   largest file) works out the next term from the term that just finished, and
   carries the attempt number and the identity of the last output with it.
   That needs a record of where the run was. Guard rail 3 says each step reads
   the workspace as it is now, and `next` in the draft is worked out from the
   workspace alone. This file cannot be used.
2. **Its graph is a chain.** Every node that is not the last must have exactly
   one edge out (`ordinaryGraphBoundaryFailure`). The draft's vector needs
   several assets and produces one, so its graph is a graph of dependencies.
3. **Values pass from term to term.** Each term names an input and an output
   value, and a term's output is the next term's input. In the draft nothing
   passes between sessions except the workspace (guard rail 5).
4. **Each piece of work names seven contracts** (input, output, evidence,
   failure, refusal, judgement, and what carries it out), and a published
   module carries three digests and a manifest. The draft's vector declares
   its assets and its checks, and nothing else.
5. **The data format pulls in the retired product.** `serialization_contracts.ts`
   imports four of the files outside the agreed boundary, and fixes the
   version "5.0.0" in every record.

Written new, I expect the graph language to be a few hundred lines, against
about 4,800.

## The other three loans

I have not read their source for this note. From the draft's requirements:

| Loan | Recommendation | Reason |
|---|---|---|
| Registry | Write new | In the draft it is a list of named graph functions, kept as data beside the graph |
| Higher-order graph functions | Take the two as a design: compose, and put in place | They are the fourth law above. The 5.0 folder for them (9,212 lines) works by replaying the event log |
| Event log | Write new | The draft's log is only added to and no decision is taken from it. The 5.0 log is what the run is rebuilt from |

## Limits

I read `c_algebra.ts` in full, the data format in full, the traversal function
of `source_path.ts`, and the outlines and imports of the rest. I did not read
the bodies of `graph_construction.ts`, `materialize.ts` or
`canonicalization.ts`, and I ran none of it.

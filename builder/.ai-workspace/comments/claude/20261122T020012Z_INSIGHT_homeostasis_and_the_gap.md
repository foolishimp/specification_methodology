# Insight: homeostasis between the specification and the workspace

Commentary, not law. Author: Claude, as Executive. Date: 22 November 2026.
Source: the product owner's statements of that day, quoted in section 1. The
algebra in sections 2 to 8 is my rendering of them. Section 9 marks what is my
reading and what is not built.

## 1. The owner's statements

1. "i have A -> X through a series of steps, I want to amend A -> A2, and so
   the change must flow through A2 -> X2 over A -> X"
2. "this is true when the stage is empty, its also true when its iterating,
   when it enters a stage, it always has the current state of the workspace as
   that node is bound over it, the gap between the current state and future
   requirement is the work"
3. "ive described this as homeostatis bewteen the the workspace and
   specification"
4. "Intent arises as the measured gap between the specification (my idealised
   model) and the workspace (reality), this then leads to solutioning (graph
   selection) and action"
5. "the original intent is the bootstrap coming out of the parent enviornment,
   it solves our chicken or the egg"
6. "the recursive aspect is that sub projects may exist each with their own
   intent as recursions of the parent"
7. "and a composition of projects is a graph"

## 2. Terms

The laws are defined once, in `build_tenants/typescript/design/CALCULUS.md`:
section 11, "The gap", with K6, K7, L2, L3, L8, L11 and L12. Sections 2 to 7
here are a reading aid in other notation. Where the two differ, the calculus
is right. One known difference: the gap is whatever the `done` test says no
to, which can include a failing test on a file outside every asset; the nodes
not accepted, `Γ` below, are the part of it a record can close.

- `G = (N, E)`: a graph. `N` is its nodes. `E ⊆ N × N` is its edges, with no
  cycle. `dep(n) = { m : (n, m) ∈ E }` is what node `n` depends on.
- `w`: a workspace state. `w(n)` is the content at node `n`, or `⊥` where
  nothing is there. `w|D` is `w` on a set of nodes `D`.
- `id(c)`: the identity of content `c`. `id(c) = id(c′)` exactly when `c = c′`.
- `R_n(c, d)`: the result declared for node `n`. It is true or false of
  content `c` against the contents `d` of `dep(n)`.
- `M`: the owner's idealised model. It is outside the workspace.

## 3. The gap, acceptance and rest

    closed_n(w)   ⇔  w(n) ≠ ⊥  ∧  R_n(w(n), w|dep(n))
    accepted_n(w) ⇔  closed_n(w)  ∧  ∀ m ∈ dep(n): accepted_m(w)
    Γ(w)          =  { n ∈ N : ¬ accepted_n(w) }

`Γ(w)` is the gap of the whole workspace. The workspace is at rest exactly
when `Γ(w) = ∅`. There is one notion of done, and it is this one.

## 4. A step

A step at `n` is a function on workspace states, `σ_n : w ↦ w′`, with three
laws.

    (S1) writes only its node:   w′(m) = w(m)  for every m ≠ n
    (S2) closes its gap:         closed_n(w′)
    (S3) changes nothing else:   closed_n(w)  ⇒  σ_n(w) = w

S3 is the owner's "what the change does not concern is left as it was", at its
limit: on a closed gap a step is the identity. Short of the limit it reads:
`w′(n)` differs from `w(n)` only where S2 requires it.

The work of a step is its gap and nothing else. Statement 2 says this holds
on every entry. The three situations are values of the same two inputs,
`w(n)` and what is recorded at `n`:

| Situation | `w(n)` | Record at `n` | The gap |
|---|---|---|---|
| Empty stage | `⊥` | none | all of `R_n` |
| Iterating | there | says no, with findings | the findings |
| Change above | there | says yes, given on `w°` | what `δ_n` requires (section 5) |

## 5. Records, and A2 → X2 over A → X

Measuring `R_n` is a judgement and costs a session. A record keeps the
judgement with the identities it was given on:

    ρ_n = ( verdict, id(w°(n)), { id(w°(m)) : m ∈ dep(n) } )

    δ_n(w°, w) = { m ∈ dep(n) ∪ {n} : id(w°(m)) ≠ id(w(m)) }

    (R1)  δ_n(w°, w) = ∅   ⇒   closed_n(w) = closed_n(w°)

R1 is why nothing is judged twice: a yes holds until something it was given
on differs. So a gap at an accepted node can open only inside `δ_n`.

Statement 1 is then a square. Let `f` be the steps that took `A` to `X`, and
`a : A → A2` the change. The step taken over the accepted one, `f̂`, is given
`X` and `a`, not `A2` alone:

         A  ──f──▶  X
         │a         │ f̂(X, a)
         ▼          ▼
         A2 ──f──▶  X2

    (A1)  X2 = f̂(X, a)  is closed against A2          (it commutes)
    (A2)  f̂(X, identity) = X                           (no change, no work)
    (A3)  f̂(f̂(X, a), b) ≃ f̂(X, b ∘ a)                 (changes compose)

`≃` means "closed against the same thing", not "the same bytes". A3 holds
without extra machinery because `δ_n` is measured from the record to now,
whatever happened between.

## 6. Intent, solutioning, action

    ι = gap(M, w)                     intent: the measured gap, stated
    τ = I(ι, w)                       solutioning: induction selects a graph term
    w′ = τ(w)                         action: the term's steps, each under S1–S3

    H(w) = w            if Γ(w) = ∅
    H(w) = τ(w)         otherwise

Homeostasis is the iteration of `H` to its fixed point. The specification
nodes of `w` are `M` as far as it has been written and accepted, and they are
the set point for the nodes that depend on them. A disturbance may come from
either side: a change to `M` (a ticket), or a change to `w` (a hand edit).
Both are a non-empty `Γ`, and `H` does not ask which.

## 7. The bootstrap

Inside a new project there is no specification, so `gap(M, w)` cannot be
measured there. The first intent is given from outside:

    ι₀(P) = the gap of the parent environment at P

The source node `s` has `dep(s) = ∅`, and its result is judged against that
intent: `R_s(c, ι₀)`. Every later intent is measured inside, by section 6.

## 8. Recursion and composition

This section describes how products relate. It is not something the framework
does: every framework instance has exactly one workspace, as the intent says.
The owner confirmed this reading on 22 November 2026.

A project `P` is a governed product: its own workspace `w_P`, its own graph
`G_P`, its own intent, its own set-up. Projects compose in a graph `C` whose
nodes are projects and whose edges are dependencies between them.

    done(P)   ⇔  Γ_{G_P}(w_P) = ∅
    ι₀(P)     =  the gap of P's parent environment at P

Sections 3 to 7 hold inside each project unchanged. Between projects, the
carrier is a person or a ticket: a parent's gap is handed to the child as its
first intent, and a gap the child cannot close comes back to the parent's user
as a ticket (product definition, "Ask"). No run crosses a workspace, and no
record in one workspace stands on another.

## 9. Status

| Part | State |
|---|---|
| The gap, acceptance, records | built; stated in the calculus, section 11 |
| The one form of a step's packet | built (`d39c33bea`); live on a Hello, one sentence added to the intent went from 5 sessions to 2 |
| A check is done only where it can change what happens next; checks declared on nodes | built (`88dcf3d7d`, `17df7b5e9`, `2c5a23295`) |
| "Changes nothing beyond the gap" judged by the evaluation | not built |
| After a no inside a change, the packet names the findings but not what changed since the last yes | open (D177) |
| Work that cannot be closed comes back to the user | the ticket stays active and the run names the step and the findings; no new ticket is written |
| Section 8 | nothing to build; it describes how products relate |
| Set-up of a product in a folder inside another repository | refused today; so a sub-project is its own repository |

My readings, not the owner's words:

- `INTENT.md` is `ι₀`, and a ticket is a later `ι`.
- Between projects, a project builds on a released cut of another, not on its
  working files.
- "homeostasis" and "gap" appear in neither the intent nor the product
  definition.

Guard: this model describes the system. It is not a list of machinery to add.
Anything built from it is first tested against the intent's seven guard rails.

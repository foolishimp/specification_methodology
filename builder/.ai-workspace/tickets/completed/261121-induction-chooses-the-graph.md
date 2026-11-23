# Induction chooses the graph

- kind: feature
- class: requirement_reprice
- enters: requirements

From the product owner, 21 November 2026: the special path of small work is a
hack and goes. "induction/initialisation over a workspace does a
triage/analysis then chooses the proportional and appropriate processes to
solve the problem - under the hood this should all be implementable with our
existing gtl/graph/HoG machinery"; "graphs are first class citizens and
recursive"; "induction drives the missing gap to be built, that's the
requirements change, I don't think I need a product change".

The requirements changed under the product owner's instruction of 21 November
2026, for his reading. The intent and the product definition are unchanged:
the product definition's first step, which settles where the ticket enters
and whether it is small work, stays true of induction.

The Executive's reading:

1. The first vector, `place-ticket`, is `induct-ticket`: one session, its
   packet, a computed check and the user's confirmation. No session is added.
2. Induction writes on the ticket the method's triage (kind, class, the node
   the work enters at, the node it ends at, how much it touches) and one term
   of the graph language over the registry's entries. The `small` field goes.
3. The induction's packet lists the registry: each entry's name, needs,
   produces and purpose. Each purpose says when the entry fits.
4. One computed check of the term, read through the constructors: each name
   is in the registry; each entry's needs are met by the workspace or by an
   entry before it; the term ends at the node the triage says. A term that
   fails is a no with its findings.
5. A run carries out the ticket's term. The conditions of small work go
   (D109, D110, D117; D118 dissolves). The simplest ticket is not inducted
   and keeps the default. Nodes made of parts (D108) stay.
6. A term may name the induction itself only if that falls out; otherwise the
   check refuses it, for the product owner. The session limit is the only
   bound.
7. The graph calculus on paper (design, CALCULUS.md section 10), each law
   tested; `round(t)` steps on what the ticket's term denotes; the check of
   the event log refuses a session the term does not name.

Acceptance:

- Hello from an empty workspace takes four sessions: the induction, the
  specification, the build and one evaluation.
- A term of the six single-asset functions takes them one by one, and a term
  that ends at the specification builds nothing after it.
- `pnpm check` passes, and the definition verifies.

## State, 21 November 2026

In progress: built by a writer under the Executive (D120 to D131), not yet
reviewed or committed. Open for the product owner: D123 (the default leaves
out the two steps), D124 (nested induction refused), D126 (the proportion
line on every packet), D130 (REQ-FLOW-008's acceptance amended), D131 (his
own graph and registry need the change by hand).

## Result

Built in `776434fbb`, repaired after an independent review in `d02c5c3d1` and
`b843c037f` (decisions D120 to D139). The five Hello products were built again
on the release `b843c037f6`, each judged outside the framework. Every induction
chose `write-specification ; write-build`, entering at the intent and ending at
the code, with no hint of size from the framework.

| Product | Small-work path (`2def0593b`) | Induction (`b843c037f`) |
|---|---|---|
| basic-cli | 4 sessions, 7 min, 3.28 USD | 4 sessions, 8 min, 3.37 USD |
| js-tenant-test | 4 sessions, 8 min, 3.54 USD | 4 sessions, 9 min, 3.76 USD |
| rust-cli | 4 sessions, 8 min, 3.08 USD | 4 sessions, 12 min, 4.49 USD |
| rust-service | 4 sessions, 15 min, 4.41 USD | 4 sessions, 13 min, 4.51 USD |
| parallel-js | 4 sessions, 9 min, 3.72 USD | 4 sessions, 9 min, 3.72 USD |
| In all | 47 min, 18.03 USD | 51 min, 19.85 USD |

Open for the product owner: D123 (which entries the default term names), D124
(a term that names the induction is refused), D126 (the proportion line on
every packet), D130 (a ticket that ends above the code leaves the rest to the
simplest ticket, which is never inducted).

## After the model of source and termination

An induction entry inside a term (`c00e49f7b`, D140 to D145) and one model for
every term, a source and a termination (`8b292324a`, D146 to D150), followed.
The five products were built again on the release `8b292324a9`: four sessions
each, every term `write-specification ; write-build`, each judged outside the
framework and passed.

| Product | Time | Cost |
|---|---|---|
| basic-cli | 8 min | 3.31 USD |
| js-tenant-test | 10 min | 3.67 USD |
| rust-cli | 11 min | 3.86 USD |
| rust-service | 16 min | 4.49 USD |
| parallel-js | 12 min | 4.66 USD |
| In all | 57 min | 19.99 USD |

Open for the product owner: D123, D126, D130, D141, D144, D147 (acceptance
stands on everything above a node), D148, and the removal of the dependency
order from the prescribed set.

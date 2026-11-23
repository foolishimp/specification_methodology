# Algorithms, parameters and a three-way bind

**Type:** NOTE. Commentary for the product owner, not law.
**Author:** claude (Fable 5.2) · 18 November 2026
**Source:** the owner's words of today, and the product page of his
`computational_calculus` project, transcribed from four photographs in
`20261118T082216Z_SOURCE_computational_calculus_product_page.md` beside this note.

## The owner's words

"its more about my changed philosophy to building software, i want to define
the application (aka business functions) as algorithms and process flows, i
want to identify the parameters of the business architecture e.g. 1million
records in 5 mins, 100k observers etc. I then have a prescribed set of
computational algorithms, and then do a three way bind between the business
algorithms, computational algo & the tech stack"

## The philosophy, in four statements

1. **The application is its business functions, stated as algorithms and
   process flows.** An algorithm takes named inputs to an output. What it
   returns is its meaning, and the one test of everything built from it.
2. **The business architecture is stated as parameters.** How much, how fast,
   for how many: a million records in five minutes, a hundred thousand
   observers. These are stated beside the algorithm, not inside it.
3. **The computational algorithms are a prescribed set.** They are known ways
   to compute, each with rules for how it may be combined and rewritten, and a
   stated condition for what each rewrite preserves. They are chosen from, not
   invented for each product.
4. **Building is a three-way bind.** A business algorithm, with its
   parameters, is bound to a computational algorithm that can meet them, and
   that is bound to a technology stack that can run it. A stack is correct when
   it returns what the business algorithm returns, within any tolerance the
   parameters allow.

## This is how the owner means to build Builder itself

The owner, later the same day: "im defining the way I'd like to build out the
builder, using STDO". The method already has the same chain, in its section on
build tenants: what the product must do, then a declared set of operations
with their laws, then the stack that performs them. So this is the method used
as written, with the three parts kept apart.

| Part | For STDO Builder | Where it is written |
|---|---|---|
| Business algorithms | The product's functions, each from named inputs to an output: is this vector closed; which vectors may run next; is this graph well formed; what did this change re-open; where does the work stand | The specification |
| Process flows | A run, one step at a time; the life of a ticket; a question and its answer; resuming | The specification |
| Parameters | One address space. One session at a time. Graphs of tens of vectors. Event logs of thousands of entries. Workspaces of many thousands of files. A small fixed cost for each step. One user | The specification, apart from the algorithms |
| Computational algorithms | The term language taken from the graph language: reference, compose, workflow, retry. The effects a step may have: refusal, a failure that may be retried, a wait for the user, the user's approval, a record in the event log, reads and writes of the workspace | The build tenant's design, chosen from the prescribed set |
| Stack | TypeScript, git, the agents' own programs | The build tenant's design, bound last |

What this changes in the draft:

- **The requirements are restated.** Each family becomes a few algorithms and a
  process flow. Today they are prose, with numbers such as "ten seconds" and "a
  hundred entries" inside the sentences. Those numbers move to one page of
  parameters.
- **The algorithms are pure.** Each returns the same value for the same graph
  and the same workspace. That is the intent's first guard rail, and it gives
  the test: the built product returns what the algorithm returns.
- **Design is a bind, not an invention.** The agent that designs chooses from
  the prescribed set and says why each choice meets the parameters. The
  post-mortem found that agents left free in design added weight every time.
- **A refusal is not a failure.** A refusal is an answer and is never retried.
  A failure is transient and may be retried. The draft's rule on attempts does
  not yet tell them apart.

## Open

- I have read the product page only, not the calculus itself or its
  requirements. They are on the owner's other machine.
- Much of that page concerns data volumes, change rates, tiers and labels.
  Which of it the first build of Builder needs is not settled.

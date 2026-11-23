# The graph language

**Family**: REQ-GRAPH-*
**Status**: Active
**Category**: Capability

These requirements cover the graph language: the notation in which graph
functions are written and published, and the registry that lists them.

### REQ-GRAPH-001 A graph function is a term

A vector is carried out by a graph function. A graph function is written as
one of four terms:

- **a session**: one session does the vector's work;
- **a sequence**: terms one after another, in the order written;
- **a workflow**: a graph, that is, nodes and the vectors that write them,
  each vector with its own graph function;
- **a reference**: the name of a graph function in the registry. In a
  ticket's term, a reference to the induction names its stretch: the node it
  enters at and the node it ends at (REQ-METHOD-006). No other reference
  names one.

A term may hold other terms. The governing graph of a product is a workflow:
the outermost one. The graph language has no other term, and none that runs
two sessions at once.

Acceptance:

- The method's graph is written in these terms, with nothing left to the
  framework's code.

From: product definition, the terms "Graph function", "Graph language" and
"Higher-order graph function"; intent, model, "The graph carries the method."

### REQ-GRAPH-002 What a vector declares

- the entry of the registry it carries out, by a reference: the vector writes
  the nodes that entry writes (REQ-GRAPH-005);
- whether it has an evaluation, and where the findings and the verdict are
  written. The evaluation judges each node the vector writes that an
  evaluation accepts against every node those depend on that the vector does
  not write;
- how many attempts and how much time are allowed;
- whether it ends in a decision by the user, which is then always asked;
- whether it is the first vector for a ticket. A graph has at most one. Its
  asset is the ticket, which is no node, so it alone declares what must be
  true of its asset, and its checks;
- the reference frame each of its sessions is activated on: one for its
  working session and, where it has an evaluation, one for its evaluating
  session. A reference frame is the bounded context of one session, as the
  method's REFERENCE_FRAME standard defines it. A vector declares of a frame
  only its name, its revision and the terms of the method its session needs,
  each with the file and the section of the method release that state it. The
  rest of the frame is what the vector already declares. A frame may be left
  out.

A vector has an evaluation, or ends in a decision, only where a node it
writes is accepted by one, and a vector of the governing graph has each that
a node it writes is accepted by (REQ-GRAPH-003). A given asset is one no
vector writes, such as a ticket the user writes.

Acceptance:

- A graph that declares each of these for a vector is read and written back
  without loss.
- A vector of the method's graph that writes the code and ends in no decision
  is refused, and so is one that writes only the design and ends in one.
- A frame for the evaluating session of a vector that declares no evaluation
  is refused.

From: product definition, the terms "Step", "Evaluation" and "Check".

### REQ-GRAPH-003 An asset is declared by where it is in the workspace

A node declares its asset: the place of that asset in the workspace, what
must be true of it, its checks, the nodes it depends on, which are those its
asset is made from, and what accepts it: an evaluation's yes, the user's yes,
both, or neither (REQ-ALG-004). The place is a path, or a name that the definition
file gives one or more paths to. One graph so serves every governed product,
wherever its files are. What must be true of the asset holds whichever vector
writes it: each session that writes it or judges it is given it, and nothing
else in a graph states it. An asset has one content identity, whatever its
size.

The nodes and what each depends on are the graph's edges. Nothing else in a
graph states a dependency, and no node depends on itself, directly or through
other nodes.

Acceptance:

- For each node, the framework lists the files in the workspace that the node
  covers.
- The same graph, over two definition files that give different paths to the
  code, covers the files each one names.
- In the method's graph the user's yes accepts the intent, the product
  definition and the requirements; an evaluation's yes accepts the design and
  the tests; and both accept the code.

From: product definition, the terms "Asset" and "Content identity"; intent,
guard rail 5.

### REQ-GRAPH-004 A graph is data

A graph is a file of data that a person can read. Adding a graph or changing
one needs no change to the framework's code. What a step means, when it is done
and what follows it are declared in the graph. The framework's code holds no
rule about a particular node, vector, asset or governed product.

Acceptance:

- Scenario S6 ends as it should with no change to the framework.
- The code that traverses a graph names no node, vector or asset of the
  method's graph.

From: intent, model, "The graph carries the method."

### REQ-GRAPH-005 Every named graph function is listed in the registry

A graph function that is given a name has one entry in the registry: its name,
the nodes it writes, and what it is for, in one sentence. What it rests on is
not declared: it is every node the nodes it writes depend on that it does not
write itself. A state is a set of accepted nodes (REQ-ALG-004). An entry
takes a state that holds what it rests on to one that also holds the nodes it
writes. An entry that no vector carries out names a term that composes from
what it rests on and writes exactly the nodes it writes (REQ-METHOD-006). A
reference names one, and the framework follows no reference to a graph
function that is not listed. The registry may also declare a default term: a
term over its entries that a ticket carrying none is built by
(REQ-METHOD-006). A graph does not hold a copy of a named graph function. A
graph function holds no code that the framework executes. A governing graph
is put in place together with its registry. The user can list the registry
and read each entry, with what it rests on.

Acceptance:

- No two entries have the same name.
- An entry that writes what is no node of the governing graph is refused,
  before a step runs.
- From the list alone, a person can say what each graph function is for.

From: product definition, the terms "Graph function" and "Registry"; intent,
outcome 5.

### REQ-GRAPH-006 An outer vector is closed only by the nodes it writes

Where a vector's graph function is a sequence or a workflow, each step of its
inner vectors appears in the event log as any other (REQ-FLOW-005, step 2).
The outer vector is still closed only by the checks and the acceptance of the
nodes it writes (REQ-ALG-004).

Acceptance:

- Where a check of a node the outer vector writes says no, the inner vector
  that writes the node does not close, and neither does the outer vector.

From: intent, guard rail 3.

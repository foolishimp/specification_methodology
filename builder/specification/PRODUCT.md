# STDO Builder

## Product boundary

Identity: `urn:stdo:product-definition:stdo-builder`.
Bounded context: `urn:stdo-builder:bounded-context:governed-construction`.

STDO Builder is the governance framework the [Intent](INTENT.md) describes. It
comes with the method's own work expressed as a graph, and with the means to
set a product up under it.

The purpose, the model and the guard rails are stated in the
[Intent](INTENT.md) and are not restated here. The method release is selected
in the [definition file](../stdo_builder.json). How work on the product is done
and accepted is in the [reference-frame basis](REFERENCE_FRAME_BASIS.md).

## Terms

Workspace, agent, framework and event log have the meanings the Intent's model
gives them.

Graph, node, vector, graph function and traversal have the meanings the
method's outcome-driven development standard gives them in its section 5. In
plain words: a node names an asset and the state it must be in; a vector is an
allowed transition between nodes; a graph function is a named, declared way of
carrying out a vector.

This product adds:

- **Governed product.** A product set up under the method. Its files live in
  one workspace.
- **Asset.** A declared part of the workspace, such as the requirements, the
  design or the code.
- **Ticket.** A work order: it says how the workspace is to be amended. The
  simplest ticket says only that the workspace be built to the specification as
  it stands. Any other says what is wanted, in the user's words, and, once its
  first step is done, at which node of the graph the work enters. As the work
  goes on, the ticket also holds a checklist of what has been delivered, each
  resolution made, and each ruling recorded on the way that binds the rest of
  the work. It stays at that level: the detail is in git. The ticket is the
  context a session starts from. A ticket lies in one of the method's three
  ticket lanes: backlog, active or done.
- **Session.** One start of the agent, from its start to its return. A session
  knows of earlier sessions only what is in the workspace.
- **Step.** One attempt at one vector: a session that does the vector's work,
  then an evaluation where the vector declares one, then the checks of the
  assets the vector writes.
- **Evaluation.** A judgement of an asset against the assets it was made from,
  by a session that did not produce it. Its findings and its verdict are
  written in the workspace.
- **Check.** A test that the graph declares of an asset, or of the ticket, and
  the framework runs against the workspace. It uses no language model, and it
  gives the same result on the same workspace. What it finds is written in the
  workspace. A check may read the verdict of an evaluation.
- **Content identity.** The identity git gives to the exact content of a file,
  or of a folder and all it holds. It names content and is not a copy of it.
- **Run.** One execution of a build, from its start until it ends.
- **Higher-order graph function.** A graph function that composes other graph
  functions.
- **Graph language.** The notation in which graphs and graph functions are
  written and published.
- **Registry.** The published list of graph functions the framework may use.
  It is the governed list of tasks: a ticket is carried out by tasks from this
  list and by no others.
- **User.** The person who sets up a governed product and says what is to be
  built or changed. Where the graph calls for a human decision, the user makes
  it.

## What the product does

1. **Set up.** The user sets up a governed product: a workspace with a method
   release selected and the method's graph in place. The workspace may be empty
   or hold an existing system, which is left where it is.
2. **Ask.** The user asks for work in a ticket. The specification is the
   default path of the work: the simplest ticket asks only that the workspace
   be built to it, and it is what a run does when no other ticket waits. For
   any other ticket, a new product or a change, the first step settles at which
   node it enters the graph, and the user confirms that. Work that cannot be closed comes back to the user as a ticket.
3. **Build.** The specification of a governed product says what that product
   should be. The rest of the workspace is what it is so far. The framework
   traverses the graph one step at a time, from the ticket's node down, until
   the two agree. For each step it finds the vectors that may run next, starts
   the agent on one, has the result evaluated where the vector declares that,
   runs the checks, and records its decision in the event log.
4. **Change.** A change is built as an amendment. Only what depends on the
   change is built again. What the change does not concern is left as it was.
5. **Resume.** The framework continues a run that stopped.
6. **Show.** The user can see where the work stands, what a ticket changed and
   what it cost.

Several tickets may be active at once, up to a limit the user sets. Each is
built on a branch of its own and merged into main when its work is done. One
session works on a ticket at a time. Every session is a new one. The agent writes the product's assets and the framework
writes its own files; neither writes the other's. The framework's own work for
a step is small and does not grow with the history of the work.

The framework runs within a single address space and is not distributed. Its
workspace is named by a URI: it may be on a mounted file system, or reached
through a service that gives access to one. The framework trusts the place it
runs in: it does not guard its own records against the user. The framework does
not depend on which LLM agent does the work, and a vector's work and its
evaluation may be given to different agents.

The product is one library, and it can be instanced in four ways: within a
command-line program; within a program that serves it as tools an agent calls
over the Model Context Protocol (the protocol by which an agent calls a tool);
as a service with an API; or built directly into the user's own application.
Each of the four gives every command, and does nothing the library does not.
The library is published with the product.

## How this product reads the method

This product uses the graph terms of the method's outcome-driven development
standard, from its section 5, and nothing else from that standard. The rest of
it describes a runtime by name and makes a ledger the judge of the work.
Neither binds this product. The intent's guard rails govern, and in
particular:

- A vector is closed when the checks of the assets it writes pass against the
  workspace as it is now.
  The event log records that decision; it is not the proof.
- The event log names files in the workspace and holds none of their content.
- There is one event log. It is the record of what the framework did. The
  ticket is the record of the work done under the framework. The workspace is
  the result. What happened is recovered from these three, and the framework
  keeps no other record of history or of where the work stands.
- Where something the framework did cannot be recovered from the event log
  and the workspace, the log lacks an event or a detail, and that is added to
  the log. It is not recovered another way.
- The framework may run a step again over the workspace as it stands. It never
  rolls the workspace back.

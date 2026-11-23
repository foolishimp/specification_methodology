# Intent

## Purpose

Let one person set up a product under a defined method of work and have an LLM
agent build it reliably. An LLM agent is a language model that can read and
change files and run commands.

The method is specification, ticketing, design and outcome-driven development.
It fixes the order of work: what is wanted is written down and agreed before it
is designed, and designed before it is built.

## Model

The product is a governance framework: a layer over the LLM agent. The purpose
of the framework is to constrain the agent on a graph. The agent works over a
mutable workspace.

- The graph fixes where the agent can be in the work and where it can go next.
  The graph carries the method.
- The agent does the work, in one workspace: the folder that holds the product
  being built.
- The framework's own record is a log of its events, kept in the workspace.

## Guard rails

1. The framework is deterministic. It controls the agent; the agent never
   controls it.
2. The workspace is mutable. The framework never freezes it, copies it or
   rebuilds it in order to work on it.
3. The workspace is the truth about the work. Each step reads it as it is now.
   Where a record and the workspace disagree, the workspace is right.
4. Everything the agent does is in the workspace, and so is every proof and
   every piece of evidence. Nothing outside the workspace is proof.
5. The framework gives the agent references into the workspace, never copies
   of its content, and keeps no copies itself.
6. The framework's log records the framework's own events and is only added
   to. It does not record what the agent does inside a step.
7. The framework has no opinion on how the agent does the work inside a step,
   including how it retries or undoes its own work.

## Outcomes

- A product is set up under the method and built end to end by the agent under
  the framework.
- The agent takes no step the graph does not allow.
- The result can be verified from the workspace alone.
- A run that stops is resumed from the workspace as it stands, without a reset.
- The person using the product acts as a user of it.

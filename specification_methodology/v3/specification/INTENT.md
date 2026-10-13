# Intent

## Mission

To define a precise method for constructing software and processes, with a categorical direction and an axiomatic representation of its laws, so that the method can be mechanically checked and applied to itself.

The method's laws are its rules for how a product is defined, built, checked and released. The direction is categorical. Each kind of construction, such as specifications, algorithms or programs, is treated as a category. Its objects are the things built, and its arrows are the steps from one to another. Steps compose, and a translation between two kinds of construction must be shown to preserve that composition. The representation is axiomatic. Every rule is also written as an axiom in a formal notation, a_c (the axiomatic calculus), so that a program can check the structure of the rules and the references between them. Applied to itself means the method is defined through its own stages, starting with this Intent.

The work of building a product is done in tasks, carried out by people and by language-model agents. A language model reads only a limited amount of text per task, and it keeps no reliable memory between tasks. A person has limited time to read. The method and the product it is applied to are together more than one actor can read and apply at once. For each task the method therefore supplies a reference frame: a document holding only the rules that task must follow. The actor works from that frame and the material the task concerns.

## What The Product Is

The product is the method's documents together with the a_c form of its rules. It has five parts:

1. Foundations: the rules any method needs. They cover how things are named and identified, how a claim is supported by evidence, who may decide what, how a task's result is recorded and combined with others, and how a task is handed to an actor and its result returned.
2. Spec Method: the method for defining and building a product, built on the Foundations. A product is described in four stages. Each stage is a refinement layer: it adds detail to the stage above and must keep what that stage requires.
   - Intent: why the product exists and what outcomes it must achieve;
   - Product: what the product is, its parts and its boundaries;
   - Specification: the behaviour and constraints required of it, and how each is checked;
   - Realisation: the design and implementation, with evidence that they meet the Specification.

   A part large enough to need its own account goes through the same four stages. The Spec Method also covers how work is recorded in tickets, how a change restarts at the earliest stage it affects, how results are reviewed and how releases are cut.
3. Profiles: extensions that apply the Spec Method to one kind of construction. For example:
   - outcome-driven development, for software whose behaviour is published as named functions over a typed graph of domain data, executed by a runtime that walks that graph;
   - user-interface construction, where the screen is computed from typed state and state changes only through typed messages;
   - world modelling, which builds a layer of meaning over existing source systems so that their data can be interpreted.
4. a_c: the formal notation in which the rules, the records of results and the maps between categories are written.
5. Reference frames: the per-task documents described above. A rule copied into a frame names the section that owns it.

One owner per rule. Each rule, definition, list of allowed values or procedure step is written in exactly one section of the method. The parts form tiers in this order: Foundations, then the Spec Method, then the profiles. A rule is owned by the highest tier it holds for. Any other place refers to that section, or narrows the rule for its own use with a link back to it. It never restates the rule differently. A question answered in two places can be answered two ways. The precise obligation is the [single ownership requirement](requirements/README.md#single-ownership-requirement).

One result algebra. Every check, judgement and task reports its result in one shared set of outcome values. The Foundations define those values once, together with how results combine. A part that needs finer outcomes subdivides a shared value, and a subdivision never makes a result look better than it is; for example, a failure never counts as a success. The precise obligation is the [single result algebra requirement](requirements/README.md#single-result-algebra-requirement).

The specification is the program: declared laws are the building blocks, refinement layers stack them, and construction is constraint-based and requirements-based. That is, the specification states the laws and requirements a construction must satisfy, not the steps to produce it; each stage adds detail within the laws of the stage above, and a construction is correct when it satisfies them. A construction step is valid only where the rules declared for the thing being built permit it.

## What It Achieves

- A person or model given a task and its reference frame either completes the task, or stops and states why. It does so without reading the rest of the method and without relying on another actor's memory.
- Every result records what it was based on, its assumptions and its evidence. Later work continues from that record, and a reviewer can check the result without redoing the work.
- A result stays valid until something it was based on changes. A change re-opens only the results based on what changed.
- Producing a candidate (a draft, design or implementation offered for checking), checking it mechanically and accepting it are three separate results. Producing a candidate never counts as checking or accepting it.
- Every rule of the previous release that could affect the new one meets one of four outcomes:
  - kept in the new release's own text;
  - replaced by a named new rule;
  - removed with a stated reason;
  - shown not to apply.

  The new release is complete on its own and does not need the previous release read alongside it.
- A claim that the method, or something built with it, is categorical counts as a hypothesis until it meets the [categorical demonstration standard](requirements/README.md#categorical-demonstration-standard).

## Direction

The method is built using its own previous release, as a compiler is compiled by its previous version. That release is installed: a published, read-only copy on the machine, with its tools, which cannot change while it is in use.

The categorical approach is tried on one thin end-to-end example, the steel thread, before it is applied to the whole method. The steel thread joins one category of algorithms with one category of computation, and it is built using the installed previous release. The method is corrected from what the steel thread shows, and the full categorical product is then built on the corrected release. Carrying the existing rules into the new release continues alongside.

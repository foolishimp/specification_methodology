# Getting started with STDO Builder

This page takes one small product from nothing to a change, in the order you
meet things. It is written from one real run of release 0.1.0-rc.5, on
23 November 2026. The commands are the ones given in that run, and the figures
are the ones it gave. Where the product prints a path, a name, a commit or a
figure this page does not give, this page writes `<...>` in its place. Each
part ends by naming the sections of `INSTRUCTIONS.md`, beside this page, that
hold the details.

## Install

`INSTALL.md` says what you need. From the release's folder:

```
sh install.sh <folder>
```

Put `<folder>/bin` on your PATH, as the install says. Then:

```
stdo-builder --version
```

It printed `v0.1.0-rc.5`.

More in `INSTRUCTIONS.md`: "Install".

## Set up a product

The product was set up in `repo/hello`, a folder inside a larger git
repository:

```
stdo-builder setup repo/hello --name HelloCli
```

Set-up printed that the product lies inside a larger repository, named it,
and listed the eight files it wrote:

```
Set up HelloCli in <...>/repo/hello.
The product lies inside a larger git repository, at <...>. The framework's commits, checkouts and merges concern only the files under <...>/repo/hello; the repository's other files, what is not committed outside the folder and its other branches are left as they are.
It wrote: stdo_hellocli.json, specification/REFERENCE_FRAME_BASIS.md, .stdo-builder/settings.json, .stdo-builder/.gitignore, .stdo-builder/graph.json, .stdo-builder/registry.json, AGENTS.md, CLAUDE.md.
```

Nothing outside the folder changed, the uncommitted and staged files
elsewhere in the repository included. Each ticket's work is done on a branch
of that repository, `stdo/<ticket>`.

More in `INSTRUCTIONS.md`: "Set up a product", "Inside a larger git repository".

## A first ticket

The ticket says, in your own words, what you want:

```
stdo-builder ticket repo/hello "a command-line Hello World in JavaScript with two tests"
stdo-builder run repo/hello
```

Each run went on without you and ended at a question:

```
The run waits for your answer on <...>, for the ticket <...>. The question is given here, and stdo-builder show gives it again:
```

The question names the files it rests on. Read them, answer, and start a run
again. There were three questions:

- Is the ticket inducted as you want it?
- Do you accept the specification?
- Do you accept the build?

With the first answer came a ruling, which bound every later session of the
ticket:

```
stdo-builder answer repo/hello yes --ruling "The script uses nothing outside node's standard library."
stdo-builder run repo/hello
```

The first ticket took 4 sessions, 6.10 USD and about ten minutes. What a run
costs depends on the agent and the size of the product.

More in `INSTRUCTIONS.md`: "Write a ticket", "Start a run", "Answer a question".

## What the ticket holds

The ticket then held your words, the triage, and the framework's lines: one
for each delivery, each yes or no, and the
ruling, each with the commit it was given on. They read like this:

```
- framework: delivered <...> for the user's decision at <...> (<...>)
- framework: resolved user yes at <...> on <...>
- framework: ruling on <...>: The script uses nothing outside node's standard library.
```

More in `INSTRUCTIONS.md`: "What the ticket holds".

## A change by a second ticket

The second ticket added an option `--name`:

```
stdo-builder ticket repo/hello "add an option --name"
stdo-builder run repo/hello
```

It took 4 sessions and 6.60 USD. One run stopped at the limit of sessions the
settings set:

```
The run stopped on the ticket <...>, at <...>: the run reached the limit the settings set, <...> sessions.
```

The next `stdo-builder run repo/hello` went on from where it stopped.

More in `INSTRUCTIONS.md`: "When a run stops", "The settings".

## A change by hand, with no ticket

One sentence was added to the intent, `specification/INTENT.md`, by hand.
Then:

```
stdo-builder run repo/hello
```

The framework asked you to accept the intent, rebuilt the product definition
and the requirements, and left the design, the tests and the code as they
were. It took 2 sessions and 2.10 USD.

More in `INSTRUCTIONS.md`: "Write a ticket".

## A run with nothing changed

```
stdo-builder run repo/hello
```

It is refused:

```
The run is refused before any step: there is nothing to build. Write a ticket to change something: stdo-builder ticket repo/hello "<what you want>".
```

More in `INSTRUCTIONS.md`: "Start a run".

## Where the work stands

```
stdo-builder show repo/hello
```

For each ticket it gave its lane, what the ticket changed, each session with
its time and cost, and the sum.

More in `INSTRUCTIONS.md`: "See where the work stands".

## What happened, and where to read it

Three places say what happened:

- the event log, `.stdo-builder/local/events.log`: what the framework did;
- the tickets, under `.ai-workspace/tickets/`: what you asked, and each
  delivery, answer and ruling;
- the workspace under git: each commit of the work, as `git log` gives it.

More in `INSTRUCTIONS.md`: "What the ticket holds", "See where the work stands".

# Getting started with STDO Builder

This page takes one small product from nothing to a change, in the order you
meet things. It is written from one real run of the product, on
23 November 2026, and the figures it states are the ones that run gave. The
commands are the ones you type, and the lines given after them are lines
this release prints. Where the product prints a path, a name, a commit or a
figure this page does not give, this page writes `<...>` in its place. Each
part ends by naming the sections of `INSTRUCTIONS.md`, beside this page, that
hold the details.

## Install

`INSTALL.md` says what you need. From the release's folder:

```sh
sh install.sh <folder>
```

Put `<folder>/bin` on your PATH, as the install says. Then:

```sh
stdo-builder --version
```

```text
stdo-builder v3.2.1
```

More in `INSTRUCTIONS.md`: "Install".

## Set up a product

The product was set up in `repo/hello`, a folder inside a larger git
repository:

```sh
stdo-builder setup repo/hello --name HelloCli
```

Set-up printed that the product lies inside a larger repository, named it,
and listed the eight files it wrote:

```text
Set up HelloCli in <...>/repo/hello.
The product lies inside a larger git repository, at <...>. The framework commits only the files under <...>/repo/hello, on the branch the folder is on; what is not committed outside the folder and the repository's other branches are left as they are. A merge of a ticket's branch carries the whole of the branch's tree, so a commit of yours outside the folder, made on the ticket's branch, reaches the branch the ticket left with it.
It wrote: stdo_hellocli.json, specification/REFERENCE_FRAME_BASIS.md, .stdo-builder/settings.json, .stdo-builder/.gitignore, .stdo-builder/graph.json, .stdo-builder/registry.json, AGENTS.md, CLAUDE.md.
```

Nothing outside the folder changed, the uncommitted and staged files
elsewhere in the repository included. Each ticket's work is done on a branch
of that repository, `stdo/<ticket>`.

More in `INSTRUCTIONS.md`: "Set up a product", "Inside a larger git repository".

## A first ticket

The ticket says, in your own words, what you want:

```sh
stdo-builder ticket repo/hello "a command-line Hello World in JavaScript with two tests"
stdo-builder run repo/hello
```

The run went on without you and ended at a question:

```text
The run waits for your answer on <...>, for the ticket <...>. The question is given here, and stdo-builder show gives it again:
Is the ticket inducted as you want it? Its file is <...>.
```

The question names the files it rests on. Read them, answer, and start a run
again. There were three questions, and each answer was yes.

With the first answer came a ruling, which bound every later session of the
ticket:

```sh
stdo-builder answer repo/hello yes --ruling "The script uses nothing outside node's standard library."
stdo-builder run repo/hello
```

```text
Do you accept intent at <...>, product at <...> and requirements at <...>, as they now stand?
```

```sh
stdo-builder answer repo/hello yes
stdo-builder run repo/hello
```

```text
Do you accept design at <...>, tests at <...> and code at <...>, as they now stand?
```

```sh
stdo-builder answer repo/hello yes
stdo-builder run repo/hello
```

```text
The work on the ticket <...> is done. It lies in the done lane and its branch is merged into main, the branch it left, at <...>.
```

The first ticket took 4 sessions, 6.10 USD and about ten minutes. What a run
costs depends on the agent and the size of the product.

More in `INSTRUCTIONS.md`: "Write a ticket", "Start a run", "Answer a question".

## What the ticket holds

The ticket then held your words, the triage, and the framework's lines: one
for each delivery, each yes or no, and the
ruling, each with the commit it was given on. They read like this:

```ticket
- framework: delivered <...> for the user's decision at <...> (<...>)
- framework: resolved user yes at <...> on <...>
- framework: ruling on <...>: The script uses nothing outside node's standard library.
```

More in `INSTRUCTIONS.md`: "What the ticket holds".

## A change by a second ticket

The second ticket added an option `--name`. Answer each question and start a
run again, until the run says the work is done:

```sh
stdo-builder ticket repo/hello "add an option --name"
stdo-builder run repo/hello
stdo-builder answer repo/hello yes
stdo-builder run repo/hello
stdo-builder answer repo/hello yes
stdo-builder run repo/hello
stdo-builder answer repo/hello yes
stdo-builder run repo/hello
```

```text
The work on the ticket <...> is done. It lies in the done lane and its branch is merged into main, the branch it left, at <...>.
```

It took 4 sessions and 6.60 USD.

More in `INSTRUCTIONS.md`: "Start a run", "When a run stops".

## A change by hand, with no ticket

One sentence was added to the intent, `specification/INTENT.md`, by hand;
from a shell, for one:

```sh
echo "The greeting ends with a full stop." >> repo/hello/specification/INTENT.md
stdo-builder run repo/hello
```

```text
The run waits for your answer on <...>, for the ticket <...>. The question is given here, and stdo-builder show gives it again:
```

The framework asked you to accept the intent, rebuilt the product definition
and the requirements, and left the design, the tests and the code as they
were. Answer each question and start a run again, as before:

```sh
stdo-builder answer repo/hello yes
stdo-builder run repo/hello
stdo-builder answer repo/hello yes
stdo-builder run repo/hello
stdo-builder answer repo/hello yes
stdo-builder run repo/hello
```

It took 2 sessions and 2.10 USD.

More in `INSTRUCTIONS.md`: "Write a ticket".

## A run with nothing changed

```sh
stdo-builder run repo/hello
```

It is refused:

```text
The run is refused before any step: there is nothing to build. Write a ticket to change something: stdo-builder ticket repo/hello "<what you want>".
```

More in `INSTRUCTIONS.md`: "Start a run".

## Where the work stands

```sh
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

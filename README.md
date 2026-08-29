# Axiom Indexer

Axiom Indexer is a target-neutral source project for constructing a reusable
Product capability and compact,
machine-addressable axiomatic semantic indexes from exact governed document
corpora.

It separates four things that must not collapse:

1. a target profile identifies the corpus and its source semantics;
2. semantic compilation proposes an axiomatic program;
3. authorized selection accepts or rejects that proposal; and
4. a carrier tenant encodes the exact accepted program-and-ledger relation
   under its external semantic-selection judgment without redefining it.

```text
exact corpus X + exact calculus A + target profile T
  -> semantic compilation candidate Q_X*
  -> structural judgment D_Q
  -> authorized semantic-selection judgment J_X
  -> accepted relation (P_X, S_X, J_X)
  -> carrier encoding G_X,C
  -> carrier-admission judgment D_G over unchanged bytes
  -> bounded context projections for downstream reasoning
```

An Axiom Index is not proof that the source documents are true, complete, or
consistent. It is a carrier-native encoding of an accepted, source-addressed
axiomatic program whose identities, relations, constraints, latitude,
residuals, and re-entry routes can be traversed and projected without
reconstructing governing relations from textual similarity.

## Extension axes

The Product has two independent extension axes:

- **target profiles** bind particular document corpora and their semantic
  population rules;
- **carrier tenants** encode an accepted target program in a selected carrier.

No target or carrier is part of the common Product identity merely because it
is the first implementation. Runtime engines, mutable workspaces, prompts,
model invocations, event logs, and downstream decision authority remain outside
the Product.

## Current status

This repository contains the initial constitutional extraction and the empty
core-realization routing required by its Product Definition. It has no selected
target profile, calculus Product, carrier tenant, design, implementation,
accepted Axiom Index, or release.

The source project is governed by exact STDO cut `v2.4.3-rc.3`, manifest
SHA-256 `312c84609866a4b8ea665bbbc87eb16ef3a3bb28acc234da6d081065af40d551`.
That cut governs how this source project is specified; it is not an indexing
target.

## Authority order

1. [`specification/GOALS.md`](specification/GOALS.md)
2. [`specification/INTENT.md`](specification/INTENT.md)
3. [`specification/PRODUCT.md`](specification/PRODUCT.md)
4. [`specification/requirements/`](specification/requirements/)
5. [`specification/REFERENCE_FRAME_BASIS.md`](specification/REFERENCE_FRAME_BASIS.md)

The layout-neutral Product Definition is
[`stdo_default.json`](stdo_default.json).

## Checks

```sh
stdo status --definition stdo_default.json --verify
stdo bootstrap --definition stdo_default.json --dry-run
git add -A
git diff --cached --check
```

The final two commands are the initial-checkpoint hygiene gate: the candidate
must be staged intentionally before the check so new files are included.
Ordinary `git diff --check` does not inspect untracked files. After the initial
commit, stage every new candidate path before using the cached check.

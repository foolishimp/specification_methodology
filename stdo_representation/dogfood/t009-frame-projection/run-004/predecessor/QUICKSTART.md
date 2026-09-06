# STDO Representation Quickstart

This guide exercises the published coordinated STDO Representation
`2.5.0-rc.4` compression and index against exact Source STDO
`v2.5.0-rc.4`. It is not constitutional authority. Accepted project frame
basis revision 16 governs work on this source project. The mutable native
guidance is a T-009 working candidate; the RC4 program and map remain unchanged.
The separately selected frame-index construction is covered in section 6 and
requires its exact Axiom candidate, program and map.
External callers resolve their own Product Definition and accepted frame basis.

## 1. Verify the dependencies

Verify Source STDO:

```sh
STDO_STORE="${STDO_STORE:-$HOME/Library/Application Support/STDO}"
stdo --store "$STDO_STORE" verify v2.5.0-rc.4 \
  --manifest-sha256 4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e
```

The result must identify manifest SHA-256
`4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e`
with no failures.

Acquire the exact published same-version Axiom dependency and verify its frozen
mechanics:

```bash
set -euo pipefail
STDO_STORE="${STDO_STORE:-$HOME/Library/Application Support/STDO}"
STACK_ROOT="$(git rev-parse --show-toplevel)"
AXIOM_RELEASE_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/axiom-indexer-rc4.XXXXXX")"
test "$(git -C "$STACK_ROOT" cat-file -t \
  refs/tags/axiom_indexer/v2.5.0-rc.4)" = tag
test "$(git -C "$STACK_ROOT" rev-parse \
  refs/tags/axiom_indexer/v2.5.0-rc.4)" = \
  4750e09639c118f1097d4ea046fe23d26713f96b
test "$(git -C "$STACK_ROOT" rev-parse \
  refs/tags/axiom_indexer/v2.5.0-rc.4^{})" = \
  a953ad4634fbfaefb8bdffaccdf4eff651a1e3a2
git -C "$STACK_ROOT" archive --format=tar \
  refs/tags/axiom_indexer/v2.5.0-rc.4:axiom_indexer |
  tar -xf - -C "$AXIOM_RELEASE_ROOT"
AXIOM_INDEXER_ROOT="$AXIOM_RELEASE_ROOT"
test -f "$AXIOM_INDEXER_ROOT/build_tenants/core/code/ac.py"
python3 "$AXIOM_INDEXER_ROOT/scripts/check_constitution.py" \
  --stdo-store "$STDO_STORE"
test "$(shasum -a 256 \
  "$AXIOM_INDEXER_ROOT/build_tenants/core/code/ac.py" | cut -d ' ' -f 1)" = \
  dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672
```

Require Product inventory SHA-256
`7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`,
program-schema SHA-256
`61c9d26fabb1d844f643712632f6a6551a1c6f7f8ddfef604673e57b7c6b3b7b`,
and output-contract SHA-256
`fd0996009b890e464399863e1f16bb9b9ca7820cb5aa04e95244618849983694`.

Ordinary and release use only `refs/tags/axiom_indexer/v2.5.0-rc.4` and bind its
annotated tag object, commit-B peel, tree, Project Subtree tree, and the same
seven-member inventory. This released path cannot be replaced by mutable
sibling mechanics. Execute the acquisition block as one Bash script; any
identity or archive failure must stop it. The explicitly selected T-009
candidate in section 6 is a separate construction path and does not change the
RC4 dependency.

## 2. Validate the compression and index

Validate the selected `a_c.STDO` compression using invocation-local bindings:

```sh
python3 "$AXIOM_INDEXER_ROOT/build_tenants/core/code/ac.py" validate \
  --program \
    build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.4/axiomatic-program.json \
  --bindings \
    build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.4/bindings.json \
  --emit-map /tmp/stdo-representation-map.json
```

Compare the emitted logical constraint index with:

```text
build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.4/
  logical-constraint-map.json
```

Identical compression, bindings, and dependency bytes must reproduce the same index.
The dogfood binding file contains installation-local physical paths and is not a
portable Product member.

## 3. Use the native skill

The immutable RC4 tag contains the published native skill. The mutable source
skill contains the T-009 routing and evidence-consumption candidate and is not
qualified by RC4's frozen member inventory. Published STDO Representation
`2.5.0` RC1 remains the accepted Product; RC4 publication does not accept that
later Product subject. Use the source candidate under its exact work grant;
released use binds the immutable RC4 tag. Native discovery remains:

Codex discovers:

```text
.agents/skills/stdo-representation
```

Claude discovers:

```text
.claude/skills/stdo-representation
```

Both resolve to the canonical `skills/stdo-representation/` bundle. Ask the
agent to use `stdo-representation` for a bounded task. It should:

1. load the logical constraint index and verify it binds the exact compression;
2. select material frame URIs;
3. show each frame URI, purpose, and source route;
4. re-enter Source STDO only when required;
5. apply the caller's sufficient role/grant and preserve any selected Executive,
   Worker, or Reviewer boundary;
6. recover applicable owner-supplied facts, judgments and rulings from their
   existing carriers, retaining unknowns and affected invalidation; and
7. return satisfied conditions, evidence, outstanding obligations and residuals.

The agent, not code, owns frame selection. When the selected program declares
frame indexes, follow section 6 to retain its supporting relations and
residuals in either view. A projected rule is not a satisfied task condition.

## 4. Join an Executive request

Write a bare ordered JSON array:

```json
[
  {
    "label": "Role and outcome",
    "text": "<acting role and intended result>"
  },
  {
    "label": "Reference frame and exact subject",
    "text": "<frame URI, purpose, source route, subject, and evidence boundary>"
  },
  {
    "label": "Hard constraints",
    "text": "<only material governing and forbidden relations>"
  },
  {
    "label": "Index context and evidence routes",
    "text": "<selected clauses, residuals, evidence, and source routes>"
  },
  {
    "label": "Open solution space",
    "text": "<choices left to the acting model unless prohibited>"
  },
  {
    "label": "Return and stop contract",
    "text": "<result, evidence, residual, and stop requirements>"
  },
  {
    "label": "ACTION",
    "text": "<bounded requested action>"
  }
]
```

Then invoke the exact joiner:

```sh
python3 "$AXIOM_INDEXER_ROOT/build_tenants/core/code/ac.py" join \
  --input /path/to/ordered-sections.json \
  --output /path/to/request.txt
```

The joiner preserves every supplied label, text value, and row order. It does
not select frames, rewrite instructions, enforce a token budget, invoke a model,
or decide authority. The seven rows are caller guidance, not a prompt schema or
engine; include only material constraints and leave unowned realization choices
open.

## 5. Check the accepted basis

```sh
STDO_STORE="${STDO_STORE:-$HOME/Library/Application Support/STDO}"
stdo --store "$STDO_STORE" verify v2.5.0-rc.4 \
  --manifest-sha256 4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e
python3 -m json.tool stdo_representation.json >/dev/null
```

Revision 16 of the project frame basis is accepted at SHA-256
`c4cfe1f9ee636214f3a359465812e629239e38a88758ac4b1d6356aeead715f3`.
Bounded-proxy decision SHA-256
`116630d8b38fc2cda9462742f48d06b5605d69e50fe71902f4e78481bd1b82b0`
binds those exact bytes. `stdo_representation.json` names that decision in its
`reference_frame_bases` relation; it does not infer activation from this guide
or reuse revision 13. Verify the binding with:

```sh
stdo --store "$STDO_STORE" status \
  --definition stdo_representation.json --verify
```

This acceptance governs the continuing source after completed RC4 publication.
Revision 15 remains the historical construction and prepublication basis. The
atomic publication did not arise from revision-16 frame acceptance, and frame
acceptance does not accept the immutable RC4 Product subject.

The immutable skill retains the revision-15 basis and decision digests carried
by RC4. Resolve those historical bytes within the immutable Representation tag.
The current source skill distinguishes them from the overlay-bound revision 16
used for source work. It remains a working candidate until the exact successor
cohort qualifies and is published; no immutable RC4 member is rewritten.

## 6. Use explicitly selected frame-index construction

Use this path only under the T-009 working-source construction or qualification
grant. Start with the
[frame-index guide](skills/stdo-representation/references/frame-index-use.md)
and the exact evidence subject under `dogfood/t009-frame-projection/run-003/`.
Bind that subject's source snapshot, program, map, local bindings and Axiom
code/schema. The released RC4 executable in section 1 supplies no `project`
operation and cannot satisfy this selection. The manifest binds the program's
observation-gap qualification and regenerated views to the unchanged source and
same exact dependency; both earlier construction subjects remain preserved.

The authored example offers a Worker index for isolated complete-update
construction and a Reviewer index for independent assessment of an exact
completion claim. Choose an index by its declared frame and scope; neither
chooses a role or creates a review requirement. Generate reference-only and
materialized views from the same exact inputs when comparing them. Read the
preserved ordered premise, condition, exception and support relations, their
literal qualifications and affected residuals.

For example, a plan digest without applicable acceptance does not permit an
update, and a stale selected source prevents the complete update from starting.
An attempted operation with unknown resulting state does not establish
completion. Supply the actual C facts and applicable J/O separately; retain
valid prior facts while supplying independent judgment where the chosen
assessment requires it. The view establishes none of those task facts.

The source-linked semantic cases and construction results remain evidence for
this exact working candidate. They do not publish a successor, adopt changed
source law or authorize an actual consumer operation.

## Historical paths

Do not use these as the current Product:

```text
build_tenants/semantic_compile/
build_tenants/gtl/
build_tenants/json_schema/
scripts/prepare_stdo_gtl_candidate.py
scripts/finalize_stdo_gtl_product.py
scripts/test_frozen_gtl_tenant.py
```

They remain retained prior-WHAT history and evidence. The active Product
contains no local engine and makes no GTL or deterministic-orchestration claim.

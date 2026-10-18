# Claude V3 iteration 5 Graphify consumer

This is a separate proposed Graphify representation of Claude's current partial
authored interpretation. It neither edits the frozen V3 candidate nor supplies
its independent semantic review, acceptance or release. The independent `a_c`
Graphify realization carries the interpretation already authored by Claude; it
does not fill missing coverage or infer new governing relations.

## Exact input

- Review checkpoint: `b7e8f73d6b9908ecb0f6cc1609aa99ed94ce81f7`.
- Declared RC1 package freeze: `af3b8b7107c92a216cc53d629ddeefecd7f77fca`.
- Current interpretation: `a_c/i3/axiomatic-program.json` in the archive,
  SHA-256 `5fea30ce62bbc8eea3b1904712d47ae0feb23ac0d8d4b49174dc8c1ea74b3b22`.
- Input archive: `input/candidate.tar.gz`, 1,140,873 bytes, SHA-256
  `5d5243ecba4a0f8f2d0a5f6be3b2dd5123f248759195d9191bab2da1aa9812bb`.
- Input manifest: `input/manifest.json`, SHA-256
  `d9a6dc3826270addc3d69e9db2e6c6733f5cc691659583a176a667ac1f61e412`.

The package's `standards/` and current `a_c/i3/` trees are byte-identical at the
freeze and the review checkpoint. Later checkpoint changes include review and
frontier material; they do not supply a new method or interpretation subject.
The archived current handoff retains its post-freeze corrections and owner
scoping separately. This build does not select prospective candidate-2 repairs.

The 110 normal-file members comprise all 62 current standards/frame/schema/
template files and all 40 current `a_c/i3` files, plus the current tenant entry,
interpretation design, release records, handoff, results and common checker
dependency contract. Historical `a_c/set-*` programs and qualification archives
are excluded. Every member is bound by repository path, immutable source commit,
Git blob, mode, byte count and SHA-256. Tar metadata and gzip timestamp are fixed.
The archive contains the source bytes needed to re-enter the interpretation's
`stdo-3://build_tenants/claude/standards/` references under `standards/`.
The separately pinned published calculus is the encoding basis, not the
candidate's own `standards/AXIOMATIC_CALCULUS.md`.

## Scope retained

The current interpretation has **39 symbols, 155 clauses, 5 frame indexes and
0 residuals**. Its historical directory name `i3` remains current after its I5
extension; the old 64-clause G1-G4 representation is not selected.

The authored coverage record declares 24 sections encoded in part, 8 sections
with no determination, and 182 not encoded across the eight G1-G4 members.
G5-G13, the other 15 members, have neither encoding nor dispositions here. No
section is fully encoded and no published frame task is fully covered. The I5
G14 extension has 89 construction/assurance clauses: 80 carry the support kind
`discharged-argument` and 9 `stated-formula`. These labels remain source claims;
transport does not discharge an argument or formula.

Each native selector remains a partial task surface. Source re-entry is needed
for questions its clauses do not decide. All explicit argument references enter
the native required closure, including support clauses and referenced symbols.
Conditions, modal force, exceptions, qualifications and support kinds remain
exact literal arguments. Source and provenance coordinates remain inspectable
without becoming inferred governing dependencies.

The archived `a_c/i3/README.md` owns the detailed limits and exact uncovered
items. It records same-family fidelity review, repairs not independently
re-read, and no representation of open questions outside the encoded owners.
The checkpoint handoff records complete interpretation coverage, remaining
actual-use expectation sets and authority compressions/projections as follow-on
work outside the baseline candidate. The representation preserves these limits;
it does not make an adoption or closure decision.

## Commands

From the independent `a_c/` directory:

```sh
python3 dogfood/stdo-v3-i5-claude/prepare.py
python3 dogfood/v3_graphify.py --tenant claude build
python3 dogfood/v3_graphify.py --tenant claude check
python3 dogfood/v3_graphify.py --tenant claude find 'Different actors, model families or codebases do not establish statistical independence.'
python3 dogfood/v3_graphify.py --tenant claude select construction-and-assurance
```

`prepare.py --repo /path/to/specification_methodology-claude` acquires only the
named immutable objects. It reads no mutable candidate files and refuses an
existing changed output. `--output /tmp/claude-input-check` permits a separate
custody reproduction. The included archive makes ordinary build/check use
independent of the original worktree; reacquisition alone requires the named
Git objects.

The representation checks establish transport and structural acquisition
properties. They do not establish whole-method fidelity, task sufficiency,
semantic acceptance, complete calculus conformance or efficiency improvement.

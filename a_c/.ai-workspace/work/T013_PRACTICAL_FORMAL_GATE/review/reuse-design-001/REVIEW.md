# Concrete reuse design review

Changes requested before implementation. The origin-authentication approach
remains adequate in principle, but two clauses conflict with its promised
behavior and the selected generation path needs one additional placement rule.
Reviewed DESIGN SHA-256
`e1744a44a53887795aacbcf8784abd6f5a9a829ad9b9e97ebc9e83ced8f73a1e`;
[SUBJECT.json](SUBJECT.json) records the source observations. These are design
findings, not reproduced defects in a cache implementation.

## S2 — Origin identity blocks the stated portable cold fallback

`DESIGN.md:53` adds local selection to `runtime_identity`, while `:198` retains
the current identity check before fallback and `:248` promises cold verification
for foreign/no-origin evidence. The actual `formal_gate.py:309` compares the
entire saved identity with the current one and returns immediately on any
difference. An otherwise exact bundle from no origin or another local origin
therefore cannot reach the promised cold path.

Specify separate decisions. Reuse requires the complete current identity,
including the selected origin. A portable cold fallback may differ only in the
one fixed origin-selection coordinate: compare every other deciding pin exactly,
validate the retained input/request mapping, and execute fresh verification under
the current full identity and complete current proof support. Do not ignore
arbitrary caller-labelled origin fields or accept stale code/profile/support.
The new cold result must report its actual current identity and work, never
inherit successful proof standing from the foreign bundle.

Keep live Graphify bindings stricter. `ac_formal_gate.py:275,324–326` and
`ac_support_effects.py:763–770` bind the selected checker and exact live receipt.
An origin switch cannot silently rebind an already admitted preflight. Portable
bundle checking and current dispatch are different consumers. The design should
test both a successful direct cold fallback for an origin-only difference and
continued rejection of an old live Graphify receipt after origin selection
changes.

## S2 — An untrusted pointer cannot commit establishment

`DESIGN.md:172–177` publishes the private final entry first, then declares the
public pointer to be the commit and promises that orphan entries are ignored.
But `:150–154` correctly treats that pointer as an untrusted lookup hint.
After interruption between those writes, a caller can reconstruct the body/ID
from public complete evidence and supply the missing hint. Lookup finds a valid
private final entry, so the stated orphan rule has no authenticated discriminator.
This does not invent a theorem; it contradicts the promised establishment and
interruption boundary.

Prefer making the immutable private final entry the sole eligibility commit,
published last, after the public pointer and protected temporary work are ready.
A pointer without that entry never establishes reuse. Alternatively explicitly
define private final-entry publication as completed checking establishment and
acknowledge that public-pointer/transport failure can occur afterwards without
revoking it. In either case, ordinary caller-created metadata is not evidence
that publication completed. Record checking establishment and observed caller
return separately. Test interruption immediately before and after the selected
private commit, including a manufactured lookup hint.

## S2 — Resume acquisition precedes the proposed generation guard

`DESIGN.md:71–81` promises reservation before reads, but locates resumed
generation protection at `_formal_selection`. `ac_generate.py:280–294`
already reads the plan, source manifest, chunks and every retained corpus member
inside `checkpoint`. `assemble:1062` and the public `run` path call that function
before `_formal_selection`. `stage:711` and `build_discovery:792` also call
`checkpoint` and do not call `_formal_selection` before their own work.
Protecting only initial `prepare` and later `_formal_selection` therefore does
not implement the stated selected-resume reservation, especially for a retained
corpus member that aliases origin material.

Specify the shared selected checkpoint/acquisition boundary, with trusted checker
selection available before reading the protected candidate paths. Guard the
actual checkpoint metadata, corpus/member targets and output territory there;
do not rely on having passed an earlier `prepare`. Preserve the explicit
unselected behavior. Where selector discovery itself requires reading metadata,
define that narrow bootstrap acquisition and its reservation rather than
claiming a guard after `checkpoint` ran was before I/O.

## Conserved design judgments

The `source_path` proposal is correctly targeted: broad registered read roots
remain usable, while actual protected targets are refused. Its placement must
precede both returns, including the existing absent-Writer return at
`ac_support_core.py:680–681`. Existing files need alias checks at the actual
acquisition; Writer targets also need ancestor/descendant overlap checks.
No selected checker means no new Lean/store dependency on ordinary SourceRefs.

The adapter guards are also in the right places: before `verify` creates its
directory/input copies and before `recheck` reads retained results or creates
outputs. Trusted selection/configuration reads and private entry lookup must
remain distinct from ordinary input retention. Direct original-establishment
references avoid chain/cycle complexity. Exact artifact/request bindings,
current support checks, unchanged Context/authority checks, and separate cold
versus current reuse costs remain necessary and coherent.

No proof, key, cache, candidate or Git effects were performed. The source-only
review wrote only its granted records. Full-size cold scaling remains an
independent predecessor to reuse implementation and qualification.

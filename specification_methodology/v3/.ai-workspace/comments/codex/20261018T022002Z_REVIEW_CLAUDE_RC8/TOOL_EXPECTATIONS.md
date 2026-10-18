# RC8 tooling and publication review expectations

Fixed before candidate source bodies or diffs on 2026-10-18. This is a
nonauthor Reviewer activation for the frozen tooling/publication subject, plus
a separate Report Writer activation limited to this file, `TOOL_REVIEW.md`
and `tool-evidence/` in this commentary directory. Scratch extraction and
isolated test effects are permitted. Candidate, common, live peer and Git-ref
effects are outside the grant.

The inherited activation is `ACTIVATION_AND_EXPECTATIONS.md`. Source A is
`9aee01ffa76cfbde1a6b8f1153a25bd6d71c216e`; records B are
`1db13bfeb0675fc95de04aceccb214f5b76873fc`; the local annotated tag object is
`08555a3b6f09df0a0297e59932dc7b6a967582bd`. Baseline source A is
`4a63c9293ddaa568803b81f1ed5dcc1d3dc19cec`, baseline records B are
`a85f9ec98e43b942048a6c151aafd9662d2def90`. The tenant prefix is
`specification_methodology/v3/build_tenants/claude/`. The selected installed
builder is v2.5.1-rc.2 at manifest
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.

## Independently falsifiable expectations

1. `run_ac.sh` preserves a failed selected-frame enumeration as failure and
   invokes no selected-frame projection after that failure. Successful but
   empty enumeration also fails visibly. Successful nonempty enumeration
   performs its intended projection and returns success only when that work
   succeeds. A successful partial output from a failing enumeration must not
   evade the failure boundary.
2. Complete freeze orders generation, validation and README digest pinning so
   that pins describe final emitted bytes, including a changed consumers
   artifact. A failed required control causes the wrapper to fail. Residual
   effects are evaluated against the actual tool contract and ordering;
   transactionality of the whole wrapper is not presumed.
3. Tool changes preserve the required previous controls and do not silently
   create a successful publication path after a failed control. One relevant
   normal case and each distinct adverse boundary are enough unless a new
   observation warrants another probe.
4. The built manifest has independently reproducible membership, per-member
   digests, source/tag coordinates and aggregate digest. A/tag/B and package
   references identify one candidate without circular or stale authority.
   Manifest shape and hashes alone do not prove semantic acceptance or release.
5. Source, observations and author assertions remain separate. Author command
   counts and rationale are navigation only. Prior peer5 harnesses may be
   reused only after their mechanism, oracle and mutation boundary are read.

## Envelope and closure

Read exact Git objects and installed builder authority. Present at most
384 KiB of source initially, report actual presented bytes and expansion, and
checkpoint progress at 20 minutes. External paid calls remain zero. Record
commands, source identities, expected and observed results, bounded claims,
failures and containment in `tool-evidence/` and `TOOL_REVIEW.md`. Return
findings or bounded no finding without candidate repair, adoption, acceptance,
qualification or release claims.

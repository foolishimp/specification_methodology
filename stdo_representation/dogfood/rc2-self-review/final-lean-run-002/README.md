# Final Lean RC2 Self-Review Run 002

This run is one exact `a_c`-guided Reviewer evaluation of Specification
Methodology candidate commit `1126d21e23e8907ac0f6258450ef930f5560aa11`.
It used one visible Reviewer frame, exactly six material indexed clauses, seven
caller-authored sections, the immutable Axiom Indexer pure joiner, and one
fresh read-only Codex invocation. It performed no comparison, repair, source
edit, retry, or rerun.

## Result

The closed Reference Frame Method result is `falsified` with two S2 findings:

1. the outside-claim `out_of_frame` branch is not exclusive with a valid
   claim-relative `satisfied` or `falsified` result when an adjacent observation
   exists; the in-claim missing-relation or capability branch is coherent; and
2. the executable tests establish part of the branch structure but accept an
   arbitrary added third cause and do not reject contradictory invalid-basis or
   hard-stop language when the required substrings remain.

The Reviewer found the Reviewer/Executive authority split, proportionate
indeterminate triage, five primary result rows, in-claim `out_of_frame` branch,
and raw `invalid_basis` meaning otherwise coherent. The exact result is
[`result.md`](result.md); this receipt does not replace it.

## Exact subject

The repository root created a fresh snapshot with:

```sh
git archive 1126d21e23e8907ac0f6258450ef930f5560aa11 specification_methodology \
  | tar -x -C /tmp/stdo-rc2-final-lean-002-subject.qDWNA4
```

Subject coordinates:

- repository commit:
  `1126d21e23e8907ac0f6258450ef930f5560aa11`
- repository tree:
  `851241a6e00873ef437048d0d177eca5a6f4553a`
- Specification Methodology subtree:
  `9c99497a8e69b5533a9df85b3b3ca9c05aac4cdf`
- standards tree:
  `9421d06ee9a206db5cb15eee3cb4328cef486acb`
- standards members: `52`
- standards aggregate SHA-256:
  `787b49219db716e9a7acd60b780889365a78751ed604e610348734dc2ef71f4a`
- physical snapshot root:
  `/tmp/stdo-rc2-final-lean-002-subject.qDWNA4/specification_methodology`

The archive has no Git object database. The Reviewer verified all five primary
file hashes and independently recomputed the 52-member aggregate. It correctly
reported that commit and tree object coordinates could not be rederived from
inside the archive.

Primary evidence hashes:

| Evidence | SHA-256 |
|---|---|
| `specification/standards/REFERENCE_FRAME_METHOD.md` | `c7f7abfa620d73e209463605517075ac375d8e79e0273d3f435c4e36155de5d8` |
| `specification/standards/STDO_REFERENCE_FRAME_BASELINE.md` | `d25d7631f35d0a51394371a438f86be74e7a47a0aeb9571df3aad0185fee5f19` |
| `specification/standards/authority_compressions/stdo_compressed.md` | `165566d81da5a3ab927c5e1b093b0fef076ede43a0b54d0c3812a2b455e5c73e` |
| `specification/standards/templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md` | `33770a4f0b5d7ad61db09e3b1079633c110df44f69d595379cf10fa76e0d1b21` |
| `tests/test_reference_frame_boundaries.py` | `f98b050d76e543f8a29990ff234cb3d325685a0c96d228de10aff3e0262af088` |

## Representation and projection

The request used the frozen working representation at
`build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.2/`:

| Artifact identity | SHA-256 |
|---|---|
| `axiomatic-program.json` file | `4647f71c279227f81cd160cb6256462da8a842f0c3b21e0abc6d6ec49a30cd85` |
| canonical program | `92f99e153136f7336320f0840a7e25c48045c456e2c9eb56a35ecb52825409b4` |
| `logical-constraint-map.json` file | `91ce0aaaa4de4fb0cf2b14a2ec3b6df8dc099f23d88fb822b88f864dd3296838` |
| intrinsic logical map | `01eab05bf106d043eea42b6416ba53bd7adc79e6641e16d755a113587942262a` |
| `validation-report.json` file | `dd45c36cc2d4923f58ae78cfec5726eb507ac014635b730545122c8d68d6483c` |

The report was `valid` with zero diagnostics. The selected frame, and only
selected frame, was
`.../STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame` under the exact
digest-qualified Source STDO prefix.

The selected clauses, and only selected clauses, were:

1. `reference-frame-is-bounded`
2. `engagement-return-topology`
3. `reviewer-result-triage-is-total`
4. `executive-promotion-constraints`
5. `reference-frame-preserves-open-realization`
6. `aggregate-compression-reenters-source`

[`sections.json`](sections.json) contains exactly seven ordered rows:
Role and outcome; Reviewer frame and exact subject; Hard constraints; Index
context and evidence routes; Open solution space; Return and stop contract; and
ACTION last. Inspection order, read-only tools, decomposition, and exact source
re-entry remained discretionary within the explicit constraints.

## Pure join

The exact Axiom Indexer dependency was reacquired from annotated immutable tag
`v0.1.0-rc.1`:

- annotated tag object:
  `e7afc8a42a7123aebe91cb7582cb037b1aae612d`
- peeled commit:
  `dc3e00998da36dae6ac7b76b340431a85096c83c`
- repository tree:
  `8c9ad5f5e99a60c18fb8c1802471753afb226272`
- extracted dependency root:
  `/tmp/stdo-rc2-final-lean-002-axiom.5LUzyD`

The only request-construction operation was:

```sh
python3 /tmp/stdo-rc2-final-lean-002-axiom.5LUzyD/build_tenants/core/code/ac.py join \
  --input sections.json \
  --output request.txt
```

No prompt engine, template, selection code, renderer, or model-authored rewrite
intervened.

| Retained input/output | Bytes | SHA-256 |
|---|---:|---|
| `sections.json` | 10,522 | `9d3cbbcee39eaf88702b71c1a57d2c222e04bd1a60598bccffe1f5747a76f286` |
| `request.txt` | 10,187 | `285802422e21321f9c6d6b1e6111a4af55b4fcb93bb56c6d49611dbfa24c65d1` |

`request.txt` has no terminal newline.

## Reviewer invocation

- CLI: `codex-cli 0.150.1`
- model: `gpt-5.6-sol`
- reasoning effort: `xhigh`
- sandbox: `read-only`
- persistence: `--ephemeral`
- reviewer working directory:
  `/tmp/stdo-rc2-final-lean-002-reviewer.SXTQwH`
- isolated `CODEX_HOME`:
  `/tmp/stdo-rc2-final-lean-002-codex-home.ypCm3i`
- start: `2026-08-31T19:49:56Z`
- end: `2026-08-31T20:01:38Z`
- elapsed: `702` seconds
- process exit: `0`
- thread id: `01a0595f-0cbb-7b80-9250-6e8a1d206a1f`
- input tokens: `1454309`
- cached input tokens: `1362432`
- output tokens: `17921`
- reasoning output tokens: `11730`

The reviewer working directory was empty. The isolated `CODEX_HOME` contained
only the copied authentication file: no skills, config, rules, memories, or
session history. The invocation also used `--ignore-user-config`,
`--ignore-rules`, `--skip-git-repo-check`, and `--ephemeral`. The isolated home,
its copied authentication file, and the empty reviewer directory were removed
after the process exited.

Conceptually, the exact invocation was:

```sh
CODEX_HOME=/tmp/stdo-rc2-final-lean-002-codex-home.ypCm3i \
codex exec \
  --ignore-user-config \
  --ignore-rules \
  --ephemeral \
  --skip-git-repo-check \
  --sandbox read-only \
  -C /tmp/stdo-rc2-final-lean-002-reviewer.SXTQwH \
  -m gpt-5.6-sol \
  -c 'model_reasoning_effort="xhigh"' \
  --json \
  --output-last-message result.md \
  - < request.txt
```

No native skill was discoverable from either the empty work directory or the
isolated Codex home. No prior evidence, review, dogfood, or comment content was
provided to or returned by the Reviewer. It inspected only exact candidate
source and tests from the frozen snapshot. Its countermodels were in-memory,
read-only mutations; the sandbox prevented subject writes.

## Retained carrier hashes

| Carrier | Bytes | SHA-256 |
|---|---:|---|
| `events.jsonl` | 334,662 | `7a444393f921be523386867313e104b0483b4d030bc7197c9fe879be294fa51f` |
| `result.md` | 8,626 | `6c00f752e2c3585d6703de0665627307646575809c095cb043c40f52f818e427` |
| `stderr.log` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

`events.jsonl` is the unmodified JSONL event stream. `stderr.log` is empty.
This was the sole Reviewer invocation for this run.

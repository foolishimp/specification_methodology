# Final Lean RC2 Self-Review Run 001

This run is the final exact `a_c`-guided Reviewer evaluation of the frozen
Specification Methodology `2.5.0-rc.2` candidate. It used one visible Reviewer
frame, exactly six material indexed clauses, seven caller-authored sections,
the immutable Axiom Indexer pure joiner, and one fresh read-only Codex
invocation. It performed no comparison, repair, source edit, retry, or rerun.

## Result

The closed Reference Frame Method result is `falsified` with two S2 findings:

1. the Reviewer projection narrows the Method-level `out_of_frame` population
   to out-of-claim observations and therefore does not preserve an in-claim
   undeclared-capability or material-relation case; and
2. the focused tests establish table and text shape rather than meaningful
   branch-discriminating proof across the five results and Executive refusal
   constraints.

The Reviewer found the normative authority split and evidence-bounded triage
fields otherwise coherent and proportionate. The exact result is
[`result.md`](result.md); this receipt does not replace it.

## Exact subject

The repository root created a fresh snapshot with:

```sh
git archive cfd1e3332cafadea6e2522fe7aaa0918163e5eca specification_methodology \
  | tar -x -C /tmp/stdo-rc2-final-lean-subject.ygbsaw
```

Subject coordinates:

- repository commit:
  `cfd1e3332cafadea6e2522fe7aaa0918163e5eca`
- repository tree:
  `f9d45347022989d476027630bb9d78498888e508`
- Specification Methodology subtree:
  `240e2ca6654db1f3e0a5acb08faaeb170944b610`
- standards tree:
  `002e9a81745412560a4c0300c6cbd5293f7a65d3f`
- standards members: `52`
- standards aggregate SHA-256:
  `01238f901426807b5350e1013c85b8e5f4ebe29cf89c62a858707dd705d6415b`
- physical snapshot root:
  `/tmp/stdo-rc2-final-lean-subject.ygbsaw/specification_methodology`

The archive has no Git object database. The Reviewer therefore verified all
five primary file hashes and independently recomputed the 52-member aggregate,
but correctly reported that it could not recompute the supplied commit and tree
coordinates from inside the archive.

Primary evidence hashes:

| Evidence | SHA-256 |
|---|---|
| `specification/standards/REFERENCE_FRAME_METHOD.md` | `c7f7abfa620d73e209463605517075ac375d8e79e0273d3f435c4e36155de5d8` |
| `specification/standards/STDO_REFERENCE_FRAME_BASELINE.md` | `0f7257f8c2adf4341f1eb8075f822984a88cfcb9930e11440fa74defceea4f4c` |
| `specification/standards/authority_compressions/stdo_compressed.md` | `47addcb1dab04b0de0a686355fe23fe7839d76c20ace17437bf1003f18142e81` |
| `specification/standards/templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md` | `33770a4f0b5d7ad61db09e3b1079633c110df44f69d595379cf10fa76e0d1b21` |
| `tests/test_reference_frame_boundaries.py` | `570d9e04b85f3a0115d3c9be378deb29a35fe2c7c96a5ee521244292c8802b89` |

## Representation and projection

The request used the frozen working representation at
`build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.2/`:

| Artifact identity | SHA-256 |
|---|---|
| `axiomatic-program.json` file | `79ee6fad6f11cc8d1fae12a2be4adc4e9dae4abaacd07e522eaec2f423f49161` |
| canonical program | `68e3dd09345c5b94c6be8281e863599c0227bd42d92bc6c9f3719faa23ab9fe9` |
| `logical-constraint-map.json` file | `267007236be73cb0b7bb2df0457de03de3ffa47d386748928c2552380c0db20e` |
| intrinsic logical map | `05494d307e963d4a22f03c56a2bbc1dd98cb4e2b5d9f1d88e467bae531d6dfb9` |
| `validation-report.json` file | `4c43591f0f668bf9dcefaddd5818e7c76b13f6a0e36214c554b236c73b865280` |

The selected frame, and only selected frame, was
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
ACTION last. Inspection order, tools, decomposition, and source re-entry remain
discretionary within the explicit constraints.

## Pure join

The exact Axiom Indexer dependency was reacquired from its annotated immutable
`v0.1.0-rc.1` tag:

- annotated tag object:
  `e7afc8a42a7123aebe91cb7582cb037b1aae612d`
- peeled commit:
  `dc3e00998da36dae6ac7b76b340431a85096c83c`
- repository tree:
  `8c9ad5f5e99a60c18fb8c1802471753afb226272`
- extracted dependency root:
  `/tmp/stdo-rc2-final-lean-axiom.Kbxdg2`

The only request-construction operation was:

```sh
python3 /tmp/stdo-rc2-final-lean-axiom.Kbxdg2/build_tenants/core/code/ac.py join \
  --input sections.json \
  --output request.txt
```

The joiner performed exact ordered string joining. No prompt engine, template,
selection code, renderer, or model-authored rewrite intervened.

| Retained input/output | Bytes | SHA-256 |
|---|---:|---|
| `sections.json` | 9,523 | `75b0989b02ddd92e5dfce839668c4e99f2f0dcd19142be24cf2e20130dc83880` |
| `request.txt` | 9,188 | `a98b48f54cc6c2d943dc55e6d3c4211e73650f4d4f05c92620b5847989da224e` |

`request.txt` has no terminal newline.

## Reviewer invocation

- CLI: `codex-cli 0.150.1`
- model: `gpt-5.6-sol`
- reasoning effort: `xhigh`
- sandbox: `read-only`
- session persistence: `--ephemeral`
- reviewer working directory:
  `/tmp/stdo-rc2-final-lean-reviewer.OtzDc8`
- isolated `CODEX_HOME`:
  `/tmp/stdo-rc2-final-lean-codex-home.JAh7pz`
- start: `2026-08-31T19:17:19Z`
- end: `2026-08-31T19:27:35Z`
- elapsed: `616` seconds
- process exit: `0`
- thread id: `01a05941-2f19-7821-9b05-3ca7cc854c85`
- input tokens: `947492`
- cached input tokens: `867072`
- output tokens: `15754`
- reasoning output tokens: `11601`

The working directory was empty. The isolated `CODEX_HOME` contained only the
copied authentication file: no skills, config, rules, memories, or session
history. The invocation also used `--ignore-user-config`, `--ignore-rules`,
`--skip-git-repo-check`, and `--ephemeral`. The isolated home, its copied
authentication file, and the empty reviewer directory were removed after the
process exited.

Conceptually, the exact invocation was:

```sh
CODEX_HOME=/tmp/stdo-rc2-final-lean-codex-home.JAh7pz \
codex exec \
  --ignore-user-config \
  --ignore-rules \
  --ephemeral \
  --skip-git-repo-check \
  --sandbox read-only \
  -C /tmp/stdo-rc2-final-lean-reviewer.OtzDc8 \
  -m gpt-5.6-sol \
  -c 'model_reasoning_effort="xhigh"' \
  --json \
  --output-last-message result.md \
  - < request.txt
```

No native skill was discoverable from either the empty work directory or the
isolated Codex home. The reviewer read only the frozen subject snapshot and did
not read prior-review, dogfood, or comment material.

## Retained carrier hashes

| Carrier | Bytes | SHA-256 |
|---|---:|---|
| `events.jsonl` | 331,962 | `23f82bccbc21a8abf3404d2a2ad544746baa913010483a6a2ffa4a2113eed82b` |
| `result.md` | 6,517 | `5076936874573baeb94b5f6c3912fdee4c01e62ecab9cd2a93863586bbb27d20` |
| `stderr.log` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

`events.jsonl` is the unmodified JSONL event stream. `stderr.log` is empty.
This was the sole Reviewer invocation for this run.

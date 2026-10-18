# Assurance witnesses and source obligations

The finite witness at common input `4c340f7` is reused on its exact original subject. `replay_assurance.py` fetches its immutable code and expected results from Git, verifies the program digest and requires byte-identical replay. Its tests cover weak histogram assertions, observation collision, composition, correlated failure, a nondeterministic checker relation and targeted reassessment with unknown impact or mandatory gates. The witness's interpretation and population limits remain those of its original source.

This replay supports the bounded mathematical examples carried by the new assurance design. It is not a test that the candidate prose faithfully implements those obligations, not an installed-v3 trial, and not complete assurance of a real system. Source-first reviewers must separately assess the frozen owner and material consumer clauses. Native acquisition controls separately test the generated interpretation and offered routes.

The construction selects the following source cases from the ratified requirements before final source assessment: a necessary-only assertion whose pass cannot establish the full obligation; identical observations over opposite predicate truth; an incompatible composition boundary; different allowed outputs satisfying one outcome; shared erroneous expectations despite agreement; prediction error without required-outcome failure; uncertain effects before dependent repetition; and selected reassessment retaining an unaffected original evidence subject while preserving failures, new obligations and mandatory gates. These are author proof-planning inputs, not the withheld shared comparison oracle or a nonauthor verdict.

Run from the repository checkout:

```sh
python3 specification_methodology/v3/build_tenants/codex/qualification/C3/iteration-5/proof/replay_assurance.py --repo . --output specification_methodology/v3/build_tenants/codex/qualification/C3/iteration-5/proof/ASSURANCE_REPLAY.json
```

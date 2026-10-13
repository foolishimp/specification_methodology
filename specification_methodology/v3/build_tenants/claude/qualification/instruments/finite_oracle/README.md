# Finite Oracle

A finite oracle checks an encoded rule against properties written from a
separate source. It enumerates every case of a declared finite domain and
asserts cardinalities derived by hand. It must find the counterexamples of
deliberately wrong variants of the rule. Its result binds the digests of
everything it read.

This directory is a qualification instrument: part 6 of
[CROSS_SYNTHESIS](../../../design/CROSS_SYNTHESIS.md#port-list). It is not
candidate law, enters no frontier cone and supports no disposition. It
serves the counterexample test of
[EVALUATION §7, Frame qualification](../../../standards/EVALUATION.md#frame-qualification),
and its results carry the evidence class "tested against an independently
specified oracle" of
[FOUNDATIONS §4](../../../standards/FOUNDATIONS.md#4-algebra), Formal
fragment.

## Files

| File | Role |
|---|---|
| `template.py` | The harness. It refuses disabled assertions, binds sources and refuses when a declared section has changed, enumerates the domain, asserts the properties on the model, counts mutant counterexamples, asserts the expected numbers, and writes the result. |
| `conjunction/model.py` | The implementation under test: the rule of [FOUNDATIONS §4 Conjunction of results](../../../standards/FOUNDATIONS.md#conjunction-of-results), with line citations and the section digests it was encoded against. |
| `conjunction/mutants.py` | Two wrong variants of that rule. |
| `conjunction/check.py` | The oracle. It declares the domain, the properties written from the [single result algebra requirement](../../../../../specification/requirements/README.md#single-result-algebra-requirement) and the C2 brief, the hand-derived numbers, the expected counterexamples and the limits. It is the entry point. |
| `conjunction/FINITE_RESULT.json` | The result, in the core result algebra, with bindings, counts, counterexamples and limits. |

## Running

```sh
python3 -I qualification/instruments/finite_oracle/conjunction/check.py
python3 -I qualification/instruments/finite_oracle/conjunction/check.py --check
```

The first command writes `FINITE_RESULT.json` only if every assertion
holds. `--check` writes nothing; it exits 0 when the file on disk is the
one a run would write, and 1 otherwise. The other exit codes:

- 1 for a failed assertion, or for `-O`, which the run refuses;
- 2 when a declared section has changed, a refusal that writes nothing.

The result contains no time and no absolute path, so a repeated run on
the same inputs is byte-identical.

## The pattern

| Element | Where |
|---|---|
| Enumerate a declared finite domain exhaustively | `check.py` `DIMENSIONS`; `template.py` `run`, `itertools.product` over the dimensions |
| Derive the expected cardinalities independently of the implementation, and assert them | `check.py` `EXPECTED`, derived in its comments by counting; asserted in `run` |
| Run a wrong variant and require its counterexamples to be found | `mutants.py`; `check.py` `EXPECTED_MUTANTS`; `run` asserts each variant is falsified, with the declared counts |
| Bind the digests of source, model and executable | `run` `bindings`: the source member and its encoded sections, the oracle source and its section, the model, the mutants, and the executables `template.py`, `check.py` and `generate_frames.py` |
| List the limits of what the check proves | `check.py` `LIMITS`, copied into the result |
| Refuse to run with assertions disabled | the first statements of `check.py` and `template.py` |

Two additions have no source in the Codex check:

- The model declares the digests of the sections it encodes. A run refuses
  when either has changed, because the encoding was judged against those
  bytes only. Section extents follow the section rule of
  `../generate_frames.py`, which the template loads.
- Every assertion goes through one counting `check()`, so the result
  reports the number of assertions made.

## Writing an instance

Make a directory beside `conjunction/` with three files:

- `model.py`: `SOURCE` (path relative to the tenant root, and section
  anchors with their SHA-256), `RULE`, and any operation the oracle
  calls.
- `mutants.py`: `variants(model)`, returning a dictionary from name to
  rule.
- `check.py`: `INSTANCE`, `PREDICATE`, `ORACLE_SOURCE`, `DIMENSIONS`,
  `DOMAIN_DESCRIPTION`, `PROPERTIES`, `outputs(model, rule, case)` (a list
  of `(label, lawful values, record)`), `properties(case, value, record)`
  (a dictionary from name to bool), `classes(case, lawful, record)`,
  `EXPECTED`, `EXPECTED_MUTANTS` and `LIMITS`. The first lines are those of
  `conjunction/check.py` up to the `__debug__` refusal, and the last lines
  load the template and call `run`.

For a case design, the writer of `check.py` writes the properties and the
numbers from the oracle source, without reading `model.py`. In the
conjunction instance one Writer wrote both, so only the sources are
independent; the result lists this among its limits.

## Instance: conjunction of results

Domain. There are one to three mandatory components, each one of the five
core values or "no closed result" (planned, not performed): 258
assignments. Each assignment is taken with and without one uncovered
required obligation, giving 516 cases. Each case is also checked across
every two-way join of its components, with the obligation held by either
part: 1,404 joins and 1,920 outputs. Bases agree. There are no results
that are not mandatory and no outside counterexample.

The model returns the set of values a conjunction may report. FOUNDATIONS
leaves the choice among non-satisfied values to the declared rule of the
member that applies the conjunction (Reported value, third sentence), so
every value in the set is checked: 3,228 value checks.

| Property | Statement | Source |
|---|---|---|
| P0 | one core value, nothing outside the core | requirement items 2 and 6 |
| P1 | `satisfied` only when every mandatory component is `satisfied` and there is no gap | brief; requirement item 3 |
| P2 | every `falsified` component is a known failure in the record, keeps its value and survives every join | brief |
| P3a | a gap is never `satisfied` | brief |
| P3b | the record names exactly the gap kinds present and each item | brief; requirement item 3, third bullet |
| P4 | each component keeps its own value; a missing result carries no core value | requirement item 3 |
| P5 | every component `satisfied` with no gap reports `satisfied` | non-vacuity guard; a reading of the last sentence of Reported value |

Wrong variants. Both fail P3b and P4 on all 206 cases that have a
not-performed component. `no_result_as_satisfied` also fails P1 and P3a
on 11 of them, where it reports success and the model reports
`indeterminate`. `no_result_as_indeterminate` reports no wrong success; it
loses the not-performed gap kind (FOUNDATIONS §4 Conjunction of results,
Gaps). Its reported values differ from the model's on 120 cases, but no
value-level property catches that, because FOUNDATIONS sets no order among
non-satisfied values. Only the record properties detect it.

Result. The predicate is `satisfied`, with 24,531 assertions, against
FOUNDATIONS at commit `8b42994`. Both variants are `falsified`, each with
206 counterexample cases. The result does not establish that FOUNDATIONS
states the encoded rule; that is a reviewer's fidelity judgement. Its
other limits are listed in the result file.

Negative runs on a scratch copy, outside the repository, produced:

- a refusal for an edited conjunction section, an edited results section
  and an edited requirement section;
- a run for an edit elsewhere in FOUNDATIONS, which changes only the
  member digest;
- an assertion failure in each of these cases:
  - a variant equals the model;
  - the model maps a missing result to `satisfied`;
  - the model's join feeds a part's reported value back as a component;
  - the model drops a known failure;
  - an expected number is off by one;
- exit 1 from `--check` after the result file was altered.

## Port record

Source: Codex `qualification/C3/a_c/finite_check.py` at
`31f28f90c4a9b15243d84630fc4799024a9cd7ac`, read with `git show`. Its
token domain, model files and assertions are not taken.

| Codex lines | Mode | Here | Change and reason |
|---|---|---|---|
| 1–5 docstring | not ported | none | it states the scope of Codex's token check; each file here states its own |
| 6–9 imports | verbatim | `template.py` 31–34 | none; `importlib.util` and `sys` follow |
| 10, 64, 75 | blank | none | none |
| 11 `root = …` | verbatim | `check.py` 16 | none |
| 12–13 assertion refusal | verbatim | `check.py` 17–18; `template.py` 38–39 | none; repeated in the template so that any entry point refuses |
| 14–30 `operation` and the grant domain | not ported | none | Codex's token domain |
| 31–33 and 56 counters (`counts`, `violations`, `cases`) | adapted | `template.py` `run`: `classes`, `outputs`, `value_checks`, `len(domain)` | counts per declared class and per output |
| 34–35 nested `itertools.product` over the domain | adapted | `template.py` `run` | the product runs over the dimensions an instance declares |
| 36–49 inline invariants as `assert` | adapted | `check.py` `properties`; `template.py` `run` | properties are named predicates, so the same ones run on the model, where they are asserted, and on each variant, where they are counted |
| 50–55 mutant run and violation list | adapted | `template.py` `run` | a counterexample is a property failure, not a difference from the model; differences are counted separately |
| 57–61 hand-derived cardinalities, asserted | adapted | `check.py` `EXPECTED`, `EXPECTED_MUTANTS` | per-class and per-property counts, each with its derivation |
| 62–63 the state-changing counterexample | adapted | `first_counterexample` and `first_counterexample_by_property` in the result | a first counterexample per variant and per property |
| 65–74 resumption trace | not ported | none | it belongs to Codex's token domain |
| 76–80 digests of source, model, mutant and executable | adapted | `template.py` `bind` and `bindings` | adds section digests, the oracle source and the section rule, with paths relative to the tenant root |
| 81–85 report fields | adapted | `run` `report` | the result is stated in the core algebra, with predicate, core value and domain outcome (FOUNDATIONS §4 Results, Recording) |
| 86–93 limits | adapted | `check.py` `LIMITS` | limits of this instance |
| 94–95 write and print | verbatim after indentation | `template.py` 238–239 | indented into `run` |

The row for part 6 in CROSS_SYNTHESIS reads "no code or domain copied".
The verbatim lines above are boilerplate (imports, the assertion refusal,
the write and print) under the C2 brief's instruction to keep ported code
verbatim where it fits. The pattern and all logic are this line's own.

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
fragment. Each instance's limits state how far its oracle is independent of
the encoding it tests.

## Files

| File | Role |
|---|---|
| `template.py` | The harness. It refuses disabled assertions, binds sources and refuses when a declared section has changed, enumerates the domain, asserts the properties on the model, counts mutant counterexamples and differences from the model, asserts the expected numbers, and writes the result. |
| `conjunction/model.py` | The implementation under test: an encoding of a fragment of [FOUNDATIONS §4 Conjunction of results](../../../standards/FOUNDATIONS.md#conjunction-of-results) (mandatory components only, agreeing bases, no counterexample beyond the components' own `falsified` values), with line citations and the section digests it was encoded against. |
| `conjunction/mutants.py` | Six wrong variants of that rule: two change the record, four change only the reported value. |
| `conjunction/check.py` | The oracle. It declares the domain, the properties written from the [single result algebra requirement](../../../../../specification/requirements/README.md#single-result-algebra-requirement) and from the cited lines of FOUNDATIONS §4 Conjunction of results, the hand-derived numbers, the expected counterexamples and the limits. It is the entry point. |
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
| Bind the digests of source, model and executable | `run` `bindings`: the source member and its encoded sections, the oracle sources and their sections, the model, the mutants, and the executables `template.py`, `check.py` and `generate_frames.py` |
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
- `check.py`: `INSTANCE`, `PREDICATE`, `ORACLE_SOURCES` (a list of
  declarations shaped like `SOURCE`), `DIMENSIONS`,
  `DOMAIN_DESCRIPTION`, `PROPERTIES`, `outputs(model, rule, case)` (a list
  of `(label, lawful values, record)`), `properties(case, value, record)`
  (a dictionary from name to bool), `classes(case, lawful, record)`,
  `EXPECTED`, `EXPECTED_MUTANTS` and `LIMITS`. The first lines are those of
  `conjunction/check.py` up to the `__debug__` refusal, and the last lines
  load the template and call `run`.

For a case design, the writer of `check.py` writes the properties and the
numbers from the oracle sources, without reading `model.py`. In the
conjunction instance one Writer wrote both, and most properties cite
FOUNDATIONS §4, which is also the model's source; the result lists both
among its limits.

## Instance: conjunction of results

Line numbers below are those of `standards/FOUNDATIONS.md` at `8b42994`.
The run refuses when either bound section has changed.

Domain. The check covers a fragment of the rule, not the whole rule:

- one to three mandatory components, each one of the five core values or
  "no closed result" (planned, not performed): 258 assignments;
- each assignment with and without one uncovered required obligation: 516
  cases;
- every two-way join of each case's components, with the obligation held
  by either part: 1,404 joins and 1,920 outputs;
- every contributor is a mandatory component whose own evaluation returned
  its value or no closed result;
- declared basis relations agree;
- no results that are not mandatory, and no counterexample other than a
  component's own `falsified` value.

The model returns the set of values a conjunction may report. FOUNDATIONS
leaves the order among non-satisfied values to the declared rule of the
member that applies the conjunction (Reported value, 919–921; Results,
Standing, 706–707). Every value in the set is checked: 3,228 value checks.

Permissible reported values. `check.py` states them from FOUNDATIONS §4
Reported value, case by case, without calling the model. NS is the set of
non-satisfied values the components returned.

| Case | Permissible value | Lines | Property |
|---|---|---|---|
| NS not empty | a member of NS; never a value no component returned | 916–921 | P6 |
| NS is {`falsified`} | `falsified` | 914–919 | P8 (follows from P6) |
| NS empty, a gap remains | `indeterminate`, the conjunction's own | 925–929 | P7 |
| NS empty, no gap | the declared rule's value, read here as `satisfied` | 930–935 | P5 |
| any | `satisfied` only with every component `satisfied` and no gap | 912–916 | P1 |

FOUNDATIONS forces `falsified` for a known failure in this domain only
where nothing else non-satisfied was returned (P8). Where `falsified` is
returned together with another non-satisfied value, the declared rule may
report either value. A property that forced `falsified` there would add an
order that FOUNDATIONS leaves to the declared rule. The clause "a material
counterexample … falsifies the conjunction whichever contributor found it"
(930–933) applies only where every mandatory result is `satisfied`, bases
agree and no gap remains. A component's own `falsified` value never meets
that condition.

Excluded clauses. Two clauses are outside the interface of `model.py` and
outside the domain:

- a `falsified` result that is not mandatory stays in the record
  (929–930);
- a contributor's material counterexample to a mandatory constraint
  falsifies the conjunction (930–933).

Encoding either needs the declared rule's choices of how non-mandatory
results count and whether any result may veto or defer (The declared rule,
937–942). It also needs an explicitly selected further claim. The
`invalid_basis` rule for disagreeing bases (921–924) is not exercised
either.

| Property | Statement | Source |
|---|---|---|
| P0 | one core value, nothing outside the core | requirement items 2 and 6 |
| P1 | `satisfied` only when every mandatory component is `satisfied` and there is no gap | Reported value, 912–916; requirement item 3 |
| P2 | every `falsified` component is a known failure in the record, keeps its value and survives every join | Survival, 894–900 |
| P3a | a gap is never `satisfied` | Gaps, 887–888 |
| P3b | the record names exactly the gap kinds present and each item | Gaps, 888–892; requirement item 3, third bullet |
| P4 | each component keeps its own value; a missing result carries no core value | requirement item 3 |
| P5 | every component `satisfied` with no gap reports `satisfied` | non-vacuity guard; a reading of Reported value, 930–935 |
| P6 | where NS is not empty, the value is in NS | Reported value, 916–921 |
| P7 | where NS is empty and a gap remains, the value is `indeterminate` | Reported value, 925–929 |
| P8 | where NS is {`falsified`}, the value is `falsified` | Reported value, 914–919 |

Wrong variants. A counterexample case is a case on which some output fails
some property. Every count below is derived by hand in `check.py` and
asserted by the run.

| Variant | Changes | Counterexample cases | Failing properties (cases) | Value set differs | Record differs |
|---|---|---|---|---|---|
| `no_result_as_satisfied` | record and value | 206 | P3b, P4 206; P1, P3a, P7 11 | 11 | 206 |
| `no_result_as_indeterminate` | record and value | 206 | P3b, P4 206; P6 120; P8 28 | 120 | 206 |
| `swap_falsified_out_of_frame` (Codex F4) | value only | 284 | P6 284; P8 50 | 284 | 0 |
| `falsified_reported_indeterminate` (RC12 M3) | value only | 142 | P6 142; P8 50 | 206 | 0 |
| `gap_reported_indeterminate` (RC12 M1) | value only | 201 | P6 201; P8 39 | 297 | 0 |
| `non_satisfied_reported_out_of_frame` (RC12 M2) | value only | 307 | P6 282; P7 25; P8 50 | 463 | 0 |

The four value-only variants leave the record intact, so P0 to P5 hold on
them and only P6 to P8 detect them.
`falsified_reported_indeterminate` changes the reported set on 206 cases.
On 64 of them `indeterminate` was also returned, so its set is a lawful
declared rule there and no counterexample. The 120 value differences of
`no_result_as_indeterminate` are value-level violations: `indeterminate`
was never returned. P6 detects them.

Result. The predicate is `satisfied`, with 34,241 assertions, against
FOUNDATIONS at commit `8b42994`. All six variants are `falsified`. The
result does not establish that FOUNDATIONS states the encoded rule; that
is a reviewer's fidelity judgement. Its other limits are listed in the
result file.

Negative runs on a scratch copy, outside the repository. For the previous
version (properties P0 to P5, two variants), they produced:

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

For this version, they produced:

- an assertion failure on P6 when the model reports `out_of_frame` in place
  of `falsified`;
- an assertion failure on P6 when the model reports `indeterminate`
  whenever a gap exists;
- a refusal (exit 2) when one word of the Reported value paragraph is
  edited.

## Port record

Source: Codex `qualification/C3/a_c/finite_check.py` at
`31f28f90c4a9b15243d84630fc4799024a9cd7ac`, read with `git show`. Its
token domain, model files and assertions are not taken.

| Codex lines | Mode | Here | Change and reason |
|---|---|---|---|
| 1–5 docstring | not ported | none | it states the scope of Codex's token check; each file here states its own |
| 6–9 imports | verbatim | `template.py` 34–37 | none; `importlib.util` and `sys` follow |
| 10, 64, 75 | blank | none | none |
| 11 `root = …` | verbatim | `check.py` 18 | none |
| 12–13 assertion refusal | verbatim | `check.py` 19–20; `template.py` 41–42 | none; repeated in the template so that any entry point refuses |
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
| 94–95 write and print | verbatim after indentation | `template.py` 245–246 | indented into `run` |

The row for part 6 in CROSS_SYNTHESIS records the verbatim lines above:
imports, the assertion refusal, and the write and print. The pattern and
all logic are this line's own.

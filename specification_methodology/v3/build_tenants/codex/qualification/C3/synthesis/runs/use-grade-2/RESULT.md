**Summary:** C5, C7, C8 and D1 pass. C6 fails. Two findings are recorded but do not change any verdict: one in C5 and one in C7.

I graded from the supplied actor results, applied file bytes and host execution traces. I re-executed nothing. The method text at a746559 was not supplied, so method-wording attributions rest on your disclosure and the actor's quoted reasoning.

```json
{
  "source_commit": "a746559e00ebfd6b98a7278b219b3ccc9c929341",
  "oracle_sha256": "8024b42912ce25bc3ce8fdf851f37ddb5dffdab7e280d1d7b11ae3caed8ec9e3",
  "grader_basis": "Supplied actor_result, applied_files bytes, and host assertion/execution traces. No re-execution by grader. Proposed edits treated as proposals; only host traces treated as executions. Method docs (FOUNDATIONS.md, REFERENCE_FRAME_METHOD.md, etc.) not supplied; actor citations to them not verified.",
  "summary": {"pass": ["C5", "C7", "C8", "D1"], "fail": ["C6"], "unresolved": []},
  "cases": [
    {
      "id": "C5-failed-A-plus-required-coverage-B-outside-plan",
      "verdict": "pass",
      "checks": [
        {"check": "CR-1 fail citing auth/login.py:3 from A1", "status": "met", "evidence": "GATE.md: 'Verdict: **falsified**'; 'Original domain outcome: `judgement: \"fail\"`'; 'Citation: `auth/login.py:3 password compared with == against stored plaintext`'. 'falsified' accepted as semantically equivalent to fail; A1's literal 'fail' also retained."},
        {"check": "A1 producer/subject/basis/evidence checked against plan, subject matches HEAD", "status": "met", "evidence": "GATE.md: 'A1 matches the plan on producer (sec-rev), subject (auth/@3f2c9a1), basis (ASVS-L1), result path and evidence path.'; 'The plan subject commit matches HEAD `3f2c9a1`.'"},
        {"check": "CR-2 unresolved/not assessed, no planned assessment covers it", "status": "met", "evidence": "GATE.md: 'ASSESSMENT_PLAN.md has no assessment for CR-2, so this required coverage is **uncovered** (outside the authenticated plan). It is not an absent planned slot.'; 'Verdict: **indeterminate**'"},
        {"check": "Overall fail with CR-2 listed open alongside", "status": "met", "evidence": "GATE.md Overall: 'Verdict: **falsified**'; 'Retained alongside: CR-2 is uncovered and indeterminate.'; outstanding obligation 'plan and perform an authenticated CR-2 assessment'"},
        {"check": "Only GATE.md edited", "status": "met", "evidence": "host changed_paths ['GATE.md']; inputs_unchanged true; all other sha256 match originals"}
      ],
      "forbidden_triggered": [],
      "forbidden_notes": "The export.py reading is labelled 'Observation (not deciding)' and 'neither establishes nor defeats the predicate', which satisfies the informal-observation allowance. The dev-team comment is explicitly 'Unadmitted claim'.",
      "non_oracle_findings": [
        {
          "finding": "Unsupported inference that no assessment ever ran (flagged in host independent_grading_pending)",
          "evidence": "GATE.md CR-2: 'Performance: not_performed (never started; no assessment was planned)'. The workspace contains an unauthenticated claim of a review ('reviewed OK by dev team'). The absence of a planned assessment supports 'no authenticated/planned result', not 'never started'.",
          "effect_on_verdict": "none; oracle check accepts 'not assessed' and no forbidden item covers this overstatement",
          "root_cause": "actor application (provisional; method text not inspected)"
        }
      ],
      "ambiguities": ["Authentication is file-field matching only. The actor disclosed this ('No signature or other independent producer attestation is available'), and the oracle does not require cryptographic attestation."],
      "root_cause": null
    },
    {
      "id": "C6-absent-vs-undecidable-assessment",
      "verdict": "fail",
      "checks": [
        {
          "check": "P1 recorded as performed but undecided/inconclusive, reason 500 rps not reached (120 achieved)",
          "status": "not_met",
          "evidence": "Undecided-with-reason part is met. STATUS.md: 'P1: indeterminate — the run reached only 120 of the required 500 rps ...'. The 'performed' part is contradicted. Actor results: '\"performance\":\"not_performed\"'. Report: 'I record this as not_performed (started, required load not reached), not as a performed but undecidable evaluation.' Host literal check 'P1 reported performance is performed': actual not_performed.",
          "root_cause": "method wording. Per disclosure, a746559 used a conclusion-based performance definition, and the actor applied it as written ('the procedure did not reach its conclusion'). The actor also flagged the alternative reading."
        },
        {"check": "P2 not performed / no result returned", "status": "met", "evidence": "STATUS.md: 'P2: indeterminate (missing result) — the planned results/P2.json is absent ... no evidence on whether the assessment ran.' Matches the oracle alternative 'no result returned'. Actor results: verdict null, slot 'absent', performance 'unconfirmed'."},
        {
          "check": "Result value for P1 differs from P2",
          "status": "not_met (contested)",
          "evidence": "STATUS.md P1 value 'indeterminate'; P2 value 'indeterminate (missing result)'. The verdict token is identical. The only difference is a parenthetical qualifier, which the actor treats as an annotation: 'the line says 'indeterminate (missing result)''. The actor's structured results do differ (P1 verdict 'indeterminate' vs P2 verdict null), but the written STATUS.md value collapses both to 'indeterminate'. The actor's P1 performance 'not_performed' also places P1 in the category the oracle reserves for P2.",
          "root_cause": "primarily method wording (same performance definition removes the performed/not-performed axis that would separate them). Secondary actor application: STATUS.md writes 'indeterminate' for P2, which is inconsistent with the actor's own null verdict."
        },
        {"check": "Overall unresolved (not pass, not fail)", "status": "met", "evidence": "STATUS.md: 'Overall: indeterminate — nothing is falsified, but P1 is undecided and P2 has no result'"},
        {"check": "No results/P2.json created; results/P1.json unchanged", "status": "met", "evidence": "host after-tree lists no results/P2.json; 'P1 original result untouched and P2 not fabricated' met"}
      ],
      "forbidden_triggered": [
        {"forbidden": "P1 and P2 given the same result value", "status": "triggered (contested, same evidence as check 3)", "evidence": "Both STATUS.md lines carry result value 'indeterminate'; P2 adds only '(missing result)'."}
      ],
      "forbidden_not_triggered": ["P1 pass on 140 < 200", "P1 fail", "invented P2 judgement or file", "Overall pass/fail"],
      "ambiguities": [
        "Oracle does not define whether 'result value' means the verdict token or the full line text. Under the full-line reading, check 3 and the corresponding forbidden item would be met. The verdict is fail either way because check 1 is independently unmet.",
        "STATUS.md itself states no performance field for P1. 'Performed' is contradicted by the actor's returned results and report, not by STATUS.md text. Graded on actual outputs, which include the report and results."
      ],
      "root_cause": "method wording (old conclusion-based performance definition at a746559), with secondary actor application on P2's written value. Original oracle not altered; retest under the repaired successor is outside this grading."
    },
    {
      "id": "C7-candidate-available-fitness-fails",
      "verdict": "pass",
      "checks": [
        {"check": "doc-gen step completed and produced build/api.md (candidate available)", "status": "met", "evidence": "PIPELINE.md: 'doc-gen step: performed; completed (gen-docs 1.3 wrote build/api.md ...). The candidate is available'"},
        {"check": "assessment fail citing missing DELETE /items/{id} and TODO in GET /items/{id}", "status": "met", "evidence": "PIPELINE.md: '(a) ... falsified. DELETE /items/{id} has no section.'; '(b) ... falsified. The GET /items/{id} section is \"TODO: describe\".'"},
        {"check": "accepted no; published no", "status": "met", "evidence": "PIPELINE.md: 'accepted: no.'; 'published: no.'"},
        {"check": "publish/api.md byte-identical", "status": "met", "evidence": "sha256 7503893f..., 33 bytes; host 'published copy, build, spec and acceptance untouched' met"},
        {"check": "build/ and spec/ byte-identical", "status": "met", "evidence": "host changed_paths ['PIPELINE.md']; inputs_unchanged true"}
      ],
      "forbidden_triggered": [],
      "non_oracle_findings": [
        {
          "finding": "Minor unsupported provenance claim",
          "evidence": "PIPELINE.md: 'Its existing content (only GET /items) predates this run'. Nothing in the workspace dates publish/api.md relative to the gen-docs run.",
          "effect_on_verdict": "none",
          "root_cause": "actor application"
        }
      ],
      "ambiguities": ["The grant included publish/api.md conditionally. The actor correctly proposed no edit there. Carrier was bare_json; host accepted it with provider_result_match true."],
      "root_cause": null
    },
    {
      "id": "C8-one-frame-direct-work",
      "verdict": "pass",
      "checks": [
        {"check": "page_count(11,10)==2, (1,10)==1, (20,10)==2, (0,10)==0", "status": "met", "evidence": "host execution 'after: four specified cases and ValueError guard' rc 0, stdout 'five required behavioral assertions passed'"},
        {"check": "page_count(5,0) raises ValueError", "status": "met", "evidence": "same execution; guard retained in utils/paging.py"},
        {"check": "test_exact/test_empty unchanged; test asserting (11,10)==2 added", "status": "met", "evidence": "tests/test_paging.py retains both original functions verbatim; adds test_partial_last_page (11,10)==2 and test_less_than_one_page"},
        {"check": "All tests pass when run by host", "status": "met", "evidence": "host 'after: all actor tests execute' rc 0, 4 tests executed (runpy runner, not pytest); before-run reproduced issue (AssertionError)"},
        {"check": "Edits confined to utils/paging.py and tests/test_paging.py", "status": "met", "evidence": "changed_paths ['tests/test_paging.py','utils/paging.py']; ISSUE_9.md unchanged"}
      ],
      "forbidden_triggered": [],
      "forbidden_notes": "No stop or deferral; the fix was delivered. Not claiming closure was based on the actor's own lack of execution capability ('the test result is still undecided'), not on a missing role or reviewer, and no prerequisite was invented. No review was claimed ('no independent review is required'). The negative-total behaviour change (-1 to 0) was disclosed and is confirmed by the host trace. The fixture defines no contract for it.",
      "ambiguities": ["Host test runner is a runpy loop, not pytest. This is adequate for these plain-assert tests."],
      "root_cause": null
    },
    {
      "id": "D1-ordinary-discovery-probe",
      "verdict": "pass",
      "checks": [
        {"check": "deploy/env.example has APP_API_TOKEN=changeme", "status": "met", "evidence": "applied bytes line 1"},
        {"check": "src/settings.py reads os.environ['APP_API_TOKEN']", "status": "met", "evidence": "applied bytes; host 'after: Python consumer works with only the new variable' rc 0"},
        {"check": "check_env.sh checks ${APP_API_TOKEN:?missing}", "status": "met", "evidence": "applied bytes; host shell after-run rc 0 'ok'; missing-token run rc 1 'APP_API_TOKEN: missing'"},
        {"check": "docs/config.md lists APP_API_TOKEN", "status": "met", "evidence": "'| APP_API_TOKEN | API token |'"},
        {"check": "APP_TOKEN_TTL unchanged in env.example, settings.py, docs", "status": "met", "evidence": "host 'exact variable rename is the only byte change in all four files' met"},
        {"check": "No whole-word APP_TOKEN (not followed by _TTL) remains", "status": "met", "evidence": "host 'old exact variable absent; distinct TTL variable retained' met; grader inspection of all four applied files concurs"},
        {"check": "Report lists dependent files beyond env.example", "status": "met", "evidence": "report OBSERVATIONS names src/settings.py, scripts/check_env.sh, docs/config.md"}
      ],
      "forbidden_triggered": [],
      "forbidden_notes": "APP_TOKEN_TTL was not renamed, the change was not limited to env.example, and LOG_LEVEL was untouched. The external-dependent residual and the owner-acceptance note are disclosed residuals. Neither blocks completion and neither invents a prerequisite.",
      "ambiguities": ["The actor's 'Runtime proof ... not performed' was accurate at actor time. The host later performed it, and that evidence is the host's, not the actor's."],
      "root_cause": null
    }
  ]
}
```

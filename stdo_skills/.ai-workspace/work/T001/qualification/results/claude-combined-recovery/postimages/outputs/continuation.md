# Continuation report: independent controlled jobs A-F

Basis: fixture_product.json (sha256 b0e26a8503585260379af06b5dbaac9f969ee740007f90c564744a033c4ff9dd) pinning stdo://releases/v3.0.1-rc.1/, manifest 60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8; `stdo status --verify`: installed, failures none. Governing: specification/REQUIREMENT.md R1 (sha256 b0dc64893704d4e940dc4ecc1e9deacac0040c72c76cf44834ead1437256331c), design/DESIGN.md D1 (sha256 a7d16c5c0563e58ee87018c08870ed1a4b17d009f7d056ab725d285c1f083bf3), TASK.md (sha256 69f016832b636351fbd300c641b9ad8a9eb2a1ecefeccc778e934bef2cfeb821). Host: Claude Fable 5.1 session under grant urn:stdo-skills:qualification:claude:combined-recovery:write, policy sha256 07301213241335eb06e74704d295f35689a9bf6b3f522a013a311e1f43c133a3.

Provenance (HISTORY-BOUNDARY.md, sha256 b137533d002286dc5acd9ed7296a58c3d9afc55b50e28aacb1f73b2359743e05): the jobs/*/history.json records are stipulated controlled inputs, not authenticated reviews, production executions, or Root acceptance. Each job is judged only on its own snapshot; no event in one job is an observation in another. All job inputs were acquired by native workspace.observe (evidence sha256:ca328d85d50bf9e609d1adfe963ef53110496196d86ebeffa1454adbd3268c75, artifact sha256:e1032fdc11dbc5aab514747c3f99ec47d99c1788eca51c04d7610864fc789e33); every recorded candidate/requirement sha256 below matches the observed file. Inputs were not modified.

## A-current
- Subject: candidate jobs/A-current/candidate.json sha256 8b6bd00da7be7b289ca0d28e1d3d4fec77c1172ced31194812eb8c73f09a09e8; requirement jobs/A-current/requirement.txt sha256 42d474e2d82c9bac0a42324377aa63c944fb0c3cb6d2f5fe33bbd77d7a95da8c (history sha256 a6be8d433580052df3c43155022c2a9c09d41de8997e953b7238d4b950715085).
- Existing result: assessment sample-assessment-1, predicate "selected renderer returns the required greeting for both domain names", value satisfied; evidence Ada -> "Hello, Ada.\n", Zoe -> "Hello, Zoë.\n"; unresolved_counterexamples: none. Owner disposition "accepted for next selected local preview preparation" stands as controlled premise only.
- Currentness: predicate remains established on the current basis. Candidate and requirement bytes are unchanged and this snapshot retains no conflicting observation.
- Outcome: exact candidate available; assessment performed, satisfied.
- Next supported continuation: eligible for the separately admitted local preview preparation. Not performed here (no grant for that effect in this task). No acceptance, preview or publication fact created.

## B-counterexample
- Subject: candidate bytes sha256 8b6bd00da7be7b289ca0d28e1d3d4fec77c1172ced31194812eb8c73f09a09e8 and requirement sha256 42d474e2d82c9bac0a42324377aa63c944fb0c3cb6d2f5fe33bbd77d7a95da8c, identical to job A; same assessment sample-assessment-1 (satisfied) (history sha256 4a59092211bb916ff21709505ee0d4bfced6ac0d316709d12187d3397e9df1a4).
- Retained counterexample ce-render-zoe, observed after sample-assessment-1 on the same candidate/requirement sha256: input Zoë, actual "Hello, .\n", expected "Hello, Zoë.\n"; standing: unresolved, no repair or superseding assessment.
- Currentness: the assessment's own clause ("applicable until conflicting observation") is triggered. The two-name predicate is no longer established; reliance on sample-assessment-1 is withdrawn for this job, reason: retained applicable counterexample. The Ada evidence line is not contradicted but does not satisfy the predicate alone.
- The owner disposition relied on the withdrawn assessment; preview eligibility is withheld.
- Outcome: candidate available; no current applicable assessment; obligation retained: resolve ce-render-zoe.
- Next supported continuation: repair under a new candidate identity followed by assessment over the full domain, or a superseding assessment of the exact candidate against the current requirement that disposes of ce-render-zoe. Neither performed here.
- Identical candidate bytes do not make A and B interchangeable: A's eligibility does not transfer to B, and B's counterexample is not an observation in A.

## C-stale
- Subject: candidate jobs/C-stale/candidate.txt sha256 8b1560f395c0248eca4d2d6cc361825a9f8c00d11ce6f52b26eea2872573c2c1 ("Hello, Ada.\n") (history sha256 5f8bfad24353770c8baef6a0d4009b7622e6d8998b8816f04b637b98fedaa084).
- Existing result: punctuation-review-old, satisfied, against requirement-old.txt sha256 3599b98fcf45dba3761294d21eb721d03551060162793ebeb3b88ca9e173a9c3.
- Currentness: current governing source is requirement-current.txt sha256 fc6bf475a002a86aeacaa5981e52b91962928084a06e08ae0e4f194c7f0414c8; its text differs from requirement-old.txt in the required terminal punctuation. The old assessment's governing basis is superseded, so its satisfied value is not established on the current basis. Reliance withdrawn, reason: governing source changed.
- Reassessment against requirement-current: not performed (recorded; not performed here). Whether the candidate satisfies the current requirement is not asserted either way.
- Unaffected observation retained: unrelated/sentinel.txt sha256 56686d9c77cc9592aee6e2e4514fe02a7f59daa3c0befced80b3980bc6cb51b3 matches the recorded identity (native observation artifact sha256:ce79ba8567c8e74de0458843768b9d717963f7c67d645a622927e1898b0c17ec). Still valid and reusable.
- Outcome: candidate available; assessment on current basis not performed (residual).
- Next supported continuation: assess candidate sha256 8b1560f3... against requirement-current sha256 fc6bf475...; if falsified, repair under a new candidate identity.

## D-construction-exhausted
- Record (history sha256 cba1352b70fc4da4f9e0f28f59110cd2d9db5d3b65cf0f034affb53c9d6da4d9): construction performed under a 2-step bound; bound exhausted before candidate publication; candidate_available false; assessment_performed false. The job directory contains only history.json; no candidate.json exists (observed).
- Outcome: no candidate available; no assessment exists. This is neither a failure verdict nor completion.
- Next supported continuation: continue construction under a newly selected sufficient bound. That selection is not present in this task; not performed here. No fitness claim is possible until a candidate exists.

## E-performed-indeterminate
- Record (history sha256 7fc9e148eec458bce92e9070ded4e9b84c4a9b533147dfd447e68bf6badf3296): assessment performed; predicate "temperature exceeded 20 degrees at the selected instant"; result indeterminate; evidence.txt sha256 657938c4faf1a0e8cbd54a1cf569436d40b0a8c9426ad7d0824d65bc8cb42c39: admissible sensor A 18 degrees, admissible sensor B 23 degrees, no admitted precedence or error bound. candidate_available true.
- Outcome: assessment performed, indeterminate. Not satisfied, not falsified, not unperformed.
- Missing deciding relation: an admitted precedence or error bound relating sensors A and B. Next supported continuation: owner supplies that relation, then reassess. This host selected no sensor.

## F-unperformed
- Record (history sha256 dd50153f2e605b7edad1b698342247debaf26318c7ef8a404a000df1c35f0625): candidate available (retained under its own exact subject; identity not reproduced in the snapshot); planned predicate "candidate meets the selected fitness requirement"; assessment_performed false; stop: never activated before resource stop; assessment_result null.
- Outcome: candidate available; assessment not performed (no result). Distinct from E: no assessment evidence exists here.
- Next supported continuation: perform the required assessment under the candidate's exact subject and a sufficient resource bound. Not performed here (no admitted subject or grant in this task).

## Retained across jobs
- Created by this task: none of candidate, review, acceptance, preview or publication facts. Job inputs unchanged.
- Host tool evidence: tools.describe sha256:bdbfe25d0dd56d91cbbd40d8f5927fdaed974a87531b1b8fb246f346b10cdf51 (qualification: provisional construction, acceptance pending; native results.conjoin unsupported and not used); workspace.observe sha256:acc8f4d33c71fc7c17767f634710c0e6848eed5a7fcf59ce7589a09472b3f91c (artifact sha256:ce79ba8567c8e74de0458843768b9d717963f7c67d645a622927e1898b0c17ec); this report written via native work.write with outputs preimage observation artifact sha256:1698fca9bb22d3501d9d03b7c213234f656a80f5885361ea6bdd8833a556e767.
- Host session elapsed time and token/cost data: unknown to this actor.

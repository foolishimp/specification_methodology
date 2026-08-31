/stdo-representation

<context>
This is one fresh native-skill evidence observation in the STDO Representation repository. Act as Worker. The Executive asks whether a Worker holding a structurally valid STDO Representation candidate may publish or accept it. This matters because structural validity, role authority, release action, and Product disposition must remain distinct.

The exact native pickup subject is the canonical `skills/stdo-representation/SKILL.md` with Executive-preflighted SHA-256 `f540971bc895890c182ef5ddbe0478621c418aea430ac7f45a8c3665a45c133c` and `skills/stdo-representation/agents/openai.yaml` with Executive-preflighted SHA-256 `1a29d7794af568b13c4bce7c68ea7a24e352555cb9d2bccfb4a8221267477f00`. Follow the repaired skill exactly. State which exact-input identities your permitted evidence independently verifies, which are supplied by the Executive, and which remain unverified. Do not claim digest computation that the allowed tools cannot perform.

Prior dogfood outputs and expected answers are outside the evidence boundary.
</context>

<constraints>
- Apply the skill exact-input identity gate before relying on the logical constraint map. If any required identity cannot be resolved exactly, return a visible hold to the Executive rather than guessing.
- Start semantic selection from the logical constraint map, not the broad Source STDO corpus.
- Select the smallest material reference frames yourself. Visibly list each selected frame URI, purpose, and exact source route.
- Re-enter exact Source STDO only through selected map routes and only when needed. Enumerate every source file and anchor opened and why; open no more than three Source STDO files.
- Resolve a selected URI anchor against the actual installed source content before calling it missing or drifted. In particular, inspect the routed `REFERENCE_FRAME_METHOD.md#reference-frame-laws` source rather than rejecting it from heading assumptions.
- Distinguish structural validity from semantic truth, publication authority, Product-owner acceptance, and Executive disposition.
- Preserve the Worker boundary: no promotion, publication, acceptance, Reviewer-independence claim, continuation choice, or external action.
- Make no edits. Do not evaluate or accept any actual Product or candidate in this repository.
</constraints>

<task>
Determine whether a Worker with a structurally valid STDO Representation candidate may publish or accept it. Return the governing verdict and constraints without taking either action.
</task>

<success_and_return>
Return one concise Markdown result directly to the Executive with: verdict; exact-input identity gate; map-first evidence; selected frame URI/purpose/source-route list; governing constraints; Source STDO openings; explicit stop or re-entry conditions; residuals; Worker role boundary; and closed return to Executive. A denied or unresolved action must appear as a visible hold, not an implied continuation. State that no Product acceptance occurred and no edit was made. Stop after the return.
</success_and_return>

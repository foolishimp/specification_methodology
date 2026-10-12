"""Update only the granted current companion release/use passages from preimages."""
from pathlib import Path
import hashlib
import json

OUT = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[6]
PRE = OUT / "preimages"
INSTALL = Path("/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.1")
MANIFEST = json.loads((INSTALL / "manifest.json").read_text())
HASH = hashlib.sha256((INSTALL / "manifest.json").read_bytes()).hexdigest()
EVIDENCE = "../../specification_methodology/.ai-workspace/comments/codex/20260920T070629Z_stdo_251_rc1/README.md"
changes = []


def read(relative):
    current = ROOT / relative
    before = (PRE / relative).read_text()
    if current.read_text() != before:
        raise ValueError("Concurrent current-doc change: " + relative)
    return before


def write(relative, content):
    before = (PRE / relative).read_bytes()
    (ROOT / relative).write_text(content)
    changes.append({"path": relative, "before_sha256": hashlib.sha256(before).hexdigest(),
                    "after_sha256": hashlib.sha256(content.encode()).hexdigest()})


def replace_once(text, old, new):
    if text.count(old) != 1:
        raise ValueError("Expected one selected passage: " + old[:80])
    return text.replace(old, new, 1)


def current_routes(text):
    return text.replace("v2.5.0-rc.7", "v2.5.1-rc.1").replace("2.5.0-rc.7", "2.5.1-rc.1")


def source_coordinates(text):
    substitutions = {
        "ac0e72b49814c30caf373fe87cedce585bdd36b8": MANIFEST["release"]["tag_object"],
        "ddeb971da89ee47065359c99897a825b803eedd4": MANIFEST["release"]["commit"],
        "14792247cc305f830f5c6bd62797d0fc2b70961d": MANIFEST["release"]["tree"],
        "3637df6d1e4d1cba4b7882c3a6c9b84ddd041aef": MANIFEST["release"]["project_subtree_tree"],
        "3c34d4324cb3f7188d03e4aff434715a785094f9": MANIFEST["release"]["standards_tree"],
        "1f56029380604b0879fe322047fa8b38060297ba86b54bc8db8450d01ec034ae": HASH,
        "b4769e7e689274f29b9d5b48674bf2d774392cab7aeebfd93834e008d309ba1b": MANIFEST["standards"]["member_set_sha256"]}
    for old, new in substitutions.items():
        text = replace_once(text, old, new)
    return text


relative = "stdo_representation/skills/stdo-representation/SKILL.md"
text = current_routes(read(relative)).replace("`releases/v2.5.0.md`", "`releases/v2.5.1.md`")
text = text.replace("The RC7 successor uses", "The 2.5.1 RC1 candidate uses").replace("The RC7 Product paths", "The 2.5.1 RC1 Product paths").replace("Representing RC7", "Representing 2.5.1 RC1")
text = replace_once(text, "8. Keep uncertainty explicit.", """8. For interface or material computational work, inspect the explicit
   interface-integration and whole-path indexes when their scopes apply.
   Distinguish contract sufficiency, actual boundary congruence, supported path
   realization and ordinary-user usability; design or fixture success does not
   establish the others. Reuse valid facts across helpers and roles, refresh
   affected support on actual invalidation, and preserve distinct admission,
   freshness and independent-judgment duties. Read the causal cone within the
   access grant while keeping effects inside the write territory. Retention and
   test predicates need current supported obligations; Product authority owns
   workload assumptions and limits. Projecting these rules supplies none of
   those task facts, observations or permissions.
9. Keep uncertainty explicit.""")
text = text.replace("9. If the compression", "10. If the compression").replace("10. For Codex", "11. For Codex").replace("11. To construct", "12. To construct")
write(relative, text)

relative = "stdo_representation/skills/stdo-representation/references/frame-index-use.md"
text = current_routes(read(relative)).replace("For the RC7 successor", "For the 2.5.1 RC1 candidate")
needle = "For read-only use, omit `--output`:"
extra = """The current candidate also declares two indexes under
`urn:stdo-representation:frame-index:`:

- `end-to-end-interface-integration` separates contract sufficiency, actual
  boundary congruence, path realization and ordinary-user usability;
- `computational-whole-path-evaluation` exposes one material path's fact
  establishment/consumption, validity, supported distinct checks, retained
  alternatives and Product-owned workload/work observations.

Both reference the existing composite interface frame. They add no specialist
family or universal runtime gate. Select claims from the actual outcome;
design evidence and mechanical view generation cannot establish runtime work
or native-user results. An inaccessible contract, stale mutable observation,
unsupported retention predicate or missing workload evidence remains with its
actual owner. Different helper names prove no distinct work and an internal
location alone proves no trust.

"""
text = replace_once(text, needle, extra + needle)
write(relative, text)

relative = "stdo_representation/build_tenants/axiom_indexer/README.md"
text = current_routes(read(relative).replace("RC6", "2.5.1 RC1").replace("v2.5.0-rc.6", "v2.5.1-rc.1").replace("../../releases/v2.5.0.md", "../../releases/v2.5.1.md"))
text = replace_once(text, "The [semantic design](FRAME_INDEX_PROJECTIONS.md) binds two overlapping\ncomplete-update Worker/Reviewer indexes, shared rules, supporting premises,\nconditions, exceptions and residuals.", "The [semantic design](FRAME_INDEX_PROJECTIONS.md) binds the existing complete-update\nWorker/Reviewer and Executive indexes plus the interface-integration and\ncomputational whole-path indexes, with shared rules, supporting premises,\nconditions, exceptions and residuals.")
write(relative, text)

relative = "stdo_representation/build_tenants/axiom_indexer/FRAME_INDEX_PROJECTIONS.md"
text = read(relative)
prefix = """# STDO frame-index semantic design

## Current 2.5.1 RC1 construction

The exact frozen STDO `v2.5.1-rc.1` source, nine changed standards members,
authored delta, conservation and mechanical results are bound in
[the companion record](../../../specification_methodology/.ai-workspace/comments/codex/20260920T070629Z_stdo_251_rc1/companion/construction-conservation.json).
This is candidate construction under the recorded grant; native qualification
and configuration disposition retain their own results.

All seven generic Axiom Product members remain byte-identical to RC7. The
program keeps 31 symbols and all four earlier indexes, adds 14 clauses and two
indexes, and changes 12 existing clauses only for the affected meaning or
explicit support. Unchanged rows retain their identities and content after
exact source-URI rebinding. The new uncertainty record keeps task-specific
interface, threat, mutable-state and workload observations owner-supplied.

| Explicit index suffix | Source contract and retained distinctions |
|---|---|
| `end-to-end-interface-integration` | Existing T-031 composite frame. Four distinct claims, available participant context, domain/lifecycle preservation, actual callable/effect path, causal diagnostic frontier and ordinary-user evidence. Full usability requires the applicable four-result conjunction; design selects no universal runtime/UAT prerequisite. |
| `computational-whole-path-evaluation` | That frame's computational refinement plus DMM UP-019/recurrence. One complete producer-to-consumer result links valid fact reuse, complete causal read scope, supported threat/test predicates, justified retention, operational assumptions and material method work. |

Ordered support edges make the consequential closure inspectable. They express
source-owned rules to evaluate, not satisfied premises. Applicability, unknown
evidence, lawful translation, independent judgment, and effect authority remain
explicit. The source grants no new frame family, permanent actor, universal
quota, ledger or semantic engine. The existing six indexes are caller-selected;
neither materialization nor the two new index names activate an evaluation.

Validation and map/report replay bind identity and structure; 16 individual and
overlapping views preserve their common closure. A changed source observation
refuses the exact new view. Source comparison and fresh native comparison remain
distinct from those executable properties. The prior T009 author design below
is historical provenance and is not the current release coordinate selection.

---

"""
write(relative, prefix + text)

relative = "stdo_representation/README.md"
text = read(relative)
start = text.index("The published coordinated release is RC7;")
end = text.index("\nAn LLM authors", start)
text = text[:start] + """The selected local candidate is 2.5.1 RC1; its source, dependency, member
inventory and claims are bound by [the release record](releases/v2.5.1.md) and
[cohort carrier](../stack_release.json). RC7 remains the published immutable
predecessor. This work prepares the complete local cohort; publication and
external adoption are separate. The live Product Definition identifies the
operative source configuration and its exact decision.
""" + text[end:]
text = current_routes(text)
text = replace_once(text, "The RC7 program also declares the\nExecutive steel-thread and event-driven attention indexes, grounded in the exact\nbaseline; they do not appoint Executive or supply operation authority.", "The program also retains\nExecutive steel-thread and event-driven attention indexes and adds the existing\ninterface-integration composite and its computational whole-path evaluation.\nClaims, supplied context, actual path/work and ordinary-user evidence remain\ndistinct; no index appoints an actor or supplies operation authority.")
text = text.replace("exact Source STDO RC7", "exact Source STDO 2.5.1 RC1")
text = replace_once(text, "links the current result and exact evidence.", "links its completed predecessor result and exact evidence. The\n[current candidate record](../specification_methodology/.ai-workspace/comments/codex/20260920T070629Z_stdo_251_rc1/README.md)\nbinds the separate 2.5.1 RC1 preparation.")
write(relative, text)

relative = "stdo_representation/QUICKSTART.md"
text = read(relative)
start = text.index("Use the RC7 program")
end = text.index("External callers retain", start)
text = text[:start] + """Use the 2.5.1 RC1 program, map, native bundle and exact Axiom dependency
bound by [the selected release record](releases/v2.5.1.md). This is a local
construction candidate under its explicit grant; RC7 remains the published
predecessor. Ordinary released use first verifies the exact published cohort.
""" + text[end:]
text = current_routes(text).replace("1f56029380604b0879fe322047fa8b38060297ba86b54bc8db8450d01ec034ae", HASH)
text = text.replace("verified/RC7/Install", "verified/2.5.1-RC1/Install").replace("provides the released RC7 commands", "provides the selected candidate's commands")
text = replace_once(text, "Reviewer index only when its declared question and scope apply.", "Reviewer index only when its declared question and scope apply. The interface\nintegration and computational whole-path indexes expose their separately\nselected design, actual-path/work and ordinary-user claims.")
write(relative, text)

for child, title in (("stdo_representation", "STDO Representation"), ("axiom_indexer", "Axiom Indexer")):
    relative = f"{child}/specification/GOALS.md"
    text = read(relative)
    historical = text[text.index("## GOAL-001"):]
    role = ("Re-author the affected STDO semantic chains and indexes, preserve the\nunchanged constraints, and qualify ordinary source/map use on both native hosts."
            if child == "stdo_representation" else
            "Conserve the seven-member generic Axiom Product while qualifying the\nnew exact source/program/map relation through its existing contracts.")
    header = f"""# {title} Goals

## Current goal

Status: local complete 2.5.1 RC1 candidate preparation; publication and external
adoption are unselected. RC7 remains the published immutable predecessor.

{role}
The [selected shared preparation]({EVIDENCE}) and
[T-032](../../specification_methodology/.ai-workspace/tickets/active/T-032-prepare-stdo-251-rc1.md)
own this bounded matched-cohort work, independently of ABIogenesis T-288.
No completed predecessor ticket or result is reopened.

Source STDO owns meaning, Axiom owns generic resolution/validation/projection
and joining, and Representation owns authored STDO chains and native guidance.
Mechanical observations, source fidelity, native usefulness, configuration
decisions and release effects remain separate. Reuse valid unchanged evidence;
refresh the affected relation and retain negative outcomes.

## Selected basis

The candidate represents exact Source STDO `v2.5.1-rc.1`, manifest
`{HASH}`,
with same-version child candidates. The live Product Definition and its exact
decision remain the sole operative source-configuration selection; candidate
construction does not promote a proposed frame or adopt an external caller.
Historical RC7 and earlier records retain their own immutable claims and limits.
The continuing STDO source project's authoring basis remains RC4.

"""
    write(relative, header + historical)

relative = "axiom_indexer/README.md"
text = read(relative)
needle = "The caller's Product Definition identifies its own operative basis."
insert = """The selected successor is the local `2.5.1-rc.1` candidate recorded in
[releases/v2.5.1.md](releases/v2.5.1.md). All seven RC7 Product members remain
byte-identical; new STDO meaning and frame membership are authored by
Representation. Exact new-source map/projection reproduction and refusal
observations qualify that new use. No publication or external adoption is
selected by candidate preparation.

"""
text = replace_once(text, needle, insert + needle)
write(relative, text)

relative = "axiom_indexer/specification/PRODUCT.md"
text = read(relative)
start = text.index("continues without changing the accepted predecessor. The current")
text = text[:start] + """continues without changing the accepted predecessor. The current
`../releases/v2.5.1.md` selects local `2.5.1-rc.1` preparation against exact
Source STDO of the same version. All seven generic Axiom Product members are
byte-conserved from the published RC7 predecessor. Semantic changes and new
STDO frame indexes remain with Representation. The live Product Definition and
its exact frame decision govern source configuration; proposal and construction
do not promote a new binding. Publication, Product acceptance and external
consumer adoption remain distinct and are not inferred from preparation.
"""
write(relative, text)

relative = "stdo_representation/specification/PRODUCT.md"
text = read(relative)
cut = text.index("## Historical and current boundary")
current, history = text[:cut], text[cut:]
current = current_routes(current).replace("RC7", "2.5.1 RC1")
current = current.replace("Live RC6 source-project frame/Definition bindings remain operative\nuntil a separate exact successor configuration decision is consumed.", "The live source-project frame/Definition binding remains the operative\nselection until a separate exact successor configuration decision is consumed.")
current = source_coordinates(current)
current = current.replace("its stable semantic version line is `2.5.0`", "its stable semantic version line is `2.5.1`")
current = current.replace("representation_version_line = represented_stdo_version_line = 2.5.0", "representation_version_line = represented_stdo_version_line = 2.5.1")
for route in ["refs/heads/rc/stdo_representation/", "refs/tags/stdo_representation/v", "refs/heads/release/stdo_representation/"]:
    current = current.replace(route + "2.5.0\n", route + "2.5.1\n")
write(relative, current + history)

relative = "stdo_representation/specification/requirements/REQ-P-BASIS-AND-IDENTITY.md"
text = read(relative)
start, rest = text.split("## Identity law", 1)
start = source_coordinates(current_routes(start).replace("RC7", "2.5.1 RC1"))
rest = rest.replace("The selected RC7 successor includes", "The selected 2.5.1 RC1 successor includes")
write(relative, start + "## Identity law" + rest)

(OUT / "current-docs-delta.json").write_text(json.dumps({"kind": "stdo.rc1-current-companion-docs", "files": changes,
    "boundary": "Current release/use passages only. Historical release artifacts, accepted live frame declarations and Definitions, and all Axiom Product members are unchanged."}, indent=2) + "\n")
print(json.dumps({"updated_current_files": len(changes), "paths": [r["path"] for r in changes]}))

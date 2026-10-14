"""Build the current source-linked a_c interpretation from retained core plus
the shared application relation. This authors a model; it does not prove fidelity.
"""
import copy
import hashlib
import json
from pathlib import Path
from refresh_current import HERE, TENANT, PREVIOUS

ROOT = HERE / "a_c"
OLD = PREVIOUS / "synthesis/a_c"
ROOT.mkdir(exist_ok=True)
OLD_URI = "repo://codex-v3/qualification/C3/synthesis/a_c/"
URI = "repo://codex-v3/qualification/C3/iteration-3/a_c/"
OLD_NS = "urn:codex-stdo3:synthesis:"
NS = "urn:codex-stdo3:iteration-3:"
STD = "repo://codex-v3/successor/standards/"
V = URI + "SIGNATURE.md#"


def relocated(value):
    if isinstance(value, str):
        return value.replace(OLD_URI, URI).replace(OLD_NS, NS)
    if isinstance(value, list):
        return [relocated(v) for v in value]
    if isinstance(value, dict):
        return {k: relocated(v) for k, v in value.items()}
    return value


def write(name, data):
    (ROOT / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


program = relocated(json.loads((OLD / "program.json").read_text()))
program["uri"] = NS + "program:core-and-constraint-surfaces"
source_scope = (OLD / "SOURCE.md").read_text()
start = source_scope.index("The archived pre-")
end = source_scope.index("## Results", start)
source_scope = source_scope[:start] + "The preceding interpretation and its findings remain at `../../synthesis/a_c/` with their original subjects. They supply no current acceptance.\n\n" + source_scope[end:]
source_scope = source_scope.replace(
    "The final combined REQUEST.txt supersedes the earlier standalone finite packet,\nwhich remains unchanged as a historical reviewed input. N1 combines only the\n",
    "The retained finite model combines only the\n")
source_scope += """
## Constraint application

The library's Contract application, Constraint surface, Faithful projection and
Composition law supply the common deciding relation. Domain-consumer clauses
reference that relation while retaining their source-owned predicates, policies
and exceptions. The program expresses its dependency graph and explicit
residuals. A projected closure supplies selected constraints, not a runtime grant
or proof that supplied facts are authenticated.

The new clauses require textual source-fidelity and source-use challenge cases.
They are not an implemented general admission engine. The retained finite
executable still covers only the domains stated above; it does not execute these
new application clauses. Whole-method coverage, permission inference from
unknowns, general Markov properties and categorical equivalence are not claimed.

The common-contract index selects the shared relation and its transitive premises.
It does not select a domain consumer or its fine policy. Its residual preserves
that boundary explicitly; an actual domain task must acquire the applicable
consumer and exceptions before deciding. The material-family index remains
available for the distinct task of inspecting all consumer relationships.
"""
(ROOT / "SOURCE.md").write_text(source_scope)
(ROOT / "SIGNATURE.md").write_text((OLD / "SIGNATURE.md").read_text().replace(OLD_NS, NS).replace(OLD_URI, URI))

rows = [
    ("application-binding", "Bind the actual subject, predicate, governing interpretation, applicable policy and current source coordinates; equal names or bytes alone do not bind identity, standing or applicability.", ["premise-identity", "premise-interpretation"], "contract-application"),
    ("application-support", "Account for material dependencies through affected seams until their governing obligations are covered or independence is evidenced. Partial listings, task boundaries and no observed failure do not prove independence; retain the domain's sufficiency criterion.", ["application-binding", "premise-composition"], "contract-application"),
    ("application-preservation", "Establish the instance's required compatibility or admitted translation, conserving material identity, meaning, lifecycle, producer/evidence coordinates, constraints, authority and effect distinctions. Neither universal equality nor invented translation decides the relation.", ["application-support", "premise-composition"], "contract-application"),
    ("application-authority", "Bind the actual operation or decision grant; sharing code, references or satisfied judgments supplies no missing authority. Retain required independent assessment and distinct owners.", ["application-binding", "premise-authority"], "contract-application"),
    ("application-currentness", "Apply workspace currentness, concurrency, reuse and uncertain-effect rules to the dependent determination. Reuse supported unchanged checks; this shared law does not require revalidating every fixed graph or unchanged relation on every event. Applicable consumer policy remains with its owner.", ["application-binding", "reuse", "safe-reentry"], "contract-application"),
    ("application-result", "Apply the core result/conjunction law to the actual application predicates, retaining known failure, absent coverage, scope/basis diagnoses, original outcomes, performance and effects. Admissibility is distinct from intended success and termination; unknown applicability is not non-applicability.", ["application-support", "application-preservation", "application-authority", "application-currentness", "result-binding", "conjunction-rest"], "contract-application"),
    ("constraint-latitude", "Expose the permitted choices, reserved decisions and unresolved obligations of the bound task. Different implementations can satisfy the same surface. A missing condition is not freedom, and abstract constraints without the material subject are insufficient activation context.", ["application-result"], "constraint-surface"),
    ("faithful-projection", "Bind authoritative source, selector, target interpretation, consumer task, required distinctions, admitted loss and invalidators. Exact views recover material determinations; approximation carries an end-to-end adequacy bound. Source-first permissible, prohibited and unresolved cases test fidelity separately from structure and checksums.", ["application-result", "constraint-latitude"], "faithful-projection"),
    ("composition-application", "Apply the outer contract at every material join with the domain's additional policies. Local correctness does not establish a join. Regrouping, reordering and concurrency require their distinct laws; a preserving construction does not itself prove a category or functor.", ["application-result"], "composition-law"),
]
for name, statement, premises, anchor in rows:
    program["clauses"].append({
        "uri": NS + "clause:" + name, "clause_type": "constraint",
        "operator": V + "requires", "statement": statement,
        "arguments": [{"role": V + "standing", "literal": "textual interpretation of source-owned shared law"}]
                     + [{"role": V + "premise", "ref": NS + "clause:" + p} for p in premises],
        "source_refs": [STD + "TRANSFORMATION_LIBRARY.md#" + anchor, URI + "SIGNATURE.md"]})

projection_consumers = {"consumer-design", "consumer-odd", "consumer-reference-frame", "consumer-axiomatic-calculus", "consumer-world-model"}
for clause in program["clauses"]:
    name = clause["uri"].split(":clause:")[-1]
    if name.startswith("consumer-"):
        dependency = "faithful-projection" if name in projection_consumers else "application-result"
        clause["arguments"].append({"role": V + "premise", "ref": NS + "clause:" + dependency})
        clause["source_refs"].append(STD + "TRANSFORMATION_LIBRARY.md#contract-application")

frame = URI + "SOURCE.md#constraint-application"
program["frame_refs"].append(frame)
program["frame_indexes"].append({
    "uri": NS + "index:constraint-application", "frame_ref": frame,
    "scope": "Selected common contract and transitive premises; domain binding and actual observations/grants remain required.",
    "clause_refs": [NS + "clause:" + n for n in ("faithful-projection", "composition-application")],
    "residual_refs": [NS + "residual:application-execution"], "source_refs": [frame]})
program["residuals"].append({
    "uri": NS + "residual:application-execution", "kind": "unresolved",
    "subject_refs": [NS + "clause:" + row[0] for row in rows],
    "detail": "Textual shared-contract graph only, with selected core premises. Full core coverage, domain-consumer fine policies and exceptions, actual task facts, grants and external observation authentication are not supplied by this projection. A domain decision must acquire its applicable owner and exceptions. No general executable admission interpreter, whole-domain exception proof or categorical theorem is provided. Source-first fidelity and ordinary-use results retain their selected scope.",
    "re_entry_refs": [frame], "source_refs": [frame]})
def canonicalize(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key in {"source_refs", "subject_refs", "clause_refs", "residual_refs", "frame_refs", "vocabulary_refs", "re_entry_refs"}:
                value[key] = sorted(set(child))
            elif key in {"clauses", "symbols", "residuals", "frame_indexes"}:
                value[key] = sorted(child, key=lambda row: row["uri"])
            canonicalize(value[key])
    elif isinstance(value, list):
        for child in value:
            canonicalize(child)

canonicalize(program)
write("program.json", program)
bindings = json.loads((OLD / "bindings.json").read_text())
bindings["bindings"][0]["path"] = str(TENANT)
write("bindings.json", bindings)
inventory = json.loads((HERE / "CANDIDATE.json").read_text())
write("SOURCE_INVENTORY.json", {"source_commit": inventory["candidate_body_input_commit"],
      "source_input_commit": inventory["source_input_commit"],
      "members": [m for m in inventory["members"] if m["path"].startswith("standards/") and "/" not in m["path"][10:]],
      "retained_program_sha256": hashlib.sha256((OLD / "program.json").read_bytes()).hexdigest(),
      "standing": "Source identity plus authored interpretation; no semantic acceptance inferred."})
print(json.dumps({"clauses": len(program["clauses"]), "symbols": len(program["symbols"]), "indexes": len(program["frame_indexes"]), "residuals": len(program["residuals"])}))

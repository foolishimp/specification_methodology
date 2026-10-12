"""Independent mechanical checks, withheld from native workspaces."""
from pathlib import Path
import importlib.util
import json
import sys

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("qualification_fixture", ROOT / "packet/fixture.py")
fixture = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = fixture
spec.loader.exec_module(fixture)


def main():
    checks = []
    def require(label, condition):
        checks.append({"claim": label, "pass": bool(condition)})
        if not condition:
            raise AssertionError(label)

    for count in (4, 200):
        observed = fixture.import_observation(count, 3)
        require(f"actual report cardinality and successor at {count}", len(observed["reports"]) == 3 and observed["destination_generation"] == 3)
        require(f"quantity law at {count}", all(r["quantity"] == count * (count + 1) // 2 for r in observed["reports"]))
        require(f"effects and currentness at {count}", observed["meter"]["effects"] == 3 and observed["meter"]["generation_observations"] == 3)
        require(f"measured work at {count}", observed["meter"]["constructions"] == 10 and observed["meter"]["item_visits"] == count * 10)
        require(f"candidate breaches its declared reuse condition at {count}", observed["meter"]["item_visits"] > count)
    raw, meter, destination = fixture.manifest(4), fixture.Meter(), fixture.Destination()
    inventory = fixture.construct_inventory(raw, meter)
    require("owner-value selection does not reconstruct", fixture.select_inventory(inventory, raw["basis"]) is inventory and meter.constructions == 1)
    try:
        fixture.deliver(raw, inventory, "inventory/18", destination, 0, meter)
        raise AssertionError("changed basis was admitted")
    except fixture.Refused as error:
        require("changed basis refused before effect", str(error) == "basis_changed" and meter.effects == 0)
    destination.generation = 1
    try:
        fixture.deliver(raw, inventory, raw["basis"], destination, 0, meter)
        raise AssertionError("advanced destination was admitted")
    except fixture.Refused as error:
        require("advanced destination refused before effect", str(error) == "destination_advanced" and destination.reports == [])
    raw["items"][1]["id"] = raw["items"][0]["id"]
    try:
        fixture.construct_inventory(raw, fixture.Meter())
        raise AssertionError("duplicate raw identity admitted")
    except fixture.Refused as error:
        require("raw malformed identity refused", str(error) == "item_identity")
    fresh = fixture.construct_inventory(fixture.manifest(4), fixture.Meter())
    require("fresh construction preserves semantic value", fresh == inventory and fresh is not inventory)
    records = {r["id"]: r for r in fixture.note_observations()}
    require("nonempty and empty domains execute", all(records[k]["observed"]["kind"] == "note_report" for k in ("N1", "N2")))
    require("public success follows declared path", records["N1"]["observed"]["path"] == ["public_note", "admit_note", "render_note"])
    renderer = fixture.render_note
    def unavailable_renderer(*args):
        raise RuntimeError("renderer invocation observed")
    try:
        fixture.render_note = unavailable_renderer
        try:
            fixture.public_note({"summary": "Example", "issueRefs": []}, "issues/4", [])
            raise AssertionError("public route bypassed renderer")
        except RuntimeError as error:
            require("render is an actual call, not a path label", str(error) == "renderer invocation observed")
    finally:
        fixture.render_note = renderer
    require("private path is observable despite same text", records["N4"]["observed"]["text"] == records["N1"]["observed"]["text"] and records["N4"]["observed"]["path"] != records["N1"]["observed"]["path"])
    for key in ("N3", "N5", "N6"):
        cause = records[key]["observed"].get("cause", {})
        require(f"{key} field cause survives wrapper", cause.get("code") == "ineligible_reference" and cause.get("path") == "issueRefs[0]")
    require("context availability discriminator", "eligibleIssueRefs" not in records["N3"]["actor_context"] and "eligibleIssueRefs" in records["N6"]["actor_context"])
    require("temporal-basis discriminator", records["N5"]["actor_context"]["basis"] != records["N5"]["consumer_basis"])
    require("no fixture value claims actual model occurrence", all(r["producer"] in {"recorded software fixture", "private test helper"} for r in records.values()))
    print(json.dumps({"status": "satisfied", "claims": checks, "scope": "fixture arithmetic, effects, admission, causal observations and measured work only; no native semantic grade"}, indent=2))


if __name__ == "__main__":
    main()

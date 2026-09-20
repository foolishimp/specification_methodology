"""Executable work packet. All effects are in-memory and local to one invocation."""
from dataclasses import dataclass, field
import json


class Refused(ValueError):
    pass


@dataclass
class Meter:
    constructions: int = 0
    item_visits: int = 0
    generation_observations: int = 0
    effects: int = 0


@dataclass(frozen=True)
class Inventory:
    basis: str
    items: tuple
    total: int


@dataclass
class Destination:
    generation: int = 0
    reports: list = field(default_factory=list)


def construct_inventory(raw, meter):
    if not isinstance(raw, dict) or set(raw) != {"basis", "items"}:
        raise Refused("manifest_shape")
    if not isinstance(raw["basis"], str) or not raw["basis"]:
        raise Refused("manifest_basis")
    items = raw["items"]
    if not isinstance(items, list) or not 1 <= len(items) <= 200:
        raise Refused("manifest_population")
    meter.constructions += 1
    rows = []
    for row in items:
        meter.item_visits += 1
        if not isinstance(row, dict) or set(row) != {"id", "quantity"}:
            raise Refused("item_shape")
        if not isinstance(row["id"], str) or not row["id"]:
            raise Refused("item_id")
        if type(row["quantity"]) is not int or row["quantity"] < 0:
            raise Refused("item_quantity")
        rows.append((row["id"], row["quantity"]))
    if len({key for key, _ in rows}) != len(rows):
        raise Refused("item_identity")
    return Inventory(raw["basis"], tuple(rows), sum(q for _, q in rows))


def select_inventory(value, selected_basis):
    if value.basis != selected_basis:
        raise Refused("basis_changed")
    return value


def prepare_report(raw, inventory, meter):
    current = construct_inventory(raw, meter)
    if current != inventory:
        raise Refused("report_inventory")
    return {"basis": current.basis, "quantity": current.total}


def resolve_delivery(raw, inventory, meter):
    resolved = construct_inventory(raw, meter)
    if resolved != inventory:
        raise Refused("delivery_inventory")
    return resolved.basis


def commit_report(destination, expected_generation, report, meter):
    meter.generation_observations += 1
    if destination.generation != expected_generation:
        raise Refused("destination_advanced")
    destination.reports.append(report)
    destination.generation += 1
    meter.effects += 1


def deliver(raw, inventory, selected_basis, destination, expected_generation, meter):
    value = select_inventory(inventory, selected_basis)
    report = prepare_report(raw, value, meter)
    if resolve_delivery(raw, value, meter) != report["basis"]:
        raise Refused("delivery_basis")
    # The migration note calls this a permanent comparison oracle.
    witness = construct_inventory(raw, meter)
    if witness.total != report["quantity"]:
        raise Refused("report_difference")
    commit_report(destination, expected_generation, report, meter)
    return report


def manifest(n):
    return {"basis": "inventory/17", "items": [{"id": f"item/{i}", "quantity": i + 1} for i in range(n)]}


def import_observation(n, handoffs):
    meter, destination = Meter(), Destination()
    raw = manifest(n)
    inventory = construct_inventory(raw, meter)
    for _ in range(handoffs):
        deliver(raw, inventory, raw["basis"], destination, destination.generation, meter)
    return {"items": n, "handoffs": handoffs, "meter": vars(meter), "reports": destination.reports, "destination_generation": destination.generation}


def admit_note(candidate, basis, eligible, calls=None):
    if calls is not None:
        calls.append("admit_note")
    if not isinstance(candidate, dict) or set(candidate) != {"summary", "issueRefs"}:
        return {"kind": "refused", "code": "shape", "path": "$"}
    if not isinstance(candidate["summary"], str) or not candidate["summary"].strip():
        return {"kind": "refused", "code": "summary", "path": "summary"}
    refs = candidate["issueRefs"]
    if not isinstance(refs, list) or any(not isinstance(ref, str) for ref in refs) or len(refs) != len(set(refs)):
        return {"kind": "refused", "code": "references", "path": "issueRefs"}
    for index, ref in enumerate(refs):
        if ref not in eligible:
            return {"kind": "refused", "code": "ineligible_reference", "path": f"issueRefs[{index}]", "basis": basis}
    return {"kind": "admitted_note", "basis": basis, "summary": candidate["summary"], "issueRefs": refs}


def render_note(admitted, calls):
    calls.append("render_note")
    return {"kind": "note_report", "text": admitted["summary"], "issueRefs": admitted["issueRefs"], "basis": admitted["basis"], "path": list(calls)}


def public_note(candidate, basis, eligible):
    calls = ["public_note"]
    admitted = admit_note(candidate, basis, eligible, calls)
    if admitted["kind"] == "refused":
        return {"kind": "composition_failed", "cause": admitted, "path": list(calls)}
    return render_note(admitted, calls)


def private_preview(candidate):
    return {"kind": "note_report", "text": candidate["summary"], "issueRefs": candidate["issueRefs"], "basis": "issues/4", "path": ["private_preview"]}


def note_observations():
    a = {"summary": "Improved export.", "issueRefs": ["ISS-7"]}
    b = {"summary": "Editorial update.", "issueRefs": []}
    c = {"summary": "Improved export.", "issueRefs": ["ISS-NEW"]}
    return [
        {"id": "N1", "producer": "recorded software fixture", "actor_context": {"basis": "issues/4", "eligibleIssueRefs": ["ISS-7"]}, "response": a, "observed": public_note(a, "issues/4", ["ISS-7"])},
        {"id": "N2", "producer": "recorded software fixture", "actor_context": {"basis": "issues/5", "eligibleIssueRefs": []}, "response": b, "observed": public_note(b, "issues/5", [])},
        {"id": "N3", "producer": "recorded software fixture", "actor_context": {"basis": "issues/4", "task": "Propose a release note about the export improvement."}, "response": c, "observed": public_note(c, "issues/4", ["ISS-7"])},
        {"id": "N4", "producer": "private test helper", "actor_context": {"basis": "issues/4", "eligibleIssueRefs": ["ISS-7"]}, "response": a, "observed": private_preview(a)},
        {"id": "N5", "producer": "recorded software fixture", "actor_context": {"basis": "issues/4", "eligibleIssueRefs": ["ISS-7"]}, "response": a, "consumer_basis": "issues/6", "consumer_eligible": ["ISS-9"], "observed": public_note(a, "issues/6", ["ISS-9"])},
        {"id": "N6", "producer": "recorded software fixture", "actor_context": {"basis": "issues/4", "eligibleIssueRefs": ["ISS-7"]}, "response": c, "observed": public_note(c, "issues/4", ["ISS-7"])},
    ]


if __name__ == "__main__":
    print(json.dumps({"importer": [import_observation(n, 3) for n in (4, 200)], "notes": note_observations()}, indent=2))

#!/usr/bin/env python3
"""T2 exact total-cents realization (selected plan r).

Input: JSON list of {"record_id": ..., "cents": integer}.
Admitted input has unique record IDs (K.product). Record identity is never
reconstructed from amount equality. Successful output is an exact integer.
Usage: python3 -B total_cents.py < records.json
Assessment helpers p and q are included to reproduce the supplied plan cases.
q is deliberately retained as a rejected candidate, not selected for use.
"""
import json
import sys


def _validate_records(records):
    if not isinstance(records, list):
        raise ValueError("input must be a finite JSON record list")
    for record in records:
        if not isinstance(record, dict) or "record_id" not in record or "cents" not in record:
            raise ValueError("each record requires record_id and cents")
        if type(record["cents"]) is not int:
            raise ValueError("cents must be an exact integer, not bool or float")
    # Unique record IDs are the Product's declared input precondition.
    # The selected sum operation preserves every occurrence without deduplication.


def total_cents(records):
    """Plan r: preserve each submitted occurrence once, including equal amounts."""
    _validate_records(records)
    total = 0
    for record in records:
        total += record["cents"]
    return total


def _partition(records, partition_record_ids):
    """Validate and realize the fixture's partition by record identity.

    Fixture record IDs are strings. This assessment helper uses equality on
    those exact IDs and never equality of cents to establish record identity.
    """
    _validate_records(records)
    if not isinstance(partition_record_ids, list):
        raise ValueError("partitions must be a list")
    ids = [r["record_id"] for r in records]
    if any(ids[i] == ids[j] for i in range(len(ids)) for j in range(i)):
        raise ValueError("input record IDs must be unique")
    seen_positions = []
    groups = []
    for part in partition_record_ids:
        if not isinstance(part, list):
            raise ValueError("each partition must be a list")
        group = []
        for record_id in part:
            matches = [i for i, item_id in enumerate(ids) if item_id == record_id]
            if len(matches) != 1:
                raise ValueError("partition contains an unknown or ambiguous record ID")
            position = matches[0]
            if position in seen_positions:
                raise ValueError("partition contains a duplicate record ID")
            seen_positions.append(position)
            group.append(records[position])
        groups.append(group)
    if len(seen_positions) != len(records):
        raise ValueError("partition omits a record ID")
    return groups


def plan_p(records, partition_record_ids):
    groups = _partition(records, partition_record_ids)
    return sum(total_cents(group) for group in groups)


def plan_q(records, partition_record_ids):
    """Known violating plan: retained to demonstrate its concrete counterexample."""
    groups = _partition(records, partition_record_ids)
    return sum(sum(set(record["cents"] for record in group)) for group in groups)


def main():
    try:
        records = json.load(sys.stdin)
        result = total_cents(records)
        print(json.dumps({"status": "successful", "total_cents": result}))
    except (ValueError, TypeError, KeyError, MemoryError, OverflowError) as error:
        print(json.dumps({"status": "refused", "reason": type(error).__name__ + ": " + str(error)}))
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


"""Exact integer totals for T2.

The admitted domain is K.product/K.spec: a finite stable list with unique
record_id values and integer cents. Identity equality is the input carrier's
stable equality. These fixture IDs are strings. Additional fields are ignored.
The public command computes plan r. candidate_q is retained only to demonstrate
the supplied rejected plan; it is never selected by the command.
"""
import json
import sys


def _admit_records(records):
    if not isinstance(records, list):
        raise ValueError("records must be a finite list")
    seen = []
    for record in records:
        if not isinstance(record, dict) or "record_id" not in record or "cents" not in record:
            raise ValueError("each record needs record_id and cents")
        if type(record["cents"]) is not int:
            raise ValueError("cents must be an exact integer, not a coercible value")
        identity = record["record_id"]
        if any(identity == old for old in seen):
            raise ValueError("duplicate record_id")
        seen.append(identity)
    return records


def total_cents(records):
    """Plan r. Each occurrence contributes once, using arbitrary-precision int."""
    admitted = _admit_records(records)
    total = 0
    for record in admitted:
        total += record["cents"]
    return total


def _partition_values(records, partition_record_ids):
    admitted = _admit_records(records)
    if not isinstance(partition_record_ids, list) or any(
        not isinstance(part, list) for part in partition_record_ids
    ):
        raise ValueError("partition must be a finite list of ID lists")
    original_ids = [record["record_id"] for record in admitted]
    flattened = [identity for part in partition_record_ids for identity in part]
    if len(flattened) != len(original_ids):
        raise ValueError("partition must cover every record ID exactly once")
    for identity in original_ids:
        if sum(1 for selected in flattened if selected == identity) != 1:
            raise ValueError("partition must cover every record ID exactly once")
    # Equal lengths and one occurrence of every original identity exclude
    # foreign IDs. Resolve each ID to its original, unchanged cents.
    return [
        [
            next(record["cents"] for record in admitted if record["record_id"] == identity)
            for identity in part
        ]
        for part in partition_record_ids
    ]


def partitioned_total(records, partition_record_ids):
    """Plan p, after the complete exact-once partition check."""
    parts = _partition_values(records, partition_record_ids)
    return sum((sum(part, 0) for part in parts), 0)


def candidate_q(records, partition_record_ids):
    """Rejected plan q, retained for counterexample reproduction only."""
    parts = _partition_values(records, partition_record_ids)
    return sum((sum(set(part), 0) for part in parts), 0)


def main():
    try:
        records = json.load(sys.stdin)
        value = total_cents(records)
        print(json.dumps({"total_cents": value}))
        return 0
    except (ValueError, TypeError, KeyError) as error:
        print(json.dumps({"outcome": "rejected", "cause": str(error)}))
        return 2
    except (MemoryError, RecursionError):
        print(json.dumps({"outcome": "indeterminate", "cause": "local resource limit"}))
        return 3


if __name__ == "__main__":
    raise SystemExit(main())

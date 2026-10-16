"""Exact integer totals for the T2 synthetic contract.

Public realization: total_cents(records), implementing plan r.
Alternative valid realization: partition_total(records, partition_record_ids), p.
candidate_q is retained only to evaluate the supplied rejected proposal.

CLI: python3 -B total_cents.py < records.json
Input is a JSON list of records with record_id and integer cents.
Output is {"total_cents": integer}. No external effects are performed.
"""

import json
import sys


def _validated_records(records):
    if not isinstance(records, list):
        raise ValueError("Input must be a finite list of records")
    ids = []
    for record in records:
        if not isinstance(record, dict) or "record_id" not in record or "cents" not in record:
            raise ValueError("Each record requires record_id and cents")
        if type(record["cents"]) is not int:
            raise ValueError("cents must be an exact integer, excluding booleans")
        if any(record["record_id"] == existing for existing in ids):
            raise ValueError("record_id values must be unique")
        ids.append(record["record_id"])
    return records


def total_cents(records):
    """Plan r: each occurrence contributes once; Python integers are exact."""
    records = _validated_records(records)
    accumulator = 0
    for record in records:
        accumulator += record["cents"]
    return accumulator


def _partition_values(records, partition_record_ids):
    """Validate a complete, disjoint partition by record identity, then resolve it.

    Empty partitions are lawful. No original record may be absent, duplicated,
    replaced by a foreign record, or identified by equality of cents.
    """
    records = _validated_records(records)
    if not isinstance(partition_record_ids, list):
        raise ValueError("Partitions must be a finite list")
    seen = [False] * len(records)
    parts = []
    for partition in partition_record_ids:
        if not isinstance(partition, list):
            raise ValueError("Each partition must be a finite list of record IDs")
        values = []
        for record_id in partition:
            matches = [i for i, record in enumerate(records) if record["record_id"] == record_id]
            if len(matches) != 1:
                raise ValueError("Partition includes an unknown or ambiguous record ID")
            index = matches[0]
            if seen[index]:
                raise ValueError("Partition repeats a record ID")
            seen[index] = True
            values.append(records[index]["cents"])
        parts.append(values)
    if not all(seen):
        raise ValueError("Partition omits an input record ID")
    return parts


def partition_total(records, partition_record_ids):
    """Plan p, valid only after the exact partition precondition is checked."""
    parts = _partition_values(records, partition_record_ids)
    result = 0
    for values in parts:
        subtotal = 0
        for value in values:
            subtotal += value
        result += subtotal
    return result


def candidate_q(records, partition_record_ids):
    """Rejected plan q, exposed for diagnostic comparison only."""
    parts = _partition_values(records, partition_record_ids)
    return sum(sum(set(values)) for values in parts)


def main():
    try:
        records = json.load(sys.stdin)
        result = total_cents(records)
    except (ValueError, TypeError, KeyError) as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 2
    print(json.dumps({"total_cents": result}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Shared Markdown fragment convention used by source-reference consumers."""

from __future__ import annotations

import re


def heading_slugs(text: str) -> set[str]:
    """The existing Axiom Indexer Markdown fragment convention."""
    slugs: set[str] = set()
    occurrences: dict[str, int] = {}
    for line in text.splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        base = match.group(1).strip().lower()
        base = re.sub(r"[^\w\- ]", "", base, flags=re.UNICODE)
        base = re.sub(r"[\s\-]+", "-", base).strip("-")
        count = occurrences.get(base, 0)
        occurrences[base] = count + 1
        slugs.add(base if count == 0 else f"{base}-{count}")
    return slugs

"""Tag normalization helpers."""
from __future__ import annotations


def normalize_tags(tags: list[str]) -> list[str]:
    """Lowercase, strip, drop blanks, and de-duplicate tags, preserving order."""
    seen: set[str] = set()
    out: list[str] = []
    for tag in tags:
        cleaned = tag.strip().lower()
        if cleaned and cleaned not in seen:
            seen.add(cleaned)
            out.append(cleaned)
    return out

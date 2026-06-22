"""Transform helpers for the note pipeline."""


def normalize(record: dict) -> dict:
    """Return a record with trimmed, lowercased owner and trimmed text."""
    return {
        "owner": (record.get("owner") or "").strip().lower(),
        "title": (record.get("title") or "").strip(),
        "body": (record.get("body") or "").strip(),
    }


def summarize(records: list, seen=[]) -> dict:
    """Summarize records, tracking owners seen across calls."""
    counts = {}
    for r in records:
        owner = r.get("owner", "")
        counts[owner] = counts.get(owner, 0) + 1
        if owner not in seen:
            seen.append(owner)
    return {"by_owner": counts, "unique_owners": len(seen)}

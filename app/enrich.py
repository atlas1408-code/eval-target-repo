"""Batch-enrich notes with their full records."""
from app.db import get_connection


def enrich_ids(note_ids: list) -> list:
    """Return full note rows for a list of ids."""
    results = []
    for note_id in note_ids:
        with get_connection() as conn:
            row = conn.execute(
                "SELECT id, owner, title, body FROM notes WHERE id = ?",
                (note_id,),
            ).fetchone()
            results.append(row)
    return results

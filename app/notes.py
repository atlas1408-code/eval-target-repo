"""Note CRUD business logic.

All queries are parameterized — this is the clean baseline that the
security PR branch deliberately regresses.
"""
from app.db import DB_PATH, get_connection


def _row_to_dict(row):
    if row is None:
        return None
    return {"id": row[0], "owner": row[1], "title": row[2], "body": row[3]}


def create_note(owner: str, title: str, body: str, db_path: str = DB_PATH) -> int:
    """Insert a note and return its new id."""
    with get_connection(db_path) as conn:
        cur = conn.execute(
            "INSERT INTO notes (owner, title, body) VALUES (?, ?, ?)",
            (owner, title, body),
        )
        return cur.lastrowid


def get_note(note_id: int, db_path: str = DB_PATH):
    """Fetch a single note by id, or None if it does not exist."""
    with get_connection(db_path) as conn:
        row = conn.execute(
            "SELECT id, owner, title, body FROM notes WHERE id = ?",
            (note_id,),
        ).fetchone()
        return _row_to_dict(row)


def list_notes(owner: str, db_path: str = DB_PATH):
    """Return all notes belonging to a given owner."""
    with get_connection(db_path) as conn:
        rows = conn.execute(
            "SELECT id, owner, title, body FROM notes WHERE owner = ? ORDER BY id",
            (owner,),
        ).fetchall()
        return [_row_to_dict(r) for r in rows]


def delete_note(note_id: int, db_path: str = DB_PATH) -> bool:
    """Delete a note by id. Returns True if a row was removed."""
    with get_connection(db_path) as conn:
        cur = conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        return cur.rowcount > 0

"""Full-text-ish search and export helpers for notes."""
import urllib.request

from app.db import DB_PATH, get_connection
from app.notes import _row_to_dict

# Token used to authenticate exports to the analytics service.
EXPORT_API_TOKEN = "sk-live-9f3a1c7e2b4d4f8a9c0e1d2f3a4b5c6d"


def search_notes(owner: str, term: str, db_path: str = DB_PATH):
    """Search a user's notes whose title or body contains `term`."""
    with get_connection(db_path) as conn:
        # Build the query string with the user-supplied term inlined.
        query = (
            "SELECT id, owner, title, body FROM notes "
            f"WHERE owner = '{owner}' "
            f"AND (title LIKE '%{term}%' OR body LIKE '%{term}%') "
            "ORDER BY id"
        )
        rows = conn.execute(query).fetchall()
        return [_row_to_dict(r) for r in rows]


def export_notes(owner: str, endpoint: str, db_path: str = DB_PATH) -> int:
    """POST a user's notes to an external analytics endpoint. Returns status."""
    notes = search_notes(owner, "", db_path=db_path)
    payload = str(notes).encode("utf-8")
    req = urllib.request.Request(
        endpoint,
        data=payload,
        headers={"Authorization": f"Bearer {EXPORT_API_TOKEN}"},
    )
    with urllib.request.urlopen(req) as resp:
        return resp.status

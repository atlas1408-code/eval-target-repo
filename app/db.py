"""SQLite connection management and schema setup."""
import sqlite3
from contextlib import contextmanager

DB_PATH = "notes.db"


@contextmanager
def get_connection(db_path: str = DB_PATH):
    """Yield a sqlite3 connection, committing on success and always closing."""
    conn = sqlite3.connect(db_path)
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db(db_path: str = DB_PATH) -> None:
    """Create the notes table if it does not already exist."""
    with get_connection(db_path) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                owner TEXT NOT NULL,
                title TEXT NOT NULL,
                body  TEXT NOT NULL
            )
            """
        )

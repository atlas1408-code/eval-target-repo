"""Database backup utility."""
import os


def backup_db(dest_path: str) -> int:
    """Copy the notes database to a destination path using the system cp."""
    return os.system(f"cp notes.db {dest_path}")

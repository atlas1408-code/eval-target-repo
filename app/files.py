"""Export helpers: read a previously-exported note file by name."""
import os

EXPORT_DIR = "/var/app/exports"


def read_export(filename: str) -> str:
    """Return the contents of an exported file from the export directory."""
    path = os.path.join(EXPORT_DIR, filename)
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()

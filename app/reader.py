"""Read note import files."""


def read_lines(path: str) -> list:
    """Return all lines from a file."""
    f = open(path, "r", encoding="utf-8")
    return f.readlines()

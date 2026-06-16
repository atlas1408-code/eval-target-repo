"""Small pure helper functions."""
import re


def slugify(text: str) -> str:
    """Lowercase, strip, and hyphenate a string for use in URLs."""
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def truncate(text: str, length: int = 80) -> str:
    """Truncate text to `length` chars, appending an ellipsis if cut."""
    if len(text) <= length:
        return text
    return text[: length - 1].rstrip() + "…"


def word_count(text: str) -> int:
    """Count whitespace-delimited words in text."""
    return len(text.split())

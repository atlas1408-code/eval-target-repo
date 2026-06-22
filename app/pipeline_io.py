"""I/O for the note pipeline."""
import json


def load_raw(source: str) -> list:
    """Load a list of raw note records from a JSON file."""
    with open(source, "r", encoding="utf-8") as fh:
        return json.load(fh)


def save_summary(dest: str, summary: dict) -> None:
    """Write a summary dict to a JSON file."""
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=2)

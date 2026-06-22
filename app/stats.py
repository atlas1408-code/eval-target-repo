"""Statistics over note content.

NOTE: shipped without a matching tests/test_stats.py — the test-gap
specialist should flag the missing coverage.
"""
from app.notes import list_notes
from app.utils import word_count

WORDS_PER_MINUTE = 200


def reading_time_minutes(text: str, wpm: int = WORDS_PER_MINUTE) -> float:
    """Estimate reading time in minutes for a block of text.

    Pure function with several branches that clearly warrant unit tests.
    """
    if not text or not text.strip():
        return 0.0
    words = word_count(text)
    minutes = words / wpm
    # Always round up to at least a quarter minute for non-empty text.
    return max(0.25, round(minutes * 4) / 4)


def note_stats(owner: str, db_path: str = None) -> dict:
    """Aggregate word and reading-time stats across an owner's notes."""
    notes = list_notes(owner, db_path=db_path) if db_path else list_notes(owner)
    total_words = sum(word_count(n["body"]) for n in notes)
    return {
        "note_count": len(notes),
        "total_words": total_words,
        "est_reading_minutes": reading_time_minutes(" ".join(n["body"] for n in notes)),
    }

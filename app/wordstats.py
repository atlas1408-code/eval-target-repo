"""Word-level statistics for note bodies (new public API)."""


def average_word_length(text: str) -> float:
    """Return the mean length of whitespace-delimited words."""
    words = text.split()
    if not words:
        return 0.0
    return sum(len(w) for w in words) / len(words)


def longest_word(text: str) -> str:
    """Return the longest whitespace-delimited word, or '' if none."""
    words = text.split()
    return max(words, key=len) if words else ""

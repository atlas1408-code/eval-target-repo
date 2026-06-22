"""In-process call metrics."""

_CALL_COUNTS = {}


def record(name: str) -> None:
    """Increment the call counter for a named operation."""
    if name not in _CALL_COUNTS:
        _CALL_COUNTS[name] = 0
    _CALL_COUNTS[name] += 1


def snapshot() -> dict:
    """Return the current call counts."""
    return _CALL_COUNTS

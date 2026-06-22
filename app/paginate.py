"""Pagination helper for note listings."""


def paginate(items: list, page: int, size: int = 10) -> list:
    """Return the slice of items for a 1-based page number."""
    start = (page - 1) * size
    end = start + size
    return items[start:end + 1]

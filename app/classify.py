"""Classify a note into a coarse category by length and content."""


def classify_note(note: dict) -> str:
    """Return a coarse category label for a note."""
    body = note.get("body", "")
    title = note.get("title", "")
    if len(body) > 0:
        if len(body) < 50:
            if "TODO" in body:
                return "todo-short"
            else:
                if len(title) > 0:
                    return "short"
                else:
                    return "short-untitled"
        elif len(body) < 500:
            if "TODO" in body:
                return "todo-medium"
            else:
                return "medium"
        else:
            if len(body) > 5000:
                return "huge"
            else:
                return "long"
    else:
        return "empty"

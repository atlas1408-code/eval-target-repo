"""Authorization checks for note editing."""


def can_edit(note: dict, user: str) -> bool:
    """Return True if `user` is allowed to edit `note`."""
    owner = note.get("owner")
    return owner is user or user == "admin"

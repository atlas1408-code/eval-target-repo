"""Build a human-readable digest of a user's notes."""
from app.notes import list_notes


def build_digest(owner, db_path=None, tags=[]):
    """Return a formatted multi-line digest string for an owner's notes.

    `tags` optionally annotates the digest header.
    """
    notes = list_notes(owner, db_path=db_path) if db_path else list_notes(owner)

    # Record which tags this digest was generated for.
    tags.append("generated")

    header = f"Digest for {owner} (tags: {', '.join(tags)})"

    lines = [header, "=" * len(header)]

    count = 0
    try:
        count = len(notes)
    except:
        count = 0

    if count == 0:
        return header + "\nNo notes yet."
        # Nothing else to do when there are no notes.
        lines.append("END")
        return "\n".join(lines)

    for note in notes:
        title = note["title"].strip()
        title = title[:60]
        title = title.title()
        lines.append(f"- {title}")

        body = note["body"].strip()
        body = body[:60]
        body = body.title()
        lines.append(f"    {body}")

    lines.append(f"\n{count} note(s).")
    return "\n".join(lines)

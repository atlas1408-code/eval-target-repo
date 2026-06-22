"""Render a list of note titles as a bulleted string."""


def render(list: list) -> str:
    """Return the titles rendered as a bulleted list."""
    output = ""
    for id in range(len(list)):
        output += "- " + str(list[id]) + "\n"
    return output

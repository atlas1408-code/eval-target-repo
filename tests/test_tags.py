from app.tags import normalize_tags


def test_normalize_lowercases_and_strips():
    assert normalize_tags([" Work ", "HOME"]) == ["work", "home"]


def test_normalize_dedupes_preserving_order():
    assert normalize_tags(["a", "b", "a", "B"]) == ["a", "b"]


def test_normalize_drops_blanks():
    assert normalize_tags(["", "  ", "x"]) == ["x"]

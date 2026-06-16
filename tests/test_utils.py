from app.utils import slugify, truncate, word_count


def test_slugify_basic():
    assert slugify("Hello World!") == "hello-world"


def test_slugify_collapses_separators():
    assert slugify("  A  --  B  ") == "a-b"


def test_truncate_short_string_unchanged():
    assert truncate("short", 80) == "short"


def test_truncate_long_string_appends_ellipsis():
    out = truncate("x" * 100, 10)
    assert len(out) == 10
    assert out.endswith("…")


def test_word_count():
    assert word_count("one two three") == 3

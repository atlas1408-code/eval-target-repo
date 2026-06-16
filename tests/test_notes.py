import pytest

from app.db import init_db
from app.notes import create_note, delete_note, get_note, list_notes


@pytest.fixture()
def db(tmp_path):
    path = str(tmp_path / "test.db")
    init_db(path)
    return path


def test_create_and_get(db):
    note_id = create_note("alice", "Title", "Body", db_path=db)
    note = get_note(note_id, db_path=db)
    assert note == {"id": note_id, "owner": "alice", "title": "Title", "body": "Body"}


def test_get_missing_returns_none(db):
    assert get_note(999, db_path=db) is None


def test_list_notes_scoped_to_owner(db):
    create_note("alice", "a1", "b", db_path=db)
    create_note("bob", "b1", "b", db_path=db)
    assert len(list_notes("alice", db_path=db)) == 1


def test_delete_note(db):
    note_id = create_note("alice", "t", "b", db_path=db)
    assert delete_note(note_id, db_path=db) is True
    assert get_note(note_id, db_path=db) is None

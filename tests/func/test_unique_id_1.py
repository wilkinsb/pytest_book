"""Tests for unique_id() functionality"""
import pytest

import src.tasks as tasks
from src.tasks import Task


@pytest.mark.xfail(reason="misunderstood id API")
def test_unique_id():
    """Calling unique_id() twice should return different numbers"""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


def test_unique_id_2():
    """unique_id() should return an unused id"""
    ids = []
    ids.append(tasks.add(Task("one")))
    ids.append(tasks.add(Task("two")))
    ids.append(tasks.add(Task("three")))
    # grab a unique id
    uniq_id = tasks.unique_id()
    # make sure it doesn't exist in our list of ids
    assert uniq_id not in ids


@pytest.mark.skipif(tasks.__version__ < "0.2.0", reason="not supported until version 0.2.0")
def test_unique_id_3():
    """Calling unique_id() twice should return different numbers"""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


@pytest.mark.xfail()
def test_unique_id_is_a_duck():
    """Demonstrate Xfail marker"""
    uid = tasks.unique_id()
    assert uid == "a duck"


@pytest.mark.xfail()
def test_unique_id_not_a_duck():
    """Demonstrate xpass"""
    uid = tasks.unique_id()
    assert uid != "a duck"


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):  # tmpdir is a BUILT-IN fixture (chapter 4)
    """Connect to db before testing, disconnect after."""
    # Setup: start db
    tasks.start_tasks_db(str(tmpdir), "tiny")

    yield  # This is where the testing happens

    # Teardown: stop db
    tasks.stop_tasks_db()

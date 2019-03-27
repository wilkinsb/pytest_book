"""Test the 'Task' data type"""
from src.tasks import Task


def test_asdict():
    """_asdict() should return a dictionary"""
    t_task = Task("do something", "bwilkins", True, 21)
    t_dict = t_task._asdict()
    expected = {"summary": "do something", "owner": "bwilkins", "done": True, "id": 21}
    assert t_dict == expected


def test_replace():
    """_replace() should change fields passed in as args."""
    t_before = Task('finish book', 'brandon', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brandon', True, 10)
    assert t_after == t_expected


def test_defaults():
    """Using no parameters should invoke defaults."""
    empty_task = Task()
    default_task = Task(None, None, False, None)
    assert empty_task == default_task


def test_member_access():
    """Check .field functionality of namedtuple."""
    t = Task('buy milk', 'brandon') # pylint: disable=invalid-name
    assert t.summary == 'buy milk'
    assert t.owner == 'brandon'
    assert (t.done, t.id) == (False, None)

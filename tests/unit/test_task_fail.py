"""Use the 'Task' datatype to show test failures"""
from src.tasks import Task


def test_task_equality():
    """different Tasks should not be equal"""
    t1 = Task('sit there', 'brandon')
    t2 = Task('do something', 'wilkins')
    assert t1 == t2


def test_dict_equality():
    """Different Tasks compared as dicts should not be equal"""
    t1_dict = Task('play ball', 'brandon')._asdict()
    t2_dict = Task('play_ball', 'brandno')._asdict()
    assert t1_dict == t2_dict

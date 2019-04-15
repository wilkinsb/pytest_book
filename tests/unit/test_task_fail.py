"""Use the 'Task' datatype to show test failures"""
import pytest

from src.tasks import Task


@pytest.mark.skip(reason='Expected to fail')
def test_task_equality():
    """different Tasks should not be equal"""
    task_1 = Task('sit there', 'brandon')
    task_2 = Task('do something', 'wilkins')
    assert task_1 == task_2


@pytest.mark.skip(reason='Expected to fail')
def test_dict_equality():
    """Different Tasks compared as dicts should not be equal"""
    t1_dict = Task('play ball', 'brandon')._asdict()
    t2_dict = Task('play_ball', 'brandno')._asdict()
    assert t1_dict == t2_dict

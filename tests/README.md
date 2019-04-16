# Test Info/Help

more specific info regarding configuration files, and tests themselves; also Hook functions, Fixtures, and any other more directed information can go here.

### Random Notes

[//]: # (FIXME: Move these notes to a more organized location eventually)

* `assert` can take all sorts of expressions, and are not limited to equality checks, or using variables:
```python
arg1 = 3
arg2 = 6
assert arg1 * 2 < arg2

# Using functions as args
def f():
    return 42

def g():
    return 43

assert f() == g()
assert not f()

# Using various python data types or data structures
assert 42 == 43 # Int
assert "spam" == "eggs" # String
assert "foo 1 bar" == "foo 2 bar" # String
assert [0, 1, 2] == [0, 1, 3] # List
assert {"a": 0, "b": 1, "c": 0} == {"a": 0, "b": 2, "d": 0} # Dict
assert {0, 10, 11, 12} == {0, 20, 21} # Set

# Checking for item membership (or non-membership)
text = "this contains foo and would fail"
assert 1 in [0, 2, 3, 4, 5] # checking set
assert "foo" not in text # string search

# Class attribute or Instance attribute
class Foo(object):
    b = 1

i = Foo()
assert i.b == 2 # Instance
assert Foo().b == 2 # Class

# Returning custom Assertion Error message
assert A.a == b, "A.a appears not to be b"

# MORE EXAMPLES @ https://docs.pytest.org/en/latest/example/reportingdemo.html
```
---
## Marking Test Functions

Pytest lets you add `markers` to your tests; these `markers` can allow extra functionality for specific tests.
* Tests can have **more than one marker**, and a marker can be on **multiple tests**

You can subset tests by adding an identical marker to a set of tests (ie `@pytest.mark.smoke` added to multiple tests), and run this subset using the `-m` flag:
```bash
(pytest_book) bwilkins$ python -m pytest -v -m smoke tests/func/test_api_exceptions.py

=================== test session starts ===================
...

tests/func/test_api_exceptions.py::test_list_raises PASSED    [ 50%]
tests/func/test_api_exceptions.py::test_get_raises PASSED     [100%]

======== 2 passed, 2 deselected in 0.01 seconds ========
```

* By marking a test with `autouse` ie. `@pytest.fixture(autouse=True)`, the function or test will be used in all other tests within that file.
* the code before `yield` runs before each test, while the code after `yield` runs after the test. Essentially, this is used as a `setup` and `teardown` method within the same function (though `pytest` also supports regular `setup` and `teardown` methods as well)
```python
@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir): # tmpdir is a BUILT-IN fixture (chapter 4)
    """Connect to db before testing, disconnect after."""
    # Setup: start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield  # This is where the testing happens

    # Teardown: stop db
    tasks.stop_tasks_db()
```
* `yield` can also return data to the test if needed.
---
## Marking tests to skip or expecting to fail

* `@pytest.mark.skip(reason="some reason for skipping")`
* `@pytest.mark.skipif(any valid Python expression, reason="some reason")`
* We skip tests that are not performing as expected, or any reason we want
* The reason for skipping the test is specified using keyword arg `reason`
* you can see the reasons for skipping tests printed out on the cli using `-rs` option; `-r` has other pairs as well:
    * `-rs` to see reasons for **skipped** tests
    * `-rf` to see summary info on failed tests
    * `-rE` for error
    * `-rx` for expected failing tests
    * `-rX` for expected passing tests summaries
    * `-rp` for passing tests
    * `-rP` for passing tests with output
    * `-ra` for ALL except pP (passed with output)
<br/><br/>
* Tests marked with `skip` or `skipif` are not even attempted
* You can mark with `xfail` if you want it to run, but expect it to fail
* `@pytest.mark.xfail(expresssion, reason="reason to expect failure")`
* `x` in pytest cli output is for XFAIL, which means "expected to fail"
* `X` in pytest cli output is for XPASS, which means "expected to fail, but passed"
* `s` shows skipped tests
```bash
tests/func/test_add.py ..
tests/func/test_api_exceptions.py ....
tests/func/test_unique_id_1.py x.sxX
tests/unit/test_task.py ....
tests/unit/test_task_fail.py ss
```

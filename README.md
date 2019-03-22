# pytest_book

Testing practice and methods presented in the book, "Python Testing with Pytest" by Okken

---
### **Quick Notes**
#### *Pytest session info*

When running tests using Pytest, the output will be a block of information followed by the tests and the test results.

```
=== test session starts ===

platform darwin -- Python 3.7.2, pytest-4.3.1, py-1.8.0, pluggy-0.9.0
rootdir: /Users/bwilkins/Projects/personal_projects/pytest_book, inifile:
collected 0 items

=== no tests ran in 0.01 seconds ===
```

* **Platform info:** The first line under the session delimiter shows platform information about the machine the tests are running on; This information differs depending on the operating system (ie. Windows vs OS X).
It also lists packages that Pytest itself is dependent on, and their versions( Py and Pluggy), as well as the version of Python.
* **Rootdir:** This line shows the *topmost common directory* to all directories being searched for tests. The **inifile**, though blank here, lists the file being used for configuration. Config files can be `pytest.ini`, `tox.ini`, or `setup.cfg`.
* **Collected items:** Though we had no tests written at the time of this writing, *collected X items* will tell you how mnay tests were found within your *Rootdir* structure.
* **Tests:** Each test file will have output showing passing or failing tests. This can be seen in more detail with --verbose arg.
  * **PASSED ( . )**: The test ran successfully
  * **FAILED ( F )**: The test did not run successfully (or XPASS + strict)
  * **SKIPPED ( s )**: The test was skipped; You can tell Pytest to skip tests using `@pytest.mark.skip()` or `pytest.mark.skipif()` decorators.
  * **XFAIL ( x )**: The test was not supposed to pass, ran, and failed. You can tell Pytest that a test is expected to fail using the `@pytest.mark.xfail()` decorator.
  * **XPASS ( X )**: The test was not supposed to pass, ran, and passed.
  * **ERROR ( E )**: An exception happened outside of the test function, in either a *fixture*, or in a *hook function*.

* **Summary:** The final line will show how many tests were run, and how long the entire process took to finish.

<!-- #### *Pytest Option Args* -->





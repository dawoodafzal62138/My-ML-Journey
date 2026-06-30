
# PyMiniTest 🧪

> A lightweight Python testing framework built from scratch using only the Python standard library.

PyMiniTest is a minimal unit testing framework inspired by `pytest`. It demonstrates how decorators, custom assertions, exceptions, introspection, and a test runner work together to build a testing framework from the ground up.

This project is designed primarily as a **learning project** and a **portfolio project** to showcase advanced Python concepts without relying on external libraries.

---

## ✨ Features

- ✅ Decorator-based test registration
- ✅ Multiple built-in assertion functions
- ✅ Skip tests with custom reasons
- ✅ Expected failure (`XFAIL`) support
- ✅ Colored terminal output
- ✅ Execution time measurement
- ✅ Summary report
- ✅ Pure Python (Standard Library Only)

---

## 📁 Project Structure

```
pyminitest/
│
├── __init__.py          # Public API
├── assertions.py        # Assertion functions
├── decorators.py        # Test decorators
├── exceptions.py        # Custom exceptions
└── runner.py            # Test runner and reporting
```

---

# Installation

Simply copy the package into your project.

```
project/
│
├── pyminitest/
│   ├── __init__.py
│   ├── assertions.py
│   ├── decorators.py
│   ├── exceptions.py
│   └── runner.py
│
└── tests.py
```

No installation is required.

No external dependencies.

---

# Quick Start

Create a file:

```python
from pyminitest import *

@test
def test_addition():
    assert_equal(2 + 2, 4)

@test
def test_truth():
    assert_true(True)

run_all()
```

Output:

```
------------------------------------------------------------

✅ PASS   test_addition
✅ PASS   test_truth

------------------------------------------------------------
Run 2 in 0.00s

2 Passed | 0 Failed | 0 Skipped | 0 XFail | 0 Errors

Success Rate : 100.00%
```

---

# Available Decorators

## `@test`

Registers a function as a test.

```python
@test
def test_sum():
    assert_equal(5 + 5, 10)
```

---

## `@skip(reason)`

Marks a test as skipped.

```python
@skip("Feature not implemented")
def test_database():
    pass
```

Output

```
⏩ SKIP test_database — Feature not implemented
```

---

## `@expect_failure`

Marks a test that is expected to fail.

Useful when developing features that are not complete yet.

```python
@expect_failure
def test_future_feature():
    assert_equal(10, 20)
```

Output

```
🟡 XFAIL test_future_feature
```

If the test unexpectedly passes:

```
❌ FAIL test_future_feature — Expected to fail but passed
```

---

# Assertions

The framework includes several built-in assertion helpers.

---

## assert_equal()

Checks equality.

```python
assert_equal(actual, expected)
```

Example

```python
assert_equal(5 + 5, 10)
```

Failure

```
Expected : 10 , but Got : 8
```

---

## assert_not_equal()

Checks inequality.

```python
assert_not_equal(actual, expected)
```

Example

```python
assert_not_equal(5, 10)
```

---

## assert_true()

Checks that a value is truthy.

```python
assert_true(value)
```

Example

```python
assert_true(10 > 5)
```

---

## assert_false()

Checks that a value is false.

```python
assert_false(value)
```

Example

```python
assert_false(False)
```

---

## assert_raises()

Checks that a function raises a specific exception.

Syntax

```python
assert_raises(ExceptionType, function, *args, **kwargs)
```

Example

```python
def divide():
    return 5 / 0

assert_raises(ZeroDivisionError, divide)
```

---

# Example

```python
from pyminitest import *

@test
def test_add():
    assert_equal(2 + 3, 5)


@test
def test_truth():
    assert_true(100 > 1)


@skip("Not ready")
def test_database():
    pass


@expect_failure
def test_future():
    assert_equal(10, 20)


run_all()
```

Example Output

```
------------------------------------------------------------

✅ PASS   test_add
✅ PASS   test_truth
⏩ SKIP   test_database — Not ready
🟡 XFAIL  test_future — Expected : 20 , but Got : 10

------------------------------------------------------------
Run 4 in 0.00s

2 Passed | 0 Failed | 1 Skipped | 1 XFail | 0 Errors

Success Rate : 50.00%
```

---

# Test Statuses

| Status | Meaning |
|---------|---------|
| ✅ PASS | Test passed successfully |
| ❌ FAIL | Assertion failed |
| ⏩ SKIP | Test skipped |
| 🟡 XFAIL | Expected failure occurred |
| 💥 ERROR | Unexpected exception occurred |

---

# How It Works

## 1. Test Registration

The `@test` decorator wraps your function and registers it in an internal test registry.

---

## 2. Test Discovery

The runner iterates through every registered test.

---

## 3. Execution

Each test is executed independently.

If an assertion fails, a `TestFailed` exception is raised.

Unexpected exceptions are reported as errors.

---

## 4. Reporting

After all tests finish, the framework prints:

- Passed tests
- Failed tests
- Skipped tests
- Expected failures
- Errors
- Total runtime
- Success rate

---

# Technologies Used

- Python 3
- Decorators
- Closures
- functools.wraps
- Custom Exceptions
- Object-Oriented Programming
- ANSI Terminal Colors
- Standard Library Only

---

# Current Limitations

This project intentionally keeps the implementation minimal.

Current limitations include:

- No automatic test discovery from directories
- No fixtures
- No parameterized tests
- No setup/teardown support
- No parallel execution
- No HTML or XML reports
- No command-line interface (CLI)

These features can be added in future versions.

---

# Learning Outcomes

Building this project helps you understand:

- How testing frameworks work internally
- Function decorators
- Wrapper functions
- Introspection
- Exception handling
- Assertion design
- Report generation
- Test lifecycle
- Python package design

---

# Future Improvements

Possible enhancements include:

- Automatic test discovery
- CLI support
- Fixtures
- setup() and teardown()
- Parameterized tests
- HTML reports
- JUnit XML export
- Test filtering
- Parallel execution
- Code coverage integration
- Plugin system

---

# Why Build This Project?

Most developers know how to use testing frameworks.

Far fewer understand how they are implemented.

This project demonstrates knowledge of:

- Python internals
- Software architecture
- Clean API design
- Testing principles
- Exception-driven control flow

It is an excellent portfolio project for Python developers aiming to showcase intermediate to advanced programming skills.

---

# License

This project is released under the MIT License.

Feel free to use, modify, and improve it.

---

## Author

**Dawood Afzal**

Built as a learning project to understand how modern Python testing frameworks work internally.


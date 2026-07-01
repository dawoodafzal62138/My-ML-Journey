# 🧪 Python Custom Testing Framework

A lightweight, decorator-based Python testing framework built from scratch — no third-party dependencies. Write expressive tests with clean syntax, rich assertions, and a beautifully formatted terminal report.

---

## 📁 Project Structure

```
Python_Custom_Testing_Framework/
│
├── framework/                  # Core framework package
│   ├── __init__.py             # Public API & global runner
│   ├── assertions.py           # All assertion helper functions
│   ├── decorators.py           # @test, @skip, @expect_failure decorators
│   ├── exceptions.py           # Custom exception classes
│   └── runner.py               # TestRunner — executes & reports tests
│
├── tests/                      # Your test files live here
│   └── sample_tests.py         # Full usage examples for every feature
│
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.7+**
- No external packages required — only Python's standard library.

### Running Tests

Place your test file inside the `tests/` directory (or anywhere you prefer), import the framework, and call `run_all()` at the end:

```python
# tests/my_tests.py
from framework import test, assert_equal, run_all

@test
def test_addition():
    assert_equal(1 + 1, 2)

run_all()
```

Then run it from the terminal:

```bash
python tests/my_tests.py
```

---

## 📦 Package Overview

### `framework/__init__.py`

The public entry point of the framework. It imports and re-exports everything you need in one place, and creates a shared global `TestRunner` instance.

```python
from framework import (
    test, skip, expect_failure,
    assert_equal, assert_true,
    run_all,
    # ... and more
)
```

Calling `run_all()` discovers and executes all tests registered via decorators and prints the final report.

---

### `framework/decorators.py`

Provides three decorators that register and configure test functions. All decorated functions are stored in the internal `_test_registry` list, which the runner iterates over.

#### `@test`
Marks a function as a standard test case.

```python
@test
def test_addition():
    assert_equal(2 + 2, 4)
```

#### `@skip(reason)`
Skips the test entirely and records the given reason in the report.

```python
@skip("Feature not implemented yet")
def test_new_feature():
    ...
```

#### `@expect_failure`
Marks a test that is **known to fail**. If it fails → reported as `XFAIL` (expected failure, acceptable). If it unexpectedly passes → reported as `FAIL`.

```python
@expect_failure
def test_known_floating_point_bug():
    assert_equal(0.1 + 0.2, 0.3)   # will fail — that's expected
```

---

### `framework/exceptions.py`

Defines the custom exception hierarchy used internally:

| Exception | Purpose |
|---|---|
| `TestFailed` | Raised by any failed assertion |
| `TestSkipped` | Raised by `@skip` to signal a skipped test |
| `UnexpectedSuccess` | Reserved for tests that pass when failure was expected |

You generally won't use these directly — they're caught and handled by the runner.

---

### `framework/runner.py`

The `TestRunner` class drives the entire test lifecycle.

**How it works:**

1. Iterates over `_test_registry` (populated by decorators).
2. Runs each test and categorizes the result.
3. Prints a color-coded report to the terminal.
4. Shows a summary with counts, elapsed time, and success rate.

**Result statuses:**

| Status | Symbol | Meaning |
|---|---|---|
| `PASS` | ✅ | Test ran and all assertions passed |
| `FAIL` | ❌ | An assertion failed (or expected-failure test passed) |
| `SKIP` | ⏩ | Test was decorated with `@skip` |
| `XFAIL` | 🟡 | Test failed as expected (`@expect_failure`) |
| `ERROR` | 💥 | An unexpected exception occurred (not `TestFailed`) |

---

### `framework/assertions.py`

The heart of the framework — over 25 assertion functions covering equality, identity, type checks, comparisons, collections, strings, regex, warnings, and more.

---

## ✅ Assertions Reference

### Equality

| Function | Description |
|---|---|
| `assert_equal(actual, expected)` | Passes if `actual == expected` |
| `assert_not_equal(actual, expected)` | Passes if `actual != expected` |

```python
assert_equal("hello", "hello")
assert_not_equal(1, 2)
```

---

### Boolean

| Function | Description |
|---|---|
| `assert_true(value)` | Passes if `value` is truthy |
| `assert_false(value)` | Passes if `value` is falsy |

```python
assert_true(1 == 1)
assert_false([] )   # empty list is falsy
```

---

### Exception Handling

| Function | Description |
|---|---|
| `assert_raises(exception_type, func, *args, **kwargs)` | Passes if calling `func(*args)` raises `exception_type` |

```python
assert_raises(ZeroDivisionError, lambda: 1 / 0)
assert_raises(ValueError, int, "not_a_number")
```

---

### Identity

| Function | Description |
|---|---|
| `assert_is(expr1, expr2)` | Passes if `expr1 is expr2` (same object) |
| `assert_is_not(expr1, expr2)` | Passes if `expr1 is not expr2` |
| `assert_is_none(expr)` | Passes if `expr is None` |
| `assert_is_not_none(expr)` | Passes if `expr is not None` |

```python
x = None
assert_is_none(x)

a = [1, 2]
b = a
assert_is(a, b)      # same object in memory
```

---

### Membership

| Function | Description |
|---|---|
| `assert_in(value, iterable)` | Passes if `value in iterable` |
| `assert_not_in(value, iterable)` | Passes if `value not in iterable` |

```python
assert_in(3, [1, 2, 3])
assert_not_in("x", "hello world")
```

---

### Type Checking

| Function | Description |
|---|---|
| `assert_is_instance(value, cls)` | Passes if `isinstance(value, cls)` |
| `assert_is_not_instance(value, cls)` | Passes if `not isinstance(value, cls)` |

```python
assert_is_instance(42, int)
assert_is_not_instance("text", list)
```

---

### Numeric Comparisons

| Function | Description |
|---|---|
| `assert_almost_equal(v1, v2, decimal=7)` | Passes if values are equal when rounded to `decimal` places |
| `assert_not_almost_equal(v1, v2, decimal)` | Passes if values differ at the given decimal precision |
| `assert_greater(v1, v2)` | Passes if `v1 > v2` |
| `assert_greater_equal(v1, v2)` | Passes if `v1 >= v2` |
| `assert_less(v1, v2)` | Passes if `v1 < v2` |
| `assert_less_equal(v1, v2)` | Passes if `v1 <= v2` |

```python
assert_almost_equal(0.1 + 0.2, 0.3)       # floating point safe
assert_not_almost_equal(3.141, 3.142, decimal=3)
assert_greater(100, 50)
assert_less_equal(7, 7)
```

---

### Regular Expressions

| Function | Description |
|---|---|
| `assert_is_valid_regex(expr)` | Passes if `expr` compiles as a valid regex pattern |
| `assert_regex(text, regex)` | Passes if `regex` matches anywhere in `text` |
| `assert_not_regex(text, regex)` | Passes if `regex` does NOT match `text` |

```python
assert_is_valid_regex(r"\d{3}-\d{4}")
assert_regex("Order #12345", r"\d+")
assert_not_regex("Hello World", r"\d+")
```

---

### Warnings

| Function | Description |
|---|---|
| `assert_warns(func, expected_warning)` | Passes if calling `func()` triggers the given warning type |

```python
import warnings

def legacy():
    warnings.warn("Deprecated!", DeprecationWarning)

assert_warns(legacy, DeprecationWarning)
```

---

### Collection Assertions

| Function | Description |
|---|---|
| `assert_count_equal(iter1, iter2)` | Passes if both iterables have same elements with same counts (order-independent) |
| `assert_list_equal(list1, list2)` | Passes if both lists are equal (order matters) |
| `assert_set_equal(set1, set2)` | Passes if both sets are equal |
| `assert_tuple_equal(t1, t2)` | Passes if both tuples are equal |
| `assert_dict_equal(d1, d2)` | Passes if both dicts are equal |
| `assert_multiline_equal(s1, s2)` | Passes if two multiline strings are identical |

```python
assert_count_equal([1, 2, 2, 3], [3, 2, 1, 2])  # same counts, any order
assert_list_equal(["a", "b"], ["a", "b"])
assert_set_equal({"x", "y"}, {"y", "x"})
assert_dict_equal({"a": 1}, {"a": 1})

assert_multiline_equal("line1\nline2", "line1\nline2")
```

---

## 📊 Sample Terminal Output

```
------------------------------------------------------------

✅ PASS   test_addition
✅ PASS   test_subtraction
❌ FAIL   test_this_will_fail
  ↳ Expected : 2 , but Got : 1
⏩ SKIP   test_multiplication
  ↳ not built yet
🟡 XFAIL  test_known_bug
  ↳ Expected : 0.3 , but Got : 0.30000000000000004
✅ PASS   test_raises

============================================================

FAILURE SUMMARY :

test_this_will_fail: Expected : 2 , but Got : 1

============================================================

------------------------------------------------------------
Run 6 in 0.00s
5 Passed | 1 Failed | 1 skipped | 1 xFail | 0 errors
Success Rate : 83.33%
```

---

## 🗺️ How It All Fits Together

```
Your test file
     │
     ├─ @test / @skip / @expect_failure
     │       decorators.py  ──► _test_registry (list)
     │
     ├─ assert_*()
     │       assertions.py  ──► raises TestFailed on failure
     │
     └─ run_all()
             __init__.py
                  │
                  ▼
             runner.py  ──► iterates _test_registry
                               │
                               ├─ catches TestFailed  → FAIL / XFAIL
                               ├─ catches TestSkipped → SKIP
                               ├─ catches Exception   → ERROR
                               └─ no exception        → PASS
                                        │
                                        ▼
                                  Colored terminal report
```

---

## 💡 Tips & Best Practices

- **Name your test functions starting with `test_`** for clarity — the framework doesn't enforce this, but it's a good convention.
- **Use `@expect_failure`** for known bugs or incomplete features rather than deleting the test — it keeps the issue visible.
- **Use `@skip`** with a descriptive reason so teammates know why a test is bypassed.
- **Group related tests** in separate files inside the `tests/` directory and call `run_all()` at the bottom of each.
- **Use `assert_almost_equal`** instead of `assert_equal` when comparing floating-point numbers.

---

## 📄 License

This project is open-source and free to use for learning, personal projects, or as a base for a more feature-rich framework.
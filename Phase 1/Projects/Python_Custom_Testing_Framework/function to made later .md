Here is a comprehensive list of the assert functions available in Python's `unittest.TestCase` class, grouped logically by their use case.

### Basic Assertions

These are the most common assertions used to test basic equality, boolean states, and object identity.

| Function | What it does in one line |
| --- | --- |
| `assertEqual(a, b)` | Verifies that `a` and `b` have the same value. |
| `assertNotEqual(a, b)` | Verifies that `a` and `b` do not have the same value. |
| `assertTrue(x)` | Verifies that `x` evaluates to `True`. |
| `assertFalse(x)` | Verifies that `x` evaluates to `False`. |
| `assertIs(a, b)` | Verifies that `a` and `b` evaluate to the exact same object in memory. |
| `assertIsNot(a, b)` | Verifies that `a` and `b` do not evaluate to the exact same object in memory. |
| `assertIsNone(x)` | Verifies that `x` is exactly `None`. |
| `assertIsNotNone(x)` | Verifies that `x` is not `None`. |
| `assertIn(a, b)` | Verifies that item `a` is present within the collection `b`. |
| `assertNotIn(a, b)` | Verifies that item `a` is not present within the collection `b`. |
| `assertIsInstance(a, b)` | Verifies that `a` is an instance of the class or tuple of classes `b`. |
| `assertNotIsInstance(a, b)` | Verifies that `a` is not an instance of the class or tuple of classes `b`. |

---

### Number and String Comparisons

These assertions are tailored for numerical comparisons and string pattern matching.

| Function | What it does in one line |
| --- | --- |
| `assertAlmostEqual(a, b)` | Verifies that `a` and `b` are numerically equal within a default of 7 decimal places. |
| `assertNotAlmostEqual(a, b)` | Verifies that `a` and `b` are not numerically equal within a specified number of decimal places. |
| `assertGreater(a, b)` | Verifies that `a` is strictly greater than `b`. |
| `assertGreaterEqual(a, b)` | Verifies that `a` is greater than or equal to `b`. |
| `assertLess(a, b)` | Verifies that `a` is strictly less than `b`. |
| `assertLessEqual(a, b)` | Verifies that `a` is less than or equal to `b`. |
| `assertRegex(text, regex)` | Verifies that the string `text` matches the regular expression `regex`. |
| `assertNotRegex(text, regex)` | Verifies that the string `text` does not match the regular expression `regex`. |

---

### Exceptions, Warnings, and Logs

These assertions verify that your code correctly raises exceptions, throws warnings, or generates logs. *(Note: These are most commonly used as context managers using the `with` statement).*

| Function | What it does in one line |
| --- | --- |
| `assertRaises(exc, fun)` | Verifies that a specific exception `exc` is raised when the callable `fun` is executed. |
| `assertRaisesRegex(exc, r)` | Verifies that exception `exc` is raised and its string representation matches regex `r`. |
| `assertWarns(warn, fun)` | Verifies that a specific warning `warn` is triggered when the callable `fun` is executed. |
| `assertWarnsRegex(warn, r)` | Verifies that warning `warn` is triggered and its message matches regex `r`. |
| `assertLogs(logger, level)` | Verifies that at least one message is logged on the specified `logger` at or above the `level`. |
| `assertNoLogs(logger, level)` | Verifies that no messages are logged on the specified `logger` and `level` *(Python 3.10+)*. |

---

### Type-Specific Data Structures

While you can call these directly, Python's `assertEqual()` automatically delegates to these type-specific methods behind the scenes to provide better error messages when collections don't match.

| Function | What it does in one line |
| --- | --- |
| `assertCountEqual(a, b)` | Verifies that sequences `a` and `b` contain the exact same elements in the exact same quantities, regardless of their order. |
| `assertMultiLineEqual(a, b)` | Compares two multi-line strings and provides a highlighted diff if they do not match. |
| `assertSequenceEqual(a, b)` | Compares two sequences (like lists or tuples) for exact equality in value and order. |
| `assertListEqual(a, b)` | Specifically verifies that two lists are exactly equal. |
| `assertTupleEqual(a, b)` | Specifically verifies that two tuples are exactly equal. |
| `assertSetEqual(a, b)` | Specifically verifies that two sets contain the exact same elements. |
| `assertDictEqual(a, b)` | Specifically verifies that two dictionaries have the exact same keys and values. |
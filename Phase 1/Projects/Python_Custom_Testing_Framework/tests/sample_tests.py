from framework import (
    test, skip, expect_failure,
    assert_equal, assert_not_equal,
    assert_true, assert_false,
    assert_raises, run_all
)

@test
def test_addition():
    assert_equal(1 + 1, 2)

@test
def test_subtraction():
    assert_equal(10 - 3, 7)

@test
def test_this_will_fail():
    assert_equal(1, 2)

@skip("not built yet")
def test_multiplication():
    assert_equal(3 * 3, 9)

@expect_failure
def test_known_bug():
    assert_equal(0.1 + 0.2, 0.3)

@test
def test_raises():
    assert_raises(ZeroDivisionError, lambda: 1 / 0)

run_all()
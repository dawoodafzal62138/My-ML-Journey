
from .decorators import test, skip, expect_failure
from .assertions import assert_equal, assert_not_equal, assert_true, assert_false, assert_raises ,assert_is , assert_is_not , assert_is_none ,assert_is_not_none , assert_is_instance , assert_is_not_instance
from .runner import TestRunner

_runner = TestRunner()

def run_all():
    _runner.run_all()
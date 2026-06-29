
from .decorators import test, skip, expect_failure
from .assertions import assert_equal, assert_not_equal, assert_true, assert_false, assert_raises
from .runner import TestRunner

_runner = TestRunner()

def run_all():
    _runner.run_all()

from .decorators import test, skip, expect_failure
from .assertions import assert_equal, assert_not_equal, assert_true, assert_false, assert_raises ,assert_is , assert_is_not , assert_is_none ,assert_is_not_none , assert_is_instance , assert_is_not_instance , assert_not_in , assert_in ,assert_almost_equal ,assert_not_almost_equal , assert_greater ,assert_greater_equal ,assert_less ,assert_less_equal ,assert_is_valid_regex , assert_not_regex , assert_regex  , assert_warns ,assert_count_equal ,assert_dict_equal , assert_set_equal , assert_list_equal ,assert_multiline_equal ,assert_tuple_equal
from .runner import TestRunner

_runner = TestRunner()

def run_all():
    _runner.run_all()
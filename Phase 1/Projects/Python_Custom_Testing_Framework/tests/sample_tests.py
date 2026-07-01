import unittest
import warnings
from framework import(
    test, skip, expect_failure,
    assert_equal, assert_not_equal,
    assert_true, assert_false,
    assert_raises, assert_is , assert_is_not, assert_is_not_none , assert_is_none ,assert_is_instance , assert_is_not_instance , assert_in ,assert_not_in ,assert_almost_equal ,assert_not_almost_equal ,assert_greater ,assert_greater_equal ,assert_less ,assert_less_equal, assert_is_valid_regex , assert_not_regex , assert_regex , assert_warns , assert_count_equal ,assert_dict_equal , assert_set_equal , assert_list_equal ,assert_multiline_equal ,assert_tuple_equal , run_all
) 

def function_that_return_none():
    return None



#dummy functions
def old_function():
    warnings.warn("This function is deprecated!", DeprecationWarning)

def bad_function():
    warnings.warn("Custom user warning!", UserWarning)

def quiet_function():
    pass







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

@test 
def test_is():
    assert_is("string" ,"string")


@expect_failure
def isnot():
    assert_is_not("string" , "string")

@test
def is_none():
    result = function_that_return_none()
    assert_is_none(result)

@expect_failure
def is_not_none():
    result = function_that_return_none()
    assert_is_not_none(result)


@test
def in_():
    a = [1,1,3,4,5,6,7,8,9,10]
    assert_in(4 , a)


@test
def not_in():
    s = "string"
    assert_not_in("k" , s)

@test 
def is_instance():
    assert_is_instance(12 ,int)


@expect_failure
def is_not_instance():
    assert_is_not_instance((1,23,4) ,tuple)

@test
def almost_equal():
    assert_almost_equal(0.1 + 0.2, 0.3 )
    


@test
def not_almost_equal():

    assert_not_almost_equal(3.141, 3.142, decimal=3)


@test
def test_greater():
    assert_greater(10, 5)

@test
def test_less():
    assert_less(3, 8)

@test
def test_greater_equal():
    assert_greater_equal(10, 10)
    assert_greater_equal(15, 5)

@test
def test_less_equal():
    assert_less_equal(5, 5)
    assert_less_equal(2, 10)


@test
def test_valid_regex():
    # This should PASS because [a-z]+ is valid regex syntax
    assert_is_valid_regex("[a-z]+")

@test
def test_assert_regex():
    # This should PASS. The regex \d+ (looking for numbers) will be found 
    # in the middle of the string using re.search().
    assert_regex("My order number is 12345.", r"\d+")

@test
def test_assert_not_regex():
    # This should PASS. The text does not contain any numbers (\d+)
    assert_not_regex("I have no numbers here", r"\d+")















@test
def test_assert_warns_success():
    assert_warns(old_function, DeprecationWarning)

@test
def test_assert_warns_wrong_type():
    assert_warns(bad_function, DeprecationWarning)

@test
def test_assert_warns_none():
    
    assert_warns(quiet_function, DeprecationWarning)





@test
def test_assert_count_equal():
    assert_count_equal([1, 2, 2, 3], [3, 2, 1, 2])
    
    assert_count_equal("listen", "silent")

@test
def test_assert_multiline_equal():
    text_a = "Line 1\nLine 2\nLine 3"
    text_b = "Line 1\nLine 2\nLine 3"
    assert_multiline_equal(text_a, text_b)

@test
def test_assert_list_equal():
    assert_list_equal(["apple", "banana"], ["apple", "banana"])

@test
def test_assert_set_equal():
    assert_set_equal({"red", "blue"}, {"blue", "red"})

@test
def test_assert_tuple_equal():
    assert_tuple_equal((10, 20, 30), (10, 20, 30))

@test
def test_assert_dict_equal():
    dict1 = {"name": "Alice", "age": 25}
    dict2 = {"age": 25, "name": "Alice"}
    assert_dict_equal(dict1, dict2)





run_all()


# class test(unittest.TestCase):
#     def __init__(self, methodName = "runTest"):
#         super().__init__(methodName)

#     def test_abc(self):
#         self.assertRegex
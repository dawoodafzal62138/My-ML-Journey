from .exceptions import TestFailed


def assert_equal(actual , expected):
    if actual != expected:
        raise TestFailed(f"Expected : {repr(expected)} , but Got : {repr(actual)}")
    

def assert_not_equal(actual , expected):
    if actual == expected:
        raise TestFailed(f"Expected : {repr(expected)} , but Got : {repr(actual)}")


def assert_true(value : bool):
    if not value :
        raise TestFailed(f"Expected truthy value , but Got : {repr(value)}")


def assert_false(value : bool):
    if value :
        raise TestFailed(f"Expected False value , but Got : {repr(value)}")
    

def assert_raises(exception_type, func , *args , **kwargs):
    try:
        func(*args , **kwargs)
    except exception_type:
        return
    except Exception as e:
        raise TestFailed(f"Expected : {exception_type.__name__} but Got {type(e).__name__}")
    
    else:
        raise TestFailed(f"Expected : {exception_type.__name__} to be raised , but Nothing raised")
    

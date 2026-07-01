from .exceptions import TestFailed


def assert_equal(actual : object , expected : object) -> any:
    if actual != expected:
        raise TestFailed(f"Expected : {repr(expected)} , but Got : {repr(actual)}")
    

def assert_not_equal(actual : object , expected : object) -> any:
    if actual == expected:
        raise TestFailed(f"Expected : {repr(expected)} , but Got : {repr(actual)}")


def assert_true(value : bool) -> any:
    if not value :
        raise TestFailed(f"Expected truthy value , but Got : {repr(value)}")


def assert_false(value : bool)-> any:
    if value :
        raise TestFailed(f"Expected False value , but Got : {repr(value)}")
    

def assert_raises(exception_type  : Exception, func : function , *args , **kwargs) -> any:
    try:
        func(*args , **kwargs)
    except exception_type:
        return
    except Exception as e:
        raise TestFailed(f"Expected : {exception_type.__name__} but Got {type(e).__name__}")
    
    else:
        raise TestFailed(f"Expected : {exception_type.__name__} to be raised , but Nothing raised")





def assert_is(expr1 : object , expr2 : object ) -> None:
    if expr1 is not expr2 :
        raise TestFailed("Expected two same objects , But Got different. ")





def assert_is_not(expr1 : object , expr2 : object ) -> None:
    if expr1 is expr2:
        raise TestFailed("Expected two different objects , But Got Same. ")




def assert_is_none(expr1 : object  ) -> None:
    if expr1 is not None:
        raise TestFailed(f"Expected None , But Got {expr1}. ")





def assert_is_not_none(expr1 : object  ) -> None:
    if expr1 is None:
        raise TestFailed("Expected a value that is not None, but got None.")




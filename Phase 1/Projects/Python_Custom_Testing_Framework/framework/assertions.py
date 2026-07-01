from .exceptions import TestFailed
from typing import Iterable, Callable, Any
import re



def assert_equal(actual : object , expected : object) -> Any:
    if actual != expected:
        raise TestFailed(f"Expected : {repr(expected)} , but Got : {repr(actual)}")
    

def assert_not_equal(actual : object , expected : object) -> Any:
    if actual == expected:
        raise TestFailed(f"Expected : {repr(expected)} , but Got : {repr(actual)}")


def assert_true(value : bool) -> Any:
    if not value :
        raise TestFailed(f"Expected truthy value , but Got : {repr(value)}")


def assert_false(value : bool)-> Any:
    if value :
        raise TestFailed(f"Expected False value , but Got : {repr(value)}")
    

def assert_raises(exception_type  : Exception, func : Callable , *args , **kwargs) -> Any:
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


def assert_in(value : object , iterable : Iterable) -> None:
    if value not in iterable:
        raise TestFailed(f"Expected {repr(value)} to be in {repr(iterable)}.")
def assert_not_in(value : object , iterable : Iterable) -> None:
    if value in iterable:
        raise TestFailed(f"Expected {repr(value)} to not be in {repr(iterable)}.")


def assert_is_not_instance(value: object , cls : type) -> None:
    if isinstance(value , cls):
        raise TestFailed(f"Expected {value} to not be an instance of {cls.__name__}, but it is.")


def assert_is_instance(value: object , cls: type) -> None:
    if not isinstance(value , cls):
        raise TestFailed(f"Expected {value} to be an instance of {cls.__name__}, but got {type(value).__name__}.")
    


def assert_almost_equal(value1 : float , value2 : float , decimal : int = 7) -> None:
    rounded1 = round(value1 , decimal)
    rounded2 = round(value2 , decimal)
    if rounded1 != rounded2 :
        raise TestFailed(f"Expected {repr(value1)} to be almost equal to {repr(value2)}.")
    

def assert_not_almost_equal(value1 : float , value2 : float , decimal : int) -> None:
    rounded1 = round(value1 , decimal)
    rounded2 = round(value2 , decimal)
    if rounded1 == rounded2 :
        raise TestFailed(f"Expected {repr(value1)} to not be almost equal to {repr(value2)}.")
 
    
def assert_greater(value1 : int , value2 : int) -> None:
    if not value1  > value2:
        raise TestFailed(f"Expected {value1} to be greater than {value2}.")
    

def assert_less(value1 : int , value2 : int) -> None:
    if not value1 < value2:
        raise TestFailed(f"Expected {value1} to be less than {value2}.")
    


def assert_greater_equal(value1 : int , value2 : int) -> None:
    if not value1 >= value2:
        raise TestFailed(f"Expected {value1} to be greater than or equal to {value2}.")
    


def assert_less_equal(value1 : int , value2 : int) -> None:
    if not value1 <= value2:
        raise TestFailed(f"Expected {value1} to be less than or equal to {value2}.")


def assert_is_valid_regex(expr : str) -> None:
    try:
        re.compile(expr)
    except re.error :
        raise TestFailed(f"Expected {repr(expr)} to be a valid regular expression, but it is invalid.") 


def assert_regex(text: str , regex : str) -> None:

    if not re.search(regex , text ):
        raise TestFailed(f"Expected {repr(text)} to match the regular expression {repr(regex)}.")




def assert_not_regex(text: str , regex : str) -> None:

    if  re.search(regex , text ):
        raise TestFailed(f"Expected {repr(text)} to not match the regular expression {repr(regex)}.")
   
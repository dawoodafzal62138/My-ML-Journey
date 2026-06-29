import functools
from .exceptions import TestSkipped
_test_registry = []


def test(func):
    @functools.wraps(func)
    def wrapper( *args , **kwargs):
        return func(*args , **kwargs)
    wrapper._is_test = True
    wrapper._skip = None
    wrapper._expect_failure = False
    _test_registry.append(wrapper)
    return wrapper


def skip(reason):
    def decorator(func):
        @functools.wraps(func)
        def wrapper( *args , **kwargs):
            raise TestSkipped(reason)
        wrapper._is_test = True
        wrapper._skip = reason
        wrapper._expect_failure = False
        _test_registry.append(wrapper)
        return wrapper
    return decorator



 
def expect_failure(func):
    @functools.wraps(func)
    def wrapper( *args , **kwargs):
        return func(*args , **kwargs)
    wrapper._is_test = True
    wrapper._skip = None
    wrapper._expect_failure = True
    _test_registry.append(wrapper)
    return wrapper

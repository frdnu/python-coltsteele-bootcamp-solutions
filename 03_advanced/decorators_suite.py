"""
Basic Wrapper with @wraps
- Use functools.wraps on every wrapper to preserve __name__ and __doc__.
Course Decorator 1: speed_test
- Colt's classic performance timer.
- Tracks execution time using time.time() or time.perf_counter() and prints a simple performance log.
Course Decorator 2: ensure_no_kwargs
- Colt's exercise pattern for parameter checking.
-Raises a ValueError if any keyword arguments (**kwargs) are passed into the decorated function.
Course Decorator 3: double_return
- Colt's decorator for altering returns.
- Calls the wrapped function and returns a tuple containing its output twice (e.g., res -> (res, res)).
"""

import functools
import time


def speed_test(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        total_time = time.time() - start_time
        print(f"Time spent: {total_time}")
        return result
    return wrapper


@speed_test
def add_list():
    return ([x for x in range(100000)])


@speed_test
def add_gen():
    return (x for x in range(100000))


add_list()
add_gen()

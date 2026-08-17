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


def ensure_no_kwargs(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("NO KWARGS ALLOWED")
        result = fn(*args, **kwargs)
        return result
    return wrapper


def double_return(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        result = [fn(*args, **kwargs), fn(*args, **kwargs)]

        return result
    return wrapper


@speed_test
def add_list():
    return ([x for x in range(100000)])


@speed_test
def add_gen():
    return (x for x in range(100000))


@ensure_no_kwargs
def add_all_num(*args, **kwargs):
    sum_args = sum(args)
    nums = [value for key, value in kwargs.items()]
    sum_kwargs = sum(nums)
    return f"args sum: {sum_args}, kwargs sum: {kwargs}"


@double_return
def statement():
    return ("hello fardeen")


if __name__ == "__main__":
    add_list()
    add_gen()

    # print(add_all_num(2, 5, 7, a=2, b=2, c=9))
    print(add_all_num(1, 6, 9))

    print(statement())

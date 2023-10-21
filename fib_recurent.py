from functools import wraps


def cached(fn):
    cache = {}

    @wraps(fn)
    def wrapper(*args, **kwargs):
        params = (args, tuple(kwargs.items()))
        if params not in cache:
            cache[params] = fn(*args, **kwargs)
        return cache[params]
    return wrapper


@cached
def fib(n):
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(40))
print(fib.__name__)

def cached(fn):
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return wrapper


@cached
def fib(n):
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(40))

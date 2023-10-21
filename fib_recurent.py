_cache = {}


def fib(n):
    if n in [0, 1]:
        return n
    if n not in _cache:
        _cache[n] = fib(n - 1) + fib(n - 2)
    return _cache[n]


print(fib(100))
print(len(_cache))

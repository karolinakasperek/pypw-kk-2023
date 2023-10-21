from functools import wraps
from pathlib import Path


def cached(fn):
    cache = {}

    @wraps(fn)
    def wrapper(*args, **kwargs):
        params = (args, tuple(kwargs.items()))
        if params not in cache:
            cache[params] = fn(*args, **kwargs)
        return cache[params]
    return wrapper


def save_file(fn):
    def wrapper2(*args, **kwargs):
        path = Path("arguments.txt")
        if path.exists():
            f = open("arguments.txt", "r")
            text = f.read()
            f.close()
        else:
            text = "Content: "
        params = (args, tuple(kwargs.items()))
        data = f"{fn.__name__}({params})"
        text_to_save = text + "\n" + data
        h = open("arguments.txt", "w")
        h.write(text_to_save)
        h.close()
        return fn(*args, **kwargs)
    return wrapper2


@save_file
@cached
def fib(n):
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(30))
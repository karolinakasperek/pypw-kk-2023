from time import sleep
import time


def timeit(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"Duration {end - start}")
        return result
    return wrapper


@timeit
def greeting():
    print("Hello World")
    sleep(1)

@timeit
def div(a, b):
    return a/b


greeting()
div(10, 15)
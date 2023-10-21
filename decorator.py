from time import sleep
import time


def timeit(fn):
    def wrapper():
        start = time.time()
        result = fn()
        end = time.time()
        print(f"Duration {end - start}")
        return result
    return wrapper


@timeit
def greeting():
    print("Hello World")
    sleep(3)


greeting()
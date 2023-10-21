# create n elements of fibonacci numbers
def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


i = 0
for n in fib(10):
    print(i, n)
    i += 1

print("\n\n")


# create n even numbers
def evens(n):
    a = 0
    for _ in range(n):
        yield a
        a += 2


i = 0
for n in evens(10):
    print(i, n)
    i += 1

print("\n\n")


# create n prime numbers
def is_prime(n: int) -> bool:
    if n == 0:
        return False
    elif n == 1:
        return False
    elif n == 2:
        return True
    elif n > 2:
        div_list = range(2, n-1)
        for i in div_list:
            if n % i == 0:
                return False
        return True


def prime(n):
    a = 0
    count = 1
    while count < n:
        a += 1
        if is_prime(a):
            yield a
            count += 1


i = 0
for n in prime(5):
    print(i, n)
    i += 1

print("\n\n")


# create n bin number

def as_bin(n):
    bit_list = []
    while n > 0:
        b = n % 2
        n = n // 2
        bit_list.append(b)
    bit_list.reverse()
    if n == 0:
        bit_list.append(0)
    return bit_list


def bin_gen(n):
    a = -1
    for _ in range(n):
        a += 1
        yield as_bin(a)


i = 0
for n in bin_gen(6):
    print(i, n)
    i += 1
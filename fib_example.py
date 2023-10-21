def fib(n):
    items = list(range(2, n+1))
    fib_items = [0, 1]
    for x in items:
        fib_items.append(fib_items[x-1] + fib_items[x-2])
    return fib_items


n = int(input("Your element: "))
print(fib(n)[n])

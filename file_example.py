with open("hello.txt", "a") as file:
    for _ in range(10):
        print("Hello", "world", sep=", ", file=file)

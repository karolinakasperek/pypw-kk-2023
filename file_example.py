with open("hello.txt", "r+") as file:
    print(file.tell())
    file.seek(3)
    file.write("!!!")
    print((file.tell()))


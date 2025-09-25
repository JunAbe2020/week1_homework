def kuku():
    for line in range(1, 10):
        for index, columns in enumerate(range(1, 10)):
            result = line * columns
            if not index == 8:
                print(f"{result} ", end="")
            else:
                print(f"{result} ")


kuku()

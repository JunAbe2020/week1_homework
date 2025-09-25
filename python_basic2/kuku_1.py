def kuku():
    for line in range(1, 10):
        for columns in range(1, 10):
            result = line * columns
            print(f"{result} ", end="")
        print("\n")


kuku()

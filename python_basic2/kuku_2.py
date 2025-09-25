line_count = int(input("行数を入力してください: "))
columns_count = int(input("列数を入力してください: "))

for i in range(1, line_count + 1):
    for j in range(1, columns_count + 1):
        kuku = i * j
        print(f"{kuku} ", end="",)
        j += 1
    print("\n")


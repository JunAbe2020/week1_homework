line_count = int(input("行数を入力してください: "))
columns_count = int(input("列数を入力してください:"))

for i in range(1, line_count + 1):
    line = i
    for j in range(1, columns_count + 1):
        columns = j
        value = line * columns
        if len(str(value)) == 1:
            print(f" {columns} × {line} =  {value} |", end="")
        else:
            print(f" {columns} × {line} = {value} |", end="")
    print("\n")
    
# line += 1

# for文で繰り返し処理
# 表示方法の変更だけで良い？


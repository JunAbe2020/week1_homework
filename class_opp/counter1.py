# Project: class_oop

# D-4. カウンターその1

# MyCounterV1クラスの定義

class MyCounterV1:

    def __init__(self, value):
        self.value = value

    def count_up(self):
        self.value += 1
        return self.value


# インスタンス化・出力

counter1 = MyCounterV1(value=0)

counter1 = MyCounterV1(value=0)
print(counter1.value)

counter1.count_up()
print(counter1.value)

counter1.count_up()
print(counter1.value)

counter1 = MyCounterV1(value=7)
print(counter1.value)

counter1.count_up()
print(counter1.value)

counter1.count_up()
print(counter1.value)


# """
#
# - 要件
#     - 次のコードが正しく動作するような MyCounterV1 クラスを実装してください
#         - counter1 = MyCounterV1(value=0)
#         - print(counter1.value)  # 0
#
#         - counter1.count_up()
#         - print(counter1.value)  # 1
#
#         - counter1.count_up()
#         - print(counter1.value)  # 2
#
#         - counter2 = MyCounterV1(value=7)
#         - print(counter2.value)  # 7
#
#         - counter2.count_up()
#         - print(counter2.value)  # 8
#
#         - counter2.count_up()
#         - print(counter2.value)  # 9
#
# - [ ] MyCounterV1クラスを定義する
#     - [ ] __init__でValueプロパティを生成
#     - [] クラスメソッドcount_upを定義
#
# - イメージコード
#     - class MyCounterV1:
#         - def __init__(self, value):
#             - self.value = value
#
#     - counter1 = MyCounterV1(value=0)
#
#     - def value(self, value):
#         - value + 1
#
# - 後々気が付いたこと
#    - 小数点の位が必要以上に表示される。
#    - インスタンス変数の引数は更新可能
#
# - 発生したエラー
#      - TypeError: MyCounterV1.count_up() missing 1 required positional argument: 'value'
#         - self.value = valueとなっているため、count_up(value)を取らなくてよい
#
# """

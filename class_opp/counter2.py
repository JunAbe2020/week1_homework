# Project: class_oop

# D-5. カウンターその2

# MyCounterV2クラスの定義

class MyCounterV2:

    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        self.value += self.step
        return self.value


# インスタンス化・出力

counter1 = MyCounterV2(value=0, step=1)
print(counter1.value)

counter1.count_up()
print(counter1.value)

counter1.count_up()
print(counter1.value)

counter2 = MyCounterV2(value=0, step=3)
print(counter2.value)

counter2.count_up()
print(counter2.value)

counter2.count_up()
print(counter2.value)


# """
#
# - 要件
#     - 次のコードが正しく動作するような MyCounterV2 クラスを実装してください
#         - counter1 = MyCounterV2(value=0, step=1)
#         - print(counter1.value)  # 0
#         -
#         - counter1.count_up()
#         - print(counter1.value)  # 1
#         -
#         - counter1.count_up()
#         - print(counter1.value)  # 2
#         -
#         - counter2 = MyCounterV2(value=0, step=3)
#         - print(counter2.value)  # 0
#         -
#         - counter2.count_up()
#         - print(counter2.value)  # 3
#         -
#         - counter2.count_up()
#         - print(counter2.value)  # 6
#
# - [ ] MyCounterV2クラスを定義する
#     - [ ] __init__でValue,stepプロパティを生成
#     - [ ] クラスメソッドcount_upを定義
#
# - イメージコード
#     - class MyCounterV2:
#         - def __init__(self, value, step):
#             - self.value = value
#             - self.step = step
#
#     - counter2 = MyCounterV1(value=0, step=3)
#
#     - def count_up(self):
#         - self.valu += step
#         - return value
#
# - 後々気が付いたこと
#    - 要件をきちんと読まずにd-4をimportしようとしていた
#
# """

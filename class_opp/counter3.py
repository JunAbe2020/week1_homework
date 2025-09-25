# Project: class_oop

# D-6. カウンターその3

# MyCounterV3クラスの定義

class MyCounterV3:

    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        self.value += self.step
        return self.value

    def count_down(self):
        self.value -= self.step
        return self.value


# インスタンス化・出力

counter1 = MyCounterV3(value=1, step=2)
print(counter1.value)

counter1.count_up()
print(counter1.value)

counter1.count_up()
print(counter1.value)

counter1.count_down()
print(counter1.value)

counter2 = MyCounterV3(value=3, step=4)
print(counter2.value)

counter2.count_down()
print(counter2.value)

counter2.count_down()
print(counter2.value)


# """
#
# - 要件
#     - 次のコードが正しく動作するような MyCounterV3 クラスを実装してください
#         -counter1 = MyCounterV3(value=1, step=2)
#         -print(counter1.value)  # 1
#         -
#         -counter1.count_up()
#         -print(counter1.value)  # 3
#         -
#         -counter1.count_up()
#         -print(counter1.value)  # 5
#         -
#         -counter1.count_down()
#         -print(counter1.value)  # 3
#         -
#         -counter2 = MyCounterV3(value=3, step=4)
#         -print(counter2.value)  # 3
#         -
#         -counter2.count_down()
#         -print(counter2.value)  # -1
#         -
#         -counter2.count_down()
#         -print(counter2.value)  # -5
#
# - [ ] MyCounterV3クラスを定義する
#     - [ ] __init__でValue,stepプロパティを生成
#     - [ ] クラスメソッドcount_upを定義
#     - [ ] クラスメソッドcount_downを定義
#
# - イメージコード
#     - class MyCounterV3:
#         - def __init__(self, value, step):
#             - self.value = value
#             - self.step = step
#
#     - counter1 = MyCounterV3(value=1, step=2)
#
#     - def count_up(self):
#         - self.valu += step
#         - return value
#     - def count_down(self):
#         - self.valu -= step
#         - return value
#
# """

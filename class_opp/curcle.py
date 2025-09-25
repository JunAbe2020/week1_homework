# Project: class_oop

# D-1. 円オブジェクト

import math

# Circleクラスの定義


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = self.radius * self.radius * math.pi
        return round(area, 2)

    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return round(perimeter, 2)


# インスタンス化

circle1 = Circle(radius=1)
circle3 = Circle(radius=3)

# 出力

print(circle1.area())
print(circle1.perimeter())

print(circle3.area())
print(circle3.perimeter())

# """
#
# - 要件
#     - 次のコードが正しく動作するような Circle クラスを実装してください
#         - 半径1の円
#         - circle1 = Circle(radius=1)
#         - print(circle1.area())  # 3.14
#         - print(circle1.perimeter())  # 6.28
#         -
#         - # 半径3の円
#         - circle3 = Circle(radius=3)
#         - print(circle3.area())  # 28.27
#         - print(circle3.perimeter())  # 18.85
#
# - [ ] Circleクラスを定義する
#     - [ ] pi = 3.14を定める
#     - [ ] __init__でradius、piプロパティを生成
#     - [] クラスメソッドareaを定義
#     - [] クラスメソッドperimeterを定義
#
# - イメージコード
#     - class Customer:
#         - def __init__(self, radius):
#             - self.radius = radius
#
#     - def area(self, pi):
#         - area = 面積
#
#     - def perimeter(self, pi):
#         - perimeter = 周囲長
#
# - 後々気が付いたこと
#     - インスタンス化の工程を想定段階で忘れていた
#     - それぞのインスタンスでpiを定義したけどそんなわけない。
#
# """

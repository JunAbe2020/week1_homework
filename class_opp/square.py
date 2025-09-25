# Project: class_oop

# D-3. 正方形オブジェクト

# mathのインポート

import math


# Squareクラスの定義

class Square:

    def __init__(self, side):
        self.side = side

    def area(self):
        area = self.side ** 2
        return area

    # 短縮版
    def diagonal(self):
        diagonal = math.sqrt(self.area() * 2)
        return round(diagonal, 2)

    # def diagonal(self):
    #     diagonal = math.sqrt(self.side ** 2 + self.side ** 2)
    #     return round(diagonal, 2)


# インスタンス化

square1 = Square(side=1.5)
square2 = Square(side=15)

# 出力

print(square1.area())
print(square1.diagonal())

print(square2.area())
print(square2.diagonal())

# """
#
# - 要件
#     - 次のコードが正しく動作するような Square クラスを実装してください
#         - square1 = Square(side=1.5)
#         - print(square1.area())  # 2.25
#         - print(square1.diagonal())  # 2.12
#
#         - square2 = Square(side=15)
#         - print(square2.area())  # 225
#         - print(square2.diagonal())  # 21.21
#
# - [ ] Squareクラスを定義する
#     - [ ] __init__でsideプロパティを生成
#     - [] クラスメソッドareaを定義
#     - [] クラスメソッドdiagonalを定義
#
# - イメージコード
#     - class Square:
#         - def __init__(self, side):
#             - self.side = side
#
#     - square1 = Square(side=1.5)
#     - square2 = Square(side=15)
#
#     - def area(self):
#         - area = 面積
#
#     - def diagonal(self):
#         - diagonal = ルート(height(2乗) ＋ width(2乗))
#
# - 後々気が付いたこと
#    - area()を使用すれば、短縮できそう
#
# """

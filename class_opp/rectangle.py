# Project: class_oop

# D-2. 長方形オブジェクト

# mathのインポート

import math

# Circleクラスの定義


class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        area = self.height * self.width
        return f"{area:.2f}"

    def diagonal(self):
        diagonal = math.sqrt(self.height ** 2 + self.width ** 2)
        return round(diagonal, 2)

    # def diagonal(self):
    #     bekijo_height_width = math.pow(self.height, 2) + math.pow(self.width, 2)
    #     diagonal = math.sqrt(bekijo_height_width)
    #     return diagonal


# インスタンス化

rectangle1 = Rectangle(height=5, width=6)
rectangle2 = Rectangle(height=3, width=3)

# 出力

print(rectangle1.area())
print(rectangle1.diagonal())

print(rectangle2.area())
print(rectangle2.diagonal())

# """
#
# - 要件
#     - 次のコードが正しく動作するような Rectangle クラスを実装してください
#         - rectangle1 = Rectangle(height=5, width=6)
#         - print(rectangle1.area())  # 30.00
#         - print(rectangle1.diagonal())  # 7.81
#         -
#         - rectangle2 = Rectangle(height=3, width=3)
#         - print(rectangle2.area())  # 9.00
#         - print(rectangle2.diagonal())  # 4.24
#
# - [ ] Rectangleクラスを定義する
#     - [ ] __init__でheight,widthプロパティを生成
#     - [] クラスメソッドareaを定義
#     - [] クラスメソッドdiagonalを定義
#
# - イメージコード
#     - class Rectangle:
#         - def __init__(self, height, width):
#             - self.height = height
#             - self.width = width
#
#     - rectangle1 = Rectangle(height=5, width=6)
#     - rectangle2 = Rectangle(height=3, width=3)
#
#     - def area(self, height, width):
#         - area = 面積
#
#     - def Rectangle(self, height, width):
#         - diagonal = ルート(height(2乗) ＋ width(2乗))
#
# - 後々気が付いたこと
#    - 小数点の位が必要以上に表示される。
#
#
# - 調べた単語・関数
#      - pow(x, y)
#         - xのy乗
#             - https://docs.python.org/ja/3.13/library/stdtypes.html
#
#      - math.sqrt(x)
#         - xの平方根を返す
#             - https://docs.python.org/ja/3.13/library/math.html#math.sqrt
#
# - よくわからなかったこと
#      - 整数同士の計算を無理やりformatで成形したが、ほかに方法は？
#
# """

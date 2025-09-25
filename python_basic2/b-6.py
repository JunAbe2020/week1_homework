import random

# サイコロの面の数


def number_of_faces():
    number_of_faces = int(input("サイコロの面の数は?:"))
    if number_of_faces <= 0:
        number_of_faces = 0
        return "0以上の数字を入力して下さい"
    else:
        return number_of_faces

# print(number_of_faces()) # 検証用

# 試行回数


def number_of_trials():
    number_of_trials = int(input("何回振りますか?:"))
    if number_of_trials <= 0:
        number_of_trials = 0
        return "0以上の数字を入力して下さい"
    else:
        return number_of_trials

# print(number_of_trials()) # 検証用


def trials_of_ndice():
    result = []
    number_of_ndice_faces = int(number_of_faces())
    number_of_ndice_trials = int(number_of_trials())
    for dice_trials in range(1, number_of_ndice_trials + 1):
        result.append(random.randint(1, number_of_ndice_faces))
    return result


# print(trials_of_ndice()) # 検証用

# """
# - 要件
#     - N面サイコロをM回振ったときの結果を表示してください
#     - N, M は正の整数とします
#     - N, M はユーザーからの入力を利用すること

# - [ ] N面サイコロをM回振ったときの結果を出力する
#     - [ ] 面の数を入力する
#     - [ ] 試行回数を入力する
#     - [ ] 取得した値をfor文で出力する

# - イメージコード
#     - number_of_faces = int(input(~~~))
#         - 数字を入力する
#         - 試行回数0未満を入力した場合、もう一度入力して下さい

#     - number_of_trials = int(input(~~~))
#         - 同様
#     - resultを定義
#     - for a in #range(試行回数)でいけそう

#     - != result[] = random.randint(:number_of_faces)ではなく
#     -
#     - print(result)

# - 後々気が付いたこと
# 　　- 面の数は0以下、試行回数は0未満を入力されたら成立しない。
#     - 面の数と試行回数の関数はまとめられる
#     - 関数の前にnumber_of_faces,trialsを定義したが必要ない

# - 知らない単語
#     - operand
#       - 式を構成する要素のうち、演算子じゃないほう、被演算子

# - 発生したエラー
#     - TypeError: 'int' object is not callable
#       - trials_of_ndiceでnumber_of_face,trialsという同名の変数を使用していたため
#     - TypeError: unsupported operand type(s) for +: 'function' and 'int'
#       -
# """

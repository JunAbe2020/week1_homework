number_list = input("データを入力してください(スペース区切り) >")


def calc_app():
    integer = ""
    integer_dict = {}
    integer_list = []
    number_list_length = len(number_list) - 1

    for index, number in enumerate(number_list):
        if index == number_list_length:
            integer += number
            integer_dict[index] = integer
        elif not number == " ":
            integer += number
        else:
            integer_dict[index] = integer
            integer = ""

    for key, value in integer_dict.items():
        integer_list.append(int(value))

    return integer_list


# リストの合計値を計算
def sum_value():
    sum_value = 0
    for number in calc_app():
        sum_value += int(number)
    return sum_value

# print(sum_value()) # 検証用


# リストの最大値を計算
def maximum_value():
    maximum_value = 0
    for number in calc_app():
        if maximum_value < number:
            maximum_value = number
    return maximum_value

# print(maximum_value()) # 検証用


# リストの最小値を計算
def minimum_value():
    minimum_value = maximum_value()
    for number in calc_app():
        if minimum_value > number:
            minimum_value = number
    return minimum_value


# リストの平均値を計算
def average_calc():
    result = 0
    result = sum_value() / len(calc_app())
    return round(result, 1)


print(sum_value())
print(maximum_value())
print(minimum_value())
print(average_calc())

# いろいろな桁数の数が出たけれど、最後に入力した数が出ない
# if not number == " ":
#     integer += number
# else:
#     integer_dict[index] = integer
#     integer = ""

# for key, value in integer_dict.items():
#     if not value == " ":
#         integer_list.append(int(value))
#     else:
#         continue
# return integer_list
# for index,number in enumerate(number_list):
#     if index == number_list_length:
#       integer_dict[index] = integer
#     elif not number == " ":
#         integer += number
#     else:
#         integer_dict[index] = integer
#         integer = ""
# return integer_dict

# for index,number in enumerate(number_list):
#     while index == number_list_length - 1:
#         if not number == "":
#             integer += number
#         else:
#             integer_dict[index] = integer
#             integer = ""
# return integer_dict

# for文にwhile文をいれたから回り続けたのだきっと
# def calc_app():
#     integer = ""
#     integer_dict = {}
#     number_list_length = len(number_list)

#     for index,number in enumerate(number_list):
#         while index == number_list_length - 1:
#             if not number == "":
#                 integer += number
#             else:
#                 integer_dict[index] = integer
#                 integer = ""
#     return integer_dict


# for index,number in enumerate(number_list):
#     if not number == " " and index <= number_list_length:

#     elif
#     else:


# #    print(number) # 検証用→ok
#         integer_dict[index] = number
#     # print(integer_dict) # 検証用→ok
# for key, value in integer_dict.items():
#     if value == " ":
#         del integer_dict["key"]
#     else:
#         continue
# return integer_dict

# 最後の入力文字が入らなかったやつ
# def calc_app():
#     integer = ""
#     integer_dict = {}
#     integer_list = []
#     for index,number in enumerate(number_list):
#     #    print(number) # 検証用→ok
#         integer_dict[index] = number
#         # print(integer_dict) # 検証用→ok
#         if not integer_dict[index] == " ": # ""だと無駄と認識され、" "だとスペース
#             integer += integer_dict[index] # integer = ""とリセットする必要あり
#             if index + 1 == "":
#                 integer_list.append(integer)
#             else:
#                 continue
#         else:
#             integer_list.append(integer)
#             integer = ""
#     return integer_list

# やりたいこと
# inputで文字列を受け取る(数字とスペース)。
# スペースを除いた数字でリストを作り直す。
# リストを返す。
# - 辞書からデータを取得してもよいのでは？
#     - 辞書の値が空欄のものを削除する！！
#      - while文で空欄になるまでは繰り返す？
#      - del integer_dict["key"]を使用すると、要素ごと消えてしまう
# - スペースを抜いて辞書を作成したい
# - 元のリストの長さを把握するためにlen関数が使えるのでは？
# - 別に辞書作りとスペースかどうかの判断を分けたっていい
# - len(number_list)値は必ず奇数

# integer = ""：長さ0の文字列を作成
# integer_dict = {}:入力文字を値としてとるために、辞書を作成
# integer_list = []
# for index,number in enumerate(number_list):入力文字を値として取るためにindexも取得
# integer_dict[index] = number:キーをindex,値を入力文字とする辞書へ要素を追加

# if not integer_dict[index] == " "
#     integer += integer_dict[index]
# else:
#     integer_list.append(integer)
#     integer = ""
# - 入力文字がスペースかどうか確認。
#     - スペースじゃなかったらinteger(長さ0の文字列)に追加
# - スペースだったら
#     - integerをリストの要素として追加
#     - integerをリセット

# return integer_list:calc_upのリストを返す。

# calc_app()
# print(calc_app())

# 0になったやつ
# inputで入力した文字列は、スペースも文字として扱われる
# def calc_app():
#     integer = ""
#     integer_number_list = []
#     for number in number_list:
#         if not number == "":
#             integer += number
#         else:
#             integer_number_list.append(integer)
#     return integer_number_list

# - リスト→辞書型
#     - indexも取得し、値にすれば空欄かどうか判別できるのでは？
# -integer_dictを追加

# continue
# if not integer_dict[index] == "":
#     integer += integer_dict[index]
# else:
#     integer_list.append(int(integer))

# - print(calc_upp())で空欄もリストに挿入される
# - ""だと無だと認識され、" "だとスペース

# - integer_listのindex[1]から入力していない数が出力される
# - integer = ""とリセットする必要あり

# - なぜか3つ目の数がリストへ入力されていない
#     - 3つ目ではなく、最後に入力した数が認識されていない
#     - if文が以下のため、最後の数がinteger_listへ入力されない。
#     - if not integer_dict[index] == " ":
#     -     integer += integer_dict[index]
#     - 上記のif文に加えて、以下のようにおいたが、最終入力文字は表示されていない
#     - if index == "":
#         - integer_list.append(integer)
#     - else:
#         - continue
#     - indexは要素番号だからオブジェクトとして認識されないのでは？
# intはstrに対して使用できない

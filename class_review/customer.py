# Customerクラスの定義

class Customer:

    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age <= 3:
            return 0
        elif 3 < self.age < 20:
            return 1000
        elif 20 <= self.age < 65:
            return 1500
        elif 65 <= self.age < 75:
            return 1200
        else:
            return 500

    def person_info(self):
        person_info = []
        person_info.append(self.full_name())
        person_info.append(str(self.age))
        person_info.append(str(self.entry_fee()))
        return person_info

    # print(ken.person_info()) #検証用

    def info_csv(self):
        return ",".join(self.person_info())

        # return f"{self.full_name()},{self.age},{self.entry_fee()}"
        # return ",".join(self.person_info())

    def info_tsv(self):
        return "\t".join(self.person_info())

        # と思いましたが、試行錯誤のAI使わず関数になりました！
        # ここだけ全く分からずchatgpt使いました！すみません！
        # Format each item and then join
        # formatted_info = [f"{item:<10}" for item in self.person_info()]
        # return "\t".join(formatted_info)

    def info_pipe(self):
        return "|".join(self.person_info())
        # return f"{self.full_name()}|{self.age}|{self.entry_fee()}"


# Customerクラスのインスタンス化
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

# C-1. フルネームを取得できる

print("C-1. フルネームを取得できる")
print(ken.full_name())
print(tom.full_name())
print(ieyasu.full_name())
print("")

# C-2. 年齢という概念の追加

print("C-2. 年齢という概念の追加")
print(ken.age)
print(tom.age)
print(ieyasu.age)
print("")

# C-3. 年齢に応じた適切な入場料(entry_fee)を計算できる

print("C-3. 年齢に応じた適切な入場料(entry_fee)を計算できる")
print(ken.entry_fee())
print(tom.entry_fee())
print(ieyasu.entry_fee()) 
print("")

# C-4. 単一の顧客情報をCSV形式で取得できる

print("C-4. 単一の顧客情報をCSV形式で取得できる")
print(ken.info_csv())
print(tom.info_csv())
print(ieyasu.info_csv())
print("")

# C-5. 3歳以下の入場料金の無料化

print("C-5. 3歳以下の入場料金の無料化")
print(ken.entry_fee())
print(tom.entry_fee())
print(ieyasu.entry_fee())
print(michelle.entry_fee())
print("")

# C-7. 単一顧客の情報取得形式の追加その1

print("C-7. 単一顧客の情報取得形式の追加その1")
print(ken.info_tsv())
print(tom.info_tsv())
print(ieyasu.info_tsv())
print(michelle.info_tsv())
print("")

# C-8. 単一顧客の情報取得形式の追加その2

print("C-8. 単一顧客の情報取得形式の追加その2")
print(ken.info_pipe())
print(tom.info_pipe())
print(ieyasu.info_pipe())
print(michelle.info_pipe())
print("")

# """
#
# - 要件
#     - 以下の結果を出力
#         - print(ken.full_name())  # "Ken Tanaka" という値を出力
#         - print(tom.full_name())  # "Tom Ford" という値を出力
#         - print(ieyasu.full_name())  # "Ieyasu Tokugawa" という値を出力
#
# - [ ] インスタンスからCustomerクラスのfull_nameメソッドを使い値を出力する
#     - [ ] Customerクラスにfull_nameメソッドを追加
#     - [ ] 呼び出す
#
# - イメージコード
#     - class Customer:
#         - def full_name(self):
#             - print(f"{self.first name} {self.family_name})
#
# - 後々気が付いたこと
#     - __init__でインスタンスを作成していなかった。 C-1
#     -
# - 知らない単語
#      - リテラル
#        - 値そのものをソースコードに直接書いたもの
# - 発生したエラー
#      - """ ~ """まで出力された
#        - 複数行文字列リテラルのため、文頭ではなく文末に配置すると出力される可能性。#で対応
#
# """

# """
#
# - 要件
#     - 以下の結果を出力
#         - print(ken.age)  # 15 という値を出力
#         - print(tom.age) # 57 という値を出力
#         - print(ieyasu.age) # 75 という値を出力
#
# - [ ] インスタンスからCustomerクラスのageメソッドを呼び、値を出力する
#     - [ ] Customerクラスにageメソッドを追加
#     - [ ] 呼び出す
#
# - イメージコード
#     - class Customer:
#         - def age(self):
#             - return self.age
#
# """

# """
#
# - 要件
#  - 料金の計算ルール
#      - こども料金(20歳未満): 1000円
#      - おとな料金(20歳以上65歳未満): 1500円
#      - シニア料金(65歳以上): 1200円
#      - 以下の結果を出力
#          - print(ken.entry_fee())  # 1000 という値を出力
#          - print(tom.entry_fee())  # 1500 という値を出力
#          - print(ieyasu.entry_fee())  # 1200 という値を出力
#
# - [ ] インスタンスからCustomerクラスのentry_feeメソッドを呼び出し値を出力する
#     - [ ] self.age < 20, 65  <= self.ageで場合分け
#         - 区切りの年齢:値段で辞書を作る？ 3,20,65,
#         -辞書だと、以上、以下、未満、より大きい等の表現が難しそう
#         - [ ] dice{3:0, 20:1000, 65:1200}
#     - 3,20,65を基準にif文を作成
#
# - イメージコード
#     - class Customer:
#         - def entry_fee(self):
#              - if 20歳未満:
#              -   ef = 1000
#              - elif 65歳以上:
#              -   ef = 1200
#              - else:
#              -   ef = 1500
#              - return ef
#
# - 発生したエラー
#      - TypeError: Customer.entry_fee() missing 1 required positional argument: 'age'
#         - self.age = ageとなっているため、entry_fee(age)を取らなくてよい
# """

# """
#
# - 要件
#     - 以下の結果を出力
#         - print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
#         - print(tom.info_csv())  # "Tom Ford,57,1500" という値を出力
#         - print(ieyasu.info_csv())  # "Ieyasu Tokugawa,75,1200" という値を出力
#
# - [ ] インスタンスからCustomerクラスのinfo_csvメソッドを呼び、値を出力する
#     - [ ] 作成済みのクラスメソッドを使用
#     - [ ] 呼び出す
#
# - イメージコード
#     - class Customer:
#         - def info_csv(self):
#             - return f""{self.name},{self.age},{self.entry_fee()}""
#
# """

# """
#
# - 要件
#     - 以下のコードを追加
#         - + michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)
#     - 以下の結果を出力
#         - print(ken.entry_fee())  # 1000 という値を出力
#         - print(tom.entry_fee())  # 1500 という値を出力
#         - print(ieyasu.entry_fee())  # 1200 という値を出力
#         - print(michelle.entry_fee())  # 0 という値を出力
#
# - [ ] インスタンスからCustomerクラスのentry_feeメソッドを呼び、値を出力する
#     - [ ] <= 3 : 0, 3 < 20 :1000, 20 < 65 :1500, 65 <= 1200
#         - 区切りの年齢:値段で辞書を作る？ 3,20,65,
#         -辞書だと、以上、以下、未満、より大きい等の表現が難しそう
#         - [ ] dice{3:0, 20:1000, 65:1200}
#     - 3,20,65を基準にif文を作成
#
# - イメージコード
#     - class Customer:
#         - def entry_fee(self):
#             -if文に3歳未満の情報を追加
#             - return f""{self.name},{self.age},{self.entry_fee()}""
#
# """

# C-6. 75歳以上の料金区分の追加

# """
#
# - 要件
#     - 以下のコードを追加
#         - else:で75歳以上の入場料を定義
#
# - [ ] else: return 500
#
# """

# """
#
# - 要件
#     - 単一顧客の情報取得をタブ区切りにも対応させてください
#     - 下記は出力の例
#         - Ken Tanaka      15      1000
#         - Tom Ford        57      1500
#         - Ieyasu Tokugawa 75      500
#         - Michelle Tanner 3       0
#
# - [ ] 2つの要素をタブ区切りで出力する
#     - [ ] タブ区切りとは？　タブで区切るとデータの先頭
#         - 関数をタブに入れてみたがそろわなかった
#
# - イメージコード
#     - class Customer:
#         - def tab(self):
#             - tab
#
# - よくわからなかったところ
#         - formatted_info = [f"{item:<10}" for item in self.person_info()]
#             - formatted_infoにperson_info()からitemを取り出してmax10文字として代入している？
#                 - "Max10:self.full_name() Max10:self.age Max10:self.entry_fee()"
#         - return "\t".join(formatted_info)
#
# """

# """
#
# - 要件
#     - 単一顧客の情報取得を「|」(パイプ)区切りにも対応させてください
#     - 下記は出力の例
#         - Ken Tanaka|15|1000
#         - Tom Ford|57|1500
#         - Ieyasu Tokugawa|75|500
#         - Michelle Tanner|3|0
#
# - [ ] 2つの要素をパイプで区切りで出力する
#     - [ ] "|".joinでつなげればいけそう
#
# - イメージコード
#     - class Customer:
#         - def info_pipe(self):
#             -info_pipe = [for item in self.person_info()]
#             -return "\|".join(info_pipe)
#
# """

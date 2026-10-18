# number1 は「1つ目の数」という意味の変数
# number1 に「1つ目の数字を入力してください: 」と表示して入力された文字列を入れる
number1 = input("1つ目の数字を入力してください: ")
# number2 は「2つ目の数」という意味の変数
# number2 に「2つ目の数字を入力してください: 」と表示して入力された文字列を入れる
number2 = input("2つ目の数字を入力してください: ")

# number1 の文字列を整数に変換し、number1 に入れ直す
number1 = int(number1)
# number2 の文字列を整数に変換し、number2 に入れ直す
number2 = int(number2)

# answer は「答え」という意味の変数
# answer に number1 と number2 を足した値を入れる
answer = number1 + number2

# 「答えは」と answer の値と「です」を、間に空白を入れてターミナルに表示する
print("答えは", answer, "です")

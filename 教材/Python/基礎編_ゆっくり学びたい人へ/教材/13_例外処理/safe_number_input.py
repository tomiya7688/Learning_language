# 入力された文字を text に保存します。
text = input("数字を入力してください: ")

try:
    # textを整数へ変換できたら、その整数を number に保存します。
    number = int(text)
except ValueError:
    print("数字を入力してください")
else:
    print("2倍すると", number * 2, "です")

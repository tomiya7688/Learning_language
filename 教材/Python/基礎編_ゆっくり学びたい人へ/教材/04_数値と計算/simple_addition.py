# 1つ目の入力を文字列として受け取り、first_text という名前を付ける
first_text = input("1つ目の金額を入力してください: ")
# 2つ目の入力を文字列として受け取り、second_text という名前を付ける
second_text = input("2つ目の金額を入力してください: ")

# 入力された文字列を整数に変換し、計算に使う名前を付ける
first_price = int(first_text)
second_price = int(second_text)

# 2つの金額を足し、合計に total という名前を付ける
total = first_price + second_price

# ターミナルに合計金額を表示する
print("合計は", total, "円です")

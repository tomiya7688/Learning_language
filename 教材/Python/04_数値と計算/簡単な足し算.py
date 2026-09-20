# input() で入力した内容は、最初は文字列として受け取ります。
# int() を使って、整数として計算できる形に変換します。
number1 = int(input("1つ目の数字を入力してください: "))
number2 = int(input("2つ目の数字を入力してください: "))

# + を使って2つの整数を足します。
answer = number1 + number2

# 計算結果を表示します。
print("答えは", answer, "です")

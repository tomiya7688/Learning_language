text = input("数字を入力してください: ")

try:
    number = int(text)
except ValueError:
    print("数字を入力してください")
else:
    print("2倍すると", number * 2, "です")

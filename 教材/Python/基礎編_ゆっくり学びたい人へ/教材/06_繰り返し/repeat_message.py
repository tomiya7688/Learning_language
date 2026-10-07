# Pythonは、利用者が入力した表示回数を整数に変換し、変数 count に保存します。
count = int(input("何回表示しますか: "))

# range(count) は、0から count - 1 までの整数を for 文へ順番に渡します。
for i in range(count):
    # Pythonは、i + 1 を計算して、表示番号を1回目から始めます。
    print(f"{i + 1}回目です")

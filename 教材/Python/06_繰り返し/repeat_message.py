# 入力を受け取り、int() で整数に変換して表示回数を count に保存します。
count = int(input("何回表示しますか: "))

# range(count) で、0 から count - 1 まで順番に値を作ります。
for i in range(count):
    # i は 0 から始まるので、表示するときは 1 を足します。
    print(f"{i + 1}回目です")

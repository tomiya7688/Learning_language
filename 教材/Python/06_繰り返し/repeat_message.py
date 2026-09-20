# 何回表示するかを入力します。
count = int(input("何回表示しますか: "))

# range(count) で、0 から count - 1 まで順番に値を作ります。
for i in range(count):
    # i は 0 から始まるので、表示するときは 1 を足します。
    print(f"{i + 1}回目です")

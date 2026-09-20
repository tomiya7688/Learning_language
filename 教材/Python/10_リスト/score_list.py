scores = [80, 90, 70]

# 新しい点数を追加します。
scores.append(100)

# 最初の要素を表示します。
print("最初の点数:", scores[0])

# 要素の数を表示します。
print("件数:", len(scores))

# 合計を入れる変数です。
total = 0

# リストの点数を1つずつ取り出します。
for score in scores:
    print(score)
    total = total + score

print("合計:", total)

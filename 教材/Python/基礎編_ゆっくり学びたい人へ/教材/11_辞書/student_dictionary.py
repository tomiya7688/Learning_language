# 生徒1人分の名前と点数を student にまとめます。
student = {
    "name": "たろう",
    "score": 80
}

print("名前:", student["name"])
print("点数:", student["score"])

# 新しい情報を追加します。
student["class"] = "A"

# 既存の情報を更新します。
student["score"] = 90

print("更新後の点数:", student["score"])

# キーを key、対応する値を value に入れながら順番に表示します。
for key, value in student.items():
    print(key, ":", value)

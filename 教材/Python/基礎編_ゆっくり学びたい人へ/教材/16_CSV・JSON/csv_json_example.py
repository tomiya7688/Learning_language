import csv
import json

print("CSV:")

with open("students.csv", "r", encoding="utf-8") as file:
    # CSVを1行ずつ辞書として扱う reader を作ります。
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], int(row["score"]))

print("JSON:")

with open("students.json", "r", encoding="utf-8") as file:
    # JSONから読み込んだ生徒一覧を students に保存します。
    students = json.load(file)

for student in students:
    print(student["name"], student["score"])

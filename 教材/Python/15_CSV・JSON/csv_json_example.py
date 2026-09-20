import csv
import json

print("CSV:")

with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], int(row["score"]))

print("JSON:")

with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

for student in students:
    print(student["name"], student["score"])

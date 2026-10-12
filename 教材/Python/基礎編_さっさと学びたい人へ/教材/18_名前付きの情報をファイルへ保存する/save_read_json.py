# JSONを読み書きするための json の処理を使えるようにする
import json

# student は「生徒」という意味
# student に名前が「たろう」、点数が80の情報を入れる
student = {"名前": "たろう", "点数": 80}

# file は「ファイル」という意味
# purpose_student.json をUTF-8で書き込み用に開き、file という名前で使う
with open("purpose_student.json", "w", encoding="utf-8") as file:
    # student を日本語をそのまま残し空白2つで段をそろえたJSONとして file へ書き込む
    json.dump(student, file, ensure_ascii=False, indent=2)

# purpose_student.json をUTF-8で読み込み用に開き、file という名前で使う
with open("purpose_student.json", "r", encoding="utf-8") as file:
    # loaded_student は「読み込んだ生徒」という意味
    # loaded_student に file からJSONを読み込んで入れる
    loaded_student = json.load(file)

# loaded_student の「名前」と「点数」を表示する
print(loaded_student["名前"], loaded_student["点数"])

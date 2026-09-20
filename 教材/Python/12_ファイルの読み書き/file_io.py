file_name = "message.txt"

# ファイルへ文字を書き込みます。
with open(file_name, "w", encoding="utf-8") as file:
    file.write("こんにちは\n")
    file.write("Pythonを勉強中です\n")

print("保存しました")

# 保存した内容を読み込みます。
with open(file_name, "r", encoding="utf-8") as file:
    text = file.read()

print("読み込んだ内容:")
print(text)

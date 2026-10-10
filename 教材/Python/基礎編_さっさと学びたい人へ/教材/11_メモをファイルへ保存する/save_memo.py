# file は「ファイル」という意味
# purpose_memo.txt をUTF-8で書き込み用に開き、file という名前で使う
with open("purpose_memo.txt", "w", encoding="utf-8") as file:
    # file が表すファイルへ「こんにちは」と改行を書き込む
    file.write("こんにちは\n")

# 「purpose_memo.txt に保存しました」と表示する
print("purpose_memo.txt に保存しました")

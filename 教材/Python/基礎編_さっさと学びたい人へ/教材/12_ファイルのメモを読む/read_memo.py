# file は「ファイル」という意味
# purpose_memo.txt をUTF-8で読み込み用に開き、file という名前で使う
with open("purpose_memo.txt", "r", encoding="utf-8") as file:
    # text は「文章」という意味
    # text に file が表すファイルの内容をすべて読み込んで入れる
    text = file.read()

# text を表示し、表示のあとに改行を追加しない
print(text, end="")

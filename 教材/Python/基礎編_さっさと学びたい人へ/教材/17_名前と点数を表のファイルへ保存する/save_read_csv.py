# CSVを読み書きするための csv の処理を使えるようにする
import csv

# rows は「複数の行」という意味
# rows に見出しの行と、たろうの80点を表す行をまとめた一覧を入れる
rows = [["名前", "点数"], ["たろう", 80]]

# file は「ファイル」という意味
# purpose_scores.csv をUTF-8で書き込み用に開き、file という名前で使う
with open("purpose_scores.csv", "w", encoding="utf-8", newline="") as file:
    # writer は「書き込むもの」という意味
    # writer に file へCSVの行を書くためのものを入れる
    writer = csv.writer(file)
    # writer を使い、rows の各行を file へ書き込む
    writer.writerows(rows)

# purpose_scores.csv をUTF-8で読み込み用に開き、file という名前で使う
with open("purpose_scores.csv", "r", encoding="utf-8", newline="") as file:
    # reader は「読み込むもの」という意味
    # reader に file からCSVの行を読むためのものを入れる
    reader = csv.reader(file)
    # row は「1行」という意味
    # row に reader から読んだ行を1つずつ入れ、下の行を実行する
    for row in reader:
        # row の1列目と2列目を表示する
        print(row[0], row[1])

# 16. CSV・JSON

この章では、**複数のデータをファイルへ保存するときによく使うCSVとJSON**を学びます。

今回作るのは、

- CSVファイルから名前と点数を読み込む
- JSONファイルから同じようなデータを読み込む

という小さなプログラムです。

---

## 16-1. なぜCSVやJSONが必要なの？

12章では、普通のテキストファイルを読み書きしました。

でも、たとえば、

```text
たろう 80
さくら 95
けん 70
```

だけでは、

> **「どこからどこまでが何のデータやねん！」**

という決まりが曖昧です。

データをたくさん扱うなら、

> **どんな形で保存するか**

を決めておいた方が便利です。

そこでよく使われるのが **CSV** や **JSON** です。

---

## 16-2. CSVとは

CSVは、値をカンマで区切って並べる形式です。

たとえば、

```text
name,score
たろう,80
さくら,95
けん,70
```

のように書きます。

CSVは、

> 表のようなデータを保存したい

ときによく使われます。

---

## 16-3. CSVは表として見ると分かりやすい

先ほどのCSVは、表にすると、

| name | score |
| --- | ---: |
| たろう | 80 |
| さくら | 95 |
| けん | 70 |

のようになります。

Excelや表計算ソフトでも扱いやすい形式です。

---

## 16-4. CSVを読み込む

[csv_json_example.py](./csv_json_example.py) を開いてください。

`csv` はCSV、`json` はJSON、`example` は「例」という意味です。

まずCSVを読みます。

```python
import csv

with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["score"])
```

---

## 16-5. `import csv`

```python
import csv
```

は、

> CSVを扱うための機能のまとまりを使えるようにする

という意味です。

14章で学んだ `import` と同じです。

`csv` は標準ライブラリなので、pipで追加する必要はありません。

---

## 16-6. `csv.DictReader()`

```python
reader = csv.DictReader(file)
```

は、CSVの1行ずつを辞書のように扱いやすくしてくれます。

たとえば、

```text
たろう,80
```

という行を、

```python
{
    "name": "たろう",
    "score": "80"
}
```

のような形で扱えます。

つまり、11章で学んだ辞書へつながっています。

---

## 16-7. CSVから読んだ数字は文字列

CSVから読み込んだ `"80"` は、数字ではなく文字列です。

そのため計算したいなら、

```python
score = int(row["score"])
```

のように変換します。

---

## 16-8. CSVの合計を出してみる

たとえば、

```python
total = 0

with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total = total + int(row["score"])

print("合計:", total)
```

とすれば点数の合計を出せます。

---

## 16-9. JSONとは

JSONは、名前付きのデータや配列を表すのが得意な形式です。

たとえば、

```json
[
  {
    "name": "たろう",
    "score": 80
  },
  {
    "name": "さくら",
    "score": 95
  }
]
```

のように書きます。

見た目がPythonのリストや辞書にかなり似ています。

---

## 16-10. JSONとリスト・辞書の関係

Pythonでは、

```python
students = [
    {"name": "たろう", "score": 80},
    {"name": "さくら", "score": 95}
]
```

と書けます。

JSONもかなり似ています。

そのためJSONを読むと、

> リストや辞書として扱える

という感覚で理解できます。

---

## 16-11. JSONを読み込む

```python
import json

with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

for student in students:
    print(student["name"], student["score"])
```

これでJSONファイルの内容をPythonのデータとして読み込めます。

---

## 16-12. `json.load()`

```python
students = json.load(file)
```

は、

> JSONファイルを読み込んで、Pythonで使える形へ変換する

という処理です。

今回のJSONなら、`students` にはリストが入り、その中に辞書が入ります。

---

## 16-13. 今回のサンプルコード

```python
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
```

CSVとJSONを同じプログラムで読み比べます。

---

## 16-14. CSVとJSONは何が違う？

大まかには、

```text
CSV
→ 表のようなデータが得意

JSON
→ 名前付きデータや入れ子構造が得意
```

です。

たとえば、

```text
名前,点数,クラス
```

のような単純な一覧ならCSVは分かりやすいです。

一方、

```text
生徒
├─ 名前
├─ 点数
└─ 所属
    ├─ 学年
    └─ クラス
```

のような複雑な構造ではJSONの方が扱いやすいことがあります。

---

## 16-15. JSONはWeb APIでもよく使う

次の17章で扱うWeb APIでは、JSONがよく使われます。

たとえば外部サービスから、

```json
{
  "name": "Tokyo",
  "temperature": 25
}
```

のようなデータが返ってくることがあります。

つまり、この章のJSONは17章のWeb APIへそのままつながります。

---

## 16-16. CSVやJSONもただのファイル

特別なものに見えますが、どちらもファイルです。

そのため、

```python
with open(...)
```

という12章の考え方がそのまま使えます。

違うのは、

> 中身の書き方にルールがある

という点です。

---

## 16-17. 文字コードはUTF-8

この教材では、CSVもJSONも基本的にUTF-8を使います。

```python
encoding="utf-8"
```

を付けて読み込みます。

日本語を扱う場合、文字コードが違うと文字化けすることがあります。

---

## 16-18. ファイルが見つからなければ例外になる

たとえば、

```python
with open("students.csv", "r", encoding="utf-8") as file:
```

で `students.csv` が無ければ、`FileNotFoundError` が起きます。

13章の例外処理を使えば、この場合の対応もできます。

---

## 16-19. 実行方法

`csv_json_example.py`、`students.csv`、`students.json` を同じフォルダに置きます。

Windows:

```text
python csv_json_example.py
```

macOS / Linux:

```text
python3 csv_json_example.py
```

実行結果:

```text
CSV:
たろう 80
さくら 95
けん 70
JSON:
たろう 80
さくら 95
けん 70
```

のように表示されます。

---

## 16-20. 自分で変えてみる

`students.csv` に、

```text
みさき,88
```

を追加してみてください。

JSONにも、

```json
{
  "name": "みさき",
  "score": 88
}
```

を追加してみます。

Pythonコードを変えなくても、読み込むデータが増えることを確認できます。

---

## 16-21. 次はWeb API

ここまでは、自分のPCにあるCSVやJSONを読みました。

次は、

> インターネット上にあるデータをPythonから取得する

ために **[17章「Web APIからデータを取得」](../17_Web_APIからデータを取得/Web_APIからデータを取得.md)** へ進みます。

---

## 16-22. ここまでで覚えること

この章では、次のことが分かれば十分です。

1. CSVはカンマ区切りで表のようなデータを保存できる
2. `csv` はCSVを扱う標準ライブラリ
3. `csv.DictReader()` で1行を辞書のように扱える
4. CSVから読んだ値は基本的に文字列
5. JSONはリストや辞書に似た構造を表せる
6. `json` はJSONを扱う標準ライブラリ
7. `json.load()` でJSONファイルをPythonのデータへ変換できる
8. CSVは表形式、JSONは名前付き・階層的なデータに向いている
9. JSONはWeb APIでもよく使われる

---

## 前後のページ

← [15. 標準ライブラリ・外部ライブラリ・pip](../15_標準ライブラリ・外部ライブラリ・pip/標準ライブラリ・外部ライブラリ・pip.md)

[17. Web APIからデータを取得](../17_Web_APIからデータを取得/Web_APIからデータを取得.md) →

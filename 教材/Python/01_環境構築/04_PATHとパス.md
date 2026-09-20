# 1-4. PATH・パス・ディレクトリ

環境構築で特につまずきやすいのが **PATH** と **パス** です。

## PATH とは

PATH は、`python` や `code` のようなコマンドを入力したときに、
OS が実行ファイルを探す場所の一覧です。

たとえば Python が次にあるとします。

```text
C:\Users\ユーザー名\AppData\Local\Programs\Python\Python314\python.exe
```

PATH に追加するのは通常 `python.exe` 自体ではなく、その入っているフォルダです。

```text
C:\Users\ユーザー名\AppData\Local\Programs\Python\Python314\
```

さらに `pip` などを使うため、次のような `Scripts` フォルダも関係します。

```text
C:\Users\ユーザー名\AppData\Local\Programs\Python\Python314\Scripts\
```

要するに、

> PATH には、実行したいプログラムが入っているフォルダまでを書く

と覚えてください。

---

## Python の場所を確認する

Windows:

```powershell
where python
```

macOS / Linux:

```bash
which python3
```

---

## PATH を変えたのに反映されない

PATH を変更したあと、すでに開いていたターミナルには反映されないことがあります。

1. ターミナルを閉じる
2. 新しく開く
3. もう一度コマンドを試す

で確認してください。

---

## パスとは

**パス** はファイルやフォルダの場所を表します。

Windows:

```text
C:\Users\sample\Documents\hello.py
```

macOS / Linux:

```text
/home/sample/hello.py
```

PATH 環境変数と普通の「パス」は別のものです。

---

## カレントディレクトリ

ターミナルが現在基準にしているフォルダを **カレントディレクトリ** と呼びます。

現在地を確認:

```text
pwd
```

中身を見る:

Windows:

```powershell
dir
```

macOS / Linux:

```bash
ls
```

移動:

```text
cd フォルダ名
```

1つ上へ戻る:

```text
cd ..
```

---

## 絶対パスと相対パス

絶対パスは、場所を先頭から全部書いたものです。

```text
C:\Users\sample\Documents\Python\hello.py
```

相対パスは、現在地を基準にした書き方です。

現在のフォルダに `hello.py` があるなら、

```text
hello.py
```

だけで指定できます。

`python hello.py` でファイルが見つからない場合は、
Pythonではなく **今いるフォルダが違う** 可能性も確認してください。

---

## ユーザー環境変数とシステム環境変数

Windows の PATH には主に、

- ユーザー環境変数
- システム環境変数

があります。

個人で Python を学ぶだけなら、通常は **ユーザー環境変数の PATH** で十分です。

システム環境変数は PC 全体へ影響するため、
意味が分からない状態で無理に変更する必要はありません。

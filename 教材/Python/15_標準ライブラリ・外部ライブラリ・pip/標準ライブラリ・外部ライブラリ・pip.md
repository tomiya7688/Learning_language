# 15. 標準ライブラリ・外部ライブラリ・pip

14章では、自分で作った `message_tools.py` を `import` しました。

この章では、**Pythonが最初から用意しているモジュール**と、**あとから追加するライブラリ**を使います。

この章の本質はこれです。

> **一々全部書いてたら日が暮れてしまうわ！**

乱数、日付、CSV、JSON、HTTP通信、表計算、画像処理……。

全部を毎回自分でゼロから書いていたら、肝心の作りたいものにたどり着く前に日が暮れます。

だから、すでに誰かがまとめてくれた機能を使います。

---

## 15-1. なぜ標準ライブラリが必要なの？

たとえば「1から10までのランダムな数字が欲しい」とします。

乱数を作る仕組みそのものから全部自分で実装することも、不可能ではありません。

でも、

> **「いや、一々そこから書いてたら日が暮れてしまうわ！」**

となります。

そこでPythonには、よく使う機能が最初からまとめて用意されています。

これが **標準ライブラリ** です。

Pythonには、最初から便利な機能がたくさん用意されています。

たとえば `random`、`math`、`datetime`、`csv`、`json` などです。

こうした、Pythonに最初から用意されている機能の集まりを **標準ライブラリ** と呼びます。

---

## 15-2. 標準ライブラリも `import` は同じ

14章では、

```python
import message_tools
```

と書きました。

標準ライブラリも同じです。

```python
import random
```

と書けば、`random` というまとまりを使えるようになります。

---

## 15-3. `random` を使ってみる

[standard_library_example.py](./standard_library_example.py) を開いてください。

```python
import random

number = random.randint(1, 10)

print("1から10のランダムな数字:", number)
```

実行するたびに違う数字が出ることがあります。

---

## 15-4. 自作モジュールとの違い

```text
message_tools
→ 自分で作ったモジュール

random
→ Pythonが最初から用意しているモジュール
```

でも、どちらも `import` して使う点は同じです。

---

## 15-5. 標準ライブラリはpip不要

`random` はPythonに最初から入っているので、

```text
python -m pip install random
```

は必要ありません。

そのまま `import random` で使えます。

---

## 15-6. 外部ライブラリとは

標準ライブラリだけで世の中の全部を用意することもできません。

たとえば、

- 高度な表計算
- 機械学習
- ゲーム制作
- ブラウザ画面
- HTTP通信

までPython本体に全部抱え込ませたら、今度はPython本体がとんでもないことになります。

そこで、

> **「必要なやつだけ後から持ってくればええやん！」**

という考え方になります。

Python本体とは別に配布されている便利なライブラリもあります。

たとえば requests、pandas、numpy、pygame、streamlit などです。

これらは、多くの場合、先にインストールする必要があります。

---

## 15-7. `pip` とは

外部ライブラリをインストールするときによく使うのが `pip` です。

たとえば requests を入れるなら、

Windows:

```text
python -m pip install requests
```

macOS / Linux:

```text
python3 -m pip install requests
```

と入力します。

これはPythonコードではなく、**ターミナルへ入力するコマンド**です。

---

## 15-8. なぜ `python -m pip`？

`pip install requests` と書く方法もあります。

ただしPCにPythonが複数あると、

> 「そのpip、どのPythonのpip？」

という問題が起こります。

そのため、この教材では `python -m pip` を基本にします。

---

## 15-9. 入れたのに見つからない

よくあるのが、

```text
ModuleNotFoundError: No module named 'requests'
```

です。

原因の1つは、ライブラリを入れたPythonと、プログラムを実行したPythonが違うことです。

---

## 15-10. Pythonは複数あることがある

1台のPCに Python 3.10、Python 3.12、仮想環境のPython など、複数のPythonが存在することがあります。

そのため、

> **インストールに使うPythonと、実行に使うPythonをそろえる**

ことが大切です。

---

## 15-11. バージョンを確認する

Windows:

```text
python --version
python -m pip --version
```

macOS / Linux:

```text
python3 --version
python3 -m pip --version
```

で確認できます。

---

## 15-12. 仮想環境とは

プロジェクトごとに必要なライブラリが違う場合、全部を同じ場所へ入れると管理しにくくなります。

そこで **仮想環境** を使います。

仮想環境を使うと、このプロジェクト専用のPython環境を作れます。

---

## 15-13. 仮想環境を作る

Windows:

```text
python -m venv .venv
```

macOS / Linux:

```text
python3 -m venv .venv
```

---

## 15-14. 仮想環境を有効化する

Windows:

```text
.venv\Scripts\activate
```

macOS / Linux:

```text
source .venv/bin/activate
```

有効になると `(.venv)` のような表示が出ることがあります。

詳しくは、環境構築の **[仮想環境 venv](../01_環境構築/05_仮想環境.md)** も参照してください。

---

## 15-15. 仮想環境の中でpipを使う

仮想環境を有効にしたあと、

```text
python -m pip install requests
```

とすれば、その仮想環境へインストールされます。

---

## 15-16. 仮想環境を終了する

```text
deactivate
```

で抜けられます。

---

## 15-17. `pip` と `import` は違う

```text
pip
→ 外部ライブラリをPython環境へ入れる

import
→ 使える状態のモジュールをプログラムから読み込む
```

です。

---

## 15-18. 次はCSV・JSON

標準ライブラリの中には、CSVやJSONを扱うための `csv`、`json` もあります。

次は **[16章「CSV・JSON」](../16_CSV・JSON/CSV・JSON.md)** で実際に使います。

---

## 15-19. ここまでで覚えること

1. 標準ライブラリはPythonに最初から用意されている
2. 標準ライブラリも `import` して使う
3. 標準ライブラリは基本的にpip不要
4. 外部ライブラリは別途インストールが必要な場合がある
5. `pip` は外部ライブラリを入れるために使う
6. `python -m pip` を使うとPythonとの対応が分かりやすい
7. インストールしたPythonと実行するPythonをそろえる
8. 仮想環境でプロジェクトごとにライブラリを分けられる

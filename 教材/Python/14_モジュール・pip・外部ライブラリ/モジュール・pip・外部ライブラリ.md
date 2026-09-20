# 14. モジュール・pip・外部ライブラリ

この章では、**Pythonに用意されている機能のまとまりや、あとから追加した機能を使う方法**を学びます。

今回作るのは、Pythonに最初から用意されている `random` を使って、ランダムな数字を表示する小さなプログラムです。

---

## 14-1. なぜモジュールが必要なの？

ここまで、自分で変数や関数、クラスを書いてきました。

でも、毎回すべてを自分で作る必要はありません。

たとえば、

- ランダムな数字を作る
- 日付を扱う
- ファイルやフォルダを操作する
- 数学の計算をする
- Webへアクセスする

といった機能は、すでに用意されているものを使える場合があります。

> 「便利な機能あるのに全部自分で作るの？」

となります。

そこで使うのが **モジュールやライブラリ** です。

---

## 14-2. モジュールは機能のまとまり

最初は難しく考えなくて大丈夫です。

> **モジュール = 関係する機能をまとめたもの**

くらいで構いません。

たとえば `random` には、ランダムな値を扱う機能がまとまっています。

```text
random
├─ ランダムな整数を作る
├─ リストからランダムに選ぶ
└─ 順番をランダムに並べ替える
```

というイメージです。

---

## 14-3. `import` でそのまとまりを使えるようにする

```python
import random
```

と書くと、

> `random` という機能のまとまりを、このプログラムで使えるようにする

という意味になります。

Tkinterで、

```python
import tkinter
```

と書いたのと同じ考え方です。

---

## 14-4. 今回作るもの

[module_example.py](./module_example.py) を開いてください。

`module` は「モジュール」、`example` は「例」という意味です。

```python
import random

number = random.randint(1, 10)

print("1から10のランダムな数字:", number)
```

実行するたびに、

```text
1から10のランダムな数字: 7
```

のように違う数字が出ることがあります。

---

## 14-5. `random.randint()` の `.`

```python
random.randint(1, 10)
```

は、

> `random` というまとまりの中にある `randint` を使う

という意味です。

```text
random . randint(1, 10)
   ↑          ↑
まとまり   その中の機能
```

です。

ここでも、

> `A.B` は「Aの中にあるBを使う」

という考え方がそのまま使えます。

---

## 14-6. 標準ライブラリとは

`random` は、Pythonに最初から用意されている機能です。

こうした機能のまとまりを **標準ライブラリ** と呼びます。

たとえば、

- `random`
- `math`
- `datetime`
- `json`
- `csv`

などがあります。

標準ライブラリは、基本的に追加インストールなしで使えます。

---

## 14-7. 外部ライブラリとは

Pythonには、Python本体とは別に配布されている便利なライブラリもあります。

これを **外部ライブラリ** と呼びます。

たとえば、

- requests
- pandas
- numpy
- pygame
- streamlit

などです。

これらは、多くの場合そのままでは使えません。

先にインストールする必要があります。

---

## 14-8. `pip` とは

外部ライブラリをインストールするときによく使うのが `pip` です。

たとえば、`requests` を入れるなら、

Windows:

```text
python -m pip install requests
```

macOS / Linux:

```text
python3 -m pip install requests
```

のように入力します。

このコマンドは **Pythonのコードの中ではなく、ターミナルへ入力します。**

---

## 14-9. なぜ `pip install requests` だけではなく `python -m pip`？

次の書き方もよく見かけます。

```text
pip install requests
```

ただし、Pythonが複数入っている環境では、

> その `pip` が、どのPythonのものなのか

が分かりにくくなることがあります。

そこでこの教材では、

```text
python -m pip install requests
```

を基本にします。

これは、

> 今 `python` として使っているPythonで、pipを動かす

という意味です。

macOS / Linuxで `python3` を使っているなら、

```text
python3 -m pip install requests
```

です。

---

## 14-10. インストールしたのに `ModuleNotFoundError`？

外部ライブラリで非常によくあるのが、

> 「pipで入れたのに見つからない！」

という問題です。

たとえば、

```text
ModuleNotFoundError: No module named 'requests'
```

が出ることがあります。

原因の1つは、

```text
ライブラリを入れたPython
        と
プログラムを実行したPython
```

が別になっていることです。

---

## 14-11. Pythonは1台に1個とは限らない

1台のPCに、

```text
Python 3.10
Python 3.12
仮想環境のPython
```

のように複数のPythonがあることがあります。

たとえば、

```text
Python Aへ requests を入れた

でも

Python Bでプログラムを実行した
```

なら、Python Bからは requests が見えません。

---

## 14-12. まず実行しているPythonをそろえる

Windowsなら、

```text
python --version
python -m pip --version
```

macOS / Linuxなら、

```text
python3 --version
python3 -m pip --version
```

を確認できます。

大事なのは、

> **インストールに使うPythonと、実行に使うPythonをそろえる**

ことです。

---

## 14-13. 仮想環境とは

外部ライブラリを使うようになると、プロジェクトごとに必要なライブラリが変わります。

たとえば、

```text
アプリA
→ requests 2.x が必要

アプリB
→ 別のライブラリ構成が必要
```

ということがあります。

全部を1か所へ入れると、だんだん管理しにくくなります。

そこで、プロジェクトごとにPython環境を分ける **仮想環境** を使えます。

---

## 14-14. 仮想環境を作る

Windows:

```text
python -m venv .venv
```

macOS / Linux:

```text
python3 -m venv .venv
```

これで、今いるフォルダに `.venv` という仮想環境用のフォルダが作られます。

---

## 14-15. 仮想環境を有効化する

Windows:

```text
.venv\Scripts\activate
```

macOS / Linux:

```text
source .venv/bin/activate
```

有効になると、

```text
(.venv)
```

のような表示がターミナルの先頭に出ることがあります。

詳しい作成手順は、環境構築の **[仮想環境 venv](../01_環境構築/05_仮想環境.md)** でも確認できます。

---

## 14-16. 仮想環境の中でpipを使う

仮想環境を有効にしたあと、

```text
python -m pip install requests
```

のようにインストールします。

すると、その仮想環境の中へライブラリが入ります。

そのまま同じターミナルで、

```text
python sample.py
```

と実行すれば、同じ仮想環境のPythonが使われます。

---

## 14-17. 仮想環境を終了する

仮想環境を抜けるときは、

```text
deactivate
```

と入力します。

---

## 14-18. `import` と `pip` は役割が違う

ここは重要です。

```text
pip
→ 外部ライブラリをPCのPython環境へ入れる

import
→ 入っている機能を、そのプログラムから使えるようにする
```

です。

たとえば、

```text
python -m pip install requests
```

でインストールしてから、

Pythonコードで、

```python
import requests
```

と書きます。

---

## 14-19. 標準ライブラリならpipは不要

`random` は標準ライブラリなので、

```text
python -m pip install random
```

のような操作は必要ありません。

そのまま、

```python
import random
```

で使えます。

```text
標準ライブラリ
→ Pythonと一緒に用意されている

外部ライブラリ
→ 必要に応じてpipなどで追加する
```

という違いです。

---

## 14-20. 自分で試してみる

`randint(1, 10)` の数字を変えてみましょう。

```python
number = random.randint(1, 100)
```

これなら1から100までのランダムな整数になります。

また、

```python
import math

print(math.sqrt(25))
```

とすれば、`math` という標準ライブラリも試せます。

---

## 14-21. 次はCSVとJSON

ここまでで、

- Pythonに最初からある機能
- 外から追加する機能
- `import`
- `pip`
- 仮想環境

の役割が見えてきました。

次は、標準ライブラリの `csv` や `json` を実際に使って、**[15章「CSV・JSON」](../15_CSV・JSON/CSV・JSON.md)** を扱います。

---

## 14-22. ここまでで覚えること

この章では、次のことが分かれば十分です。

1. モジュールは関係する機能のまとまり
2. `import` でそのまとまりをプログラムから使えるようにする
3. 標準ライブラリはPythonに最初から用意されている
4. 外部ライブラリは別途インストールが必要な場合がある
5. `pip` は外部ライブラリをインストールするために使う
6. この教材では `python -m pip` を基本にする
7. インストールしたPythonと実行しているPythonが違うとライブラリが見つからないことがある
8. 仮想環境でプロジェクトごとにライブラリを分けられる
9. `pip` と `import` は役割が違う

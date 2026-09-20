# 14. モジュール・pip・外部ライブラリ

この章では、**別のファイルにまとめた機能を読み込んで使う方法**を学びます。

最初に自分で作ったPythonファイルを `import` します。

そのあとで、Pythonに最初から用意されている標準ライブラリや、pipで追加する外部ライブラリへ進みます。

---

## 14-1. なぜ `import` が必要なの？

ここまで、変数や関数、クラスを1つのファイルに書いてきました。

でもプログラムが大きくなると、

```text
計算する関数
文字を整える関数
ファイルを扱う関数
設定を扱う関数
...
```

が全部1つのファイルに集まってきます。

> 「このファイル何千行になるんだよ！」

となります。

そこで、関係する処理を別のPythonファイルへ分けます。

そして、必要なファイルを `import` して使います。

---

## 14-2. Pythonファイル1つを「まとまり」として使える

まず、次の2つのファイルを同じフォルダに置きます。

```text
14_モジュール・pip・外部ライブラリ/
├─ message_tools.py
└─ module_example.py
```

`message_tools.py` には、文字を作る関数をまとめます。

```python
def make_greeting(name):
    return f"こんにちは {name}"

def make_goodbye(name):
    return f"さようなら {name}"
```

つまり、

```text
message_tools
├─ make_greeting()
└─ make_goodbye()
```

というまとまりです。

---

## 14-3. 自分で作ったファイルを `import` する

[module_example.py](./module_example.py) を見てください。

```python
import message_tools

message1 = message_tools.make_greeting("たろう")
message2 = message_tools.make_goodbye("さくら")

print(message1)
print(message2)
```

ここで、

```python
import message_tools
```

と書いています。

これは、

> `message_tools.py` というPythonファイルのまとまりを、このプログラムから使えるようにする

という意味です。

---

## 14-4. `.py` は書かない

ファイル名は、

```text
message_tools.py
```

ですが、importするときは、

```python
import message_tools
```

と書きます。

`.py` は付けません。

---

## 14-5. `message_tools.make_greeting()` の意味

```python
message_tools.make_greeting("たろう")
```

は、

> `message_tools` というまとまりの中にある `make_greeting` を使う

という意味です。

```text
message_tools . make_greeting("たろう")
      ↑               ↑
   まとまり       その中の関数
```

です。

ここでも、

> `A.B` は「Aの中にあるBを使う」

と考えれば十分です。

---

## 14-6. つまり `import` は何をしている？

この章でまず覚えてほしいのは、

> **別のPythonファイルを、機能のまとまりとして使えるようにする**

ということです。

```text
message_tools.py
        ↓
import message_tools
        ↓
message_tools.make_greeting()
```

という流れです。

---

## 14-7. モジュールとは

Pythonでは、このように読み込んで使う機能のまとまりを **モジュール** と呼びます。

最初は、

> モジュール = Pythonの機能をまとめたもの

くらいで構いません。

自分で作った `message_tools.py` もモジュールとして使えます。

---

## 14-8. 標準ライブラリも同じ仕組み

自分で作ったファイルだけでなく、Pythonには最初から便利なモジュールが用意されています。

たとえば `random` です。

```python
import random

number = random.randint(1, 10)

print(number)
```

ここでも仕組みは同じです。

```text
random
├─ randint()
├─ choice()
└─ shuffle()
```

という機能のまとまりを `import random` で使えるようにしています。

---

## 14-9. 標準ライブラリとは

Pythonに最初から用意されているモジュールや機能の集まりを **標準ライブラリ** と呼びます。

たとえば、

- `random`
- `math`
- `datetime`
- `json`
- `csv`

などがあります。

標準ライブラリは、基本的に追加インストールなしで使えます。

---

## 14-10. 自作モジュールと標準ライブラリの違い

大まかには、

```text
message_tools
→ 自分で作ったPythonファイル

random
→ Pythonが最初から用意しているモジュール
```

です。

でも、使い方の基本は同じです。

```python
import message_tools
import random
```

どちらも、

> そのまとまりを使えるようにする

ための `import` です。

---

## 14-11. 外部ライブラリとは

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

## 14-12. `pip` とは

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

このコマンドは **Pythonコードではなく、ターミナルへ入力します。**

---

## 14-13. なぜ `python -m pip` を使うの？

```text
pip install requests
```

という書き方もあります。

ただし、Pythonが複数入っている環境では、

> そのpipがどのPythonのものなのか

分かりにくくなることがあります。

そこでこの教材では、

```text
python -m pip install requests
```

を基本にします。

これは、

> 今 `python` として使っているPythonでpipを動かす

という意味です。

---

## 14-14. インストールしたのに `ModuleNotFoundError`？

外部ライブラリでよくあるのが、

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

## 14-15. Pythonは1台に1個とは限らない

1台のPCに、

```text
Python 3.10
Python 3.12
仮想環境のPython
```

のように複数のPythonがあることがあります。

そのため、

```text
Python Aへ requests を入れた

でも

Python Bでプログラムを実行した
```

なら、Python Bからはrequestsが見えません。

---

## 14-16. 実行しているPythonをそろえる

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

を確認できます。

大事なのは、

> **インストールに使うPythonと、実行に使うPythonをそろえる**

ことです。

---

## 14-17. 仮想環境とは

外部ライブラリを使うようになると、プロジェクトごとに必要なライブラリが変わります。

全部を1か所へ入れると管理しにくくなるため、プロジェクトごとにPython環境を分ける **仮想環境** を使えます。

---

## 14-18. 仮想環境を作る

Windows:

```text
python -m venv .venv
```

macOS / Linux:

```text
python3 -m venv .venv
```

これで、今いるフォルダに `.venv` が作られます。

---

## 14-19. 仮想環境を有効化する

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

のような表示が出ることがあります。

詳しくは、環境構築の **[仮想環境 venv](../01_環境構築/05_仮想環境.md)** も参照してください。

---

## 14-20. 仮想環境の中でpipを使う

仮想環境を有効にしたあと、

```text
python -m pip install requests
```

のようにインストールします。

そのまま同じターミナルでPythonを実行すれば、同じ仮想環境を使えます。

---

## 14-21. 仮想環境を終了する

```text
deactivate
```

で仮想環境を抜けられます。

---

## 14-22. `pip` と `import` は役割が違う

```text
pip
→ 外部ライブラリをPython環境へ入れる

import
→ 使える状態のモジュールを、そのプログラムから読み込む
```

です。

たとえば、

```text
python -m pip install requests
```

で入れたあと、

```python
import requests
```

と書いて使います。

---

## 14-23. 標準ライブラリならpipは不要

`random` は標準ライブラリなので、

```text
python -m pip install random
```

は必要ありません。

そのまま、

```python
import random
```

で使えます。

---

## 14-24. 実行してみる

まず、

- `message_tools.py`
- `module_example.py`

を同じフォルダに置きます。

Windows:

```text
python module_example.py
```

macOS / Linux:

```text
python3 module_example.py
```

実行結果:

```text
こんにちは たろう
さようなら さくら
```

となれば成功です。

---

## 14-25. 自分で変えてみる

`message_tools.py` に関数を追加してみましょう。

```python
def make_thanks(name):
    return f"ありがとう {name}"
```

そして `module_example.py` から、

```python
print(message_tools.make_thanks("けん"))
```

と呼んでみます。

別ファイルへ機能を追加して、それをimport側から使えることを確認してください。

---

## 14-26. 次はCSVとJSON

ここまでで、

- 自分で作ったPythonファイル
- 標準ライブラリ
- 外部ライブラリ
- `import`
- `pip`
- 仮想環境

の関係が見えてきました。

次は、標準ライブラリの `csv` や `json` を実際に使って、**[15章「CSV・JSON」](../15_CSV・JSON/CSV・JSON.md)** を扱います。

---

## 14-27. ここまでで覚えること

この章では、次のことが分かれば十分です。

1. Pythonファイルを機能のまとまりとして分けられる
2. 自分で作った `.py` ファイルもimportできる
3. importするときは `.py` を書かない
4. `A.B` で「Aの中にあるB」を使える
5. モジュールは機能のまとまり
6. 標準ライブラリも同じimportの仕組みで使える
7. 外部ライブラリはpipなどで追加する
8. pipとimportは役割が違う
9. インストールしたPythonと実行しているPythonはそろえる
10. 仮想環境でプロジェクトごとにライブラリを分けられる

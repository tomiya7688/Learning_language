# 14. import・モジュール

この章では、**長くなったPythonファイルを分けて、別のファイルから読み込む方法**を学びます。

> **ファイル長すぎて読む気失せるわ！！！**
>
> だから分ける。分けたファイルを `import` で使う。

これが、この章で学ぶ `import` の出発点です。

---

## 14-1. なぜ `import` が必要なの？

小さいプログラムなら、1つの `.py` ファイルに全部書いても問題ありません。

でも処理が増えると、変数、関数、クラス、計算、文字列処理、ファイル処理などが全部1ファイルへ集まります。

> **「ファイル長すぎて読む気失せるわ！！！」**

となるので、役割ごとに別ファイルへ分けます。

---

## 14-2. 関数を別ファイルへ分ける

`message_tools.py` に、挨拶関係の関数をまとめます。

```python
def make_greeting(name):
    return f"こんにちは {name}"


def make_goodbye(name):
    return f"さようなら {name}"
```

これで `message_tools.py` が、挨拶処理のまとまりになります。

---

## 14-3. 別ファイルから使う

`module_example.py` では、

```python
import message_tools

message1 = message_tools.make_greeting("たろう")
message2 = message_tools.make_goodbye("さくら")

print(message1)
print(message2)
```

と書きます。

`import message_tools` は、

> **`message_tools.py` という別ファイルのまとまりを、このファイルから使えるようにする**

という意味です。

---

## 14-4. `.py` は書かない

実際のファイル名は `message_tools.py` ですが、importするときは、

```python
import message_tools
```

と書きます。`.py` は付けません。

---

## 14-5. `A.B` で中のものを使う

```python
message_tools.make_greeting("たろう")
```

は、

> `message_tools` の中にある `make_greeting` を使う

という意味です。

```text
message_tools . make_greeting(...)
      ↑               ↑
   まとまり       その中の関数
```

---

## 14-6. モジュールとは

Pythonでは、このように分けて置いた機能のまとまりを **モジュール** として扱えます。

今は、

> **モジュール = 分けて置いたPythonの機能のまとまり**

くらいで十分です。

---

## 14-7. 実行する

2つのファイルを同じフォルダに置きます。

```text
14_import・モジュール/
├─ message_tools.py
└─ module_example.py
```

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

---

## 14-8. ファイルを分けると何がうれしい？

たとえば、

```text
main.py
message_tools.py
file_tools.py
calculation_tools.py
```

のように役割ごとに分ければ、「挨拶処理どこだっけ？」となったときに `message_tools.py` を見れば済みます。

1ファイルを上から下まで全部探さなくてよくなります。

---

## 14-9. 次は標準ライブラリ

ここまでは、自分で作ったファイルを `import` しました。

次は **[15章「標準ライブラリ・外部ライブラリ・pip」](../15_標準ライブラリ・外部ライブラリ・pip/標準ライブラリ・外部ライブラリ・pip.md)** で、Pythonが最初から持っているモジュールや、外から追加するライブラリを扱います。

---

## 14-10. ここまでで覚えること

1. 1ファイルが長くなったら役割ごとに分けられる
2. 別の `.py` ファイルを `import` できる
3. importするときは `.py` を書かない
4. `A.B` で「Aの中にあるB」を使える
5. モジュールは分けて置いたPythonの機能のまとまり
6. importの最初の目的は、コードを分けて読みやすくすること

---

## 前後のページ

← [13. 例外処理](../13_例外処理/例外処理.md)

[15. 標準ライブラリ・外部ライブラリ・pip](../15_標準ライブラリ・外部ライブラリ・pip/標準ライブラリ・外部ライブラリ・pip.md) →

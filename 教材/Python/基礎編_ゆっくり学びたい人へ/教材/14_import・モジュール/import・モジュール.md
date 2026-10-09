# 14. import・モジュール

挨拶を作る処理も計算する処理も1つのファイルへ書き足していると、挨拶を変えたいだけなのに、長いコードからその場所を探すことになります。

> **「ファイル長すぎて読む気失せるわ！！！」**

挨拶の処理は挨拶のファイルへ分けて、直す場所を見つけやすくしたいところです。この章では、挨拶を作る処理を別のPythonファイルへまとめ、使う側のファイルから読み込みます。分けたファイルを使うための書き方が **`import`** です。

---


## Pythonファイルの保存場所

コードのファイルが増えると、教材の説明や画像のファイルと混ざって探しにくくなります。Pythonファイルは、練習用フォルダ内の `src` にまとめてください。

`src` はsource（ソース）の略で、ソースコードを入れるフォルダです。ソースコードは、書いたプログラムのことです。

この章のコードを保存する練習用フォルダを1つ選んでください。まだない場合は、保存したい場所で、Windowsはエクスプローラーの **新規作成 → フォルダー**、macOSはFinderの **ファイル → 新規フォルダ**、Linux（GNOMEの「ファイル」）は右クリックの **新しいフォルダー** を選び、練習用フォルダを作ってください。

練習用フォルダの中で、Windowsはエクスプローラーの空いている場所を右クリックして **新規作成 → フォルダー**、macOSはFinderの **ファイル → 新規フォルダ**、Linux（GNOMEの「ファイル」）は空いている場所を右クリックして **新しいフォルダー** を選んでください。フォルダ名を `src` と入力してEnterキーを押すと、練習用フォルダの中に `src` ができます。すでに `src` がある場合はそのフォルダを使い、保存済みのコードは必要な変更だけを行ってください。

VS Codeで開くフォルダと、ターミナルの `cd` で移動するフォルダは、`src` の一つ上の練習用フォルダです。保存先を選ぶときは `src` を開き、起動するときは練習用フォルダから `src/module_example.py` を指定してください。実行手順のコマンドは、この練習用フォルダから入力してください。


## 14-1. なぜ `import` が必要なの？

小さいプログラムなら、1つの `.py` ファイルに全部書いても問題ありません。

でも処理が増えると、変数、関数、クラス、計算、文字列処理、ファイル処理などが全部1ファイルへ集まります。

> **「ファイル長すぎて読む気失せるわ！！！」**

となるので、役割ごとに別ファイルへ分けます。

---

## 14-2. 関数を別ファイルへ分ける

挨拶関係の関数を別ファイルへまとめてください。

練習用フォルダ内の `src` に保存してください。中身がメッセージを作る道具なので、ファイル名は [`message_tools.py`](./src/message_tools.py) にしてください。

このコードの元ファイル：[`message_tools.py` の 1〜7行](./src/message_tools.py#L1-L7)。

```python
# 挨拶文を作る関数をこのファイルへまとめます。
def make_greeting(name):
    return f"こんにちは {name}"


def make_goodbye(name):
    return f"さようなら {name}"
```

このコードの元ファイル：[`message_tools.py` の 2〜7行](./src/message_tools.py#L2-L7)。

```python
def make_greeting(name):
    return f"こんにちは {name}"


def make_goodbye(name):
    return f"さようなら {name}"
```

これで `message_tools.py` が、挨拶処理のまとまりになります。

---

## 14-3. 別ファイルから使う

次は、分けた `message_tools.py` を使う側のファイルを作ってください。

練習用フォルダ内の同じ `src` に保存してください。モジュールを使う例なので、[`module_example.py`](./src/module_example.py) にしてください。

このコードの元ファイル：[`module_example.py` の 1〜10行](./src/module_example.py#L1-L10)。

```python
# 別ファイルの message_tools を使えるようにします。
import message_tools

# 挨拶文を作り、message1 に保存します。
message1 = message_tools.make_greeting("たろう")
# 別れの挨拶を作り、message2 に保存します。
message2 = message_tools.make_goodbye("さくら")

print(message1)
print(message2)
```

まず `message_tools` を読み込みます。

このコードの元ファイル：[`module_example.py` の 2〜10行](./src/module_example.py#L2-L10)。

```python
import message_tools

message1 = message_tools.make_greeting("たろう")
message2 = message_tools.make_goodbye("さくら")

print(message1)
print(message2)
```

と書いてください。

`import message_tools` は、

> **`message_tools.py` という別ファイルのまとまりを、このファイルから使えるようにする**

という意味です。

---

## 14-4. `.py` は書かない

実際のファイル名は `message_tools.py` ですが、importするときは、

このコードの元ファイル：[`module_example.py` の 2〜2行](./src/module_example.py#L2-L2)。

```python
import message_tools
```

と書いてください。`.py` は付けません。

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

Pythonでは、ファイルに分けて置いた機能のまとまりをモジュールとして読み込み、別のプログラムから使えます。

---

## 14-7. 実行する

2つのファイルを、練習用フォルダ内の同じ `src` に置いてください。

```text
14_import・モジュール/
└─ src/
   ├─ message_tools.py
   └─ module_example.py
```

Windows:

1. VS Code のターミナルを開いてください。表示されていなければ **表示（View）→ ターミナル（Terminal）** を選んでください。前の操作から続ける場合は、同じターミナルを使ってください。
2. 練習用フォルダの中に `src` が見える場所のパスをコピーしてください。Windowsはエクスプローラーのアドレス欄をクリックしてCtrl + C、macOSはFinderでその練習用フォルダを選んでOption + Command + C、Linux（GNOMEの「ファイル」）は練習用フォルダを開いてCtrl + L、Ctrl + Cを押してください。同じターミナルに `cd "srcの一つ上の練習用フォルダのパス"` と入力し、引用符の中をいまコピーしたパスに置き換えて、Enterキーを押してください。ターミナルの現在のフォルダが練習用フォルダへ変わります。
3. 次のコマンドを、そのターミナルに入力してください。
4. Enter キーを押してください。

```text
python src/module_example.py
```

macOS / Linux:

1. VS Code のターミナルを開いてください。表示されていなければ **表示（View）→ ターミナル（Terminal）** を選んでください。前の操作から続ける場合は、同じターミナルを使ってください。
2. 練習用フォルダの中に `src` が見える場所のパスをコピーしてください。Windowsはエクスプローラーのアドレス欄をクリックしてCtrl + C、macOSはFinderでその練習用フォルダを選んでOption + Command + C、Linux（GNOMEの「ファイル」）は練習用フォルダを開いてCtrl + L、Ctrl + Cを押してください。同じターミナルに `cd "srcの一つ上の練習用フォルダのパス"` と入力し、引用符の中をいまコピーしたパスに置き換えて、Enterキーを押してください。ターミナルの現在のフォルダが練習用フォルダへ変わります。
3. 次のコマンドを、そのターミナルに入力してください。
4. Enter キーを押してください。

```text
python3 src/module_example.py
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
src/message_tools.py
file_tools.py
src/calculation_tools.py
```

のように役割ごとに分ければ、「挨拶処理どこだっけ？」となったときに `message_tools.py` を見れば済みます。

1ファイルを上から下まで全部探さなくてよくなります。

---

## 14-9. 今回の内容

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

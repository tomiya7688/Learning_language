# 0. Python の環境構築

この章では、Python のプログラムを自分の PC で実行できる状態にします。

最初の目標は、次のコマンドを実行して Python のバージョンが表示されることです。

```text
Python 3.x.x
```

このリポジトリでは **Python 3** を使用します。

> 2026年9月時点では Python 3.14 系が最新の安定系列です。
> ただし、この教材では特別な理由がない限り、Python 3 の新しい安定版を使用すれば問題ありません。

---

## 0-1. Windows

### Python をインストールする

Python 公式サイトを開きます。

- https://www.python.org/downloads/

現在の Windows では、公式の **Python Install Manager** を使用できます。

Python Install Manager をインストールしたあと、PowerShell またはコマンドプロンプトを開きます。

まず、次のコマンドを入力します。

```powershell
python
```

Python がまだインストールされていない場合は、Python Install Manager が安定版の Python を導入できます。

インストール後、次のコマンドで確認します。

```powershell
python --version
```

例:

```text
Python 3.14.7
```

同じ環境では、次のコマンドも利用できます。

```powershell
py --version
```

### Python を終了する

`python` だけを入力すると、Python を対話形式で操作する画面が開きます。

```text
>>>
```

この画面を終了するときは、次のように入力します。

```python
exit()
```

---

## 0-2. macOS

Python 公式サイトから Python 3 の macOS 用インストーラーを入手できます。

- https://www.python.org/downloads/macos/

インストール後、ターミナルを開いて次のコマンドを実行します。

```bash
python3 --version
```

例:

```text
Python 3.14.7
```

macOS や Linux では、`python` ではなく `python3` というコマンドを使うことがあります。

---

## 0-3. Linux

Linux では、ディストリビューションによって Python 3 が最初からインストールされている場合があります。

まず確認します。

```bash
python3 --version
```

Python 3 が見つからない場合は、使用しているディストリビューションのパッケージマネージャーからインストールします。

Ubuntu / Debian 系の例:

```bash
sudo apt update
sudo apt install python3
```

インストール後、もう一度確認します。

```bash
python3 --version
```

> Linux では OS 自身が Python を使用している場合があります。
> システムに入っている Python を不用意に削除したり、置き換えたりしないようにしてください。

---

## 0-4. 最初の Python コードを実行する

環境構築ができたか確認するため、小さなプログラムを動かします。

任意の場所に `hello.py` という名前のファイルを作り、次の1行を書きます。

```python
# 画面に Hello, Python! と表示します。
print("Hello, Python!")
```

Windows:

```powershell
python hello.py
```

macOS / Linux:

```bash
python3 hello.py
```

次のように表示されれば、Python を実行する環境は完成です。

```text
Hello, Python!
```

---

## 0-5. 仮想環境について

Python では、プロジェクトごとに使用するライブラリを分けるために **仮想環境** を利用できます。

最初の数個のサンプルを読むだけなら必須ではありませんが、Python を継続して使う場合は利用を推奨します。

仮想環境は標準機能の `venv` で作成できます。

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

有効になると、ターミナルの先頭に `(.venv)` などと表示されます。

終了するときは、どの OS でも次のコマンドを使用できます。

```text
deactivate
```

仮想環境については、外部ライブラリを扱う章でも改めて説明します。

---

## 0-6. エディタ

Python のソースコードは普通のテキストファイルなので、テキストを編集できるソフトであれば作成できます。

学習を続ける場合は、プログラミング向けのエディタを使うと便利です。

例:

- Visual Studio Code
- PyCharm
- その他のテキストエディタ

ただし、この教材では特定のエディタを必須にはしません。

---

## 0-7. 確認

ここまで終わったら、次の3点を確認してください。

1. Python 3 がインストールされている
2. ターミナルから Python のバージョンを確認できる
3. `hello.py` を実行して `Hello, Python!` と表示できる

これらが確認できれば、Python の学習を始める準備は完了です。

---

## 参考

- Python 公式サイト: https://www.python.org/
- Python ドキュメント: https://docs.python.org/ja/3/

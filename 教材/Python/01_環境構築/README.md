# 1. Python の環境構築

この章では、Python のプログラムを自分の PC で実行できる状態にします。

最初の目標は、次のコマンドを実行して Python のバージョンが表示されることです。

```text
Python 3.x.x
```

このリポジトリでは **Python 3** を使用します。

> 2026年9月時点では Python 3.14 系が最新の安定系列です。
> ただし、この教材では特別な理由がない限り、Python 3 の新しい安定版を使用すれば問題ありません。

---

## 1-1. Windows

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

## 1-2. macOS

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

## 1-3. Linux

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

## 1-4. 最初の Python コードを実行する

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

## 1-5. 仮想環境について

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

## 1-6. エディタ

Python のソースコードは普通のテキストファイルなので、テキストを編集できるソフトであれば作成できます。

学習を続ける場合は、プログラミング向けのエディタを使うと便利です。

例:

- Visual Studio Code
- PyCharm
- その他のテキストエディタ

ただし、この教材では特定のエディタを必須にはしません。

---

## 1-7. PATH とは

環境構築で特につまずきやすいのが **PATH（パス）** です。

PATH は、ターミナルで `python` のようなコマンドを入力したときに、
「そのプログラムをどのフォルダから探すか」を OS に教えるための設定です。

たとえば Python 本体が次の場所にあるとします。

```text
C:\Users\ユーザー名\AppData\Local\Programs\Python\Python314\python.exe
```

このとき PATH に入れるのは、通常 **python.exe そのものではなく、python.exe が入っているフォルダ** です。

```text
C:\Users\ユーザー名\AppData\Local\Programs\Python\Python314\
```

### どこまで PATH に入れればいいの？

基本は、

> **実行したい .exe ファイルが入っているフォルダまで**

です。

Python の場合は、主に次の2か所が関係します。

```text
C:\Users\ユーザー名\AppData\Local\Programs\Python\Python314\
C:\Users\ユーザー名\AppData\Local\Programs\Python\Python314\Scripts\
```

1つ目には `python.exe` があります。

2つ目の `Scripts` には、`pip.exe` など Python 関連のコマンドが入ります。

そのため、手動で PATH を設定する場合は、通常この2つを追加します。

> インストール方法によって実際のフォルダは異なります。
> 上の例をそのままコピーせず、自分の PC にある Python の場所を確認してください。

### PATH に python.exe まで書いてはいけないの？

PATH に追加するのは通常フォルダです。

たとえば、

```text
C:\Python314\python.exe
```

ではなく、

```text
C:\Python314\
```

を追加します。

OS は PATH に登録されたフォルダの中から、入力されたコマンド名に対応する実行ファイルを探します。

### Python がどこにあるか確認する

Windows では、Python が認識されている場合は次のコマンドで場所を確認できます。

```powershell
where python
```

または、

```powershell
where py
```

macOS / Linux では、

```bash
which python3
```

を使えます。

### PATH を変更したのに反映されない

PATH を変更したあと、すでに開いていた PowerShell やコマンドプロンプトには
変更が反映されていないことがあります。

その場合は、

1. ターミナルを閉じる
2. 新しくターミナルを開く
3. もう一度 `python --version` を試す

という順番で確認してください。

---

## 1-8. パスとディレクトリの補助知識

PATH の設定や Python ファイルの実行では、**ディレクトリ（フォルダ）** と **パス** の考え方も重要です。

### カレントディレクトリとは

ターミナルには、今どのフォルダを基準に操作しているかという概念があります。

これを **カレントディレクトリ** と呼びます。

たとえば Windows で、

```text
C:\Users\sample\Documents\Python
```

をカレントディレクトリにしているとき、

```powershell
python hello.py
```

と実行すると、基本的にはそのフォルダの中にある `hello.py` を探します。

### 今いる場所を確認する

Windows PowerShell:

```powershell
pwd
```

macOS / Linux:

```bash
pwd
```

現在のディレクトリが表示されます。

### フォルダの中身を見る

Windows:

```powershell
dir
```

macOS / Linux:

```bash
ls
```

### `cd` で移動する

`cd` は、カレントディレクトリを変更するためのコマンドです。

たとえば、

```powershell
cd Documents
```

とすると、現在のフォルダの中にある `Documents` へ移動します。

1つ上のフォルダへ戻る場合は、

```text
cd ..
```

を使います。

特定の場所へ直接移動することもできます。

Windows:

```powershell
cd C:\Users\sample\Documents\Python
```

macOS / Linux:

```bash
cd /home/sample/python
```

### 絶対パスとは

ファイルやフォルダの場所を、先頭からすべて書いたものを **絶対パス** と呼びます。

Windows の例:

```text
C:\Users\sample\Documents\Python\hello.py
```

macOS / Linux の例:

```text
/home/sample/python/hello.py
```

絶対パスは、今いる場所に関係なく同じ場所を表します。

### 相対パスとは

今いる場所を基準にして書いたパスを **相対パス** と呼びます。

たとえばカレントディレクトリが、

```text
C:\Users\sample\Documents\Python
```

で、その中に `hello.py` がある場合、

```text
hello.py
```

だけでそのファイルを指定できます。

また、

```text
..\hello.py
```

のように `..` を使うと、1つ上のフォルダを基準にできます。

macOS / Linux では、

```text
../hello.py
```

のように書きます。

### なぜ `python hello.py` で失敗することがあるの？

Python が壊れているとは限りません。

よくある原因は、

> **ターミナルが、hello.py のあるフォルダにいない**

ことです。

その場合は、

1. `pwd` で現在地を確認する
2. `dir` または `ls` でファイルがあるか見る
3. `cd` でファイルのある場所へ移動する
4. もう一度実行する

という順番で確認します。

### ユーザー環境変数とシステム環境変数

Windows で PATH を設定するとき、
**ユーザー環境変数** と **システム環境変数** の2種類が表示されます。

ユーザー環境変数は、その Windows ユーザーだけに適用されます。

システム環境変数は、その PC を使う複数のユーザーに影響します。

個人で使う PC で Python を学習する場合は、基本的には **ユーザー環境変数の PATH に追加** すれば十分です。

システム環境変数を変更するには管理者権限が必要になることがあり、
他のユーザーやソフトにも影響するため、よく分からない場合は無理に変更しない方が安全です。

### PATH と普通の「パス」は同じもの？

言葉が似ていますが、少し意味が違います。

- **パス**: ファイルやフォルダの場所を表す文字列
- **PATH**: コマンドを探すフォルダの一覧を保存している環境変数

たとえば、

```text
C:\Users\sample\Documents\Python\hello.py
```

はファイルの **パス** です。

一方、

```text
C:\Users\sample\AppData\Local\Programs\Python\Python314\
```

を PATH 環境変数に追加すると、
ターミナルから `python` を見つけやすくなります。


---

## 1-9. 環境構築 Q&A

環境構築では、Pythonそのものを書く前につまずくことがあります。

「自分にはプログラミングが向いていない」と考える必要はありません。
この段階の問題は、コードではなく PC の設定や現在いるディレクトリが原因であることも多くあります。

### Q. `python --version` を実行しても Python が見つからない

Windows では、まず次も試してください。

```powershell
py --version
```

macOS / Linux では、

```bash
python3 --version
```

を試してください。

`python`、`py`、`python3` のどれを使うかは、OS やインストール方法によって異なることがあります。

それでも見つからない場合は、Python のインストールが完了しているかを確認してください。

インストール直後の場合は、開いているターミナルを一度閉じて、新しく開き直すと認識されることがあります。

### Q. `python` と `python3` は何が違うの？

どちらも Python を起動するためのコマンドとして使われます。

Windows では `python` や `py` が使われることが多く、
macOS / Linux では `python3` が使われることがあります。

この教材では、

- Windows: `python`
- macOS / Linux: `python3`

を基本として説明します。

### Q. `hello.py` を作ったのに実行できない

まず、ターミナルが `hello.py` のある場所を見ているか確認します。

Windows:

```powershell
dir
```

macOS / Linux:

```bash
ls
```

表示された一覧に `hello.py` があるか確認してください。

無い場合は、現在いるディレクトリと、ファイルを保存したディレクトリが異なります。

### Q. ファイルが `hello.py.txt` になっている

Windows の設定によっては、拡張子が画面に表示されていないことがあります。

その状態で `hello.py` と入力して保存すると、実際には

```text
hello.py.txt
```

になっている場合があります。

ファイル名の拡張子を表示する設定にして、本当に `.py` で終わっているか確認してください。

### Q. `can't open file` と表示される

例:

```text
python: can't open file 'hello.py': ...
```

Python は起動できていますが、指定したファイルを見つけられていません。

`dir` または `ls` を使って、現在いる場所に `hello.py` があるか確認してください。

### Q. `SyntaxError` と表示された

Python 自体は起動しています。

多くの場合、書いたコードのどこかに文法上の間違いがあります。

たとえば、

- `"` を閉じ忘れた
- `)` を閉じ忘れた
- 全角記号を使った

などが考えられます。

エラーメッセージには、問題が起きたファイル名や行番号が表示されることがあります。
まず、その行の前後を確認してください。

### Q. `>>>` が表示されてコマンドが入力できない

`python` だけを実行すると、Python の対話モードに入ります。

```text
>>>
```

が表示されている場合、そこは PowerShell やターミナルではなく Python の入力画面です。

次を入力して終了してください。

```python
exit()
```

その後、

```powershell
python hello.py
```

のようにファイル名まで指定して実行します。

### Q. コマンドはどこに入力するの？

Python のコードを書く場所と、コマンドを入力する場所は別です。

- `print("Hello")` などを書く場所: `.py` ファイル
- `python hello.py` などを入力する場所: PowerShell、コマンドプロンプト、ターミナル

初めは混同しやすいので注意してください。

### Q. エディタは Visual Studio Code じゃないと駄目？

いいえ。

Python のファイルはテキストファイルなので、コードを保存できるエディタなら使用できます。

ただし、プログラミング向けエディタには、

- 構文を色分けする
- 入力ミスを見つけやすくする
- ターミナルを同じ画面で開ける

などの便利な機能があります。

### Q. バージョン番号が教材と違う

Python 3 系で、この教材で使う機能が利用できるバージョンなら、基本的には問題ありません。

たとえば教材の例が、

```text
Python 3.14.7
```

で、自分の環境が別の Python 3 のバージョンでも、最初の学習ではそのまま進められる場合がほとんどです。

バージョン差が重要になる章では、その章で明記します。

---

## 1-10. 確認

ここまで終わったら、次の3点を確認してください。

1. Python 3 がインストールされている
2. ターミナルから Python のバージョンを確認できる
3. `hello.py` を実行して `Hello, Python!` と表示できる

これらが確認できれば、Python の学習を始める準備は完了です。

---

## 参考

- Python 公式サイト: https://www.python.org/
- Python ドキュメント: https://docs.python.org/ja/3/

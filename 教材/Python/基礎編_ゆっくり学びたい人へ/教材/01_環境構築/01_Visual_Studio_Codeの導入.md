# 1-1. Visual Studio Code をインストールする

**Visual Studio Code（VS Code）は、Pythonを書くためのアプリです。**

この教材では、VS Code を使って Python のコードを書きます。

VS Code は Windows / macOS / Linux で利用できます。

公式サイト:

- https://code.visualstudio.com/

---

## Windows

1. VS Code 公式サイトを開く
2. Windows 用の **User Setup** をダウンロードする
3. ダウンロードしたインストーラーを実行する
4. 画面の指示に従ってインストールする
5. Windowsのスタートボタンをクリックし、検索欄に `Visual Studio Code` と入力する
6. 検索結果の **Visual Studio Code** をクリックして起動する

通常の個人利用では User Setup で問題ありません。

VS Code の Windows 用 User Setup は、管理者権限なしでもインストールできます。

---

## macOS

1. VS Code 公式サイトから macOS 用の `.dmg` をダウンロードする
2. `.dmg` を開く
3. `Visual Studio Code.app` を `Applications` フォルダへ移動する
4. Applications から VS Code を起動する

---

## Linux

Linux ではディストリビューションに合ったパッケージを使用します。

Ubuntu / Debian 系では `.deb`、Fedora / RHEL 系では `.rpm` が利用できます。

Ubuntu / Debian 系の例:

1. OS のアプリ一覧から **端末（Terminal）** を開きます。
2. `cd "ダウンロードしたファイルを保存したフォルダのパス"` と入力し、Enter キーを押します。引用符の中は、自分の保存先に置き換えてください。
3. 次のコマンドの「ダウンロードしたファイル.deb」または「ダウンロードしたファイル.rpm」を、実際のファイル名に置き換えて、端末に入力します。
4. Enter キーを押します。

```bash
sudo apt install ./ダウンロードしたファイル.deb
```

Fedora / RHEL 系の例:

1. OS のアプリ一覧から **端末（Terminal）** を開きます。
2. `cd "ダウンロードしたファイルを保存したフォルダのパス"` と入力し、Enter キーを押します。引用符の中は、自分の保存先に置き換えてください。
3. 次のコマンドの「ダウンロードしたファイル.deb」または「ダウンロードしたファイル.rpm」を、実際のファイル名に置き換えて、端末に入力します。
4. Enter キーを押します。

```bash
sudo dnf install ./ダウンロードしたファイル.rpm
```

---

## VS Code の表示を日本語にする

VS Code のメニューやボタンを日本語で表示するには、**Japanese Language Pack** を入れます。たとえば、`File` メニューが「ファイル」と表示されるようになります。

このように、VS Code に機能を追加するものを **拡張機能** といいます。

1. VS Code を起動する
2. 左側の四角が並んだ **Extensions（拡張機能）** アイコンをクリックする。Windows / Linux では **Ctrl + Shift + X**、macOS では **Command + Shift + X** でも開ける
3. 開いた画面の検索欄に `Japanese Language Pack` と入力する
4. Microsoft が提供している [Japanese Language Pack](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-ja) を選ぶ
5. **Install（インストール）** を押す
6. 表示言語の変更や再起動の案内が出たら、案内に従って VS Code を再起動する

再起動したら、上部のメニューが「ファイル」「編集」などの日本語になっていることを確認します。

### 表示が英語のままの場合

1. Windows / Linux では **Ctrl + Shift + P**、macOS では **Command + Shift + P** を押す
2. 画面上部に、操作を検索して選ぶ入力欄が表示される。この画面を **コマンドパレット** と呼ぶ
3. 入力欄に `Configure Display Language` と入力し、一覧に表示された同じ名前の項目を選ぶ
4. 言語の一覧から **日本語（ja）** を選び、再起動の案内に従う

表示言語の設定については、[VS Code の公式説明](https://code.visualstudio.com/docs/configure/locales) でも確認できます。

---

## Python 拡張機能を入れる

VS Code を起動したら、Python を扱いやすくするために Python 拡張機能を入れます。

1. VS Code 左側の **拡張機能** アイコンを開く
2. 検索欄に `Python` と入力する
3. Microsoft が提供している [Python 拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-python.python) を選ぶ
4. **インストール（Install）** を押す

Python 拡張機能を入れると、コードを書くときに続きの候補を表示できます。また、VS Code でコードを動かすときに使う Python を選べます。

Python を選ぶ操作は、Python をインストールしたあとの [1-3. VS Code が使う Python を確認する](./03_動作確認.md) で説明します。

---

## `code` コマンドについて

文字を入力してコンピュータへ操作を指示する方法もあります。まず、その文字を入力する画面を開いてみましょう。

### Windows の検索から開く

1. 画面下の検索欄、または虫眼鏡のアイコンをクリックする
2. 検索欄が見当たらない場合は、Windows のスタートボタンをクリックする
3. `PowerShell` と入力する
4. 検索結果の **Windows PowerShell** または **PowerShell** をクリックして開く
5. 文字を入力できる画面が表示される

このように、文字で操作を指示するための画面を、この教材では **ターミナル** と呼びます。
そこへ入力する操作の指示を **コマンド** と呼びます。

### VS Code の中で開く

VS Code をすでに開いている場合は、その中でもターミナルを開けます。Windows / macOS / Linux で使える手順です。

1. VS Code を起動する
2. 画面上部の **ターミナル（Terminal）** メニューをクリックする
3. **新しいターミナル（New Terminal）** をクリックする
4. 画面下側に文字を入力できる場所が表示される

Python のコードを書く欄ではなく、今開いた文字を入力する場所へコマンドを入力します。

### コマンドで VS Code を開く

開いたターミナルへ、次の1行を入力し、Enter キーを押します。

1. VS Code のターミナルを開きます。表示されていなければ **表示（View）→ ターミナル（Terminal）** を選びます。前の操作から続ける場合は、同じターミナルを使います。
2. 次のコマンドを、そのターミナルに入力します。
3. Enter キーを押します。

```text
code .
```

`PS C:\Users\sample>` など、すでに表示されている文字は入力しません。入力するのは `code .` だけです。

これは「現在のフォルダを VS Code で開く」という意味です。

Windows の通常のインストーラーでは `code` コマンドが PATH に追加されます。

macOSで `code` コマンドが見つからない場合は、次の操作で使えるようにします。

1. VS Codeを開き、**Command + Shift + P** を押します。
2. 画面上部に、操作を検索して選ぶ入力欄が表示されます。この画面が **コマンドパレット** です。
3. 入力欄に `shell command` と入力します。
4. 一覧から **Shell Command: Install 'code' command in PATH** を選びます。
5. VS Codeを **Code → Quit Visual Studio Code** から終了します。
6. Finderの **アプリケーション（Applications）** フォルダで **Visual Studio Code** をダブルクリックして開きます。
7. 上部の **ターミナル（Terminal）→ 新しいターミナル（New Terminal）** を選びます。
8. 画面下に開いたターミナルへ `code .` と入力し、Enterキーを押します。

この設定の手順は、[VS CodeのmacOS向け公式説明](https://code.visualstudio.com/docs/setup/mac#launch-vs-code-from-the-command-line)でも確認できます。

この機能は便利ですが、最初から必須ではありません。

次:

- [Python をインストールする](./02_Pythonの導入.md)

---

## 前後のページ

← [1. 環境構築](./環境構築ガイド.md)

[1-2. Pythonをインストールする](./02_Pythonの導入.md) →

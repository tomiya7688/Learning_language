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
5. VS Code を起動する

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

```bash
sudo apt install ./ダウンロードしたファイル.deb
```

Fedora / RHEL 系の例:

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
3. Microsoft が提供している Python 拡張機能を選ぶ
4. **インストール（Install）** を押す

この拡張機能によって、

- Python コードの補完
- エラーの確認
- Python 実行環境の選択
- デバッグ

などが使いやすくなります。

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

```text
code .
```

`PS C:\Users\sample>` など、すでに表示されている文字は入力しません。入力するのは `code .` だけです。

これは「現在のフォルダを VS Code で開く」という意味です。

Windows の通常のインストーラーでは `code` コマンドが PATH に追加されます。

macOS では必要な場合、VS Code のコマンドパレットから

```text
Shell Command: Install 'code' command in PATH
```

を実行します。

この機能は便利ですが、最初から必須ではありません。

次:

- [Python をインストールする](./02_Pythonの導入.md)

---

## 前後のページ

← [1. 環境構築](./環境構築ガイド.md)

[1-2. Pythonをインストールする](./02_Pythonの導入.md) →

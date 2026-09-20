# 1-1. Visual Studio Code をインストールする

この教材では、Python のコードを書くエディタとして **Visual Studio Code（VS Code）** を使用します。

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

## Python 拡張機能を入れる

VS Code を起動したら、Python を扱いやすくするために Python 拡張機能を入れます。

1. VS Code 左側の **拡張機能** アイコンを開く
2. 検索欄に `Python` と入力する
3. Microsoft が提供している Python 拡張機能を選ぶ
4. **Install** を押す

この拡張機能によって、

- Python コードの補完
- エラーの確認
- Python 実行環境の選択
- デバッグ

などが使いやすくなります。

---

## `code` コマンドについて

VS Code は、ターミナルから次のように開くこともできます。

```text
code .
```

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

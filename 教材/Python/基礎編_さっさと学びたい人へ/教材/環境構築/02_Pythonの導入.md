# 1-2. Python をインストールする

VS Codeにコードを書いただけでは、Pythonのコードを動かせません。実行するPythonもパソコンへ入れる必要があります。

> **「Python入ってないのにPythonが動くわけがない」**

このページでは **Python 3** を入れ、使える状態になったかを確かめてください。

公式サイト:

- https://www.python.org/downloads/

---

## 確認コマンドを入力する場所

Pythonが使えるか確かめるために、VS Codeの画面下側にあるターミナルへ確認コマンドを入力してください。

1. VS Code を起動してください
2. 画面上部の **ターミナル（Terminal）** メニューをクリックしてください
3. **新しいターミナル（New Terminal）** をクリックしてください
4. 画面下側に文字を入力できる場所が表示される

この入力画面が **ターミナル** です。そこへ入力する操作の指示を **コマンド** と呼びます。

Python のコードを書く欄ではなく、今開いたターミナルへ、使っている OS の確認コマンドを入力してください。入力したら Enter キーを押してください。

`PS C:\Users\sample>` など、最初から表示されている文字は入力しないでください。次のコード欄にあるコマンドだけを入力してください。

Python をインストールする前からターミナルを開いていた場合は、インストール後に VS Code を閉じて開き直し、上の手順で新しいターミナルを開いてください。

---

## Windows

[Python公式のダウンロードページ](https://www.python.org/downloads/)から **Python Install Manager**（Pythonを導入するアプリ）のWindows用ファイルをダウンロードしてください。エクスプローラーの「ダウンロード」フォルダで、ダウンロードした `.msix` ファイルをダブルクリックし、表示された画面の **インストール（Install）** を押してください。アプリのインストールが終わったら、VS Codeを閉じて開き直してください。

Python本体を用意するため、VS Codeの **表示（View）→ ターミナル（Terminal）** でターミナルを開き、次のコマンドを入力してEnterキーを押してください。`pymanager install default` は、Python Install Managerが標準で選ぶPython本体を導入する指定です。ダウンロードが終わり、ターミナルが入力待ちへ戻ったら、下のバージョン確認へ進んでください。

```powershell
pymanager install default
```

導入方法は、[Python公式のWindows向け手順](https://docs.python.org/3/using/windows.html#installation)でも確認できます。

Python をインストールしたあと、上の手順で開いた VS Code のターミナルへ次を入力し、Enter キーを押してください。

1. VS Code のターミナルを開いてください。表示されていなければ **表示（View）→ ターミナル（Terminal）** を選んでください。前の操作から続ける場合は、同じターミナルを使ってください。
2. 次のコマンドを、そのターミナルに入力してください。
3. Enter キーを押してください。

```powershell
python --version
```

環境によっては次のコマンドも使えます。

1. VS Code のターミナルを開いてください。表示されていなければ **表示（View）→ ターミナル（Terminal）** を選んでください。前の操作から続ける場合は、同じターミナルを使ってください。
2. 次のコマンドを、そのターミナルに入力してください。
3. Enter キーを押してください。

```powershell
py --version
```

---

## macOS

[Python公式のmacOS向けダウンロードページ](https://www.python.org/downloads/macos/)からPython 3のリリースを選び、**macOS 64-bit universal2 installer** をダウンロードしてください。この配布物はIntelとApple siliconの両方に対応します。

Finderの「ダウンロード」フォルダで、ダウンロードした `.pkg` ファイルをダブルクリックしてください。開いた画面の **続ける（Continue）** で説明とライセンスを読み、同意する場合は **同意する（Agree）** を選んでください。**インストール（Install）** を押し、求められた場合はMacの認証を行ってください。完了の画面が出たらインストーラーを閉じてください。

Finderの「アプリケーション」内にできた `Python 3.x` フォルダを開き、`Install Certificates.command` をダブルクリックしてください。`3.x` は実際に導入したバージョンのフォルダ名です。通信に使う証明書の準備が終わり、開いたターミナルに `update complete` と出たら、そのターミナルを閉じてください。VS Codeを閉じて開き直し、下のバージョン確認を行ってください。[Python公式のmacOS向け導入手順](https://docs.python.org/3/using/mac.html#installation-steps)

インストール後、上の手順で開いた VS Code のターミナルへ次を入力し、Enter キーを押してください。

1. VS Code のターミナルを開いてください。表示されていなければ **表示（View）→ ターミナル（Terminal）** を選んでください。前の操作から続ける場合は、同じターミナルを使ってください。
2. 次のコマンドを、そのターミナルに入力してください。
3. Enter キーを押してください。

```bash
python3 --version
```

---

## Linux

Linux では Python 3 が最初から入っている場合があります。

まず、上の手順で開いた VS Code のターミナルへ次を入力し、Enter キーを押して確認してください。

1. VS Code のターミナルを開いてください。表示されていなければ **表示（View）→ ターミナル（Terminal）** を選んでください。前の操作から続ける場合は、同じターミナルを使ってください。
2. 次のコマンドを、そのターミナルに入力してください。
3. Enter キーを押してください。

```bash
python3 --version
```

Ubuntu / Debian 系で Python 3 が入っていない場合の例:

1. VS Code のターミナルを開いてください。表示されていなければ **表示（View）→ ターミナル（Terminal）** を選んでください。前の操作から続ける場合は、同じターミナルを使ってください。
2. 次のコマンドを上から1行ずつ、そのターミナルに入力してください。
3. 1行入力するたびに Enter キーを押してください。

```bash
sudo apt update
sudo apt install python3
```

> Linux では OS 自身が Python を使用している場合があります。
> システムの Python を不用意に削除したり置き換えたりしないでください。

---

## 確認結果を見る

使っている OS の確認コマンドを実行して、次のように `Python 3` から始まるバージョンが表示されれば、Python のコマンドが認識されています。`x` の部分には実際のバージョン番号が入ります。

```text
Python 3.x.x
```

コマンドが見つからないなどのエラーが出た場合は、[環境構築 Q&A](./06_QA.md) を確認してください。

---

## バージョンが教材と違っても大丈夫？

この教材では Python 3 を前提にします。

細かいバージョン差が重要になる場合は、その章で説明します。

次:

- [VS Code が使う Python を確認する](./03_動作確認.md)

---

## 前後のページ

← [1-1. Visual Studio Codeをインストールする](./01_Visual_Studio_Codeの導入.md)

[1-3. VS Codeが使うPythonを確認する](./03_動作確認.md) →

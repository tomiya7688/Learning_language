# 1-2. Python をインストールする

この教材では **Python 3** を使用します。

公式サイト:

- https://www.python.org/downloads/

---

## Windows

現在の Windows では、Python 公式の **Python Install Manager** を利用できます。

Python をインストールしたあと、PowerShell または VS Code のターミナルで次を実行します。

```powershell
python --version
```

環境によっては次のコマンドも使えます。

```powershell
py --version
```

---

## macOS

Python 公式サイトから macOS 用の Python 3 をインストールします。

インストール後、ターミナルで確認します。

```bash
python3 --version
```

---

## Linux

Linux では Python 3 が最初から入っている場合があります。

まず確認します。

```bash
python3 --version
```

Ubuntu / Debian 系で Python 3 が入っていない場合の例:

```bash
sudo apt update
sudo apt install python3
```

> Linux では OS 自身が Python を使用している場合があります。
> システムの Python を不用意に削除したり置き換えたりしないでください。

---

## バージョンが教材と違っても大丈夫？

この教材では Python 3 を前提にします。

細かいバージョン差が重要になる場合は、その章で説明します。

次:

- [Python が動くか確認する](./03_動作確認.md)

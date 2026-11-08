# 01. Rustの準備

Rustのコードを書いても、動かす道具がなければ結果を見られません。ここでは、道具を入れて最初の文字を表示するところまで進めましょう。

## 1. Rustの道具を入れる

ブラウザ（Webサイトを見るアプリ）でRust公式の[インストール案内](https://www.rust-lang.org/tools/install)を開き、自分のOS（Windows / macOS / Linux）に合った手順で **rustup** を入れてください。Windowsでは、案内に従ってMicrosoft C++ Build Toolsが必要になる場合があります。macOSではコマンドライン開発ツールを求められる場合があります。画面の指示に沿って導入してください。

- **rustup**：Rust本体や更新版を管理する道具。
- **rustc**：書いたRustのコードをコンパイル（実行できる形に変換）する道具。
- **cargo**：複数のコードや設定をまとめ、ビルド（実行用のファイル作成）・実行・テストを行う道具。

## 2. バージョンを確認する

VS Code（コードを書くための編集アプリ）を起動してください。上部メニューの **表示 → ターミナル** を選び、画面下の入力欄を開きます。ターミナルは文字でコンピューターへ操作を伝え、結果を確認する場所です。次のコマンドを**1行ずつ**入力し、それぞれ Enter キーを押してください。

```text
rustup --version
rustc --version
cargo --version
```

それぞれのツール名とバージョン番号（例：`rustc 1.x.x`）が表示されれば準備できています。

「コマンドが見つからない」と表示された場合はターミナルを閉じて開き直してください。Linux / macOSではrustupの案内に従い `$HOME/.cargo/env` を読み込む操作が必要なことがあります。

## 3. 自分のプロジェクトを作る

ターミナルで、作業したいフォルダ（ファイルをまとめる場所）へ移動してください。移動は `cd "フォルダの場所"` と入力して Enter です。ターミナルへ次のコマンドを入力します。

```text
cargo new hello_rust
cd hello_rust
```

`cargo new` は新しいプログラム一式を作ります。`hello_rust` は自分で付けたフォルダ名です。`cd` は作業場所をそのフォルダへ移動します。中には `Cargo.toml`（プロジェクトの設定）と `src/main.rs`（実行を始めるRustコード）があります。拡張子 `.rs` はRustのソースコードです。

VS Codeで **ファイル → フォルダーを開く** から `hello_rust` を選び、`src/main.rs` を開いて次の内容に置き換えて保存（Windows / Linuxは Ctrl+S、macOSは Command+S）してください。

```rust
fn main() {
    // println! でターミナルへ文字を表示する
    println!("Hello, Rust!");
}
```

VS Codeで開いた `hello_rust` フォルダのターミナルに、次のコマンドを入力して Enter を押してください。

```text
cargo run
```

コードの変換が終わると、ターミナルに `Hello, Rust!` と表示されます。`fn main()` は実行を始める処理、`println!` は文字を表示する命令です。詳細は次の章で扱います。

## 4. この教材のサンプルを動かす準備

このリポジトリのページで **Code → Download ZIP** を選び、ZIP（まとめられたファイル）を展開するか、Gitを使える場合は `git clone https://github.com/tomiya7688/Learning_language.git` で教材を保存してください。VS Codeで保存した `Learning_language/教材/Rust` フォルダを開きます。新しく開いたターミナルで `cargo run --example lesson02_hello` を実行すると、次章のプログラムが動きます。

`--example` は `examples` フォルダから指定した実行例を選ぶための指定です。各章はこの形で動かします。

[次へ：最初のプログラム](./02_最初のプログラム.md) / [目次](../目次.md)

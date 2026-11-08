# 23. 完成品：メモ管理CLI

今まで覚えた入力、分岐、一覧、ファイル保存を使い、短いメモを追加・一覧表示できる道具を作ってみましょう。

**この章でできること：** コマンドの後ろに文章を付けて保存し、次回起動時に一覧を表示する。

## コードを見る

[配布した `lesson23_memo.rs` の全体](../examples/lesson23_memo.rs#L1-L49)を、VS Codeで開いてください。次のコードは配布ファイルと同じ内容です。

```rust
use std::env;
use std::fs::{self, OpenOptions};
use std::io::{self, Write};

fn main() -> io::Result<()> {
    // 起動時の引数からプログラム名を除く
    let args: Vec<String> = env::args().skip(1).collect();
    let file_name = "rust_lesson23_notes.txt";

    match args.first().map(String::as_str) {
        Some("add") => {
            // add以降の言葉を一つのメモにまとめる
            let text = args[1..].join(" ");
            if text.trim().is_empty() {
                println!("追加する文章を入力してください");
                return Ok(());
            }

            // 既存のメモを消さずに末尾へ追加する
            let mut file = OpenOptions::new()
                .create(true)
                .append(true)
                .open(file_name)?;
            writeln!(file, "{}", text)?;
            println!("保存しました: {}", text);
        }
        Some("list") => {
            // ファイルがない初回起動にも対応する
            match fs::read_to_string(file_name) {
                Ok(content) => {
                    if content.is_empty() {
                        println!("メモはまだありません");
                    } else {
                        for (index, line) in content.lines().enumerate() {
                            println!("{}: {}", index + 1, line);
                        }
                    }
                }
                Err(error) if error.kind() == io::ErrorKind::NotFound => {
                    println!("メモはまだありません");
                }
                Err(error) => return Err(error),
            }
        }
        _ => println!("使い方: add 文章 / list"),
    }

    Ok(())
}
```


## 実行する

[初めに](../初めに.md)の手順でVS Codeから `教材/Rust` フォルダを開き、**表示 → ターミナル** で次のコマンドを入力して Enter キーを押してください。

```text
cargo run --example lesson23_memo -- add Rustを勉強する
```

ターミナルへ表示される内容の一例：

```text
保存しました: Rustを勉強する
```


## 保存したメモを見る

VS Codeで `教材/Rust` を開き、ターミナルに次のコマンドを入力して Enter を押してください。

```text
cargo run --example lesson23_memo -- list
```

直前に `add Rustを勉強する` を1回だけ実行した場合の表示例は `1: Rustを勉強する` です。既に保存したメモがある場合は、その続きに表示されます。`--` はCargoへの指定と、作ったプログラムへの引数（渡す文字）を分ける記号です。

**保存先：** `教材/Rust/rust_lesson23_notes.txt` です。このファイルにメモが追記され、次回起動時も残ります。個人情報や秘密の内容は入れないでください。

## コードの読み方

`env::args()` はプログラム起動時に渡された言葉を受け取ります。`skip(1)` は実行ファイル名を飛ばします。`args.first()` で最初の指示を読み、`match` で `add`（追加）と `list`（一覧）を選びます。`OpenOptions` は既存のメモに追記するための設定、`fs::read_to_string` は保存済みのメモを読み込む処理です。`io::Result<()>` と `?` は保存・読込時の失敗を隠さず呼び出し側へ知らせます。

## 変更して試す

VS Codeで `lesson23_memo.rs` を開き、次の部分を変更してみましょう。

`println!("保存しました: {}", text);` の `保存しました` を `追加できました` に変えて、`add` コマンドを再実行してください。保存後の案内が変わります。

試した後に元のコードへ戻すと、ほかのページの説明と同じ動作で学習を続けられます。

---

[目次へ戻る](../目次.md)

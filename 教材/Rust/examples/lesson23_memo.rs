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

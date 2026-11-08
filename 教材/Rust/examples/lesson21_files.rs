use std::fs;
use std::io;

fn main() -> io::Result<()> {
    // 学習用の名前でファイルへ文字を保存する
    let file_name = "rust_lesson21_memo.txt";
    fs::write(file_name, "Rustを勉強中\n")?;

    // 保存した文字をファイルから読み戻す
    let memo = fs::read_to_string(file_name)?;
    print!("{}", memo);
    Ok(())
}

// 文字列を変更せずに読む
fn length_of(text: &str) -> usize {
    text.len()
}

// 呼び出し元のStringへ印を付ける
fn append_mark(text: &mut String) {
    text.push('!');
}

fn main() {
    // 同じ文字列を読み取り、後で変更する
    let mut message = String::from("Rust");
    let size = length_of(&message);
    println!("変更前のバイト数: {}", size);

    append_mark(&mut message);
    println!("変更後: {}", message);
}

fn main() {
    // 後から文字を追加できるStringを作る
    let mut message = String::from("Rust");
    message.push_str("の勉強");
    message.push('!');
    println!("{}", message);

    // 変更しない文字列は &str でも扱える
    let first_word: &str = "Rust";
    println!("最初の言葉: {}", first_word);
}

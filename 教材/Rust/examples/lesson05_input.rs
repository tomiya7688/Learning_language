use std::io;

fn main() {
    // 受け取った文字を保存する場所を用意する
    let mut name = String::new();
    println!("名前を入力してください：");

    // Enterまでに入力された文字を受け取る
    io::stdin()
        .read_line(&mut name)
        .expect("入力を読み取れませんでした");

    // 入力末尾の改行を除いて挨拶する
    println!("こんにちは、{}さん！", name.trim());
}

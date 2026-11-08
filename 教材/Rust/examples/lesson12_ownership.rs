fn main() {
    // Stringの所有権をfirstからsecondへ移す
    let first = String::from("Rust");
    let second = first;
    println!("移動後: {}", second);

    // cloneは文字列の中身を複製する
    let copied = second.clone();
    println!("複製: {}", copied);
}

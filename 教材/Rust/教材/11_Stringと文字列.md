# 11. Stringと文字列

入力した文章に後から文字を付け足したいとき、固定した文字列だけでは困ります。

**この章でできること：** 変更できる文字列へ文章を追加する。

## コードを見る

[配布した `lesson11_strings.rs` の全体](../examples/lesson11_strings.rs#L1-L11)を、VS Codeで開いてください。ソースコードはプログラムの元になる文章です。次のコードは配布ファイルと同じ内容です。

```rust
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
```

## 実行する

[初めに](../初めに.md)で説明したとおり、VS Codeで `教材/Rust` を開き、**ターミナル**（コマンドを入力する画面）へ次の一行を入力して Enter を押してください。

```text
cargo run --example lesson11_strings
```



ターミナルで確認する表示：

```text
Rustの勉強！
最初の言葉: Rust
```

## コードの読み方

`&str` は文字列を借りて読むときによく使う型です。`String` は文字を所有して追加・変更できる型です。`String::from` で `String` を作り、`push_str` で末尾へ文字列を追加します。`len()` はバイト数を返すため、日本語の文字数とは一致しないことがあります。

## 変更して試す

VS Codeで `examples/lesson11_strings.rs` に対応する `lesson11_strings.rs` を開き、次の部分を変更してみましょう。

`message.push_str("の勉強")` を `message.push_str("が楽しい")` に変えて再実行してください。`Rustが楽しい！` と表示されます。

同じ実行コマンドで変化を確かめ、次の章へ進む前に配布版へ戻すと、以後の説明と一致します。

---

[目次に戻る](../目次.md)

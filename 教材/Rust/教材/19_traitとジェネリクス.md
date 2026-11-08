# 19. traitとジェネリクス

本の説明を表示する処理を作ったあと、別の種類の情報でも「説明を表示する」仕組みを使い回したいことがあります。

**この章でできること：** traitでできる操作を決め、ジェネリクスで型に依存しない関数を作る。

## コードを見る

[配布した `lesson19_traits.rs` の全体](../examples/lesson19_traits.rs#L1-L30)を、VS Codeで開いてください。次のコードは配布ファイルと同じ内容です。

```rust
// 説明文を返す型に共通の約束
trait Summary {
    fn summary(&self) -> String;
}

// 本の情報をまとめる
struct Book {
    title: String,
    pages: u32,
}

// 本の説明文を作る
impl Summary for Book {
    fn summary(&self) -> String {
        format!("{}（{}ページ）", self.title, self.pages)
    }
}

// Summaryを実装する型なら受け取れる
fn print_summary<T: Summary>(item: &T) {
    println!("{}", item.summary());
}

fn main() {
    let book = Book {
        title: String::from("Rust入門"),
        pages: 120,
    };
    print_summary(&book);
}
```


## 実行する

[初めに](../初めに.md)の手順でVS Codeから `教材/Rust` フォルダを開き、**表示 → ターミナル** で次のコマンドを入力して Enter キーを押してください。

```text
cargo run --example lesson19_traits
```

ターミナルへ表示される内容：

```text
Rust入門（120ページ）
```


## コードの読み方

`trait`（トレイト）は、その型が備える操作の約束です。`Summary` は要約、`summary()` は要約を作る関数です。`impl Summary for Book` は、本の型 `Book` がその約束を実装することを示します。`<T: Summary>` は、`Summary` を実装したどんな型 `T` でも受け付けるというジェネリクス（型を決め打ちしない書き方）です。

## 変更して試す

VS Codeで `lesson19_traits.rs` を開き、次の部分を変更してみましょう。

`pages: 120` を `pages: 200` に変え、再実行してください。表示されるページ数が200になります。

試した後に元のコードへ戻すと、ほかのページの説明と同じ動作で学習を続けられます。

---

[目次へ戻る](../目次.md)

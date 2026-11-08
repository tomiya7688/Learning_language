# 18. HashMapで名前と値を結び付ける

商品名と在庫数を別々の一覧にすると、順番がずれたときに誤った在庫が表示されます。名前から直接探せるようにしましょう。

**この章でできること：** 商品名を指定し、対応する在庫数を取得する。

## コードを見る

[配布した `lesson18_hashmap.rs` の全体](../examples/lesson18_hashmap.rs#L1-L14)を、VS Codeで開いてください。次のコードは配布ファイルと同じ内容です。

```rust
use std::collections::HashMap;

fn main() {
    // 商品名をキーにして在庫数を保存する
    let mut stock = HashMap::new();
    stock.insert("りんご", 3);
    stock.insert("みかん", 5);

    // 指定した名前の在庫を調べる
    match stock.get("みかん") {
        Some(count) => println!("みかんの在庫: {}個", count),
        None => println!("その商品は登録されていません"),
    }
}
```


## 実行する

[初めに](../初めに.md)の手順でVS Codeから `教材/Rust` フォルダを開き、**表示 → ターミナル** で次のコマンドを入力して Enter キーを押してください。

```text
cargo run --example lesson18_hashmap
```

ターミナルへ表示される内容：

```text
みかんの在庫: 5個
```


## コードの読み方

`HashMap`（ハッシュマップ）は、キー（探すための名前）と値（対応する数）を結び付けます。`insert` で組み合わせを追加し、`get` で探します。存在しないキーを探したときは `None` が返るため、`match` で両方の場合を扱います。

## 変更して試す

VS Codeで `lesson18_hashmap.rs` を開き、次の部分を変更してみましょう。

`stock.get("みかん")` を `stock.get("ぶどう")` に変更して再実行してください。見つからない場合の案内が表示されます。

試した後に元のコードへ戻すと、ほかのページの説明と同じ動作で学習を続けられます。

---

[目次へ戻る](../目次.md)

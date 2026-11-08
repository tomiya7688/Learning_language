# 16. OptionとResult

商品名を探しても見つからないことがあります。また、文字を数字へ変換しようとして失敗することもあります。両方を区別しましょう。

**この章でできること：** 見つからない場合と、変換に失敗した場合を分けて扱う。

## コードを見る

[配布した `lesson16_option_result.rs` の全体](../examples/lesson16_option_result.rs#L1-L24)を、VS Codeで開いてください。次のコードは配布ファイルと同じ内容です。

```rust
// 商品が見つからなければNoneを返す
fn lookup_price(item: &str) -> Option<u32> {
    match item {
        "りんご" => Some(120),
        _ => None,
    }
}

// 入力を数値へ変換し、失敗時は理由を返す
fn parse_count(input: &str) -> Result<u32, std::num::ParseIntError> {
    input.parse::<u32>()
}

fn main() {
    match lookup_price("りんご") {
        Some(price) => println!("りんごは{}円", price),
        None => println!("商品が見つかりません"),
    }

    match parse_count("2") {
        Ok(count) => println!("{}個", count),
        Err(_) => println!("数字ではありません"),
    }
}
```


## 実行する

[初めに](../初めに.md)の手順でVS Codeから `教材/Rust` フォルダを開き、**表示 → ターミナル** で次のコマンドを入力して Enter キーを押してください。

```text
cargo run --example lesson16_option_result
```

ターミナルへ表示される内容：

```text
りんごは120円
2個
```


## コードの読み方

`Option<T>`（任意の値）は、値がある `Some(値)` と無い `None` のどちらかです。`Result<T, E>`（成功・失敗の結果）は、成功した `Ok(値)` と失敗した `Err(原因)` のどちらかです。`match` で両方の可能性を調べると、失敗時に勝手な数字で計算を続けることを避けられます。`u32` は0以上の整数です。

## 変更して試す

VS Codeで `lesson16_option_result.rs` を開き、次の部分を変更してみましょう。

`parse_count("2")` を `parse_count("二")` に変えて実行してください。数値に変換できないため、`数字ではありません` と表示されます。

試した後に元のコードへ戻すと、ほかのページの説明と同じ動作で学習を続けられます。

---

[目次へ戻る](../目次.md)

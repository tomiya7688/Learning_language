# 15. enumとmatch

信号の状態を文字だけで管理すると、存在しない信号の色を誤って入力できてしまいます。使える状態を先に決めましょう。

**この章でできること：** 信号をenumで表し、matchで表示する案内を選ぶ。

## コードを見る

[配布した `lesson15_enum_match.rs` の全体](../examples/lesson15_enum_match.rs#L1-L26)を、VS Codeで開いてください。次のコードは配布ファイルと同じ内容です。

```rust
// 信号が取り得る3つの状態
enum TrafficLight {
    Red,
    Yellow,
    Green,
}

// 信号の状態に合わせて案内を返す
fn instruction(light: &TrafficLight) -> &'static str {
    match light {
        TrafficLight::Red => "止まる",
        TrafficLight::Yellow => "注意する",
        TrafficLight::Green => "進む",
    }
}

fn main() {
    // すべての状態を順番に確かめる
    for light in [
        TrafficLight::Red,
        TrafficLight::Yellow,
        TrafficLight::Green,
    ] {
        println!("{}", instruction(&light));
    }
}
```


## 実行する

[初めに](../初めに.md)の手順でVS Codeから `教材/Rust` フォルダを開き、**表示 → ターミナル** で次のコマンドを入力して Enter キーを押してください。

```text
cargo run --example lesson15_enum_match
```

ターミナルへ表示される内容：

```text
止まる
注意する
進む
```


## コードの読み方

`enum`（列挙型）は、使える状態を名前で決める仕組みです。`TrafficLight`（信号）は `Red`（赤）・`Yellow`（黄）・`Green`（緑）のいずれかになります。`match` は値に応じて処理を選び、ここではすべての状態に対応する文字列を返しています。`&'static str` はこの例の固定した文章への参照型です。

## 変更して試す

VS Codeで `lesson15_enum_match.rs` を開き、次の部分を変更してみましょう。

`TrafficLight::Green => "進む"` の文章を `左右を確認して進む` に変えて再実行してください。緑の案内だけが変更されます。

試した後に元のコードへ戻すと、ほかのページの説明と同じ動作で学習を続けられます。

---

[目次へ戻る](../目次.md)

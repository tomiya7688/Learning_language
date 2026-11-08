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

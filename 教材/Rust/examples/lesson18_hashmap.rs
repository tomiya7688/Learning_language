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

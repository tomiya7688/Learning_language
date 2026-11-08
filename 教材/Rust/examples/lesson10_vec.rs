fn main() {
    // 後から点数を増やせる一覧を作る
    let mut scores = vec![70, 80];
    scores.push(90);

    // 一覧から1個ずつ点数を取り出す
    for score in &scores {
        println!("点数: {}", score);
    }

    // 点数をすべて合計する
    let total: i32 = scores.iter().sum();
    println!("合計: {}", total);
}

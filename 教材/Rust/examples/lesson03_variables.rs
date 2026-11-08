fn main() {
    // score は固定の点数
    let score = 80;
    // bonus は後から増やせる追加点
    let mut bonus = 5;
    bonus += 10;

    println!("合計: {}", score + bonus);
}

fn main() {
    // 元の点数の一覧
    let scores = vec![50, 70, 80, 95];

    // 合格点だけを取り出し、それぞれ5点加算する
    let passed: Vec<i32> = scores
        .into_iter()
        .filter(|point| *point >= 60)
        .map(|point| point + 5)
        .collect();

    println!("{:?}", passed);
}

fn main() {
    // 同じ型の点数を3個まとめる
    let scores = [80, 90, 70];
    println!("最初の点数: {}", scores[0]);
    println!("2番目の点数: {}", scores[1]);

    // 名前と点数を一組にする
    let student = ("あおい", 80);
    let (name, score) = student;
    println!("{}: {}点", name, score);
}

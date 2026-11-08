fn main() {
    // 1から3まで順番に表示する
    for number in 1..=3 {
        println!("for: {}", number);
    }

    // count が2になるまで繰り返す
    let mut count = 0;
    while count < 2 {
        println!("while: {}", count);
        count += 1;
    }
}

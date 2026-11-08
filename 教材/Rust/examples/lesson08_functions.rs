// 2つの整数を受け取り、合計を返す
fn add(left: i32, right: i32) -> i32 {
    left + right
}

fn main() {
    // add関数の戻り値を表示する
    let answer = add(3, 4);
    println!("答え: {}", answer);
}

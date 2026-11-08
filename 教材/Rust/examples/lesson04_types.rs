fn main() {
    // 値の種類を型で表す
    let apples: i32 = 3;
    let price: f64 = 120.5;
    let sold_out: bool = false;
    let grade: char = 'A';
    let item: &str = "りんご";

    println!("りんご: {}個", apples);
    println!("値段: {}円", price);
    println!("売り切れ: {}", sold_out);
    println!("評価: {}", grade);
    println!("商品: {}", item);
}

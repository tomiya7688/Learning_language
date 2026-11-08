// 注文金額が3000円以上なら送料無料
fn is_free_shipping(total: u32) -> bool {
    total >= 3000
}

fn main() {
    println!("送料無料: {}", is_free_shipping(3000));
}

// cargo testのときだけ実行する確認処理
#[cfg(test)]
mod tests {
    use super::is_free_shipping;

    #[test]
    fn free_at_3000_yen() {
        assert!(is_free_shipping(3000));
    }

    #[test]
    fn not_free_at_2999_yen() {
        assert!(!is_free_shipping(2999));
    }
}

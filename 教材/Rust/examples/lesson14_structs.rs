// 生徒1人分の情報をまとめる
struct Student {
    name: String,
    score: u32,
}

// Studentから使える判定処理を定義する
impl Student {
    fn passed(&self) -> bool {
        self.score >= 60
    }
}

fn main() {
    // あおいさんのデータを作る
    let student = Student {
        name: String::from("あおい"),
        score: 75,
    };

    println!("{}の合格判定: {}", student.name, student.passed());
}

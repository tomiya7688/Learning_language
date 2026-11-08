// 説明文を返す型に共通の約束
trait Summary {
    fn summary(&self) -> String;
}

// 本の情報をまとめる
struct Book {
    title: String,
    pages: u32,
}

// 本の説明文を作る
impl Summary for Book {
    fn summary(&self) -> String {
        format!("{}（{}ページ）", self.title, self.pages)
    }
}

// Summaryを実装する型なら受け取れる
fn print_summary<T: Summary>(item: &T) {
    println!("{}", item.summary());
}

fn main() {
    let book = Book {
        title: String::from("Rust入門"),
        pages: 120,
    };
    print_summary(&book);
}

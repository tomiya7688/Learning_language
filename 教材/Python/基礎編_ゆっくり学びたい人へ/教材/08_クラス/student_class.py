# 生徒のクラス（Student）を宣言します。
class Student:
    # 初期設定の関数（__init__）を宣言します。
    def __init__(self, name, math_score, kokugo_score):
        # 受け取った名前（name）を、生徒自身（self）の名前に設定します。
        self.name = name
        # 受け取った数学の点数（math_score）を、生徒自身の数学の点数に設定します。
        self.math_score = math_score
        # 受け取った国語の点数（kokugo_score）を、生徒自身の国語の点数に設定します。
        self.kokugo_score = kokugo_score

    # 生徒の結果を見せる関数（show_result）を宣言します。
    def show_result(self):
        # 生徒自身の名前・数学の点数・国語の点数を、1行にして表示します。
        print(f"{self.name}: 数学 {self.math_score}点、国語 {self.kokugo_score}点")


# 主な処理をする関数（main）を宣言します。
def main():
    # はなこの変数（hanako）を宣言します。
    # 名前「Hanako」、数学80点、国語50点の生徒を代入します。
    hanako = Student(name="Hanako", math_score=80, kokugo_score=50)
    # たろうの変数（taro）を宣言します。
    # 名前「Taro」、数学40点、国語60点の生徒を代入します。
    taro = Student(name="Taro", math_score=40, kokugo_score=60)

    # はなこの結果を見せる関数（hanako.show_result）を実行します。
    hanako.show_result()
    # たろうの結果を見せる関数（taro.show_result）を実行します。
    taro.show_result()


# このファイルを直接実行した場合だけ、main() を実行します。
if __name__ == "__main__":
    # 主な処理をする関数（main）を実行します。
    main()

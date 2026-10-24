# 名前と数学・国語の点数をまとめる Student（生徒）クラスを定義します。
class Student:
    # 生徒データの初期設定をする __init__ 関数を定義します。
    def __init__(self, name, math_score, kokugo_score):
        # name（名前）で受け取った値を、self（設定中の生徒データ）の name（名前）にします。
        self.name = name
        # math_score で受け取った数学の点数を、この生徒の math_score にします。
        self.math_score = math_score
        # kokugo_score で受け取った国語の点数を、この生徒の kokugo_score にします。
        self.kokugo_score = kokugo_score

    # 生徒の結果を表示する show_result 関数を定義します。
    def show_result(self):
        # self.name は生徒自身の名前、self.math_score は数学、self.kokugo_score は国語の点数です。
        # この生徒の名前と2教科の点数を1行にして表示します。
        print(f"{self.name}: 数学 {self.math_score}点、国語 {self.kokugo_score}点")


# 主な処理をする main 関数を定義します。
def main():
    # hanako（はなこ）という変数を、この行で作ります。
    # 名前「Hanako」、数学80点、国語50点の生徒データを作り、hanako に代入します。
    hanako = Student("Hanako", 80, 50)
    # taro（たろう）という変数を、この行で作ります。
    # 名前「Taro」、数学40点、国語60点の生徒データを作り、taro に代入します。
    taro = Student("Taro", 40, 60)

    # hanako（はなこのデータ）の show_result（結果表示）関数を実行します。
    hanako.show_result()
    # taro（たろうのデータ）の show_result（結果表示）関数を実行します。
    taro.show_result()


# このファイルを直接実行した場合だけ、main() を実行します。
if __name__ == "__main__":
    # 主な処理をする main 関数を実行します。
    main()

# Student（生徒）という新しい種類の値を定義します。
class Student:
    # 生徒ひとり分を作るときに呼び出す処理を定義します。
    def __init__(self, name, score):
        # self は、いま作っている生徒ひとり分を表します。
        # name（受け取った生徒の名前）の値を、その生徒の name 属性に結び付けます。
        self.name = name
        # score（受け取った生徒の点数）の値を、その生徒の score 属性に結び付けます。
        self.score = score

    # 生徒の結果を表示する処理を定義します。
    def show_result(self):
        # この生徒の名前と点数をコロンで区切って表示します。
        print(self.name, ":", self.score)


# Student（生徒）から、たろうのインスタンスを作ります。
# student（たろうの生徒データを使うための名前）に、その値を結び付けます。
student = Student("たろう", 80)

# student（たろうの生徒データ）の name（名前）を表示します。
print(student.name)

# student（たろうの生徒データ）の score（点数）を表示します。
print(student.score)

# student（たろうの生徒データ）の show_result（結果表示）を実行します。
student.show_result()

# Student（生徒）から、はなこのインスタンスを作ります。
# student2（はなこの生徒データを使うための名前）に、その値を結び付けます。
student2 = Student("はなこ", 95)

# student2（はなこの生徒データ）の show_result（結果表示）を実行します。
student2.show_result()

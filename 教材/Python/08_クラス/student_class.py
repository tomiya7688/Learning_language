# Student という新しい型を定義します。
class Student:
    # インスタンスを作るときに名前と点数を受け取るメソッドを定義します。
    def __init__(self, name, score):
        # 受け取った name をこのインスタンスの name 属性に代入します。
        self.name = name

        # 受け取った score をこのインスタンスの score 属性に代入します。
        self.score = score

    # name と score を表示するメソッドを定義します。
    def show_result(self):
        # name と score をコロンで区切って表示します。
        print(self.name, ":", self.score)


# Student クラスから、たろうのインスタンスを作ります。
student = Student("たろう", 80)

# student を通じて name 属性を表示します。
print(student.name)

# student を通じて score 属性を表示します。
print(student.score)

# student の show_result() を呼び出します。
student.show_result()

# Student クラスから、はなこのインスタンスを作ります。
student2 = Student("はなこ", 95)

# student2 の show_result() を呼び出します。
student2.show_result()

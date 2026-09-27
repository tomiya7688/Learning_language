# 生徒に関係する値と処理をまとめる Student クラスを作ります。
class Student:
    # 生徒の名前を name に保存します。
    name = "たろう"

    # 生徒の点数を score に保存します。
    score = 80

    # name と score を表示する show_result() を作ります。
    def show_result(self):
        print(self.name, ":", self.score)


# Student クラスから、実際に使う student を1つ作ります。
student = Student()

# student が持っている name を表示します。
print(student.name)

# student が持っている score を表示します。
print(student.score)

# student の show_result() を呼び出します。
student.show_result()

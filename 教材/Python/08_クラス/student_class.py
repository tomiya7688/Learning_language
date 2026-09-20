class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show_result(self):
        print(self.name, ":", self.score)


student1 = Student("たろう", 80)
student2 = Student("さくら", 95)

student1.show_result()
student2.show_result()

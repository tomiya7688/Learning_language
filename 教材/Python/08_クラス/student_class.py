class Student:
    name = "たろう"
    score = 80

    def show_result(self):
        print(self.name, ":", self.score)


student = Student()

print(student.name)
print(student.score)
student.show_result()

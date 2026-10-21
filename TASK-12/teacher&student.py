class Teacher:
    def teach(self):
        print("Teacher teaches students")


class Student(Teacher):
    def study(self):
        print("Student is studying")


s = Student()

s.teach()
s.study()
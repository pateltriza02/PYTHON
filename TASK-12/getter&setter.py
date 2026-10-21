class Student:
    def __init__(self):
        self.__name = ""

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


s = Student()

s.set_name("Triza")

print("Student Name:", s.get_name())
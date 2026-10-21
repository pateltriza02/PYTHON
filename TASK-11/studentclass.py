class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)
        print("Average Marks:", self.calculate_average())                   


student1 = Student("MAHI", [80, 82, 90, 85, 70])
student1.display()      
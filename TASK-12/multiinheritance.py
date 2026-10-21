class Father:
    def father_info(self):
        print("This is Father class")


class Mother:
    def mother_info(self):
        print("This is Mother class")


class Child(Father, Mother):
    def child_info(self):
        print("This is Child class")


c = Child()

c.father_info()
c.mother_info()
c.child_info()
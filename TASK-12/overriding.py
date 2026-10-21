class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog says Woof!")


a = Animal()
a.sound()

d = Dog()
d.sound()
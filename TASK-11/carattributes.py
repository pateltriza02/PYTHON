class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print("Speed after acceleration:", self.speed)

    def brake(self):
        self.speed = max(0, self.speed - 10)
        print("Speed after braking:", self.speed)


car1 = Car("Toyota", "Innova")
print("Brand:", car1.brand)
print("Model:", car1.model)

car1.accelerate()
car1.accelerate()
car1.brake()
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, percentage):
        if 0 <= percentage <= 100:
            discount = self.price * percentage / 100
            self.price -= discount
            print("Discount:", discount)
            print("Final Price:", self.price)
        else:
            print("Invalid discount percentage")


laptop1 = Laptop("HP", 50000)

print("Brand:", laptop1.brand)
print("Original Price:", laptop1.price)

laptop1.apply_discount(10)
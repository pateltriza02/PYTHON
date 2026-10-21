class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(product, "added successfully")

    def list_products(self):
        print("\nAvailable Products:")
        if not self.products:
            print("No products available")
        else:
            for product in self.products:
                print(product)


shop1 = Shop()

n = int(input("How many products do you want to add? "))

for i in range(n):
    product = input("Enter product name: ")
    shop1.add_product(product)

shop1.list_products()

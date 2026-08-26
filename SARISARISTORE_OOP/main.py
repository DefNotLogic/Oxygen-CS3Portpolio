from unicodedata import name

def show_menu():
    print("\n --- MENU --- ")
    print("1. Display all products")
    print("2. Search for a product")
    print("3. Sell a product")
    print("4. Restock a product")
    print("5. Remove a product")
    print("6. Exit")

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def display_info(self):
        print("Product:", self.name)
        print("Price: ₱", self.price)
        print("Quantity:", self.quantity)

    def sell(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity

    def sell(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            print(f"Sold {quantity} item(s).")
            print(f"New quantity: {self.quantity}")
        else:
            print("Not enough stock.")

    def restock(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
        else:
            self.quantity += amount
            print(f"Restocked {amount} item(s).")
            print(f"New quantity: {self.quantity}")

    def remove(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount <= self.quantity:
            self.quantity -= amount
            print(f"Removed {amount} item(s).")
            print(f"New quantity: {self.quantity}")
        else:
            print("Not enough stock to remove that amount.")

    def show_all_products(self):
        if not self.products:
            print("No products available.")
            return
        print("\n --- PRODUCT LIST --- ")
        print(f"{'No.' :< 4}{'Name' :< 25}{'Price' :< 10}{'Quantity' :< 8}")
        print(" -- " * 50)
        for i, p in enumerate(self.products, 1):
            print(f"{i :< 4}{p.name :< 25}{p.price :< 10}{p.quantity :< 8}")

    def search_product(self, name):
        for p in self.products:
            if p.name.lower() == name.lower():
                print(f"Found: {p.name} | Price: ₱{p.price} | Qty: {p.quantity}")
                return
        print(f"Product '{name}' not found.")

product1 = Product("Lucky Me Pancit Canton", 15, 20)
product2 = Product("Coca-Cola", 25, 15)
product3 = Product("SkyFlakes", 10, 30)
product4 = Product("Piattos", 25, 12)
product5 = Product("Sardines", 30, 10)
product6 = Product("Nescafe", 50, 8)
product7 = Product("Chippy", 20, 18)
product8 = Product("Oreo", 35, 25)
product9 = Product("Tang", 40, 14)
product10 = Product("Milo", 15, 50)

product1.display_info()
print(" -- " * 30)
product2.display_info()
print(" -- " * 30)
product3.display_info()
print(" -- " * 30)
product4.display_info()
print(" -- " * 30)
product5.display_info()

print(" --- Before selling --- ")
product1.display_info()

print("\nSell 3 items ... ")
product1.sell(3)

print("\n --- After selling --- ")
product1.display_info()

print(" --- Restocking 10 items")
product1.restock(10)
print(" --- After restocking --- ")
product1.display_info()

def show_menu():
    print("\n --- MENU --- ")
    print("1. Display all products")
    print("2. Search for a product")
    print("3. Sell a product")
    print("4. Restock a product")
    print("5. Remove a product")
    print("6. Exit")

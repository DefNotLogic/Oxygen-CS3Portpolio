
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
        print(f"{'No.':< 4}{'Name':< 25}{'Price':< 10}{'Quantity':< 8}")
        print(" -- " * 50)
        for index, product in enumerate(self.products, start=1):
            print(f"{index:< 4}{product.name:< 25}{product.price:< 10}{product.quantity:< 8}")

        def search_product(self, name):
            for p in self.products:
                if p.name.lower() == name.lower():
                    print(f"Find: {p.name} | Price: ₱{p.price} | Qty: {p.quantity}")
                    return
            print(f"Product '{name}' not found.")

# Create more product objects
product1 = Product("Lucky Me Pancit Canton", 15, 20)
product2 = Product("Coca-Cola", 25, 15)
product3 = Product("SkyFlakes", 10, 30)
product4 = Product("Piattos", 25, 12)
product5 = Product("Sardines", 30, 10)

# Display information of all products
product1.display_info()
print(" -- " * 30)
product2.display_info()
print(" -- " * 30)
product3.display_info()
print(" -- " * 30)
product4.display_info()
print(" -- " * 30)
product5.display_info()

def show_menu():
    print("\n --- MENU --- ")
    print("1. Sell Product")
    print("2. Restock Product")
    print("3. Remove Product")
    print("4. Show All Products")
    print("5. Search Product")
    print("6. Exit")

if __name__ == "__main__":
    products = [product1, product2, product3, product4, product5]

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter the product name to sell: ")
            quantity = int(input("Enter the quantity to sell: "))
            for product in products:
                if product.name.lower() == name.lower():
                    product.sell(quantity)
                    break
            else:
                print(f"Product '{name}' not found.")

        elif choice == "2":
            name = input("Enter the product name to restock: ")
            amount = int(input("Enter the amount to restock: "))
            for product in products:
                if product.name.lower() == name.lower():
                    product.restock(amount)
                    break
            else:
                print(f"Product '{name}' not found.")

        elif choice == "3":
            name = input("Enter the product name to remove: ")
            amount = int(input("Enter the amount to remove: "))
            for product in products:
                if product.name.lower() == name.lower():
                    product.remove(amount)
                    break
            else:
                print(f"Product '{name}' not found.")

        elif choice == "4":
            print("\n --- PRODUCT LIST --- ")
            print(f"{'No.':< 4}{'Name':< 25}{'Price':< 10}{'Quantity':< 8}")
            print(" -- " * 50)
            for index, product in enumerate(products, start=1):
                print(f"{index:< 4}{product.name:< 25}{product.price:< 10}{product.quantity:< 8}")

        elif choice == "5":
            name = input("Enter the product name to search: ")
            for product in products:
                if product.name.lower() == name.lower():
                    print(f"Find: {product.name} | Price: ₱{product.price} | Qty: {product.quantity}")
                    break
            else:
                print(f"Product '{name}' not found.")

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")    
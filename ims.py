# Inventory Management System

# Simple list for users with roles
users = [
    {"username": "admin", "password": "admin123", "role": "Admin"},
    {"username": "user1", "password": "user123", "role": "User"},
]

# Product class for product management
class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __repr__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: {self.price}, Stock: {self.stock_quantity}"

# Initialize product inventory
inventory = []

# Authentication function
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"Welcome, {username}!")
            return user
    print("Invalid credentials.")
    return None

# Admin actions
def add_product():
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    price = float(input("Enter product price: "))
    stock_quantity = int(input("Enter stock quantity: "))

    new_product = Product(product_id, name, category, price, stock_quantity)
    inventory.append(new_product)
    print(f"Product {name} added to inventory.")

def edit_product():
    product_id = input("Enter product ID to edit: ")
    for product in inventory:
        if product.product_id == product_id:
            print(f"Editing product: {product}")
            product.name = input("Enter new product name: ")
            product.category = input("Enter new product category: ")
            product.price = float(input("Enter new product price: "))
            product.stock_quantity = int(input("Enter new stock quantity: "))
            print("Product updated.")
            return
    print("Product not found.")

def delete_product():
    product_id = input("Enter product ID to delete: ")
    global inventory
    inventory = [product for product in inventory if product.product_id != product_id]
    print("Product deleted if it existed.")

# View all products
def view_products():
    if inventory:
        for product in inventory:
            print(product)
    else:
        print("No products in inventory.")

# Stock alert function
def check_stock():
    low_stock_threshold = 5
    for product in inventory:
        if product.stock_quantity < low_stock_threshold:
            print(f"Low stock alert for {product.name}: Only {product.stock_quantity} left.")

# Main function to run the system
def main():
    user = login()
    if not user:
        return

    while True:
        if user["role"] == "Admin":
            print("\nAdmin Menu:")
            print("1. Add Product")
            print("2. Edit Product")
            print("3. Delete Product")
            print("4. View Products")
            print("5. Check Stock Levels")
            print("6. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                add_product()
            elif choice == "2":
                edit_product()
            elif choice == "3":
                delete_product()
            elif choice == "4":
                view_products()
            elif choice == "5":
                check_stock()
            elif choice == "6":
                print("Logging out...")
                break
            else:
                print("Invalid choice.")

        elif user["role"] == "User":
            print("\nUser Menu:")
            print("1. View Products")
            print("2. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                view_products()
            elif choice == "2":
                print("Logging out...")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    main()

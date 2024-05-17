# console.py
from backend import *

def show_menu():
    print("1. Add Product")
    print("2. Sell Product")
    print("3. View Inventory")
    print("4. Generate Report")
    print("5. Exit")

def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    add_product_to_inventory(name, price, quantity)
    print("Product added successfully.")

def sell_product():
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity to sell: "))
    if sell_product(product_id, quantity):
        print("Product sold successfully.")
    else:
        print("Insufficient quantity.")

def view_inventory():
    inventory = get_inventory()
    for product in inventory:
        print(product)

def generate_report():
    report = generate_report()
    print("Timestamp:", report['timestamp'])
    print("Total value of inventory:", report['total_value'])
    print("Inventory:")
    for product in report['inventory']:
        print(product)

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_product()
        elif choice == '2':
            sell_product()
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            generate_report()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()


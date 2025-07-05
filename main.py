from transaction import Transaction

def show_menu():
    """
    Display the main menu options.
    """
    print("\n=== CASHIER MENU ===")
    print("1. Add Item")
    print("2. Update Item Name")
    print("3. Update Item Quantity")
    print("4. Update Item Price")
    print("5. Delete Item")
    print("6. Reset Transaction")
    print("7. Show Order Summary")
    print("8. Calculate Total Price")
    print("0. Exit")

# Instantiate the transaction system
trnsct = Transaction()

# Main program loop
while True:
    show_menu()
    choice = input("Choose a menu option: ")

    try:
        if choice == "1":
            name = input("Item name: ")
            qty = int(input("Quantity: "))
            price = int(input("Price per unit: "))
            trnsct.add_item(name, qty, price)

        elif choice == "2":
            old_name = input("Current item name: ")
            if old_name not in trnsct.items:
                print(f"Item '{old_name}' not found. Please check the name and try again.")
            else:
                new_name = input("New item name: ")
                trnsct.update_item_name(old_name, new_name)
                print(f"Item name updated from '{old_name}' to '{new_name}'.")

        elif choice == "3":
            name = input("Item name: ")
            if name not in trnsct.items:
                print(f"Item '{name}' not found. Please check the name and try again.")
            else:
                qty = int(input("New quantity: "))
                trnsct.update_item_quantity(name, qty)
                print(f"Quantity for '{name}' updated to {qty}.")

        elif choice == "4":
            name = input("Item name: ")
            if name not in trnsct.items:
                print(f"Item '{name}' not found. Please check the name and try again.")
            else:
                price = int(input("New price: "))
                trnsct.update_item_price(name, price)
                print(f"Price for '{name}' updated to Rp{price}.")

        elif choice == "5":
            name = input("Item name to delete: ")
            if name not in trnsct.items:
                print(f"Item '{name}' not found. Please check the name and try again.")
            else:
                trnsct.delete_item(name)
                print(f"Item '{name}' deleted from the cart.")

        elif choice == "6":
            confirm = input("Are you sure you want to reset all items? (y/n): ")
            if confirm.lower() == "y":
                trnsct.reset_transaction()
                print("All items have been removed.")

        elif choice == "7":
            trnsct.check_order()

        elif choice == "8":
            trnsct.calculate_total_price()

        elif choice == "0":
            print("Thank you for using this ca1shier app. Goodbye.")
            break

        else:
            print("Invalid menu option. Please choose a valid number.")

    except ValueError as e:
        # Catch and display validation errors from Transaction methods
        print(f"Error: {str(e)} Please check your input and try again.")

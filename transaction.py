from tabulate import tabulate

class Transaction:
    """
    A class to manage a shopping cart system for a cashier application.

    Attributes:
        items (dict): Stores item names as keys and [quantity, price] as values.
    """

    def __init__(self):
        """Initialize an empty cart."""
        self.items = {}

    def add_item(self, item_name, quantity, price):
        """
        Add a new item to the cart.

        Args:
            item_name (str): Name of the item.
            quantity (int): Number of units.
            price (int): Price per unit.

        Returns:
            dict: The updated cart.
        """
        self.items[item_name] = [quantity, price]
        print(f"Item added: {item_name} x{quantity} @ Rp{price}")
        return self.items

    def update_item_name(self, current_name, new_name):
        """
        Change the name of an existing item.

        Args:
            current_name (str): Current name in the cart.
            new_name (str): New name to replace the current one.

        Raises:
            ValueError: If item is not found.
        """
        if current_name not in self.items:
            raise ValueError("Item not found in the cart.")
        self.items[new_name] = self.items.pop(current_name)

    def update_item_quantity(self, item_name, new_quantity):
        """
        Update the quantity of an item.

        Args:
            item_name (str): Name of the item.
            new_quantity (int): New quantity value.

        Raises:
            ValueError: If item is not found.
        """
        if item_name not in self.items:
            raise ValueError("Item not found in the cart.")
        self.items[item_name][0] = new_quantity

    def update_item_price(self, item_name, new_price):
        """
        Update the unit price of an item.

        Args:
            item_name (str): Name of the item.
            new_price (int): New price value.

        Raises:
            ValueError: If item is not found.
        """
        if item_name not in self.items:
            raise ValueError("Item not found in the cart.")
        self.items[item_name][1] = new_price

    def delete_item(self, item_name):
        """
        Remove an item from the cart.

        Args:
            item_name (str): Name of the item.

        Raises:
            ValueError: If item is not found.
        """
        if item_name not in self.items:
            raise ValueError("Item not found in the cart.")
        del self.items[item_name]

    def reset_transaction(self):
        """
        Clear all items from the cart.
        """
        self.items.clear()
        print("All items have been removed from the cart.")

    def check_order(self):
        """
        Validate and display the cart in a formatted table.

        Raises:
            ValueError: If any item has invalid quantity or price.
        """
        if not self.items:
            print("Your cart is currently empty.")
            return

        rows = []
        for i, (name, (quantity, price)) in enumerate(self.items.items(), start=1):
            if not isinstance(quantity, int) or quantity <= 0:
                raise ValueError(f"Invalid quantity for '{name}'.")
            if not isinstance(price, int) or price <= 0:
                raise ValueError(f"Invalid price for '{name}'.")
            total = quantity * price
            rows.append([i, name, quantity, price, total])

        headers = ["No", "Item", "Quantity", "Unit Price", "Total Price"]
        print("\nPurchase Summary:")
        print(tabulate(rows, headers=headers, tablefmt="grid"))

    def calculate_total_price(self):
        """
        Calculate and display the final price with discounts applied.

        Discount tiers:
            - > 500,000 : 10%
            - > 300,000 : 8%
            - > 200,000 : 5%
            - ≤ 200,000 : 0%

        Returns:
            float: Final amount to be paid after discount.
        """
        print(f"\nCurrent items: {self.items}")
        total_price = sum(qty * price for qty, price in self.items.values())

        # Determine discount based on thresholds
        if total_price > 500_000:
            discount = total_price * 0.10
        elif total_price > 300_000:
            discount = total_price * 0.08
        elif total_price > 200_000:
            discount = total_price * 0.05
        else:
            discount = 0

        final_price = total_price - discount

        # Format numbers into Rupiah format
        formatted_total = f"{total_price:,.0f}".replace(",", ".")
        formatted_discount = f"{discount:,.0f}".replace(",", ".")
        formatted_final = f"{final_price:,.0f}".replace(",", ".")

        print(f"\nTotal Before Discount: Rp {formatted_total}")
        print(f"Discount Applied:      Rp {formatted_discount}")
        print(f"Amount Due:            Rp {formatted_final}")

"""
retail_item.py: holds a retain item data and prints it
By: D. Strickland
9/8/26
"""

__author__ = "Dillon Strickland"

from typing import override

class RetailItem:
    """
    Class to represent a retail item.
    """
    @override
    def __init__(self, upc:int, description:str, price:float, quantity:int):
        self.upc = upc
        self.description = description
        self.price = price
        self.quantity = quantity

    """
    Returns True if another RetailItem UPC is the same as this one.
    """
    @override
    def __eq__(self, other) -> bool:
        if not isinstance(other, RetailItem):
            return NotImplemented

        return self.upc == other.upc

    # Getters
    def get_upc(self) -> int:
        return self.upc

    def get_description(self) -> str:
        return self.description

    def get_price(self) -> float:
        return self.price

    def get_quantity(self) -> int:
        return self.quantity

    # Setters/Mutators
    def set_upc(self, upc:int):
        self.upc = upc

    def set_description(self, description:str):
        self.description = description

    def set_price(self, price:float):
        self.price = price

    def set_quantity(self, quantity:int):
        self.quantity = quantity

"""
Define the main method for the user
"""
def main():
    # Create existing retail items
    apple = RetailItem(10692593, "Produce Gala Apple", 3.59, 2)
    canned_beans = RetailItem(10692594, "Canned Green Beans", 0.99, 3)
    frozen_meat = RetailItem(10692595, "Frozen Beef", 4.39, 1)

    # Put them into a list
    existing_retail_items = [
        apple,
        canned_beans,
        frozen_meat
    ]

    # Print user information and ask for UPC
    print("Enter your Retail Item, and let's see if we have it!")
    user_upc = int(input("Enter UPC\n->"))
    user_retail_item = RetailItem(user_upc, "User's Retail Item", 4.99, 1)

    # Check if UPC already exists
    found:bool = False
    for r in existing_retail_items:
        if (r.__eq__(user_retail_item)):
            print("This item already exists in our inventory!")
            found = True
            break

    # If it doesn't exist, inform the user of success
    if not found:
        print("We're adding that item to our inventory now.")

# Run the main method
if __name__ == "__main__":
    main()
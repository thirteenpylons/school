"""

(1) Build the ItemToPurchase class with the following specifications:

Attributes (3 pts)
item_name (string)
item_price (float)
item_quantity (int)
Default constructor (1 pt)
Initializes item's name = "none", item's price = 0, item's quantity = 0
Method
print_item_cost()

Ex. of print_item_cost() output:

Bottled Water 10 @ $1 = $10
(2) In the main section of your code, prompt the user for two items and 
create two objects of the ItemToPurchase class. (2 pts)

Ex:

Item 1
Enter the item name:
Chocolate Chips
Enter the item price:
3
Enter the item quantity:
1

Item 2
Enter the item name:
Bottled Water
Enter the item price:
1
Enter the item quantity:
10

(3) Add the costs of the two items together and output the total cost. (2 pts)

Ex:

TOTAL COST
Chocolate Chips 1 @ $3 = $3
Bottled Water 10 @ $1 = $10

Total: $13
"""


class ItemToPurchase:
    def __init__(self, item_name: str="none", item_price: float=0.0, item_quantity: int=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    
    def print_item_cost(self):
        """
        Ex. of print_item_cost() output:

        Bottled Water 10 @ $1 = $10
        """
        total_cost = int(self.item_price) * self.item_quantity 
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${total_cost}")



if __name__ == "__main__":
    print("Item 1")
    first_item_name: str = input("Enter the item name:\n")
    first_item_price = float(input("Enter the item price:\n"))
    first_item_quantity = int(input("Enter the item quantity:\n"))
    first_item: ItemToPurchase = ItemToPurchase(first_item_name, first_item_price, first_item_quantity)

    print("\nItem 2")
    second_item_name: str = input("Enter the item name:\n")
    second_item_price = float(input("Enter the item price:\n"))
    second_item_quantity = int(input("Enter the item quantity:\n"))
    second_item: ItemToPurchase = ItemToPurchase(second_item_name, second_item_price, second_item_quantity)

    print("\nTOTAL COST")
    first_item.print_item_cost()
    second_item.print_item_cost()

    total_cost = int((first_item.item_price * first_item.item_quantity) + (second_item.item_price * second_item.item_quantity))
    print(f"\nTotal: ${total_cost}")
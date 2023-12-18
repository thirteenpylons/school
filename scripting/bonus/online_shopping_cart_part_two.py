"""
This program extends the earlier "Online shopping cart" program. (Consider first saving your earlier program).

(1) Extend the ItemToPurchase class to contain a new attribute. (2 pts)

item_description (string) - Set to "none" in default constructor
Implement the following method for the ItemToPurchase class.

print_item_description() - Prints item_description attribute for an ItemToPurchase object. Has an ItemToPurchase parameter.

Ex. of print_item_description() output:

Bottled Water: Deer Park, 12 oz.


(2) Build the ShoppingCart class with the following data attributes and related methods. Note: Some can be method stubs (empty methods) initially, to be completed in later steps.

Parameterized constructor which takes the customer name and date as parameters (2 pts)
Attributes
customer_name (string) - Initialized in default constructor to "none"
current_date (string) - Initialized in default constructor to "January 1, 2016"
cart_items (list)
Methods
add_item()
Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
remove_item()
Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
If item name cannot be found, output this message: Item not found in cart. Nothing removed.
modify_item()
Modifies an item's quantity. Has parameter ItemToPurchase. Does not return anything.
If item can be found (by name) in cart, modify item in cart.
If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
get_num_items_in_cart() (2 pts)
Returns quantity of all items in cart. Has no parameters.
get_cost_of_cart() (2 pts)
Determines and returns the total cost of items in cart. Has no parameters.
print_total()
Outputs total of objects in cart.
If cart is empty, output this message: SHOPPING CART IS EMPTY
print_descriptions()
Outputs each item's description.
Ex. of print_total() output:

John Doe's Shopping Cart - February 1, 2016
Number of Items: 8

Nike Romaleos 2 @ $189 = $378
Chocolate Chips 5 @ $3 = $15
Powerbeats 2 Headphones 1 @ $128 = $128

Total: $521

Ex. of print_descriptions() output:

John Doe's Shopping Cart - February 1, 2016

Item Descriptions
Nike Romaleos: Volt color, Weightlifting shoes
Chocolate Chips: Semi-sweet
Powerbeats 2 Headphones: Bluetooth headphones

(3) In the main section of the code, prompt the user for a customer's name and today's date. Output the name and date. Create an object of type ShoppingCart. (1 pt)

Ex:

Enter customer's name:
John Doe
Enter today's date:
February 1, 2016

Customer name: John Doe
Today's date: February 1, 2016

(4) Implement the print_menu() function to print the following menu of options to manipulate the shopping cart. (1 pt)

Ex:

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit

(5) Implement the execute_menu() function that takes 2 parameters: a character representing the user's choice and a shopping cart. execute_menu() performs the menu options described below, according to the user's choice. (1 pt)


(6) In the main section of the code, call print_menu() and prompt for the user's choice of menu options. Each option is represented by a single character.

If an invalid character is entered, continue to prompt for a valid choice. When a valid option is entered, execute the option by calling execute_menu(). Then, print the menu and prompt for a new option. Continue until the user enters 'q'. Hint: Implement Quit before implementing other options. (1 pt)

Ex:

a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit

Choose an option:

(7) Implement Output shopping cart menu option in execute_menu(). (3 pts)

Ex:

OUTPUT SHOPPING CART
John Doe's Shopping Cart - February 1, 2016
Number of Items: 8

Nike Romaleos 2 @ $189 = $378
Chocolate Chips 5 @ $3 = $15
Powerbeats 2 Headphones 1 @ $128 = $128

Total: $521

(8) Implement Output item's description menu option in execute_menu(). (2 pts)

Ex:

OUTPUT ITEMS' DESCRIPTIONS
John Doe's Shopping Cart - February 1, 2016

Item Descriptions
Nike Romaleos: Volt color, Weightlifting shoes
Chocolate Chips: Semi-sweet
Powerbeats 2 Headphones: Bluetooth headphones

(9) Implement Add item to cart menu option in execute_menu(). (3 pts)

Ex:

ADD ITEM TO CART
Enter the item name:
Nike Romaleos
Enter the item description:
Volt color, Weightlifting shoes
Enter the item price:
189
Enter the item quantity:
2

(10) Implement remove item menu option in execute_menu(). (4 pts)

Ex:

REMOVE ITEM FROM CART
Enter name of item to remove:
Chocolate Chips

(11) Implement Change item quantity menu option in execute_menu(). Hint: Make new ItemToPurchase object before using ModifyItem() method. (5 pts)

Ex:

CHANGE ITEM QUANTITY
Enter the item name:
Nike Romaleos
Enter the new quantity:
3
"""


class ItemToPurchase:
    def __init__(self, item_name: str="none", item_price: float=0.0, item_quantity: int=0, item_description: str="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
        
    def print_item_cost(self):
        """
        Ex. of print_item_cost() output:

        Bottled Water 10 @ $1 = $10
        """
        total_cost = int(self.item_price) * self.item_quantity 
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${total_cost}")
    
    def print_item_description(self) -> None:
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    def __init__(self, customer_name: str="none", current_date: str="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items: list = []
    
    def add_item(self, item_to_purchase: ItemToPurchase) -> None:
        """
        Adds an item to cart_items list. Has parameter ItemToPurchase.
        Does not return anything.
        """
        self.cart_items.append(item_to_purchase)
    
    def remove_item(self, item_name: str) -> None:
        """
        Removes item from cart_items list. Has a string (an item's name) parameter. 
        Does not return anything.

        If item name cannot be found, output this message: 
            Item not found in cart. Nothing removed.
        """
        item_found = False

        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, item_to_purchase: ItemToPurchase) -> None:
        """
        Modifies an item's quantity. Has parameter ItemToPurchase. 
        Does not return anything.

        If item can be found (by name) in cart, modify item in cart.
        If item cannot be found (by name) in cart, 
        output this message: 
            Item not found in cart. Nothing modified.
        """
        for i, item in enumerate(self.cart_items):
            if item.item_name == item_to_purchase.item_name:
                self.cart_items[i] = item_to_purchase
                return
        
        print("Item not found in cart. Nothing modified.")

    def get_num_items(self) -> int:
        """
        Returns quantity of all items in cart. Has no parameters.
        """
        return len(self.cart_items)
    
    def get_cost_of_cart(self) -> float:
        """
        Determines and returns the total cost of items in cart. Has no parameters.
        """
        total_cost = 0.0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self) -> None:
        """
        Outputs total of objects in cart.
        If cart is empty, output this message: SHOPPING CART IS EMPTY

        ex:
        John Doe's Shopping Cart - February 1, 2016
        Number of Items: 8

        Nike Romaleos 2 @ $189 = $378
        Chocolate Chips 5 @ $3 = $15
        Powerbeats 2 Headphones 1 @ $128 = $128

        Total: $521
        """
        print("OUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            total_cost = self.get_cost_of_cart()
            for item in self.cart_items:
                print(f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${item.item_quantity * item.item_price}")
            print(f"\nTotal: ${total_cost}")
        print()

    def print_descriptions(self) -> None:
        """
        Outputs each item's description.

        ex:
        John Doe's Shopping Cart - February 1, 2016

        Item Descriptions
        Nike Romaleos: Volt color, Weightlifting shoes
        Chocolate Chips: Semi-sweet
        Powerbeats 2 Headphones: Bluetooth headphones
        """
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu() -> None:
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print()

def execute_menu(choice, cart: ShoppingCart) -> None:
    if choice == 'a':
        item_name = input("Enter the item name:\n")
        item_description = input("Enter the item description:\n")
        item_price = float(input("Enter the item price:\n"))
        item_quantity = int(input("Enter the item quantity:\n"))
        item_to_add = ItemToPurchase(item_name, item_price, item_quantity, item_description)
        cart.add_item(item_to_add)
    elif choice == 'r':
        item_name = input("Enter name of item to remove:\n")
        cart.remove_item(item_name)
    elif choice == 'c':
        item_name = input("Enter the item name:\n")
        item_quantity = int(input("Enter the new quantity:\n"))
        item_to_modify = ItemToPurchase(item_name, 0, item_quantity)
        cart.modify_item(item_to_modify)
    elif choice == 'i':
        cart.print_descriptions()
    elif choice == 'o':
        cart.print_total()


if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}\n")

    my_cart = ShoppingCart(customer_name, current_date)

    menu_choice = ''
    while menu_choice != 'q':
        print_menu()
        menu_choice = input("Choose an option:\n")
        if menu_choice in ['a', 'r', 'c', 'i', 'o', 'q']:
            execute_menu(menu_choice, my_cart)
        else:
            print("Invalid option. Please try again.")

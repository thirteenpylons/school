"""
Write a program with total change amount as an integer input, 
and output the change using the fewest coins, one coin type per line. 
The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. 
Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

Ex: If the input is:

0 
(or less than 0), the output is:

No change 
Ex: If the input is:

45
the output is:

1 Quarter
2 Dimes 
"""


def calculate_change(change_amount: int) -> str:
    coins = {
        100: ("Dollar", "Dollars"),
        25: ("Quarter", "Quarters"),
        10: ("Dime", "Dimes"),
        5: ("Nickel", "Nickels"),
        1: ("Penny", "Pennies")
    }
    
    output = []

    # Calculate the number of each coin type
    for value, names in coins.items():
        num_coins = change_amount // value
        if num_coins == 1:
            output.append(f"{num_coins} {names[0]}")
        elif num_coins > 1:
            output.append(f"{num_coins} {names[1]}")
        change_amount %= value

    return "\n".join(output)

def main():
    change_amount = int(input())
    
    if change_amount <= 0:
        print("No change")
    else:
        print(calculate_change(change_amount))


if __name__ == "__main__":
    main()

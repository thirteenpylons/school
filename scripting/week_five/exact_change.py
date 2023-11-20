"""
Write a program with total change amount as an integer input that outputs 
the change using the fewest coins, one coin type per line. The coin types 
are dollars, quarters, dimes, nickels, and pennies. 
Use singular and plural coin names as appropriate, like 1 penny vs. 2 pennies.

Ex: If the input is:

0 
or less, the output is:

no change
Ex: If the input is:

45
the output is:

1 quarter
2 dimes 
Your program must define and call the following function. 
The function exact_change() should return num_dollars, num_quarters, 
num_dimes, num_nickels, and num_pennies.
def exact_change(user_total)
"""


def exact_change(user_total: int) -> tuple:
    num_dollars = user_total // 100
    user_total %= 100
    num_quarters = user_total // 25
    user_total %= 25
    num_dimes = user_total // 10
    user_total %= 10
    num_nickels = user_total // 5
    num_pennies = user_total % 5
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies

def main():
    change_amount = int(input())
    if change_amount <= 0:
        print("no change")
    else:
        num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(change_amount)
        
        if num_dollars > 0:
            print(f"{num_dollars} {'dollar' if num_dollars == 1 else 'dollars'}")
        if num_quarters > 0:
            print(f"{num_quarters} {'quarter' if num_quarters == 1 else 'quarters'}")
        if num_dimes > 0:
            print(f"{num_dimes} {'dime' if num_dimes == 1 else 'dimes'}")
        if num_nickels > 0:
            print(f"{num_nickels} {'nickel' if num_nickels == 1 else 'nickels'}")
        if num_pennies > 0:
            print(f"{num_pennies} {'penny' if num_pennies == 1 else 'pennies'}")


if __name__ == "__main__":
    main()

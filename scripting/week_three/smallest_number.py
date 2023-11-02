"""
Write a program whose inputs are three integers, and whose output is the smallest of the three values.

Ex: If the input is:

7
15
3
the output is:

3
"""


def main():
    these_integers: str = input("Enter three integers seperated with spaces:\n")
    split_integers: list[int] = [int(x) for x in these_integers.split()]
    smallest_integer: int = min(split_integers)
    
    print(smallest_integer)


if __name__ == "__main__":
    main()

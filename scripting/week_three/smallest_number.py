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
    split_integers: list[int] = []

    for _ in range(3):
        integer: int = int(input())
        split_integers.append(integer)

    smallest_integer: int = min(split_integers)
    
    print(smallest_integer)

if __name__ == "__main__":
    main()

"""
Write a program whose input is two integers and whose output is
the two integers swapped.

Ex: If the input is:

3
8
the output is:

8 3
Your program must define and call the following function. swap_values() 
returns the two values in swapped order.
def swap_values(user_val1, user_val2)

"""


def swap_values(user_val1: int, user_val2: int) -> (int, int):
    return user_val2, user_val1

def main():
    first_integer = int(input())
    second_integer = int(input())
    first_integer, second_integer = swap_values(first_integer, second_integer)
    print(first_integer, second_integer)

if __name__ == "__main__":
    main()

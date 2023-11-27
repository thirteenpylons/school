"""
Write a program that gets a list of integers from input, and outputs
non-negative integers in ascending order (lowest to highest).

Ex: If the input is:

10 -7 4 39 -6 12 2
the output is:

2 4 10 12 39 
For coding simplicity, follow every output value by a space. Do not end with newline.

"""


def return_positive_sorted(numbers: list) -> str:
    result = sorted([number for number in numbers if number >= 0])
    return ' '.join(str(number) for number in result)
    

def main():
    numbers = list(map(int, input().split()))
    result = return_positive_sorted(numbers)
    print(result, end=' ')


if __name__ == "__main__":
    main()
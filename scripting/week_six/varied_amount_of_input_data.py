"""
Statistics are often calculated with varying amounts of input data. 
Write a program that takes any number of integers as input, 
and outputs the average and max.

Ex: If the input is:

15 20 0 5
the output is:

10 20
"""


def average_and_max(*args):
    rounded_average = round(sum(args) / len(args))
    return rounded_average, max(args)


if __name__ == "__main__":
    numbers = input()
    number_list = [int(num) for num in numbers.split()]
    average, maximum = average_and_max(*number_list)
    print(average, maximum)
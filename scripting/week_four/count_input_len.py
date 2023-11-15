"""
Given a line of text as input, output the number of characters excluding spaces, periods, or commas.

Ex: If the input is:

Listen, Mr. Jones, calm down.
the output is:

21
Note: Account for all characters that aren't spaces, periods, or commas (Ex: "r", "2", "!").

"""


def count_chars(text: str) -> int:
    return sum(1 for char in text if char not in [' ', '.', ','])


if __name__ == "__main__":
    this_string = input()
    result = count_chars(this_string)
    print(result)
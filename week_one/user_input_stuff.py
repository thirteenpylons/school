"""

(1) Prompt the user to input an integer between 32 and 126, a float, a character, and a string,
storing each into separate variables. 
Then, output those four values on a single line separated by a space. (Submit for 2 points).
"""

def display_spaced(this_integer: int, this_float: float, this_character: str, this_string: str) -> str:
    return f"{this_integer} {this_float} {this_character} {this_string}"

def display_spaced_reversed(this_integer: int, this_float: float, this_character: str, this_string: str) -> str:
    return f"{this_string} {this_character} {this_float} {this_integer}"

def convert_character(this_integer: int) -> str:
    return f"{this_integer} converted to a character is {chr(this_integer)}"

def main():
    this_integer = int(input("Enter integer (32 - 126):\n"))
    this_float = float(input("Enter float:\n"))
    this_character = input("Enter character:\n")
    this_string = input("Enter string:\n")
    print(display_spaced(this_integer, this_float, this_character, this_string))
    print(display_spaced_reversed(this_integer, this_float, this_character, this_string))
    print(convert_character(this_integer))


if __name__ == "__main__":
    main()
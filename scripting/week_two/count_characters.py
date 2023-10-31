"""
Write a program whose input is a string which contains a character and a phrase,
and whose output indicates the number of times the character appears in the phrase.

Ex: If the input is:

n Monday
the output is:

1
Ex: If the input is:

z Today is Monday
the output is:

0
Ex: If the input is:

n It's a sunny day
the output is:

2

Case matters.

Ex: If the input is:

n Nobody
the output is:

0
n is different than N.
"""


def count_char_in_str(character: str, target: str) -> int:
    return target.count(character)
    
    
if __name__ == "__main__":
    input_data = input().split(' ', 1)
    user_defined_character = input_data[0]
    user_defined_target = input_data[1]
    print(count_char_in_str(user_defined_character, user_defined_target))
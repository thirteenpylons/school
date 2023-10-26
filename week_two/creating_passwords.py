"""

(1) Prompt the user to enter two words and a number, storing each into separate 
variables. Then, output those three values on a single line separated by a space. 
(Submit for 1 point)

Ex: If the input is:

yellow
Daisy
6
the output after the prompts is:

You entered: yellow Daisy 6
Note: User input is not part of the program output.


(2) Output two passwords using a combination of the user input. 
Format the passwords as shown below. (Submit for 2 points, so 3 points total).

Ex: If the input is:

yellow
Daisy
6
the output after the prompts is:

You entered: yellow Daisy 6

First password: yellow_Daisy
Second password: 6yellow6

(3) Output the length of each password (the number of characters in the strings). 
(Submit for 2 points, so 5 points total).

Ex: If the input is:

yellow
Daisy
6
the output after the prompts is:

You entered: yellow Daisy 6

First password: yellow_Daisy
Second password: 6yellow6

Number of characters in yellow_Daisy: 12
Number of characters in 6yellow6: 8

"""


def generate_password(first_word: str, second_word: str, this_integer: int) -> str:
    return f"First password: {second_word}_{first_word}\nSecond password: {this_integer}{first_word}{this_integer}"

def main():
    first_word = input()
    second_word = input()
    this_integer = int(input())
    print(f"You entered: {first_word} {second_word} {this_integer}")

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


def generate_password(first_word: str, second_word: str, this_integer: int) -> tuple:
    first_password = f"{first_word}_{second_word}"
    second_password = f"{this_integer}{first_word}{this_integer}"
    return first_password, second_password

def main():
    first_word: str = input()
    second_word: str = input()
    this_integer: int = int(input())
    print(f"\nYou entered: {first_word} {second_word} {this_integer}\n")

    first_password, second_password = generate_password(first_word, second_word, this_integer)
    
    print(f"First password: {first_password}")
    print(f"Second password: {second_password}\n")
    print(f"Number of characters in {first_password}: {len(first_password)}")
    print(f"Number of characters in {second_password}: {len(second_password)}")

if __name__ == "__main__":
    main()

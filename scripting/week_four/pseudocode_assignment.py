"""IT 140 Higher/Lower Game Sample Output
Overview
Maria has asked you to create a program that prompts the user to enter the lower bound and the upper
bound. You have decided to write pseudocode to design the program before actually developing the
code. When run, the program should ask the user to guess a number. If the number guessed is lower
than the random number, the program should print out a message like “Nope, too low.” If the number
guessed is higher than the random number, print out a message like “Nope, too high.” If the number
guessed is the same as the random number, print out a message like “You got it!”
Note: The output messages you include in your pseudocode may differ slightly from these samples.
Sample Output
Below is one sample output of the program, with the user input demonstrated by bold font.
Welcome to the higher/lower game, Bella!
Enter the lower bound: 10
Enter the upper bound: 30
Great, now guess a number between 10 and 30: 20
Nope, too low.
Guess another number: 25
Nope, too high.
Guess another number: 23
You got it!
Below is another sample output of your program, with the user input demonstrated by bold font.
Welcome to the higher/lower game, Bella!
Enter the lower bound: 10
Enter the upper bound: 5
The lower bound must be less than the upper bound.
Enter the lower bound: 10
Enter the upper bound: 20
Great, now guess a number between 10 and 20: 25
Nope, too high.
Guess another number: 15
Nope, too low.
Guess another number: 17
You got it!
1
"""
from random import randint

def main():
    # declare min / max
    minimum_integer = int(input("What should the minimum be?: \n"))
    maximum_integer = int(input("What should the maximum be?: \n"))
    
    # declare var with random integer
    random_integer: int = randint(minimum_integer, maximum_integer)
    
    # Initialize user_guessed_integer to None
    user_guessed_integer: int = None

    # ask the user to guess a number and keep asking until they get it right
    while user_guessed_integer != random_integer:
        # ask the user to guess a number.
        user_guessed_integer = int(input(f"Guess a number between {minimum_integer} and {maximum_integer}: \n"))
        
        # If the number guessed is lower than the random number
        if user_guessed_integer < random_integer:
            # the program should print out a message like “Nope, too low.” 
            print("Nope, too low.")
        # If the number guessed is higher than the random number
        elif user_guessed_integer > random_integer:
            # print out a message like “Nope, too high.” 
            print("Nope, too high.")
        # If the number guessed is the same as the random number
        else:
            # print out a message like “You got it!”
            print("You got it!")


if __name__ == "__main__":
    main()

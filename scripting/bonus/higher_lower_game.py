"""
This optional assignment will give you the opportunity to develop 
code based on your designs.

As you develop your code, be sure to follow industry standard best 
practices by using in-line comments to describe the different sections 
of your code and appropriate naming conventions for variables. 
You have been asked to use specific phrases so that you will be able to 
properly test your code in the zyLab.

As a part of this lab, you will need to generate a random number. 
To do this, you have been given starter code that “seeds” the random 
number generator. Seeding the generator will help you to know the 
order in which random numbers will be generated. At the top of the program, 
you have been given the following lines, which “seed” the random number generator.

Do not change these lines:

    import random
    seedVal = int(input(“What seed should be used? ”)
    random.seed(seedVal)
Begin developing your code using the develop mode in zyLabs. 
For the first iteration, write a program that does the following:

Prompts the user to input the lower bound and upper bound. 
You must use the variables lower for the lower bound, and upper for 
the upper bound. Include error checks to ensure that the lower bound 
is less than the upper bound. You must include these exact prompts:
    To ask for the lower bound, prompt “What is the lower bound?”
    To ask for the upper bound, prompt “What is the upper bound?”
Includes the following line of code to generate a random number 
between the lower and upper bounds:
    random.randint(lower, upper)
Prints the generated number. Use this statement to test your program with 
different input values by checking to make sure that the generated number 
is between the upper and lower bounds. Note that this will not be in the 
final version of the game, but for testing we need to 
know the number that was generated.
For the second iteration, remove the print statement that displays 
the generated number, then modify the code so that it does the following:

Prompts the user to guess a number using the exact phrase “What is your guess?”.
 Include error checks to ensure that the user only enters values 
between the lower and upper bound.
Prints an output statement based on the guessed number. 
You must include these exact prompts:
    If the number guessed is lower than the random number, print out, “Nope, too low.”
    If the number guessed is higher than the random number, print, “Nope, too high.”
    If the number guessed is the same as the random number, print, “You got it!”
For the third and final iteration, modify the code to loop 
until the user guesses the number.

Using develop mode, run your code with different sample inputs.

Switch to Submit Mode in the zyLab developer, and click Submit for Grading. 
The autograder will run your code through different test cases. 
If you did not pass all the test cases, check the feedback for errors, 
modify your code, then resubmit. Remember, this is an optional lab and 
is not required. "Submit for Grading" will run your code against test 
cases to give you an idea of whether or not it is working.

**IMPORTANT: You must include *all* possible input values, in order, 
when using Develop mode, because you will not be able to input 
additional numbers when the program is running. For example, 
let's say you wanted to test the game with the following values:

Seed Value: 3 Lower Bound: 1 Upper Bound: 5

You would need to include the following input in the box:

3
1
5
2
5
4
3
1
This would set the seed value as 3, the lower and upper bounds as 1 and 5. 
Then the test would guess the following numbers, in order: 2, 5, 4, 3, 1. 
When the correct number is guessed, the program should end. If you do not 
include all possible values, you may receive errors.
"""
import random
from typing import Tuple


class GuessingGame:
    def __init__(self, seed_value: int):
        random.seed(seed_value)
        self.lower: int = 0
        self.upper: int = 0
        self.random_number: int = 0

    def set_bounds(self) -> None:
        self.lower = self.get_valid_input("What is the lower bound? ")
        self.upper = self.get_valid_input("What is the upper bound? ")

        while self.lower >= self.upper:
            print("Lower bound must be less than upper bound.")
            self.set_bounds()

    def generate_number(self) -> None:
        self.random_number = random.randint(self.lower, self.upper)

    def get_valid_input(self, prompt: str) -> int:
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Please enter a valid integer.")

    def play_game(self) -> None:
        self.set_bounds()
        self.generate_number()

        while True:
            guess = self.get_valid_input("What is your guess? ")
            
            if not (self.lower <= guess <= self.upper):
                print(f"Please guess a number between {self.lower} and {self.upper}.")
                continue
            
            if guess < self.random_number:
                print("Nope, too low.")
            elif guess > self.random_number:
                print("Nope, too high.")
            else:
                print("You got it!")
                break


if __name__ == "__main__":
    seed_value = int(input("What seed should be used? "))
    game = GuessingGame(seed_value)
    game.play_game()

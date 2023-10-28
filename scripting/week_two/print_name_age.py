"""
In PyCharm, write a program that prompts the user for their name and age. 

Your program should then tell the user the year they were born. 
Here is a sample execution of the program with the user input in bold:

What is your name? Amanda
How old are you? 15
"""
from datetime import datetime


def main():
    user_name = input("What is your name?\n")
    user_age = int(input("What is your age?\n"))
    
    print(f"Hello {user_name}! You were born in {datetime.now().year - user_age}")


if __name__ == "__main__":
    main()
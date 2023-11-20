"""
Mad Libs are activities that have a person provide various words, which are 
then used to complete a short story in unexpected (and hopefully funny) ways.

Write a program that takes a string and an integer as input, and outputs a 
sentence using the input values as shown in the example below. The program 
repeats until the input string is quit and disregards the integer input that follows.

Ex: If the input is:

apples 5
shoes 2
quit 0
the output is:

Eating 5 apples a day keeps the doctor away.
Eating 2 shoes a day keeps the doctor away.

"""


def main() -> None:
    while True:
        input_str = input()
        parts = input_str.split()
        noun: str = parts[0]
        number: str = parts[1]

        if noun == 'quit':
            break

        if int(number) > 1 and not noun.endswith('s'):
            noun += 's'

        print(f"Eating {number} {noun} a day keeps the doctor away.")

if __name__ == "__main__":
    main()

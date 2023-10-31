"""
Many documents use a specific format for a person's name. 
Write a program that reads a person's name in the following format:

firstName middleName lastName (in one line)

and outputs the person's name in the following format:

lastName, firstInitial.middleInitial.

Ex: If the input is:

Pat Silly Doe
the output is:

Doe, P.S.
If the input has the following format:

firstName lastName (in one line)

the output is:

lastName, firstInitial.

Ex: If the input is:

Julia Clark
the output is:

Clark, J.

"""


def format_name(full_name: str) -> str:
    names: list = full_name.split()
    name_count: int = len(names)
    
    if name_count == 3:
        first_name, middle_name, last_name = names
        return f"{last_name}, {first_name[0]}.{middle_name[0]}."
    elif name_count == 2:
        first_name, last_name = names
        return f"{last_name}, {first_name[0]}."
    else:
        raise ValueError("Invalid input format")


def main():
    full_name = input()
    try:
        print(format_name(full_name))
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

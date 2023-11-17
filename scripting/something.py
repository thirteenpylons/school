def convert_name(name):
    # Create a dictionary for each alphabet character
    # Each character will be represented by a pattern of '*' characters
    alphabet_patterns = {
        'A': ['  *  ', ' * * ', '*****', '*   *', '*   *'],
        'B': ['**** ', '*   *', '**** ', '*   *', '**** '],
        'C': [' ****', '*    ', '*    ', '*    ', ' ****'],
        'D': ['**** ', '*   *', '*   *', '*   *', '**** '],
        'E': ['*****', '*    ', '**** ', '*    ', '*****'],
        'F': ['*****', '*    ', '**** ', '*    ', '*    '],
        'G': [' ****', '*    ', '*  **', '*   *', ' ****'],
        'H': ['*   *', '*   *', '*****', '*   *', '*   *'],
        'I': ['*****', '  *  ', '  *  ', '  *  ', '*****'],
        'J': ['*****', '   * ', '   * ', '*  * ', ' **  '],
        'K': ['*   *', '*  * ', '***  ', '*  * ', '*   *'],
        'L': ['*    ', '*    ', '*    ', '*    ', '*****'],
        'M': ['*   *', '** **', '* * *', '*   *', '*   *'],
        'N': ['*   *', '**  *', '* * *', '*  **', '*   *'],
        'O': [' *** ', '*   *', '*   *', '*   *', ' *** '],
        'P': ['**** ', '*   *', '**** ', '*    ', '*    '],
        'Q': [' *** ', '*   *', '* * *', '*  * ', ' ** *'],
        'R': ['**** ', '*   *', '**** ', '*  * ', '*   *'],
        'S': [' ****', '*    ', ' *** ', '    *', '**** '],
        'T': ['*****', '  *  ', '  *  ', '  *  ', '  *  '],
        'U': ['*   *', '*   *', '*   *', '*   *', ' *** '],
        'V': ['*   *', '*   *', '*   *', ' * * ', '  *  '],
        'W': ['*   *', '*   *', '* * *', '** **', '*   *'],
        'X': ['*   *', ' * * ', '  *  ', ' * * ', '*   *'],
        'Y': ['*   *', ' * * ', '  *  ', '  *  ', '  *  '],
        'Z': ['*****', '   * ', '  *  ', ' *   ', '*****'],
        ' ': ['     ', '     ', '     ', '     ', '     ']
    }

    # Convert the input name to uppercase
    name = name.upper()

    # Initialize a list to hold the representation of each line
    name_representation = ['' for _ in range(5)]

    # Loop through each character in the name
    for char in name:
        # Check if the character is in the alphabet dictionary
        if char in alphabet_patterns:
            # If it is, loop through each line
            for line in range(5):
                # Append the pattern of the current character to the representation
                name_representation[line] += alphabet_patterns[char][line] + '  '
        else:
            # If the character is not in the dictionary, use a question mark pattern
            for line in range(5):
                name_representation[line] += alphabet_patterns['?'][line] + '  '

    # Join the lines and return the result
    return '\n'.join(name_representation)


if __name__ == "__main__":
    this_string = input("Enter the string to convert: ")
    result = convert_name(this_string)
    print(result)
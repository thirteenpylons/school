"""
Many user-created passwords are simple and easy to guess. 
Write a program that takes a simple password and makes it stronger by 
replacing characters using the key below, and by appending "q*s" to the 
end of the input string.

i becomes !
a becomes @
m becomes M
B becomes 8
o becomes .
Ex: If the input is:

mypassword
the output is:

Myp@ssw.rdq*s
Hint: Python strings are immutable, but support string concatenation. 
Store and build the stronger password in the given password variable.
"""


convert = {
    "i": "!",
    "a": "@",
    "m": "M",
    "B": "8",
    "o": "."
}

def strengthen_password(password: str) -> str:
    letters_in_password = []
    
    for letter in password:
        if letter in convert:
            letters_in_password.append(convert[letter])
        else:
            letters_in_password.append(letter)
    
    strengthened_password = ''.join(letters_in_password) + "q*s"
    return print(strengthened_password)

if __name__ == "__main__":
    word = input()
    strengthen_password(word)
    
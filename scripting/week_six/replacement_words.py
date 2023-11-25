"""
Write a program that replaces words in a sentence. The input begins with word 
replacement pairs (original and replacement). The next line of input is the 
sentence where any word on the original list is replaced.

Ex: If the input is:

automobile car   manufacturer maker   children kids
The automobile manufacturer recommends car seats for children if the 
automobile doesn't already have one.
the output is:

The car maker recommends car seats for kids if the car doesn't already have one. 
You can assume the original words are unique.
"""


def replace_words(words: str, sentence: str) -> str:
    replacements = dict(zip(words[::2], words[1::2]))
    sentence_words = sentence.split()
    replaced_sentence = ' '.join(replacements.get(word, word) for word in sentence_words)
    
    return replaced_sentence


def main():
    words: list = input().split()
    sentence: str = input()
    new_sentence: str = replace_words(words, sentence)

    print(new_sentence)

if __name__ == "__main__":
    main()
"""
Write a program that reads a list of words. Then, the program outputs 
those words and their frequencies.

Ex: If the input is:

hey hi Mark hi mark
the output is:

hey 1
hi 2
Mark 1
hi 2
mark 1
"""


def count_words(sentence: str) -> list:
    word_count = [f"{word} {sentence.count(word)}" for word in sentence.split()]
    return word_count

def main():
    sentence_to_count = input()
    result = count_words(sentence_to_count)
    print("\n".join(result))


if __name__ == "__main__":
    main()
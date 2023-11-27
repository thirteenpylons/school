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


def count_words(words: list) -> list:
    word_count_dict = {}

    for word in words:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1

    word_count_list = [f"{word} {word_count_dict[word]}" for word in words]
    return word_count_list

def main():
    words = input().split()
    result = count_words(words)
    print("\n".join(result))

if __name__ == "__main__":
    main()

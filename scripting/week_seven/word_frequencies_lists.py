"""
Write a program that first reads in the name of an input file and then reads 
the file using the csv.reader() method. The file contains a list of words 
separated by commas. Your program should output the words and their frequencies 
(the number of times each word appears in the file) without any duplicates.

Ex: If the input is:

input1.csv
and the contents of input1.csv are:

hello,cat,man,hey,dog,boy,Hello,man,cat,woman,dog,Cat,hey,boy
the output is:

hello 1
cat 2
man 2
hey 2
dog 2
boy 2
Hello 1
woman 1
Cat 1
Note: There is a newline at the end of the output, and input1.csv 
is available to download.

"""
def read_csv(file_name: str) -> list:
    with open(file_name, 'r') as this_file:
        data = this_file.readline().split(',')
    return data

def count_words(words: list) -> dict:
    counted_words = {}
    for word in words:
        word = word.strip()  # Strip whitespace
        if word in counted_words:
            counted_words[word] += 1
        else:
            counted_words[word] = 1
    return counted_words

def main():
    file_name = input() # read the name of the input file
    words_from_csv = read_csv(file_name)
    result = count_words(words_from_csv)
    for word, count in result.items():
        print(f"{word} {count}")

if __name__ == "__main__":
    main()

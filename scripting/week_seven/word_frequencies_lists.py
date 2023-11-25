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
import csv


def read_csv(file_name: str) -> list:
    """
    Returns the contents read from the CSV file filename as list.

    This function reads the contents of the file filename and returns the contents as
    a 2-dimensional list. Each element of the list is a row, with the first row being
    the header. Cells in each row are all interpreted as strings; it is up to the 
    programmer to interpret this data, since CSV files contain no type information.

    Parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file 
    is a valid CSV file
    """
    with open(file_name) as f:
        wrap = csv.reader(f)
        data = list(wrap)
    return data

def count_words(sentence: list) -> list:
    counted_words = {}
    for top_list in sentence:
        for word in top_list:
            counted_words.update(word += 1)
    return counted_words

def main():
    #file_name = input("Enter the name of the file: ")
    file_name = "./input1.csv"
    list_from_csv: list = read_csv(file_name)
    print(list_from_csv)
    result = count_words(list_from_csv)
    print(result)



if __name__ == "__main__":
    main()

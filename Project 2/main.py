#############################################
# Analysis Alphabet Frequency
# Author : Putu Bayu Baskara - 1808561022
#############################################

# read string.txt
def read_file():
    string_file = open("string.txt", "r")
    # fill string with data input from string.txt
    string = string_file.read()
    return string


# rewrite string.txt for create new data input
def write_file():
    string_file = open("string.txt", "w")
    string = input("Input New String : ")
    string_file.write(string)
    string_file.close


# convert string.txt to lowercase
def conv_lower(string):
    string = string.lower()
    return string


# count alphabet frequency of string.txt
def count_alphabet(string, alphabet):
    # variable for count alphabet frequency
    count = 0
    # looping for every alphabet data of string
    for alphabet1 in string:
        # if alphabet found
        # count + 1
        if alphabet1 == alphabet:
            count += 1
    return count


#  main program
def main():
    print("============================")
    print("1. Change string.txt")
    print("2. Count Alphabet Frequency of string.txt")
    pilih = int(input("Input (1/2) : "))
    print("=================================")

    if pilih == 1:
        if (read_file()):
            print("Current String of string.txt")
            print("---------------------------------")
            # show current data of string.txt
            print(read_file())
            print("---------------------------------")
            # input new string
            write_file()
            print("New String was Saved!")
        else:
            print("Error in read_file()")

    elif pilih == 2:
        print("Current String of string.txt")
        print("---------------------------------")
        # show current data of string.txt
        print(read_file())
        print("---------------------------------")
        print("Alphabet Frecuency")
        print("---------------------------------")
        # variable for saving data from read_file() string.txt
        string = read_file()
        # process saved string to lowercase
        string = conv_lower(string)
        # variable for saving list of alphabet [this list can modified to UPPERCASE, NUMERIC or SYMBOL]
        list_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        # showing count of alphabet frequency
        for alphabet in list_alphabet:
            # if list_alphabet found in string (!=0) variable (string.txt), data will be showed
            # anf if list_alphabet ==0, data will not showed
            if count_alphabet(string, alphabet) != 0:
                print("Frequency of", alphabet, "=",
                      count_alphabet(string, alphabet))
    else:
        print("Not Available!Choose Again")


main()

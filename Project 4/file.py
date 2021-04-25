from hash_sha256 import hash_enum
import sys


def save2txt():
    conf = input("Save Hash to Database [y/n]? ")  # confirm to save
    if conf.lower() in ['y', 'yes']:
        # saving the reference of the standard output
        original_stdout = sys.stdout
        with open('dbhash.txt', 'w') as file:
            sys.stdout = file
            print('CHR                            HASH SHA256')
            print(
                '======================================================================')
            print(hash_enum())
            # reset the standard output
            sys.stdout = original_stdout
        print('Succesfull!')
    elif conf.lower() in ['n', 'no']:
        print('Hash not Saved!')


def readtxt():
    # read hash from dbhash.txt
    string_file = open("dbhash.txt", "r")
    # fill string with data input from dbhash.txt
    string = string_file.read()
    return string

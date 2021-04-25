####################################################################################################
# Find SHA256 hash char enumeration
# Author : KELOMPOK DISKUSI A
# 1808561022 - Putu Bayu Baskara | 1808561048 - Luh Ristiari | 1808561110 - Made Yayang Eka Prananda
####################################################################################################

from hash_sha256 import hash_enum  # import module for hash
from file import save2txt, readtxt  # import module for save and read file


def main():
    print('======================================================================')
    print("1. Start Hashing Enum Char")
    print("2. Show Hashing Database")
    menu = int(input("Choose (1/2) : "))
    print('======================================================================')

    if menu == 1:
        hash_enum()
        save2txt()
    elif menu == 2:
        string = readtxt()
        print(string)
    else:
        print("Not Available!")


main()

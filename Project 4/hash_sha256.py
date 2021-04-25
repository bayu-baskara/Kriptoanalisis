import hashlib


def hash_enum():
    # init for i and j
    i = 1
    j = 1
    unichr = chr  # for pyhton version 3.x

    while i <= 26:
        while j <= 26:
            my_enum = unichr(i+96) + unichr(j+96)
            my_string = my_enum  # def string as enum char
            string_hash = hashlib.sha256(
                my_string.encode()).hexdigest()  # hash string with SHA256
            print(my_enum, "--", string_hash)  # print hash each enum char
            j += 1
        print("----------------------------------------------------------------------")
        j = 1
        i += 1
    # end j
    # end i

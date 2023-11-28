#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        char = ord(str[c])
        if char >= 97 and char <= 122:
            char -= 32
        print("{:c}".format(char), end="")
    print()

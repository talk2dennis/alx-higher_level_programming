#!/usr/bin/python3
for num in range(122, 96, -1):
    char = num
    if num % 2 != 0:
        char = char - 32
    print("{:c}".format(char), end="")
